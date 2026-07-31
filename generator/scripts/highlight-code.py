#!/usr/bin/env python3
"""
highlight-code.py — Syntax colouring for fenced code blocks in rendered HTML.

Wraps tokens inside ``<pre class="faber-code"><code class="lang-…">`` in
``<span class="tok-…">`` elements that the stylesheet colours. The generator
emits the fence and its language class; this adds the tokens, so no Faber-side
change is needed and no client-side highlighter ships to readers.

Faber's keyword vocabulary is not hardcoded here. It is read from the
search-index JSON the build already generates from the corpus, per locale —
so a locale tree whose fences are written in that locale's own spellings gets
highlighted in that spelling, and the vocabulary cannot drift from the
language. Anything the index does not know simply stays uncoloured.

Idempotent: a block that already contains token spans is left alone.

Usage:
    highlight-code.py <dist_dir>
"""

from __future__ import annotations

import html as html_mod
import json
import re
import sys
from pathlib import Path

BLOCK_RE = re.compile(
    r'(<pre class="faber-code"><code class="lang-([a-zA-Z0-9_-]+)">)(.*?)(</code></pre>)',
    re.S,
)

# Languages worth colouring. `text` fences are program output, not source.
SUPPORTED = {"faber", "bash", "toml"}

# Faber's operator glyphs, longest first so ≠ never loses to =.
FABER_OPERATORS = [
    "←", "→", "≡", "≠", "≥", "≤", "⊕", "⊗", "∈", "∉", "∪", "∩", "×", "÷", "√",
    "…", "¬", "∀", "∃", "≈", "∞", "±",
    "?.", "!.", "::", "..", "|>", "&&", "||", "==", "!=", "<=", ">=", "->", "=>",
    "+", "-", "*", "/", "%", "<", ">", "=", "|", "&", "!", "?", ":",
]


def load_keywords(index_path: Path) -> set[str]:
    """Keyword spellings from a generated search index, Latin and localized."""
    if not index_path.is_file():
        return set()
    try:
        entries = json.loads(index_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return set()

    words: set[str] = set()
    for entry in entries:
        if entry.get("k") != "keyword":
            continue
        for key in ("t", "d"):
            value = entry.get(key)
            if isinstance(value, str) and value.strip():
                words.add(value.strip())
    return words


def keyword_pattern(words: set[str]) -> re.Pattern | None:
    if not words:
        return None
    ordered = sorted(words, key=len, reverse=True)
    alternation = "|".join(re.escape(word) for word in ordered)
    # Latin-script keywords must not match inside a longer identifier. The
    # lookarounds use the ASCII identifier class so CJK spellings, which have
    # no such boundary, still match.
    return re.compile(rf"(?<![A-Za-z0-9_])(?:{alternation})(?![A-Za-z0-9_])")


def faber_scanner(keywords: re.Pattern | None) -> re.Pattern:
    operators = "|".join(re.escape(op) for op in FABER_OPERATORS)
    parts = [
        r"(?P<co>(?m:^[ \t]*\#[^\n]*))",
        r"(?P<st>\"(?:[^\"\\\n]|\\.)*\"|'(?:[^'\\\n]|\\.)*'|`[^`\n]*`|«[^»\n]*»)",
        r"(?P<an>@[A-Za-z_][\w.-]*)",
        r"(?P<nu>(?<![\w.])\d[\d_]*(?:\.\d+)?)",
    ]
    if keywords is not None:
        parts.append(f"(?P<kw>{keywords.pattern})")
    parts.append(rf"(?P<op>{operators})")
    return re.compile("|".join(parts))


BASH_SCANNER = re.compile(
    r"(?P<co>(?m:^[ \t]*\#[^\n]*))"
    r"|(?P<st>\"(?:[^\"\\\n]|\\.)*\"|'[^'\n]*')"
    # The command at the head of a line. Skips `key = value` assignments and
    # ALL-CAPS words so heredoc delimiters and env names stay plain.
    r"|(?m:^[ \t]*)(?P<fn>[a-z_][\w./-]*)(?![\w.-]*[ \t]*=)"
    r"|(?P<op>(?<=\s)--?[A-Za-z][\w-]*)"
    r"|(?P<nu>\$\{?[A-Za-z_]\w*\}?)"
)

TOML_SCANNER = re.compile(
    r"(?P<co>(?m:^[ \t]*\#[^\n]*))"
    r"|(?P<st>\"(?:[^\"\\\n]|\\.)*\"|'[^'\n]*')"
    r"|(?P<kw>(?m:^[ \t]*\[[^\]\n]*\]))"
    r"|(?P<an>(?m:^[ \t]*)[A-Za-z_][\w.-]*(?=[ \t]*=))"
    r"|(?P<nu>(?<![\w.])\d[\d_]*(?:\.\d+)?)"
)


def paint(source: str, scanner: re.Pattern) -> str:
    """Escape ``source`` and wrap recognised tokens in span elements."""
    out: list[str] = []
    cursor = 0
    for match in scanner.finditer(source):
        kind = match.lastgroup
        if kind is None:
            continue
        out.append(html_mod.escape(source[cursor : match.start()], quote=False))
        text = html_mod.escape(match.group(), quote=False)
        out.append(f'<span class="tok-{kind}">{text}</span>')
        cursor = match.end()
    out.append(html_mod.escape(source[cursor:], quote=False))
    return "".join(out)


def locale_of(page: Path, dist: Path) -> str | None:
    try:
        parts = page.relative_to(dist).parts
    except ValueError:
        return None
    return parts[0] if len(parts) > 1 else None


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: highlight-code.py <dist_dir>", file=sys.stderr)
        return 1

    dist = Path(sys.argv[1])
    if not dist.is_dir():
        print(f"ERROR: not a directory: {dist}", file=sys.stderr)
        return 1

    scanners: dict[str | None, re.Pattern] = {}

    def faber_for(locale: str | None) -> re.Pattern:
        if locale not in scanners:
            name = "search-index.json" if locale is None else f"search-index.{locale}.json"
            index = dist / name
            if not index.is_file():
                index = dist / "search-index.json"
            scanners[locale] = faber_scanner(keyword_pattern(load_keywords(index)))
        return scanners[locale]

    blocks = 0
    touched = 0

    for page in sorted(dist.rglob("*.html")):
        text = page.read_text(encoding="utf-8")
        if 'class="faber-code"' not in text or "tok-" in text:
            continue

        locale = locale_of(page, dist)
        stats = {"n": 0}

        def replace(match: re.Match) -> str:
            open_tag, language, body, close_tag = match.groups()
            if language not in SUPPORTED:
                return match.group(0)
            source = html_mod.unescape(body)
            if language == "faber":
                scanner = faber_for(locale)
            elif language == "bash":
                scanner = BASH_SCANNER
            else:
                scanner = TOML_SCANNER
            stats["n"] += 1
            return f"{open_tag}{paint(source, scanner)}{close_tag}"

        updated = BLOCK_RE.sub(replace, text)
        if updated != text:
            page.write_text(updated, encoding="utf-8")
            touched += 1
            blocks += stats["n"]

    print(f"  [highlight] {blocks} code block(s) across {touched} page(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
