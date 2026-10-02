#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write meta-refresh redirect stubs into dist/ from generator/redirects/*.toml.

Each fragment file holds rows mapping a retired site path to its successor:

    "/en-US/features/glyphs.html" = "/en-US/language/behavior/glyphs.html"

A stub is written only when the old path has no live page in dist/ (a real
rendered page always wins over a redirect) and the target page exists. The
stub format matches the hand-written retired-root stubs already in dist/.
Idempotent: a byte-identical stub is left untouched.

Usage:
    python3 apply-redirects.py [--dist dist] [--redirects generator/redirects]
                               [--dry-run]
"""

import argparse
import sys
from pathlib import Path

import tomllib

STUB_TEMPLATE = """<!DOCTYPE html>
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
"""


def is_stub(path: Path) -> bool:
    try:
        return 'http-equiv="refresh"' in path.read_text(encoding="utf-8")
    except OSError:
        return False


def main() -> int:
    repo = Path(__file__).resolve().parent.parent.parent
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dist", type=Path, default=repo / "dist")
    parser.add_argument("--redirects", type=Path, default=repo / "generator" / "redirects")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.redirects.is_dir():
        print(f"apply-redirects: no redirect fragments at {args.redirects}; nothing to do")
        return 0

    errors: list[str] = []
    written = unchanged = 0
    for fragment in sorted(args.redirects.glob("*.toml")):
        try:
            rows = tomllib.loads(fragment.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"{fragment.name}: invalid TOML: {exc}")
            continue
        for old, new in rows.items():
            if not (old.startswith("/") and new.startswith("/")):
                errors.append(f"{fragment.name}: paths must be site-absolute: {old!r} -> {new!r}")
                continue
            target = args.dist / new.lstrip("/")
            if not target.is_file():
                errors.append(f"{fragment.name}: target {new} missing in dist/")
                continue
            stub_path = args.dist / old.lstrip("/")
            if stub_path.is_file() and not is_stub(stub_path):
                errors.append(f"{fragment.name}: {old} is a live page; a stub would shadow it")
                continue
            content = STUB_TEMPLATE.format(target=new)
            if stub_path.is_file() and stub_path.read_text(encoding="utf-8") == content:
                unchanged += 1
                continue
            print(f"{'would write' if args.dry_run else 'write'} stub {old} -> {new}")
            if not args.dry_run:
                stub_path.parent.mkdir(parents=True, exist_ok=True)
                stub_path.write_text(content, encoding="utf-8")
            written += 1

    print(f"apply-redirects: {written} stubs {'to write' if args.dry_run else 'written'}, {unchanged} unchanged")
    if errors:
        for err in errors:
            print(f"apply-redirects: ERROR {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
