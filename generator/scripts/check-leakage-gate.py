#!/usr/bin/env python3
"""
check-leakage-gate.py — Verify no public nav leaks to draft/non-public
locale content, and that locale pages carry honesty notices.

Phase 1 updates:
  - English content lives under dist/en-US/ only.
  - Root-level redirect stubs are not checked for English→locale leakage.
  - Only non-en-US locales need Translation status notices.
  - en-US pages must NOT be required to have notices.

Checks:
  1. No en-US page links to other locale dirs (/ar/, /th-TH/, …).
  2. llms.txt and llms-full.txt don't expose locale-specific paths
     (en-US paths are expected/OK).
  3. No factory/internal/private files in dist/.
  4. Non-en-US locale pages have a visible "Translation status" notice.

Usage:
    check-leakage-gate.py [dist_dir]

Exit code 0 = no leakage; 1 = leakage or honesty gap found.
"""

import argparse
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from locales_registry import load_registry, locale_dir_names

REG = load_registry()
ALL_LOCALES = locale_dir_names(REG)
NON_EN_LOCALES = ALL_LOCALES - {"en-US"}


# ── helpers ──────────────────────────────────────────────────────────────────


def _skip_special(segments: list[str]) -> bool:
    """Return True if path segments contain a special tree to skip."""
    for seg in segments:
        if seg == ".well-known":
            return True
        if seg == "agents":
            return True
    return False


# ── Check 1: en-US → other locale links ──────────────────────────────────────


def check_english_to_locale(dist: Path):
    """Check 1: no en-US page links to other locale dirs.

    Walks dist/en-US/**/*.html only. Root redirect stubs are excluded.
    """
    hits = []
    en_root = dist / "en-US"
    if not en_root.is_dir():
        return hits

    for root, _, files in os.walk(en_root):
        parts = os.path.relpath(root, dist).split(os.sep)
        if _skip_special(parts):
            continue
        for name in files:
            if not name.endswith(".html"):
                continue
            html = (Path(root) / name).read_text(encoding="utf-8")
            for m in re.finditer(r'href="(/[^"]*)"', html):
                href = m.group(1)
                first_seg = href.lstrip("/").split("/")[0]
                if first_seg in NON_EN_LOCALES:
                    hits.append((str(Path(root) / name), href))
    return hits


# ── Check 2: llms files ──────────────────────────────────────────────────────


def check_llms_locale_refs(dist: Path):
    """Check 2: llms.txt / llms-full.txt don't reference non-en-US locale paths.

    en-US paths in llms files are OK.
    """
    hits = []
    for txt in ["llms.txt", "llms-full.txt"]:
        path = dist / txt
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        for loc in NON_EN_LOCALES:
            if re.search(rf'/{re.escape(loc)}/', content):
                hits.append((txt, loc))
    return hits


# ── Check 3: factory leak (unchanged logic) ──────────────────────────────────


def check_factory_leak(dist: Path):
    """Check 3: no factory/internal files in dist/."""
    hits = []
    for p in sorted(dist.rglob("*.html")):
        rel = str(p.relative_to(dist))
        lower_rel = rel.lower()
        for pat in ["factory", "campaign", "internal", "secret"]:
            if pat in lower_rel:
                hits.append((rel, pat))
    return hits


# ── Check 4: locale notice (non-en-US only) ──────────────────────────────────


def _looks_translated(html: str) -> bool:
    """Heuristic: main content has substantial non-Latin script.

    Translated pages drop the honesty banner (GOAL Phase 6). Absent notice is
    allowed when body content is no longer English-only fallback.
    """
    m = re.search(r'(?is)<div class="content"[^>]*>(.*)</div>\s*</main>', html)
    body = m.group(1) if m else html
    # Count letters outside Basic Latin / Latin-1 Supplement common range
    non_latin = sum(1 for ch in body if ord(ch) > 0x024F and ch.isalpha())
    return non_latin >= 40


def check_locale_notices(dist: Path):
    """Check 4: fallback locale pages carry 'Translation status' notice.

    en-US pages must NOT be required to have notices.
    Redirect pages are exempt.
    Pages that look translated (non-Latin body prose) may omit the notice.
    """
    missing_by_type = {}
    total_by_type = {}
    translated_ok = 0
    for loc in NON_EN_LOCALES:
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
            is_redirect = (
                'http-equiv="refresh"' in html
                or "http-equiv='refresh'" in html
            )
            if is_redirect:
                continue
            if "translation status" in html.lower():
                continue
            if _looks_translated(html):
                translated_ok += 1
                continue
            missing_by_type[ptype] = missing_by_type.get(ptype, 0) + 1
    return total_by_type, missing_by_type, translated_ok


# ── main ─────────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(description="Leakage gate for dist/")
    parser.add_argument("dist_dir", nargs="?", default="dist")
    args = parser.parse_args()

    dist = Path(args.dist_dir)
    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2

    exit_code = 0

    # Check 1 — en-US → other locale links
    hits = check_english_to_locale(dist)
    print("--- 1. en-US pages → other-locale links ---")
    if hits:
        print(f"  LEAKAGE: {len(hits)} links found")
        for f, h in hits[:5]:
            print(f"    {f}: {h}")
        exit_code = 1
    else:
        print("  CLEAN")

    # Check 2 — llms files
    hits = check_llms_locale_refs(dist)
    print("\n--- 2. llms.txt non-en-US locale path references ---")
    if hits:
        print(f"  LEAKAGE: {hits}")
        exit_code = 1
    else:
        print("  CLEAN")

    # Check 3 — factory/internal files (unchanged)
    hits = check_factory_leak(dist)
    print("\n--- 3. Factory/internal files in dist/ ---")
    if hits:
        print(f"  FOUND: {len(hits)}")
        for f, p in hits[:5]:
            print(f"    {f} (matched: {p})")
        exit_code = 1
    else:
        print("  CLEAN")

    # Check 4 — non-en-US locale notices (translated pages may omit banner)
    total, missing, translated_ok = check_locale_notices(dist)
    print("\n--- 4. Non-en-US locale pages 'Translation status' notice ---")
    for ptype in sorted(total):
        t = total.get(ptype, 0)
        m = missing.get(ptype, 0)
        status = "GAP" if m > 0 else "OK"
        print(f"  {ptype:10s}: {t - m:4d} with notice, {m:4d} without  [{status}]")
    if translated_ok:
        print(f"  translated (no notice, non-Latin body): {translated_ok}")
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
