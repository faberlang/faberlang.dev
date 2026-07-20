#!/usr/bin/env bash
# ==========================================================================
# build-site.sh — Batch render all Markdown pages to a static site
# ==========================================================================
# Renders every locale directory under src/ into dist/ as .html, with
# en-US URL-path prefix structure (Phase 1 URL migration).
#
# Usage:
#   build-site.sh                                       # full site
#   build-site.sh <source_dir> <output_dir> <site_locale> <reader_locale>
#
# Full site: discovers src/* directories, renders each locale, then runs
# redirect generation, smoke tests, post-process, gates, and sitemap.
#
# Single-locale mode: renders one locale into the given output directory.
# ==========================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
GENERATOR_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_DIR="$(cd "$GENERATOR_DIR/.." && pwd)"
WORKSPACE_DIR="$(cd "$REPO_DIR/.." && pwd)"

STYLESHEET="/speculum.css"

# ------------------------------------------------------------------
# Python discovery (stdlib tomllib preferred)
# ------------------------------------------------------------------
PYTHON="${PYTHON:-}"
if [ -z "$PYTHON" ]; then
    for candidate in python3.13 python3.12 python3.11 python3; do
        if command -v "$candidate" >/dev/null 2>&1 \
            && "$candidate" -c 'import tomllib' >/dev/null 2>&1; then
            PYTHON="$candidate"
            break
        fi
    done
fi

FABER="${FABER:-faber}"
BUILD_DIR="${GENERATOR_DIR}/target/faber"

# Binary path candidates (old radix-out subdir vs new top-level target)
BINARY_OLD="${BUILD_DIR}/target/debug/speculum-gen"
BINARY_NEW="${GENERATOR_DIR}/target/debug/speculum-gen"

# List of temp dirs to clean on exit
TEMPDIRS=()

cleanup() {
    for d in "${TEMPDIRS[@]}"; do
        rm -rf "$d"
    done
}
trap cleanup EXIT

# ------------------------------------------------------------------
# Find the speculum-gen binary, preferring newer mtime.
# ------------------------------------------------------------------
find_binary() {
    local old_exists=0 new_exists=0
    [ -x "$BINARY_OLD" ] && old_exists=1
    [ -x "$BINARY_NEW" ] && new_exists=1

    if [ "$old_exists" = 1 ] && [ "$new_exists" = 1 ]; then
        if [ "$BINARY_NEW" -nt "$BINARY_OLD" ]; then
            echo "$BINARY_NEW"
        else
            echo "$BINARY_OLD"
        fi
    elif [ "$old_exists" = 1 ]; then
        echo "$BINARY_OLD"
    elif [ "$new_exists" = 1 ]; then
        echo "$BINARY_NEW"
    else
        echo ""
    fi
}

# ------------------------------------------------------------------
# Smoke check helper
# ------------------------------------------------------------------
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

# ------------------------------------------------------------------
# Parse invocation mode
# ------------------------------------------------------------------
FULL_SITE=false

