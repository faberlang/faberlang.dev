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


def replace_in_text_nodes(html: str, search: str, replace: str) -> tuple[str, int]:
    """Replace ``search`` with ``replace`` only outside HTML tags/attributes.

    Prevents path segments like ``/start/install.html`` from being mangled when
    chrome labels share words with URL slugs (e.g. ``install``).
    """
    if not search or search not in html:
        return html, 0
    parts = re.split(r"(<[^>]+>)", html)
    count = 0
    out: list[str] = []
    for part in parts:
        if part.startswith("<"):
            out.append(part)
            continue
        n = part.count(search)
        if n:
            part = part.replace(search, replace)
            count += n
        out.append(part)
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


def apply_replacements_to_chrome(html: str, replacements: list[tuple[str, str]]) -> tuple[str, int]:
    """Apply string replacements only inside chrome regions of the document."""
    total = 0

    def _sub(match: re.Match[str]) -> str:
        nonlocal total
        chunk = match.group(0)
        for search, replace in replacements:
            chunk, n = replace_in_text_nodes(chunk, search, replace)
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
    replacements: list[tuple[str, str]] = []
    for key, en_value in en_chrome.items():
        locale_value = locale_chrome.get(key)
        if locale_value is None or locale_value == en_value:
            continue
        # HTML-escape for matching against rendered HTML
        escaped_en = html_mod.escape(en_value, quote=False)
        escaped_locale = html_mod.escape(locale_value, quote=False)
        replacements.append((escaped_en, escaped_locale))

    # Sort by search string length descending to replace longer strings first
    # This prevents partial clobber (e.g. "Install" replacing inside "Install &amp; download")
    replacements.sort(key=lambda r: len(r[0]), reverse=True)

    if not replacements:
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

            html, count = apply_replacements_to_chrome(html, replacements)
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
