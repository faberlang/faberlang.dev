#!/usr/bin/env python3
"""Generate the public /llms.txt surface from corpus frontmatter."""

from __future__ import annotations

import argparse
import collections
import re
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 fallback
    import tomli as tomllib  # type: ignore

from corpus_locale import default_reader_root, display_slug, load_pack


@dataclass(frozen=True)
class Term:
    name: str
    kind: str
    category: str
    summary: str
    syntax: str
    aliases: tuple[str, ...] = field(default_factory=tuple)
    related: tuple[str, ...] = field(default_factory=tuple)
    source: str = ""


def parse_frontmatter(path: Path) -> dict[str, object] | None:
    parts = path.read_text().split("+++", 2)
    if len(parts) != 3:
        return None
    return tomllib.loads(parts[1])


def as_list(value: object) -> tuple[str, ...]:
    if not isinstance(value, list):
        return ()
    return tuple(str(item) for item in value)


def corpus_slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "uncategorized"


_EN_PACK = load_pack(default_reader_root(), "en")


def corpus_page(term: str, kind: str = "keyword") -> str:
    """English-site filename: pack slug, falling back to the Latin identity."""
    return quote(f"{display_slug(term, kind, _EN_PACK)}.html", safe="")


def load_terms(corpus: Path) -> tuple[list[Term], dict[str, list[str]], int]:
    canonical: dict[str, Term] = {}
    aliases: dict[str, list[str]] = collections.defaultdict(list)
    distinct_terms: set[str] = set()

    for path in sorted(corpus.rglob("*.fab")):
        fields = parse_frontmatter(path)
        if not fields:
            continue
        term = str(fields.get("term", "")).strip()
        if not term:
            continue
        distinct_terms.add(term)
        if bool(fields.get("canonical", False)) and term not in canonical:
            rel = path.relative_to(corpus)
            canonical[term] = Term(
                name=term,
                kind=str(fields.get("kind", "unknown")),
                category=str(fields.get("category", "uncategorized")),
                summary=str(fields.get("summary", "")).strip(),
                syntax=str(fields.get("syntax", "")).strip(),
                aliases=as_list(fields.get("aliases")),
                related=as_list(fields.get("related")),
                source=str(rel),
            )
        for alias in as_list(fields.get("aliases")):
            aliases[alias].append(term)

    terms = sorted(canonical.values(), key=lambda term: term.name)
    return terms, aliases, len(distinct_terms)


def write_section(lines: list[str], title: str) -> None:
    lines.extend(["", f"## {title}", ""])


