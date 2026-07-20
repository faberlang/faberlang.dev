"""Pure helpers for provenance hashing and locale sync reporting.

Hash rules (Decision 18d):
  - prose_hash over body with code fences stripped (replaced by stable placeholder)
  - code_hash over fence info+bodies only
  - Format: "sha256:" + 64 hex chars
"""

import hashlib
import re
import subprocess
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
    "load_markdown",
    "stamp_frontmatter",
    "strip_fences_for_prompt",
    "reinsert_fences_from_en",
    "current_git_head",
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


# ---------------------------------------------------------------------------
# Phase 5 — sync-translate helpers
# ---------------------------------------------------------------------------

# Regex to match a frontmatter key = "value" line for removal/replacement.
_FM_KEY_LINE = re.compile(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*=')

# Keys that stamp_frontmatter manages exclusively.
_STAMPED_KEYS = frozenset({
    "prose_hash", "code_hash", "source_commit", "source_locale", "source_hash",
})


def load_markdown(path: Path) -> str:
    """Read UTF-8 text from *path* and return it."""
    return path.read_text(encoding="utf-8")


def stamp_frontmatter(
    text: str,
    prose_hash: str,
    code_hash: str,
    source_commit: str,
    translation_kind: str | None = None,
) -> str:
    """Rewrite ``+++`` frontmatter to set provenance fields.

    Sets or replaces: ``prose_hash``, ``code_hash``, ``source_commit``,
    ``source_locale = "en-US"``.
    Removes legacy ``source_hash`` if present.
    Keeps ``title``, ``section``, ``order``, ``sources``, and all other keys.

    If *translation_kind* is provided, sets ``translation_kind`` in the
    frontmatter. Otherwise leaves any existing ``translation_kind`` in place.

    Returns the full file text with updated frontmatter.
    """
    fm_inner, body = split_frontmatter(text)

    if not fm_inner:
        # No existing frontmatter — create one
        lines: list[str] = [
            "+++",
            f'prose_hash = "{prose_hash}"',
            f'code_hash = "{code_hash}"',
            f'source_commit = "{source_commit}"',
            'source_locale = "en-US"',
        ]
        if translation_kind is not None:
            lines.append(f'translation_kind = "{translation_kind}"')
        lines.append("+++")
        if body:
            lines.append("")
            lines.append(body)
        return "\n".join(lines)

    # Filter out stamped keys; track whether we saw translation_kind
    kept: list[str] = []
    saw_translation_kind = False
    for line in fm_inner.split("\n"):
        m = _FM_KEY_LINE.match(line)
        key = m.group(1) if m else None
        if key in _STAMPED_KEYS:
            continue  # remove existing value
        if key == "translation_kind":
            saw_translation_kind = True
            if translation_kind is not None:
                # Replace with new value
                kept.append(f'translation_kind = "{translation_kind}"')
            # If translation_kind is None, skip the old line
            continue
        kept.append(line)

    # If we never saw translation_kind in the file and caller provided one
    if not saw_translation_kind and translation_kind is not None:
        kept.append(f'translation_kind = "{translation_kind}"')

    # Build new frontmatter inner
    new_fm_lines: list[str] = kept + [
        "",
        f'prose_hash = "{prose_hash}"',
        f'code_hash = "{code_hash}"',
        f'source_commit = "{source_commit}"',
        'source_locale = "en-US"',
    ]

    result = "+++\n" + "\n".join(new_fm_lines) + "\n+++\n"
    if body:
        result += body
    return result


def _extract_fence_blocks(body: str) -> list[tuple[int, int, str, str]]:
    """Return list of (start_line, end_line, info_string, content).

    Line numbers are 0-based indexes into ``body.split("\\n")``.
    ``end_line`` is the index of the closing `` ``` `` line.
    """
    blocks: list[tuple[int, int, str, str]] = []
    lines = body.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```") and len(line) >= 3:
            start = i
            info = line[3:].strip()
            content_lines: list[str] = []
            i += 1
            while i < len(lines):
                if lines[i].startswith("```"):
                    end = i
                    break
                content_lines.append(lines[i])
                i += 1
            else:
                # Unterminated fence — treat rest as content
                end = len(lines) - 1
            content = "\n".join(content_lines)
            blocks.append((start, end, info, content))
        i += 1
    return blocks


_FENCE_MARKER_RE = re.compile(r"<<<FENCE (\d+)>>>")


def strip_fences_for_prompt(body: str) -> str:
    """Replace each code fence block with a ``<<<FENCE n>>>`` marker.

    Returns the body with fences replaced by markers. The marker index *n*
    corresponds to the document-order position of the fence (0-based).
    """
    blocks = _extract_fence_blocks(body)
    if not blocks:
        return body

    lines = body.split("\n")
    # Process in reverse order so line indices stay valid
    for start, end, _info, _content in reversed(blocks):
        # Replace the entire fence block (including both ``` lines)
        # with a single marker line
        marker = f"<<<FENCE {blocks.index((start, end, _info, _content))}>>>"
        lines[start : end + 1] = [marker]
    return "\n".join(lines)


def reinsert_fences_from_en(translated_body_with_markers: str, en_body: str) -> str:
    """Replace ``<<<FENCE n>>>`` markers with actual fence blocks from en-US.

    If no markers are present, returns *translated_body_with_markers* unchanged.

    Each marker is replaced by the full `` ```info`` … `` ``` `` block from
    the nth fence in *en_body* (document order, 0-based).
    """
    if "<<<FENCE" not in translated_body_with_markers:
        return translated_body_with_markers

    en_blocks = _extract_fence_blocks(en_body)

    def _replace_marker(m: re.Match) -> str:
        idx = int(m.group(1))
        if idx < len(en_blocks):
            _start, _end, info, content = en_blocks[idx]
            fence = f"```{info}\n{content}\n```" if content else f"```{info}\n```"
            return fence
        # Fallback: keep marker if index out of range
        return m.group(0)

    return _FENCE_MARKER_RE.sub(_replace_marker, translated_body_with_markers)


def current_git_head(repo: Path) -> str:
    """Return the full SHA of HEAD in *repo* via ``git rev-parse HEAD``.

    Raises ``subprocess.CalledProcessError`` if the git command fails.
    """
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
        cwd=str(repo),
    )
    return result.stdout.strip()
