#!/usr/bin/env python3
"""
matrix-cells.py — Presentation pass over the rendered target matrix pages.

The matrix Markdown is generated from faber/docs/EBNF_MATRIX.md, whose term
cells open with a raw `<a id="term"></a>` anchor. The Markdown renderer
escapes inline HTML, so those anchors show up as literal text. This pass:

  1. turns the escaped anchors back into real, empty anchors (the ids stay
     linkable, nothing is visible); an anchor whose id is empty (glyph terms
     such as `⊜` have none) is dropped rather than emitted as `id=""`;
  2. adds a status class to every cell whose whole text is one legend glyph,
     so the stylesheet can colour it. The glyph stays: colour only reinforces.

Glyph to class follows the page legend:
    ✓ fully supported   -> st-ok
    ◐ partial           -> st-warn
    ✕ not supported     -> st-no
    ○ planned           -> st-defer
    — not measured      -> st-defer

Idempotent: a second run finds nothing left to change.

Usage:
    matrix-cells.py [dist_dir]
"""

import re
import sys
from pathlib import Path

GLYPH_CLASS = {
    "✓": "st-ok",
    "◐": "st-warn",
    "✕": "st-no",
    "○": "st-defer",
    "—": "st-defer",
}

ESCAPED_ANCHOR = re.compile(r"&lt;a id=&quot;([A-Za-z0-9_.-]*)&quot;&gt;&lt;/a&gt;")
GLYPH_CELL = re.compile(r"<td>([✓◐✕○—])</td>")


def process(html: str) -> tuple[str, int, int]:
    html, anchors = ESCAPED_ANCHOR.subn(
        lambda m: f'<a id="{m.group(1)}"></a>' if m.group(1) else "", html
    )
    html, cells = GLYPH_CELL.subn(
        lambda m: f'<td class="{GLYPH_CLASS[m.group(1)]}">{m.group(1)}</td>', html
    )
    return html, anchors, cells


def main() -> int:
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2

    pages = anchors = cells = 0
    for path in sorted(dist.glob("*/toolchain/target-matrix.html")):
        html = path.read_text(encoding="utf-8")
        new_html, a, c = process(html)
        if new_html != html:
            path.write_text(new_html, encoding="utf-8")
            pages += 1
        anchors += a
        cells += c

    print(f"Matrix pages: {pages}, anchors restored: {anchors}, status cells classed: {cells}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
