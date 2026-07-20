#!/usr/bin/env python3
"""
check-internal-links.py — Verify internal href targets exist in dist/.

Default scan (Phase 1):
  - Root-level HTML (redirect stubs + any root pages)
  - dist/en-US/** (primary English content)

Non-English locale trees are excluded by default because partial Stage-7
slices only ship start/* + corpus; full chrome still points at untranslated
section paths under that locale. Pass --include-all-locales to scan them.

Usage:
    check-internal-links.py [dist_dir] [--include-all-locales]

Exit code 0 = no broken links; 1 = broken links found.
"""

import argparse
import html
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from locales_registry import load_registry, locale_dir_names

REG = load_registry()
ALL_LOCALES = locale_dir_names(REG)
NON_EN_LOCALES = ALL_LOCALES - {"en-US"}


def collect_html(dist_dir, include_all_locales):
    """Collect HTML files for the link scan."""
    files = []
    for root, _, names in os.walk(dist_dir):
        parts = os.path.relpath(root, dist_dir).split(os.sep)
        first = parts[0]
        if first in NON_EN_LOCALES and not include_all_locales:
            continue
        if ".well-known" in parts or "agents" in parts:
            continue
        for name in names:
            if name.endswith(".html"):
                files.append(os.path.join(root, name))
    return sorted(files)


def check_target(dist_dir, href):
    """Return True if the href target exists in dist_dir."""
    path = html.unescape(href.split("?")[0].lstrip("/"))
    target = os.path.join(dist_dir, path)

    if os.path.exists(target):
        return True
    if os.path.isfile(os.path.join(target, "index.html")):
        return True
    return False


def scan(dist_dir, include_all_locales):
    """Scan HTML files for broken internal links."""
    html_files = collect_html(dist_dir, include_all_locales)
    broken = []
    total_links = 0

    for hf in html_files:
        with open(hf, encoding="utf-8") as fh:
            content = fh.read()
        hrefs = set(re.findall(r'href="(/[^"]*)"', content))
        for href in hrefs:
            if href.startswith(("http", "mailto:", "data:", "#")):
                continue
            total_links += 1
            if not check_target(dist_dir, href):
                broken.append((hf, href))

    return html_files, total_links, broken


def main():
    parser = argparse.ArgumentParser(description="Check internal links in dist/")
    parser.add_argument("dist_dir", nargs="?", default="dist")
    parser.add_argument(
        "--include-all-locales",
        action="store_true",
        help="Also scan non-English locale trees (partial slices may fail)",
    )
    args = parser.parse_args()

    if not os.path.isdir(args.dist_dir):
        print(f"ERROR: {args.dist_dir} is not a directory", file=sys.stderr)
        return 2

    html_files, total_links, broken = scan(args.dist_dir, args.include_all_locales)

    print(f"HTML pages scanned: {len(html_files)}")
    print(f"Unique internal links checked: {total_links}")
    print(f"Broken links: {len(broken)}")

    if broken:
        missing = {}
        for hf, href in broken:
            missing.setdefault(href, []).append(hf)
        print(f"\nUnique missing targets: {len(missing)}")
        for href in sorted(missing):
            refs = missing[href]
            sample = refs[0].replace(args.dist_dir + "/", "")
            print(f"  {href}  ({len(refs)} ref(s), e.g. {sample})")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
