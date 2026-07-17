#!/usr/bin/env bash
# Render a bounded corpus term page through the Faber generator.
#
# The wrapper owns traversal and bundle creation. Frontmatter parsing, kind
# policy, Markdown templating, HTML rendering, and bundle reads remain in Faber.
#
# Usage: render-corpus.sh <term> <output.html> [locale] [stylesheet]

set -euo pipefail

GENERATOR_DIR="$(cd "$(dirname "$0")/.." && pwd)"
WORKSPACE_DIR="$(cd "$GENERATOR_DIR/.." && pwd)"
CORPUS_DIR="${WORKSPACE_DIR}/../examples/corpus"
BUILD_DIR="${GENERATOR_DIR}/target/faber"
FABER="${FABER:-faber}"

TERM="${1:-}"
OUTPUT="${2:-}"
LOCALE="${3:-la}"
STYLESHEET="${4:-/speculum.css}"
PROOF_MARKDOWN="${PROOF_MARKDOWN:-}"

if [ -z "$TERM" ] || [ -z "$OUTPUT" ]; then
    echo "Usage: render-corpus.sh <term> <output.html> [locale] [stylesheet]" >&2
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
(cd "$BUILD_DIR" && cargo build --quiet 2>/dev/null)

mkdir -p "$(dirname "$OUTPUT")"
"${BUILD_DIR}/target/debug/speculum-gen" -- --corpus "$TERM" "$BUNDLE" "$LOCALE" "$STYLESHEET" > "$OUTPUT"
echo "Wrote: $OUTPUT" >&2

if [ -n "$PROOF_MARKDOWN" ]; then
    mkdir -p "$(dirname "$PROOF_MARKDOWN")"
    "${BUILD_DIR}/target/debug/speculum-gen" -- --corpus-markdown "$TERM" "$BUNDLE" > "$PROOF_MARKDOWN"
    echo "Wrote proof Markdown: $PROOF_MARKDOWN" >&2
fi

# Generate static alias bridges from the selected canonical example. These are
# intentionally files, not runtime rewrites, so deployment remains static-host
# friendly and every alias has one canonical destination.
BUNDLE_PATH="$BUNDLE" CORPUS_DIR="$CORPUS_DIR" TERM="$TERM" OUTPUT="$OUTPUT" LOCALE="$LOCALE" STYLESHEET="$STYLESHEET" BIN="${BUILD_DIR}/target/debug/speculum-gen" python3 << 'PYEOF'
import os
import tomllib
from pathlib import Path

corpus = Path(os.environ["CORPUS_DIR"])
term = os.environ["TERM"]
output = Path(os.environ["OUTPUT"])
locale = os.environ["LOCALE"]
stylesheet = os.environ["STYLESHEET"]
binary = os.environ["BIN"]
canonical = None
aliases = []
for path in sorted(corpus.rglob("*.fab")):
    source = path.read_text()
    parts = source.split("+++", 2)
    if len(parts) != 3:
        continue
    fields = tomllib.loads(parts[1])
    if fields.get("term") == term and fields.get("canonical", False):
        canonical = term
        aliases = fields.get("aliases", [])
        break
if canonical is None:
    raise SystemExit(0)
for alias in aliases:
    alias_path = output.parent / f"{alias}.html"
    alias_path.parent.mkdir(parents=True, exist_ok=True)
    rendered = __import__("subprocess").check_output(
        [binary, "--", "--alias", alias, canonical, locale, stylesheet], text=True
    )
    alias_path.write_text(rendered)
    print(f"Wrote: {alias_path}", file=os.sys.stderr)
PYEOF
