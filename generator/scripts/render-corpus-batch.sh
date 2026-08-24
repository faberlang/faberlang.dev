#!/usr/bin/env bash
# Render all canonical corpus term pages, aliases, category indexes, and the corpus hub.
#
# The shell/Python wrapper owns filesystem traversal and batch orchestration. The
# Faber generator owns term-page Markdown/HTML rendering and alias bridge HTML.
#
# Usage:
#   render-corpus-batch.sh <output-dir> <site_locale> <reader_locale> [stylesheet]
#
# Environment:
#   PROOF_DIR=<dir>  also write generated term Markdown for fence validation

set -euo pipefail

GENERATOR_DIR="$(cd "$(dirname "$0")/.." && pwd)"
REPO_DIR="$(cd "$GENERATOR_DIR/.." && pwd)"
WORKSPACE_DIR="$(cd "$REPO_DIR/.." && pwd)"
CORPUS_DIR="${WORKSPACE_DIR}/radix/corpus"
if [ ! -d "$CORPUS_DIR" ] && [ -d "${WORKSPACE_DIR}/../radix/corpus" ]; then
    WORKSPACE_DIR="$(cd "$WORKSPACE_DIR/.." && pwd)"
    CORPUS_DIR="${WORKSPACE_DIR}/radix/corpus"
fi
BUILD_DIR="${GENERATOR_DIR}/target/faber"
FABER="${FABER:-faber}"

OUTPUT_DIR="${1:-${REPO_DIR}/dist}"
SITE_LOCALE="${2:-en-US}"
READER_LOCALE="${3:-la}"
STYLESHEET="${4:-/speculum.css}"
PROOF_DIR="${PROOF_DIR:-}"

if [ ! -d "$CORPUS_DIR" ]; then
    echo "ERROR: corpus directory not found: $CORPUS_DIR" >&2
    exit 1
fi

mkdir -p "$OUTPUT_DIR/corpus"
if [ -n "$PROOF_DIR" ]; then
    rm -rf "$PROOF_DIR"
    mkdir -p "$PROOF_DIR"
fi

# Build the Faber generator once. Corpus mode and file reads live in the
# generated CLI via norma:solum, so this wrapper only orchestrates traversal.
echo "Building generator for corpus batch..." >&2
"$FABER" build "$GENERATOR_DIR" -t rust 2>/dev/null

# Prefer 3.11+ for tomllib (batch orchestration); fall back to python3.
PYTHON="${PYTHON:-}"
if [ -z "$PYTHON" ]; then
    if command -v python3.11 >/dev/null 2>&1; then
        PYTHON=python3.11
    elif command -v python3.13 >/dev/null 2>&1; then
        PYTHON=python3.13
    else
        PYTHON=python3
    fi
fi

echo "Compiling corpus batch generator..." >&2
(cd "$BUILD_DIR" && cargo build --release --quiet 2>/dev/null)

CORPUS_DIR="$CORPUS_DIR" BUILD_DIR="$BUILD_DIR" OUTPUT_DIR="$OUTPUT_DIR" \
SITE_LOCALE="$SITE_LOCALE" READER_LOCALE="$READER_LOCALE" \
STYLESHEET="$STYLESHEET" PROOF_DIR="$PROOF_DIR" \
GENERATOR_DIR="$GENERATOR_DIR" \
READER_ROOT="${WORKSPACE_DIR}/radix/stdlib/locale" \
"$PYTHON" << 'PYEOF'
import html as html_lib
import json
import os
import re
import subprocess
import sys
try:
    import tomllib
except ModuleNotFoundError:  # Python < 3.11
    import tomli as tomllib  # type: ignore
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(os.environ["GENERATOR_DIR"]) / "scripts"))
from corpus_locale import assign_slugs, load_pack

corpus = Path(os.environ["CORPUS_DIR"])
build = Path(os.environ["BUILD_DIR"])
output = Path(os.environ["OUTPUT_DIR"])
site_locale = os.environ["SITE_LOCALE"]
reader_locale = os.environ["READER_LOCALE"]
stylesheet = os.environ["STYLESHEET"]
proof_dir = os.environ.get("PROOF_DIR")
generator_dir = Path(os.environ["GENERATOR_DIR"])
reader_root = Path(os.environ["READER_ROOT"])
binary = build / "target/release/speculum-gen"

