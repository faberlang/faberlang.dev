#!/usr/bin/env python3
"""sync-translate — LLM differential translate tool for locale Markdown files.

Drafts locale-file updates by building structured prompts for an LLM,
applying translated output, and stamping provenance hashes.

Usage:
    sync-translate.py --locale LOC --rel PATH [options]

Modes:
    --write-prompt OUT     Build a structured prompt file for an LLM.
    --stamp-only           Stamp locale file with current en-US hashes only.
    --apply-body FILE      Apply translated output (LLM response) and stamp.
    --merge-en-fences      After apply, replace `` ```faber `` fences with
                           corresponding en-US fences by order.
"""

import argparse
import sys
import tomllib
from pathlib import Path

# Add generator/scripts to sys.path so sync_lib can be imported
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from sync_lib import (  # noqa: E402
    current_git_head,
    hashes_for_markdown,
    load_markdown,
    reinsert_fences_from_en,
    split_frontmatter,
    stamp_frontmatter,
    strip_fences_for_prompt,
)

# Add generator/scripts parent so locales_registry can be imported
_GENERATOR_DIR = _SCRIPT_DIR.parent
if str(_GENERATOR_DIR) not in sys.path:
    sys.path.insert(0, str(_GENERATOR_DIR))

from scripts.locales_registry import load_registry, reader_locale  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _resolve_repo_root(args_path: str | None) -> Path:
    """Resolve repo root from CLI argument or default to parent of generator/."""
    if args_path:
        return Path(args_path).resolve()
    return _SCRIPT_DIR.parent.parent.resolve()


def _workspace_root(repo_root: Path) -> Path:
    """The faberlang workspace root is the parent of the faberlang.dev repo."""
    return repo_root.resolve().parent


def _read_llm_snippet(workspace: Path, reader: str) -> str:
    """Read ``[llm] system_prompt_snippet`` from the reader pack.toml.

    Args:
        workspace: The faberlang workspace root (parent of faberlang.dev/).
        reader: The reader locale code (e.g. ``'th-TH'``, ``'la'``).

    Returns:
        The system_prompt_snippet string, or an empty string if the pack
        file or snippet key is missing.
    """
    pack_path = workspace / "radix" / "stdlib" / "reader" / reader / "pack.toml"
    if not pack_path.is_file():
        print(
            f"warning: pack not found at {pack_path}", file=sys.stderr,
        )
        return ""
    try:
        with pack_path.open("rb") as f:
            data = tomllib.load(f)
        llm_section = data.get("llm", {})
        if isinstance(llm_section, dict):
            return llm_section.get("system_prompt_snippet", "")
        return ""
    except Exception as exc:
        print(f"warning: failed to read pack snippet: {exc}", file=sys.stderr)
        return ""


def _resolve_paths(repo_root: Path, locale: str, rel: str) -> dict:
    """Resolve locale and en-US file paths.

    Returns a dict with:
        rel_path, locale_path, en_path, locale_exists
    """
    src_root = repo_root / "src"
    en_root = src_root / "en-US"
    rel_path = Path(rel)
    locale_path = src_root / locale / rel_path
    en_path = en_root / rel_path
    return {
        "rel_path": rel_path,
        "locale_path": locale_path,
        "en_path": en_path,
        "locale_exists": locale_path.is_file(),
    }


# ---------------------------------------------------------------------------
# Mode handlers
# ---------------------------------------------------------------------------

