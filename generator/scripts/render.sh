#!/usr/bin/env bash
# ==========================================================================
# render.sh — Shell wrapper for the Speculum site generator
# ==========================================================================
# This wrapper builds the generator to Rust, compiles it, and invokes the
# generator CLI. Source file reads are handled inside Speculum via norma:solum.
#
# Usage:
#   render.sh <source.md> [locale] [stylesheet] [output]
#
# The output is written to stdout if no output file is specified.
# ==========================================================================

set -euo pipefail

GENERATOR_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BUILD_DIR="${GENERATOR_DIR}/target/faber"
FABER="${FABER:-faber}"

SOURCE="${1:-}"
LOCALE="${2:-la}"
STYLESHEET="${3:-/speculum.css}"
OUTPUT="${4:-}"

if [ -z "$SOURCE" ]; then
    echo "Usage: render.sh <source.md> [locale] [stylesheet] [output]"
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
if [ -n "$OUTPUT" ]; then
    "${BUILD_DIR}/target/debug/speculum-gen" "$SOURCE" "$LOCALE" "$STYLESHEET" > "$OUTPUT"
    echo "Wrote: $OUTPUT" >&2
else
    "${BUILD_DIR}/target/debug/speculum-gen" "$SOURCE" "$LOCALE" "$STYLESHEET"
fi
