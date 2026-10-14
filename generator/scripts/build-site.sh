#!/usr/bin/env bash
# build-site.sh — build the faberlang.dev site. A thin launcher: the build is
# `build.py`, one process that owns staleness, rendering and the gates.
#
#   build-site.sh                       incremental build against the pinned radix
#   build-site.sh --full                wipe dist and the manifest, rebuild everything
#   build-site.sh --refresh-upstream    re-pin radix HEAD and regenerate what derives from it
#   build-site.sh --refresh-upstream REV
#
# Needs Python 3.11+ (tomllib) and a `faber` on PATH (or --faber PATH).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

PYTHON="${PYTHON:-}"
if [ -z "$PYTHON" ]; then
    for candidate in python3.14 python3.13 python3.12 python3.11 python3; do
        if command -v "$candidate" >/dev/null 2>&1 \
            && "$candidate" -c 'import tomllib' >/dev/null 2>&1; then
            PYTHON="$candidate"
            break
        fi
    done
fi
if [ -z "$PYTHON" ]; then
    echo "ERROR: Python 3.11+ is required" >&2
    exit 1
fi

exec "$PYTHON" "${SCRIPT_DIR}/build.py" "$@"
