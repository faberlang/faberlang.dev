#!/usr/bin/env python3
"""Generate dist/search-index*.json — renderbar keyword-search datasets.

Walks examples/corpus/**/*.fab TOML frontmatter (same source as
render-llms.py) and emits, per site locale, a compact JSON array:

    [{"t": term, "d": display, "k": kind, "c": category, "s": summary,
      "a": [aliases]}]

"d" is the locale's pack spelling for the term (from
stdlib/reader/{reader_locale}/pack.toml [keywords]/[types]); it is omitted
when the pack has no mapping or the mapping is Latin-identical, so the
client falls back to the canonical Latin "t". As packs fill in, rebuilding
regenerates richer indexes — no schema change.

Also emits the locale-less base search-index.json (no "d"), which the
client falls back to if a per-locale file is missing.

Hrefs stay locale-prefixed Latin-term pages — built client-side as
/{site_locale}/corpus/{encodeURIComponent(term)}.html, matching the corpus
renderer (see render-llms.py corpus_page).

Usage:
    generate-search-index.py --corpus <examples/corpus> --output-dir <dist>
        [--locales generator/locales.toml]
        [--reader-root workspace/radix/stdlib/reader]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 fallback
    import tomli as tomllib  # type: ignore


def parse_frontmatter(path: Path) -> dict[str, object] | None:
    parts = path.read_text(encoding="utf-8").split("+++", 2)
    if len(parts) != 3:
        return None
    return tomllib.loads(parts[1])


def as_list(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item) for item in value]


def load_toml(path: Path) -> dict:
    with path.open("rb") as f:
        return tomllib.load(f)


def pack_display_map(pack_path: Path) -> dict[str, str]:
    """Latin term → localized spelling from a reader pack."""
    if not pack_path.is_file():
        return {}
    data = load_toml(pack_path)
    display: dict[str, str] = {}
    for section in ("keywords", "types"):
        for latin, native in data.get(section, {}).items():
            if isinstance(native, str) and native and native != latin:
                display[latin] = native
    return display


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--locales", type=Path, default=None)
    parser.add_argument("--reader-root", type=Path, default=None)
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    generator_dir = script_dir.parent
    if args.locales is None:
        args.locales = generator_dir / "locales.toml"
    if args.reader_root is None:
        args.reader_root = generator_dir.parent.parent / "radix" / "stdlib" / "reader"

    canonical: dict[str, dict[str, object]] = {}
    for path in sorted(args.corpus.rglob("*.fab")):
        fields = parse_frontmatter(path)
        if not fields:
            continue
        term = str(fields.get("term", "")).strip()
        if not term or not bool(fields.get("canonical", False)) or term in canonical:
            continue
        canonical[term] = {
            "t": term,
            "k": str(fields.get("kind", "unknown")),
            "c": re.sub(r"[^a-z0-9]+", "-", str(fields.get("category", "")).lower()).strip("-"),
            "s": str(fields.get("summary", "")).strip(),
            "a": as_list(fields.get("aliases")),
        }

    terms = sorted(canonical, key=str.casefold)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    def emit(path: Path, display: dict[str, str]) -> None:
        entries = []
        for term in terms:
            entry = dict(canonical[term])
            if term in display:
                entry["d"] = display[term]
            entries.append(entry)
        path.write_text(
            json.dumps(entries, ensure_ascii=False, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )

    # Base (locale-less) index: canonical Latin only.
    emit(args.output_dir / "search-index.json", {})

    # Per-site-locale indexes with pack display spellings.
    registry = load_toml(args.locales).get("locales", {})
    for site, entry in sorted(registry.items()):
        reader_loc = entry.get("reader_locale", site)
        display = pack_display_map(args.reader_root / reader_loc / "pack.toml")
        out = args.output_dir / f"search-index.{site}.json"
        emit(out, display)
        print(f"  {out.name}: {len(terms)} terms, {sum(1 for t in terms if t in display)} localized spellings")

    print(f"generated {len(terms)} canonical terms → {args.output_dir}")


if __name__ == "__main__":
    main()