def _write_prompt(
    locale: str,
    rel: str,
    args: argparse.Namespace,
    repo_root: Path,
) -> int:
    """Write a structured prompt file for LLM translation."""
    paths = _resolve_paths(repo_root, locale, rel)

    if not paths["en_path"].is_file():
        print(
            f"error: en-US source not found: {paths['en_path']}",
            file=sys.stderr,
        )
        return 1

    en_text = load_markdown(paths["en_path"])
    _, en_body = split_frontmatter(en_text)

    # Read locale body (may be fallback text or missing)
    locale_body = ""
    if paths["locale_exists"]:
        locale_text = load_markdown(paths["locale_path"])
        _, locale_body = split_frontmatter(locale_text)

    # Resolve reader locale from registry
    workspace = _workspace_root(repo_root)
    registry = load_registry(repo_root / "generator" / "locales.toml")
    reader = reader_locale(registry, locale)

    # Get LLM snippet
    snippet = _read_llm_snippet(workspace, reader)

    # Build prompt content
    parts: list[str] = []

    # Part 1: System prompt snippet
    if snippet:
        parts.append("## System prompt snippet (reader pack)")
        parts.append("")
        parts.append(snippet)
        parts.append("")

    # Part 2: Instructions
    parts.append("## Instructions")
    parts.append("")
    parts.append(
        "Translate the prose below from English to the target locale. "
        "Follow these rules:"
    )
    parts.append("")
    bullet_rules = [
        "Translate prose only. Do NOT translate code fences.",
        "Preserve {#anchors} (heading anchors) exactly.",
        "Preserve markdown structure (headings, paragraphs, lists).",
        "Preserve table shapes (column count, alignment).",
        "Preserve links. Paths may stay absolute (/start/...) "
        "since the generator prefixes locale paths.",
        'Fences are shown as "<<<FENCE n>>>" markers. Leave these '
        "markers unchanged in your output.",
        "Return the full body text with markers in place.",
    ]
    for rule in bullet_rules:
        parts.append(f"- {rule}")
    parts.append("")

    # Part 3: English body (fences → markers)
    parts.append("## English source body (fences as <<<FENCE n>>>)")
    parts.append("")
    parts.append(strip_fences_for_prompt(en_body))
    parts.append("")

    # Part 4: Current locale body (fences → markers)
    if locale_body:
        parts.append("## Current locale body (fences as <<<FENCE n>>>)")
        parts.append("")
        parts.append(strip_fences_for_prompt(locale_body))
        parts.append("")

    # Part 5: Optional git context
    # If the file already has a source_commit we could show diff,
    # but for MVP just note the en-US file path.
    parts.append("## Notes")
    parts.append("")
    parts.append(f"Source file: {paths['en_path']}")
    parts.append(f"Locale file: {paths['locale_path']}")
    parts.append("")

    prompt_text = "\n".join(parts)

    out_path = Path(args.write_prompt)
    out_path.write_text(prompt_text, encoding="utf-8")
    print(f"Prompt written to {out_path}")

    return 0


def _stamp_only(
    locale: str,
    rel: str,
    _args: argparse.Namespace,
    repo_root: Path,
) -> int:
    """Stamp locale file with current en-US provenance hashes."""
    paths = _resolve_paths(repo_root, locale, rel)

    if not paths["locale_exists"]:
        print(
            f"error: locale file not found: {paths['locale_path']}",
            file=sys.stderr,
        )
        return 1
    if not paths["en_path"].is_file():
        print(
            f"error: en-US source not found: {paths['en_path']}",
            file=sys.stderr,
        )
        return 1

    en_text = load_markdown(paths["en_path"])
    prose_hash, code_hash = hashes_for_markdown(en_text)
    source_commit = current_git_head(repo_root)

    locale_text = load_markdown(paths["locale_path"])
    stamped = stamp_frontmatter(
        locale_text,
        prose_hash=prose_hash,
        code_hash=code_hash,
        source_commit=source_commit,
    )

    paths["locale_path"].write_text(stamped, encoding="utf-8")

    print(f"Stamped {paths['locale_path']}")
    print(f"  prose_hash: {prose_hash}")
    print(f"  code_hash:  {code_hash}")
    print(f"  commit:     {source_commit}")

    return 0


def _apply_body(
    locale: str,
    rel: str,
    args: argparse.Namespace,
    repo_root: Path,
) -> int:
    """Apply translated output from LLM and stamp."""
    paths = _resolve_paths(repo_root, locale, rel)

    if not paths["en_path"].is_file():
        print(
            f"error: en-US source not found: {paths['en_path']}",
            file=sys.stderr,
        )
        return 1

    if not paths["locale_exists"]:
        print(
            f"error: locale file not found (needed for frontmatter): "
            f"{paths['locale_path']}",
            file=sys.stderr,
        )
        return 1

    # Read apply file
    apply_path = Path(args.apply_body)
    if not apply_path.is_file():
        print(f"error: apply file not found: {apply_path}", file=sys.stderr)
        return 1

    apply_text = apply_path.read_text(encoding="utf-8")

    # Read en-US for fences and hashes
    en_text = load_markdown(paths["en_path"])
    _, en_body = split_frontmatter(en_text)
    prose_hash, code_hash = hashes_for_markdown(en_text)
    source_commit = current_git_head(repo_root)

    # Read existing locale for frontmatter
    locale_text = load_markdown(paths["locale_path"])

    # Determine if apply text is full markdown or body-only
    # Full markdown starts with +++
    if apply_text.lstrip().startswith("+++"):
        # Full markdown: take body from apply
        _, apply_body = split_frontmatter(apply_text)
    else:
        # Body-only: use as-is
        apply_body = apply_text

    # Reinsert en-US fences if markers present
    if "<<<FENCE" in apply_body:
        apply_body = reinsert_fences_from_en(apply_body, en_body)

    # If --merge-en-fences, replace ```faber fences with en-US versions
    if args.merge_en_fences:
        apply_body = _merge_en_fences(apply_body, en_body)

    # Reconstruct file: frontmatter + body
    # Use stamp_frontmatter which handles all provenance keys
    reconstructed = stamp_frontmatter(
        locale_text,
        prose_hash=prose_hash,
        code_hash=code_hash,
        source_commit=source_commit,
    )

    # Now replace the body in reconstructed with apply_body
    # We need the stamped frontmatter + apply_body
    stamped_fm_inner, _ = split_frontmatter(reconstructed)
    result = "+++\n" + stamped_fm_inner + "\n+++\n" + apply_body

    # If apply_body has trailing whitespace issues, clean up
    if not result.endswith("\n"):
        result += "\n"

    paths["locale_path"].write_text(result, encoding="utf-8")

    print(f"Applied to {paths['locale_path']}")
    print(f"  prose_hash: {prose_hash}")
    print(f"  code_hash:  {code_hash}")
    print(f"  commit:     {source_commit}")

    return 0


