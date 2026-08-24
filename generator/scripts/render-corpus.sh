#!/usr/bin/env bash
# Render a bounded corpus term page through the Faber generator.
#
# The wrapper owns traversal and bundle creation. Frontmatter parsing, kind
# policy, Markdown templating, HTML rendering, and bundle reads remain in Faber.
#
# Usage: render-corpus.sh <term> <output.html> [site_locale] [reader_locale] [stylesheet]

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

TERM="${1:-}"
OUTPUT="${2:-}"
SITE_LOCALE="${3:-en-US}"
READER_LOCALE="${4:-la}"
STYLESHEET="${5:-/speculum.css}"
PROOF_MARKDOWN="${PROOF_MARKDOWN:-}"

if [ -z "$TERM" ] || [ -z "$OUTPUT" ]; then
    echo "Usage: render-corpus.sh <term> <output.html> [site_locale] [reader_locale] [stylesheet]" >&2
    exit 1
fi

if [ ! -d "$CORPUS_DIR" ]; then
    echo "ERROR: corpus directory not found: $CORPUS_DIR" >&2
    exit 1
fi

# Build the same generator used by render.sh. Corpus mode and bundle reads live
# in the generated CLI via norma:solum.
echo "Building generator for corpus term $TERM..." >&2
"$FABER" build "$GENERATOR_DIR" -t rust 2>/dev/null

BUNDLE="${BUILD_DIR}/corpus-${TERM}.bundle"
BUNDLE_PATH="$BUNDLE" CORPUS_DIR="$CORPUS_DIR" TERM="$TERM" python3 << 'PYEOF'
import os
import tomllib
from pathlib import Path

corpus = Path(os.environ["CORPUS_DIR"])
term = os.environ["TERM"]
selected = []

for path in sorted(corpus.rglob("*.fab")):
    source = path.read_text()
    parts = source.split("+++", 2)
    if len(parts) != 3:
        continue
    try:
        fields = tomllib.loads(parts[1])
    except tomllib.TOMLDecodeError as error:
        raise SystemExit(f"invalid frontmatter in {path}: {error}")
    if fields.get("term") != term:
        continue
    # A term page is canonical-first. Explicit reject exempla are supporting
    # examples so the page proves the fence outcome contract without treating
    # every historical/smoke fixture as a compile target.
    if not fields.get("canonical", False) and fields.get("kind") != "reject":
        continue
    expected_path = path.with_suffix(".expected")
    expected = expected_path.read_text() if expected_path.exists() else ""
    selected.append((not fields.get("canonical", False), str(path.relative_to(corpus.parent.parent)), source, expected))

if not selected:
    raise SystemExit(f"no canonical or reject corpus examples found for {term!r}")

selected.sort(key=lambda item: (item[0], item[1]))
marker = "\n§§CORPUS_RECORD§§\n"
source_marker = "\n§§CORPUS_SOURCE§§\n"
expected_marker = "\n§§CORPUS_EXPECTED§§\n"
records = []
for _, path, source, expected in selected:
    records.append(path + source_marker + source + expected_marker + expected)
Path(os.environ["BUNDLE_PATH"]).write_text(marker.join(records))
PYEOF

echo "Compiling corpus generator..." >&2
(cd "$BUILD_DIR" && cargo build --release --quiet 2>/dev/null)

mkdir -p "$(dirname "$OUTPUT")"
TERM="$TERM" OUTPUT="$OUTPUT" SITE_LOCALE="$SITE_LOCALE" \
READER_LOCALE="$READER_LOCALE" STYLESHEET="$STYLESHEET" \
PROOF_MARKDOWN="$PROOF_MARKDOWN" BUNDLE="$BUNDLE" \
BIN="${BUILD_DIR}/target/release/speculum-gen" \
GENERATOR_DIR="$GENERATOR_DIR" CORPUS_DIR="$CORPUS_DIR" \
READER_ROOT="${FABER_LIBRARY_HOME:-$WORKSPACE_DIR}/radix/stdlib/locale" \
python3 << 'PYEOF'
import os
import subprocess
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(os.environ["GENERATOR_DIR"]) / "scripts"))
from corpus_locale import display_slug, load_pack

term = os.environ["TERM"]
output = Path(os.environ["OUTPUT"])
site_locale = os.environ["SITE_LOCALE"]
reader_locale = os.environ["READER_LOCALE"]
stylesheet = os.environ["STYLESHEET"]
binary = os.environ["BIN"]
bundle = os.environ["BUNDLE"]
proof = os.environ.get("PROOF_MARKDOWN") or ""
corpus = Path(os.environ["CORPUS_DIR"])
pack = load_pack(Path(os.environ["READER_ROOT"]), reader_locale)

kind = "keyword"
aliases = []
for path in sorted(corpus.rglob("*.fab")):
    source = path.read_text()
    parts = source.split("+++", 2)
    if len(parts) != 3:
        continue
    fields = tomllib.loads(parts[1])
    if fields.get("term") == term and fields.get("canonical", False):
        kind = str(fields.get("kind", "keyword"))
        aliases = fields.get("aliases", [])
        break

slug = display_slug(term, kind, pack)
if output.name == f"{term}.html" and slug != term:
    page_path = output.with_name(f"{slug}.html")
else:
    page_path = output
page_path.parent.mkdir(parents=True, exist_ok=True)
page_path.write_text(subprocess.check_output(
    [binary, "--", "--corpus", term, bundle, site_locale, reader_locale, stylesheet, slug],
    text=True,
))
print(f"Wrote: {page_path}", file=sys.stderr)

if proof:
    proof_path = Path(proof)
    if proof_path.name == f"{term}.md" and slug != term:
        proof_path = proof_path.with_name(f"{slug}.md")
    proof_path.parent.mkdir(parents=True, exist_ok=True)
    proof_path.write_text(subprocess.check_output(
        [binary, "--", "--corpus-markdown", term, bundle, slug],
        text=True,
    ))
    print(f"Wrote proof Markdown: {proof_path}", file=sys.stderr)

redirects = []
if term != slug:
    redirects.append(term)
for alias in aliases:
    if alias != slug:
        redirects.append(alias)
for alias in redirects:
    alias_path = page_path.with_name(f"{alias}.html")
    alias_path.write_text(subprocess.check_output(
        [binary, "--", "--alias", alias, slug, site_locale, stylesheet],
        text=True,
    ))
    print(f"Wrote: {alias_path}", file=sys.stderr)
PYEOF
