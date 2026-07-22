#!/usr/bin/env python3
"""Generate tooling/targets.md from radix/EBNF_MATRIX.md + locale string packs.

Prose/chrome lives in generator/locales/<locale>/targets.toml so matrix
regeneration does not wipe translations. Table cells (term/target ids and
glyphs) stay language-neutral.

Usage:
  python3 generator/scripts/generate-target-matrix.py
  python3 generator/scripts/generate-target-matrix.py --all-locales
  python3 generator/scripts/generate-target-matrix.py --matrix /path/to/EBNF_MATRIX.md
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tomllib
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
DEFAULT_MATRIX = WORKSPACE / "radix" / "EBNF_MATRIX.md"
LOCALES_DIR = REPO / "generator" / "locales"
DEFAULT_OUT = REPO / "src" / "en-US" / "tooling" / "targets.md"

REQUIRED_KEYS = (
    "title",
    "intro",
    "meta_generated",
    "meta_measurement",
    "meta_join",
    "official",
    "legend_heading",
    "legend_col_glyph",
    "legend_col_meaning",
    "legend_full",
    "legend_partial",
    "legend_planned",
    "legend_unsupported",
    "legend_unmeasured",
    "legend_note",
    "summary_heading",
    "app_lane",
    "sys_lane",
    "col_target",
    "col_capable",
    "col_analyzable",
    "col_pct",
    "col_term",
    "keywords_app",
    "operators_app",
    "keywords_sys",
    "operators_sys",
    "other_terms",
    "h3_keyword",
    "h3_operator_group",
    "h3_existing_home",
)


def load_pack(locale: str) -> dict[str, str]:
    path = LOCALES_DIR / locale / "targets.toml"
    if not path.is_file():
        raise FileNotFoundError(f"missing locale pack: {path}")
    with path.open("rb") as f:
        data = tomllib.load(f)
    missing = [k for k in REQUIRED_KEYS if k not in data]
    if missing:
        raise ValueError(f"{path}: missing keys: {', '.join(missing)}")
    return {k: str(data[k]).strip() for k in REQUIRED_KEYS}


def strip_leading_h1(body: str) -> str:
    lines = body.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and lines[0].strip() == "":
            lines = lines[1:]
    return "\n".join(lines).rstrip() + "\n"


def drop_regeneration_section(body: str) -> str:
    m = re.search(r"\n## Regeneration\n", body)
    if not m:
        return body
    return body[: m.start()].rstrip() + "\n"


def extract_generated_date(matrix_text: str) -> str:
    m = re.search(r"\*\*Generated\*\*:\s*(\d{4}-\d{2}-\d{2})", matrix_text)
    return m.group(1) if m else "unknown"


def extract_table_blocks(section_body: str) -> list[str]:
    """Return GFM pipe-table blocks (header + separator + rows) in order."""
    lines = section_body.splitlines()
    tables: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("|") and i + 1 < len(lines) and re.match(
            r"^\|[\s\-:|]+\|$", lines[i + 1].replace(" ", "")
        ) or (
            line.startswith("|")
            and i + 1 < len(lines)
            and set(lines[i + 1].replace("|", "").replace("-", "").replace(":", "").strip())
            <= {""}
            and "---" in lines[i + 1]
        ):
            block = [line, lines[i + 1]]
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                block.append(lines[i])
                i += 1
            tables.append("\n".join(block))
            continue
        i += 1
    return tables


def rewrite_summary_header(table: str, pack: dict[str, str]) -> str:
    lines = table.splitlines()
    # first data header row
    if not lines:
        return table
    # expect: | target | capable | analyzable | % |
    lines[0] = (
        f"| {pack['col_target']} | {pack['col_capable']} | "
        f"{pack['col_analyzable']} | {pack['col_pct']} |"
    )
    return "\n".join(lines)


def rewrite_term_header(table: str, pack: dict[str, str]) -> str:
    lines = table.splitlines()
    if not lines:
        return table
    cells = [c.strip() for c in lines[0].strip("|").split("|")]
    if not cells:
        return table
    cells[0] = pack["col_term"]
    lines[0] = "| " + " | ".join(cells) + " |"
    return "\n".join(lines)


def parse_matrix_sections(matrix_text: str) -> dict[str, str]:
    """Slice EBNF_MATRIX.md into named raw sections (English headings)."""
    body = drop_regeneration_section(strip_leading_h1(matrix_text))

    # Drop everything before "## Corpus-wide summary" for table extraction.
    # Legend is rebuilt from the locale pack.
    m = re.search(r"^## Corpus-wide summary", body, re.M)
    if not m:
        raise ValueError("matrix missing '## Corpus-wide summary'")
    rest = body[m.start() :]

    # Split on ## headings
    parts = re.split(r"(?m)^(## .+)$", rest)
    # parts[0] may be empty; then heading, body, heading, body...
    sections: dict[str, str] = {}
    i = 1
    while i + 1 < len(parts):
        heading = parts[i].strip()
        content = parts[i + 1]
        sections[heading] = content
        i += 2
    return sections


def current_git_head() -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO), "rev-parse", "HEAD"],
            text=True,
        )
        return out.strip()
    except Exception:
        return "unknown"


def prose_hash(text: str) -> str:
    import hashlib

    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def frontmatter(pack: dict[str, str], *, locale: str, body_for_hash: str) -> str:
    # Single-line sources (Speculum line-oriented frontmatter).
    sources = "radix/EBNF_MATRIX.md · target-capability-matrix.md · faber targets"
    lines = [
        "+++",
        f'title = "{pack["title"]}"',
        'section = "targets"',
        "order = 2",
        f'sources = "{sources}"',
    ]
    if locale != "en-US":
        commit = current_git_head()
        ph = prose_hash(body_for_hash)
        lines.extend(
            [
                "",
                'translation_kind = "translated"',
                f'prose_hash = "{ph}"',
                'code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"',
                f'source_commit = "{commit}"',
                'source_locale = "en-US"',
            ]
        )
    lines.append("+++")
    return "\n".join(lines) + "\n"


def build_legend(pack: dict[str, str]) -> str:
    return "\n".join(
        [
            f"## {pack['legend_heading']}",
            "",
            f"| {pack['legend_col_glyph']} | {pack['legend_col_meaning']} |",
            "|---|---|",
            f"| ✓ | {pack['legend_full']} |",
            f"| ◐ | {pack['legend_partial']} |",
            f"| ○ | {pack['legend_planned']} |",
            f"| ✕ | {pack['legend_unsupported']} |",
            f"| — | {pack['legend_unmeasured']} |",
            "",
            f"> {pack['legend_note'].replace(chr(10), chr(10) + '> ')}",
            "",
        ]
    )


def build_summary(sections: dict[str, str], pack: dict[str, str]) -> str:
    key = next(k for k in sections if k.startswith("## Corpus-wide summary"))
    content = sections[key]
    tables = extract_table_blocks(content)
    if len(tables) < 2:
        raise ValueError(f"expected 2 summary tables, got {len(tables)}")
    app = rewrite_summary_header(tables[0], pack)
    sys_ = rewrite_summary_header(tables[1], pack)
    return "\n".join(
        [
            f"## {pack['summary_heading']}",
            "",
            f"**{pack['app_lane']}**",
            "",
            app,
            "",
            f"**{pack['sys_lane']}**",
            "",
            sys_,
            "",
        ]
    )


def section_table(content: str, pack: dict[str, str], h2: str, h3: str) -> str:
    tables = extract_table_blocks(content)
    if not tables:
        raise ValueError(f"no table under section for {h2}")
    table = rewrite_term_header(tables[0], pack)
    return "\n".join([f"## {h2}", "", f"### {h3}", "", table, ""])


def build_page(matrix_text: str, pack: dict[str, str], *, locale: str) -> str:
    date = extract_generated_date(matrix_text)
    sections = parse_matrix_sections(matrix_text)

    body_parts: list[str] = [
        pack["intro"].strip(),
        "",
        pack["meta_generated"].format(date=date),
        pack["meta_measurement"],
        pack["meta_join"],
        "",
        pack["official"].strip(),
        "",
        build_legend(pack).rstrip(),
        "",
        build_summary(sections, pack).rstrip(),
        "",
    ]

    # Map English matrix headings → localized h2 + h3 keys
    mapping = [
        ("## Keywords — application lane", pack["keywords_app"], pack["h3_keyword"]),
        ("## Operators — application lane", pack["operators_app"], pack["h3_operator_group"]),
        ("## Keywords — systems lane", pack["keywords_sys"], pack["h3_keyword"]),
        ("## Operators — systems lane", pack["operators_sys"], pack["h3_operator_group"]),
        ("## Other terms", pack["other_terms"], pack["h3_existing_home"]),
    ]
    for en_prefix, h2, h3 in mapping:
        key = next((k for k in sections if k.startswith(en_prefix)), None)
        if key is None:
            raise ValueError(f"matrix missing section starting {en_prefix!r}")
        body_parts.append(section_table(sections[key], pack, h2, h3).rstrip())
        body_parts.append("")

    body = "\n".join(body_parts).rstrip() + "\n"
    fm = frontmatter(pack, locale=locale, body_for_hash=body)
    return fm + "\n" + body


def locale_dirs(src_root: Path) -> list[Path]:
    return sorted(p for p in src_root.iterdir() if p.is_dir())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--matrix", type=Path, default=DEFAULT_MATRIX)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--all-locales",
        action="store_true",
        help="Write targets.md for every src/<locale>/ that has a targets.toml pack",
    )
    parser.add_argument(
        "--locale",
        action="append",
        default=[],
        help="Write only these locales (repeatable). Default en-US only.",
    )
    args = parser.parse_args()

    if not args.matrix.is_file():
        print(f"ERROR: matrix not found: {args.matrix}", file=sys.stderr)
        return 1

    matrix_text = args.matrix.read_text(encoding="utf-8")

    locales: list[str]
    if args.all_locales:
        locales = []
        for p in locale_dirs(REPO / "src"):
            if (LOCALES_DIR / p.name / "targets.toml").is_file():
                locales.append(p.name)
        if "en-US" not in locales and (LOCALES_DIR / "en-US" / "targets.toml").is_file():
            locales.insert(0, "en-US")
    elif args.locale:
        locales = args.locale
    else:
        locales = ["en-US"]

    for locale in locales:
        try:
            pack = load_pack(locale)
        except (FileNotFoundError, ValueError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 1
        page = build_page(matrix_text, pack, locale=locale)
        out = (
            args.output
            if locale == "en-US" and args.output != DEFAULT_OUT
            else REPO / "src" / locale / "tooling" / "targets.md"
        )
        if locale == "en-US" and not args.all_locales and not args.locale:
            out = args.output
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        print(f"wrote {out.relative_to(REPO)} ({len(page.splitlines())} lines) [{locale}]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
