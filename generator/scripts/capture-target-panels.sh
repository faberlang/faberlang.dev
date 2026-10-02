#!/usr/bin/env bash
# capture-target-panels.sh — regenerate the By Target pages' compiled-output panels.
#
# The By Target pages put Faber source beside what it actually lowers to. Every
# panel is captured compiler output, never hand-authored, for the same reason
# the landing panels are: a page that claims "this is the Rust we emit" must be
# showing the Rust we actually emit.
#
# Cache law (same as generator/diagrams/ and generator/locale-tabs/): this
# script is a source-side authoring step that needs the toolchain; the site
# build only ever READS generator/target-panels/<target>/. A missing panel
# leaves the committed page's existing panel in place rather than failing the
# build.
#
# A target that cannot lower an exemplar produces no panel for it — the gap is
# information, and generate-target-lanes.py renders it as such. A failure never
# deletes a panel that is already committed.
#
# Re-run after a compiler upgrade, then rebuild:
#   bash generator/scripts/capture-target-panels.sh
#   bash generator/scripts/build-site.sh
#
# Requires `faber` (or the workspace `radix` build). The device emitters are
# currently rejected by the workspace toolchain, so their panels stay at the
# last committed capture; see the header note in generate-target-lanes.py.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR_DIR="$(dirname "$SCRIPT_DIR")"
WORKSPACE="$(cd "${GENERATOR_DIR}/../.." && pwd)"

OUT="${GENERATOR_DIR}/target-panels"
SRC="${OUT}/exemplars"

# Prefer the workspace development build over whatever is on PATH; a stale copy
# silently captures panels against a compiler that is not the one the site
# documents. In a worktree the workspace row(s) live in the sibling checkout,
# so the usual workspace root is searched too. A PATH copy is the last resort
# and is reported.
DEV_ROOT="${FABER_DEV_ROOT:-$HOME/work/faberlang}"
for candidate in \
    "${WORKSPACE}/radix/target/debug/faber" \
    "${WORKSPACE}/radix/target/release/faber" \
    "${WORKSPACE}/../radix/target/debug/faber" \
    "${WORKSPACE}/../radix/target/release/faber" \
    "${DEV_ROOT}/radix/target/debug/faber" \
    "${DEV_ROOT}/radix/target/release/faber"; do
    [ -x "$candidate" ] && FABER="$candidate" && break
done
FABER="${FABER:-faber}"
echo "toolchain: $("$FABER" --version 2>/dev/null || echo unknown) at ${FABER}"

# Application and systems lanes take ordinary programs; the device lanes need
# an `@ nucleum` kernel, which is a different kind of source.
HOST_TARGETS="rust ts go faber llvm-text wasm-text"
DEVICE_TARGETS="wgsl-text metal-text"
HOST_PROGRAMS="tensores fallibilis collectiones"
DEVICE_PROGRAMS="nucleum"

capture() {
    local target="$1"
    local program="$2"
    local dir="${OUT}/${target}"
    local src="${SRC}/${program}.fab"
    local outfile="${dir}/${program}.out.txt"

    [ -f "$src" ] || { echo "  missing exemplar: ${src}" >&2; return; }
    mkdir -p "$dir"

    # `--locale la` declares the canonical Latin input surface. Without it the
    # released `faber emit` warns LOCALE002 per identifier and the diagnostics
    # text would end up beside the panel.
    if "$FABER" emit --locale la -t "$target" "$src" \
        > "${outfile}.tmp" 2>/dev/null && [ -s "${outfile}.tmp" ]; then
        mv -f "${outfile}.tmp" "$outfile"
        cp "$src" "${dir}/${program}.fab"
        printf '  %-11s %-13s %s lines\n' \
            "$target" "$program" "$(wc -l < "$outfile" | tr -d ' ')"
    else
        rm -f "${outfile}.tmp"
        if [ -f "$outfile" ]; then
            printf '  %-11s %-13s no lowering — kept committed panel\n' \
                "$target" "$program"
        else
            printf '  %-11s %-13s no lowering — panel omitted\n' \
                "$target" "$program"
        fi
    fi
}

for target in $HOST_TARGETS; do
    for program in $HOST_PROGRAMS; do
        capture "$target" "$program"
    done
done
for target in $DEVICE_TARGETS; do
    for program in $DEVICE_PROGRAMS; do
        capture "$target" "$program"
    done
done

echo "panels → ${OUT}/<target>/"
