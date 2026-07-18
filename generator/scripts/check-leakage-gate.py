#!/usr/bin/env python3
"""
check-leakage-gate.py — Verify no public nav leaks to draft/non-public
locale content, and that locale pages carry honesty notices.

Checks:
  1. No English-authored page links to locale dirs (/ar/, /th-TH/, …).
  2. llms.txt and llms-full.txt don't expose locale-specific paths.
  3. No factory/internal/private files in dist/.
  4. Locale pages have a visible "Translation status" notice (reports gaps).

Usage:
    check-leakage-gate.py [dist_dir]

Exit code 0 = no leakage; 1 = leakage or honesty gap found.
"""

import argparse
import os
import re
import sys
from pathlib import Path

LOCALE_DIRS = ["ar", "th-TH", "vi", "hi", "zh-Hans", "zh-Hant"]


def check_english_to_locale(dist: Path):
    """Check 1: no English page links to locale dirs."""
    hits = []
    for root, _, files in os.walk(dist):
        parts = os.path.relpath(root, dist).split(os.sep)
        if parts[0] in LOCALE_DIRS:
            continue
        if ".well-known" in root or os.sep + "agents" in root:
            continue
        for name in files:
            if not name.endswith(".html"):
                continue
            html = (Path(root) / name).read_text(encoding="utf-8")
            for m in re.finditer(r'href="(/[^"]*)"', html):
                href = m.group(1)
                first_seg = href.lstrip("/").split("/")[0]
                if first_seg in LOCALE_DIRS:
                    hits.append((str(Path(root) / name), href))
    return hits


def check_llms_locale_refs(dist: Path):
    """Check 2: llms.txt / llms-full.txt don't reference locale paths."""
    hits = []
    for txt in ["llms.txt", "llms-full.txt"]:
        path = dist / txt
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        for loc in LOCALE_DIRS:
            if re.search(rf'/{re.escape(loc)}/', content):
                hits.append((txt, loc))
    return hits


def check_factory_leak(dist: Path):
    """Check 3: no factory/internal files in dist/."""
    # Known legitimate corpus terms that match suspicious patterns
    legit_corpus = {"private", "todo", "protected", "public", "class"}
    hits = []
    for p in sorted(dist.rglob("*.html")):
        rel = str(p.relative_to(dist))
        name = p.stem
        # Only flag if the filename itself looks like internal docs
        lower_rel = rel.lower()
        for pat in ["factory", "campaign", "internal", "secret"]:
            if pat in lower_rel:
                hits.append((rel, pat))
    return hits


def check_locale_notices(dist: Path):
    """Check 4: locale pages carry 'Translation status' notice."""
    missing_by_type = {}
    total_by_type = {}
    for loc in LOCALE_DIRS:
        loc_dir = dist / loc
        if not loc_dir.exists():
            continue
        for p in sorted(loc_dir.rglob("*.html")):
            rel = str(p.relative_to(dist))
            if "/corpus/" in rel:
                ptype = "corpus"
            elif "/start/" in rel:
                ptype = "start"
            elif rel == f"{loc}/index.html":
                ptype = "portal"
            else:
                ptype = "other"

            total_by_type[ptype] = total_by_type.get(ptype, 0) + 1
            html = p.read_text(encoding="utf-8")
            # Alias redirect pages use <meta http-equiv="refresh"> and have
            # no content to translate — exempt from notice requirement.
            is_redirect = 'http-equiv="refresh"' in html or 'http-equiv=\'refresh\'' in html
            if not is_redirect and "translation status" not in html.lower():
                missing_by_type[ptype] = missing_by_type.get(ptype, 0) + 1
    return total_by_type, missing_by_type


def main():
    parser = argparse.ArgumentParser(description="Leakage gate for dist/")
    parser.add_argument("dist_dir", nargs="?", default="dist")
    args = parser.parse_args()

    dist = Path(args.dist_dir)
    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2

    exit_code = 0

    # Check 1
    hits = check_english_to_locale(dist)
    print("--- 1. English pages → locale dir links ---")
    if hits:
        print(f"  LEAKAGE: {len(hits)} links found")
        for f, h in hits[:5]:
            print(f"    {f}: {h}")
        exit_code = 1
    else:
        print("  CLEAN")

    # Check 2
    hits = check_llms_locale_refs(dist)
    print("\n--- 2. llms.txt locale path references ---")
    if hits:
        print(f"  LEAKAGE: {hits}")
        exit_code = 1
    else:
        print("  CLEAN")

    # Check 3
    hits = check_factory_leak(dist)
    print("\n--- 3. Factory/internal files in dist/ ---")
    if hits:
        print(f"  FOUND: {len(hits)}")
        for f, p in hits[:5]:
            print(f"    {f} (matched: {p})")
        exit_code = 1
    else:
        print("  CLEAN")

    # Check 4
    total, missing = check_locale_notices(dist)
    print("\n--- 4. Locale pages 'Translation status' notice ---")
    for ptype in sorted(total):
        t = total.get(ptype, 0)
        m = missing.get(ptype, 0)
        status = "GAP" if m > 0 else "OK"
        print(f"  {ptype:10s}: {t - m:4d} with notice, {m:4d} without  [{status}]")
    if any(missing.values()):
        exit_code = 1

    print()
    if exit_code == 0:
        print("RESULT: PASS — no leakage, no honesty gaps")
    else:
        print("RESULT: FAIL — leakage or honesty gap found")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
