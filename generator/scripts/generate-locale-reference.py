#!/usr/bin/env python3
"""Generate the Reader locales section from the eight reader packs.

This is the human counterpart of `generate-agent-locales.py`: the same join on
the canonical (Latin) key, rendered as a reference a person browses rather than
a table a model fetches. Pages written under `src/en-US/language/locales/`:

  keywords.md      one full mapping page — canonical key across all eight packs
  <locale>.md      one page per locale: English beside that locale, native name,
                   script, and a direction note where it matters
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

Usage:
    generate-locale-reference.py [--packs PATH] [--output-dir DIR] [--check]
"""

from __future__ import annotations

import argparse
import os
import sys
import unicodedata
from pathlib import Path

from agent_locales import PACK_COLUMNS, SECTIONS, incomplete, read_packs, rows
from corpus_locale import default_reader_root

REPO = Path(__file__).resolve().parents[2]
DEFAULT_OUT = REPO / "src" / "en-US" / "language" / "locales"
DEFAULT_CAPTURES = REPO / "generator" / "locale-captures"
DEFAULT_TABS = REPO / "generator" / "locale-tabs"
# The committed hello-world panel set: `main { print "Salve, munde!" }`.
DEFAULT_EXAMPLE_KEY = "0aca787373d25281"


def default_packs() -> Path:
    """Locate the reader packs.

    A normal checkout finds them beside the repo (`corpus_locale`). A git
    worktree does not, so the workspace path is next; `FABER_LOCALE_PACKS`
    overrides both.
    """
    override = os.environ.get("FABER_LOCALE_PACKS")
    if override:
        return Path(override)
    found = default_reader_root()
    if found.is_dir():
        return found
    for candidate in (REPO.parent / "radix" / "locale",
                      Path("/Users/ianzepp/work/faberlang/radix/locale")):
        if candidate.is_dir():
            return candidate
    return found

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
        "note": "The canonical pack. Every other pack is a translation of this "
                "one, and the pack key — the canonical name — *is* the Latin "
                "spelling.",
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

# Table headers. Short locale codes keep the full mapping narrow; the legend
# above it carries the native names.
COLUMN_HEADERS = ("en", "la", "ar", "hi", "th-TH", "vi", "zh-Hans", "zh-Hant")


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
        "The eight installed packs, in the column order used below:",
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


def render_keywords(packs: dict) -> str:
    lines = frontmatter(
        "Keyword reference", 1, ["radix/locale/<locale>/pack.toml"]
    )
    lines += [
        "Every Faber keyword, primitive type, and intrinsic has one canonical "
        "(Latin) name and one spelling per reader pack. This page is the full "
        "join across all eight packs, so a term can be translated by reading "
        "across a row.",
        "",
        "The tables are generated from the packs themselves and cannot drift "
        "from the compiler by hand. A blank cell is a pack that declares no "
        "spelling for that term — the contested rows are listed at the end "
        "rather than filled in.",
        "",
        "## How to read a table {#reading}",
        "",
        "- **Across a row** translates one term into any of the eight surfaces.",
        "- **Down a column** is the vocabulary one locale writes Faber in.",
        "- The `la` column is the canonical name, which is also the compiler's "
        "internal identity. It is one locale among eight, not a privileged one: "
        "rendering to English and rendering to Thai are the same operation.",
        "",
        "Arabic is right-to-left; its column runs in logical order inside this "
        "left-to-right block, so the characters read correctly even though the "
        "row places them among Latin script.",
        "",
    ]
    lines += legend()

    for section in SECTIONS:
        lines += [f"## {SECTION_TITLES[section]} {{#{section}}}", ""]
        records = [
            tuple(cells.get(loc, "") or "—" for loc in COLUMN_HEADERS)
            for _canonical, cells in rows(packs, section)
        ]
        lines += ["```text locale=la"]
        lines += frozen_table(COLUMN_HEADERS, records)
        lines += ["```", ""]

    found = incomplete(packs)
    lines += ["## Rows the packs do not all declare {#contested}", ""]
    if not found:
        lines += [
            "Every pack declares every key. Latin is identity-by-absence for "
            "intrinsics, which the table shows by carrying the canonical name.",
            "",
        ]
    else:
        lines += [
            f"{len(found)} rows are not declared by every pack. Each is owned by "
            "a compiler-side pack fix; the table above shows them as they are. "
            "The canonical names stay in the frozen block for the same reason "
            "the mapping does.",
            "",
        ]
        records = [
            (section, canonical, ", ".join(missing))
            for section, canonical, missing in found
        ]
        lines += ["```text locale=la"]
        lines += frozen_table(("section", "canonical key", "not declared by"), records)
        lines += ["```", ""]
    return "\n".join(lines) + "\n"


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
    if loc == "en":
        lines += [
            "Because English is a base surface, this page's two columns carry "
            "the same spelling: the English reader word is the canonical pack "
            "value for English.",
            "",
        ]
    lines += [
        f"## English ↔ {meta['name']} {{#mapping}}",
        "",
        "Generated from the packs; the canonical (Latin) name keys the full "
        "[keyword reference](/language/locales/keywords.html).",
        "",
    ]
    for section in SECTIONS:
        lines += [f"### {SECTION_TITLES[section]} {{#{section.lower()}}}", ""]
        records = [
            (cells.get("en", "") or "—", cells.get(loc, "") or "—")
            for _canonical, cells in rows(packs, section)
        ]
        lines += ["```text locale=la"]
        lines += frozen_table(("English", meta["native"]), records)
        lines += ["```", ""]
    lines += [
        "---",
        "",
        "[All reader locales](/language/reader-locales.html) · "
        "[Full keyword mapping](/language/locales/keywords.html) · "
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
        "Run `faber check --diagnostics --locale <locale>` to reproduce it.",
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
        "panel is canonical Faber; the rest are that same program rendered "
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
            lines += ["The canonical surface every other panel is a re-rendering of.", ""]
    lines += [
        "---",
        "",
        "[All reader locales](/language/reader-locales.html) · "
        "[Keyword reference](/language/locales/keywords.html)",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packs", type=Path, default=default_packs(),
                        help="workspace radix/locale root")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--captures", type=Path, default=DEFAULT_CAPTURES)
    parser.add_argument("--tabs", type=Path, default=DEFAULT_TABS)
    parser.add_argument("--example-key", default=DEFAULT_EXAMPLE_KEY)
    parser.add_argument("--check", action="store_true", help="report without writing")
    args = parser.parse_args()

    if not args.packs.is_dir():
        print(f"locale packs not found: {args.packs}", file=sys.stderr)
        return 1

    packs = read_packs(args.packs)
    missing = [loc for loc in PACK_COLUMNS if loc not in packs]
    for loc in missing:
        print(f"WARNING: no pack installed for {loc} under {args.packs}", file=sys.stderr)

    pages: dict[str, str] = {"keywords.md": render_keywords(packs)}
    for loc in PACK_COLUMNS:
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

    if args.check:
        for name in pages:
            print(f"would write {args.output_dir / name}")
        return 0

    args.output_dir.mkdir(parents=True, exist_ok=True)
    known = set(pages) | {f"{loc}.md" for loc in PACK_COLUMNS}
    for existing in args.output_dir.glob("*.md"):
        if existing.name not in pages and existing.name in known:
            existing.unlink()
    for name, text in pages.items():
        path = args.output_dir / name
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
