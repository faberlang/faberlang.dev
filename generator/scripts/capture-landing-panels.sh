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
for candidate in "${WORKSPACE}/radix/target/release/faber" \
                 "${WORKSPACE}/radix/target/debug/faber"; do
    [ -x "$candidate" ] && FABER="$candidate" && break
done
FABER="${FABER:-faber}"
# Installed releases lag the workspace tree; resolve library packs from the
# workspace so `faber convert` validates against current reader packs.
export FABER_LIBRARY_HOME="${FABER_LIBRARY_HOME:-${WORKSPACE}}"

echo "toolchain: $("$RADIX" --version) at ${RADIX}"
echo "toolchain: $("$FABER" --version) at ${FABER}"
# `faber convert --to` resolves reader packs relative to its own binary, and
# a workspace build has no share/faber/locale/. Without this every locale panel
# fails and the committed captures quietly stay at whatever the toolchain
# produced last time — which is how tensor/vacua sat untranslated in the
# shipped panels long after the compiler learned to render them.
PACK_SRC="${WORKSPACE}/radix/locale"
PACK_DEST="$(cd "$(dirname "$FABER")/.." && pwd)/share/faber/locale"
if [ -d "$PACK_SRC" ]; then
    mkdir -p "$PACK_DEST"
    for pack in "$PACK_SRC"/*/; do
        name="$(basename "$pack")"
        [ -f "${pack}pack.toml" ] || continue
        [ -e "${PACK_DEST}/${name}" ] || ln -s "$pack" "${PACK_DEST}/${name}"
    done
    echo "reader packs: $(ls "$PACK_DEST" | wc -l | tr -d ' ') at ${PACK_DEST}"
fi

OUT="${GENERATOR_DIR}/landing"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

mkdir -p "${OUT}/locales" "${OUT}/targets"

# -- the demo program ---------------------------------------------------------
# Deliberately not hello-world. This is a small dense-tensor computation:
# construct two typed matrices, multiply them, and print the result. The
# locale and application-target tabs therefore demonstrate the same
# compute-shaped program that the headline promises, while the separate
# GPU axis below shows the kernel form used for device execution.
#
# The program is the universal-vocabulary form the localization page ships:
# shape-bearing tensor types, the `·` matmul glyph, and `vacua`/`empty`
# spelled by each pack — no strue/matmul/media members, which translated
# packs lack. Locale panels must regenerate localization.md byte-for-byte.
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
    fixum tensor<f32, [2, 3]> a ← vacua
    fixum tensor<f32, [3, 4]> b ← vacua
    fixum tensor<f32, [2, 4]> product ← a · b
    nota product
}
FAB

cp "${WORK}/demo/src/main.fab" "${OUT}/targets/source.fab"

# The reader axis must carry the `·` glyph — translated packs have no matmul
# member row — but the Go and TypeScript backends reject the glyph outright
# (CODEGEN001, Phase 3 parity). The target axis therefore lowers the
# member-call form of the same program: identical declarations and shape
# arithmetic, the matmul spelled `a.matmul(b)` the way every backend accepts.
sed 's/a · b/a.matmul(b)/' "${WORK}/demo/src/main.fab" > "${WORK}/main-targets.fab"

# -- axis 1: reader locales ---------------------------------------------------
# `en` is the English reader surface; `la` is canonical Faber. The rest are
# the shipped human reader packs. The demo source is Latin with no
# frontmatter, and `faber convert` defaults `--from` to the source's
# frontmatter locale (falling back to `en`), so the Latin identity must be
# stated explicitly or every parse dies on `vacua`.
echo "reader locales:"
for loc in la en th-TH zh-Hans zh-Hant vi ar hi; do
    if "$FABER" convert --from la --to "$loc" --stdout "${WORK}/demo" \
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
    if "$RADIX" emit --target "$t" "${WORK}/main-targets.fab" \
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