def emit_llms_txt(terms: list[Term], aliases: dict[str, list[str]], distinct_terms: int) -> str:
    categories = collections.Counter(term.category for term in terms)
    kinds = collections.Counter(term.kind for term in terms)
    alias_rows = [(alias, sorted(set(targets))) for alias, targets in aliases.items()]
    alias_rows.sort(key=lambda item: item[0])

    lines: list[str] = [
        "# Faber",
        "",
        "Faber is a package-oriented programming language. Meaning lives in a",
        "semantic core (HIR); reader locales and codegen targets are renderings",
        "of that core. Write the English reader spelling unless asked otherwise.",
        "",
        "The writing guide is https://faberlang.dev/agents/index.md.",
        "Follow only /agents/ links from that page.",
        "This file is the generated keyword catalog, not the writing guide.",
    ]

    write_section(lines, "Start here")
    lines.extend([
        "1. Fetch https://faberlang.dev/agents/index.md and follow it.",
        "2. Host: https://faberlang.dev. `/` is the product landing page. `/porta/` is the locale chooser.",
        "3. The records below are a term lookup. They are not the writing guide.",
        "4. Install the CLI by following https://faberlang.dev/install.md.",
    ])

    write_section(lines, "Language shape")
    lines.extend([
        "- Type-first bindings: `string name`, not `name: string`.",
        "- English reader words: `fn`, `class`, `const`, `return`, `if`, `for`, `main`, `print`.",
        "- Glyphs: `←` bind, `→` return type, `≡` equality, `∪` union.",
        "- Nullable type: `T ∪ none`. Null value: `null`.",
        "- Comments: `#` only, on its own line. No `//`, no trailing `#`.",
        "- Packages: directory with `faber.toml` + `src/*.fab`.",
    ])

    write_section(lines, "Generated corpus frontmatter reference")
    lines.extend([
        f"- Distinct frontmatter terms: {distinct_terms}",
        f"- Canonical term pages: {len(terms)}",
        f"- Alias spellings: {len(alias_rows)}",
        f"- Categories: {len(categories)}",
        "- Source: radix/corpus/**/*.fab TOML frontmatter",
        "",
        "Each canonical record has: term, kind, category, summary, syntax signature, aliases, relations, and page URL.",
    ])

    lines.extend(["", "### Categories", ""])
    for category, count in sorted(categories.items(), key=lambda item: item[0]):
        lines.append(f"- {category} ({count}) — https://faberlang.dev/en-US/corpus/category/{corpus_slug(category)}.html")

    lines.extend(["", "### Kinds", ""])
    for kind, count in sorted(kinds.items(), key=lambda item: item[0]):
        lines.append(f"- {kind}: {count}")

    lines.extend(["", "### Canonical terms", ""])
    for term in terms:
        aliases_text = ", ".join(f"`{alias}`" for alias in term.aliases) or "none"
        related_text = ", ".join(f"`{rel}`" for rel in term.related) or "none"
        syntax_text = term.syntax or "n/a"
        summary_text = term.summary or "n/a"
        lines.extend([
            f"#### `{term.name}`",
            "",
            f"- Canonical: `{term.name}`",
            f"- Kind: {term.kind}",
            f"- Category: {term.category}",
            f"- Summary: {summary_text}",
            f"- Syntax: `{syntax_text}`",
            f"- Aliases: {aliases_text}",
            f"- Related: {related_text}",
            f"- Page: https://faberlang.dev/en-US/corpus/{corpus_page(term.name, term.kind)}",
            f"- Source: radix/corpus/{term.source}",
            "",
        ])

    lines.extend(["### Alias map", ""])
    for alias, targets in alias_rows:
        target_text = ", ".join(f"`{target}`" for target in targets)
        lines.append(f"- `{alias}` → {target_text}")

    write_section(lines, "Documentation map")
    lines.extend([
        "- https://faberlang.dev/ — language portal (pick a site locale)",
        "- https://faberlang.dev/en-US/ — English overview (canonical full tree)",
        "- https://faberlang.dev/install.md — install route for agents; the human page is /en-US/start/",
        "- https://faberlang.dev/en-US/localization.html — the eight reader locales, and why each",
        "- https://faberlang.dev/en-US/cheatsheet/ — short worked examples by topic",
        "- https://faberlang.dev/en-US/language/ — language reference",
        "- https://faberlang.dev/en-US/toolchain/ — compiler, CLI, targets, device execution",
        "- https://faberlang.dev/en-US/targets/ — source beside what each target lowers to",
        "- https://faberlang.dev/en-US/examples/ — real package source",
        "- https://faberlang.dev/en-US/libraries/ — Norma, Triga, the corpus",
        "- https://faberlang.dev/en-US/corpus/ — generated keyword / construct pages",
        "- https://faberlang.dev/en-US/releases/ — every version, pinned installs, release notes",
        "- https://faberlang.dev/en-US/open-source.html — licensing, repositories, issue routing",
        "- https://faberlang.dev/en-US/reference/ — EBNF, design docs",
        "- Prefer /en-US/… over bare paths. /syntax/, /features/, /tooling/,",
        "  /ecosystem/, /history/ and /references/ are retired redirect stubs.",
    ])

    write_section(lines, "Repositories")
    lines.extend([
        "- https://github.com/faberlang/faber — public target APIs and project home",
        "- https://github.com/faberlang/releases — tagged CLI release assets",
        "- https://github.com/faberlang/norma — standard library",
        "- https://github.com/faberlang/cista — package store",
        "- https://github.com/faberlang/triga — graphics / geometry",
        "- https://github.com/faberlang/examples — corpus + application packages",
        "- https://github.com/faberlang/faberlang.dev — this site",
    ])

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    terms, aliases, distinct_terms = load_terms(args.corpus)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(emit_llms_txt(terms, aliases, distinct_terms))
    print(f"generated {args.output} from {len(terms)} canonical terms")


if __name__ == "__main__":
    main()
