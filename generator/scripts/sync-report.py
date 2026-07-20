#!/usr/bin/env python3
"""sync-report — provenance oracle for locale Markdown files.

Reports sync status of each locale ``.md`` file against its paired
``src/en-US/`` source using two-hash provenance (Decision 18d).

Usage:
    sync-report.py [--locale LOC] [--json] [--fail-on-stale] [--self-check] [repo_root]
"""

import argparse
import json
import sys
from pathlib import Path

# Add generator/scripts to sys.path so sync_lib can be imported
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from sync_lib import (  # noqa: E402
    hashes_for_markdown,
    parse_frontmatter_fields,
    rel_pair,
    split_frontmatter,
)


def discover_locale_dirs(src_root: Path) -> list[str]:
    """Return locale directory names under *src_root*, excluding 'en-US'."""
    locales: list[str] = []
    if not src_root.is_dir():
        return locales
    for entry in sorted(src_root.iterdir()):
        if entry.is_dir() and entry.name != "en-US":
            locales.append(entry.name)
    return locales


def collect_md_files(locale_dir: Path) -> list[Path]:
    """Return all ``.md`` files under *locale_dir* (recursive)."""
    if not locale_dir.is_dir():
        return []
    return sorted(locale_dir.rglob("*.md"))


def classify_file(
    locale_path: Path,
    locale: str,
    en_root: Path,
) -> dict:
    """Classify a single locale file against its paired en-US source.

    Returns a record dict with keys:
        file, locale, bucket, legacy_source_hash,
        prose_hash, code_hash (stored in locale),
        current_prose_hash, current_code_hash (from en-US).
    """
    record: dict = {
        "file": str(locale_path),
        "locale": locale,
        "bucket": None,
        "legacy_source_hash": False,
        "prose_hash": None,
        "code_hash": None,
        "source_commit": None,
        "current_prose_hash": None,
        "current_code_hash": None,
    }

    # Find paired en-US file
    en_path = rel_pair(locale_path, locale, en_root)
    if en_path is None or not en_path.exists():
        record["bucket"] = "missing_en"
        return record

    # Read locale file and parse frontmatter
    locale_text = locale_path.read_text(encoding="utf-8")
    fm_inner, _ = split_frontmatter(locale_text)
    locale_fields = parse_frontmatter_fields(fm_inner)

    stored_prose = locale_fields.get("prose_hash", "")
    stored_code = locale_fields.get("code_hash", "")
    stored_commit = locale_fields.get("source_commit", "")
    has_source_hash = "source_hash" in locale_fields

    record["prose_hash"] = stored_prose if stored_prose else None
    record["code_hash"] = stored_code if stored_code else None
    record["source_commit"] = stored_commit if stored_commit else None
    record["legacy_source_hash"] = has_source_hash

    # Compute current en-US hashes
    en_text = en_path.read_text(encoding="utf-8")
    current_prose, current_code = hashes_for_markdown(en_text)
    record["current_prose_hash"] = current_prose
    record["current_code_hash"] = current_code

    # Classify
    if not stored_prose:
        record["bucket"] = "missing_provenance"
    elif stored_prose != current_prose:
        record["bucket"] = "stale_prose"
    elif stored_code != current_code:
        record["bucket"] = "stale_code_only"
    else:
        record["bucket"] = "current"

    return record


def print_human_report(locale: str, records: list[dict]) -> None:
    """Print human-readable sync report for one locale."""
    buckets = {
        "missing_en": 0,
        "missing_provenance": 0,
        "stale_prose": 0,
        "stale_code_only": 0,
        "current": 0,
    }
    for r in records:
        b = r["bucket"]
        if b in buckets:
            buckets[b] += 1

    print(f"=== sync-report {locale} ===")
    for bucket_name in [
        "missing_provenance",
        "stale_prose",
        "stale_code_only",
        "current",
        "missing_en",
    ]:
        print(f"{bucket_name}: {buckets[bucket_name]}")
    print(f"total: {len(records)}")
    print()

    # Per-file listing
    for r in records:
        annotations: list[str] = []
        if r["legacy_source_hash"]:
            annotations.append("legacy source_hash present")
        ann_str = f"  ({'; '.join(annotations)})" if annotations else ""
        print(f"  {r['file']}  {r['bucket']}{ann_str}")
    print()


