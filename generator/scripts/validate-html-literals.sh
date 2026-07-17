#!/usr/bin/env bash
# Fail when generator Faber sources emit raw HTML outside the serializer.
# Comments are ignored; document_ir.fab owns tag serialization.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
GENERATOR_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SRC_DIR="${1:-${GENERATOR_DIR}/src}"

fail=0
while IFS= read -r file; do
    base="$(basename "$file")"
    if [ "$base" = "document_ir.fab" ]; then
        continue
    fi

    matches="$(python3 - "$file" <<'PY'
import re
import sys
path = sys.argv[1]
pattern = re.compile(r'<(?:!DOCTYPE|/?(?:html|head|body|main|div|span|section|aside|footer|nav|ul|li|p|a|code|pre|table|thead|tbody|tr|th|td|h1|h2|h3|h4|h5|h6|meta|link|title|strong|em|br|hr)\b)')
with open(path, encoding='utf-8') as f:
    for lineno, line in enumerate(f, 1):
        stripped = line.lstrip()
        if stripped.startswith('#'):
            continue
        if pattern.search(line):
            print(f"{path}:{lineno}:{line.rstrip()}")
PY
)"

    if [ -n "$matches" ]; then
        printf '%s\n' "$matches"
        fail=1
    fi
done < <(find "$SRC_DIR" -maxdepth 1 -name '*.fab' -type f | sort)

if [ "$fail" -ne 0 ]; then
    echo "HTML literal validation failed: only generator/src/document_ir.fab may write raw tags." >&2
    exit 1
fi

echo "HTML literal validation passed: raw tag emission is confined to document_ir.fab"
