#!/usr/bin/env python3
"""
inject-toc.py — Per-page contents rail and heading self-links.

Adds two things to every rendered page that is long enough to need them:

  1. ``<nav class="toc">`` after ``</main>`` — a sticky list of the page's own
     h2/h3 headings. The stylesheet gives it the third grid column, which is
     what keeps the prose column at a readable measure on wide screens
     instead of stretching the text across the whole viewport.
  2. A quiet ``#`` self-link inside each heading that already carries an id.

The rail's label comes from the page's own locale chrome (``[toc].heading``);
a locale without that key gets an unlabelled rail rather than English text,
so this cannot leak untranslated chrome into a locale tree.

Idempotent: pages that already carry a rail are left alone.

Usage:
    inject-toc.py <dist_dir>

Requires Python 3.11+ (uses tomllib).
"""

from __future__ import annotations

import html as html_mod
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
GENERATOR_DIR = SCRIPT_DIR.parent

# A page needs at least this many headings before a rail earns its column.
MIN_HEADINGS = 3

MAIN_RE = re.compile(r"<main\b[^>]*>(.*?)</main>", re.S)
HEADING_RE = re.compile(r"<(h2|h3|h4)\b([^>]*)>(.*?)</\1>", re.S)
ID_RE = re.compile(r'\bid="([^"]+)"')
BODY_RE = re.compile(r"<body\b([^>]*)>")
CLASS_RE = re.compile(r'class="([^"]*)"')
TAG_RE = re.compile(r"<[^>]+>")

# Headings listed in the rail. h4 gets an id and a self-link but no entry.
RAIL_LEVELS = ("h2", "h3")


def load_toc_heading(locale: str) -> str | None:
    """Locale's contents-rail label, or None when it has no translation."""
    import tomllib

    path = GENERATOR_DIR / "locales" / locale / "chrome.toml"
    if not path.is_file():
        return None
    with open(path, "rb") as handle:
        data = tomllib.load(handle)
    heading = data.get("toc", {}).get("heading")
    return heading if isinstance(heading, str) and heading.strip() else None


def heading_text(inner: str) -> str:
    """Visible text of a heading, with markup and self-links removed."""
    inner = re.sub(r'<a class="anchor".*?</a>', "", inner, flags=re.S)
    return html_mod.escape(html_mod.unescape(TAG_RE.sub("", inner)).strip(), quote=False)


def add_body_class(html: str, name: str) -> str:
    match = BODY_RE.search(html)
    if not match:
        return html
    attrs = match.group(1)
    class_match = CLASS_RE.search(attrs)
    if class_match:
        classes = class_match.group(1).split()
        if name in classes:
            return html
        classes.append(name)
        new_attrs = CLASS_RE.sub(f'class="{" ".join(classes)}"', attrs, count=1)
    else:
        new_attrs = f'{attrs} class="{name}"'
    return html[: match.start()] + f"<body{new_attrs}>" + html[match.end() :]


def slugify(text: str, taken: set[str]) -> str:
    """GitHub-style slug for a heading, unique within the page.

    The generator only emits an id when the Markdown spells one out as
    ``{#anchor}``, so most headings arrive without one and cannot be linked
    to. Deriving the rest here keeps every heading addressable; explicit
    anchors are never touched, so existing links stay valid.
    """
    slug = re.sub(r"[^\w\s-]", "", text.lower(), flags=re.UNICODE).strip()
    slug = re.sub(r"[\s_]+", "-", slug).strip("-") or "section"
    candidate = slug
    suffix = 2
    while candidate in taken:
        candidate = f"{slug}-{suffix}"
        suffix += 1
    taken.add(candidate)
    return candidate


def anchor_headings(main_html: str) -> tuple[str, list[tuple[str, str, str]]]:
    """Give every heading an id and a self-link; report the rail entries."""
    taken = set(ID_RE.findall(main_html))
    collected: list[tuple[str, str, str]] = []

    def rewrite(match: re.Match) -> str:
        tag, attrs, inner = match.group(1), match.group(2), match.group(3)
        text = heading_text(inner)
        if not text:
            return match.group(0)

        id_match = ID_RE.search(attrs)
        if id_match:
            ident = id_match.group(1)
            new_attrs = attrs
        else:
            ident = slugify(html_mod.unescape(text), taken)
            new_attrs = f'{attrs} id="{ident}"'

        if tag in RAIL_LEVELS:
            collected.append((tag, ident, text))

        if 'class="anchor"' in inner:
            return f"<{tag}{new_attrs}>{inner}</{tag}>"
        anchor = f'<a class="anchor" href="#{ident}">#</a>'
        return f"<{tag}{new_attrs}>{inner}{anchor}</{tag}>"

    return HEADING_RE.sub(rewrite, main_html), collected


def build_rail(headings: list[tuple[str, str, str]], label: str | None) -> str:
    items = []
    for tag, ident, text in headings:
        level = "toc-2" if tag == "h2" else "toc-3"
        items.append(f'<li class="{level}"><a href="#{ident}">{text}</a></li>')
    if label:
        head = f'<div class="toc-h" id="toc-label">{html_mod.escape(label, quote=False)}</div>'
        open_tag = '<nav class="toc" aria-labelledby="toc-label">'
    else:
        head = '<div class="toc-h" aria-hidden="true"></div>'
        open_tag = '<nav class="toc">'
    return (
        f"{open_tag}{head}"
        f'<div class="toc-body"><ul>{"".join(items)}</ul></div>'
        "</nav>"
    )


def locale_of(page: Path, dist: Path) -> str | None:
    try:
        parts = page.relative_to(dist).parts
    except ValueError:
        return None
    return parts[0] if len(parts) > 1 else None


def process(page: Path, dist: Path, labels: dict[str, str | None]) -> bool:
    html = page.read_text(encoding="utf-8")
    if 'class="toc"' in html:
        return False

    # Standalone chrome pages (landing, portal) are not documentation: they
    # carry their own navigation and their headings are copy, not section
    # anchors. Heading '#' self-links and a contents rail only add noise.
    if re.search(r'<body class="(?:landing|porta)\b', html):
        return False

    main_match = MAIN_RE.search(html)
    if not main_match:
        return False

    main_html = main_match.group(1)
    linked_main, headings = anchor_headings(main_html)
    updated = html[: main_match.start(1)] + linked_main + html[main_match.end(1) :]

    if len(headings) >= MIN_HEADINGS:
        locale = locale_of(page, dist)
        label = labels.get(locale) if locale else None
        rail = build_rail(headings, label)
        end = updated.index("</main>") + len("</main>")
        updated = updated[:end] + rail + updated[end:]
        updated = add_body_class(updated, "has-toc")

    if updated == html:
        return False
    page.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: inject-toc.py <dist_dir>", file=sys.stderr)
        return 1

    dist = Path(sys.argv[1])
    if not dist.is_dir():
        print(f"ERROR: not a directory: {dist}", file=sys.stderr)
        return 1

    labels: dict[str, str | None] = {}
    for locale_dir in sorted((GENERATOR_DIR / "locales").glob("*/")):
        labels[locale_dir.name] = load_toc_heading(locale_dir.name)

    touched = sum(process(page, dist, labels) for page in sorted(dist.rglob("*.html")))
    print(f"  [toc] {touched} page(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
