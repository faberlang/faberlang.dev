#!/usr/bin/env bash
# ==========================================================================
# build-site.sh — Batch render all Markdown pages to a static site
# ==========================================================================
# Renders the maintained src/en-US tree into dist/en-US, with reader-pack
# surfaces and aliases for retired locale URLs.
#
# Usage:
#   build-site.sh                                       # full site
#   build-site.sh <source_dir> <output_dir> <site_locale> <reader_locale>
#
# Full site: generates English source pages, renders en-US, writes URL aliases,
# then runs smoke tests, post-process, gates, and sitemap.
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

if [ -z "$PYTHON" ]; then
    echo "ERROR: Python 3 is required" >&2
    exit 1
fi
RENDERER="${SCRIPT_DIR}/speculum_py.py"
FABER="${FABER:-faber}"
# Toolchain for the fence-localize (transcode) step. Defaults to $FABER;
# pin separately when reader packs are newer than the installed faber's
# pack validator (e.g. FABER_LOCALIZE=path/to/workspace-faber).
FABER_LOCALIZE="${FABER_LOCALIZE:-$FABER}"
# Rendering source INTO a reader locale is `faber convert --to`; radix cannot
# do it (`emit -t faber` is canonical Latin by definition). Prefer the
# workspace build, which is current with the packs, but fall back to the
# resolving binary when that build is absent or does not support convert.
WORKSPACE_FABER="${WORKSPACE_DIR}/radix/target/release/faber"
if [ -x "$WORKSPACE_FABER" ] && [ "${FABER_LOCALIZE}" = "$FABER" ] \
    && "$WORKSPACE_FABER" convert --help >/dev/null 2>&1; then
    FABER_LOCALIZE="$WORKSPACE_FABER"
fi
if ! "$FABER_LOCALIZE" convert --help >/dev/null 2>&1; then
    echo "ERROR: ${FABER_LOCALIZE} does not support 'faber convert'" >&2
    exit 1
fi
export FABER_LOCALIZE
# Provider manifests are in the container's hosts checkout. In a normal
# checkout WORKSPACE_DIR is already the container root; in this workspace's
# worktree layout, the container root is its parent.
SUPPORT_PATH_ROOT="$WORKSPACE_DIR"
if [ ! -f "$SUPPORT_PATH_ROOT/hosts/crates/solum/src/manifest.json" ] \
    && [ -f "$SUPPORT_PATH_ROOT/../hosts/crates/solum/src/manifest.json" ]; then
    SUPPORT_PATH_ROOT="$(cd "$SUPPORT_PATH_ROOT/.." && pwd)"
fi
if [ -f "$SUPPORT_PATH_ROOT/hosts/crates/solum/src/manifest.json" ]; then
    export FABER_SUPPORT_PATH_OVERRIDE="${FABER_SUPPORT_PATH_OVERRIDE:-$SUPPORT_PATH_ROOT}"
fi
BUILD_DIR="${GENERATOR_DIR}/target/faber"

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

    if ! grep -Fq "$needle" "$file" \
       && ! sed 's/<[^>]*>//g' "$file" | grep -Fq "$needle"; then
        echo "ERROR: smoke failed ${label}: missing ${needle} in ${file}" >&2
        exit 1
    fi
}

