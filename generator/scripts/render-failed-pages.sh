#!/usr/bin/env bash
# render-failed-pages.sh — re-render pages a build marked ✗ (typically the
# large grammar pages that outlived a tight PAGE_TIMEOUT), with a long bound.
# The ✗ lines are locale-relative, so the current [locale] line is tracked.
# Usage: render-failed-pages.sh <build-log> [timeout-seconds]
set -uo pipefail
LOG="${1:?build log}"
TMO="${2:-1800}"
REPO_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_DIR"
tmp="$(mktemp)"
locale=""
rc=0
while IFS= read -r line; do
    case "$line" in
        *" [locale] "*) locale="$(echo "$line" | sed 's/.*\[locale\] \([^ ]*\).*/\1/')" ;;
        *"✗ FAILED: "*)
            rel="$(echo "$line" | sed 's/.*✗ FAILED: //' | tr -d '\r')"
            echo "$locale|$rel" >> "$tmp"
            ;;
    esac
done < "$LOG"
mapfile -t FAILED < <(sort -u "$tmp")
rm -f "$tmp"
if [ "${#FAILED[@]}" -eq 0 ]; then echo "no failed pages in $LOG"; exit 0; fi
echo "re-rendering ${#FAILED[@]} failed page(s) with ${TMO}s bound"
for pair in "${FAILED[@]}"; do
    locale="${pair%%|*}"
    rel="${pair#*|}"
    iter="${rel%.md}"
    src="src/${locale}/${iter}.md"
    if [ ! -f "$src" ]; then echo "  ✗ no source for ${locale}/${rel}"; rc=1; continue; fi
    if gtimeout "$TMO" generator/scripts/speculum-run.sh --page "$iter" "$src" "$locale" "$locale" /speculum.css > "dist/${locale}/${iter}.html" 2>/dev/null; then
        echo "  ✓ ${locale}/${iter}.html"
    else
        echo "  ✗ still failing: ${locale}/${iter}"
        rm -f "dist/${locale}/${iter}.html"
        rc=1
    fi
done
exit $rc
