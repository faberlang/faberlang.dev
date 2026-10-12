#!/usr/bin/env python3
"""Write and verify aliases for the retired translated site trees."""
from __future__ import annotations

import argparse
import sys
import tomllib
from urllib.parse import unquote
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MANIFEST = REPO / "generator" / "redirects" / "retired-locales.toml"
STUB = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="https://faberlang.dev{target}">
<meta name="robots" content="noindex">
<title>Moved</title>
</head>
<body><p>This page moved to <a href="{target}">{target}</a>.</p></body>
</html>
'''


def entries() -> list[tuple[str, str]]:
    with MANIFEST.open("rb") as f:
        records = tomllib.load(f).get("redirects", [])
    return [(row["from"], row["to"]) for row in records]


def path_for(dist: Path, url: str) -> Path:
    path = dist / unquote(url.lstrip("/"))
    return path / "index.html" if url.endswith("/") else path


def stubs(dist: Path) -> int:
    rows = entries()
    for old, target in rows:
        path = path_for(dist, old)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(STUB.format(target=target), encoding="utf-8")
    print(f"retired locale stubs: wrote {len(rows)}")
    return 0


def check(dist: Path) -> int:
    rows = entries()
    errors: list[str] = []
    for old, target in rows:
        path = path_for(dist, old)
        if not path.is_file():
            errors.append(f"missing stub: {old}")
            continue
        html = path.read_text(encoding="utf-8")
        if 'http-equiv="refresh" content="0; url=' + target + '"' not in html:
            errors.append(f"wrong refresh target: {old} -> {target}")
        if not path_for(dist, target).is_file():
            errors.append(f"unresolved target: {old} -> {target}")
    print(f"retired locale aliases checked: {len(rows)}")
    if errors:
        for error in errors[:30]:
            print("ERROR:", error, file=sys.stderr)
        print(f"ERROR: {len(errors)} alias errors", file=sys.stderr)
        return 1
    print("retired locale aliases: PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("stubs", "check"))
    parser.add_argument("--dist", type=Path, default=REPO / "dist")
    args = parser.parse_args()
    return (stubs(args.dist) or 0) if args.command == "stubs" else check(args.dist)

if __name__ == "__main__":
    raise SystemExit(main())
