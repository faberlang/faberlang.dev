#!/usr/bin/env bash
# ==========================================================================
# render.sh — Shell wrapper for the Speculum site generator
# ==========================================================================
# The generator package is pure text-to-text. This wrapper handles file I/O
# by building the generator to Rust, injecting a file-reading main(), and
# compiling+running the result.
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

MAIN_RS="${BUILD_DIR}/src/main.rs"
if [ ! -f "$MAIN_RS" ]; then
    echo "ERROR: generated main.rs not found at $MAIN_RS"
    exit 1
fi

# Patch the generated main() to read a file and call genera().
# Uses brace-depth tracking to find the full main() block.
MAIN_RS_PATH="$MAIN_RS" python3 << 'PYEOF'
import os, sys

path = os.environ["MAIN_RS_PATH"]
with open(path, "r") as f:
    src = f.read()

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

echo "Compiling..." >&2
(cd "$BUILD_DIR" && cargo build --quiet 2>/dev/null)

echo "Rendering $SOURCE..." >&2
if [ -n "$OUTPUT" ]; then
    "${BUILD_DIR}/target/debug/speculum-gen" "$SOURCE" "$LOCALE" "$STYLESHEET" > "$OUTPUT"
    echo "Wrote: $OUTPUT" >&2
else
    "${BUILD_DIR}/target/debug/speculum-gen" "$SOURCE" "$LOCALE" "$STYLESHEET"
fi
