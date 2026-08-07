#!/usr/bin/env bash
# capture-lane-panels.sh — regenerate the Target lanes section's panels.
#
# The Target lanes pages put Faber source beside what it lowers to. Every
# generated panel here is captured compiler output, never hand-authored, for
# the same reason the landing panels are: a page that claims "this is the Rust
# we emit" must be showing the Rust we actually emit.
#
# Several scenarios, each emitted to every target that accepts it. A target
# that cannot lower a scenario is recorded as a gap rather than quietly
# skipped — that absence is information, and generate-target-lanes.py renders
# it as such.
#
# Re-run after a compiler upgrade, then rebuild:
#   bash generator/scripts/capture-lane-panels.sh
#   bash generator/scripts/build-site.sh
#
# Requires `radix`.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR_DIR="$(dirname "$SCRIPT_DIR")"
WORKSPACE="$(cd "${GENERATOR_DIR}/../.." && pwd)"

# Prefer the repo's own build over PATH; a stale copy silently captures panels
# against a compiler that is not the one the site documents.
for candidate in "${WORKSPACE}/radix/target/release/radix" \
                 "${WORKSPACE}/radix/target/debug/radix"; do
    [ -x "$candidate" ] && RADIX="$candidate" && break
done
RADIX="${RADIX:-radix}"
echo "toolchain: $("$RADIX" --version) at ${RADIX}"

OUT="${GENERATOR_DIR}/lanes"
SRC="${OUT}/scenarios"
mkdir -p "${SRC}" "${OUT}/out"
rm -f "${OUT}/out/"*.txt

# Application and systems lanes take ordinary programs.
HOST_TARGETS="rust go ts faber llvm-text wasm-text"
# Device lanes need an `@ nucleum` kernel, which is a different kind of source.
DEVICE_TARGETS="wgsl-text metal-text"

capture() {
    local scenario="$1"
    local targets="$2"
    local file="${SRC}/${scenario}.fab"

    [ -f "$file" ] || { echo "  missing scenario: $file" >&2; return; }
    echo "scenario: ${scenario}"
    for t in $targets; do
        if "$RADIX" emit --target "$t" "$file" \
            > "${OUT}/out/${scenario}.${t}.txt" 2>/dev/null \
            && [ -s "${OUT}/out/${scenario}.${t}.txt" ]; then
            printf '  %-11s %s lines\n' "$t" "$(wc -l < "${OUT}/out/${scenario}.${t}.txt" | tr -d ' ')"
        else
            rm -f "${OUT}/out/${scenario}.${t}.txt"
            printf '  %-11s no lowering — recorded as a gap\n' "$t"
        fi
    done
}

capture tensores "$HOST_TARGETS"
capture fallibilis "$HOST_TARGETS"
capture collectiones "$HOST_TARGETS"
capture nucleum "$DEVICE_TARGETS"

echo "panels → ${OUT}/out"
