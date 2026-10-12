# Delivery: Phase 5 — sync-translate (LLM differential)

## Goal

Human-run tool that drafts locale-file updates fenced from code, stamps
provenance, lands as a reviewable file change.

## CLI

```
sync-translate.py --locale LOC --rel PATH [--write-prompt OUT | --apply-body FILE | --stamp-only] [--merge-en-fences] [--repo ROOT]
```

PATH is relative to `src/{locale}/` — e.g. `start/hello.md`.

### Modes

| Mode | Flag | Description |
|---|---|---|
| **Write prompt** | `--write-prompt OUT` | Build a structured prompt file for an LLM (includes pack system_prompt_snippet, en-US body with fences stripped to `<<<FENCE n>>>` markers, current locale body, and instructions). |
| **Apply body** | `--apply-body FILE` | Take LLM output (full markdown or body-only), re-insert en-US fence blocks from markers, stamp provenance hashes, write to locale path. |
| **Stamp only** | `--stamp-only` | Recompute en-US hashes and stamp locale frontmatter without changing prose. Useful for files that were manually updated or are fallback-ok. |

### Additional flags

| Flag | Description |
|---|---|
| `--merge-en-fences` | After `--apply-body`, replace `` ```faber `` fences in the output with corresponding fences from en-US by order (same count required). |
| `--repo ROOT` | Repo root path (default: parent of `generator/scripts/`). |

### Prompt file structure

1. `[llm] system_prompt_snippet` from `radix/stdlib/reader/{reader_locale}/pack.toml`
2. Instructions: translate prose only; preserve anchors, structure, tables, links; do NOT translate code; leave `<<<FENCE n>>>` markers unchanged
3. English source body (fences replaced by `<<<FENCE n>>>` markers)
4. Current locale body (fences replaced by markers), if the file exists
5. Source/locale file paths reference

## sync_lib.py additions (Phase 5)

```python
def load_markdown(path: Path) -> str: ...

def stamp_frontmatter(text, prose_hash, code_hash, source_commit, translation_kind=None) -> str: ...

def strip_fences_for_prompt(body: str) -> str: ...

def reinsert_fences_from_en(translated_body_with_markers: str, en_body: str) -> str: ...

def current_git_head(repo: Path) -> str: ...
```

## Stamp format

Sets the following frontmatter keys:
- `prose_hash = "sha256:..."` (over body with fences stripped)
- `code_hash = "sha256:..."` (over fence payloads only)
- `source_commit = "<full SHA>"`
- `source_locale = "en-US"`
- Removes legacy `source_hash` if present
- Preserves `title`, `section`, `order`, `sources`, and all other keys

## Apply algorithm

1. Read apply file. If it starts with `+++`, treat as full markdown and extract body. Otherwise treat as body-only.
2. If the body contains `<<<FENCE n>>>` markers, replace each with the corresponding fence block from the current en-US source (by document order).
3. If `--merge-en-fences` is set, replace `` ```faber `` fences with corresponding en-US fences (by order, same count).
4. Compute prose_hash and code_hash from current en-US source.
5. Get `source_commit` from `git rev-parse HEAD` in the repo.
6. Stamp frontmatter on the existing locale file (preserving all non-provenance keys).
7. Replace the body with the translated body.
8. Write to `src/{locale}/{rel}`.

## Gate (for parent apply run)

One file (`th-TH/start/hello.md`) updated with Thai prose (or honest Thai
translation of lead), fences preserved, provenance stamped, sync-report
classifies that file as `current`.
