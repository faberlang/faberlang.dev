#!/usr/bin/env python3
"""
migrate-ia.py — one-shot information-architecture migration.

Restructures src/<locale>/ from ten shallow sections into five grouped by
what a reader is trying to do:

    Start · Language · Toolchain · Libraries · Reference

Roughly half the old pages were under 300 words, so the tree existed to serve
stubs. This merges those into pages worth opening and demotes their headings
one level so the merged page keeps a sane outline.

Runs across every src/<locale>/ tree identically. Locale frontmatter keys
(translation_kind and friends) are carried through from the first source file
of each merge, and translated prose is concatenated rather than regenerated,
so no translation work is lost.

    python3 generator/scripts/migrate-ia.py [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
SRC = REPO / "src"

# (new path, title, section, order, [sources...])
# A single source is a move; several is a merge with heading demotion.
MERGES: list[tuple[str, str, str, int, list[str]]] = [
    # ── Language ─────────────────────────────────────────────────────────
    ("language/types.md", "Types and values", "language", 2, [
        "syntax/types.md", "syntax/variables.md", "syntax/collections.md",
        "syntax/strings.md", "syntax/nullability.md", "syntax/conversion.md",
    ]),
    ("language/functions.md", "Functions and control flow", "language", 3, [
        "syntax/functions.md", "syntax/control-flow.md", "syntax/generics.md",
    ]),
    ("language/errors.md", "Errors and testing", "language", 4, [
        "syntax/errors.md", "features/testing.md",
    ]),
    ("language/glyphs.md", "Glyphs and Latin", "language", 5, [
        "syntax/glyphs.md", "features/latin-and-glyphs.md",
        "features/canonical-vs-sugar.md",
    ]),
    ("language/reader-locales.md", "Reader locales", "language", 6, [
        "features/reader-locale.md", "ecosystem/reader-locale-packages.md",
    ]),
    ("language/capabilities.md", "Capabilities and frames", "language", 7, [
        "features/frames.md",
    ]),

    # ── Toolchain ────────────────────────────────────────────────────────
    ("toolchain/cli.md", "The faber CLI", "toolchain", 1, [
        "tooling/faber-build-tool.md", "tooling/scripting.md",
    ]),
    ("toolchain/compiling.md", "Compiling and targets", "toolchain", 2, [
        "tooling/codegen-targets.md", "features/compilation-lanes.md",
        "tooling/performance.md",
    ]),
    ("toolchain/packages.md", "Packages with Cista", "toolchain", 3, [
        "tooling/cista-package-manager.md",
    ]),
    ("toolchain/radix.md", "Inside Radix", "toolchain", 4, [
        "tooling/radix-compiler.md", "tooling/radix-architecture.md",
    ]),

    # ── Libraries ────────────────────────────────────────────────────────
    ("libraries/norma.md", "Norma — the standard library", "libraries", 1, [
        "ecosystem/norma.md",
    ]),
    ("libraries/triga.md", "Triga — graphics and geometry", "libraries", 2, [
        "ecosystem/triga.md",
    ]),
    ("libraries/corpus.md", "The language corpus", "libraries", 3, [
        "ecosystem/corpus.md",
    ]),

    # ── Reference ────────────────────────────────────────────────────────
    ("reference/grammar.md", "Grammar", "reference", 1, [
        "references/ebnf.md",
    ]),
    ("reference/design.md", "Design notes", "reference", 3, [
        "features/commandments.md", "references/design-docs.md",
        "history/index.md",
    ]),
    ("reference/repositories.md", "Repositories", "reference", 4, [
        "references/repositories.md",
    ]),

    # ── Absorbed into Start ──────────────────────────────────────────────
    ("start/examples.md", "Examples", "examples", 5, [
        "start/examples.md", "ecosystem/ai-workbench.md",
        "ecosystem/coreutils.md",
    ]),
]

# Generated pages: moved verbatim, never merged. Their producing scripts are
# repointed separately.
GENERATED_MOVES: list[tuple[str, str]] = [
    ("tooling/targets.md", "toolchain/target-matrix.md"),
    ("history/releases.md", "reference/releases.md"),
]

# Section index pages are rewritten by hand after the migration, not merged;
# the old ones are removed here.
DROP: list[str] = [
    "syntax/index.md", "features/index.md", "tooling/index.md",
    "ecosystem/index.md", "references/index.md",
]

FM = re.compile(r"\A\+\+\+\n(.*?)\n\+\+\+\n?", re.S)


def split_front(text: str) -> tuple[str, str]:
    m = FM.match(text)
    return (m.group(1), text[m.end():]) if m else ("", text)


def fm_get(front: str, key: str) -> str | None:
    m = re.search(rf'^{key}\s*=\s*"(.*?)"\s*$', front, re.M)
    return m.group(1) if m else None


def fm_extra_keys(front: str) -> str:
    """Locale-only keys worth carrying through (translation_kind, etc.)."""
    keep = []
    for line in front.split("\n"):
        k = line.split("=")[0].strip()
        if k in ("translation_kind", "translation_status", "reader_locale"):
            keep.append(line.strip())
    return "\n".join(keep)


def collect_sources(front: str) -> list[str]:
    m = re.search(r"^sources\s*=\s*\[(.*?)\]", front, re.S | re.M)
    if not m:
        one = fm_get(front, "sources")
        return [one] if one else []
    return re.findall(r'"(.*?)"', m.group(1))


def demote(body: str) -> str:
    """Push every ATX heading down one level, skipping fenced code."""
    out, fenced = [], False
    for line in body.split("\n"):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        if not fenced and re.match(r"^#{1,5} ", line):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def migrate_locale(root: Path, dry: bool) -> tuple[int, int]:
    written = removed = 0
    consumed: set[Path] = set()

    for new_rel, title, section, order, olds in MERGES:
        parts, sources, extra = [], [], ""
        present = [root / o for o in olds if (root / o).is_file()]
        if not present:
            continue

        multi = len(present) > 1
        for i, p in enumerate(present):
            front, body = split_front(p.read_text(encoding="utf-8"))
            if i == 0:
                extra = fm_extra_keys(front)
            sources.extend(collect_sources(front))
            body = body.strip()
            if multi:
                sub = fm_get(front, "title") or p.stem.replace("-", " ").title()
                parts.append(f"## {sub}\n\n{demote(body)}")
            else:
                parts.append(body)
            consumed.add(p)

        uniq = list(dict.fromkeys(s for s in sources if s))
        src_block = ("sources = [\n"
                     + "".join(f'  "{s}",\n' for s in uniq) + "]"
                     ) if uniq else "sources = []"
        head = "+++\n" + (extra + "\n\n" if extra else "")
        head += (f'title = "{title}"\nsection = "{section}"\n'
                 f"order = {order}\n{src_block}\n+++\n\n")

        out = root / new_rel
        if not dry:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(head + "\n\n".join(parts) + "\n", encoding="utf-8")
        written += 1

    for old, new in GENERATED_MOVES:
        p = root / old
        if p.is_file():
            if not dry:
                (root / new).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(p, root / new)
            consumed.add(p)
            written += 1

    for d in DROP:
        p = root / d
        if p.is_file():
            consumed.add(p)

    for p in consumed:
        # start/examples.md is both a source and a destination
        if p.name == "examples.md" and p.parent.name == "start":
            continue
        if not dry:
            p.unlink()
        removed += 1

    if not dry:
        for d in ("syntax", "features", "tooling", "ecosystem",
                  "references", "history"):
            dd = root / d
            if dd.is_dir() and not any(dd.iterdir()):
                dd.rmdir()

    return written, removed


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    for loc in sorted(p for p in SRC.iterdir() if p.is_dir()):
        w, r = migrate_locale(loc, args.dry_run)
        print(f"{loc.name:9s} wrote {w:2d}  removed {r:2d}")
    if args.dry_run:
        print("\n(dry run — nothing written)")


if __name__ == "__main__":
    main()
