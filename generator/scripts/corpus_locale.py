#!/usr/bin/env python3
"""Map Latin corpus identity keys to a reader-locale URL slug.

The language corpus stays Latin (`term = "functio"`). Website term pages,
search hrefs, and hub links use the matching reader-pack spelling so each
site locale organizes the corpus the way that locale writes Faber.

Keyword pages prefer `[keywords]`, then `[types]`. Type pages do the reverse.
That keeps `nihil` (kind=keyword) at English `null` rather than the type
disambiguator `null_ty`.

If two terms want the same slug, the earlier identity (sorted) keeps it and
the other stays on its Latin key so we never overwrite a real page.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 fallback
    import tomli as tomllib  # type: ignore


def default_reader_root() -> Path:
    """Locate the workspace `radix/stdlib/locale` checkout."""
    configured = os.environ.get("FABER_LIBRARY_HOME")
    if configured:
        candidate = Path(configured) / "radix" / "stdlib" / "locale"
        if candidate.is_dir():
            return candidate
    for parent in Path(__file__).resolve().parents:
        candidate = parent / "radix" / "stdlib" / "locale"
        if candidate.is_dir():
            return candidate
    return Path(__file__).resolve().parents[3] / "radix" / "stdlib" / "locale"


def load_pack(reader_root: Path, reader_locale: str) -> dict[str, dict[str, str]]:
    """Return `{keywords, types}` maps. Missing pack → empty tables."""
    pack_path = reader_root / reader_locale / "pack.toml"
    if not pack_path.is_file():
        return {"keywords": {}, "types": {}}
    with pack_path.open("rb") as handle:
        data = tomllib.load(handle)
    tables: dict[str, dict[str, str]] = {"keywords": {}, "types": {}}
    for section in tables:
        for latin, native in (data.get(section) or {}).items():
            if isinstance(native, str) and native.strip():
                tables[section][str(latin)] = native.strip()
    return tables


def display_slug(term: str, kind: str, pack: dict[str, dict[str, str]]) -> str:
    """Localized filename stem for one identity key, or the key itself."""
    keywords = pack.get("keywords", {})
    types = pack.get("types", {})
    if (kind or "").lower() == "type":
        primary, secondary = types, keywords
    else:
        primary, secondary = keywords, types
    for table in (primary, secondary):
        native = table.get(term)
        if native:
            return native
    return term


def assign_slugs(
    entries: list[tuple[str, str]],
    pack: dict[str, dict[str, str]],
) -> tuple[dict[str, str], list[tuple[str, str, str]]]:
    """Return `{latin: slug}` and collision triples `(term, wanted, owner)`."""
    wanted = {term: display_slug(term, kind, pack) for term, kind in entries}
    taken: dict[str, str] = {}
    slugs: dict[str, str] = {}
    collisions: list[tuple[str, str, str]] = []
    for term in sorted(wanted):
        slug = wanted[term]
        owner = taken.get(slug)
        if owner is None:
            taken[slug] = term
            slugs[term] = slug
        elif owner == term:
            slugs[term] = slug
        else:
            collisions.append((term, slug, owner))
            slugs[term] = term
    return slugs, collisions
