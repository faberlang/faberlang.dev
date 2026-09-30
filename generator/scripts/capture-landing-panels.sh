#!/usr/bin/env bash
# capture-landing-panels.sh — regenerate the landing page's demo panels.
#
# The landing page shows two things, and both are COMPILER OUTPUT captured
# here rather than hand-authored, so the page cannot claim something the
# toolchain does not actually produce:
#
#   1. one program (landing/program.fab) rendered in every reader locale
#      (`faber convert --to`), with its real `faber run` output;
#   2. one small library (landing/targets/span.fab) emitted as source for
#      every target that can lower it (`radix emit`).
#
# Both sources are authored in the English reader surface and are the only
# hand-written inputs. Re-run after a compiler upgrade or a reader-pack
# change, then rebuild:
#   bash generator/scripts/capture-landing-panels.sh
#   bash generator/scripts/build-site.sh
#
# Program constraints, each learned from a compiler diagnostic:
#   - float literals are written explicitly (`0.0`, not `0`) in f64 slots;
#     `faber convert` fails hir_meaning_diverged on an integer literal in an
#     f64 slot (reported to the compiler owners).
#   - no library members (`.first()`, `.length`): translated packs do not
#     all carry them, so a locale panel would leak a Latin spelling.
#   - the library avoids `⤒`/`⤓` and generics: Go/Swift emit method calls on
#     floats for the clamp operators, and Swift/Python reject generics.
#
# Requires a workspace build of `faber` and `radix` (radix/target/debug or
# release). A PATH copy is used only as a fallback and is reported.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR_DIR="$(dirname "$SCRIPT_DIR")"
WORKSPACE="$(cd "${GENERATOR_DIR}/../.." && pwd)"

# Prefer the repo's own build over whatever is on PATH. A stale ~/.cargo/bin
# copy silently produced wrong results once: panels were captured — and claims
# written — against a compiler days behind the tree. Pin it, and print what
# was used.
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
export FABER_LIBRARY_HOME="${FABER_LIBRARY_HOME:-${WORKSPACE}}"

echo "toolchain: $("$RADIX" --version) at ${RADIX}"
echo "toolchain: $("$FABER" --version) at ${FABER}"

# `faber convert --to` resolves reader packs relative to its own binary, and
# a workspace build has no share/faber/locale/. Without this every locale panel
# fails and the committed captures quietly stay at whatever the toolchain
# produced last time.
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

[locale]
locale = "en"
TOML
cp "${OUT}/program.fab" "${WORK}/demo/src/main.fab"

echo "program check + run:"
"$FABER" check "${WORK}/demo" >/dev/null
"$FABER" run "${WORK}/demo" 2>/dev/null > "${OUT}/program.out.txt"
sed 's/^/  /' "${OUT}/program.out.txt"

# -- axis 1: reader locales ---------------------------------------------------
# `en` is the English reader surface; `la` is canonical Faber; the rest are
# the shipped human reader packs. Each converted panel is re-checked in its
# own locale, so a panel that no longer parses fails the capture instead of
# shipping.
echo "reader locales:"
for loc in en la th-TH zh-Hans zh-Hant vi ar hi; do
    if [ "$loc" = "en" ]; then
        cp "${OUT}/program.fab" "${OUT}/locales/en.fab"
    else
        "$FABER" convert --from en --to "$loc" --stdout "${WORK}/demo" \
            > "${OUT}/locales/${loc}.fab"
    fi
    [ -s "${OUT}/locales/${loc}.fab" ] || { echo "  ${loc} — EMPTY" >&2; exit 1; }
    # Strip the frontmatter the converter adds: the panel is rendered in a
    # <pre> that already names its locale.
    python3 - "${OUT}/locales/${loc}.fab" <<'PY'
import sys, re
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
s = re.sub(r"\A\+\+\+\n.*?\n\+\+\+\n", "", s, count=1, flags=re.S)
open(p, "w", encoding="utf-8").write(s)
PY
    mkdir -p "${WORK}/chk-${loc}/src"
    sed "s/^locale = .*/locale = \"${loc}\"/" "${WORK}/demo/faber.toml" > "${WORK}/chk-${loc}/faber.toml"
    cp "${OUT}/locales/${loc}.fab" "${WORK}/chk-${loc}/src/main.fab"
    # The `la` surface is canonical Faber; the manifest spells it "la".
    if ! "$FABER" check "${WORK}/chk-${loc}" >/dev/null 2>&1; then
        echo "  ${loc} — converted panel FAILS faber check" >&2
        "$FABER" check "${WORK}/chk-${loc}" 2>&1 | head -5 >&2
        exit 1
    fi
    # Each panel must not only check but RUN, and print what the program prints.
    if ! "$FABER" run "${WORK}/chk-${loc}" 2>/dev/null | cmp -s - "${OUT}/program.out.txt"; then
        echo "  ${loc} — converted panel does not reproduce the program output" >&2
        exit 1
    fi
    echo "  ${loc}"
done

# -- axis 2: the library, emitted for each target ------------------------------
# The library is a separate source: no main, `@ public` surface. `radix emit`
# is the Radix/Faber-boundary contract — Radix lowers and serializes; target
# build tools are not run here.
echo "library targets:"
rm -f "${OUT}/targets"/out.*.txt
# Only targets whose emitted library was compile-checked in its own toolchain
# (rustc against the faber runtime crate, tsc, go vet, swiftc -typecheck).
# Python is omitted: its class-method lowering is broken (name-mangled
# `__faber_fdiv` helper, class-level field access) — reported, not shown.
for t in rust ts go swift; do
    if "$RADIX" emit --locale en --target "$t" "${OUT}/targets/span.fab" \
        > "${OUT}/targets/out.${t}.txt" 2>"${WORK}/err-${t}.txt" \
        && [ -s "${OUT}/targets/out.${t}.txt" ]; then
        echo "  ${t}"
    else
        rm -f "${OUT}/targets/out.${t}.txt"
        echo "  ${t} — FAILED, panel omitted" >&2
        head -3 "${WORK}/err-${t}.txt" >&2
    fi
done
# The capability table on the page is parsed from `faber targets`, so it
# cannot drift from the toolchain.
"$FABER" targets > "${OUT}/targets/faber-targets.txt"
echo "  faber targets: $(wc -l < "${OUT}/targets/faber-targets.txt" | tr -d ' ') rows"
echo "captured to ${OUT}"
