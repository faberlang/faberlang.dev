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

One corpus page is named `?..html`. A raw `?` starts a query string, so
`/en-US/corpus/?..html` actually requests `/en-US/corpus/` (and its canonical
pointed there). A `?` whose "query" is itself an `.html` file name (no `=`,
no `&`) is part of the path and becomes `%3F`.

`rel="canonical"` and `og:url` are encoded completely, with the same
`urllib.parse.quote(path, safe="/")` that `generate-sitemap.py` uses, so a
page's canonical is byte-identical to its sitemap `<loc>` (`%21..html`,
`%E2%86%92.html`, not `!..html`, `→.html`).

Usage:
    encode-urls.py <dist_dir>
"""

from __future__ import annotations

import html as html_mod
import re
import sys
from pathlib import Path
from urllib.parse import quote, unquote

HOST = "https://faberlang.dev"
HREF_RE = re.compile(r'(<a\b[^>]*?\shref=|<link\b[^>]*?\shref=)"([^"]*)"')
OG_URL_RE = re.compile(r'(<meta property="og:url" content=)"([^"]*)"')
CANONICAL_RE = re.compile(r'(<link rel="canonical" href=)"([^"]*)"')
REFRESH_RE = re.compile(r'(<meta http-equiv="refresh" content="0; url=)([^"]*)"')
FIX = {" ": "%20", "<": "%3C", ">": "%3E"}


def split_url(raw: str) -> tuple[str, str]:
    """Split a site URL into (path, rest), keeping a file-name `?` in the path."""
    hash_at = raw.find("#")
    before_hash = raw if hash_at == -1 else raw[:hash_at]
    q = before_hash.find("?")
    if q != -1:
        query = before_hash[q + 1:]
        if query.endswith(".html") and "=" not in query and "&" not in query:
            q = -1  # `?` is part of the file name, not a query string
    cut = len(raw) if hash_at == -1 else hash_at
    if q != -1:
        cut = min(cut, q)
    return raw[:cut], raw[cut:]


def encode(value: str) -> str:
    raw = html_mod.unescape(value)
    if not (raw.startswith("/") or raw.startswith(HOST + "/")):
        return value
    path, rest = split_url(raw)
    fixed = "".join(FIX.get(ch, ch) for ch in path)
    fixed = fixed.replace("?", "%3F")
    if fixed == path:
        return value
    return html_mod.escape(fixed + rest, quote=False)


def encode_full(value: str) -> str:
    """Canonical/og:url: percent-encode the whole path exactly like the sitemap."""
    raw = html_mod.unescape(value)
    if raw.startswith(HOST + "/"):
        prefix, raw = HOST, raw[len(HOST):]
    elif raw.startswith("/"):
        prefix = ""
    else:
        return value
    path, rest = split_url(raw)
    fixed = quote(unquote(path), safe="/")
    return html_mod.escape(prefix + fixed + rest, quote=False)


def process(html: str) -> str:
    html = CANONICAL_RE.sub(lambda m: f'{m.group(1)}"{encode_full(m.group(2))}"', html)
    html = HREF_RE.sub(lambda m: f'{m.group(1)}"{encode(m.group(2))}"', html)
    html = OG_URL_RE.sub(lambda m: f'{m.group(1)}"{encode_full(m.group(2))}"', html)
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
