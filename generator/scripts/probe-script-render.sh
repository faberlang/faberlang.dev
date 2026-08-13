#!/usr/bin/env bash
# Probe: run Speculum through the MIR stepper on the Latin document_ir
# path. No tela:tela. html.fab is the pre-Tela Latin emitter.
#
# `faber script` is the wrong command here: it injects the English reader
# pack and has no --locale, so Latin Speculum fails PARSE001 in ~60ms.
# `faber run -t fmir --locale la` is the executed-lane probe.
#
# Usage:
#   probe-script-render.sh [page.md] [site_locale]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GEN="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO="$(cd "$GEN/.." && pwd)"
PACKET="$(cd "$REPO/.." && pwd)"

PAGE="${1:-$REPO/src/en-US/404.md}"
SITE="${2:-en-US}"

if [[ ! -f "$PAGE" ]]; then
    echo "probe-script-render: missing page $PAGE" >&2
    exit 1
fi

if [[ -n "${FABER_BIN:-}" && -x "${FABER_BIN}" ]]; then
    :
elif [[ -n "${FABER:-}" && -x "${FABER}" ]]; then
    FABER_BIN="$FABER"
elif [[ -x "$PACKET/radix/target/debug/faber" ]]; then
    FABER_BIN="$PACKET/radix/target/debug/faber"
else
    FABER_BIN="$(command -v faber || true)"
fi
if [[ -z "${FABER_BIN}" || ! -x "${FABER_BIN}" ]]; then
    echo "probe-script-render: no faber binary (set FABER_BIN)" >&2
    exit 1
fi

if [[ -d "${FABER_LIBRARY_HOME:-}/norma/src" ]]; then
    :
else
    walk="$PACKET"
    while [[ "$walk" != "/" ]]; do
        if [[ -d "$walk/norma/src" ]]; then
            export FABER_LIBRARY_HOME="$walk"
            break
        fi
        walk="$(cd "$walk/.." && pwd)"
    done
fi
if [[ ! -d "${FABER_LIBRARY_HOME:-}/norma/src" ]]; then
    echo "probe-script-render: norma not found (set FABER_LIBRARY_HOME)" >&2
    exit 1
fi

STAGE="$(mktemp -d "${TMPDIR:-/tmp}/speculum-script-probe.XXXXXX")"
trap 'rm -rf "$STAGE"' EXIT
# Copy only what script needs — never generator/target (Rust crate, tens of MB).
mkdir -p "$STAGE/src"
cp "$GEN/faber.toml" "$STAGE/"
# Live tree includes tela_island.fab; this probe is document_ir only.
for fab in "$GEN/src/"*.fab; do
    base="$(basename "$fab")"
    if [[ "$base" == "tela_island.fab" ]]; then
        continue
    fi
    cp "$fab" "$STAGE/src/"
done
# Pre-Tela Latin emitter (document_ir brand, no tela:tela).
git -C "$REPO" show 'HEAD~1:generator/src/html.fab' > "$STAGE/src/html.fab"
# Keep Latin reader locale; drop Tela from the live tree only.
# faber.toml [locale] la is fine without a Tela import.

ITER="$(basename "${PAGE%.md}")"
OUT="$STAGE/out.html"

echo "probe-script-render: faber=$FABER_BIN"
echo "probe-script-render: FABER_LIBRARY_HOME=$FABER_LIBRARY_HOME"
echo "probe-script-render: page=$PAGE ($ITER / $SITE)"
echo "probe-script-render: html.fab=$(wc -l < "$STAGE/src/html.fab") lines, no tela import"
echo "probe-script-render: cmd=faber run -t fmir --locale la (not faber script)"

TIMEOUT_SEC="${PROBE_TIMEOUT_SEC:-30}"
set +e
/usr/bin/time -p perl -e 'alarm shift; exec @ARGV' "$TIMEOUT_SEC" \
    "$FABER_BIN" run -t fmir --locale la "$STAGE" -- \
    --page "$ITER" "$PAGE" "$SITE" la /speculum.css \
    > "$OUT" 2>"$STAGE/err"
rc=$?
set -e
if [[ "$rc" -eq 142 ]]; then
    echo "probe-script-render: TIMEOUT after ${TIMEOUT_SEC}s" >&2
fi

echo "----- stderr (non-LOCALE002) -----"
grep -v '^warning: LOCALE002' "$STAGE/err" || true
echo "----- timing -----"
grep -E '^(real|user|sys) ' "$STAGE/err" || true
echo "----- result -----"
if [[ "$rc" -ne 0 ]]; then
    echo "probe-script-render: FAIL exit $rc"
    exit "$rc"
fi
if ! grep -q '<aside>' "$OUT"; then
    echo "probe-script-render: FAIL no <aside> in output"
    echo "first 20 lines:"
    head -20 "$OUT"
    exit 1
fi
if ! grep -q 'class="brand"' "$OUT"; then
    echo "probe-script-render: FAIL no brand in output"
    exit 1
fi
bytes=$(wc -c < "$OUT" | tr -d ' ')
echo "probe-script-render: OK $bytes bytes"
grep -o '<a class="brand"[^<]*' "$OUT" | head -1
echo "probe-script-render: GREEN"
