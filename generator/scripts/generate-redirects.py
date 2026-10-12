#!/usr/bin/env python3
"""
generate-redirects — Generate bare-path HTML redirect stubs.

Walk ``dist/<source_site_locale>/**/*.html`` and write a minimal HTML
meta-refresh stub at ``dist/<rel>`` for every rendered page. Uses directory
URL style (``/en-US/``, not ``/en-US/index.html``).

``dist/index.html`` is owned by the portal and is never overwritten
(skipped). Stubs carry noindex so they do not compete with the real locale
pages.

This is the Python restoration of the native-Faber gate (NSM Wave-2 F1):
radix core-norma N2 retired the I/O kernel modules (`faber:solum`,
`faber:processus`, `faber:consolum`) from script mode, so the staged `.fab`
gate can no longer run. Byte-stable with both the retired
`generate-redirects.py` and the `.fab` conversion.

Usage:
    generate-redirects <dist_dir> <source_site_locale>

Exit contract: 0 on success — also when the source locale directory is
missing (a warning, not a failure) — and 2 on usage errors.
"""

from __future__ import annotations

import argparse
import html as html_mod
from pathlib import Path

BASE_URL = "https://faberlang.dev"

# Template for each redirect stub. Uses directory URL style for index files.
# noindex: thin stubs should not compete with real locale pages.
STUB = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={target_url}">
<link rel="canonical" href="{canonical_url}">
<title>Redirect</title>
</head>
<body><p>Moved to <a href="{target_url}">{target_url}</a>.</p></body>
</html>
"""


def target_url(site_locale: str, rel: str) -> str:
    """Site-absolute target path for a page relative to the locale dir."""
    return f"/{site_locale}/{rel}"


def absolute_url(path: str) -> str:
    if path.startswith("http"):
        return path
    return BASE_URL + path


def main() -> int:
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
        return 0

    written = 0
    skipped = 0

    for html_path in sorted(source_dir.rglob("*.html")):
        rel = html_path.relative_to(source_dir)
        rel_str = str(rel)

        # Phase 2: portal owns / — do not overwrite dist/index.html
        if rel_str == "index.html":
            skipped += 1
            continue

        target = target_url(site_locale, rel_str)
        stub_path = dist_dir / rel

        stub_path.parent.mkdir(parents=True, exist_ok=True)
        encoded_target = html_mod.escape(target, quote=True)
        encoded_canonical = html_mod.escape(absolute_url(target), quote=True)
        stub_path.write_text(
            STUB.format(target_url=encoded_target, canonical_url=encoded_canonical)
        )
        written += 1

    print(f"Generated {written} redirect stubs for {site_locale} → bare paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
