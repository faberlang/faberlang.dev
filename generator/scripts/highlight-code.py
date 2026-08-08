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

# Match on the inner `code.lang-…`, not the wrapper's class. What a block is
# written in is independent of how its container is presented: docs fences wear
# `pre.faber-code`, the landing page's tab panels and kernel block wear their
# own presentational classes, and all of them deserve colour.
#
# The class also carries the fence's whole info string, not just its language:
# ```faber locale=la  renders as  class="lang-faber locale=la". Capture the
# attribute wholesale and take the language off the front, or every annotated
# fence — including the only real Faber sample on the examples page — silently
# goes unpainted.
BLOCK_RE = re.compile(
    r'(<pre[^>]*><code class="lang-([^"]+)">)(.*?)(</code></pre>)',
    re.S,
)

# Languages worth colouring. `text` fences are program output, not source.
SUPPORTED = {
    "faber", "bash", "toml",
    # Generated target output, shown beside the Faber it came from.
    "rust", "go", "ts", "typescript",
    "metal-text", "wgsl-text", "llvm-text", "wasm-text",
}

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


# Generated target output. These panels exist to be *compared* with the Faber
# source beside them, so they need enough colour to read as code — not a second
# language implementation. Comments, strings, numbers, types and a shared
# keyword spine carry that; anything subtler stays plain.
CLIKE_KEYWORDS = (
    "fn|let|const|var|mut|pub|use|mod|impl|trait|struct|enum|match|move|dyn|as|"
    "func|package|import|type|interface|chan|defer|go|range|map|"
    "class|export|function|new|await|async|of|in|"
    "if|else|for|while|loop|do|switch|case|default|break|continue|return|"
    "true|false|null|nil|undefined|this|self|"
    "void|uniform|buffer|shared|kernel|constant|device|threadgroup|"
    "compute|group|binding|builtin|workgroup|array|vec2|vec3|vec4|thread"
)
CLIKE_TYPES = (
    "i8|i16|i32|i64|u8|u16|u32|u64|f16|f32|f64|usize|isize|bool|str|String|Vec|"
    "int|int8|int16|int32|int64|uint|uint32|uint64|float|float2|float3|float4|"
    "half|number|string|boolean|any|unknown|byte|rune|error"
)

CLIKE_SCANNER = re.compile(
    r"(?P<co>//[^\n]*|/\*.*?\*/)"
    r"|(?P<st>\"(?:[^\"\\\n]|\\.)*\"|'(?:[^'\\\n]|\\.)*'|`[^`]*`)"
    r"|(?P<an>@[A-Za-z_][\w.]*|\#\[[^\]\n]*\])"
    rf"|(?P<ty>(?<![\w.])(?:{CLIKE_TYPES})(?![\w]))"
    rf"|(?P<kw>(?<![\w.])(?:{CLIKE_KEYWORDS})(?![\w]))"
    r"|(?P<nu>(?<![\w.])\d[\d_]*(?:\.\d+)?(?:[eE][-+]?\d+)?)",
    re.S,
)

# Textual IR. Comment syntax differs (`;` for LLVM, `;;` for WAT) and the
# interesting tokens are the sigil-prefixed names, not keywords.
IR_SCANNER = re.compile(
    r"(?P<co>;[^\n]*)"
    r"|(?P<st>\"(?:[^\"\\\n]|\\.)*\")"
    r"|(?P<an>[%@$][\w.]+)"
    rf"|(?P<ty>(?<![\w.])(?:{CLIKE_TYPES}|i1|ptr|label|metadata)(?![\w]))"
    r"|(?P<kw>(?<![\w.])(?:define|declare|module|func|global|local|param|result|"
    r"call|call_indirect|ret|br|br_if|block|end|loop|memory|table|elem|data|"
    r"export|import|type|alloca|load|store|getelementptr|bitcast|icmp|fcmp|phi|"
    r"select|switch|unreachable|attributes|source_filename|target)(?![\w]))"
    r"|(?P<nu>(?<![\w.])\d[\d_]*(?:\.\d+)?)"
)

TARGET_SCANNERS: dict[str, re.Pattern] = {
    "rust": CLIKE_SCANNER,
    "go": CLIKE_SCANNER,
    "ts": CLIKE_SCANNER,
    "typescript": CLIKE_SCANNER,
    "metal-text": CLIKE_SCANNER,
    "wgsl-text": CLIKE_SCANNER,
    "llvm-text": IR_SCANNER,
    "wasm-text": IR_SCANNER,
}


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

    # A fence names a reader locale the way the compiler does (`en`, `la`),
    # while the search indexes are named for site locales (`en-US`).
    INDEX_ALIAS = {"en": "en-US"}

    # Reader-pack vocabularies cached by locale-tabs.py. These are the
    # authority for a locale's spellings; the search indexes carry Latin
    # canonical terms and would leave an English panel's keywords grey.
    vocab_dir = Path(__file__).resolve().parents[1] / "locale-tabs"

    def faber_for(locale: str | None) -> re.Pattern:
        if locale not in scanners:
            words: set[str] = set()
            if locale:
                vocab = vocab_dir / f"vocab.{locale}.json"
                if vocab.is_file():
                    try:
                        words = set(json.loads(vocab.read_text(encoding="utf-8")))
                    except (json.JSONDecodeError, OSError):
                        words = set()
            if not words:
                resolved = INDEX_ALIAS.get(locale or "", locale)
                name = ("search-index.json" if resolved is None
                        else f"search-index.{resolved}.json")
                index = dist / name
                if not index.is_file():
                    index = dist / "search-index.json"
                words = load_keywords(index)
            scanners[locale] = faber_scanner(keyword_pattern(words))
        return scanners[locale]

    blocks = 0
    touched = 0

    for page in sorted(dist.rglob("*.html")):
        text = page.read_text(encoding="utf-8")
        if '<code class="lang-' not in text or "tok-" in text:
            continue

        locale = locale_of(page, dist)
        stats = {"n": 0}

        def replace(match: re.Match) -> str:
            open_tag, info, body, close_tag = match.groups()
            fields = info.split()
            language = fields[0] if fields else ""
            if language not in SUPPORTED:
                return match.group(0)
            source = html_mod.unescape(body)
            if language == "faber":
                # A fence may name its own reader locale (```faber locale=th-TH),
                # which outranks the page's. The landing page needs this: it is
                # locale-less at the site root, yet its hero strip shows the same
                # program in eight reader locales side by side.
                fence_locale = next(
                    (f.split("=", 1)[1] for f in fields[1:] if f.startswith("locale=")),
                    None,
                )
                scanner = faber_for(fence_locale or locale)
            elif language == "bash":
                scanner = BASH_SCANNER
            elif language == "toml":
                scanner = TOML_SCANNER
            else:
                scanner = TARGET_SCANNERS[language]
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
