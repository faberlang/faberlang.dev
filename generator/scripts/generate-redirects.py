#!/usr/bin/env python3
"""
generate-redirects.py — Generate bare-path HTML redirect stubs for Phase 1 URL migration.

Walk ``dist/<source_site_locale>/**/*.html`` and write a minimal HTML
meta-refresh stub at ``dist/<rel>`` for every rendered page. Uses directory
URL style (``/en-US/``, not ``/en-US/index.html``).

Usage::

    generate-redirects.py <dist_dir> <source_site_locale>

The source_site_locale is the locale whose pages get bare-path stubs
(typically "en-US" for the Phase 1 landing path).
"""

from __future__ import annotations

import argparse
import html as html_mod
from pathlib import Path

# Template for each redirect stub. Uses directory URL style for index files.
STUB = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={target_url}">
<link rel="canonical" href="{target_url}">
<title>Redirect</title>
</head>
<body><p>Moved to <a href="{target_url}">{target_url}</a>.</p></body>
</html>
"""


def target_url(site_locale: str, rel: str) -> str:
    """Build the canonical target URL from relative path.

    Directory URL style: ``index.html`` → ``/en-US/``.
    All other paths: ``start/install.html`` → ``/en-US/start/install.html``.
    """
    if rel == "index.html":
        return f"/{site_locale}/"
    return f"/{site_locale}/{rel}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dist_dir", type=Path, help="Root of the dist directory")
    parser.add_argument(
        "source_site_locale",
        help="Locale whose rendered pages get bare-path redirect stubs",
    )
    args = parser.parse_args()

    dist_dir: Path = args.dist_dir
    site_locale: str = args.source_site_locale

    source_dir = dist_dir / site_locale
    if not source_dir.is_dir():
        print(f"WARNING: source locale directory not found: {source_dir}")
        return

    written = 0
    skipped = 0

    for html_path in sorted(source_dir.rglob("*.html")):
        # Compute relative path under the source locale dir
        rel = html_path.relative_to(source_dir)
        rel_str = str(rel)
        target = target_url(site_locale, rel_str)
        stub_path = dist_dir / rel

        # Write the redirect stub
        stub_path.parent.mkdir(parents=True, exist_ok=True)
        encoded_target = html_mod.escape(target, quote=True)
        stub_path.write_text(STUB.format(target_url=encoded_target))
        written += 1

    # Also ensure the top-level index.html exists (it would already be
    # written by the loop if en-US/index.html is present, but guard
    # explicitly for clarity / non-en-US caller edge case).
    if site_locale == "en-US":
        top_index = dist_dir / "index.html"
        if not top_index.exists():
            top_index.parent.mkdir(parents=True, exist_ok=True)
            target = "/en-US/"
            encoded_target = html_mod.escape(target, quote=True)
            top_index.write_text(STUB.format(target_url=encoded_target))
            written += 1

    print(f"Generated {written} redirect stubs for {site_locale} → bare paths")


if __name__ == "__main__":
    main()
