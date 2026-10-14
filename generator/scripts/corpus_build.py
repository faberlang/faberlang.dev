"""Corpus term pages, alias redirects, category/bucket/A-Z indexes and the hub.

This is the batch that used to live in `render-corpus-batch.sh`. It renders
in-process (`speculum_py` is imported, not spawned per term) and reads the
`faber explain --list` registry from the committed snapshot rather than from
whatever binary happens to be installed. Conversions go through the cached
`localize.Converter`; a record already written in the reader locale is never
sent to the compiler, and a conversion that fails is a recorded degradation.

Output is the corpus tree under `<output>/corpus/`, post-processed the way the
old batch did (link remap, translation notice, anatomy), ready for the
presentation passes in `build.py`.
"""
from __future__ import annotations

import html as html_lib
import json
import re
import sys
import tomllib
from collections import defaultdict
from pathlib import Path

import corpus_ia
import receipt
import speculum_py
from corpus_locale import assign_slugs, load_pack
from localize import Converter
from project_reader_terms import load_mapping, project_code, project_prose

MARKER = "\n§§CORPUS_RECORD§§\n"
SOURCE_MARKER = "\n§§CORPUS_SOURCE§§\n"
EXPECTED_MARKER = "\n§§CORPUS_EXPECTED§§\n"
CORPUS_HREF = "{site}/corpus/"


