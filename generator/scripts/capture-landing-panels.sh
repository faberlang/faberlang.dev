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
WORKSPACE="$(cd "${GENERATOR_DIR}/../.." && pwd)"

# Prefer the repo's own build over whatever is on PATH. A stale ~/.cargo/bin
# copy silently produced wrong capability results once: 0.78.0 rejected rank-2
# device views and the Metal matmul lowering that 0.79.0 emits fine, so panels
# were captured — and claims written — against a compiler three days behind the
# tree. Pin it, and print what was used.
for candidate in "${WORKSPACE}/radix/target/release/radix" \
                 "${WORKSPACE}/radix/target/debug/radix"; do
    [ -x "$candidate" ] && RADIX="$candidate" && break
done
RADIX="${RADIX:-radix}"
FABER="${WORKSPACE}/faber/target/release/faber"
[ -x "$FABER" ] || FABER="faber"

echo "toolchain: $("$RADIX" --version) at ${RADIX}"
echo "toolchain: $("$FABER" --version) at ${FABER}"
OUT="${GENERATOR_DIR}/landing"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

mkdir -p "${OUT}/locales" "${OUT}/targets"

# -- the demo program ---------------------------------------------------------
# Deliberately not hello-world. This is a small dense-tensor computation:
# construct two typed matrices, multiply them, and reduce the result to a
# scalar. The locale and application-target tabs therefore demonstrate the
# same compute-shaped program that the headline promises, while the separate
# GPU axis below shows the kernel form used for device execution.
#
# Keep the example small enough to read at a glance, but real enough to expose
# shape-bearing tensor types, matrix multiplication, and a reduction.
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
incipit {
    fixum lista<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    fixum lista<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    fixum tf32[] seed ← vacua
    fixum tf32[2, 3] a ← seed.strue(flat_a, [2, 3])
    fixum tf32[3, 4] b ← seed.strue(flat_b, [3, 4])
    fixum tf32[2, 4] product ← a.matmul(b)
    fixum f32 mean ← product.media()
    nota mean
}
FAB

cp "${WORK}/demo/src/main.fab" "${OUT}/targets/source.fab"

# -- axis 1: reader locales ---------------------------------------------------
# `en` is the English reader surface; `la` is canonical Faber. The rest are
# the shipped human reader packs.
#
# NOTE: `faber format --reader-locale la` fails pack validation on faber 1.4.0,
# so canonical Latin comes from `"$RADIX" emit -t faber` (canonical re-emission),
# which produces the same surface by a different path. Revisit once the `la`
# pack validates.
echo "reader locales:"
"$RADIX" emit -t faber "${WORK}/demo/src/main.fab" > "${OUT}/locales/la.fab"
echo "  la (via radix emit -t faber)"

for loc in en th-TH zh-Hans zh-Hant vi ar hi; do
    if "$FABER" format --locale "$loc" --stdout "${WORK}/demo" \
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
    if "$RADIX" emit --target "$t" "${WORK}/demo/src/main.fab" \
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
# The GPU kernel is its own source. A one-line scalar kernel understated the
# case: the interesting part is that three buffer parameters and a bounds
# guard become two entirely different ABIs, so the kernel takes two inputs,
# an output view and an index.
KERNEL="${WORK}/kernel.fab"
cat > "$KERNEL" <<'FAB'
@ nucleum
functio multiplico(tf32[16, 8] a, tf32[8, 16] b, tf32[16, 16] out, u32 id) → vacuum {
    fixum tf32[16, 16] c ← a.matmul(b)
}
FAB
cp "$KERNEL" "${OUT}/targets/kernel.fab"
for t in wgsl-text metal-text; do
    if "$RADIX" emit --target "$t" "$KERNEL" \
        > "${OUT}/targets/out.${t}.txt" 2>/dev/null \
        && [ -s "${OUT}/targets/out.${t}.txt" ]; then
        echo "  ${t} (from kernel.fab)"
    else
        rm -f "${OUT}/targets/out.${t}.txt"
        echo "  ${t} — FAILED, panel omitted" >&2
    fi
done
echo "captured to ${OUT}"
