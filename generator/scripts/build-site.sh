#!/usr/bin/env bash
# ==========================================================================
# build-site.sh — Batch render all Markdown pages to a static site
# ==========================================================================
# Renders every .md file under src/en-US/ into dist/ as .html.
# Copies the shared stylesheet and any static assets.
#
# Usage:
#   build-site.sh [source_dir] [output_dir] [locale]
#
# Defaults: src/en-US → dist → la
# ==========================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
GENERATOR_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_DIR="$(cd "$GENERATOR_DIR/.." && pwd)"

SOURCE_DIR="${1:-${REPO_DIR}/src/en-US}"
OUTPUT_DIR="${2:-${REPO_DIR}/dist}"
STYLESHEET="/speculum.css"
LOCALE="${3:-la}"

FABER="${FABER:-faber}"
BUILD_DIR="${GENERATOR_DIR}/target/faber"
BINARY="${BUILD_DIR}/target/debug/speculum-gen"

echo "=== Speculum site builder ==="
echo "Source:  $SOURCE_DIR"
echo "Output:  $OUTPUT_DIR"
echo "Locale:  $LOCALE"
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

# Copy static agent surfaces (skills, agents/*.md, etc.). /llms.txt is generated
# from corpus frontmatter after corpus traversal.
STATIC_DIR="${REPO_DIR}/static"
if [ -d "$STATIC_DIR" ] && [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
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
RENDER_SOURCE="$SOURCE_DIR"
LOCALIZED_SOURCE=""

if [ "$LOCALE" != "la" ]; then
    LOCALIZED_SOURCE="$(mktemp -d)"
    trap 'rm -rf "$LOCALIZED_SOURCE"' EXIT
    "${SCRIPT_DIR}/localize-markdown.py" "$SOURCE_DIR" "$LOCALIZED_SOURCE" --locale "$LOCALE" --faber "$FABER"
    RENDER_SOURCE="$LOCALIZED_SOURCE"
fi

find "$RENDER_SOURCE" -name "*.md" -type f | sort | while read -r md_file; do
    # Derive output path: strip source dir prefix, change .md to .html
    rel_path="${md_file#${RENDER_SOURCE}/}"
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
if [ -d "$STATIC_DIR" ] && [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
    cp -R "${STATIC_DIR}/." "${OUTPUT_DIR}/"
fi

if [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
    python3 "${SCRIPT_DIR}/render-llms.py" --corpus "${REPO_DIR}/../examples/corpus" --output "${OUTPUT_DIR}/llms.txt"
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
if [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
    smoke_contains "${OUTPUT_DIR}/llms.txt" "Generated corpus frontmatter reference" "generated llms surface"
    smoke_contains "${OUTPUT_DIR}/llms.txt" "Distinct frontmatter terms: 183" "generated llms term count"
fi
smoke_contains "${OUTPUT_DIR}/start/install.html" "<!DOCTYPE html>" "install doctype"
smoke_contains "${OUTPUT_DIR}/start/install.html" "/start/install.html" "install path"
smoke_contains "${OUTPUT_DIR}/start/install.html" "faber-v1.1.1" "install release link"
smoke_contains "${OUTPUT_DIR}/start/hello.html" "Salve, munde" "hello start page"
smoke_contains "${OUTPUT_DIR}/start/commands.html" "faber check" "commands start page"
smoke_contains "${OUTPUT_DIR}/start/projects.html" "faberlang/examples" "projects start page"

if [ "${SPECULUM_SKIP_LOCALES:-0}" != "1" ] && [ "$SOURCE_DIR" = "${REPO_DIR}/src/en-US" ] && [ "$OUTPUT_DIR" = "${REPO_DIR}/dist" ]; then
    find "${REPO_DIR}/src" -mindepth 1 -maxdepth 1 -type d | sort | while read -r locale_dir; do
        locale_name="$(basename "$locale_dir")"
        if [ "$locale_name" = "en-US" ]; then
            continue
        fi
        echo "[locale] Rendering ${locale_name} → ${OUTPUT_DIR}/${locale_name}"
        SPECULUM_SKIP_LOCALES=1 SPECULUM_SKIP_STATIC=1 "$0" "$locale_dir" "${OUTPUT_DIR}/${locale_name}" "$locale_name"
    done
fi

# Post-build gates: link integrity + leakage (top-level build only)
if [ "${SPECULUM_SKIP_LOCALES:-0}" != "1" ] && [ "$SOURCE_DIR" = "${REPO_DIR}/src/en-US" ] && [ "$OUTPUT_DIR" = "${REPO_DIR}/dist" ]; then
    echo ""
    echo "[gate] Internal link check..."
    python3 "${SCRIPT_DIR}/check-internal-links.py" "$OUTPUT_DIR" || {
        echo "ERROR: internal link gate failed" >&2
        exit 1
    }

    echo "[gate] Leakage gate..."
    python3 "${SCRIPT_DIR}/check-leakage-gate.py" "$OUTPUT_DIR" || {
        echo "ERROR: leakage gate failed" >&2
        exit 1
    }
fi

# Count results
PAGE_COUNT=$(find "$OUTPUT_DIR" -name "*.html" -type f | wc -l | tr -d ' ')
STATIC_COUNT=$(find "$OUTPUT_DIR" \( -name "*.txt" -o -name "*.md" -o -name "*.json" \) -type f | wc -l | tr -d ' ')

echo ""
echo "=== Build complete: ${PAGE_COUNT} HTML pages, ${STATIC_COUNT} static machine files → ${OUTPUT_DIR} ==="