def _merge_en_fences(body: str, en_body: str) -> str:
    """Replace `` ```faber `` fences in *body* with en-US originals.

    Walks the body line by line, replacing each `` ```faber `` fence block
    with the corresponding `` ```faber `` block from *en_body* (by faber-only
    document order, same count required).
    """
    from sync_lib import extract_fences

    # Extract only ```faber fences by order
    def _faber_only(fences):
        return [(i, info, content) for i, (info, content) in enumerate(fences) if info == "faber"]

    en_faber = _faber_only(extract_fences(en_body))
    locale_faber = _faber_only(extract_fences(body))

    if len(locale_faber) != len(en_faber):
        print(
            f"warning: ```faber fence count mismatch "
            f"(locale={len(locale_faber)}, en={len(en_faber)}); "
            f"skipping fence merge",
            file=sys.stderr,
        )
        return body

    if not en_faber:
        return body

    # Rebuild body, replacing each ```faber block with en-US counterpart
    lines = body.split("\n")
    out: list[str] = []
    fi = 0  # index into faber-only lists
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```") and len(line) >= 3:
            info = line[3:].strip()
            if info == "faber" and fi < len(en_faber):
                # Replace this fence block with en-US version
                _orig_idx, en_info, en_content = en_faber[fi]
                out.append(f"```{en_info}")
                if en_content:
                    out.extend(en_content.split("\n"))
                out.append("```")
                # Skip past old locale fence body
                i += 1
                while i < len(lines) and not lines[i].startswith("```"):
                    i += 1
                if i < len(lines):
                    i += 1  # skip closing ```
                fi += 1
            else:
                # Pass through non-faber fences unchanged
                out.append(line)
                i += 1
                while i < len(lines) and not lines[i].startswith("```"):
                    out.append(lines[i])
                    i += 1
                if i < len(lines):
                    out.append(lines[i])
                    i += 1
        else:
            out.append(line)
            i += 1

    return "\n".join(out)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="sync-translate — LLM differential translate tool",
    )
    parser.add_argument(
        "--locale", type=str, required=True,
        help="Locale code (e.g. th-TH)",
    )
    parser.add_argument(
        "--rel", type=str, required=True,
        help="Relative path under src/{locale}/ (e.g. start/hello.md)",
    )
    parser.add_argument(
        "--write-prompt", type=str, default=None,
        metavar="OUT",
        help="Write structured prompt file to OUT",
    )
    parser.add_argument(
        "--apply-body", type=str, default=None,
        metavar="FILE",
        help="Apply LLM output from FILE and stamp",
    )
    parser.add_argument(
        "--stamp-only", action="store_true", default=False,
        help="Only stamp provenance hashes on locale file",
    )
    parser.add_argument(
        "--merge-en-fences", action="store_true", default=False,
        help="After apply, replace ```faber fences with en-US originals",
    )
    parser.add_argument(
        "--repo", type=str, default=None,
        metavar="ROOT",
        help="Repository root path (default: parent of generator/)",
    )

    args = parser.parse_args()
    repo_root = _resolve_repo_root(args.repo)

    # Validate locale + rel
    if not args.locale:
        print("error: --locale is required", file=sys.stderr)
        return 1
    if not args.rel:
        print("error: --rel is required", file=sys.stderr)
        return 1

    # Determine mode
    modes = sum([
        bool(args.write_prompt),
        bool(args.apply_body),
        bool(args.stamp_only),
    ])
    if modes == 0:
        print(
            "error: specify one of --write-prompt, --apply-body, or --stamp-only",
            file=sys.stderr,
        )
        return 1
    if modes > 1:
        print(
            "error: --write-prompt, --apply-body, and --stamp-only are mutually "
            "exclusive",
            file=sys.stderr,
        )
        return 1

    if args.write_prompt:
        return _write_prompt(args.locale, args.rel, args, repo_root)
    elif args.stamp_only:
        return _stamp_only(args.locale, args.rel, args, repo_root)
    elif args.apply_body:
        return _apply_body(args.locale, args.rel, args, repo_root)

    return 0


if __name__ == "__main__":
    sys.exit(main())
