#!/usr/bin/env python3
"""Project Markdown terms into a reader locale's keyword surface."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from project_reader_terms import load_mapping, project_markdown


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Markdown file or localized tree")
    parser.add_argument("--locale", required=True)
    parser.add_argument("--packs", type=Path, default=Path(__file__).resolve().parents[3] / "radix" / "locale")
    args = parser.parse_args()
    if args.locale == "la":
        return 0
    pack = args.packs / args.locale / "pack.toml"
    if not pack.is_file():
        print(f"reader pack not found: {pack}", file=sys.stderr)
        return 1
    mapping = load_mapping(pack)
    files = [args.path] if args.path.is_file() else sorted(args.path.rglob("*.md"))
    for path in files:
        original = path.read_text(encoding="utf-8")
        updated = project_markdown(original, mapping, relative_path=path.as_posix(), reader=args.locale)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
