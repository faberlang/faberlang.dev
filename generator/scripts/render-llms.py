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


def corpus_page(term: str) -> str:
    return quote(f"{term}.html", safe="")


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
        "Faber is a package-oriented programming language with a Latin behavioural",
        "vocabulary, a small regular grammar, and a type-first static type system.",
        "Source compiles through the Radix compiler to reviewable Rust and native",
        "binaries. Meaning lives in a semantic core (HIR); every human-language",
        "keyword surface and every codegen target is a rendering of that core.",
        "",
        "This document is the machine-readable public entrypoint for agents.",
        "It is generated during the site build from examples/corpus frontmatter.",
    ]

    write_section(lines, "Start here")
    lines.extend([
        "1. Host: https://faberlang.dev — `/` is the language portal (locale chooser).",
        "2. Full authored HTML docs: https://faberlang.dev/en-US/ (prefer this unless the user asked for another locale).",
        "3. Read this file before editing Faber source or scaffolding packages.",
        "4. Use corpus term links below for exact keyword, syntax, alias, and relation data.",
        "5. Read https://faberlang.dev/agents/index.md for the agent learning path.",
        "6. Read https://faberlang.dev/llms-full.txt for the generated keyword/category/alias catalog.",
        "7. Choose focused skills from https://faberlang.dev/.well-known/agent-skills/index.json.",
        "8. Other site locales (`/th-TH/`, `/zh-Hans/`, `/ar/`, …) ship full translated prose docs + localized chrome; code via each pack's reader locale.",
    ])

    write_section(lines, "Install")
    lines.extend([
        "Current release: Faber 1.1.1",
        "",
        "- Release: https://github.com/faberlang/releases/releases/tag/faber-v1.1.1",
        "- macOS arm64: https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz",
        "- Linux x64: https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz",
        "- Human install page: https://faberlang.dev/en-US/start/install.html",
        "",
        "Minimal verify after install:",
        "",
        "```bash",
        "faber --version",
        "faber explain SEM001",
        "```",
    ])

    write_section(lines, "Language shape")
    lines.extend([
        "- Type-first bindings: `textus nomen` not `nomen: textus`.",
        "- Latin behavioural words: `functio`, `genus`, `fixum`, `redde`, `si`, `itera`.",
        "- Glyphs: `←` bind, `→` return type, `∴` compact branch, `≡` equality, `∪` union.",
        "- Nullable: `T ∪ nihil`.",
        "- Comments: `#` only, on its own line. No `//`, no trailing `#`.",
        "- Packages: directory with `faber.toml` + `src/*.fab`.",
    ])

    write_section(lines, "Generated corpus frontmatter reference")
    lines.extend([
        f"- Distinct frontmatter terms: {distinct_terms}",
        f"- Canonical term pages: {len(terms)}",
        f"- Alias spellings: {len(alias_rows)}",
        f"- Categories: {len(categories)}",
        "- Source: examples/corpus/**/*.fab TOML frontmatter",
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
            f"- Page: https://faberlang.dev/en-US/corpus/{corpus_page(term.name)}",
            f"- Source: examples/corpus/{term.source}",
            "",
        ])

    lines.extend(["### Alias map", ""])
    for alias, targets in alias_rows:
        target_text = ", ".join(f"`{target}`" for target in targets)
        lines.append(f"- `{alias}` → {target_text}")

    write_section(lines, "Documentation map")
    lines.extend([
        "- https://faberlang.dev/ — language portal (pick a site locale)",
        "- https://faberlang.dev/en-US/ — English overview + download (canonical full tree)",
        "- https://faberlang.dev/en-US/start/ — quick tour",
        "- https://faberlang.dev/en-US/features/ — locales, lanes, glyphs, principles",
        "- https://faberlang.dev/en-US/syntax/ — language reference",
        "- https://faberlang.dev/en-US/tooling/ — compiler, CLI, targets",
        "- https://faberlang.dev/en-US/ecosystem/ — Norma, Cista, Triga, workbench",
        "- https://faberlang.dev/en-US/corpus/ — generated keyword / construct pages",
        "- https://faberlang.dev/en-US/references/ — EBNF, design docs, repos",
        "- https://faberlang.dev/en-US/history/ — timeline",
        "- Prefer /en-US/… over bare /start/… or /syntax/… (those are redirect stubs).",
    ])

    write_section(lines, "Repositories")
    lines.extend([
        "- https://github.com/faberlang/faber — public user CLI",
        "- https://github.com/faberlang/releases — tagged CLI release assets",
        "- https://github.com/faberlang/faber-runtime — runtime types for generated Rust",
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
