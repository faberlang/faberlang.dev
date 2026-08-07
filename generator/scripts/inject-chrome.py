#!/usr/bin/env python3
"""
inject-chrome.py — Replace chrome UI strings in rendered HTML with locale values.

Loads generator/locales/{locale}/chrome.toml and generator/locales/en-US/chrome.toml.
Walks dist/{locale}/**/*.html, replacing English UI strings with locale values
for any key where the values differ.

Usage:
    inject-chrome.py <dist_dir> <locale>

Requires Python 3.11+ (uses tomllib).
"""

import html as html_mod
import os
import re
import sys
from pathlib import Path


def load_chrome(chrome_path: Path) -> dict[str, str]:
    """Load a chrome.toml and return a flat dict of key → value."""
    import tomllib

    with open(chrome_path, "rb") as f:
        data = tomllib.load(f)

    result: dict[str, str] = {}
    for section, entries in data.items():
        if isinstance(entries, dict):
            for key, value in entries.items():
                if isinstance(value, str):
                    result[f"{section}.{key}"] = value
    return result


def replace_in_text_nodes(html: str, table: dict[str, str]) -> tuple[str, int]:
    """Apply the whole replacement table in ONE pass, outside tags/attributes.

    One pass, not one pass per key. Replacing sequentially lets a short label
    eat a longer one it happens to prefix: with "Target" translated and
    "Target lanes" not, sequential replacement produced a half-Arabic
    "الهدف lanes". A single alternation ordered longest-first consumes the
    longer label before the shorter pattern can see it — which is also why the
    table carries identity entries for labels a locale has not translated.
    They translate to themselves, and in doing so shield themselves.

    Staying outside tags keeps path segments like ``/start/install.html`` from
    being mangled when a label shares a word with a URL slug.
    """
    if not table:
        return html, 0
    pattern = re.compile(
        "|".join(re.escape(k) for k in sorted(table, key=len, reverse=True))
    )
    parts = re.split(r"(<[^>]+>)", html)
    count = 0
    out: list[str] = []
    for part in parts:
        if part.startswith("<"):
            out.append(part)
            continue

        def _one(m: re.Match[str]) -> str:
            nonlocal count
            count += 1
            return table[m.group(0)]

        out.append(pattern.sub(_one, part))
    return "".join(out), count


# Only rewrite chrome chrome regions so English body prose is not clobbered
# (e.g. "Install and download" mid-paragraph while sidebar is localized).
_CHROME_REGIONS = re.compile(
    r"(?is)("
    r"<aside\b[^>]*>.*?</aside>"
    r"|<div class=\"renderbar\"[^>]*>.*?</div>\s*</div>"
    r"|<span class=\"agent-notice-label\"[^>]*>.*?</span>"
    r"|<footer\b[^>]*>.*?</footer>"
    r")"
)


def apply_replacements_to_chrome(html: str, table: dict[str, str]) -> tuple[str, int]:
    """Apply the replacement table only inside chrome regions of the document."""
    total = 0

    def _sub(match: re.Match[str]) -> str:
        nonlocal total
        chunk, n = replace_in_text_nodes(match.group(0), table)
        total += n
        return chunk

    return _CHROME_REGIONS.sub(_sub, html), total


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: inject-chrome.py <dist_dir> <locale>", file=sys.stderr)
        return 1

    dist_dir = Path(sys.argv[1])
    locale = sys.argv[2]

    # Paths
    script_dir = Path(__file__).resolve().parent
    generator_dir = script_dir.parent
    en_chrome_path = generator_dir / "locales" / "en-US" / "chrome.toml"
    locale_chrome_path = generator_dir / "locales" / locale / "chrome.toml"

    if not locale_chrome_path.is_file():
        print(f"  [chrome] No chrome.toml for {locale}, skipping")
        return 0

    # Load chrome
    en_chrome = load_chrome(en_chrome_path)
    locale_chrome = load_chrome(locale_chrome_path)

    # Build replacements: for each key where en value != locale value
    # HTML-escape both search and replacement values to match rendered output
    # Every declared English label enters the table, translated or not. An
    # untranslated one maps to itself, which costs nothing and stops a shorter
    # translated label from being substituted inside it.
    table: dict[str, str] = {}
    translated = 0
    for key, en_value in en_chrome.items():
        escaped_en = html_mod.escape(en_value, quote=False)
        locale_value = locale_chrome.get(key)
        if locale_value is None or locale_value == en_value:
            table.setdefault(escaped_en, escaped_en)
            continue
        table[escaped_en] = html_mod.escape(locale_value, quote=False)
        translated += 1

    if not translated:
        print(f"  [chrome] No differences between en-US and {locale}, nothing to inject")
        return 0

    # Walk HTML files for this locale
    locale_dir = dist_dir / locale
    if not locale_dir.is_dir():
        print(f"  [chrome] {locale_dir} does not exist, skipping")
        return 0

    files_modified = 0
    total_replacements = 0

    for root, _dirs, files in os.walk(locale_dir):
        for name in files:
            if not name.endswith(".html"):
                continue
            path = Path(root) / name
            html = path.read_text(encoding="utf-8")

            html, count = apply_replacements_to_chrome(html, table)
            if count > 0:
                total_replacements += count
                path.write_text(html, encoding="utf-8")
                files_modified += 1

    print(
        f"  [chrome] {locale}: {files_modified} files modified, "
        f"{total_replacements} replacements"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
