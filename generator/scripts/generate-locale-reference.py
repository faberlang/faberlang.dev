#!/usr/bin/env python3
"""Generate the Reader locales section from the eight reader packs.

This is the human counterpart of `generate-agent-locales.py`: the same join on
the canonical (Latin) key, rendered as a reference a person browses rather than
a table a model fetches. Pages written under `src/en-US/language/locales/`:

  keywords.md      index of the mapping pages plus the pack legend — the full
                   eight-pack join stays machine-facing at /agents/locales.md
  <locale>.md      one mapping page per reader language (la, ar, hi, th-TH, vi,
                   zh-Hans, zh-Hant): English | Latin | target, except the
                   Latin page, which stays two-column (Latin | English).
                   English has no page: it is the page language itself and a
                   base surface, so its spelling leads every table instead
  diagnostics.md   one compiler failure (`faber check --diagnostics`) captured
                   in every installed locale by capture-locale-diagnostics.sh
  examples.md      one program shown across all eight surfaces, read from the
                   committed locale-tabs cache — never re-rendered here

The packs are read with `agent_locales`, so the column order, the Latin
identity fallback, and the "designed incompleteness" rules stay identical to
the agent table. Only installed packs appear; a missing pack is a build
problem with its own report.

Why every table is a fenced block: on an English page the render pipeline
projects inline canonical terms to their English spelling
(`project_reader_terms.py`), which is right for prose and wrong for a reference
whose whole job is to show the canonical key. `translate_spans = false` skips
only the later HTML pass. A fence declaring `locale=la` is left byte-exact by
both passes, so each mapping is written as a fixed-width block inside one. The
per-locale tables need it as much as the full one: an English value can itself
be another row's canonical key (`nihil`, `per`), and projection would rewrite
the cell it is printed in.

Gate E (`--check`): the mapping rows are extracted back out of every mapping
page's frozen tables and diffed against an independent join from the packs
(`agent_locales.rows`). The run must report zero missing rows (pack rows
absent from the page) and zero dead rows (page rows with no pack backing),
and the current-epoch rows (sort/ordinata, bytes/octeti, at/apud) must appear
on every mapping page.

Usage:
    generate-locale-reference.py [--packs PATH] [--output-dir DIR] [--check]
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

from agent_locales import PACK_COLUMNS, SECTIONS, read_packs, rows
from corpus_locale import default_reader_root

REPO = Path(__file__).resolve().parents[2]
DEFAULT_OUT = REPO / "src" / "en-US" / "language" / "locales"
DEFAULT_CAPTURES = REPO / "generator" / "locale-captures"
DEFAULT_TABS = REPO / "generator" / "locale-tabs"
# The committed hello-world panel set: `main { print "Salve, munde!" }`.
DEFAULT_EXAMPLE_KEY = "0aca787373d25281"


def default_packs() -> Path:
    """The pinned reader packs (see upstream.py)."""
    return default_reader_root()


SECTION_TITLES = {
    "keywords": "Keywords",
    "types": "Types",
    "intrinsics": "Intrinsics",
}

# Ordered join, same as agent_locales.PACK_COLUMNS. English first; Latin second
# as one locale among eight.
LOCALES: dict[str, dict[str, str]] = {
    "en": {
        "name": "English",
        "native": "English",
        "script": "Latin",
        "direction": "left-to-right",
        "note": "A base surface: English keywords map to the English word, so "
                "its reader spelling is also what an English reader writes.",
    },
    "la": {
        "name": "Latin",
        "native": "Latina",
        "script": "Latin",
        "direction": "left-to-right",
        "note": "The identity pack. Every other pack maps the same keys to its "
                "own words, and the pack key *is* the Latin spelling.",
    },
    "ar": {
        "name": "Arabic",
        "native": "العربية",
        "script": "Arabic",
        "direction": "right-to-left",
        "note": "Right-to-left script written in logical order inside a "
                "left-to-right code block. HTML diagnostics wrap Arabic "
                "keywords in `<bdi>` so an error does not point at the wrong "
                "character.",
    },
    "hi": {
        "name": "Hindi",
        "native": "हिन्दी",
        "script": "Devanagari",
        "direction": "left-to-right",
        "note": "Matra and virama consonant clusters, where one grapheme spans "
                "several code points. Indic numeral glyphs (०–९) are rejected "
                "inside numeric literals; digits stay ASCII.",
    },
    "th-TH": {
        "name": "Thai",
        "native": "ไทย",
        "script": "Thai",
        "direction": "left-to-right",
        "note": "A spaceless script: there are no inter-word boundaries, so the "
                "lexer resolves every token boundary by keyword matching. "
                "Combining vowel and tone marks stack on base characters.",
    },
    "vi": {
        "name": "Vietnamese",
        "native": "Tiếng Việt",
        "script": "Latin (Vietnamese)",
        "direction": "left-to-right",
        "note": "Latin script, but not English — the control case. Heavy "
                "diacritics stress NFKC equivalence, and multi-word keywords "
                "join with underscores (`bắt_đầu`).",
    },
    "zh-Hans": {
        "name": "Simplified Chinese",
        "native": "简体中文",
        "script": "Han (Simplified)",
        "direction": "left-to-right",
        "note": "Paired keywords (如果 / 否则) are single tokens needing pack "
                "keyword groups, and full/half-width punctuation collapses "
                "under NFKC normalization.",
    },
    "zh-Hant": {
        "name": "Traditional Chinese",
        "native": "繁體中文",
        "script": "Han (Traditional)",
        "direction": "left-to-right",
        "note": "A sibling pack, not a variant spelling: it carries different "
                "vocabulary (定值 against 常量) over the same semantics.",
    },
}

# The mapping pages: every reader pack except English. English is the page
# language itself and a base surface, so its spelling leads every table instead
# of carrying its own page; Latin stays two-column as the canonical identity.
MAPPING_PAGES: tuple[str, ...] = tuple(loc for loc in PACK_COLUMNS if loc != "en")

# Placeholder for a pack that declares no spelling for a term.
EMPTY_CELL = "—"


def width(text: str) -> int:
    """Display width in a monospace cell: CJK and fullwidth are double."""
    total = 0
    for ch in text:
        if unicodedata.combining(ch):
            continue
        total += 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1
    return total


def pad(text: str, columns: int) -> str:
    return text + " " * max(0, columns - width(text))


def frontmatter(title: str, order: int, sources: list[str]) -> list[str]:
    lines = [
        "+++",
        f'title = "{title}"',
        'section = "locales"',
        f"order = {order}",
        "sources = [",
    ]
    lines += [f'  "{source}",' for source in sources]
    lines += [
        "]",
        "# This page is about the vocabulary itself; the reader-span pass would",
        "# otherwise translate the reference it exists to show.",
        "translate_spans = false",
        "+++",
        "",
    ]
    return lines


def frozen_table(header: tuple[str, ...], records: list[tuple[str, ...]]) -> list[str]:
    """A fixed-width grid inside a `locale=la` fence.

    The leading `|` keeps every line from starting with a canonical key, so the
    Markdown localizer never mistakes the block for translatable Faber.
    """
    widths = [
        max(width(header[i]), *(width(row[i]) for row in records))
        for i in range(len(header))
    ]
    lines = ["| " + "  ".join(pad(header[i], widths[i]) for i in range(len(header))).rstrip()]
    lines.append("| " + "  ".join("-" * widths[i] for i in range(len(header))))
    for row in records:
        lines.append("| " + "  ".join(pad(row[i], widths[i]) for i in range(len(header))).rstrip())
    return lines


def legend() -> list[str]:
    lines = [
        "The eight installed packs:",
        "",
        "| Code | Native name | Script | Direction |",
        "|---|---|---|---|",
    ]
    for loc in PACK_COLUMNS:
        meta = LOCALES[loc]
        lines.append(
            f"| `{loc}` | {meta['native']} | {meta['script']} | {meta['direction']} |"
        )
    lines.append("")
    return lines


def render_index(packs: dict) -> str:
    lines = frontmatter(
        "Keyword reference", 1, ["radix/locale/<locale>/pack.toml"]
    )
    lines += [
        "Every Faber keyword, primitive type, and intrinsic has one pack key "
        "(a Latin spelling) and one spelling per reader pack. This page indexes the "
        "mapping pages generated from those packs; read any row across to "
        "translate one term.",
        "",
        "English is the page language and a base surface: English keywords map "
        "to the English word, so its reader spelling is also what an English "
        "reader writes. Every mapping page therefore leads with the English "
        "column, and English carries no separate page. The Latin column is the "
        "pack key — the compiler's internal identity, one locale among "
        "eight rather than a privileged one: rendering to English and "
        "rendering to Thai are the same operation.",
        "",
        "The full eight-pack join stays machine-facing at "
        "[/agents/locales.md](/agents/locales.md); rows the packs do not all "
        "declare are listed there, not on the human pages.",
        "",
        "## Mapping pages {#pages}",
        "",
        "| Page | Locale | Columns |",
        "|---|---|---|",
    ]
    for loc in MAPPING_PAGES:
        meta = LOCALES[loc]
        if loc == "la":
            columns = "Latin · English"
        else:
            columns = f"English · Latin · {meta['native']}"
        lines.append(
            f"| [{meta['native']} ({meta['name']})](/language/locales/{loc}.html)"
            f" | `{loc}` | {columns} |"
        )
    lines += [
        "| [Diagnostics by locale](/language/locales/diagnostics.html) | — | "
        "one failure, every pack |",
        "| [Locale examples](/language/locales/examples.html) | — | "
        "one program, eight surfaces |",
        "",
        "The tables on those pages are generated from the packs themselves and "
        "cannot drift from the compiler by hand. A blank cell is a pack that "
        "declares no spelling for that term.",
        "",
    ]
    lines += legend()
    lines += [
        "---",
        "",
        "[All reader locales](/language/reader-locales.html)",
        "",
    ]
    return "\n".join(lines)


def page_header(loc: str) -> tuple[str, ...]:
    """The frozen-table column header for one mapping page."""
    if loc == "la":
        return ("Latin", "English")
    return ("English", "Latin", LOCALES[loc]["native"])


def page_row(cells: dict, loc: str) -> tuple[str, ...]:
    """One mapping row as the page renders it, from one joined pack row."""
    if loc == "la":
        return (cells["la"], cells.get("en", "") or EMPTY_CELL)
    return (
        cells.get("en", "") or EMPTY_CELL,
        cells["la"],
        cells.get(loc, "") or EMPTY_CELL,
    )


def render_locale_page(packs: dict, loc: str) -> str:
    meta = LOCALES[loc]
    lines = frontmatter(f"{meta['name']} reader locale", 10 + PACK_COLUMNS.index(loc),
                        ["radix/locale/<locale>/pack.toml"])
    lines += [
        f"**{meta['native']}** — the `{loc}` reader pack. Script: "
        f"{meta['script']}; direction: {meta['direction']}.",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| **Locale code** | `{loc}` |",
        f"| **Native name** | {meta['native']} |",
        f"| **Script** | {meta['script']} |",
        f"| **Direction** | {meta['direction']} |",
        "",
        meta["note"],
        "",
    ]
    if loc == "la":
        lines += [
            "## Latin ↔ English {#mapping}",
            "",
            "Generated from the packs. The Latin column is the pack key and "
            "the compiler's internal identity; the English "
            "column is the base-surface spelling. The other reader languages "
            "lead with English on [their mapping pages]"
            "(/language/locales/keywords.html).",
            "",
        ]
    else:
        lines += [
            f"## English ↔ {meta['name']} {{#mapping}}",
            "",
            "Generated from the packs; read a row across to translate one "
            "term. The Latin column is the pack key, which keys the "
            "[keyword reference](/language/locales/keywords.html).",
            "",
        ]
    header = page_header(loc)
    for section in SECTIONS:
        lines += [f"### {SECTION_TITLES[section]} {{#{section.lower()}}}", ""]
        records = [page_row(cells, loc) for _canonical, cells in rows(packs, section)]
        lines += ["```text locale=la"]
        lines += frozen_table(header, records)
        lines += ["```", ""]
    lines += [
        "---",
        "",
        "[All reader locales](/language/reader-locales.html) · "
        "[Keyword reference](/language/locales/keywords.html) · "
        "[Diagnostics in this locale](/language/locales/diagnostics.html)",
        "",
    ]
    return "\n".join(lines)


def render_diagnostics(captures: Path) -> str | None:
    fixture = captures / "error.fab"
    present = [loc for loc in PACK_COLUMNS if (captures / f"{loc}.txt").is_file()]
    if not present:
        return None
    lines = frontmatter(
        "Diagnostics by locale", 2, ["generator/locale-captures/"]
    )
    lines += [
        "Diagnostics are structured facts before prose. Each carries a stable "
        "code and named arguments, and the reader pack owns the rendered "
        "template — so the same failure can be printed in any locale without "
        "changing the diagnosis.",
        "",
        "One deliberately broken program, checked once per reader pack:",
        "",
    ]
    # `locale=la` pins the block out of both the Markdown and HTML localization
    # passes, so the captured bytes read exactly as the compiler printed them.
    if fixture.is_file():
        lines += ["```console locale=la", fixture.read_text(encoding="utf-8").rstrip(), "```", ""]
    lines += [
        "The failure is lexical, so it is identical in every locale: a string "
        "literal with no closing quote, `LEX001`. Only the message text moves. "
        "Run `faber check --diagnostics --diagnostics-locale <locale>` to reproduce it.",
        "",
    ]
    for loc in present:
        meta = LOCALES.get(loc, {"name": loc, "native": loc})
        lines += [
            f"## {meta['name']} (`{loc}`) {{#{loc.lower()}}}",
            "",
            "```console locale=la",
            (captures / f"{loc}.txt").read_text(encoding="utf-8").rstrip(),
            "```",
            "",
        ]
    lines += [
        "---",
        "",
        "[All reader locales](/language/reader-locales.html) · "
        "[Keyword reference](/language/locales/keywords.html)",
        "",
    ]
    return "\n".join(lines)


def render_examples(tabs: Path, key: str) -> str | None:
    panels = {
        loc: tabs / f"{key}.{loc}.fab"
        for loc in PACK_COLUMNS
        if (tabs / f"{key}.{loc}.fab").is_file()
    }
    if len(panels) < 2:
        return None
    lines = frontmatter(
        "Locale examples", 3, ["generator/locale-tabs/"]
    )
    lines += [
        "One program, eight reader surfaces. Faber source is written once and "
        "printed in whichever locale the reader asks for: keywords and type "
        "names change, while identifiers, strings, and the glyphs carrying "
        "structure stay put.",
        "",
        "The panels below are the committed `generator/locale-tabs/` cache — "
        "`faber convert` output, not hand-written Thai or Arabic. The Latin "
        "panel is the identity pack's rendering; the rest are that same program rendered "
        "into each locale.",
        "",
    ]
    for loc in PACK_COLUMNS:
        path = panels.get(loc)
        if path is None:
            continue
        meta = LOCALES[loc]
        lines += [f"## {meta['name']} (`{loc}`) {{#{loc.lower()}}}", ""]
        body = path.read_text(encoding="utf-8").rstrip()
        if loc == "la":
            # An explicit locale keeps the canonical panel out of the en-US
            # fence localizer, which would otherwise print it as English.
            lines += ["```faber locale=la", body, "```", ""]
        else:
            lines += [f"```text locale={loc}", body, "```", ""]
        if loc == "la":
            lines += ["The same program on the identity pack, whose words are the pack keys.", ""]
    lines += [
        "---",
        "",
        "[All reader locales](/language/reader-locales.html) · "
        "[Keyword reference](/language/locales/keywords.html)",
        "",
    ]
    return "\n".join(lines)


# Gate E epoch rows: the (English, Latin) spelling pairs that prove the tables
# carry the current epoch of the packs, not a stale snapshot. Resolved against
# the pack join at check time, so the pack keys are discovered, not hardcoded.
EPOCH_PAIRS: tuple[tuple[str, str], ...] = (
    ("sort", "ordinata"),
    ("bytes", "octeti"),
    ("at", "apud"),
)


def split_frozen_line(line: str) -> list[str]:
    """One frozen-table line as cells; columns are 2+ spaces apart."""
    return re.split(r"\s{2,}", line.strip().lstrip("|").strip())


def extract_frozen_tables(text: str) -> list[list[tuple[str, ...]]]:
    """Every `locale=la` text fence as a row grid (header, rule, data...).

    The extraction reads only the rendered page — the same bytes a reader or
    the renderer sees — so drift is measured in the artifact, not in memory.
    """
    tables: list[list[tuple[str, ...]]] = []
    block: list[str] = []
    inside = False
    for line in text.splitlines():
        if not inside and line.startswith("```text locale=la"):
            inside, block = True, []
        elif inside and line.startswith("```"):
            inside = False
            if len(block) >= 3:
                tables.append([tuple(split_frozen_line(row)) for row in block])
        elif inside:
            block.append(line)
    return tables


def expected_section_rows(packs: dict, section: str, loc: str) -> list[tuple[str, ...]]:
    """The rows one mapping page must carry for a section, from the pack join."""
    return [page_row(cells, loc) for _canonical, cells in rows(packs, section)]


def epoch_join(packs: dict) -> list[tuple[str, str, dict]]:
    """`(section, canonical, cells)` for every pack row matching an epoch pair."""
    found: list[tuple[str, str, dict]] = []
    for section in SECTIONS:
        for canonical, cells in rows(packs, section):
            if (cells.get("en", ""), cells["la"]) in EPOCH_PAIRS:
                found.append((section, canonical, cells))
    return found


def check_mapping_pages(packs: dict, pages: dict[str, str]) -> bool:
    """Gate E: frozen tables vs the pack join. Prints the report; True = green."""
    problems: list[str] = []
    missing_total = dead_total = 0
    extracted: dict[str, list[list[tuple[str, ...]]]] = {}
    checked = 0
    for loc in MAPPING_PAGES:
        name = f"{loc}.md"
        if name not in pages:
            problems.append(f"{name}: not generated")
            continue
        checked += 1
        tables = extract_frozen_tables(pages[name])
        extracted[loc] = tables
        if len(tables) != len(SECTIONS):
            problems.append(
                f"{name}: found {len(tables)} frozen tables, expected {len(SECTIONS)}"
            )
            continue
        header = page_header(loc)
        for section, table in zip(SECTIONS, tables):
            if tuple(table[0]) != header:
                problems.append(f"{name} {section}: header {list(table[0])} != {list(header)}")
                continue
            expected = Counter(expected_section_rows(packs, section, loc))
            actual = Counter(table[2:])
            missing = expected - actual
            dead = actual - expected
            missing_total += sum(missing.values())
            dead_total += sum(dead.values())
            if missing:
                problems.append(f"{name} {section}: missing {sorted(missing)}")
            if dead:
                problems.append(f"{name} {section}: dead {sorted(dead)}")

    print(
        f"Gate E: {checked} mapping pages checked — "
        f"{missing_total} missing, {dead_total} dead rows"
    )
    for problem in problems:
        print(f"  DRIFT {problem}")

    epoch_failures = 0
    for section, canonical, cells in epoch_join(packs):
        present = 0
        for loc in MAPPING_PAGES:
            tables = extracted.get(loc, [])
            on_page = (
                len(tables) == len(SECTIONS)
                and page_row(cells, loc) in {tuple(r) for r in tables[SECTIONS.index(section)][2:]}
            )
            present += on_page
        spell = f"{cells.get('en', EMPTY_CELL)} ↔ {cells['la']}"
        print(f"  epoch {spell} ({section}/{canonical}): on {present}/{len(MAPPING_PAGES)} pages")
        if present != len(MAPPING_PAGES):
            epoch_failures += 1
            problems.append(f"epoch row {spell} absent from some pages")

    if problems:
        print(f"Gate E: FAIL ({len(problems)} findings)")
        return False
    print("Gate E: green — zero dead, zero missing, all epoch rows present")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packs", type=Path, default=default_packs(),
                        help="workspace radix/locale root")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--captures", type=Path, default=DEFAULT_CAPTURES)
    parser.add_argument("--tabs", type=Path, default=DEFAULT_TABS)
    parser.add_argument("--example-key", default=DEFAULT_EXAMPLE_KEY)
    parser.add_argument("--check", action="store_true",
                        help="Gate E: write, then verify the written mapping pages against the pack join")
    args = parser.parse_args()

    if not args.packs.is_dir():
        print(f"locale packs not found: {args.packs}", file=sys.stderr)
        return 1

    packs = read_packs(args.packs)
    missing = [loc for loc in PACK_COLUMNS if loc not in packs]
    for loc in missing:
        print(f"WARNING: no pack installed for {loc} under {args.packs}", file=sys.stderr)

    pages: dict[str, str] = {"keywords.md": render_index(packs)}
    for loc in MAPPING_PAGES:
        if loc in packs:
            pages[f"{loc}.md"] = render_locale_page(packs, loc)

    diagnostics = render_diagnostics(args.captures)
    if diagnostics is not None:
        pages["diagnostics.md"] = diagnostics
    else:
        print("  no diagnostics captures; leaving diagnostics.md alone", file=sys.stderr)

    examples = render_examples(args.tabs, args.example_key)
    if examples is not None:
        pages["examples.md"] = examples
    else:
        print("  no locale-tabs panels for that key; leaving examples.md alone",
              file=sys.stderr)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    # `en.md` is retired (English is the page language; its base-surface
    # sentence lives on the hub index) but stays in the cleanup set so a
    # checkout that still carries it is regenerated away.
    known = set(pages) | {f"{loc}.md" for loc in PACK_COLUMNS}
    for existing in args.output_dir.glob("*.md"):
        if existing.name not in pages and existing.name in known:
            existing.unlink()
    for name, text in pages.items():
        path = args.output_dir / name
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path.relative_to(REPO)}")

    # Gate E verifies the written state, not the in-memory pages dict: read
    # the mapping pages back from disk and diff them against the pack join.
    if args.check:
        written = {
            f"{loc}.md": (args.output_dir / f"{loc}.md").read_text(encoding="utf-8")
            for loc in MAPPING_PAGES
            if (args.output_dir / f"{loc}.md").is_file()
        }
        return 0 if check_mapping_pages(packs, written) else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
