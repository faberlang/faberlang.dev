#!/usr/bin/env python3
"""
inject-canonical.py — Add <link rel="canonical"> to pages missing one.

Scans dist/ HTML files (excluding locale dirs) and injects a canonical
URL tag into <head> for any page that doesn't already have one.

Usage:
    inject-canonical.py [dist_dir] [base_url]
"""

import os
import re
import sys
from pathlib import Path

LOCALE_DIRS = {"ar", "th-TH", "vi", "hi", "zh-Hans", "zh-Hant"}


def file_to_url(dist: Path, file: Path, base_url: str) -> str:
    """Map a dist file path to its canonical URL."""
    rel = str(file.relative_to(dist))
    if rel == "index.html":
        return f"{base_url}/"
    if rel.endswith("/index.html"):
        return f"{base_url}/{rel[:-10]}/"
    return f"{base_url}/{rel}"


def main():
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    base_url = sys.argv[2] if len(sys.argv) > 2 else "https://faberlang.dev"
    base_url = base_url.rstrip("/")

    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2

    injected = 0
    skipped = 0
    for root, _, files in os.walk(dist):
        parts = os.path.relpath(root, dist).split(os.sep)
        if parts[0] in LOCALE_DIRS:
            continue
        if ".well-known" in root or os.sep + "agents" in root:
            continue
        for name in files:
            if not name.endswith(".html"):
                continue
            path = Path(root) / name
            html = path.read_text(encoding="utf-8")
            if 'rel="canonical"' in html:
                skipped += 1
                continue
            canonical = file_to_url(dist, path, base_url)
            tag = f'<link rel="canonical" href="{canonical}">'
            # Inject before </head>
            html = html.replace("</head>", f"{tag}</head>", 1)
            path.write_text(html, encoding="utf-8")
            injected += 1

    print(f"Canonical tags: {injected} injected, {skipped} already present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
