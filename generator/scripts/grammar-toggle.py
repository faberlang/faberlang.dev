#!/usr/bin/env python3
"""Add pre-rendered reader spelling layers and a CSS-only grammar selector."""
from __future__ import annotations

import html
import re
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import upstream  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
PACKS = upstream.radix_root() / "locale"
LOCALES = [
    ("en-US", "English", "en"),
    ("la", "Latina", "la"),
    ("ar", "العربية", "ar"),
    ("hi", "हिन्दी", "hi"),
    ("th-TH", "ไทย", "th-TH"),
    ("vi", "Tiếng Việt", "vi"),
    ("zh-Hans", "简体中文", "zh-Hans"),
    ("zh-Hant", "繁體中文", "zh-Hant"),
]


def tables(locale: str) -> dict[str, str]:
    data = tomllib.loads((PACKS / locale / "pack.toml").read_text(encoding="utf-8"))
    merged: dict[str, str] = {}
    for section in ("keywords", "types"):
        values = data.get(section, {})
        if isinstance(values, dict):
            merged.update({key: value for key, value in values.items() if isinstance(value, str)})
    return merged


def add_layers(code: str, english_keys: dict[str, str], maps: dict[str, dict[str, str]]) -> str:
    # Markdown fenced content is escaped by the renderer. Operate on that text,
    # introducing markup only after the Markdown pass has completed.
    reverse: dict[str, str] = {}
    for key, spelling in english_keys.items():
        reverse.setdefault(html.escape(spelling, quote=False), key)
    candidates = sorted(reverse, key=len, reverse=True)
    if not candidates:
        return code
    pattern = re.compile(r"(?<![\w])(?:" + "|".join(re.escape(x) for x in candidates) + r")(?![\w])")

    def layered(match: re.Match[str]) -> str:
        source = match.group(0)
        key = reverse[source]
        out = [f'<span class="grammar-spelling" data-locale="en-US">{source}</span>']
        for locale, _, pack_locale in LOCALES[1:]:
            value = maps[pack_locale].get(key, english_keys.get(key, source))
            out.append(f'<span class="grammar-spelling" data-locale="{locale}" hidden>{html.escape(value, quote=False)}</span>')
        return "".join(out)

    return pattern.sub(layered, code)


def production_block(english: dict[str, str], maps: dict[str, dict[str, str]]) -> str:
    source = (REPO / "static/agents/grammar/productions.md").read_text(encoding="utf-8")
    match = re.search(r"```ebnf\n(.*?)\n```", source, re.DOTALL)
    if not match:
        raise SystemExit("grammar-toggle: production fence missing from agent grammar source")
    code = add_layers(html.escape(match.group(1), quote=False), english, maps)
    return ('<section class="grammar-productions"><h2>Formal productions</h2>'
            '<pre><code class="language-ebnf">' + code + '</code></pre></section>')


def process(page: Path, english: dict[str, str], maps: dict[str, dict[str, str]], productions: str) -> None:
    text = page.read_text(encoding="utf-8")
    if 'id="grammar-locale-en-US"' in text:
        return
    code_pattern = re.compile(r'(<pre><code\b[^>]*>)(.*?)(</code></pre>)', re.DOTALL)
    text = code_pattern.sub(lambda m: m.group(1) + add_layers(m.group(2), english, maps) + m.group(3), text)
    heading = re.search(r"<h1(?:\s[^>]*)?>.*?</h1>", text, re.DOTALL)
    if not heading:
        raise SystemExit(f"grammar-toggle: grammar heading missing from {page}")
    controls = ['<fieldset class="grammar-toggle"><legend>Keyword spelling</legend>']
    for index, (locale, label, _) in enumerate(LOCALES):
        checked = " checked" if index == 0 else ""
        controls.append(f'<label><input type="radio" name="grammar-locale" id="grammar-locale-{locale}"{checked}> {label}</label>')
    controls.append("</fieldset>")
    text = text[:heading.end()] + "".join(controls) + text[heading.end():]
    if page.name == "grammar.html":
        text = text.replace("</main>", productions + "</main>", 1)
    page.write_text(text, encoding="utf-8")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: grammar-toggle.py <rendered-grammar-page-or-directory>")
    target = Path(sys.argv[1])
    pages = sorted(target.glob("**/*.html")) if target.is_dir() else [target]
    pages = [p for p in pages if p.name == "grammar.html" or p.parent.name == "grammar"]
    if not pages:
        raise SystemExit(f"grammar-toggle: no grammar HTML pages under {target}")
    english = tables("en")
    maps = {pack: tables(pack) for _, _, pack in LOCALES[1:]}
    productions = production_block(english, maps)
    for page in pages:
        process(page, english, maps, productions)


if __name__ == "__main__":
    main()
