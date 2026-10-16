#!/usr/bin/env python3
"""
encode-urls.py — percent-encode site URLs that carry spaces or angle brackets.

Corpus pages are named after their term, so a few files have a space or `<>`
in the name (`async fs leget.html`, `modulus<i32>.html`). Written raw into an
`href`, a space is invalid and `<`/`>` are only legal as HTML entities. This
pass rewrites every internal `href` (site-relative or absolute on the site
host), the `og:url` meta and the meta-refresh target so the path carries
`%20`, `%3C` and `%3E`. Display text is never touched, and the file names on
disk stay as they are. Idempotent: an encoded URL no longer matches.

Usage:
    encode-urls.py <dist_dir>
"""

from __future__ import annotations

import html as html_mod
import re
import sys
from pathlib import Path

HOST = "https://faberlang.dev"
HREF_RE = re.compile(r'(<a\b[^>]*?\shref=|<link\b[^>]*?\shref=)"([^"]*)"')
OG_URL_RE = re.compile(r'(<meta property="og:url" content=)"([^"]*)"')
REFRESH_RE = re.compile(r'(<meta http-equiv="refresh" content="0; url=)([^"]*)"')
FIX = {" ": "%20", "<": "%3C", ">": "%3E"}


def encode(value: str) -> str:
    raw = html_mod.unescape(value)
    if not (raw.startswith("/") or raw.startswith(HOST + "/")):
        return value
    cut = len(raw)
    for sep in ("?", "#"):
        at = raw.find(sep)
        if at != -1:
            cut = min(cut, at)
    path, rest = raw[:cut], raw[cut:]
    fixed = "".join(FIX.get(ch, ch) for ch in path)
    if fixed == path:
        return value
    return html_mod.escape(fixed + rest, quote=False)


def process(html: str) -> str:
    html = HREF_RE.sub(lambda m: f'{m.group(1)}"{encode(m.group(2))}"', html)
    html = OG_URL_RE.sub(lambda m: f'{m.group(1)}"{encode(m.group(2))}"', html)
    return REFRESH_RE.sub(lambda m: f'{m.group(1)}{encode(m.group(2))}"', html)


def main() -> int:
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2
    pages = 0
    for path in sorted(dist.rglob("*.html")):
        html = path.read_text(encoding="utf-8")
        out = process(html)
        if out != html:
            path.write_text(out, encoding="utf-8")
            pages += 1
    print(f"encode-urls: {pages} page(s) rewritten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
