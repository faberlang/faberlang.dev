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
from urllib.parse import unquote

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
    # Unescape first so entity-encoded characters (e.g. &#x27; for ') are
    # not split by the literal '#' inside the entity.
    path = html.unescape(href).split("?")[0].split("#")[0].lstrip("/")
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


# Agent surfaces are plain text and Markdown, so the HTML link scan never sees
# them. They cite absolute https://faberlang.dev/... URLs, and they went a whole
# information-architecture generation pointing at retired sections before anyone
# noticed — every URL still "worked", via a redirect stub. Both halves matter:
# a broken URL is a bug, and a URL that only resolves through a stub is a
# citation of an address the site no longer considers canonical.
AGENT_SURFACES = (
    "llms.txt",
    "llms-full.txt",
    "agents/index.md",
    ".well-known/agent-skills/index.json",
)
AGENT_SURFACE_GLOBS = (".well-known/agent-skills/*/SKILL.md",)

# Placeholder URLs that teach a shape rather than naming a page.
AGENT_URL_PLACEHOLDER = re.compile(r"[<{]")

# Written after the gates run, so it is legitimately absent at check time.
AGENT_URL_DEFERRED = {"/sitemap.xml"}

SITE = "https://faberlang.dev"


def agent_surface_files(dist_dir):
    root = Path(dist_dir)
    files = [root / name for name in AGENT_SURFACES]
    for pattern in AGENT_SURFACE_GLOBS:
        files.extend(sorted(root.glob(pattern)))
    return [f for f in files if f.is_file()]


def resolve_site_path(dist_dir, path):
    path = path.split("#")[0].split("?")[0]
    if path in ("", "/") or path in AGENT_URL_DEFERRED:
        return "ok"
    # Corpus terms include glyphs and spaces, so their URLs are percent-encoded.
    # Compare against the filenames on disk, which are not.
    path = unquote(path)
    target = Path(dist_dir) / path.lstrip("/")
    if target.is_dir():
        target = target / "index.html"
    elif not target.exists() and (target.parent / (target.name + "/index.html")).is_file():
        target = target.parent / (target.name + "/index.html")
    if not target.is_file():
        return "missing"
    if target.suffix == ".html":
        head = target.read_text(encoding="utf-8", errors="ignore")[:600]
        if 'http-equiv="refresh"' in head:
            return "stub"
    return "ok"


def scan_agent_surfaces(dist_dir):
    """Every faberlang.dev URL cited by an agent surface, and how it resolves."""
    missing, stubs, count = [], [], 0
    pattern = re.compile(re.escape(SITE) + r"(/[^\s)\"'|`,\]]*)")
    for f in agent_surface_files(dist_dir):
        text = f.read_text(encoding="utf-8", errors="ignore")
        for match in pattern.finditer(text):
            url = match.group(1).rstrip(".,;")
            if AGENT_URL_PLACEHOLDER.search(url):
                continue
            count += 1
            state = resolve_site_path(dist_dir, url)
            label = str(f.relative_to(dist_dir))
            if state == "missing":
                missing.append((label, url))
            elif state == "stub":
                stubs.append((label, url))
    return count, missing, stubs


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

    agent_count, agent_missing, agent_stubs = scan_agent_surfaces(args.dist_dir)
    print(f"Agent-surface URLs checked: {agent_count}")
    print(f"  broken: {len(agent_missing)}, via redirect stub: {len(agent_stubs)}")
    for label, url in agent_missing:
        print(f"  BROKEN {url}  ({label})")
    for label, url in agent_stubs:
        print(f"  STUB   {url}  ({label}) — cite the current path")

    if broken:
        missing = {}
        for hf, href in broken:
            missing.setdefault(href, []).append(hf)
        print(f"\nUnique missing targets: {len(missing)}")
        for href in sorted(missing):
            refs = missing[href]
            sample = refs[0].replace(args.dist_dir + "/", "")
            print(f"  {href}  ({len(refs)} ref(s), e.g. {sample})")

    return 1 if (broken or agent_missing or agent_stubs) else 0


if __name__ == "__main__":
    sys.exit(main())
