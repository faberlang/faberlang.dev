#!/usr/bin/env python3
"""
tag-glyph-chips.py — mark glyph-only inline code so the stylesheet can size it.

Faber's structural glyphs (← ↤ → ⇥ ∪ ≡ ∈ · ⊜ §) are drawn small by every
monospace face: the symbol fills one narrow cell, so an inline chip holding
just a glyph is hard to read at the body size. CSS cannot select "a code
element with no letters in it", so this pass adds ``class="glyph"`` to each
plain inline ``<code>`` whose text is one to four non-space characters and
contains no ASCII letter or digit. The stylesheet (``code.glyph``) gives those
chips a larger, bolder, centred face.

Fenced blocks are left alone (everything inside ``<pre>`` is skipped), and a
``<code>`` that already has a class (``kw``, ``typ``, ``lang-…``) is never
touched. Idempotent: a tagged chip no longer matches the plain ``<code>`` form.

Usage:
    tag-glyph-chips.py <dist_dir>
"""

from __future__ import annotations

import html as html_mod
import re
import sys
from pathlib import Path

PRE_RE = re.compile(r"(<pre\b.*?</pre>)", re.S)
CODE_RE = re.compile(r"<code>([^<>]*)</code>")
MAX_CHARS = 4


def is_glyph(text: str) -> bool:
    plain = "".join(html_mod.unescape(text).split())
    return 1 <= len(plain) <= MAX_CHARS and not re.search(r"[A-Za-z0-9]", plain)


def tag(match: re.Match) -> str:
    inner = match.group(1)
    return f'<code class="glyph">{inner}</code>' if is_glyph(inner) else match.group(0)


def process(html: str) -> str:
    parts = PRE_RE.split(html)
    for i in range(0, len(parts), 2):  # even parts are outside any <pre>
        parts[i] = CODE_RE.sub(tag, parts[i])
    return "".join(parts)


def main() -> int:
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2

    pages = chips = 0
    for path in sorted(dist.rglob("*.html")):
        html = path.read_text(encoding="utf-8")
        if "<code>" not in html:
            continue
        before = html.count('<code class="glyph">')
        updated = process(html)
        if updated != html:
            path.write_text(updated, encoding="utf-8")
            pages += 1
            chips += updated.count('<code class="glyph">') - before

    print(f"Glyph chips: {chips} tagged on {pages} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
