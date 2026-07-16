#!/usr/bin/env bash
# ==========================================================================
# validate-fences.sh — CI fence contract validator for faberlang.dev
# ==========================================================================
# Extracts every ```faber code block from Markdown files and validates
# it against the declared fence contract:
#
#   ```faber [locale=<X>] [mode=fluid|pinned] [outcome=compiles|rejects|output-matches]
#
# Default contract: locale=la, mode=fluid, outcome=compiles.
#
# The script extracts each fence to a temporary .fab file and runs:
#   - outcome=compiles  → radix check must succeed
#   - outcome=rejects   → radix check must fail
#   - outcome=output-matches → TBD (needs .expected file)
#
# Usage:
#   scripts/validate-fences.sh <markdown-file-or-dir>
#
# Exit codes:
#   0 = all fences pass
#   1 = one or more fences failed validation
# ==========================================================================

set -euo pipefail

# --- Configuration ---
RADIX="${RADIX:-radix}"
TMPDIR_BASE="$(mktemp -d)"
trap 'rm -rf "$TMPDIR_BASE"' EXIT

PASS=0
FAIL=0
SKIP=0

# --- Helpers ---
log_pass() { printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
log_fail() { printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
log_skip() { printf "  \033[33mSKIP\033[0m  %s\n" "$1"; }

# --- Extract fences from a single Markdown file ---
# Output: lines of "fence_index|locale|mode|outcome|tmpfile_path"
extract_fences() {
    local md_file="$1"
    local fence_idx=0
    local in_fence=false
    local info_line=""
    local body=""
    local line_num=0

    while IFS= read -r line; do
        line_num=$((line_num + 1))

        if [[ "$line" =~ ^\`\`\`faber ]]; then
            in_fence=true
            info_line="$line"
            body=""
            continue
        fi

        if $in_fence && [[ "$line" =~ ^\`\`\`$ ]]; then
            in_fence=false
            # Parse info line for locale/mode/outcome
            local locale="la"
            local mode="fluid"
            local outcome="compiles"

            if echo "$info_line" | grep -qo 'locale=[a-zA-Z-]*'; then
                locale=$(echo "$info_line" | grep -o 'locale=[a-zA-Z-]*' | cut -d= -f2)
            fi
            if echo "$info_line" | grep -qo 'mode=[a-z]*'; then
                mode=$(echo "$info_line" | grep -o 'mode=[a-z]*' | cut -d= -f2)
            fi
            if echo "$info_line" | grep -qo 'outcome=[a-z-]*'; then
                outcome=$(echo "$info_line" | grep -o 'outcome=[a-z-]*' | cut -d= -f2)
            fi

            # Write body to temp file
            local tmpfile="$TMPDIR_BASE/fence_${fence_idx}.fab"
            printf '%s\n' "$body" > "$tmpfile"

            printf '%s|%s|%s|%s|%s|%d\n' "$fence_idx" "$locale" "$mode" "$outcome" "$tmpfile" "$line_num"
            fence_idx=$((fence_idx + 1))
            continue
        fi

        if $in_fence; then
            if [ -z "$body" ]; then
                body="$line"
            else
                body="${body}"$'\n'"${line}"
            fi
        fi
    done < "$md_file"
}

# --- Validate a single fence ---
validate_fence() {
    local md_file="$1"
    local fence_id="$2"
    local locale="$3"
    local mode="$4"
    local outcome="$5"
    local tmpfile="$6"
    local line_num="$7"

    local label="${md_file}:fence#${fence_id} (L${line_num}, ${locale}/${mode}/${outcome})"

    case "$outcome" in
        compiles)
            if "$RADIX" check "$tmpfile" > /dev/null 2>&1; then
                log_pass "$label"
                PASS=$((PASS + 1))
            else
                log_fail "$label — expected compiles, radix check failed"
                FAIL=$((FAIL + 1))
            fi
            ;;
        rejects)
            if "$RADIX" check "$tmpfile" > /dev/null 2>&1; then
                log_fail "$label — expected rejects, radix check succeeded"
                FAIL=$((FAIL + 1))
            else
                log_pass "$label"
                PASS=$((PASS + 1))
            fi
            ;;
        output-matches)
            # TODO: needs .expected file support — Stage 4 corpus path
            log_skip "$label — output-matches not yet implemented"
            SKIP=$((SKIP + 1))
            ;;
        *)
            log_skip "$label — unknown outcome: $outcome"
            SKIP=$((SKIP + 1))
            ;;
    esac
}

# --- Main ---
main() {
    local target="$1"

    if [ -z "$target" ]; then
        echo "Usage: $0 <markdown-file-or-dir>"
        exit 1
    fi

    # Check radix is available
    if ! command -v "$RADIX" > /dev/null 2>&1; then
        echo "ERROR: '$RADIX' not found in PATH. Set RADIX env var or install radix."
        exit 1
    fi

    echo "Validating fences in: $target"
    echo "Using: $(command -v "$RADIX")"
    echo ""

    # Collect Markdown files
    local md_files=()
    if [ -f "$target" ]; then
        md_files=("$target")
    elif [ -d "$target" ]; then
        while IFS= read -r f; do
            md_files+=("$f")
        done < <(find "$target" -name '*.md' -type f | sort)
    else
        echo "ERROR: '$target' is not a file or directory"
        exit 1
    fi

    # Process each file
    for md_file in "${md_files[@]}"; do
        echo "  File: $md_file"
        while IFS='|' read -r fid locale mode outcome tmpfile linenum; do
            validate_fence "$md_file" "$fid" "$locale" "$mode" "$outcome" "$tmpfile" "$linenum"
        done < <(extract_fences "$md_file")
    done

    echo ""
    echo "Results: $PASS passed, $FAIL failed, $SKIP skipped"

    if [ "$FAIL" -gt 0 ]; then
        exit 1
    fi
    exit 0
}

main "${1:-}"