if [ $# -eq 0 ]; then
    FULL_SITE=true
    # Defaults for full-site preamble steps
    SOURCE_DIR="${REPO_DIR}/src/en-US"
    OUTPUT_DIR="${REPO_DIR}/dist"
    SITE_LOCALE="en-US"
    READER_LOCALE="la"
elif [ $# -eq 4 ]; then
    SOURCE_DIR="$1"
    OUTPUT_DIR="$2"
    SITE_LOCALE="$3"
    READER_LOCALE="$4"
else
    echo "Usage:"
    echo "  build-site.sh                                       # full site"
    echo "  build-site.sh <source_dir> <output_dir> <site_locale> <reader_locale>"
    exit 1
fi

echo "=== Speculum site builder ==="
echo "Mode:     $([ "$FULL_SITE" = true ] && echo 'full site' || echo 'single locale')"
echo "Source:   $SOURCE_DIR"
echo "Output:   $OUTPUT_DIR"
echo "Site:     $SITE_LOCALE"
echo "Reader:   $READER_LOCALE"
echo ""

# ------------------------------------------------------------------
# render_locale — render one locale's markdown into its output dir
# ------------------------------------------------------------------
render_locale() {
    local src="$1"
    local out="$2"
    local site="$3"
    local reader="$4"
    local style="$5"
    local binary="$6"

    local render_source="$src"
    local localized_source=""

    if [ "$reader" != "la" ] && [ "$site" != "en-US" ]; then
        localized_source="$(mktemp -d)"
        TEMPDIRS+=("$localized_source")
        "${SCRIPT_DIR}/localize-markdown.py" "$src" "$localized_source" --locale "$reader" --faber "$FABER"
        render_source="$localized_source"
    fi

    find "$render_source" -name "*.md" -type f | sort | while read -r md_file; do
        rel_path="${md_file#${render_source}/}"
        out_path="${out}/${rel_path%.md}.html"
        mkdir -p "$(dirname "$out_path")"

        if "$binary" "$md_file" "$site" "$reader" "$style" > "$out_path" 2>/dev/null; then
            echo "  ✓ ${rel_path%.md}.html"
        else
            echo "  ✗ FAILED: ${rel_path}"
            rm -f "$out_path"
        fi
    done

    # Corpus pages for this locale
    echo "  [corpus] Rendering corpus pages for ${site}..."
    "${SCRIPT_DIR}/render-corpus-batch.sh" "$out" "$site" "$reader" "$style"
}

# ==================================================================
# FULL SITE BUILD
# ==================================================================
if [ "$FULL_SITE" = true ]; then

    # Step 1: Validate and build generator (once)
    echo "[1/9] Validating generator source..."
    "${SCRIPT_DIR}/validate-html-literals.sh" "${GENERATOR_DIR}/src"

    echo "[1/9] Building generator..."
    "$FABER" build "$GENERATOR_DIR" -t rust 2>/dev/null

    echo "[2/9] Compiling generator..."
    (cd "$BUILD_DIR" && cargo build --quiet 2>/dev/null)

    # Locate binary after build
    BINARY="$(find_binary)"
    if [ -z "$BINARY" ]; then
        echo "ERROR: speculum-gen binary not found after build. Checked:" >&2
        echo "  $BINARY_OLD" >&2
        echo "  $BINARY_NEW" >&2
        exit 1
    fi
    echo "  Binary: $BINARY"

    # Step 2: Clean and prepare output directory
    echo "[3/9] Preparing output directory..."
    rm -rf "$OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR"

    # Copy stylesheet
    cp "${GENERATOR_DIR}/www/speculum.css" "${OUTPUT_DIR}/speculum.css"

    # Copy static agent surfaces
    STATIC_DIR="${REPO_DIR}/static"
    if [ -d "$STATIC_DIR" ] && [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
        echo "  copying static/ → dist/"
        cp -R "${STATIC_DIR}/." "${OUTPUT_DIR}/"
    fi

    # Step 3: Discover locale directories under src/
    LOCALE_DIRS=()
    while IFS= read -r dir; do
        LOCALE_DIRS+=("$(basename "$dir")")
    done < <(find "${REPO_DIR}/src" -mindepth 1 -maxdepth 1 -type d | sort)

    echo "[4/9] Rendering ${#LOCALE_DIRS[@]} locales..."

    for site in "${LOCALE_DIRS[@]}"; do
        reader=$("$PYTHON" "${SCRIPT_DIR}/locales_registry.py" reader "$site")
        echo "  [locale] ${site} (reader: ${reader})"
        render_locale "${REPO_DIR}/src/${site}" "${OUTPUT_DIR}/${site}" "$site" "$reader" "$STYLESHEET" "$BINARY"
    done

    # Step 4: Re-copy static after render
    echo "[5/9] Re-copying static assets after render..."
    if [ -d "$STATIC_DIR" ] && [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
        cp -R "${STATIC_DIR}/." "${OUTPUT_DIR}/"
    fi

    # Step 5: Generate llms.txt
    echo "[6/9] Generating llms.txt..."
    if [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
        "$PYTHON" "${SCRIPT_DIR}/render-llms.py" \
            --corpus "${WORKSPACE_DIR}/examples/corpus" \
            --output "${OUTPUT_DIR}/llms.txt"
    fi

    # Step 6: Generate redirect stubs (en-US → bare path)
    echo "[7/10] Generating en-US redirect stubs..."
    "$PYTHON" "${SCRIPT_DIR}/generate-redirects.py" "$OUTPUT_DIR" "en-US"

    # Step 7: Generate language portal (overwrites dist/index.html)
    echo "[8/10] Generating language portal..."
    "$PYTHON" "${SCRIPT_DIR}/generate-portal.py" "${OUTPUT_DIR}/index.html"

    # Step 8: Smoke checks against en-US paths
    echo "[9/10] Smoke checks..."
    smoke_contains "${OUTPUT_DIR}/en-US/index.html" "<!DOCTYPE html>" "home doctype"
    if [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
        smoke_contains "${OUTPUT_DIR}/en-US/index.html" "/llms.txt" "home agent link"
        smoke_contains "${OUTPUT_DIR}/en-US/index.html" "faber-v1.1.1" "home release link"
        smoke_contains "${OUTPUT_DIR}/llms.txt" "Generated corpus frontmatter reference" "llms surface"
        smoke_contains "${OUTPUT_DIR}/en-US/start/install.html" "<!DOCTYPE html>" "install doctype"
        smoke_contains "${OUTPUT_DIR}/en-US/start/install.html" "/en-US/start/install.html" "install path"
        smoke_contains "${OUTPUT_DIR}/en-US/start/install.html" "faber-v1.1.1" "install release link"
        smoke_contains "${OUTPUT_DIR}/en-US/start/hello.html" "Salve, munde" "hello start page"
        smoke_contains "${OUTPUT_DIR}/en-US/start/commands.html" "faber check" "commands start page"
        smoke_contains "${OUTPUT_DIR}/en-US/start/projects.html" "faberlang/examples" "projects start page"
        smoke_contains "${OUTPUT_DIR}/en-US/404.html" "404" "404 page"
        smoke_contains "${OUTPUT_DIR}/en-US/history/releases.html" "faber-v1.1.1" "releases inventory"
        smoke_contains "${OUTPUT_DIR}/en-US/history/releases.html" "Historical releases" "releases archive heading"
        smoke_contains "${OUTPUT_DIR}/robots.txt" "Sitemap:" "robots.txt"

        # Portal checks
        smoke_contains "${OUTPUT_DIR}/index.html" 'class="porta"' "portal body class"
        smoke_contains "${OUTPUT_DIR}/index.html" "ภาษาไทย" "portal Thai native"
        smoke_contains "${OUTPUT_DIR}/index.html" "العربية" "portal Arabic native"
        smoke_contains "${OUTPUT_DIR}/index.html" "简体中文" "portal zh-Hans native"
        smoke_contains "${OUTPUT_DIR}/index.html" "incipit" "portal Latin sample"
        smoke_contains "${OUTPUT_DIR}/index.html" 'href="/en-US/"' "portal en-US link"
        # Must NOT be a meta-refresh redirect
        if grep -Fq 'http-equiv="refresh"' "${OUTPUT_DIR}/index.html"; then
            echo "ERROR: portal index must not meta-refresh" >&2
            exit 1
        fi

        # Redirect stub checks
        smoke_contains "${OUTPUT_DIR}/start/install.html" "<!DOCTYPE html>" "redirect install doctype"
        smoke_contains "${OUTPUT_DIR}/start/install.html" "/en-US/start/install.html" "redirect install target"
    fi

    # Step 9: Post-process
    echo "[10/10] Post-processing..."
    "$PYTHON" "${SCRIPT_DIR}/strip-empty-sources.py" "$OUTPUT_DIR"
    "$PYTHON" "${SCRIPT_DIR}/inject-skip-link.py" "$OUTPUT_DIR"

    # Step 10: Gates (link check, leakage) — only for full site
    echo "[10/10] Gates..."
    echo "  [gate] Internal link check..."
    "$PYTHON" "${SCRIPT_DIR}/check-internal-links.py" "$OUTPUT_DIR" || {
        echo "ERROR: internal link gate failed" >&2
        exit 1
    }

    echo "  [gate] Leakage gate..."
    "$PYTHON" "${SCRIPT_DIR}/check-leakage-gate.py" "$OUTPUT_DIR" || {
        echo "ERROR: leakage gate failed" >&2
        exit 1
    }

    # Sitemap and canonical
    echo "  [sitemap] Generating sitemap.xml..."
    "$PYTHON" "${SCRIPT_DIR}/generate-sitemap.py" "$OUTPUT_DIR" "https://faberlang.dev"
    smoke_contains "${OUTPUT_DIR}/sitemap.xml" "<urlset" "sitemap"

    echo "  [canonical] Injecting canonical URL tags..."
    "$PYTHON" "${SCRIPT_DIR}/inject-canonical.py" "$OUTPUT_DIR" "https://faberlang.dev"

else
    # ==============================================================
    # SINGLE-LOCALE MODE (4 positional args)
    # ==============================================================

    # Build for single-locale mode only if binary not found
    BINARY="$(find_binary)"
    if [ -z "$BINARY" ]; then
        echo "[1/2] Building generator..."
        "$FABER" build "$GENERATOR_DIR" -t rust 2>/dev/null
        echo "[2/2] Compiling generator..."
        (cd "$BUILD_DIR" && cargo build --quiet 2>/dev/null)
        BINARY="$(find_binary)"
        if [ -z "$BINARY" ]; then
            echo "ERROR: speculum-gen binary not found after build." >&2
            exit 1
        fi
        echo "  Binary: $BINARY"
    else
        echo "  Binary: $BINARY (reusing existing build)"
    fi

    echo "Rendering ${SITE_LOCALE} → ${OUTPUT_DIR}..."
    mkdir -p "$OUTPUT_DIR"
    cp "${GENERATOR_DIR}/www/speculum.css" "${OUTPUT_DIR}/speculum.css"
    render_locale "$SOURCE_DIR" "$OUTPUT_DIR" "$SITE_LOCALE" "$READER_LOCALE" "$STYLESHEET" "$BINARY"
    echo "Re-copying static..."
    STATIC_DIR="${REPO_DIR}/static"
    if [ -d "$STATIC_DIR" ] && [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
        cp -R "${STATIC_DIR}/." "$(dirname "$OUTPUT_DIR")/"
    fi
fi

# ------------------------------------------------------------------
# Summary
# ------------------------------------------------------------------
PAGE_COUNT=$(find "$OUTPUT_DIR" -name "*.html" -type f | wc -l | tr -d ' ')
STATIC_COUNT=$(find "$OUTPUT_DIR" \( -name "*.txt" -o -name "*.md" -o -name "*.json" \) -type f | wc -l | tr -d ' ')

echo ""
echo "=== Build complete: ${PAGE_COUNT} HTML pages, ${STATIC_COUNT} static machine files → ${OUTPUT_DIR} ==="
