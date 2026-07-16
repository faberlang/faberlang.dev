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
# Step 1: Build the generator binary (once)
# ------------------------------------------------------------------
echo "[1/4] Building generator..."
"$FABER" build "$GENERATOR_DIR" -t rust 2>/dev/null

MAIN_RS="${BUILD_DIR}/src/main.rs"
if [ ! -f "$MAIN_RS" ]; then
    echo "ERROR: generated main.rs not found at $MAIN_RS"
    exit 1
fi

# Patch main() to read a file and call genera()
MAIN_RS_PATH="$MAIN_RS" python3 << 'PYEOF'
import os, sys

path = os.environ["MAIN_RS_PATH"]
with open(path, "r") as f:
    src = f.read()

# Check if already patched
if "speculum-gen" in src:
    sys.exit(0)

new_main = '''fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: speculum-gen <source.md> [locale] [stylesheet]");
        std::process::exit(1);
    }
    let source_path = &args[1];
    let locale = if args.len() > 2 { args[2].clone() } else { "la".to_string() };
    let stylesheet = if args.len() > 3 { args[3].clone() } else { "/speculum.css".to_string() };
    let source = std::fs::read_to_string(source_path).expect("failed to read source file");
    let iter = deriva_iter(source_path.clone());
    let html = genera(source, iter, locale, stylesheet);
    println!("{}", html);
}'''

idx = src.find("fn main()")
if idx < 0:
    print("ERROR: fn main() not found", file=sys.stderr)
    sys.exit(1)

brace_start = src.find("{", idx)
depth = 0
end = brace_start
for i in range(brace_start, len(src)):
    if src[i] == "{":
        depth += 1
    elif src[i] == "}":
        depth -= 1
        if depth == 0:
            end = i + 1
            break

result = src[:idx] + new_main + src[end:]
with open(path, "w") as f:
    f.write(result)
PYEOF

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

# Count results
PAGE_COUNT=$(find "$OUTPUT_DIR" -name "*.html" -type f | wc -l | tr -d ' ')

echo ""
echo "=== Build complete: ${PAGE_COUNT} pages rendered to ${OUTPUT_DIR} ==="
