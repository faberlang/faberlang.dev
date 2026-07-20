"""Pure helpers for provenance hashing and locale sync reporting.

Hash rules (Decision 18d):
  - prose_hash over body with code fences stripped (replaced by stable placeholder)
  - code_hash over fence info+bodies only
  - Format: "sha256:" + 64 hex chars
"""

import hashlib
import re
from pathlib import Path

__all__ = [
    "split_frontmatter",
    "extract_fences",
    "prose_body",
    "code_payload",
    "sha256_hex",
    "hashes_for_markdown",
    "parse_frontmatter_fields",
    "rel_pair",
]

# Stable placeholder inserted for each fence block when computing prose_hash.
# Correct CommonMark triple-backtick fence with empty body.
PROSE_PLACEHOLDER = "\n```\n\n```\n"


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_inner_or_empty, body).

    Frontmatter is delimited by +++ ... +++ lines at the start of the file.
    frontmatter_inner is the raw content between the delimiters (or empty).
    body is everything after the closing +++ (or the whole text if no
    frontmatter).
    """
    if not text.startswith("+++"):
        return ("", text)

    # Strip leading "+++\n"
    rest = text[3:]
    if rest.startswith("\n"):
        rest = rest[1:]

    # Find the closing +++ marker
    idx = rest.find("\n+++")
    if idx == -1:
        # Opening +++ but no closing +++ => no frontmatter
        return ("", text)

    frontmatter = rest[:idx]
    body = rest[idx + 5:]  # skip '\n+++\n' (5 chars)
    if body.startswith("\n"):
        body = body[1:]

    return (frontmatter, body)


def extract_fences(body: str) -> list[tuple[str, str]]:
    """List of (info_string, fence_body) in document order.

    Standard CommonMark triple-backtick fences:
      ```info
      body
      ```
    info_string is the optional text after the opening ``` (stripped).
    fence_body is the content between fences (no trailing newline).
    """
    fences: list[tuple[str, str]] = []
    lines = body.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```") and len(line) >= 3:
            info = line[3:].strip()
            # Collect fence body until closing fence
            fence_lines: list[str] = []
            i += 1
            while i < len(lines):
                if lines[i].startswith("```"):
                    break
                fence_lines.append(lines[i])
                i += 1
            fence_body = "\n".join(fence_lines)
            fences.append((info, fence_body))
        i += 1
    return fences


def prose_body(body: str) -> str:
    """Return body with each fence block replaced by the stable placeholder.

    Uses ``PROSE_PLACEHOLDER`` (`` ``` `` + blank line + `` ``` ``) so fence
    content changes do not affect the prose hash while keeping structure
    stable.
    """
    result: list[str] = []
    lines = body.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```") and len(line) >= 3:
            # Replace this entire fence block with placeholder
            result.extend(["```", "", "```"])
            i += 1
            while i < len(lines):
                if lines[i].startswith("```"):
                    i += 1
                    break
                i += 1
        else:
            result.append(line)
            i += 1
    return "\n".join(result)


def code_payload(body: str) -> str:
    """Join all fence info+bodies separated by `` \\n---\\n ``.

    Returns empty string if there are no code fences.
    """
    fences = extract_fences(body)
    parts: list[str] = []
    for info, fence_body in fences:
        parts.append(f"{info}\n{fence_body}")
    return "\n---\n".join(parts)


def sha256_hex(data: str) -> str:
    """Return 'sha256:' + hex digest of UTF-8 encoded *data*."""
    digest = hashlib.sha256(data.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def hashes_for_markdown(text: str) -> tuple[str, str]:
    """Return (prose_hash, code_hash) for the full file text.

    Both hashes are computed over the body (after frontmatter split).
    prose_hash uses the prose_body with fences replaced by placeholder.
    code_hash uses the concatenated fence payloads.
    """
    _, body = split_frontmatter(text)
    return (sha256_hex(prose_body(body)), sha256_hex(code_payload(body)))


# Regex for simple key = "value" TOML lines
_TOML_LINE_RE = re.compile(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*"([^"]*)"\s*$')


def parse_frontmatter_fields(fm_inner: str) -> dict[str, str]:
    """Minimal TOML-ish parse for simple ``key = "value"`` lines.

    Handles flat key-value pairs only (no nested tables, no arrays, no
    booleans). Returns a dict of string values.
    """
    result: dict[str, str] = {}
    for line in fm_inner.split("\n"):
        m = _TOML_LINE_RE.match(line)
        if m:
            result[m.group(1)] = m.group(2)
    return result


def rel_pair(locale_path: Path, locale: str, en_root: Path) -> Path | None:
    """Map ``src/{locale}/foo.md`` → ``src/en-US/foo.md`` if the target exists.

    *locale_path* is the absolute path to the locale file.
    *locale* is the locale code (e.g. ``'th-TH'``).
    *en_root* is the absolute path to the en-US source directory.

    Returns ``None`` when no paired en-US file exists.
    """
    # Walk up to find the parent directory named after *locale*
    parent = locale_path.parent
    while parent.name != locale and parent != parent.parent:
        parent = parent.parent
    if parent.name != locale:
        return None
    rel = locale_path.relative_to(parent)
    en_path = en_root / rel
    return en_path if en_path.exists() else None
