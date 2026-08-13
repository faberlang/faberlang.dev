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
# Toolchain for the fence-localize (transcode) step. Defaults to $FABER;
# pin separately when reader packs are newer than the installed faber's
# pack validator (e.g. FABER_LOCALIZE=path/to/workspace-faber).
FABER_LOCALIZE="${FABER_LOCALIZE:-$FABER}"
# Rendering source INTO a reader locale is `faber format --locale`; radix
# cannot do it (`emit -t faber` is canonical Latin by definition). Prefer the
# workspace build, which is current with the packs.
WORKSPACE_FABER="${WORKSPACE_DIR}/faber/target/release/faber"
if [ -x "$WORKSPACE_FABER" ] && [ "${FABER_LOCALIZE}" = "$FABER" ]; then
    FABER_LOCALIZE="$WORKSPACE_FABER"
fi
BUILD_DIR="${GENERATOR_DIR}/target/faber"

# Binary path candidates (old radix-out subdir vs new top-level target)
# Release, not debug. The generator is Faber-compiled Rust whose hot path is
# superlinear in page size under -O0: a 6.5k-word page took 4.5s debug and
# 0.10s release (44x). Debug cost ~70s per full build across seven locales.
BINARY_OLD="${BUILD_DIR}/target/release/speculum-gen"
BINARY_NEW="${GENERATOR_DIR}/target/release/speculum-gen"

# List of temp dirs to clean on exit
TEMPDIRS=()

