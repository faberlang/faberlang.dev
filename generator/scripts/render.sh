#!/usr/bin/env bash
# ==========================================================================
# render.sh — Shell wrapper for the Speculum site generator
# ==========================================================================
# Invokes the Python renderer (speculum_py.py — the byte-equivalent port of
# the Faber generator) with separate site and reader locale parameters.
#
# Usage:
#   render.sh <source.md> [site_locale] [reader_locale] [stylesheet] [output]
#
# The output is written to stdout if no output file is specified.
# ==========================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="${PYTHON:-python3}"

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

echo "Rendering $SOURCE (Python renderer)..." >&2
echo "  Site locale: $SITE_LOCALE" >&2
echo "  Reader locale: $READER_LOCALE" >&2

# The renderer derives the page iter from the source path using the established
# site URL rule.
if [ -n "$OUTPUT" ]; then
    "$PYTHON" "${SCRIPT_DIR}/speculum_py.py" "$SOURCE" "$SITE_LOCALE" "$READER_LOCALE" "$STYLESHEET" > "$OUTPUT"
    echo "Wrote: $OUTPUT" >&2
else
    exec "$PYTHON" "${SCRIPT_DIR}/speculum_py.py" "$SOURCE" "$SITE_LOCALE" "$READER_LOCALE" "$STYLESHEET"
fi
