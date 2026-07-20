#!/usr/bin/env python3
"""
inject-canonical.py — Add <link rel="canonical"> to pages missing one.

Phase 1: processes dist/en-US/ tree only. Canonical URL uses /en-US/ prefix.
Root-level redirect stubs and special trees (.well-known, agents) are skipped.

Usage:
    inject-canonical.py [dist_dir] [base_url]
"""

import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from locales_registry import load_registry, locale_dir_names

REG = load_registry()
ALL_LOCALES = locale_dir_names(REG)
NON_EN_LOCALES = ALL_LOCALES - {"en-US"}

EN_DIR = "en-US"


def file_to_url(file: Path, en_root: Path, base_url: str) -> str:
    """Map a file path under en_root to its canonical URL with /en-US/ prefix."""
    rel = str(file.relative_to(en_root))
    if rel == "index.html":
        return f"{base_url}/{EN_DIR}/"
    if rel.endswith("/index.html"):
        return f"{base_url}/{EN_DIR}/{rel[:-10]}/"
    return f"{base_url}/{EN_DIR}/{rel}"


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

    injected = 0
    skipped = 0
    for root, _, files in os.walk(en_root):
        # Skip special trees within en-US/
        parts = os.path.relpath(root, en_root).split(os.sep)
        skip = False
        for seg in parts:
            if seg == ".well-known" or seg == "agents":
                skip = True
                break
        if skip:
            continue
        for name in files:
            if not name.endswith(".html"):
                continue
            path = Path(root) / name
            html = path.read_text(encoding="utf-8")
            if 'rel="canonical"' in html:
                skipped += 1
                continue
            canonical = file_to_url(path, en_root, base_url)
            tag = f'<link rel="canonical" href="{canonical}">'
            html = html.replace("</head>", f"{tag}</head>", 1)
            path.write_text(html, encoding="utf-8")
            injected += 1

    print(f"Canonical tags: {injected} injected, {skipped} already present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