def _slug(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "uncategorized"


def _clean_generated(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.splitlines()) + "\n"


def _as_subprocess_text(output: str) -> str:
    """Match what a captured child process used to hand back: text plus a
    newline, with universal-newline translation."""
    return (output + "\n").replace("\r\n", "\n").replace("\r", "\n")


def _record_locale(front: str) -> str:
    """A record's own source locale: its `locale` field, else the product default."""
    match = re.search(r'(?m)^locale\s*=\s*"([^"]+)"\s*$', front)
    return match.group(1) if match else "en"


def _record_kind(front: str) -> str:
    match = re.search(r'(?m)^kind\s*=\s*"([^"]+)"\s*$', front)
    return match.group(1) if match else ""


def project_record(source: str, mapping: dict[str, str], reader: str,
                   converter: Converter | None, label: str) -> str:
    """Convert/project one corpus record without changing identity or path fields."""
    parts = source.split("+++", 2)
    if len(parts) != 3:
        return source
    front, body = parts[1], parts[2]
    # A rejection exemplar is source the compiler refuses by design, so it can
    # never convert; it is projected token-wise like any other uncompilable text.
    if reader != "la" and converter is not None and _record_kind(front) != "reject":
        own = _record_locale(front)
        if own != reader:
            converted = converter.convert(body.lstrip("\n"), own, label, "corpus-convert")
            if converted is not None:
                body = converted

    def value_replace(match: re.Match) -> str:
        key, quote, value = match.group(1), match.group(2), match.group(3)
        if key == "syntax":
            value = project_code(value, mapping)
        else:
            value = project_prose(value, mapping)
        return f"{key} = {quote}{value}{quote}"

    front = re.sub(r'(?m)^(summary|syntax)\s*=\s*(["\'])(.*?)\2\s*$', value_replace, front)
    return "+++" + front + "+++\n" + project_code(body, mapping)


def build(*, corpus: Path, reader_root: Path, output: Path, generator_dir: Path,
          site_locale: str, reader_locale: str, stylesheet: str,
          explain_text: str, converter: Converter | None) -> dict:
    """Render the whole corpus tree into `<output>/corpus`; return its manifest."""
    records_by_term: dict[str, list] = defaultdict(list)
    canonical: dict[str, dict] = {}
    category_terms: dict[str, list] = defaultdict(list)

    for path in sorted(corpus.rglob("*.fab")):
        source = path.read_text()
        parts = source.split("+++", 2)
        if len(parts) != 3:
            continue
        fields = tomllib.loads(parts[1])
        term = fields.get("term")
        if not term:
            continue
        include = bool(fields.get("canonical", False)) or fields.get("kind") == "reject"
        if include:
            expected_path = path.with_suffix(".expected")
            expected = expected_path.read_text() if expected_path.exists() else ""
            rel = path.relative_to(corpus.parent.parent)
            records_by_term[term].append(
                (not fields.get("canonical", False), str(rel), source, expected)
            )
        if fields.get("canonical", False):
            canonical.setdefault(term, fields)

    terms = sorted(canonical)
    term_set = set(terms)
    pack = load_pack(reader_root, reader_locale)
    term_mapping = (
        load_mapping(reader_root / reader_locale / "pack.toml") if reader_locale != "la" else {}
    )
    explain_registry: dict[str, dict[str, str]] = {}
    from agent_reference import parse_list

    _, entries = parse_list(explain_text)
    for entry in entries:
        explain_registry.setdefault(
            entry["term"], {"category": entry["category"], "summary": entry["summary"]}
        )
    buckets = corpus_ia.load_buckets(generator_dir)
    term_bucket = {}
    slugs, collisions = assign_slugs(
        [(term, str(canonical[term].get("kind", "keyword"))) for term in terms],
        pack,
    )
    for term, wanted, owner in collisions:
        receipt.degraded(
            "corpus-slug-collision", term,
            f"slug {wanted!r} already owned by {owner!r}; kept on its identity key",
        )
    slug_values = set(slugs.values())

    for term in terms:
        fields = canonical[term]
        category_terms[fields.get("category", "uncategorized")].append(term)
        term_bucket[term] = corpus_ia.bucket_for(fields.get("category", "uncategorized"), buckets)

    corpus_out = output / "corpus"
    corpus_out.mkdir(parents=True, exist_ok=True)

    anatomy_payloads: dict[str, tuple[str, str]] = {}
    semantics_added = semantics_duplicate = semantics_missing = 0

    for term in terms:
        term_slug = slugs[term]
        selected = sorted(records_by_term[term], key=lambda item: (item[0], item[1]))
        bundle_records = []
        for _, path, source, expected in selected:
            if reader_locale != "la":
                source = project_record(source, term_mapping, reader_locale, converter, path)
            bundle_records.append(path + SOURCE_MARKER + source + EXPECTED_MARKER + expected)
        bundle = MARKER.join(bundle_records)
        display = term_slug if term_slug.isascii() else ""
        html = _as_subprocess_text(speculum_py.genera_corpus(
            speculum_py.termen_ex_canonica(bundle), bundle,
            site_locale, reader_locale, stylesheet, display,
        ))
        if term_slug != term:
            html = html.replace(f"<title>{term} — Faber</title>", f"<title>{term_slug} — Faber</title>")
            html = html.replace(f"<h1>{term}</h1>", f"<h1>{term_slug}</h1>")
            html = html.replace(f"/corpus/{term}.html", f"/corpus/{term_slug}.html")
            html = html.replace(f'content="{term} — Faber"', f'content="{term_slug} — Faber"')
        (corpus_out / f"{term_slug}.html").write_text(_clean_generated(html))
        bucket = term_bucket[term]
        crumb = corpus_ia.breadcrumb_html([
            ("Corpus", f"/{site_locale}/corpus/index.html"),
            (bucket.label, f"/{site_locale}/corpus/bucket/{bucket.key}.html"),
            (term_slug, None),
        ])
        sem = ""
        verdict = "missing"
        entry = explain_registry.get(term)
        if entry and entry.get("summary", "").strip():
            text = entry["summary"].strip()
            if reader_locale != "la":
                text = project_prose(text, term_mapping)
            if f"<p>{html_lib.escape(text)}</p>" in html:
                verdict = "duplicate"
            else:
                sem = corpus_ia.semantics_html(text)
                verdict = "added"
        anatomy_payloads[term_slug] = (crumb, sem)
        if verdict == "added":
            semantics_added += 1
        elif verdict == "duplicate":
            semantics_duplicate += 1
        else:
            semantics_missing += 1

    redirects: dict[str, str] = {}
    skipped_aliases: list = []
    for term in terms:
        term_slug = slugs[term]
        if term != term_slug:
            redirects[term] = term_slug
        for alias in canonical[term].get("aliases", []):
            if alias == term_slug:
                continue
            if alias in term_set or alias in slug_values:
                skipped_aliases.append((alias, [term], "canonical-term-path"))
                continue
            existing = redirects.get(alias)
            if existing is None:
                redirects[alias] = term_slug
            elif existing != term_slug:
                skipped_aliases.append((alias, [term], f"duplicate-alias-kept:{existing}"))

    written_aliases: set[str] = set()
    for alias, target in sorted(redirects.items()):
        alias_html = _as_subprocess_text(
            speculum_py.genera_alias_redirect(alias, target, site_locale, stylesheet)
        )
        (corpus_out / f"{alias}.html").write_text(_clean_generated(alias_html))
        written_aliases.add(alias)

    if skipped_aliases:
        residuals = generator_dir / "target" / "corpus-alias-residuals.json"
        residuals.parent.mkdir(parents=True, exist_ok=True)
        residuals.write_text(json.dumps(skipped_aliases, indent=2, sort_keys=True))

    # Category indexes and the corpus hub go through the same page generator.
    generated_dir = generator_dir / "target" / "generated-corpus-pages"
    generated_dir.mkdir(parents=True, exist_ok=True)

    def render_page(iter_: str, source_path: Path) -> str:
        source = speculum_py.read_source(str(source_path))
        return _as_subprocess_text(
            speculum_py.genera(source, iter_, site_locale, reader_locale, stylesheet)
        )

    category_index = []
    for category in sorted(category_terms):
        terms_in_category = sorted(category_terms[category])
        category_slug = _slug(category)
        md = [
            "+++",
            f'title = "Corpus: {category}"',
            'section = "corpus"',
            'sources = []',
            "+++",
            "",
            f"# Corpus category: `{category}`",
            "",
            f"{len(terms_in_category)} canonical terms in this category.",
            "",
        ]
        md.extend(f"- [`{slugs[term]}`](/corpus/{slugs[term]}.html)" for term in terms_in_category)
        source = generated_dir / f"category-{category_slug}.md"
        source.write_text("\n".join(md) + "\n")
        out = corpus_out / "category" / f"{category_slug}.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(_clean_generated(render_page(f"corpus/category/{category_slug}", source)))
        category_index.append((category, category_slug, len(terms_in_category)))

    bucket_counts: dict[str, int] = {}
    for term in terms:
        key = term_bucket[term].key
        bucket_counts[key] = bucket_counts.get(key, 0) + 1

    hub_source = generated_dir / "corpus-index.md"
    hub_source.write_text(corpus_ia.hub_markdown(buckets, bucket_counts, len(terms)))
    (corpus_out / "index.html").write_text(
        _clean_generated(render_page("corpus/index", hub_source))
    )

    bucket_dir = corpus_out / "bucket"
    bucket_dir.mkdir(parents=True, exist_ok=True)
    extra_crumbs = []
    for bucket in buckets:
        members = sorted(
            (term for term in terms if term_bucket[term].key == bucket.key),
            key=lambda t: slugs[t].casefold(),
        )
        source = generated_dir / f"bucket-{bucket.key}.md"
        source.write_text(corpus_ia.bucket_markdown(bucket, [slugs[t] for t in members]))
        out = bucket_dir / f"{bucket.key}.html"
        out.write_text(_clean_generated(render_page(f"corpus/bucket/{bucket.key}", source)))
        extra_crumbs.append((
            out,
            corpus_ia.breadcrumb_html(
                [("Corpus", f"/{site_locale}/corpus/index.html"), (bucket.label, None)]
            ),
        ))

    az_slugs = sorted(set(slugs.values()), key=lambda s: (s.casefold(), s))
    az_source = generated_dir / "corpus-az.md"
    az_source.write_text(corpus_ia.az_markdown(az_slugs))
    az_path = corpus_out / "az.html"
    az_path.write_text(_clean_generated(render_page("corpus/az", az_source)))
    extra_crumbs.append((
        az_path,
        corpus_ia.breadcrumb_html(
            [("Corpus", f"/{site_locale}/corpus/index.html"), ("A–Z", None)]
        ),
    ))

    # Remap leftover Latin identity hrefs onto this locale's pack slugs, then
    # drop any remaining href whose file was never written.
    existing_corpus = {str(p.relative_to(corpus_out)) for p in corpus_out.rglob("*.html")}
    stem_to_slug = {term: slugs[term] for term in terms if slugs[term] != term}
    suppress_count = remap_count = 0

    def rewrite_link(match: re.Match) -> str:
        nonlocal suppress_count, remap_count
        raw = html_lib.unescape(match.group(1))
        label = match.group(2)
        stem = raw[:-5] if raw.endswith(".html") else raw
        slug = stem_to_slug.get(stem)
        if slug:
            remap_count += 1
            new_href = f"/{site_locale}/corpus/{slug}.html"
            new_label = slug if html_lib.unescape(re.sub(r"<[^>]+>", "", label)) == stem else label
            return f'<a href="{new_href}">{new_label}</a>'
        target = raw if raw.endswith(".html") else raw + ".html"
        if target not in existing_corpus:
            suppress_count += 1
            return label
        return match.group(0)

    corpus_href_re = re.compile(
        rf'<a [^>]*href="/{re.escape(site_locale)}/corpus/([^"]+)"[^>]*>(.*?)</a>'
    )
    for p in corpus_out.rglob("*.html"):
        p.write_text(corpus_href_re.sub(rewrite_link, p.read_text()))

    # Translation-status notice on locale corpus pages.
    notice_count = 0
    if reader_locale != "la":
        locales_toml = generator_dir / "locales.toml"
        locales_data = {}
        if locales_toml.exists():
            with locales_toml.open("rb") as handle:
                locales_data = tomllib.load(handle).get("locales", {})
        lang_name = locales_data.get(site_locale, {}).get("native_name", site_locale)
        notice = (
            f'<p><strong>Translation status:</strong> {lang_name} reader-locale proof. '
            f'Term names and code fences follow the <code>{reader_locale}</code> pack; '
            f'supporting prose may still be English.</p>'
        )
        for p in corpus_out.rglob("*.html"):
            page = p.read_text()
            if "translation status" in page.lower():
                continue
            page = re.sub(
                r'(<main><h1[^>]*>.*?</h1>)(<div class="content")',
                r'\1' + notice + r'\2', page, count=1,
            )
            p.write_text(page)
            notice_count += 1

    # Term-page anatomy is deliberately the LAST post-process: the notice pass
    # above matches `</h1><div class="content"`, which the semantics line breaks.
    anatomy_pages = 0
    for term_slug, (crumb, sem) in anatomy_payloads.items():
        page = corpus_out / f"{term_slug}.html"
        if not page.is_file():
            continue
        page.write_text(corpus_ia.apply_anatomy(page.read_text(), crumb, sem))
        anatomy_pages += 1
    for page_path, crumb in extra_crumbs:
        page_path.write_text(corpus_ia.apply_anatomy(page_path.read_text(), crumb, ""))

    return {
        "terms": len(terms),
        "localized_slugs": sum(1 for term in terms if slugs[term] != term),
        "aliases": len(written_aliases),
        "alias_residuals": len(skipped_aliases),
        "categories": len(category_terms),
        "curated_buckets": len(buckets),
        "az_terms": len(az_slugs),
        "anatomy_pages": anatomy_pages,
        "semantics_added": semantics_added,
        "semantics_duplicate": semantics_duplicate,
        "semantics_missing": semantics_missing,
        "hrefs_remapped": remap_count,
        "dead_links_suppressed": suppress_count,
        "locale_notices_injected": notice_count,
        "slug_collisions": len(collisions),
    }
