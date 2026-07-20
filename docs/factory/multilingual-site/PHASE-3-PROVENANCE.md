# Delivery: Phase 3 — Provenance + sync-report oracle

## Interpreted unit

Implement Decision 18d two-hash provenance (`prose_hash`, `code_hash`,
`source_commit`) and a `sync-report` oracle that flags locale pages whose
English source has drifted. Not a build step — human-run tooling.

## Normalized spec

### Hash basis (reproducible)

Given an `en-US` Markdown file:

1. Split `+++` TOML frontmatter from body.
2. **Code fences** = every fenced block matching CommonMark triple-backtick
   fences (opening line ` ``` ` optional info string, body until closing fence).
3. **`prose_hash`** = `sha256:` + hex of UTF-8 body with each fence block
   replaced by a stable placeholder `\n```\n\n```\n` (or empty fence marker)
   so fence *content* changes do not affect prose hash. Leading/trailing
   whitespace of the residual prose is not reflowed beyond fence removal.
4. **`code_hash`** = `sha256:` + hex of the concatenation of fence bodies only
   (info string + body), each fence separated by `\n---\n`, in document order.
5. **`source_commit`** = full git commit SHA of the repo tip when the locale
   file was last stamped as in sync with that `en-US` content (recorded in
   locale frontmatter; empty/missing ⇒ never stamped).

### Frontmatter keys (locale files)

```toml
prose_hash = "sha256:…"      # of paired en-US at last sync
code_hash = "sha256:…"
source_commit = "abc123…"    # git SHA
source_locale = "en-US"      # keep existing
translation_kind = "fallback" | "translated" | …
# source_hash retained if present but ignored by oracle (legacy)
```

### sync-report CLI

```
sync-report.py [--locale th-TH] [--json] [repo_root]
```

For each `src/{locale}/**/*.md` (excluding `en-US`):

| Bucket | Condition |
|---|---|
| `missing_en` | No paired `src/en-US/{rel}` |
| `missing_provenance` | No `prose_hash` (or empty) — treat as needs sync |
| `stale_prose` | `prose_hash` ≠ current en-US prose_hash |
| `stale_code_only` | prose matches but `code_hash` ≠ en-US code_hash |
| `current` | both hashes match |
| `legacy_source_hash` | note if only old `source_hash` present |

Print human summary + optional JSON. Exit 0 by default (report is informational).
`--fail-on-stale` exit 1 if any non-current.

### Self-check (zero false positive on example-only edits)

Unit test or `--self-check` mode:

1. Take a fixture body with prose + fence.
2. Mutate only fence interior → `prose_hash` unchanged, `code_hash` changes.
3. Mutate only prose → `prose_hash` changes, `code_hash` unchanged.

### Gate

- Running `sync-report` on the live tree reports existing locale slices as
  non-current (missing provenance and/or legacy stale `source_hash`).
- Self-check passes.

## Non-goals

- Auto-stamping locale files in this phase (stamp lands with sync-translate).
- LLM translation (Phase 5).
- Build integration (oracle is not a build gate by default).

## Implementation work — DONE

| ID | Work | Path | Status |
|---|---|---|---|
| W1 | Shared hash/split helpers | `generator/scripts/sync_lib.py` | done |
| W2 | Oracle CLI | `generator/scripts/sync-report.py` | done |
| W3 | Self-check | `sync-report.py --self-check` | done |
| W4 | Delivery + factory ledger | docs | done |

## Validation — PASS

```bash
python3 generator/scripts/sync-report.py --self-check
# self-check: PASS

python3 generator/scripts/sync-report.py --locale th-TH
# === sync-report th-TH ===
# missing_provenance: 7
# stale_prose: 0
# ...
#   src/th-TH/index.md  missing_provenance  (legacy source_hash present)
```
