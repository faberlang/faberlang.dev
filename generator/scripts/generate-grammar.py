#!/usr/bin/env python3
"""
generate-grammar.py — build the Grammar reference page from the Radix EBNF.

The site claims the Grammar page is "the full EBNF". For a long time it was a
28-line stub pointing readers at `radix/EBNF.md` — a file in a closed-source
repository, which nobody outside the project can open. The grammar is one of
the three things the project promises to publish even while the compiler is
closed (see /open-source.html), so it belongs on the site, rendered.

Sources, one per locale, from the sibling radix checkout:

    radix/EBNF.md            the Latin/canonical grammar (en-US page)
    radix/EBNF.<locale>.md   the reader-locale surface of the same grammar

The locale files are complete translations of the same document, not
fallbacks, so each localized Grammar page carries real translated content.

Outputs `src/<locale>/reference/grammar.md`. A locale whose EBNF file is
missing is skipped with a warning rather than falling back to English — a
half-English grammar page is worse than the stub it replaces.

Usage:
    generate-grammar.py [--all-locales] [--locale <name>]...
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
EBNF_DIR = WORKSPACE / "radix"

# Each source file opens with its own one-paragraph lead. On the en-US page
# that lead is replaced: it addresses compiler maintainers ("the active
# compiler implementation is crates/radix") rather than readers looking up
# syntax. Localized pages keep theirs — it is the only in-locale lead that
# exists, and an English replacement is exactly the leakage the honesty gate
# is there to catch.
LEAD_EN = """\
The formal grammar for every Faber production, generated from the compiler's
own specification. This is the authority on whether something is valid syntax;
the [target matrix](/toolchain/target-matrix.html) is the authority on whether
a given target supports it.

Uppercase names in the productions are lexical terminals. Grammar examples are
fragments shown to illustrate a production — they are not standalone programs
and are not expected to compile on their own.
"""

# Repo-relative links point into checkouts the reader does not have. The
# paragraphs carrying them are internal documentation contracts rather than
# grammar, so the paragraph goes rather than just the link.
RELATIVE_LINK = re.compile(r"\]\(\.{1,2}/")


def strip_preamble(lines: list[str]) -> list[str]:
    """Drop the H1 and the internal-facing header block above the grammar.

    Every source file opens with its own title, and the locale files add a
    blockquote addressed to translators ("Latin/source-of-truth grammar
    remains EBNF.md") that is written in English on every locale surface.
    """
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("# ") or line.startswith(">"):
            i += 1
            continue
        break
    return lines[i:]


def drop_lead_paragraph(lines: list[str]) -> list[str]:
    i = 0
    while i < len(lines) and lines[i].strip():
        i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    return lines[i:]


def transform(raw: str, *, drop_lead: bool) -> str:
    lines = strip_preamble(raw.splitlines())
    if drop_lead:
        lines = drop_lead_paragraph(lines)

    out: list[str] = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            # `fab` blocks in the grammar are fragments — bare signatures,
            # loose expressions, declarations without bodies. They are not
            # programs, so they must not be tagged with the language the
            # fence contract validates and compiles.
            if in_fence and line.strip() == "```fab":
                out.append("```text")
                continue
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if RELATIVE_LINK.search(line):
            continue
        out.append(line)

    body = "\n".join(out).strip()
    # Dropping paragraphs and the preamble leaves runs of blank lines and
    # sometimes a leading horizontal rule with nothing above it.
    body = re.sub(r"\n{3,}", "\n\n", body)
    body = re.sub(r"\A---\n+", "", body)
    return body + "\n"


def render_page(body: str, locale: str) -> str:
    head = ["+++"]
    if locale != "en-US":
        head.append('translation_kind = "translated"')
        head.append("")
    head += [
        'title = "Grammar"',
        'section = "reference"',
        "order = 1",
        "sources = [",
        f'  "radix/{"EBNF.md" if locale == "en-US" else f"EBNF.{locale}.md"}",',
        "]",
        "+++",
        "",
    ]
    if locale == "en-US":
        head += [LEAD_EN.rstrip(), ""]
    return "\n".join(head) + "\n" + body


def source_for(locale: str) -> Path:
    return EBNF_DIR / ("EBNF.md" if locale == "en-US" else f"EBNF.{locale}.md")


def locale_names() -> list[str]:
    return sorted(p.name for p in (REPO / "src").iterdir() if p.is_dir())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--all-locales", action="store_true")
    ap.add_argument("--locale", action="append", default=[])
    args = ap.parse_args()

    if args.all_locales:
        locales = locale_names()
    elif args.locale:
        locales = args.locale
    else:
        locales = ["en-US"]

    written = 0
    for locale in locales:
        src = source_for(locale)
        if not src.is_file():
            print(f"  warning: no grammar source for {locale} ({src})", file=sys.stderr)
            continue
        body = transform(src.read_text(encoding="utf-8"), drop_lead=locale == "en-US")
        page = render_page(body, locale)
        out = REPO / "src" / locale / "reference" / "grammar.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        print(f"  grammar: {out.relative_to(REPO)} ({len(page.splitlines())} lines)")
        written += 1

    if not written:
        print("ERROR: no grammar page written", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