cleanup() {
    # Guard the expansion: under `set -u`, bash 3.2 treats an empty array as
    # unbound, so an early exit would report that instead of the real error.
    if [ "${#TEMPDIRS[@]}" -gt 0 ]; then
        for d in "${TEMPDIRS[@]}"; do
            rm -rf "$d"
        done
    fi
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

    # Every locale renders its code in its own reader locale, English
    # included. Latin stays the canonical source surface in src/ and the
    # interchange dialect the compiler uses internally, but a reader who chose
    # the English site did not choose to decode Latin keywords: `la` is a
    # reference surface here, not the one the page presents.
    if [ "$reader" != "la" ]; then
        localized_source="$(mktemp -d)"
        TEMPDIRS+=("$localized_source")
        "${SCRIPT_DIR}/localize-markdown.py" "$src" "$localized_source" --locale "$reader" --faber "$FABER_LOCALIZE"
        render_source="$localized_source"
    fi

    find "$render_source" -name "*.md" -type f | sort | while read -r md_file; do
        rel_path="${md_file#${render_source}/}"
        iter="${rel_path%.md}"
        out_path="${out}/${iter}.html"
        mkdir -p "$(dirname "$out_path")"

        # Pass --page so canonical/og:url use the locale-relative slug even
        # when the source lives in a temp localize directory (no src/ prefix).
        if "$binary" -- --page "$iter" "$md_file" "$site" "$reader" "$style" > "$out_path" 2>/dev/null; then
            echo "  ✓ ${iter}.html"
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

    # Step 0: Refresh generated matrix pages when radix sibling is present
    if [ -f "${WORKSPACE_DIR}/radix/EBNF_MATRIX.md" ]; then
        echo "[0/10] Generating target compatibility matrix pages..."
        "$PYTHON" "${SCRIPT_DIR}/generate-target-matrix.py" --all-locales
    else
        echo "[0/10] Skipping target matrix generate (no ${WORKSPACE_DIR}/radix/EBNF_MATRIX.md)"
    fi

    # Step 0b: Regenerate the sections assembled from captured panels and
    # sibling checkouts. All of these write src/ and so must run before the
    # render. Each degrades to leaving its committed output alone when its
    # inputs are absent, so a checkout without siblings still builds.
    echo "[0/10] Generating target lanes, examples, grammar, and localization..."
    "$PYTHON" "${SCRIPT_DIR}/generate-target-lanes.py"
    "$PYTHON" "${SCRIPT_DIR}/generate-localization.py"
    "$PYTHON" "${SCRIPT_DIR}/generate-examples.py"
    if [ -f "${WORKSPACE_DIR}/radix/EBNF.md" ]; then
        "${SCRIPT_DIR}/generate-grammar" --all-locales
    else
        echo "  Skipping grammar generate (no ${WORKSPACE_DIR}/radix/EBNF.md)"
    fi

    # Releases is NOT regenerated here: it needs `gh` and network access, and a
    # build that silently depends on the network is a build that breaks on a
    # plane. Run generate-releases.py by hand when a release lands.

    # Step 1: Validate and build generator (once)
    echo "[1/9] Validating generator source..."
    "${SCRIPT_DIR}/validate-html-literals.sh" "${GENERATOR_DIR}/src"

    echo "[1/9] Building generator..."
    "$FABER" build "$GENERATOR_DIR" -t rust 2>/dev/null

    echo "[2/9] Compiling generator..."
    (cd "$BUILD_DIR" && cargo build --release --quiet 2>/dev/null)

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

    # Step 5: Generate llms-full.txt (keyword catalog)
    echo "[6/9] Generating llms-full.txt..."
    if [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
        "$PYTHON" "${SCRIPT_DIR}/render-llms.py" \
            --corpus "${WORKSPACE_DIR}/radix/corpus" \
            --output "${OUTPUT_DIR}/llms-full.txt"
        "$PYTHON" "${SCRIPT_DIR}/generate-search-index.py" \
            --corpus "${WORKSPACE_DIR}/radix/corpus" \
            --output-dir "${OUTPUT_DIR}"
    fi

    # Step 5b: Retired-path stubs from the 2026-08 IA restructure
    "$PYTHON" "${SCRIPT_DIR}/ia-redirects.py" stubs

    # Step 6: Generate redirect stubs (en-US → bare path)
    echo "[7/10] Generating en-US redirect stubs..."
    "${SCRIPT_DIR}/generate-redirects" "$OUTPUT_DIR" "en-US"

    # Step 7: Generate the landing page (/) and the language portal (/porta/).
    # The landing page states the claim and proves it; the portal is the
    # locale chooser it links to, no longer the site's front door.
    echo "[8/10] Generating landing page and language portal..."
    "$PYTHON" "${SCRIPT_DIR}/generate-landing.py" "${OUTPUT_DIR}/index.html"
    mkdir -p "${OUTPUT_DIR}/porta"
    "$PYTHON" "${SCRIPT_DIR}/generate-portal.py" "${OUTPUT_DIR}/porta/index.html"

    # Step 8: Smoke checks against en-US paths
    echo "[9/10] Smoke checks..."
    # The current release is stated once, in the Install page's fact table.
    # Reading it back from there keeps a version bump a content edit rather
    # than a build-script edit, and still fails closed if the download links
    # were left pointing at the previous version.
    current_faber="$(sed -n 's/^| \*\*Version\*\* | \(.*\) |$/\1/p' \
        "${REPO_DIR}/src/en-US/start/install.md" | head -1)"
    if [ -z "$current_faber" ]; then
        echo "ERROR: smoke could not read the current version from src/en-US/start/install.md" >&2
        exit 1
    fi
    smoke_contains "${OUTPUT_DIR}/en-US/index.html" "<!DOCTYPE html>" "home doctype"
    if [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
        smoke_contains "${OUTPUT_DIR}/en-US/index.html" "/llms.txt" "home agent link"
        smoke_contains "${OUTPUT_DIR}/en-US/index.html" "faber-v${current_faber}" "home release link"
        smoke_contains "${OUTPUT_DIR}/llms-full.txt" "Generated corpus frontmatter reference" "llms-full surface"
        smoke_contains "${OUTPUT_DIR}/en-US/start/install.html" "<!DOCTYPE html>" "install doctype"
        smoke_contains "${OUTPUT_DIR}/en-US/start/install.html" "/en-US/start/install.html" "install path"
        smoke_contains "${OUTPUT_DIR}/en-US/start/install.html" "faber-v${current_faber}" "install release link"
        smoke_contains "${OUTPUT_DIR}/en-US/start/hello.html" "Salve, munde" "hello start page"
        smoke_contains "${OUTPUT_DIR}/en-US/cheatsheet/commands.html" "faber check" "cheat sheet commands"
        smoke_contains "${OUTPUT_DIR}/en-US/cheatsheet/index.html" "Cheat sheet" "cheat sheet index"
        smoke_contains "${OUTPUT_DIR}/en-US/cheatsheet/errors.html" "error channel" "cheat sheet errors"
        smoke_contains "${OUTPUT_DIR}/en-US/start/projects.html" "faberlang/examples" "projects start page"
        smoke_contains "${OUTPUT_DIR}/en-US/examples/index.html" "device-summa" "examples index"
        smoke_contains "${OUTPUT_DIR}/en-US/examples/cat.html" "faber-code" "example source shown"
        smoke_contains "${OUTPUT_DIR}/en-US/targets/index.html" "Target lanes" "target lanes index"
        smoke_contains "${OUTPUT_DIR}/en-US/404.html" "404" "404 page"
        smoke_contains "${OUTPUT_DIR}/en-US/releases/index.html" "Faber ${current_faber}" "releases index"
        smoke_contains "${OUTPUT_DIR}/en-US/releases/faber-1.4.0.html" "faber-v1.4.0" "pinned release page"
        smoke_contains "${OUTPUT_DIR}/en-US/releases/radix-0.79.0.html" "Release notes" "release notes imported"
        smoke_contains "${OUTPUT_DIR}/en-US/toolchain/target-matrix.html" "Target compatibility" "targets matrix title"
        smoke_contains "${OUTPUT_DIR}/en-US/toolchain/target-matrix.html" "table-scroll" "targets matrix scroll wrap"
        smoke_contains "${OUTPUT_DIR}/en-US/toolchain/target-matrix.html" "Application lane" "targets HIR summary"
        smoke_contains "${OUTPUT_DIR}/en-US/toolchain/target-matrix.html" "Systems lane" "targets MIR summary"
        smoke_contains "${OUTPUT_DIR}/en-US/index.html" "/toolchain/target-matrix.html" "sidebar target matrix link"
        smoke_contains "${OUTPUT_DIR}/robots.txt" "Sitemap:" "robots.txt"
        smoke_contains "${OUTPUT_DIR}/robots.txt" "Allow: /" "robots allow all"
        smoke_contains "${OUTPUT_DIR}/search-index.json" '"t":"redde"' "search index dataset"
        smoke_contains "${OUTPUT_DIR}/search-index.zh-Hans.json" '"d":"函数"' "search index zh-Hans spellings"
        # IA restructure: the five journey sections must all render
        for sec in language toolchain libraries reference; do
            smoke_contains "${OUTPUT_DIR}/en-US/${sec}/index.html" "<!DOCTYPE html>" "${sec} index"
        done
        smoke_contains "${OUTPUT_DIR}/en-US/language/index.html" "saturate" "language index shows code"
        # The en-US pages render in the `en` reader locale, not `la`. This is
        # the guard on that: `functio` is the Latin spelling of `fn`, so its
        # presence in a rendered en-US body means the transcode step was
        # skipped and English readers are back to decoding Latin keywords.
        smoke_contains "${OUTPUT_DIR}/en-US/language/index.html" "fn saturate" "en-US renders English keywords"
        smoke_contains "${OUTPUT_DIR}/en-US/language/types.html" "const int" "en-US types page in English"
        smoke_contains "${OUTPUT_DIR}/en-US/toolchain/index.html" "faber check" "toolchain index shows commands"
        # Retired paths must redirect, not 404
        smoke_contains "${OUTPUT_DIR}/en-US/syntax/types.html" "http-equiv=\"refresh\"" "retired syntax path redirects"
        smoke_contains "${OUTPUT_DIR}/en-US/index.html" 'data-search' "renderbar searchbox"
        smoke_contains "${OUTPUT_DIR}/en-US/index.html" 'faber-search.js' "search script include"
        smoke_contains "${OUTPUT_DIR}/en-US/index.html" 'faber-ambient.js' "ambient script include"
        smoke_contains "${OUTPUT_DIR}/index.html" 'faber-ambient.js' "landing ambient script include"
        smoke_contains "${OUTPUT_DIR}/porta/index.html" 'faber-ambient.js' "portal ambient script include"
        if grep -Eq '^Disallow: /(ar|th-TH|vi|hi|zh-Hans|zh-Hant)/' "${OUTPUT_DIR}/robots.txt"; then
            echo "ERROR: robots.txt must not disallow locale trees" >&2
            exit 1
        fi

        # Landing page checks (/) — user outcome, honesty bounds, and proofs.
        # The capability ladder is no longer a card grid: each rung is stated by
        # the section that demonstrates it, so the checks below assert the
        # not-shipped boundaries survive rather than looking for the old grid.
        smoke_contains "${OUTPUT_DIR}/index.html" 'class="landing"' "landing body class"
        smoke_contains "${OUTPUT_DIR}/index.html" "Write compute programs" "landing headline"
        smoke_contains "${OUTPUT_DIR}/index.html" "device inference is not shipped" "landing inference bound"
        smoke_contains "${OUTPUT_DIR}/index.html" "Readable in your language" "landing locale axis"
        smoke_contains "${OUTPUT_DIR}/index.html" "Training through Metal or CUDA" "landing training section"
        smoke_contains "${OUTPUT_DIR}/index.html" "faber run --backend cuda" "landing CUDA route"
        smoke_contains "${OUTPUT_DIR}/index.html" "Inference is being built next" "landing inference status"
        smoke_contains "${OUTPUT_DIR}/index.html" "Future · multi-device scale" "landing multi-device status"
        smoke_contains "${OUTPUT_DIR}/index.html" "const list&lt;f32&gt; flat_a" "landing English reader panel"
        smoke_contains "${OUTPUT_DIR}/index.html" "fixum lista&lt;f32&gt; flat_a" "landing Latin reader panel"
        smoke_contains "${OUTPUT_DIR}/index.html" "ภาษาไทย" "landing Thai reader panel"
        smoke_contains "${OUTPUT_DIR}/index.html" "tf32" "landing demo shows tensor types"
        smoke_contains "${OUTPUT_DIR}/index.html" "a.matmul(b)" "landing demo shows matrix multiplication"
        smoke_contains "${OUTPUT_DIR}/index.html" "tensor_matmul" "landing WASM target shows tensor lowering"
        smoke_contains "${OUTPUT_DIR}/index.html" "@compute @workgroup_size" "landing WGSL target panel"
        smoke_contains "${OUTPUT_DIR}/index.html" "metal_stdlib" "landing Metal target panel"
        smoke_contains "${OUTPUT_DIR}/index.html" "triga-budapest.png" "landing GPU frame"
        # The reader axis must never present Latin under an English label again.
        if grep -q 'fl-loc-t-en[^>]*>English' "${OUTPUT_DIR}/index.html" \
           && grep -q 'fl-loc-p-en[^>]*>.*functio ' "${OUTPUT_DIR}/index.html"; then
            echo "ERROR: landing English reader panel is rendering Latin" >&2
            exit 1
        fi
        smoke_contains "${OUTPUT_DIR}/index.html" 'href="/porta/"' "landing portal link"
        for frame in triga-budapest triga-terrain triga-geometries; do
            if [ ! -s "${OUTPUT_DIR}/images/${frame}.png" ]; then
                echo "ERROR: landing frame asset missing: images/${frame}.png" >&2
                exit 1
            fi
        done
        # Must NOT be a meta-refresh redirect
        if grep -Fq 'http-equiv="refresh"' "${OUTPUT_DIR}/index.html"; then
            echo "ERROR: landing index must not meta-refresh" >&2
            exit 1
        fi

        # Portal checks (/porta/)
        smoke_contains "${OUTPUT_DIR}/porta/index.html" 'class="porta"' "portal body class"
        smoke_contains "${OUTPUT_DIR}/porta/index.html" "ภาษาไทย" "portal Thai native"
        smoke_contains "${OUTPUT_DIR}/porta/index.html" "العربية" "portal Arabic native"
        smoke_contains "${OUTPUT_DIR}/porta/index.html" "简体中文" "portal zh-Hans native"
        smoke_contains "${OUTPUT_DIR}/porta/index.html" 'href="/en-US/"' "portal en-US link"

        # Redirect stub checks
        smoke_contains "${OUTPUT_DIR}/start/install.html" "<!DOCTYPE html>" "redirect install doctype"
        smoke_contains "${OUTPUT_DIR}/start/install.html" "/en-US/start/install.html" "redirect install target"
    fi

    # Step 9: Post-process
    echo "[9/10] Post-processing..."
    "$PYTHON" "${SCRIPT_DIR}/strip-empty-sources.py" "$OUTPUT_DIR"
    "$PYTHON" "${SCRIPT_DIR}/inject-skip-link.py" "$OUTPUT_DIR"

    echo "[9/10] Chrome injection..."
    for site in "${LOCALE_DIRS[@]}"; do
        if [ -f "${SCRIPT_DIR}/../locales/${site}/chrome.toml" ]; then
            "$PYTHON" "${SCRIPT_DIR}/inject-chrome.py" "$OUTPUT_DIR" "$site"
        fi
    done

    # Presentation post-process. Diagram rendering needs Node and a headless
    # browser, so it is best-effort: a machine without them keeps the cached
    # SVGs it already has, and any diagram with no cache entry stays a
    # readable code block rather than failing the build.
    echo "[9/10] Diagrams..."
    "$PYTHON" "${SCRIPT_DIR}/diagrams.py" render "${REPO_DIR}/src" || \
        echo "  WARNING: diagram render skipped; using cached SVGs only" >&2
    "$PYTHON" "${SCRIPT_DIR}/diagrams.py" inject "$OUTPUT_DIR"

    # Before highlighting: the tab cards carry per-locale panels, and each
    # panel names its own reader locale so the highlighter paints it in that
    # locale's spellings. Injecting after highlighting would leave them plain.
    echo "[9/10] Reader-locale example tabs..."
    "$PYTHON" "${SCRIPT_DIR}/locale-tabs.py" inject "$OUTPUT_DIR"

    # Inline language terms follow the reader locale, same as the fences.
    # Runs before highlighting so the highlighter paints the local spelling
    # rather than a Latin one that is no longer on the page.
    echo "[9/10] Reader-locale inline terms..."
    "$PYTHON" "${SCRIPT_DIR}/localize-spans.py" "$OUTPUT_DIR"

    echo "[9/10] Code highlighting..."
    "$PYTHON" "${SCRIPT_DIR}/highlight-code.py" "$OUTPUT_DIR"

    echo "[9/10] Contents rails..."
    "$PYTHON" "${SCRIPT_DIR}/inject-toc.py" "$OUTPUT_DIR"

    # Step 10: Gates (link check, leakage) — only for full site
    echo "[10/10] Gates..."
    echo "  [gate] Width gate..."
    "$PYTHON" "${SCRIPT_DIR}/check-width-gate.py"

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
    "${SCRIPT_DIR}/generate-sitemap" "$OUTPUT_DIR" "https://faberlang.dev"
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
        (cd "$BUILD_DIR" && cargo build --release --quiet 2>/dev/null)
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
