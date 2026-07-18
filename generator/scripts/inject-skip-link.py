#!/usr/bin/env python3
"""
inject-skip-link.py — Add accessibility skip-to-content link.

Injects <a class="skip-link"> after <body> and adds id="main-content"
to <main> for keyboard/screen reader navigation.

Usage:
    inject-skip-link.py [dist_dir]
"""

import os
import re
import sys
from pathlib import Path

SKIP_LINK = '<a href="#main-content" class="skip-link">Skip to content</a>'


def main():
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2

    injected = 0
    skipped = 0
    for root, _, files in os.walk(dist):
        for name in files:
            if not name.endswith(".html"):
                continue
            path = Path(root) / name
            html = path.read_text(encoding="utf-8")

            # Skip pages without <main> (alias redirects)
            if "<main>" not in html and '<main id=' not in html:
                skipped += 1
                continue
            # Skip if already has skip-link
            if "skip-link" in html:
                skipped += 1
                continue

            # Add id to <main>
            html = html.replace("<main>", '<main id="main-content">', 1)

            # Inject skip link after <body ...>
            html = re.sub(
                r"(<body[^>]*>)",
                r"\1" + SKIP_LINK,
                html,
                count=1,
            )

            path.write_text(html, encoding="utf-8")
            injected += 1

    print(f"Skip links injected: {injected}, skipped: {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
