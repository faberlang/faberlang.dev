#!/usr/bin/env bash
# speculum-run.sh — interpreted runner for the Speculum generator.
#
# `faber build -t rust` is blocked at plan time on current radix: the
# generator's file I/O routes through norma:fs (`call 'solum:lege'` frames),
# and no host provider serves those routes since the native host was dropped
# with `hosts` (native I/O returns with core-norma N2). The MIR runner serves
# solum in-process, so the package runs interpreted:
#
#   speculum-run.sh --page <iter> <source.md> <site> [reader] [style]
#
# Args are the compiled binary's contract minus its leading `--` (faber's own
# `--` separator replaces it), so call sites read the same as before.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKSPACE_DIR="$(cd "$GENERATOR_DIR/../.." && pwd)"
FABER="${FABER:-${WORKSPACE_DIR}/radix/target/debug/faber}"
if [[ ! -x "$FABER" ]]; then
    echo "speculum-run: faber binary not found: $FABER (set FABER)" >&2
    exit 1
fi
exec "$FABER" run "$GENERATOR_DIR" -- "$@"
