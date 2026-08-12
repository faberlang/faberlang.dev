#!/usr/bin/env bash
# Speculum island: Latin generator module imports tela:tela and the
# three fragments match document_ir bytes. Does not build or rewrite
# the site. document_ir remains the live serializer.
#
# Usage: ./generator/scripts/check-tela-island.sh
set -euo pipefail

GEN="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT="$(cd "$GEN/.." && pwd)"
ISLAND="$GEN/src/tela_island.fab"

if [[ -n "${RADIX_BIN:-}" && -x "${RADIX_BIN}" ]]; then
    :
elif [[ -n "${RADIX:-}" && -x "${RADIX}" ]]; then
    RADIX_BIN="$RADIX"
elif [[ -x "$ROOT/../radix/target/debug/radix" ]]; then
    RADIX_BIN="$ROOT/../radix/target/debug/radix"
elif [[ -x "$GEN/../../radix/target/debug/radix" ]]; then
    RADIX_BIN="$GEN/../../radix/target/debug/radix"
else
    RADIX_BIN="$(command -v radix || true)"
fi

if [[ -z "${RADIX_BIN}" || ! -x "${RADIX_BIN}" ]]; then
    echo "check-tela-island: no radix binary (set RADIX_BIN)" >&2
    exit 1
fi

# Packet layout: hand-12/{faberlang.dev,tela,radix}. Container: faberlang/{faberlang.dev,tela}.
if [[ -f "$ROOT/../tela/src/tela.fab" ]]; then
    export FABER_LIBRARY_HOME="$(cd "$ROOT/.." && pwd)"
elif [[ -f "$ROOT/tela/src/tela.fab" ]]; then
    export FABER_LIBRARY_HOME="$ROOT"
else
    export FABER_LIBRARY_HOME="${FABER_LIBRARY_HOME:-$ROOT/..}"
fi

if [[ ! -f "$FABER_LIBRARY_HOME/tela/src/tela.fab" ]]; then
    echo "check-tela-island: tela not found under FABER_LIBRARY_HOME=$FABER_LIBRARY_HOME" >&2
    exit 1
fi

echo "check-tela-island: radix=$RADIX_BIN"
echo "check-tela-island: FABER_LIBRARY_HOME=$FABER_LIBRARY_HOME"

echo "check-tela-island: radix check (Latin Speculum imports Tela)"
if ! out="$("$RADIX_BIN" check --locale la "$ISLAND" 2>&1)"; then
    echo "$out" >&2
    echo "check-tela-island: expected ok on $ISLAND" >&2
    exit 1
fi
if ! grep -q "^ok:" <<<"$out"; then
    echo "$out" >&2
    echo "check-tela-island: missing ok: line" >&2
    exit 1
fi
echo "$out"

# Runtime: assemble TS (validate + tela + document_ir + island) and execute
# fragmenta_paria(). Surface names on the island bind to Tela's canonical
# English exports. @ts-nocheck: the island emit types tela.Visus, which is a
# locale surface, not a Tela source type.
TELA_SRC="$FABER_LIBRARY_HOME/tela/src"
SCRATCH="$(mktemp -d "${TMPDIR:-/tmp}/tela-island.XXXXXX")"
trap 'rm -rf "$SCRATCH"' EXIT

echo "check-tela-island: emit TS"
"$RADIX_BIN" emit -t ts --locale en "$TELA_SRC/validate.fab" -o "$SCRATCH/validate.ts" >/dev/null 2>&1
"$RADIX_BIN" emit -t ts --locale en "$TELA_SRC/tela.fab" -o "$SCRATCH/tela.ts" >/dev/null 2>&1
"$RADIX_BIN" emit -t ts --locale la "$GEN/src/document_ir.fab" -o "$SCRATCH/document_ir.ts" >/dev/null 2>&1
"$RADIX_BIN" emit -t ts --locale la "$ISLAND" -o "$SCRATCH/island.ts" >/dev/null 2>&1

strip() { sed '1,2d' "$1" | grep -v '^import '; }

{
    echo "// @ts-nocheck"
    echo "function __faberDisplay(v, _hint) { return String(v); }"
    strip "$SCRATCH/validate.ts"
    echo "const validate = { valid_space, valid_tag_name, valid_attribute_name, valid_name_in_space, valid_void_html, valid_void_structure };"
    strip "$SCRATCH/tela.ts"
    echo "const tela = { textus_visus: text_view, elementum_visus: element_view, html_spatium: html_space, html_visus: html_visus };"
    echo "const speculum = (() => {"
    strip "$SCRATCH/document_ir.ts"
    echo "return { leaf, node_html, text, void_element };"
    echo "})();"
    strip "$SCRATCH/island.ts"
} > "$SCRATCH/joined.ts"

echo "check-tela-island: node (byte compare)"
if ! out="$(node "$SCRATCH/joined.ts" 2>&1)"; then
    echo "$out" >&2
    echo "check-tela-island: fragment bytes diverged or emit failed to run" >&2
    exit 1
fi
if [[ "$out" != "salve &amp; vale" && "$out" != "<p>salve &amp; vale</p>" ]]; then
    echo "$out" >&2
    echo "check-tela-island: unexpected printed fragment: $out" >&2
    exit 1
fi
echo "check-tela-island: matched ($out)"

echo "check-tela-island: GREEN"
