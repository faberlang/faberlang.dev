#!/usr/bin/env python3
"""
generate-sitemap — Generate sitemap.xml from dist/ HTML pages.

Emits ``dist/sitemap.xml``: the portal root, then every HTML page under each
locale directory, in lexicographic order. Locale discovery reads the
directory set under ``src/`` (the registry comment in
``generator/locales.toml``: dir presence under src/ still discovers
locales). Redirect stubs (retired paths carrying a meta refresh + noindex)
are skipped; so is any 404.html.

This is the Python restoration of the native-Faber gate (NSM Wave-2 F1):
radix core-norma N2 retired the I/O kernel modules from script mode, so the
staged `.fab` gate can no longer run. Byte-stable with the `.fab` behavior
it replaces (stub skip, src/-based locale discovery, portal-first order).

Usage:
    generate-sitemap [dist_dir] [base_url]

Exit contract: 0 on success, 2 when <dist_dir> is not a directory.
"""

from __future__ import annotations

import sys
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape as xml_escape_sax


def loc_for(file: Path, locale_root: Path, locale: str, base: str) -> str | None:
    """Map a file under dist/{locale}/ to an absolute sitemap loc."""
    if file.name == "404.html":
        return None
    # Corpus terms put spaces and `<>` in file names; the URL carries them
    # percent-encoded (`quote` leaves `/` and unreserved characters alone).
    rel = quote(file.relative_to(locale_root).as_posix(), safe="/")
    if rel == "index.html":
        return f"{base}/{locale}/"
    if rel.endswith("/index.html"):
        dir_part = rel[: -len("index.html")]
        return f"{base}/{locale}/{dir_part}"
    return f"{base}/{locale}/{rel}"


def main(argv: list[str]) -> int:
    dist = Path(argv[1]) if len(argv) > 1 else Path("dist")
    base = argv[2] if len(argv) > 2 else "https://faberlang.dev"
    base = base.rstrip("/")

    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2

    # Locale discovery mirrors the .fab gate: the directory set under src/.
    src_root = Path(__file__).resolve().parents[2] / "src"
    all_locales = sorted(p.name for p in src_root.iterdir() if p.is_dir()) \
        if src_root.is_dir() else []

    urls: list[str] = [f"{base}/"]
    for locale in all_locales:
        locale_root = dist / locale
        if not locale_root.is_dir():
            continue
        for page in sorted(locale_root.rglob("*.html")):
            # Redirect stubs (retired paths) carry noindex; listing them in
            # the sitemap tells crawlers to index a page that asks not to be
            # indexed. Skip anything that meta-refreshes away.
            try:
                head = page.read_text(encoding="utf-8", errors="replace")[:1024]
            except OSError:
                continue
            if 'http-equiv="refresh"' in head or "http-equiv='refresh'" in head:
                continue
            loc = loc_for(page, locale_root, locale, base)
            if loc:
                urls.append(loc)

    # Stable order: portal first, then lexicographic unique rest.
    portal = f"{base}/"
    rest_urls: list[str] = []
    prev = ""
    for url in sorted(urls):
        if url == portal:
            continue
        if url == prev:
            continue
        rest_urls.append(url)
        prev = url

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += f"  <url><loc>{xml_escape_sax(portal)}</loc></url>\n"
    for url in rest_urls:
        xml += f"  <url><loc>{xml_escape_sax(url)}</loc></url>\n"
    xml += "</urlset>\n"
    (dist / "sitemap.xml").write_text(xml, encoding="utf-8")
    print(
        f"Generated {dist}/sitemap.xml: {len(rest_urls) + 1} URLs "
        f"({len(all_locales)} locales + portal)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
