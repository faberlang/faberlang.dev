#!/usr/bin/env python3
"""Generate tooling/targets.md from radix/EBNF_MATRIX.md.

The matrix is the official measured grammar × target lowerability table
(HIR application lane + MIR systems lane). Do not hand-edit the body.

Usage:
  python3 generator/scripts/generate-target-matrix.py
  python3 generator/scripts/generate-target-matrix.py --matrix /path/to/EBNF_MATRIX.md
  python3 generator/scripts/generate-target-matrix.py --all-locales
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
DEFAULT_MATRIX = WORKSPACE / "radix" / "EBNF_MATRIX.md"
DEFAULT_OUT = REPO / "src" / "en-US" / "tooling" / "targets.md"

# Speculum frontmatter parser is line-oriented: multi-line TOML arrays
# collapse to a bare `[` value. Use a single string source line instead.
FRONTMATTER = """\
+++
title = "Target compatibility"
section = "targets"
order = 2
sources = "radix/EBNF_MATRIX.md · target-capability-matrix.md · faber targets"
+++
"""

INTRO = """\
Faber is one language with many compilation contracts. This page is the
**measured lowerability matrix**: for each corpus term, which targets can
lower it, and at what support level.

Policy verbs (support / erase / warn / reject / defer) and pipeline routing
live on [Codegen targets](/tooling/codegen-targets.html). This page is the
large scannable row list — HIR application-lane targets and MIR systems-lane
targets side by side in the tables below.

Live CLI summary: `faber targets`.
"""

# Honesty banner for non-en locales: the matrix body is measurement glyphs +
# Latin target/term ids, not prose translation work. Leakage gate requires
# either this notice or ≥40 non-ASCII letters in `.content`.
LOCALE_NOTICE = (
    "**Translation status:** target matrix is shared measurement data "
    "(Latin term/target ids and ✓/◐/○/✕ glyphs). Intro prose may still be "
    "English; the tables are the product surface.\n"
)

# Drop radix-internal links that do not resolve on the public site.
_LINK_REWRITE = [
    (
        re.compile(
            r"\[`docs/design/target-capability-matrix\.md`\]"
            r"\(docs/design/target-capability-matrix\.md\)"
        ),
        "[Codegen targets](/tooling/codegen-targets.html)",
    ),
    (
        re.compile(
            r"\[docs/design/target-capability-matrix\.md\]"
            r"\(docs/design/target-capability-matrix\.md\)"
        ),
        "[Codegen targets](/tooling/codegen-targets.html)",
    ),
]


def strip_leading_h1(body: str) -> str:
    lines = body.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and lines[0].strip() == "":
            lines = lines[1:]
    return "\n".join(lines).rstrip() + "\n"


def rewrite_links(body: str) -> str:
    for pattern, repl in _LINK_REWRITE:
        body = pattern.sub(repl, body)
    return body


def drop_regeneration_section(body: str) -> str:
    """Public site does not need the local cargo regenerate recipe."""
    m = re.search(r"\n## Regeneration\n", body)
    if not m:
        return body
    return body[: m.start()].rstrip() + "\n"


def build_page(matrix_text: str, *, locale_notice: bool = False) -> str:
    body = strip_leading_h1(matrix_text)
    body = rewrite_links(body)
    body = drop_regeneration_section(body)
    parts = [FRONTMATTER, ""]
    if locale_notice:
        parts.extend([LOCALE_NOTICE, ""])
    parts.extend([INTRO, "", body])
    return "\n".join(parts) if parts[-1].endswith("\n") else "\n".join(parts) + "\n"


def locale_dirs(src_root: Path) -> list[Path]:
    return sorted(p for p in src_root.iterdir() if p.is_dir())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--matrix",
        type=Path,
        default=DEFAULT_MATRIX,
        help=f"Source matrix markdown (default: {DEFAULT_MATRIX})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUT,
        help=f"Output path for en-US (default: {DEFAULT_OUT})",
    )
    parser.add_argument(
        "--all-locales",
        action="store_true",
        help="Also write the same matrix page into every src/<locale>/tooling/",
    )
    args = parser.parse_args()

    matrix_path: Path = args.matrix
    if not matrix_path.is_file():
        print(f"ERROR: matrix not found: {matrix_path}", file=sys.stderr)
        print(
            "Checkout the radix sibling next to faberlang.dev, or pass --matrix.",
            file=sys.stderr,
        )
        return 1

    matrix_text = matrix_path.read_text(encoding="utf-8")
    page_en = build_page(matrix_text, locale_notice=False)
    page_locale = build_page(matrix_text, locale_notice=True)

    outputs: list[tuple[Path, str]] = [(args.output, page_en)]
    if args.all_locales:
        src_root = REPO / "src"
        for loc in locale_dirs(src_root):
            if loc.name == "en-US":
                continue
            outputs.append((loc / "tooling" / "targets.md", page_locale))

    for out, page in outputs:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        print(f"wrote {out.relative_to(REPO)} ({len(page.splitlines())} lines)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
