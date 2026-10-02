#!/usr/bin/env bash
# capture-locale-diagnostics.sh — record one compiler failure in every reader locale.
#
# The Reader locales tour claims that diagnostics render in the reader's own
# language, not English prose inside localized source. This script proves it
# with the compiler: it checks one deliberately broken program once per reader
# pack and commits the raw `faber check --diagnostics` output under
# generator/locale-captures/. A page then shows the same failure spelled in
# each language, and the file it reads is the command's own output, never a
# hand-copied transcript.
#
# The program is lexical (a string literal with no closing quote), so the
# failure is identical in every locale: LEX001. Only the message text changes.
# The identifier and the string are chosen so no locale's warning pass fires —
# `salve` reads like the English keyword `false` and would add a LOCALE002
# warning to the `en` capture alone.
#
# `--locale` selects the reader pack the whole run is rendered against, message
# language included. `--diagnostics` is what prints the prose; without it the
# toolchain emits codes and source spans only.
#
# Requires a workspace build of `faber`. A PATH copy is used only as a
# fallback and is reported.
#
# Re-run after a compiler or reader-pack change, then re-render the section:
#   bash generator/scripts/capture-locale-diagnostics.sh
#   python3 generator/scripts/generate-locale-reference.py --packs <radix/locale>

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "${SCRIPT_DIR}/../.." && pwd)"

# Ordered join, same as agent_locales.PACK_COLUMNS. English first; Latin second
# as one locale among eight.
LOCALES=(en la ar hi th-TH vi zh-Hans zh-Hant)

# Reader packs. A normal checkout has them one directory up from the repo; a
# git worktree does not, so the workspace fallback is next. Override either way
# with FABER_LOCALE_PACKS.
PACKS="${FABER_LOCALE_PACKS:-}"
if [ -z "$PACKS" ]; then
    for candidate in "${REPO}/../radix/locale" \
                     "/Users/ianzepp/work/faberlang/radix/locale"; do
        if [ -d "$candidate" ]; then
            PACKS="$(cd "$candidate" && pwd)"
            break
        fi
    done
fi
if [ -z "$PACKS" ] || [ ! -d "$PACKS" ]; then
    echo "ERROR: reader packs not found; set FABER_LOCALE_PACKS" >&2
    exit 1
fi

# Prefer the workspace development build, which is current with the packs; a
# stale installed copy can reject a newer pack schema.
FABER="${FABER:-}"
if [ -z "$FABER" ]; then
    for candidate in "/Users/ianzepp/work/faberlang/radix/target/debug/faber" \
                     "/Users/ianzepp/work/faberlang/radix/target/release/faber" \
                     "${REPO}/../radix/target/debug/faber" \
                     "${REPO}/../radix/target/release/faber"; do
        [ -x "$candidate" ] && FABER="$candidate" && break
    done
fi
FABER="${FABER:-faber}"
command -v "$FABER" >/dev/null 2>&1 || { echo "ERROR: no faber binary found; set FABER" >&2; exit 1; }

OUT="${REPO}/generator/locale-captures"
FIXTURE="${OUT}/error.fab"
mkdir -p "$OUT"

# One deliberately broken program. Latin keywords are the canonical surface;
# the missing closing quote is the error. Checked under each locale, the lexer
# stops at the same place, so the failure is identical everywhere.
cat > "$FIXTURE" <<'FAB'
# The closing quote is missing, so the string literal runs to the end of the
# line. Every reader pack renders the same LEX001 in its own language.
fixum textus nuntius ← "Salve, munde!
FAB

echo "toolchain: $("$FABER" --version 2>/dev/null || echo unknown) at ${FABER}"
echo "reader packs: ${PACKS}"
echo "capturing:"

installed=0
have_cjk=0
for loc in "${LOCALES[@]}"; do
    [ -f "${PACKS}/${loc}/pack.toml" ] || { echo "  ${loc} — no pack, skipped" >&2; continue; }
    case "$loc" in th-TH|zh-Hans|zh-Hant) have_cjk=1 ;; esac

    # Run from the repo root, then rewrite the root prefix the toolchain prints
    # to a repo-relative one. The diagnostic itself is byte-exact; only the
    # absolute path would differ between a checkout and a worktree, and a
    # capture that changes with the directory it ran in is not a capture.
    set +e
    (cd "$REPO" && "$FABER" check --diagnostics --locale "$loc" \
        "generator/locale-captures/error.fab") 2>&1 \
        | sed "s|${REPO}/||g" > "${OUT}/${loc}.txt"
    set -e

    if [ ! -s "${OUT}/${loc}.txt" ] || ! grep -q 'LEX001' "${OUT}/${loc}.txt"; then
        echo "  ${loc} — FAILED to capture a LEX001 diagnostic" >&2
        exit 1
    fi
    installed=$((installed + 1))
    echo "  ${loc}: $(grep -m1 '^error\[' "${OUT}/${loc}.txt" | sed 's/^error\[[^]]*\] [a-z]* [^:]*: //')"
done

# The feature tour needs the two base surfaces and at least one non-Latin
# script; a CJK capture is what proves the wider-script path.
[ -f "${OUT}/en.txt" ] && [ -f "${OUT}/la.txt" ] || { echo "ERROR: en and la captures are required" >&2; exit 1; }
[ "$have_cjk" = 1 ] || { echo "ERROR: no CJK reader pack installed" >&2; exit 1; }

echo "wrote ${installed} captures to generator/locale-captures/"
echo "next: python3 generator/scripts/generate-locale-reference.py"
