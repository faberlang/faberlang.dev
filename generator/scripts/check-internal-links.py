#!/usr/bin/env python3
"""
check-internal-links.py — Verify internal href targets exist in dist/.

Scans all HTML pages under dist/ (excluding locale dirs by default) for
internal href links and reports any whose target file is missing.

Usage:
    check-internal-links.py [dist_dir] [--include-locales]

Exit code 0 = no broken links; 1 = broken links found.
"""

import argparse
import os
import re
import sys

LOCALE_DIRS = {"ar", "th-TH", "vi", "hi", "zh-Hans", "zh-Hant"}


def collect_html(dist_dir, include_locales):
    """Collect HTML files, optionally excluding locale dirs."""
    files = []
    for root, _, names in os.walk(dist_dir):
        parts = os.path.relpath(root, dist_dir).split(os.sep)
        if not include_locales and len(parts) >= 1 and parts[0] in LOCALE_DIRS:
            continue
        if ".well-known" in root or os.sep + "agents" in root:
            continue
        for name in names:
            if name.endswith(".html"):
                files.append(os.path.join(root, name))
    return sorted(files)


def check_target(dist_dir, href):
    """Return True if the href target exists in dist_dir."""
    path = href.split("?")[0].lstrip("/")
    target = os.path.join(dist_dir, path)

    if os.path.exists(target):
        return True
    # Try directory + index.html
    if os.path.isfile(os.path.join(target, "index.html")):
        return True
    return False


def scan(dist_dir, include_locales):
    """Scan all HTML files for broken internal links."""
    html_files = collect_html(dist_dir, include_locales)
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
    parser.add_argument("--include-locales", action="store_true")
    args = parser.parse_args()

    if not os.path.isdir(args.dist_dir):
        print(f"ERROR: {args.dist_dir} is not a directory", file=sys.stderr)
        return 2

    html_files, total_links, broken = scan(args.dist_dir, args.include_locales)

    print(f"HTML pages scanned: {len(html_files)}")
    print(f"Unique internal links checked: {total_links}")
    print(f"Broken links: {len(broken)}")

    if broken:
        # Report unique missing targets
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
