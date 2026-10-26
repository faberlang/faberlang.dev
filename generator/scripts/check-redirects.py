#!/usr/bin/env python3
"""
check-redirects.py — every meta-refresh stub in dist/ is a single clean hop.

GitHub Pages cannot send HTTP redirects, so retired URLs are HTML stubs with
`<meta http-equiv="refresh" content="0; url=…">`. Google follows an instant
meta refresh like a permanent redirect, but only one hop at a time and only
to a URL that exists. This gate fails when a stub:

  - points at a file that does not exist in dist/,
  - points at another stub (a redirect chain), or
  - points at a `/index.html` URL instead of the directory URL that the
    destination page declares as its canonical.

Usage:
    check-redirects.py <dist_dir>
"""

from __future__ import annotations

import html as html_mod
import re
import sys
from pathlib import Path
from urllib.parse import unquote

REFRESH_RE = re.compile(r'http-equiv="refresh" content="0; url=([^"]*)"')


def refresh_target(path: Path) -> str | None:
    head = path.read_text(encoding="utf-8", errors="replace")[:2048]
    match = REFRESH_RE.search(head)
    return html_mod.unescape(match.group(1)) if match else None


def file_for(dist: Path, url: str) -> Path:
    path = unquote(url.split("#", 1)[0])
    resolved = dist / path.lstrip("/")
    return resolved / "index.html" if path.endswith("/") else resolved


def main() -> int:
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2
    stubs = {}
    for page in dist.rglob("*.html"):
        target = refresh_target(page)
        if target is not None:
            stubs[page] = target
    errors: list[str] = []
    for page, target in sorted(stubs.items()):
        rel = "/" + page.relative_to(dist).as_posix()
        if not target.startswith("/"):
            errors.append(f"{rel}: non-site-relative target {target}")
            continue
        if target.split("#", 1)[0].endswith("/index.html"):
            errors.append(f"{rel}: targets {target} (use the directory URL)")
        dest = file_for(dist, target)
        if not dest.is_file():
            errors.append(f"{rel}: target {target} does not exist")
        elif dest in stubs:
            errors.append(f"{rel}: chain {target} -> {stubs[dest]}")
    print(f"redirect stubs checked: {len(stubs)}")
    if errors:
        for error in errors[:30]:
            print("ERROR:", error, file=sys.stderr)
        print(f"ERROR: {len(errors)} redirect stub errors", file=sys.stderr)
        return 1
    print("redirect stubs: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
