#!/usr/bin/env python3
"""Curated-corpus IA helpers for render-corpus-batch.sh.

Owns the human-navigation passes the corpus batch applies around the Faber
generator's term pages (site-ia-rework unit 3, corpus half):

  * curated taxonomy   — mechanical `category` tags → corpus-categories.toml
  * term anatomy       — breadcrumb (Corpus › bucket › term) plus a one-line
                         semantics sentence sourced from `faber explain`
  * bucket pages       — /corpus/bucket/<key>.html linked from the hub
  * A–Z index          — /corpus/az.html with per-letter anchors

The generator (html.fab) is untouched: everything here post-processes
rendered HTML or emits generated Markdown the generator renders as a page.
"""

from __future__ import annotations

import html as html_lib
import os
import re
import shutil
import subprocess
import tomllib
from dataclasses import dataclass
from pathlib import Path


class CorpusTaxonomyError(RuntimeError):
    """The curated taxonomy file is malformed or contradictory."""


@dataclass(frozen=True)
class Bucket:
    key: str
    label: str
    blurb: str
    tags: tuple[str, ...]
    catchall: bool = False


def load_buckets(generator_dir: Path) -> list[Bucket]:
    """Parse and validate generator/corpus-categories.toml (hub order)."""
    path = generator_dir / "corpus-categories.toml"
    with open(path, "rb") as handle:
        data = tomllib.load(handle)
    buckets = [
        Bucket(
            key=str(entry["key"]),
            label=str(entry["label"]),
            blurb=str(entry.get("blurb", "")),
            tags=tuple(str(tag) for tag in entry.get("tags", ())),
            catchall=bool(entry.get("catchall", False)),
        )
        for entry in data.get("bucket", ())
    ]
    if not buckets:
        raise CorpusTaxonomyError(f"{path}: no [[bucket]] entries")
    seen: dict[str, str] = {}
    for bucket in buckets:
        if bucket.catchall and bucket.tags:
            raise CorpusTaxonomyError(
                f"{path}: catch-all bucket {bucket.key!r} must list no tags"
            )
        for tag in bucket.tags:
            if tag in seen:
                raise CorpusTaxonomyError(
                    f"{path}: tag {tag!r} mapped to both {seen[tag]!r} and {bucket.key!r}"
                )
            seen[tag] = bucket.key
    if sum(1 for bucket in buckets if bucket.catchall) != 1:
        raise CorpusTaxonomyError(f"{path}: exactly one catch-all bucket required")
    return buckets


def bucket_for(tag: str, buckets: list[Bucket]) -> Bucket:
    """The curated bucket for a mechanical tag; unmapped tags hit catch-all."""
    for bucket in buckets:
        if tag in bucket.tags:
            return bucket
    return next(bucket for bucket in buckets if bucket.catchall)


def resolve_faber(radix_dir: Path) -> str:
    """A faber binary for convert/explain: radix workspace build, then PATH.

    Debug first: it parses the current corpus and resolves the reference
    pack, which the release build on this machine does not (stale parser).
    An installed `faber` carries neither corpus reference nor reader packs,
    so letting it win silently degrades the transcode to token projection
    and empties the semantics source.
    """
    for build in ("debug", "release"):
        candidate = radix_dir / "target" / build / "faber"
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)
    found = shutil.which("faber")
    if not found:
        raise CorpusTaxonomyError("no faber binary found for corpus IA passes")
    return found


def stage_reader_packs(faber: str, radix_dir: Path) -> tuple[bool, str]:
    """Make reader packs resolvable beside the faber binary.

    `faber convert` looks for share/faber/locale/<X>/pack.toml relative to
    its own executable; a workspace build has no such directory. Symlink the
    radix packs into place. Writes only inside radix/target/, which is build
    output. Same staging locale-tabs.py performs for its own panels.
    """
    src = radix_dir / "locale"
    if not src.is_dir():
        return False, ""
    dest = Path(faber).resolve().parent.parent / "share" / "faber" / "locale"
    dest.mkdir(parents=True, exist_ok=True)
    linked = 0
    for pack in sorted(src.iterdir()):
        if not (pack / "pack.toml").is_file():
            continue
        link = dest / pack.name
        if not link.exists():
            link.symlink_to(pack, target_is_directory=True)
        linked += 1
    return linked > 0, str(dest)


