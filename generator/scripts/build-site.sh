#!/usr/bin/env bash
# ==========================================================================
# build-site.sh — Batch render all Markdown pages to a static site
# ==========================================================================
# Renders every .md file under src/en-US/ into dist/ as .html.
# Copies the shared stylesheet and any static assets.
#
# Usage:
#   build-site.sh [source_dir] [output_dir]
#
# Defaults: src/en-US → dist
# ==========================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
GENERATOR_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_DIR="$(cd "$GENERATOR_DIR/.." && pwd)"

SOURCE_DIR="${1:-${REPO_DIR}/src/en-US}"
OUTPUT_DIR="${2:-${REPO_DIR}/dist}"
STYLESHEET="/speculum.css"
LOCALE="la"

FABER="${FABER:-faber}"
BUILD_DIR="${GENERATOR_DIR}/target/faber"
BINARY="${BUILD_DIR}/target/debug/speculum-gen"

echo "=== Speculum site builder ==="
echo "Source:  $SOURCE_DIR"
echo "Output:  $OUTPUT_DIR"
echo ""

# ------------------------------------------------------------------
# Step 1: Validate source gates and build the generator binary (once)
# ------------------------------------------------------------------
echo "[1/4] Validating generator source..."
"${SCRIPT_DIR}/validate-html-literals.sh" "${GENERATOR_DIR}/src"

echo "[1/4] Building generator..."
"$FABER" build "$GENERATOR_DIR" -t rust 2>/dev/null

echo "[2/4] Compiling generator..."
(cd "$BUILD_DIR" && cargo build --quiet 2>/dev/null)

# ------------------------------------------------------------------
# Step 2: Clean and prepare output directory
# ------------------------------------------------------------------
echo "[3/4] Preparing output directory..."
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

# Copy stylesheet
cp "${GENERATOR_DIR}/www/speculum.css" "${OUTPUT_DIR}/speculum.css"

# Copy static agent surfaces (llms.txt, skills, agents/*.md, etc.)
STATIC_DIR="${REPO_DIR}/static"
if [ -d "$STATIC_DIR" ]; then
    echo "  copying static/ → dist/"
    # Preserve structure; do not overwrite generated HTML with same path.
    cp -R "${STATIC_DIR}/." "${OUTPUT_DIR}/"
fi

# ------------------------------------------------------------------
# Step 3: Render all Markdown pages
# ------------------------------------------------------------------
echo "[4/4] Rendering pages..."
PAGE_COUNT=0
FAIL_COUNT=0

find "$SOURCE_DIR" -name "*.md" -type f | sort | while read -r md_file; do
    # Derive output path: strip source dir prefix, change .md to .html
    rel_path="${md_file#${SOURCE_DIR}/}"
    out_path="${OUTPUT_DIR}/${rel_path%.md}.html"

    # Create subdirectories
    mkdir -p "$(dirname "$out_path")"

    # Render
    if "$BINARY" "$md_file" "$LOCALE" "$STYLESHEET" > "$out_path" 2>/dev/null; then
        echo "  ✓ ${rel_path%.md}.html"
    else
        echo "  ✗ FAILED: ${rel_path}"
        rm -f "$out_path"
    fi
done

# Corpus pages. Corpus traversal and frontmatter selection stay in the
# corpus batch wrapper; term-page rendering stays in the Faber generator.
"${SCRIPT_DIR}/render-corpus-batch.sh" "${OUTPUT_DIR}" "$LOCALE" "$STYLESHEET"

# Re-copy static after render so agent markdown is never replaced by HTML.
if [ -d "$STATIC_DIR" ]; then
    cp -R "${STATIC_DIR}/." "${OUTPUT_DIR}/"
fi

smoke_contains() {
    local file="$1"
    local needle="$2"
    local label="$3"

    if [ ! -f "$file" ]; then
        echo "ERROR: smoke missing ${label}: ${file}" >&2
        exit 1
    fi

    if ! grep -Fq "$needle" "$file"; then
        echo "ERROR: smoke failed ${label}: missing ${needle} in ${file}" >&2
        exit 1
    fi
}

echo "[smoke] Checking rendered core pages..."
smoke_contains "${OUTPUT_DIR}/index.html" "<!DOCTYPE html>" "home doctype"
smoke_contains "${OUTPUT_DIR}/index.html" "/llms.txt" "home agent link"
smoke_contains "${OUTPUT_DIR}/index.html" "faber-v1.1.1" "home release link"
smoke_contains "${OUTPUT_DIR}/start/install.html" "<!DOCTYPE html>" "install doctype"
smoke_contains "${OUTPUT_DIR}/start/install.html" "/start/install.html" "install path"
smoke_contains "${OUTPUT_DIR}/start/install.html" "faber-v1.1.1" "install release link"

# Count results
PAGE_COUNT=$(find "$OUTPUT_DIR" -name "*.html" -type f | wc -l | tr -d ' ')
STATIC_COUNT=$(find "$OUTPUT_DIR" \( -name "*.txt" -o -name "*.md" -o -name "*.json" \) -type f | wc -l | tr -d ' ')

echo ""
echo "=== Build complete: ${PAGE_COUNT} HTML pages, ${STATIC_COUNT} static machine files → ${OUTPUT_DIR} ==="
