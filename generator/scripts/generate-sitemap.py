#!/usr/bin/env python3
"""
generate-sitemap.py — Generate sitemap.xml from dist/ HTML pages.

Phase 1: includes English pages under dist/en-US/ only. Other locale dirs
and root-level redirect stubs are excluded. 404.html is skipped.

Usage:
    generate-sitemap.py [dist_dir] [base_url]

Output: <dist_dir>/sitemap.xml
"""

import os
import sys
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
from locales_registry import load_registry, locale_dir_names

REG = load_registry()
ALL_LOCALES = locale_dir_names(REG)
NON_EN_LOCALES = ALL_LOCALES - {"en-US"}

EN_DIR = "en-US"


def main():
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    base_url = sys.argv[2] if len(sys.argv) > 2 else "https://faberlang.dev"
    base_url = base_url.rstrip("/")

    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2

    en_root = dist / EN_DIR
    if not en_root.is_dir():
        print(f"ERROR: {dist}/en-US/ does not exist", file=sys.stderr)
        return 2

    urls = []
    for root, _, files in os.walk(en_root):
        for name in files:
            if not name.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(root, name), en_root)
            # Skip 404.html
            if name == "404.html":
                continue
            # Normalize: index.html → trailing slash URL
            if name == "index.html":
                dir_part = os.path.dirname(rel).replace(os.sep, "/")
                page_path = f"/{EN_DIR}/{dir_part}" if dir_part else f"/{EN_DIR}/"
            else:
                page_path = f"/{EN_DIR}/{rel.replace(os.sep, '/').replace('.html', '.html')}"
            urls.append(base_url + page_path)

    # Phase 2: include portal root (/) as the first URL
    urls.sort()
    # Deduplicate
    seen = set()
    unique = []
    portal_root = base_url + "/"
    if portal_root not in seen and portal_root not in urls:
        seen.add(portal_root)
        unique.append(portal_root)
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
