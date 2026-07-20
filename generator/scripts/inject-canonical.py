#!/usr/bin/env python3
"""
inject-canonical.py — Ensure <link rel="canonical"> on locale HTML pages.

Self-canonicalizes every page under dist/{locale}/ (all registry locales).
Skips pages that already have a canonical (generator-emitted). Absolute URLs
use the given base_url (default https://faberlang.dev).

Root redirect stubs and special trees (.well-known, agents) are not walked
because they live outside locale directories.

Usage:
    inject-canonical.py [dist_dir] [base_url]
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from locales_registry import load_registry, locale_dir_names

REG = load_registry()
ALL_LOCALES = sorted(locale_dir_names(REG))


def file_to_url(file: Path, locale_root: Path, locale: str, base_url: str) -> str:
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

    injected = 0
    skipped = 0
    missing_locale = 0

    for locale in ALL_LOCALES:
        locale_root = dist / locale
        if not locale_root.is_dir():
            missing_locale += 1
            continue
        for root, dirnames, files in os.walk(locale_root):
            # Skip agent/skill trees if ever nested under a locale
            dirnames[:] = [d for d in dirnames if d not in (".well-known", "agents")]
            for name in files:
                if not name.endswith(".html"):
                    continue
                path = Path(root) / name
                html = path.read_text(encoding="utf-8")
                if 'rel="canonical"' in html:
                    skipped += 1
                    continue
                canonical = file_to_url(path, locale_root, locale, base_url)
                tag = f'<link rel="canonical" href="{canonical}">'
                if "</head>" not in html:
                    print(f"WARN: no </head> in {path}", file=sys.stderr)
                    continue
                path.write_text(html.replace("</head>", f"{tag}</head>", 1), encoding="utf-8")
                injected += 1

    print(
        f"Canonical tags: {injected} injected, {skipped} already present"
        + (f", {missing_locale} locale dirs missing" if missing_locale else "")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
