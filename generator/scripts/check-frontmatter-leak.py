#!/usr/bin/env python3
"""check-frontmatter-leak.py <dist> — fail if a converter stamp reached rendered code.

`faber convert --stdout` prefixes its output with a TOML frontmatter block
(`+++`, `locale = "xx"`, `+++`). A transcoded code fence must not keep it: it
would show up as stray text inside the rendered code block. Pages that document
frontmatter legitimately contain `+++` lines, so the signature is the exact
three-line locale stamp, not the delimiter.
"""
import html
import re
import sys
from pathlib import Path

STAMP = re.compile(r'(?:^|\n)\+\+\+\nlocale = "[A-Za-z-]+"\n\+\+\+(?:\n|$)')


CODE = re.compile(r"<code[^>]*>(.*?)</code>", re.S)
TAGS = re.compile(r"<[^>]+>")


def leaks(page: Path) -> bool:
    # The highlighter splits `+++` into operator spans, so compare the TEXT of
    # each code block, not its markup.
    text = page.read_text(encoding="utf-8", errors="ignore")
    return any(STAMP.search(html.unescape(TAGS.sub("", block)))
               for block in CODE.findall(text))


def main() -> int:
    dist = Path(sys.argv[1])
    bad = [p for p in sorted(dist.rglob("*.html")) if leaks(p)]
    for p in bad[:10]:
        print(f"  frontmatter stamp in rendered code: {p.relative_to(dist)}", file=sys.stderr)
    print(f"Frontmatter leak gate: {len(bad)} page(s) affected")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
