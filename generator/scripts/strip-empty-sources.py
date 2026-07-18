#!/usr/bin/env python3
"""
strip-empty-sources.py — Remove empty source-list footers from HTML.

When frontmatter has sources = [], the generator renders <li>[]</li>.
This script strips those empty source-list footers.

Usage:
    strip-empty-sources.py [dist_dir]
"""

import os
import re
import sys
from pathlib import Path

# Match the exact empty-source footer pattern
EMPTY_FOOTER = re.compile(
    r'<footer><div class="source-list"><span class="side-h">Sources</span><ul><li>\[\]</li></ul></div></footer>'
)


def main():
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2

    stripped = 0
    for root, _, files in os.walk(dist):
        for name in files:
            if not name.endswith(".html"):
                continue
            path = Path(root) / name
            html = path.read_text(encoding="utf-8")
            new_html, count = EMPTY_FOOTER.subn("", html)
            if count:
                path.write_text(new_html, encoding="utf-8")
                stripped += count

    print(f"Empty source footers stripped: {stripped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
