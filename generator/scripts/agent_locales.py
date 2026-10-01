#!/usr/bin/env python3
"""Join the eight locale packs into the /agents/locales.md cross-language table.

Each pack (`radix/locale/<locale>/pack.toml`) is keyed by the canonical name and
valued by that locale's surface spelling. The canonical key is the only key all
eight packs share, so the join runs on it. English leads the rendered columns
because `/agents/` is English-first; Latin sits second as one locale among eight.

Two shapes are design rather than drift:

- `la` has no `[intrinsics]` section. Latin is identity-by-absence for
  intrinsics, and `crates/radix-module/src/intrinsic_pack_completeness_test.rs`
  asserts both halves: every non-la pack owns a translated row, and `la` keeps
  the canonical spelling.
- A row may be a table instead of a string. `en` declares
  `approximata = { canonical = "approx", aliases = ["approximata"] }`, so the
  English spelling is `approx` and `approximata` is an accepted alias.

Every other disagreement is drift. Drift is rendered on the page and checked by
`--strict`, which fails on incompleteness that is neither design nor expected,
and equally on an expectation that no longer reproduces.
"""

from __future__ import annotations

from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 fallback
    import tomli as tomllib  # type: ignore

# Column order. English first, Latin second as one locale among eight.
PACK_COLUMNS: tuple[str, ...] = ("en", "la", "ar", "hi", "th-TH", "vi", "zh-Hans", "zh-Hant")
COLUMN_LABELS: dict[str, str] = {"en": "English", "la": "Latin"}

SECTIONS: tuple[str, ...] = ("keywords", "types", "intrinsics")
SECTION_TITLES: dict[str, str] = {
    "keywords": "Keywords",
    "types": "Types",
    "intrinsics": "Intrinsics",
}
SECTION_NOTES: dict[str, str] = {
    "intrinsics": (
        "Latin has no `[intrinsics]` section, so the Latin column carries each "
        "intrinsic's canonical name, which is the Latin spelling. Two canonicals can "
        "share one English word — `unio` and `union` both read `union` — so read the "
        "Latin column to tell them apart."
    ),
}

# Sections where a missing Latin section is the designed shape, not drift.
# Owner: crates/radix-module/src/intrinsic_pack_completeness_test.rs
IDENTITY_BY_ABSENCE: frozenset[str] = frozenset({"intrinsics"})

# Incompleteness that exists today and is owned by another item. `--strict`
# accepts exactly this and fails when an entry stops reproducing, so the list
# cannot silently rot.
# Owner: Vivi need 8349003b (locale packs: key-set drift across the eight packs).
EXPECTED_INCOMPLETE: dict[tuple[str, str], tuple[str, ...]] = {
    ("keywords", "conversion"): ("en", "la"),
    ("keywords", "nihil"): ("la",),
}

Spelling = tuple[str, tuple[str, ...]]  # surface spelling, accepted aliases
Pack = dict[str, dict[str, Spelling]]


def normalize(value: object) -> Spelling:
    """One pack row as `(spelling, aliases)`. A table row names its canonical."""
    if isinstance(value, dict):
        spelling = str(value.get("canonical") or "").strip()
        raw = value.get("aliases") or ()
        aliases = tuple(sorted(str(item).strip() for item in raw if str(item).strip()))
        return spelling, aliases
    return str(value).strip(), ()


def read_packs(root: Path) -> Pack:
    """Return `{locale: {section: {canonical: (spelling, aliases)}}}`.

    Only installed packs appear. An uninstalled locale is a build problem with
    its own report (`missing_packs`); counting it as incomplete would bury the
    real drift under five columns of noise.
    """
    packs: Pack = {}
    for locale in PACK_COLUMNS:
        path = root / locale / "pack.toml"
        if not path.is_file():
            continue
        with path.open("rb") as handle:
            data = tomllib.load(handle)
        tables: dict[str, dict[str, Spelling]] = {section: {} for section in SECTIONS}
        for section in SECTIONS:
            for canonical, value in (data.get(section) or {}).items():
                spelling, aliases = normalize(value)
                if spelling:
                    tables[section][str(canonical)] = (spelling, aliases)
        packs[locale] = tables
    return packs


def installed(packs: Pack) -> tuple[str, ...]:
    return tuple(locale for locale in PACK_COLUMNS if locale in packs)


def missing_packs(packs: Pack) -> tuple[str, ...]:
    return tuple(locale for locale in PACK_COLUMNS if locale not in packs)


def union_keys(packs: Pack, section: str) -> list[str]:
    keys: set[str] = set()
    for locale in installed(packs):
        keys.update(packs[locale].get(section, {}))
    return sorted(keys)


def incomplete(packs: Pack) -> list[tuple[str, str, tuple[str, ...]]]:
    """`(section, canonical, locales that lack it)`, excluding designed shapes."""
    found: list[tuple[str, str, tuple[str, ...]]] = []
    for section in SECTIONS:
        for canonical in union_keys(packs, section):
            missing = tuple(
                locale
                for locale in installed(packs)
                if canonical not in packs[locale].get(section, {})
                and not (section in IDENTITY_BY_ABSENCE and locale == "la")
            )
            if missing:
                found.append((section, canonical, missing))
    return found