# ------------------------------------------------------------------
# Parse invocation mode
# ------------------------------------------------------------------
FULL_SITE=false
FORCE_FULL=false
if [ "${1:-}" = "--full" ]; then FORCE_FULL=true; shift; fi

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
    echo "  build-site.sh [--full]                              # incremental; --full forces clean rebuild"
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

    local render_source="$src"
    local localized_source=""

    # Every locale renders its code in its own reader locale, English
    # included. Latin stays the canonical source surface in src/ and the
    # interchange dialect the compiler uses internally, but a reader who chose
    # the English site did not choose to decode Latin keywords: `la` is a
    # reference surface here, not the one the page presents.
    if [ "$reader" != "la" ]; then
        localized_source="${GENERATOR_DIR}/target/localized-${site}"
        mkdir -p "${GENERATOR_DIR}/target"
        if [ "$FORCE_FULL" = true ] || [ ! -f "${GENERATOR_DIR}/target/build-manifest.json" ]; then
            loc_fingerprint=$("$PYTHON" "${SCRIPT_DIR}/build_manifest.py" hash "$src" "${SCRIPT_DIR}/localize-markdown.py" "${SCRIPT_DIR}/project-reader-terms.py" "${WORKSPACE_DIR}/radix/locale/${reader}/pack.toml")
            if [ ! -f "${localized_source}/.fingerprint" ] || [ "$(cat "${localized_source}/.fingerprint")" != "$loc_fingerprint" ]; then
                rm -rf "$localized_source"; mkdir -p "$localized_source"
                "${SCRIPT_DIR}/localize-markdown.py" "$src" "$localized_source" --locale "$reader" --faber "$FABER_LOCALIZE"
                "$PYTHON" "${SCRIPT_DIR}/project-reader-terms.py" "$localized_source" --locale "$reader"
                printf '%s' "$loc_fingerprint" > "${localized_source}/.fingerprint"
            fi
            render_source="$localized_source"
        else
            # Incremental mode reads authored Markdown first. A stale page is
            # localized alone below, avoiding whole-tree conversions on edits.
            render_source="$src"
        fi
    fi

    # Render only stale pages into an isolated tree. Post-process that tree,
    # then replace only those outputs so unchanged dist pages are untouched.
    local stage="${GENERATOR_DIR}/target/page-stage"
    rm -rf "$stage"
    mkdir -p "$stage"
    local changed=0
    while IFS= read -r md_file; do
        rel_path="${md_file#${render_source}/}"
        iter="${rel_path%.md}"
        out_path="${out}/${iter}.html"
        rel_output="${site}/${iter}.html"
        localized_file="${localized_source}/${rel_path}"
        local_inputs=("${src}/${rel_path}" "${SCRIPT_DIR}/speculum_py.py" \
          "${SCRIPT_DIR}/inject-chrome.py" "${GENERATOR_DIR}/locales/${site}/chrome.toml" \
          "${SCRIPT_DIR}/inject-skip-link.py" "${SCRIPT_DIR}/strip-empty-sources.py" \
          "${SCRIPT_DIR}/localize-spans.py" "${WORKSPACE_DIR}/radix/locale/en/pack.toml" \
          "${SCRIPT_DIR}/highlight-code.py" "${GENERATOR_DIR}/locale-tabs/vocab.en.json" \
          "${SCRIPT_DIR}/inject-toc.py" "${SCRIPT_DIR}/tag-glyph-chips.py" \
          "${SCRIPT_DIR}/matrix-cells.py" "${SCRIPT_DIR}/diagrams.py" \
          "${SCRIPT_DIR}/locale-tabs.py" "${SCRIPT_DIR}/inject-pass.py" \
          "${GENERATOR_DIR}/www/speculum.css")
        if [ "$reader" != "la" ]; then
            local_inputs+=("$localized_file" "${WORKSPACE_DIR}/radix/locale/${reader}/pack.toml" "${SCRIPT_DIR}/localize-markdown.py" "${SCRIPT_DIR}/project-reader-terms.py")
        fi
        cached=$("$PYTHON" "${SCRIPT_DIR}/build_manifest.py" current "$rel_output" "${local_inputs[@]}")
        if [ "$cached" = yes ] && [ -f "$out_path" ]; then
            continue
        fi
        if [ "$reader" != la ] && [ "$render_source" = "$src" ]; then
            one_source="${GENERATOR_DIR}/target/page-localize-input"
            one_output="${GENERATOR_DIR}/target/page-localize-output"
            rm -rf "$one_source" "$one_output"
            mkdir -p "$(dirname "${one_source}/${rel_path}")"
            cp "${src}/${rel_path}" "${one_source}/${rel_path}"
            "$PYTHON" "${SCRIPT_DIR}/localize-markdown.py" "$one_source" "$one_output" --locale "$reader" --faber "$FABER_LOCALIZE"
            "$PYTHON" "${SCRIPT_DIR}/project-reader-terms.py" "${one_output}/${rel_path}" --locale "$reader"
            mkdir -p "$(dirname "$localized_file")"
            cp "${one_output}/${rel_path}" "$localized_file"
            md_file="$localized_file"
        fi
        stage_page="${stage}/${site}/${iter}.html"
        mkdir -p "$(dirname "$stage_page")"
        if "$PYTHON" "$RENDERER" --page "$iter" "$md_file" "$site" "$reader" "$style" > "$stage_page" 2>/dev/null; then
            echo "  ↻ ${iter}.html"
            changed=$((changed + 1))
        else
            echo "  ✗ FAILED: ${rel_path}"
            rm -f "$stage_page"
        fi
    done < <(find "$render_source" -name "*.md" -type f | sort)
    if [ "$changed" -gt 0 ]; then
        while IFS= read -r rendered; do
            rel="${rendered#${stage}/}"
            mkdir -p "$(dirname "${OUTPUT_DIR}/${rel}")"
            cp "$rendered" "${OUTPUT_DIR}/${rel}"
        done < <(find "$stage/${site}" -name '*.html' -type f)
    fi
    echo "  [incremental] ${changed} authored pages rendered"
}

