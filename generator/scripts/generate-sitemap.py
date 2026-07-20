#!/usr/bin/env python3
"""
generate-sitemap.py — Generate sitemap.xml from dist/ HTML pages.

Includes:
  - portal root https://…/
  - every HTML page under each locale directory in locales.toml
  - skips 404.html and root-level redirect stubs (outside locale dirs)

Usage:
    generate-sitemap.py [dist_dir] [base_url]

Output: <dist_dir>/sitemap.xml
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
from locales_registry import load_registry, locale_dir_names

REG = load_registry()
ALL_LOCALES = sorted(locale_dir_names(REG))


def file_to_loc(file: Path, locale_root: Path, locale: str, base_url: str) -> str | None:
    """Map a file under dist/{locale}/ to an absolute sitemap loc."""
    if file.name == "404.html":
        return None
    rel = file.relative_to(locale_root).as_posix()
    if rel == "index.html":
        return f"{base_url}/{locale}/"
    if rel.endswith("/index.html"):
        dir_part = rel[: -len("/index.html")]
        return f"{base_url}/{locale}/{dir_part}/"
    return f"{base_url}/{locale}/{rel}"


def main() -> int:
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    base_url = (sys.argv[2] if len(sys.argv) > 2 else "https://faberlang.dev").rstrip("/")

    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2

    urls: list[str] = [f"{base_url}/"]

    for locale in ALL_LOCALES:
        locale_root = dist / locale
        if not locale_root.is_dir():
            continue
        for root, _, files in os.walk(locale_root):
            for name in files:
                if not name.endswith(".html"):
                    continue
                path = Path(root) / name
                loc = file_to_loc(path, locale_root, locale, base_url)
                if loc:
                    urls.append(loc)

    # Stable order, portal first, then lexicographic
    portal = f"{base_url}/"
    rest = sorted({u for u in urls if u != portal})
    unique = [portal] + rest

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for u in unique:
        lines.append(f"  <url><loc>{escape(u)}</loc></url>")
    lines.append("</urlset>")

    sitemap = dist / "sitemap.xml"
    sitemap.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {sitemap}: {len(unique)} URLs ({len(ALL_LOCALES)} locales + portal)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