def run_report(
    repo_root: Path,
    locale_filter: str | None,
    fmt: str,
) -> tuple[int, list[dict]]:
    """Run sync report and return (exit_code, all_records)."""
    src_root = repo_root / "src"
    en_root = src_root / "en-US"

    if not en_root.is_dir():
        print(f"error: {en_root} does not exist", file=sys.stderr)
        return 1, []

    if locale_filter:
        locales = [locale_filter]
    else:
        locales = discover_locale_dirs(src_root)

    all_records: list[dict] = []

    for locale in locales:
        locale_dir = src_root / locale
        md_files = collect_md_files(locale_dir)
        records: list[dict] = []
        for md_path in md_files:
            rec = classify_file(md_path, locale, en_root)
            records.append(rec)
        all_records.extend(records)

        if fmt == "human":
            print_human_report(locale, records)

    if fmt == "json":
        if locale_filter:
            print(json.dumps(all_records, indent=2))
        else:
            # Group by locale
            grouped: dict[str, list[dict]] = {}
            for r in all_records:
                grouped.setdefault(r["locale"], []).append(r)
            print(json.dumps(grouped, indent=2))

    return 0, all_records


def self_check() -> int:
    """Run self-check assertions.

    Builds fixture markdown and verifies:
    - Mutating fence interior → prose_hash unchanged, code_hash changed.
    - Mutating prose → prose_hash changed, code_hash unchanged.
    """
    fm = '+++\ntitle = "self-check"\n+++\n'

    # Base fixture with prose + fence
    body1 = fm + "Some introductory text.\n\n```python\nprint(1)\n```\n\nTrailing prose.\n"

    # Mutate only fence interior
    body2 = fm + "Some introductory text.\n\n```python\nprint(999)\n```\n\nTrailing prose.\n"

    # Mutate only prose
    body3 = fm + "Different text.\n\n```python\nprint(1)\n```\n\nTrailing prose.\n"

    h1 = hashes_for_markdown(body1)
    h2 = hashes_for_markdown(body2)
    h3 = hashes_for_markdown(body3)

    try:
        assert h1[0] == h2[0], (
            f"FAIL: prose_hash changed when fence mutated\n"
            f"  base: {h1[0]}\n  mutated: {h2[0]}"
        )
        assert h1[1] != h2[1], (
            f"FAIL: code_hash unchanged when fence mutated\n"
            f"  both: {h1[1]}"
        )
        assert h1[0] != h3[0], (
            f"FAIL: prose_hash unchanged when prose mutated\n"
            f"  base: {h1[0]}\n  mutated: {h3[0]}"
        )
        assert h1[1] == h3[1], (
            f"FAIL: code_hash changed when prose mutated\n"
            f"  base: {h1[1]}\n  mutated: {h3[1]}"
        )

        print("self-check: PASS")
        return 0
    except AssertionError as e:
        print(e, file=sys.stderr)
        return 1


def resolve_repo_root(args_path: str | None) -> Path:
    """Resolve repo root from CLI argument or default to parent of generator/."""
    if args_path:
        return Path(args_path).resolve()
    # Default: parent of generator/scripts/
    return _SCRIPT_DIR.parent.parent.resolve()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Provenance sync-report oracle for locale Markdown files"
    )
    parser.add_argument(
        "--locale",
        type=str,
        default=None,
        help="Only report for LOCALE (e.g. th-TH)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        default=False,
        help="Output JSON instead of human-readable report",
    )
    parser.add_argument(
        "--fail-on-stale",
        action="store_true",
        default=False,
        help="Exit code 1 if any file is not current",
    )
    parser.add_argument(
        "--self-check",
        action="store_true",
        default=False,
        help="Run self-check assertions and exit",
    )
    parser.add_argument(
        "repo_root",
        nargs="?",
        type=str,
        default=None,
        help="Repository root path (default: parent of generator/)",
    )

    args = parser.parse_args()

    if args.self_check:
        return self_check()

    repo_root = resolve_repo_root(args.repo_root)
    fmt = "json" if args.json else "human"
    exit_code, records = run_report(repo_root, args.locale, fmt)

    if args.fail_on_stale:
        non_current = [r for r in records if r["bucket"] != "current"]
        if non_current:
            print(
                f"fail-on-stale: {len(non_current)} non-current file(s)",
                file=sys.stderr,
            )
            return 1

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
