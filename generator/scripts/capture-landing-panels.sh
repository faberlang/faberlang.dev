#!/usr/bin/env bash
# capture-landing-panels.sh — regenerate the landing page's demo panels.
#
# The landing page shows one program on two axes: rendered for every reader
# locale, and lowered to every compilation target. Both sets are COMPILER
# OUTPUT, captured here rather than hand-authored, so the page cannot claim
# something the toolchain does not actually produce.
#
# Re-run after a compiler upgrade or a reader-pack change, then rebuild:
#   bash generator/scripts/capture-landing-panels.sh
#   bash generator/scripts/build-site.sh
#
# Requires `faber` and `radix` on PATH.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR_DIR="$(dirname "$SCRIPT_DIR")"
OUT="${GENERATOR_DIR}/landing"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

mkdir -p "${OUT}/locales" "${OUT}/targets"

# -- the demo program ---------------------------------------------------------
# Deliberately not hello-world: a clamp reads as something a person would
# actually write, exercises control flow and a typed signature, renders in
# every reader pack, and lowers to every non-GPU target.
mkdir -p "${WORK}/demo/src"
cat > "${WORK}/demo/faber.toml" <<'TOML'
[package]
name = "demo"
version = "0.1.0"
edition = "2026"

[paths]
source = "src"
entry = "main.fab"

[build]
kind = "bin"
target = "rust"
TOML

cat > "${WORK}/demo/src/main.fab" <<'FAB'
functio saturate(numerus x) → numerus {
    si x < 0 ergo redde 0
    si x > 255 ergo redde 255
    redde x
}

incipit {
    fixum numerus v ← saturate(300)
    nota v
}
FAB

cp "${WORK}/demo/src/main.fab" "${OUT}/targets/source.fab"

# -- axis 1: reader locales ---------------------------------------------------
# `llm` is the model-facing surface; `la` is canonical Faber. The rest are the
# shipped human reader packs.
#
# NOTE: `faber format --reader-locale la` fails pack validation on faber 1.4.0,
# so canonical Latin comes from `radix emit -t faber` (canonical re-emission),
# which produces the same surface by a different path. Revisit once the `la`
# pack validates.
echo "reader locales:"
radix emit -t faber "${WORK}/demo/src/main.fab" > "${OUT}/locales/la.fab"
echo "  la (via radix emit -t faber)"

for loc in llm th-TH zh-Hans zh-Hant vi ar hi; do
    if faber format --reader-locale "$loc" --stdout "${WORK}/demo" \
        > "${OUT}/locales/${loc}.fab" 2>/dev/null \
        && [ -s "${OUT}/locales/${loc}.fab" ]; then
        echo "  ${loc}"
    else
        rm -f "${OUT}/locales/${loc}.fab"
        echo "  ${loc} — FAILED, panel omitted" >&2
    fi
done

# -- axis 2: compilation targets ----------------------------------------------
echo "targets:"
for t in rust go ts llvm-text wasm-text; do
    if radix emit --target "$t" "${WORK}/demo/src/main.fab" \
        > "${OUT}/targets/out.${t}.txt" 2>/dev/null \
        && [ -s "${OUT}/targets/out.${t}.txt" ]; then
        echo "  ${t}"
    else
        rm -f "${OUT}/targets/out.${t}.txt"
        echo "  ${t} — FAILED, panel omitted" >&2
    fi
done

# GPU targets require an `@ nucleum` kernel entry point, so they use a separate
# (also real) source. The page labels this difference rather than eliding it.
KERNEL="$(cd "${GENERATOR_DIR}/../.." && pwd)/radix/corpus/vector/kernel.fab"
if [ -f "$KERNEL" ]; then
    sed -n '/^@ nucleum/,$p' "$KERNEL" > "${OUT}/targets/kernel.fab"
    for t in wgsl-text metal-text; do
        if radix emit --target "$t" "$KERNEL" \
            > "${OUT}/targets/out.${t}.txt" 2>/dev/null \
            && [ -s "${OUT}/targets/out.${t}.txt" ]; then
            echo "  ${t} (from kernel.fab)"
        else
            rm -f "${OUT}/targets/out.${t}.txt"
            echo "  ${t} — FAILED, panel omitted" >&2
        fi
    done
else
    echo "  wgsl-text/metal-text — kernel source not found at ${KERNEL}" >&2
fi

echo "captured to ${OUT}"