# ==================================================================
# FULL SITE BUILD
# ==================================================================
if [ "$FULL_SITE" = true ]; then
    if [ "$FORCE_FULL" = true ]; then rm -f "${GENERATOR_DIR}/target/build-manifest.json"; fi

    # Step 0: Refresh generated matrix pages when the radix grammar is present
    if [ -f "${WORKSPACE_DIR}/radix/grammar/EBNF_MATRIX.md" ]; then
        echo "[0/10] Generating target compatibility matrix pages..."
        "$PYTHON" "${SCRIPT_DIR}/generate-target-matrix.py" --locale en-US
    else
        echo "[0/10] Skipping target matrix generate (no ${WORKSPACE_DIR}/radix/grammar/EBNF_MATRIX.md)"
    fi

    # Step 0b: Regenerate the sections assembled from captured panels and
    # sibling checkouts. All of these write src/ and so must run before the
    # render. Each degrades to leaving its committed output alone when its
    # inputs are absent, so a checkout without siblings still builds.
    echo "[0/10] Generating target lanes, grammar, and localization..."
    "$PYTHON" "${SCRIPT_DIR}/generate-target-lanes.py" --output-dir "${REPO_DIR}/src/en-US/targets"
    "$PYTHON" "${SCRIPT_DIR}/generate-localization.py" --output "${REPO_DIR}/src/en-US/localization.md"
    "$PYTHON" "${SCRIPT_DIR}/generate-overview.py" --output "${REPO_DIR}/src/en-US/language/overview.md"
    if [ -f "${WORKSPACE_DIR}/radix/grammar/EBNF.md" ]; then
        "${SCRIPT_DIR}/generate-grammar" --locale en-US
    else
        echo "  Skipping grammar generate (no ${WORKSPACE_DIR}/radix/grammar/EBNF.md)"
    fi
    "$PYTHON" "${SCRIPT_DIR}/generate-grammar-tree.py"

    # The agent locales table joins the eight reader packs in radix/locale. It
    # writes static/ and dist/ rather than src/, so it must run before the
    # static copy. --strict fails on drift that is neither a designed shape nor
    # the expected list in agent_locales.py.
    echo "[0/10] Generating the agent locales table..."
    "$PYTHON" "${SCRIPT_DIR}/generate-agent-locales.py" --strict

    # The reader-locale reference joins the same packs. Diagnostics captures
    # are a committed cache refreshed by hand (capture-locale-diagnostics.sh),
    # so the build never depends on a faber run here. --check is Gate E: the
    # mapping pages must match the pack join with zero dead and zero missing
    # rows.
    if [ -d "${WORKSPACE_DIR}/radix/locale" ]; then
        echo "[0/10] Generating the reader-locale reference..."
        "$PYTHON" "${SCRIPT_DIR}/generate-locale-reference.py" \
            --packs "${WORKSPACE_DIR}/radix/locale" --check
    fi

    # The agent reference mirrors the compiler's explain registry, so it needs
    # a faber binary that can resolve its reference pack. The workspace
    # development build is preferred; the generator reports when none is found
    # rather than emptying the tree.
    agent_reference_inputs=("${SCRIPT_DIR}/generate-agent-reference.py" "${WORKSPACE_DIR}/radix/locale" "${WORKSPACE_DIR}/radix/target/debug/faber")
    agent_reference_output="agents/reference/index.md"
    if [ "$FORCE_FULL" = true ] || [ "$("$PYTHON" "${SCRIPT_DIR}/build_manifest.py" current "$agent_reference_output" "${agent_reference_inputs[@]}")" != yes ]; then
        echo "[0/10] Generating the agent reference tree..."
        if "$PYTHON" "${SCRIPT_DIR}/generate-agent-reference.py" --strict; then
            "$PYTHON" "${SCRIPT_DIR}/build_manifest.py" record "$agent_reference_output" "${agent_reference_inputs[@]}"
        else
            echo "ERROR: agent reference generate failed" >&2
            exit 1
        fi
    else
        echo "[0/10] Agent reference unchanged; skipped (~197 explain calls)"
    fi

    # Releases is NOT regenerated here: it needs `gh` and network access, and a
    # build that silently depends on the network is a build that breaks on a
    # plane. Run generate-releases.py by hand when a release lands.

    # Step 1: Python renderer availability
    echo "[1/9] Python renderer: $PYTHON"
    "$PYTHON" -c 'import sys; assert sys.version_info >= (3, 9)'

    # Step 2: Prepare output directory. Only --full discards the old tree.
    echo "[2/9] Preparing output directory..."
    if [ "$FORCE_FULL" = true ]; then rm -rf "$OUTPUT_DIR"; fi
    mkdir -p "$OUTPUT_DIR"

    # Copy stylesheet
    cp "${GENERATOR_DIR}/www/speculum.css" "${OUTPUT_DIR}/speculum.css"

    # Copy static agent surfaces
    STATIC_DIR="${REPO_DIR}/static"
    if [ -d "$STATIC_DIR" ] && [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
        echo "  copying static/ → dist/"
        cp -R "${STATIC_DIR}/." "${OUTPUT_DIR}/"
    fi

    # Corpus is a single deterministic batch. Its fingerprint covers source
    # exempla, pack projection, renderer/driver, and corpus post-processors.
    corpus_inputs=("${WORKSPACE_DIR}/radix/corpus" "${WORKSPACE_DIR}/radix/locale/en/pack.toml"
      "${SCRIPT_DIR}/corpus_ia.py" "${SCRIPT_DIR}/corpus_locale.py" "${SCRIPT_DIR}/project_reader_terms.py"
      "${SCRIPT_DIR}/render-corpus-batch.sh" "${RENDERER}" "${SCRIPT_DIR}/diagrams.py"
      "${SCRIPT_DIR}/highlight-code.py" "${SCRIPT_DIR}/inject-toc.py" "${SCRIPT_DIR}/tag-glyph-chips.py"
      "${SCRIPT_DIR}/localize-spans.py" "${SCRIPT_DIR}/inject-chrome.py" "${SCRIPT_DIR}/strip-empty-sources.py"
      "${SCRIPT_DIR}/inject-skip-link.py" "${GENERATOR_DIR}/locales/en-US/chrome.toml")
    corpus_changed=false
    if [ "$FORCE_FULL" = true ] || [ "$("$PYTHON" "${SCRIPT_DIR}/build_manifest.py" current "en-US/corpus/index.html" "${corpus_inputs[@]}")" != yes ]; then
        corpus_changed=true
        echo "[corpus] Inputs changed; rebuilding corpus batch..."
        rm -rf "${OUTPUT_DIR}/en-US/corpus"
        "${SCRIPT_DIR}/render-corpus-batch.sh" "${OUTPUT_DIR}/en-US" en-US en "$STYLESHEET"
        corpus_stage="${GENERATOR_DIR}/target/corpus-stage"
        rm -rf "$corpus_stage"; mkdir -p "$corpus_stage/en-US"
        cp -R "${OUTPUT_DIR}/en-US/corpus" "$corpus_stage/en-US/"
        "$PYTHON" "${SCRIPT_DIR}/strip-empty-sources.py" "$corpus_stage"
        "$PYTHON" "${SCRIPT_DIR}/inject-skip-link.py" "$corpus_stage"
        "$PYTHON" "${SCRIPT_DIR}/inject-chrome.py" "$corpus_stage" en-US
        "$PYTHON" "${SCRIPT_DIR}/diagrams.py" inject "$corpus_stage"
        "$PYTHON" "${SCRIPT_DIR}/locale-tabs.py" inject "$corpus_stage"
        "$PYTHON" "${SCRIPT_DIR}/localize-spans.py" "$corpus_stage"
        "$PYTHON" "${SCRIPT_DIR}/highlight-code.py" "$corpus_stage"
        "$PYTHON" "${SCRIPT_DIR}/matrix-cells.py" "$corpus_stage"
        "$PYTHON" "${SCRIPT_DIR}/inject-toc.py" "$corpus_stage"
        "$PYTHON" "${SCRIPT_DIR}/tag-glyph-chips.py" "$corpus_stage"
        cp -R "$corpus_stage/en-US/corpus/." "${OUTPUT_DIR}/en-US/corpus/"
        "$PYTHON" "${SCRIPT_DIR}/build_manifest.py" record "en-US/corpus/index.html" "${corpus_inputs[@]}"
    else
        echo "[corpus] Inputs unchanged; skipped"
    fi

    # U4 maintains one prose tree. Reader packs remain available in generated surfaces.
    LOCALE_DIRS=("en-US")
    echo "[4/9] Rendering the en-US tree..."
    site="en-US"
    reader=$("$PYTHON" "${SCRIPT_DIR}/locales_registry.py" reader "$site")
    render_locale "${REPO_DIR}/src/${site}" "${OUTPUT_DIR}/${site}" "$site" "$reader" "$STYLESHEET"

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
            --output-dir "${OUTPUT_DIR}" --locale en-US
    fi

    # Step 5b: Retired-path stubs from the 2026-08 IA restructure
    "$PYTHON" "${SCRIPT_DIR}/ia-redirects.py" stubs
    # Retired translated URLs remain addressable as English aliases.
    "$PYTHON" "${SCRIPT_DIR}/retired-locales.py" stubs --dist "$OUTPUT_DIR"

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
    # The current release is stated once, in the agent lobby static/install.md
    # ("Current release: Faber X.Y.Z."). Reading it back from there keeps a
    # version bump a content edit rather than a build-script edit, and still
    # fails closed if the install skill or the skill catalog were left on the
    # previous version.
    current_faber="$(sed -n 's/^Current release: Faber \(.*\)\.$/\1/p' \
        "${REPO_DIR}/static/install.md" | head -1)"
    if [ -z "$current_faber" ]; then
        echo "ERROR: smoke could not read the current version from static/install.md" >&2
        exit 1
    fi
    smoke_contains "${OUTPUT_DIR}/en-US/index.html" "<!DOCTYPE html>" "home doctype"
    if [ "${SPECULUM_SKIP_STATIC:-0}" != "1" ]; then
        smoke_contains "${OUTPUT_DIR}/en-US/index.html" "/llms.txt" "home agent link"
        smoke_contains "${OUTPUT_DIR}/llms-full.txt" "Generated corpus frontmatter reference" "llms-full surface"
        # The agent front door: /llms.txt points at /install.md, the lobby
        # states the current release, and the skill and catalog carry it.
        smoke_contains "${OUTPUT_DIR}/llms.txt" "https://faberlang.dev/install.md" "llms.txt install pointer"
        smoke_contains "${OUTPUT_DIR}/install.md" "Current release: Faber ${current_faber}." "install lobby version"
        smoke_contains "${OUTPUT_DIR}/.well-known/agent-skills/install/SKILL.md" "faber-v${current_faber}" "install skill release link"
        smoke_contains "${OUTPUT_DIR}/.well-known/agent-skills/index.json" "\"version\": \"${current_faber}\"" "skill catalog version"
        smoke_contains "${OUTPUT_DIR}/en-US/start/install.html" "url=/en-US/start/" "retired install page redirects to start"
        smoke_contains "${OUTPUT_DIR}/en-US/cheatsheet/commands.html" "faber check" "cheat sheet commands"
        smoke_contains "${OUTPUT_DIR}/en-US/cheatsheet/index.html" "Cheat sheet" "cheat sheet index"
        smoke_contains "${OUTPUT_DIR}/en-US/cheatsheet/errors.html" "error channel" "cheat sheet errors"
        smoke_contains "${OUTPUT_DIR}/en-US/examples/index.html" "url=/en-US/cheatsheet/" "retired examples index redirects to the cheat sheet"
        smoke_contains "${OUTPUT_DIR}/en-US/examples/cat.html" "url=/en-US/cheatsheet/" "retired example page redirects to the cheat sheet"
        smoke_contains "${OUTPUT_DIR}/examples/cat.html" "url=/en-US/examples/cat.html" "retired root example stub"
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
        smoke_contains "${OUTPUT_DIR}/search-index.en-US.json" '"d":"fn"' "search index English slugs"
        smoke_contains "${OUTPUT_DIR}/en-US/corpus/fn.html" "<title>fn — Faber</title>" "localized corpus fn page"
        smoke_contains "${OUTPUT_DIR}/en-US/corpus/functio.html" "url=/en-US/corpus/fn.html" "latin corpus identity redirects"
        # IA restructure: the five journey sections must all render
        for sec in language toolchain libraries reference; do
            smoke_contains "${OUTPUT_DIR}/en-US/${sec}/index.html" "<!DOCTYPE html>" "${sec} index"
        done
        smoke_contains "${OUTPUT_DIR}/en-US/language/index.html" "saturate" "language index shows code"
        # Library pages and their sidebar entries
        for lib in norma triga gradus tela inferentia; do
            smoke_contains "${OUTPUT_DIR}/en-US/libraries/${lib}.html" "<!DOCTYPE html>" "library page ${lib}"
            smoke_contains "${OUTPUT_DIR}/en-US/libraries/index.html" "/libraries/${lib}.html" "libraries index links ${lib}"
            smoke_contains "${OUTPUT_DIR}/en-US/index.html" "/en-US/libraries/${lib}.html" "sidebar library link ${lib}"
        done
        smoke_contains "${OUTPUT_DIR}/en-US/libraries/tela.html" "html_view" "Tela page shows the serializer"
        smoke_contains "${OUTPUT_DIR}/en-US/libraries/inferentia.html" "/generate" "Inferentia page lists the API"
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
        if grep -Eq '^Disallow: /(ar|th-TH|vi|hi|zh-Hans|zh-Hant)/' "${OUTPUT_DIR}/robots.txt"; then
            echo "ERROR: robots.txt must not disallow locale trees" >&2
            exit 1
        fi

        # Landing page checks (/) — what the language is, the locale doors,
        # the cross-compile proof, the libraries, and the honesty bounds.
        # These run on the raw generated page, before highlighting.
        smoke_contains "${OUTPUT_DIR}/index.html" 'class="landing"' "landing body class"
        smoke_contains "${OUTPUT_DIR}/index.html" "Written by models," "landing headline"
        smoke_contains "${OUTPUT_DIR}/index.html" "Built for models to write" "landing LLM-first section"
        smoke_contains "${OUTPUT_DIR}/index.html" "A mechanical grammar" "landing grammar point"
        smoke_contains "${OUTPUT_DIR}/index.html" "Explicit static and generic types" "landing typing point"
        smoke_contains "${OUTPUT_DIR}/index.html" "Math-oriented operators" "landing operators point"
        smoke_contains "${OUTPUT_DIR}/index.html" "Start in your own language" "landing locale section"
        smoke_contains "${OUTPUT_DIR}/index.html" "Write it once. Put it in the project you already have." "landing cross-compile section"
        smoke_contains "${OUTPUT_DIR}/index.html" "Libraries written in Faber" "landing libraries section"
        smoke_contains "${OUTPUT_DIR}/index.html" "device inference is not shipped" "landing inference bound"
        smoke_contains "${OUTPUT_DIR}/index.html" "fail-closed" "landing device fail-closed bound"
        # Language doors lead to U5 mapping pages; English remains the docs home.
        for locale in ar hi th-TH vi zh-Hans zh-Hant; do
            smoke_contains "${OUTPUT_DIR}/index.html" "href=\"/en-US/language/locales/${locale}.html\"" "landing mapping door ${locale}"
            smoke_contains "${OUTPUT_DIR}/porta/index.html" "href=\"/en-US/language/locales/${locale}.html\"" "portal mapping door ${locale}"
        done
        smoke_contains "${OUTPUT_DIR}/index.html" 'href="/en-US/language/locales/la.html"' "landing Latin mapping door"
        smoke_contains "${OUTPUT_DIR}/index.html" 'href="/en-US/"' "landing English docs door"
        for lib in Norma Gradus Triga Tela Inferentia Cista; do
            smoke_contains "${OUTPUT_DIR}/index.html" "<strong>${lib}</strong>" "landing library ${lib}"
        done
        smoke_contains "${OUTPUT_DIR}/index.html" "const Span bytes ← Span { low = 0.0, high = 255.0 }" "landing English reader panel"
        smoke_contains "${OUTPUT_DIR}/index.html" "fixum Span bytes ← Span { low = 0.0, high = 255.0 }" "landing Latin reader panel"
        smoke_contains "${OUTPUT_DIR}/index.html" "ภาษาไทย" "landing Thai reader panel"
        smoke_contains "${OUTPUT_DIR}/index.html" "÷ 2.0" "landing demo shows true division"
        smoke_contains "${OUTPUT_DIR}/index.html" "pub struct Span" "landing Rust target panel"
        smoke_contains "${OUTPUT_DIR}/index.html" "class Span {" "landing TypeScript/Swift target panel"
        smoke_contains "${OUTPUT_DIR}/index.html" "type Span struct" "landing Go target panel"
        smoke_contains "${OUTPUT_DIR}/index.html" "radix emit --target swift" "landing Swift target panel"
        smoke_contains "${OUTPUT_DIR}/index.html" "<code>faber targets</code>" "landing capability table source"
        smoke_contains "${OUTPUT_DIR}/index.html" "grammar productions" "landing grammar size"
        smoke_contains "${OUTPUT_DIR}/index.html" "triga-budapest.png" "landing Triga frame"
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

        # Instrument theme: both pages carry the shared enhancer (UTC clock,
        # copy buttons), and the landing pass links the one install surface.
        smoke_contains "${OUTPUT_DIR}/index.html" 'faber-instrument.js' "landing instrument script include"
        smoke_contains "${OUTPUT_DIR}/porta/index.html" 'faber-instrument.js' "portal instrument script include"
        smoke_contains "${OUTPUT_DIR}/faber-instrument.js" 'data-copy' "instrument script copied to dist"
        smoke_contains "${OUTPUT_DIR}/index.html" 'class="channel" href="/install.md"' "landing agent pass install link"

        # Redirect stub checks
        smoke_contains "${OUTPUT_DIR}/start/install.html" "<!DOCTYPE html>" "redirect install doctype"
        smoke_contains "${OUTPUT_DIR}/start/install.html" "/en-US/start/install.html" "redirect install target"
    fi

    # Presentation passes operate only on freshly rendered authored pages.
    # Smoke checks above intentionally see raw renderer output, as before.
    authored_stage="${GENERATOR_DIR}/target/page-stage"
    if [ -d "$authored_stage/en-US" ] && [ -n "$(find "$authored_stage/en-US" -name '*.html' -type f -print -quit)" ]; then
        "$PYTHON" "${SCRIPT_DIR}/strip-empty-sources.py" "$authored_stage"
        "$PYTHON" "${SCRIPT_DIR}/inject-skip-link.py" "$authored_stage"
        "$PYTHON" "${SCRIPT_DIR}/inject-chrome.py" "$authored_stage" en-US
        "$PYTHON" "${SCRIPT_DIR}/diagrams.py" inject "$authored_stage"
        "$PYTHON" "${SCRIPT_DIR}/locale-tabs.py" inject "$authored_stage"
        "$PYTHON" "${SCRIPT_DIR}/localize-spans.py" "$authored_stage"
        "$PYTHON" "${SCRIPT_DIR}/highlight-code.py" "$authored_stage"
        "$PYTHON" "${SCRIPT_DIR}/matrix-cells.py" "$authored_stage"
        "$PYTHON" "${SCRIPT_DIR}/inject-toc.py" "$authored_stage"
        "$PYTHON" "${SCRIPT_DIR}/tag-glyph-chips.py" "$authored_stage"
        "$PYTHON" "${SCRIPT_DIR}/inject-pass.py" "$authored_stage"
        while IFS= read -r rendered; do
            rel="${rendered#${authored_stage}/}"
            mkdir -p "$(dirname "${OUTPUT_DIR}/${rel}")"
            cp "$rendered" "${OUTPUT_DIR}/${rel}"
            source_file="${REPO_DIR}/src/${rel%.html}.md"
            localized_file="${GENERATOR_DIR}/target/localized-en-US/${rel#en-US/}"; localized_file="${localized_file%.html}.md"
            manifest_inputs=("$source_file" "${SCRIPT_DIR}/speculum_py.py" "${SCRIPT_DIR}/inject-chrome.py" "${GENERATOR_DIR}/locales/en-US/chrome.toml" "${SCRIPT_DIR}/inject-skip-link.py" "${SCRIPT_DIR}/strip-empty-sources.py" "${SCRIPT_DIR}/localize-spans.py" "${WORKSPACE_DIR}/radix/locale/en/pack.toml" "${SCRIPT_DIR}/highlight-code.py" "${GENERATOR_DIR}/locale-tabs/vocab.en.json" "${SCRIPT_DIR}/inject-toc.py" "${SCRIPT_DIR}/tag-glyph-chips.py" "${SCRIPT_DIR}/matrix-cells.py" "${SCRIPT_DIR}/diagrams.py" "${SCRIPT_DIR}/locale-tabs.py" "${SCRIPT_DIR}/inject-pass.py" "${GENERATOR_DIR}/www/speculum.css" "$localized_file" "${WORKSPACE_DIR}/radix/locale/en/pack.toml" "${SCRIPT_DIR}/localize-markdown.py" "${SCRIPT_DIR}/project-reader-terms.py")
            "$PYTHON" "${SCRIPT_DIR}/build_manifest.py" record "$rel" "${manifest_inputs[@]}"
        done < <(find "$authored_stage/en-US" -name '*.html' -type f)
        rm -rf "$authored_stage"
    fi

    # Source diagrams may refresh their committed cache; page/corpus injection
    # is scoped to only outputs rebuilt above.
    echo "[9/10] Refreshing diagram cache..."
    "$PYTHON" "${SCRIPT_DIR}/diagrams.py" render "${REPO_DIR}/src" || \
        echo "  WARNING: diagram render skipped; using cached SVGs only" >&2

    # Step 10: Gates (link check, leakage) — only for full site
    echo "[10/10] Gates..."
    echo "  [gate] Width gate..."
    "$PYTHON" "${SCRIPT_DIR}/check-width-gate.py"

    echo "  [gate] Internal link check..."
    "$PYTHON" "${SCRIPT_DIR}/check-internal-links.py" "$OUTPUT_DIR" \
        --allow-missing /en-US/language/locales/ar.html \
        --allow-missing /en-US/language/locales/hi.html \
        --allow-missing /en-US/language/locales/th-TH.html \
        --allow-missing /en-US/language/locales/vi.html \
        --allow-missing /en-US/language/locales/zh-Hans.html \
        --allow-missing /en-US/language/locales/zh-Hant.html || {
        echo "ERROR: internal link gate failed" >&2
        exit 1
    }
    "$PYTHON" "${SCRIPT_DIR}/retired-locales.py" check --dist "$OUTPUT_DIR"

    echo "  [gate] Leakage gate..."
    "$PYTHON" "${SCRIPT_DIR}/check-leakage-gate.py" "$OUTPUT_DIR" || {
        echo "ERROR: leakage gate failed" >&2
        exit 1
    }

    # A `faber convert` stamp (`+++ locale = ... +++`) inside a rendered code
    # block means a transcoded fence kept the converter's frontmatter.
    echo "  [gate] Stray frontmatter in rendered code..."
    "$PYTHON" "${SCRIPT_DIR}/check-frontmatter-leak.py" "$OUTPUT_DIR" || {
        echo "ERROR: converter frontmatter leaked into rendered code" >&2
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

    echo "Rendering ${SITE_LOCALE} → ${OUTPUT_DIR}..."
    mkdir -p "$OUTPUT_DIR"
    cp "${GENERATOR_DIR}/www/speculum.css" "${OUTPUT_DIR}/speculum.css"
    render_locale "$SOURCE_DIR" "$OUTPUT_DIR" "$SITE_LOCALE" "$READER_LOCALE" "$STYLESHEET"
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
if [ "$FULL_SITE" = true ]; then "$PYTHON" "${SCRIPT_DIR}/build_manifest.py" prune; fi
echo "=== Build complete: ${PAGE_COUNT} HTML pages, ${STATIC_COUNT} static machine files → ${OUTPUT_DIR} ==="
