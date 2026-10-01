#!/usr/bin/env python3
"""Generate the /agents/locales.md cross-language table from the eight locale packs."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from agent_locales import (
    incomplete,
    missing_packs,
    read_packs,
    render,
    stale_expectations,
    unexpected,
)
from corpus_locale import default_reader_root

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUTS = (
    REPO_ROOT / "static" / "agents" / "locales.md",
    REPO_ROOT / "dist" / "agents" / "locales.md",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packs", type=Path, default=default_reader_root(),
                        help="workspace radix/locale root")
    parser.add_argument("--out", type=Path, action="append", default=None,
                        help="output path (repeatable); defaults to static/ and dist/")
    parser.add_argument("--strict", action="store_true",
                        help="fail on incompleteness that is neither design nor expected")
    parser.add_argument("--check", action="store_true",
                        help="report without writing")
    args = parser.parse_args()

    if not args.packs.is_dir():
        print(f"locale packs not found: {args.packs}", file=sys.stderr)
        return 1

    packs = read_packs(args.packs)
    found = incomplete(packs)
    surprise = unexpected(found)
    stale = stale_expectations(found)
    absent = missing_packs(packs)

    for locale in absent:
        print(f"WARNING: no pack installed for {locale} under {args.packs}", file=sys.stderr)

    for section, canonical, missing in found:
        print(f"drift: {section} '{canonical}' missing from {', '.join(missing)}", file=sys.stderr)
    for section, canonical, missing in surprise:
        print(f"UNEXPECTED: {section} '{canonical}' missing from {', '.join(missing)}", file=sys.stderr)
    for section, canonical, missing in stale:
        print(f"STALE EXPECTATION: {section} '{canonical}' now reads {', '.join(missing) or 'complete'}", file=sys.stderr)

    if not args.check:
        text = render(packs)
        for path in args.out or DEFAULT_OUTPUTS:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            print(f"wrote {path.relative_to(REPO_ROOT)}")

    if args.strict and (surprise or stale):
        print("ERROR: agent locales drift gate failed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