def unexpected(found: list[tuple[str, str, tuple[str, ...]]]) -> list[tuple[str, str, tuple[str, ...]]]:
    return [item for item in found if EXPECTED_INCOMPLETE.get((item[0], item[1])) != item[2]]


def stale_expectations(found: list[tuple[str, str, tuple[str, ...]]]) -> list[tuple[str, str, tuple[str, ...]]]:
    actual = {(section, canonical): missing for section, canonical, missing in found}
    return [
        (section, canonical, missing)
        for (section, canonical), missing in sorted(EXPECTED_INCOMPLETE.items())
        if actual.get((section, canonical)) != missing
    ]


def alias_rows(packs: Pack) -> list[tuple[str, str, tuple[str, ...]]]:
    """`(section, canonical, aliases)` for every table-shaped row."""
    out: list[tuple[str, str, tuple[str, ...]]] = []
    for section in SECTIONS:
        for locale in PACK_COLUMNS:
            for canonical, (_spelling, aliases) in sorted(packs.get(locale, {}).get(section, {}).items()):
                if aliases:
                    out.append((section, canonical, aliases))
    return out


def cell(text: str) -> str:
    """One table cell: code-spanned, with pipes escaped so the row survives."""
    cleaned = text.replace("`", "'").replace("|", "\\|").replace("\n", " ").strip()
    return f"`{cleaned}`" if cleaned else ""


def rows(packs: Pack, section: str) -> list[tuple[str, dict[str, str]]]:
    """`(canonical, {locale: spelling})` for one section, sorted by English.

    The Latin column falls back to the canonical key. A pack key *is* the Latin
    spelling (the pack maps Latin to each locale's surface), and Latin is
    identity-by-absence wherever its pack omits a row — `la` carries no
    `[intrinsics]` section at all.
    """
    out: list[tuple[str, dict[str, str]]] = []
    for canonical in union_keys(packs, section):
        cells = {
            locale: packs.get(locale, {}).get(section, {}).get(canonical, ("", ()))[0]
            for locale in PACK_COLUMNS
        }
        cells["la"] = cells["la"] or canonical
        out.append((canonical, cells))
    out.sort(key=lambda pair: ((pair[1].get("en") or pair[0]).casefold(), pair[0]))
    return out


def render(packs: Pack) -> str:
    lines: list[str] = [
        "# Locales",
        "",
        "One source file uses one locale pack. The files in this canon are English.",
        "Keywords, types, and library members in a file come from that pack.",
        "",
        "```faber locale=en",
        "# English source.",
        "main {",
        '    print "en"',
        "}",
        "```",
        "",
        "Do not write `//`. That is rejected as `LEX006` `c_style_line_comment`. Do not",
        "put `#` after code on the same line. That is rejected as `LEX007`",
        "`inline_hash_after_code`.",
        "",
        "Everything below is the cross-language table, generated from the eight locale",
        "packs so it cannot drift from the compiler by hand.",
        "",
        "A program writes the spelling in its own locale's column. English is the spelling",
        "this canon writes. The Latin column is the canonical name, which the compiler also",
        "uses as its internal identity; it is otherwise one locale among eight. Read a row",
        "across to translate a term; read a column down to translate a program. A blank",
        "cell means that locale's pack declares no spelling for the term, which for the",
        "six translations is the signal that the packs disagree; the contested rows are",
        "listed at the end.",
        "",
    ]
    for section in SECTIONS:
        lines.append(f"## {SECTION_TITLES[section]}")
        lines.append("")
        note = SECTION_NOTES.get(section)
        if note:
            lines.append(note)
            lines.append("")
        header = " | ".join(COLUMN_LABELS.get(locale, locale) for locale in PACK_COLUMNS)
        lines.append(f"| {header} |")
        lines.append("| " + " | ".join("---" for _ in PACK_COLUMNS) + " |")
        for _canonical, cells in rows(packs, section):
            rendered = " | ".join(cell(cells.get(locale, "")) for locale in PACK_COLUMNS)
            lines.append(f"| {rendered} |")
        lines.append("")

    aliases = alias_rows(packs)
    if aliases:
        lines.append("### Alias rows")
        lines.append("")
        lines.append("These rows name an accepted alternate spelling. Both spellings are legal.")
        lines.append("")
        for section, canonical, names in aliases:
            spelled = ", ".join(f"`{name}`" for name in names)
            lines.append(f"- `{canonical}` in `{section}` is also written {spelled}.")
        lines.append("")

    found = incomplete(packs)
    lines.append("## Contested rows")
    lines.append("")
    if not found:
        lines.append("Every pack agrees, apart from the designed shapes noted above.")
    else:
        lines.append(
            f"{len(found)} rows are not declared by every pack. Each is owned by the "
            "compiler-side pack fix rather than by this table, which shows them as they are."
        )
        lines.append("")
        for section, canonical, missing in found:
            lacking = ", ".join(f"`{locale}`" for locale in missing)
            lines.append(f"- `{canonical}` in `{section}`: missing from {lacking}.")
    lines.append("")
    lines.append("Fetch list: https://faberlang.dev/agents/index.md")
    lines.append("")
    return "\n".join(lines)