marker = "\n§§CORPUS_RECORD§§\n"
source_marker = "\n§§CORPUS_SOURCE§§\n"
expected_marker = "\n§§CORPUS_EXPECTED§§\n"

def slug(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "uncategorized"

def clean_generated(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.splitlines()) + "\n"

records_by_term = defaultdict(list)
canonical = {}
category_terms = defaultdict(list)

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
        records_by_term[term].append((not fields.get("canonical", False), str(rel), source, expected))
    if fields.get("canonical", False):
        canonical.setdefault(term, fields)

terms = sorted(canonical)
term_set = set(terms)
pack = load_pack(reader_root, reader_locale)
slugs, collisions = assign_slugs(
    [(term, str(canonical[term].get("kind", "keyword"))) for term in terms],
    pack,
)
if collisions:
    for term, wanted, owner in collisions:
        print(
            f"warning: corpus slug {wanted!r} already owned by {owner!r}; "
            f"keeping {term!r} on its identity key",
            file=sys.stderr,
        )
slug_values = set(slugs.values())

for term in terms:
    fields = canonical[term]
    category_terms[fields.get("category", "uncategorized")].append(term)

bundle_dir = build / "corpus-bundles"
bundle_dir.mkdir(parents=True, exist_ok=True)
corpus_out = output / "corpus"
corpus_out.mkdir(parents=True, exist_ok=True)

for term in terms:
    term_slug = slugs[term]
    selected = sorted(records_by_term[term], key=lambda item: (item[0], item[1]))
    bundle = bundle_dir / f"{term}.bundle"
    bundle.write_text(marker.join(path + source_marker + source + expected_marker + expected for _, path, source, expected in selected))
    html_path = corpus_out / f"{term_slug}.html"
    html = subprocess.check_output(
        [str(binary), "--", "--corpus", term, str(bundle), site_locale, reader_locale, stylesheet, term_slug],
        text=True,
    )
    if term_slug != term:
        html = html.replace(f"<title>{term} — Faber</title>", f"<title>{term_slug} — Faber</title>")
        html = html.replace(f"<h1>{term}</h1>", f"<h1>{term_slug}</h1>")
        html = html.replace(f"/corpus/{term}.html", f"/corpus/{term_slug}.html")
        html = html.replace(f'content="{term} — Faber"', f'content="{term_slug} — Faber"')
    html_path.write_text(clean_generated(html))
    if proof_dir:
        proof_path = Path(proof_dir) / f"{term_slug}.md"
        proof_path.parent.mkdir(parents=True, exist_ok=True)
        markdown = subprocess.check_output(
            [str(binary), "--", "--corpus-markdown", term, str(bundle), term_slug],
            text=True,
        )
        proof_path.write_text(markdown)

redirects = {}
skipped_aliases = []
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

written_aliases = set()
for alias, target in sorted(redirects.items()):
    alias_path = corpus_out / f"{alias}.html"
    alias_html = subprocess.check_output(
        [str(binary), "--", "--alias", alias, target, site_locale, stylesheet],
        text=True,
    )
    alias_path.write_text(clean_generated(alias_html))
    written_aliases.add(alias)

if skipped_aliases:
    (build / "corpus-alias-residuals.json").write_text(json.dumps(skipped_aliases, indent=2, sort_keys=True))

# Render category indexes and the corpus hub through the same page generator.
generated_dir = build / "generated-corpus-pages"
generated_dir.mkdir(parents=True, exist_ok=True)

# Helper: fetch native_name from locales.toml
locales_toml_path = generator_dir / "locales.toml"
if locales_toml_path.exists():
    with open(locales_toml_path, "rb") as f:
        locales_data = tomllib.load(f).get("locales", {})
else:
    locales_data = {}

def native_name_for(locale_code: str) -> str:
    entry = locales_data.get(locale_code, {})
    return entry.get("native_name", locale_code)

category_index = []
for category in sorted(category_terms):
    terms_in_category = sorted(category_terms[category])
    category_slug = slug(category)
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
    md.extend(
        f"- [`{slugs[term]}`](/corpus/{slugs[term]}.html)"
        for term in terms_in_category
    )
    source = generated_dir / f"category-{category_slug}.md"
    source.write_text("\n".join(md) + "\n")
    out = corpus_out / "category" / f"{category_slug}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    html = subprocess.check_output([str(binary), "--", "--page", f"corpus/category/{category_slug}", str(source), site_locale, reader_locale, stylesheet], text=True)
    out.write_text(clean_generated(html))
    category_index.append((category, category_slug, len(terms_in_category)))

hub = [
    "+++",
    'title = "Corpus"',
    'section = "corpus"',
    'sources = []',
    "+++",
    "",
    "# Corpus",
    "",
    f"Generated reference pages for {len(terms)} canonical Faber corpus terms.",
    "",
    "## Categories",
    "",
]
hub.extend(f"- [{category}](/corpus/category/{category_slug}.html) — {count} terms" for category, category_slug, count in category_index)
hub.extend(["", "## Terms", ""])
hub.extend(f"- [`{slugs[term]}`](/corpus/{slugs[term]}.html)" for term in terms)
hub_source = generated_dir / "corpus-index.md"
hub_source.write_text("\n".join(hub) + "\n")
hub_html = subprocess.check_output([str(binary), "--", "--page", "corpus/index", str(hub_source), site_locale, reader_locale, stylesheet], text=True)
(corpus_out / "index.html").write_text(clean_generated(hub_html))

# Remap leftover Latin identity hrefs (related links from the Faber
# generator still emit `term`) onto this locale's pack slugs, then drop
# any remaining href whose file was never written.
existing_corpus = set()
for p in corpus_out.rglob("*.html"):
    existing_corpus.add(str(p.relative_to(corpus_out)))

stem_to_slug = {term: slugs[term] for term in terms if slugs[term] != term}

suppress_count = [0]
remap_count = [0]

def _rewrite_corpus_link(m):
    raw = html_lib.unescape(m.group(1))
    label = m.group(2)
    stem = raw[:-5] if raw.endswith(".html") else raw
    slug = stem_to_slug.get(stem)
    if slug:
        remap_count[0] += 1
        new_href = f"/{site_locale}/corpus/{slug}.html"
        new_label = slug if html_lib.unescape(re.sub(r"<[^>]+>", "", label)) == stem else label
        return f'<a href="{new_href}">{new_label}</a>'
    target = raw if raw.endswith(".html") else raw + ".html"
    if target not in existing_corpus:
        suppress_count[0] += 1
        return label
    return m.group(0)

# Generator prefixes content paths: /{site_locale}/corpus/…
corpus_href_re = re.compile(
    rf'<a [^>]*href="/{re.escape(site_locale)}/corpus/([^"]+)"[^>]*>(.*?)</a>'
)
for p in corpus_out.rglob("*.html"):
    page_html = p.read_text()
    page_html = corpus_href_re.sub(_rewrite_corpus_link, page_html)
    p.write_text(page_html)

# --- Inject Translation status notice on locale corpus pages ---
# Portal/start pages get their notice from authored Markdown. Corpus pages
# are generated; inject a notice for non-la locales so readers know the
# term names follow the pack while supporting prose may still be English.
notice_count = 0
if reader_locale != "la":
    lang_name = native_name_for(site_locale)
    notice = (
        f'<p><strong>Translation status:</strong> {lang_name} reader-locale proof. '
        f'Term names and code fences follow the <code>{reader_locale}</code> pack; '
        f'supporting prose may still be English.</p>'
    )
    for p in corpus_out.rglob("*.html"):
        html = p.read_text()
        if "translation status" in html.lower():
            continue
        html = re.sub(r'(<main><h1[^>]*>.*?</h1>)(<div class="content")', r'\1' + notice + r'\2', html, count=1)
        p.write_text(html)
        notice_count += 1

manifest = {
    "terms": len(terms),
    "localized_slugs": sum(1 for term in terms if slugs[term] != term),
    "aliases": len(written_aliases),
    "alias_residuals": len(skipped_aliases),
    "categories": len(category_terms),
    "hrefs_remapped": remap_count[0],
    "dead_links_suppressed": suppress_count[0],
    "locale_notices_injected": notice_count,
    "slug_collisions": len(collisions),
}
print(json.dumps(manifest, sort_keys=True))
PYEOF