def load_explain_semantics(faber: str) -> dict[str, dict[str, str]]:
    """`term → {category, summary}` from one `faber explain --list` call.

    The registry derives from the same corpus the batch renders but does not
    cover every canonical term; callers omit the semantics line for absent
    terms — never invent one. Same parsing as the agent reference tree.
    """
    try:
        result = subprocess.run(
            [faber, "explain", "--list"], capture_output=True, text=True, timeout=120
        )
    except (OSError, subprocess.TimeoutExpired):
        return {}
    if result.returncode != 0:
        return {}
    from agent_reference import parse_list

    _, entries = parse_list(result.stdout)
    registry: dict[str, dict[str, str]] = {}
    for entry in entries:
        registry.setdefault(
            entry["term"], {"category": entry["category"], "summary": entry["summary"]}
        )
    return registry


def breadcrumb_html(trail: list[tuple[str, str | None]]) -> str:
    """`<nav class="breadcrumb">` from `(label, href)` pairs; last href None."""
    parts = []
    for label, href in trail:
        text = html_lib.escape(label)
        parts.append(f'<a href="{html_lib.escape(href, quote=True)}">{text}</a>' if href else text)
    return f'<nav class="breadcrumb" aria-label="Breadcrumb">{" &rsaquo; ".join(parts)}</nav>'


def semantics_html(text: str) -> str:
    return f'<p class="term-semantics">{html_lib.escape(text)}</p>'


def apply_anatomy(page_html: str, crumb: str, semantics: str) -> str:
    """Insert the breadcrumb after `<main>` and the semantics line after `</h1>`.

    Must run as the LAST corpus post-process: the translation-notice pass
    matches `</h1><div class="content"` on term pages, and both insertions
    would break that match.
    """
    if crumb:
        page_html = re.sub(r"(<main[^>]*>)", r"\1" + crumb.replace("\\", "\\\\"), page_html, count=1)
    if semantics:
        page_html = page_html.replace("</h1>", "</h1>" + semantics, 1)
    return page_html


def az_markdown(slugs: list[str]) -> str:
    """A–Z index Markdown: every term page under per-letter anchors."""
    groups: dict[str, list[str]] = {}
    for term_slug in slugs:
        first = term_slug[:1].upper()
        letter = first if first.isalpha() and first.isascii() else "Symbols"
        groups.setdefault(letter, []).append(term_slug)
    letters = sorted((l for l in groups if l != "Symbols")) + (
        ["Symbols"] if "Symbols" in groups else []
    )
    anchor = lambda letter: f"letter-{letter.lower()}"
    lines = [
        "+++",
        'title = "Corpus A–Z"',
        'section = "corpus"',
        "sources = []",
        "+++",
        "",
        "# Corpus A–Z",
        "",
        f"Every one of the {len(slugs)} Faber corpus term pages, alphabetical. "
        "The concept path lives on the [corpus hub](/corpus/index.html); this is the flat one.",
        "",
        " ".join(f"[{letter}](#{anchor(letter)})" for letter in letters),
        "",
    ]
    for letter in letters:
        lines.append(f"## {letter} {{#{anchor(letter)}}}")
        lines.append("")
        lines.extend(f"- [`{s}`](/corpus/{s}.html)" for s in groups[letter])
        lines.append("")
    return "\n".join(lines).rstrip("\n") + "\n"


def bucket_markdown(bucket: Bucket, term_slugs: list[str]) -> str:
    """One curated bucket page: blurb plus its term links."""
    lines = [
        "+++",
        f'title = "Corpus: {bucket.label}"',
        'section = "corpus"',
        "sources = []",
        "+++",
        "",
        f"# Corpus: {bucket.label}",
        "",
    ]
    if bucket.blurb:
        lines.append(f"{bucket.blurb} {len(term_slugs)} canonical terms.")
        lines.append("")
    lines.extend(f"- [`{s}`](/corpus/{s}.html)" for s in term_slugs)
    return "\n".join(lines) + "\n"


def hub_markdown(
    buckets: list[Bucket], counts: dict[str, int], total_terms: int
) -> str:
    """Corpus hub Markdown: curated buckets plus the A–Z index, nothing else."""
    lines = [
        "+++",
        'title = "Corpus"',
        'section = "corpus"',
        "sources = []",
        "+++",
        "",
        "# Corpus",
        "",
        f"Reference pages for {total_terms} canonical Faber corpus terms. "
        "Browse by concept below, or take the flat "
        "[A–Z index](/corpus/az.html).",
        "",
    ]
    for bucket in buckets:
        count = counts.get(bucket.key, 0)
        lines.append(
            f"- [{bucket.label}](/corpus/bucket/{bucket.key}.html) — {count} terms. "
            f"{bucket.blurb}"
        )
    return "\n".join(lines) + "\n"
