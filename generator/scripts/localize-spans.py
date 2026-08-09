#!/usr/bin/env python3
"""
localize-spans.py — render inline language terms in the page's reader locale.

Code *fences* have followed the reader locale since the en-US build stopped
being pinned to `la`. Inline spans never did, in any locale, which left pages
arguing with themselves: a table calling a type `numerus` directly above a
code block calling it `int`, or Chinese prose reading
"`numerus` 和 `fractus` 拥有默认位宽".

No new markup is needed to fix that, and CONTENT-PLAN.md § Machine contracts
§4 explains why: the translatable vocabulary is closed, and everything outside
it — glyphs, CLI verbs, compounds, paths — is invariant by design. The
generator already resolves that closed set. `generator/src/span.fab` matches
each inline span against 37 keywords + 13 types and emits `class="kw"` or
`class="typ"`; anything else falls through to a plain `<code>`. The
classification is therefore already sitting in the rendered HTML, in every
locale. This script supplies the step that was never written: look the term up
in the page's reader pack and print the local spelling.

Which makes this a presentation post-process like `highlight-code.py` — it
reads rendered HTML, it is idempotent, and it needs no generator rebuild.

Not translated:

    reference/grammar.html      the productions ARE the canonical grammar
    toolchain/target-matrix.html  the terms are the matrix's row keys
    corpus/                     a term page is *about* its Latin term

    pages marked `translate_spans = false` in frontmatter — prose that
    discusses Latin as Latin. "Latin behavioural words: `functio`, `genus`,
    `si`" must not become "Latin behavioural words: `fn`, `class`, `if`".

Usage:
    localize-spans.py <dist_dir>
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from locales_registry import load_registry  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
PACKS = WORKSPACE / "radix" / "stdlib" / "locale"

# Whole pages whose Latin is the subject rather than the spelling.
SKIP_PAGES = {
    Path("reference/grammar.html"),
    Path("toolchain/target-matrix.html"),
}
SKIP_DIRS = {"corpus"}

SPAN_RE = re.compile(r'<code class="(kw|typ)">([^<]*)</code>')


def term_map(reader: str) -> dict[str, dict[str, str]]:
    """Latin spelling → this pack's spelling, keyed by span class.

    `kw` and `typ` are kept apart because a term can appear in both tables
    with different spellings, and the two are not interchangeable. `nihil` is
    the case that matters: the en pack spells the literal `null` and the type
    `null_ty`. span.fab classifies `nihil` as a keyword, so a merged map that
    let `[types]` win would print `null_ty` in running prose — an internal
    disambiguation token, not an English word.
    """
    pack = PACKS / reader / "pack.toml"
    if not pack.is_file():
        return {}
    with pack.open("rb") as handle:
        data = tomllib.load(handle)
    out: dict[str, dict[str, str]] = {"kw": {}, "typ": {}}
    for cls, section in (("kw", "keywords"), ("typ", "types")):
        for latin, local in (data.get(section) or {}).items():
            local = str(local).strip()
            if local:
                out[cls][latin] = local
    return out


def opted_out(dist: Path, page: Path, locale: str) -> bool:
    """True when the page's Markdown source declares `translate_spans = false`.

    Frontmatter rather than a list in this file: the pages that discuss Latin
    as Latin are authored pages, and the person writing one should be able to
    say so in the page instead of knowing that this script exists.
    """
    rel = page.relative_to(dist / locale)
    src = REPO / "src" / locale / rel.with_suffix(".md")
    if not src.is_file():
        return False
    head = src.read_text(encoding="utf-8").split("+++")
    if len(head) < 3:
        return False
    return "translate_spans = false" in head[1]


def localize_page(page: Path, mapping: dict[str, dict[str, str]]) -> int:
    text = page.read_text(encoding="utf-8")
    swapped = 0

    def replace(match: re.Match) -> str:
        nonlocal swapped
        cls, term = match.group(1), match.group(2)
        local = mapping[cls].get(term)
        if local is None or local == term:
            return match.group(0)
        swapped += 1
        return f'<code class="{cls}">{local}</code>'

    updated = SPAN_RE.sub(replace, text)
    if swapped:
        page.write_text(updated, encoding="utf-8")
    return swapped


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: localize-spans.py <dist_dir>", file=sys.stderr)
        return 1
    dist = Path(sys.argv[1]).resolve()

    if not PACKS.is_dir():
        # dist/ is committed, so a build without the radix sibling leaves the
        # previous, already-localized pages in place rather than reverting
        # them to Latin. Same posture as the diagram and locale-tab caches.
        print(f"  [spans] no reader packs at {PACKS}, spans left as-is")
        return 0

    registry = load_registry()
    total = pages = 0
    for locale, meta in sorted(registry.items()):
        root = dist / locale
        if not root.is_dir():
            continue
        mapping = term_map(meta.get("reader_locale", locale))
        if not any(mapping.values()):
            print(f"  [spans] {locale}: no pack, skipped", file=sys.stderr)
            continue
        for page in sorted(root.rglob("*.html")):
            rel = page.relative_to(root)
            if rel in SKIP_PAGES or (rel.parts and rel.parts[0] in SKIP_DIRS):
                continue
            if opted_out(dist, page, locale):
                continue
            swapped = localize_page(page, mapping)
            if swapped:
                total += swapped
                pages += 1

    print(f"  [spans] {total} inline term(s) localized across {pages} page(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
