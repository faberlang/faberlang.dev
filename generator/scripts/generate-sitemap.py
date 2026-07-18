#!/usr/bin/env python3
"""
generate-sitemap.py — Generate sitemap.xml from dist/ HTML pages.

Includes English pages only (excludes locale dirs: ar, th-TH, vi, hi,
zh-Hans, zh-Hant). Corpus term pages are included for discoverability.

Usage:
    generate-sitemap.py [dist_dir] [base_url]

Output: <dist_dir>/sitemap.xml
"""

import os
import sys
from pathlib import Path
from xml.sax.saxutils import escape

LOCALE_DIRS = {"ar", "th-TH", "vi", "hi", "zh-Hans", "zh-Hant"}


def main():
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    base_url = sys.argv[2] if len(sys.argv) > 2 else "https://faberlang.dev"

    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2

    urls = []
    for root, _, files in os.walk(dist):
        parts = os.path.relpath(root, dist).split(os.sep)
        if parts[0] in LOCALE_DIRS:
            continue
        if ".well-known" in root or os.sep + "agents" in root:
            continue
        for name in files:
            if not name.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(root, name), dist)
            # Normalize: index.html → directory URL
            if name == "404.html":
                continue
            if name == "index.html":
                page_path = "/" + os.path.dirname(rel).replace(os.sep, "/")
                if page_path != "/":
                    page_path += "/"
            else:
                page_path = "/" + rel.replace(os.sep, "/").replace(".html", ".html")
            urls.append(base_url + page_path)

    urls.sort()
    # Deduplicate (index.html → / may collide with root)
    seen = set()
    unique = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            unique.append(u)

    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in unique:
        lines.append(f"  <url><loc>{escape(u)}</loc></url>")
    lines.append("</urlset>")

    sitemap = dist / "sitemap.xml"
    sitemap.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {sitemap}: {len(unique)} URLs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
