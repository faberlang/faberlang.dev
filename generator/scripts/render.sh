#!/usr/bin/env bash
# ==========================================================================
# render.sh — Shell wrapper for the Speculum site generator
# ==========================================================================
# Wrapper builds the generator to Rust, compiles it, and invokes the
# generator CLI with separate site and reader locale parameters.
#
# Usage:
#   render.sh <source.md> [site_locale] [reader_locale] [stylesheet] [output]
#
# The output is written to stdout if no output file is specified.
# ==========================================================================

set -euo pipefail

GENERATOR_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BUILD_DIR="${GENERATOR_DIR}/target/faber"
FABER="${FABER:-faber}"

SOURCE="${1:-}"
SITE_LOCALE="${2:-en-US}"
READER_LOCALE="${3:-la}"
STYLESHEET="${4:-/speculum.css}"
OUTPUT="${5:-}"

if [ -z "$SOURCE" ]; then
    echo "Usage: render.sh <source.md> [site_locale] [reader_locale] [stylesheet] [output]"
    exit 1
fi

if [ ! -f "$SOURCE" ]; then
    echo "ERROR: source file not found: $SOURCE"
    exit 1
fi

echo "Building generator..." >&2
"$FABER" build "$GENERATOR_DIR" -t rust 2>/dev/null

echo "Compiling..." >&2
(cd "$BUILD_DIR" && cargo build --quiet 2>/dev/null)

echo "Rendering $SOURCE..." >&2
echo "  Site locale: $SITE_LOCALE" >&2
echo "  Reader locale: $READER_LOCALE" >&2

if [ -n "$OUTPUT" ]; then
    "${BUILD_DIR}/target/debug/speculum-gen" "$SOURCE" "$SITE_LOCALE" "$READER_LOCALE" "$STYLESHEET" > "$OUTPUT"
    echo "Wrote: $OUTPUT" >&2
else
    "${BUILD_DIR}/target/debug/speculum-gen" "$SOURCE" "$SITE_LOCALE" "$READER_LOCALE" "$STYLESHEET"
fi
