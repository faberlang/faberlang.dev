# Production translate — all docs × all locales

**Status:** setup law (not yet fully executed)  
**Orchestration:** parallel Grok Build agents (parent Mind / this session)  
**Models:** per-locale preferred from `translation-bench/PREFERRED-MODELS.md`  
**Effort:** **medium** first draft; optional **xhigh** polish later; **manual**
English-snippet pass before ship.

## Scale

| Item | Count |
|---|---|
| English pages (`src/en-US/**/*.md`) | **48** |
| Target locales | **6** (`th-TH`, `zh-Hans`, `zh-Hant`, `ar`, `hi`, `vi`) |
| Full matrix cells | **288** |
| Already present (start track + home) | **7 × 6 = 42** (quality mixed; re-translate or keep) |
| Missing locale files | **~246** |

### Preferred model per locale

| Locale | Model | Effort (draft) |
|---|---|---|
| th-TH | `gpt-5.6-luna-codex` | medium |
| zh-Hans | `glm-5-2-zai` | medium |
| zh-Hant | `gpt-5.6-luna-codex` | medium |
| ar | `deepseek-v4-pro` | medium |
| hi | `gpt-5.6-luna-codex` | medium |
| vi | `gpt-5.6-luna-codex` | medium |

## Architecture (one job = one file)

```text
en-US/{rel}
    │
    ▼
[1] scaffold   → src/{locale}/{rel}  (frontmatter shell if missing)
    │
    ▼
[2] write-prompt (body-only contract) → prompts/prod/{locale}/{rel}.prompt.md
    │
    ▼
[3] Grok agent (preferred model, medium, parallel)
    │   writes body-only → outputs/prod/{locale}/{rel}.body.md
    │
    ▼
[4] apply-body --merge-en-fences → src/{locale}/{rel}
    │
    ▼
[5] structural gate (fences, anchors, no chrome)
    │
    ▼
[6] later: manual residual EN pass + optional xhigh polish
```

### Tools already in repo

| Step | Tool |
|---|---|
| Prompt | `generator/scripts/sync-translate.py --write-prompt` |
| Apply + stamp | `sync-translate.py --apply-body FILE --merge-en-fences` |
| Staleness oracle | `generator/scripts/sync-report.py` |
| Preferred models | `translation-bench/PREFERRED-MODELS.md` |
| Job queue | `generator/scripts/translate-queue.py` (manifest) |

**Prompt hygiene (from bench):** agents must translate **English body only** —
no “Current locale body”, no post-body Notes path chrome in the *agent return*.
Contract + body-only is safer than raw `sync-translate` prompts that include
current locale + Notes (those caused chrome contamination in P4/P5/P6).

## Parallel Grok agent layout

### Unit of work

One agent job = **one** `(locale, rel)` pair.  
Writes **one** body file. Does not edit other locales. Does not commit.

### Waves (do not launch 288 at once)

| Wave | Scope | Jobs (approx) | Why first |
|---|---|---|---|
| **W0** | Scaffold missing files for all locales | 246 scaffolds | Apply requires locale path |
| **W1** | `start/**` + root `index.md` re-sync with preferred models | 7 × 6 = 42 | Public onboarding path |
| **W2** | `features/**` | 8 × 6 = 48 | Core language story |
| **W3** | `syntax/**` | 12 × 6 = 72 | Dense technical |
| **W4** | `tooling/**` + `ecosystem/**` | 14 × 6 = 84 | Tooling + packages |
| **W5** | `references/**` + `history/**` + `404.md` | 7 × 6 = 42 | Long-tail |

### Concurrency

| Setting | Value | Rationale |
|---|---|---|
| Max parallel agents | **8–12** (start 8) | Avoid provider 429s; bench learned stagger helps |
| Grouping | Prefer same **locale** per wave slice | Sticky model + pack snippet |
| Isolation | Shared workspace; **non-overlapping paths** | Multi-agent dirt rules |
| Effort | `medium` | Production law; xhigh later |
| Subagent type | `general-purpose` | read-write to output path only |

Parent loop:

1. Build/read job manifest (`translate-queue.py --wave W1`).
2. Take next N pending jobs (N ≤ concurrency).
3. `spawn_subagent` × N with `model` = preferred for that locale.
4. Wait for batch; apply-body for each success; structural check.
5. Mark jobs done/failed; refill until wave empty.
6. `sync-report.py --locale LOC` smoke; commit wave when green.

### Agent prompt contract (per job)

```text
1. Read launch prompt at prompts/prod/{locale}/{rel_slug}.prompt.md
2. Translate to target locale only.
3. Write ONLY translated Markdown body to outputs/prod/{locale}/{rel_slug}.body.md
4. Keep <<<FENCE n>>> and {#anchors}; absolute paths; Latin Faber tokens in code.
5. No frontmatter, no contract, no notes.
6. Print: DONE fences=N
```

Parent (not agent) runs apply:

```bash
python3 generator/scripts/sync-translate.py \
  --locale th-TH --rel start/hello.md \
  --apply-body outputs/prod/th-TH/start-hello.body.md \
  --merge-en-fences
```

## Scaffold rule (W0)

For each missing `src/{locale}/{rel}`:

1. Copy en-US frontmatter keys: `title`, `section`, `order`, `sources`.
2. Set `translation_kind = "pending"` (or omit until apply).
3. Body may be English placeholder **or** empty one-liner — apply replaces body.
4. Do **not** stamp as current until real translate applies.

`translate-queue.py --scaffold` can create these shells.

## Structural gate (per applied file)

Hard fail → do not commit that file; requeue job:

- Fence count matches en-US (via markers reinsert).
- All `{#anchors}` from en-US present.
- No launch chrome (`System prompt`, `Instructions`, `CONTRACT`, `PAGE TO`).
- Table column counts match (spot-check for dense pages).
- `sync-report` classifies file **current** after apply.

## Residual English pass (after waves)

Separate from agent fan-out:

1. Grep locale trees for common EN leftovers (Previous/Next, Source/Meaning,
   Check/Build/Run as section titles when prose is translated, etc.).
2. Human or single high-effort Luna pass per hit list.
3. Optional **xhigh** only on publish-critical pages (start + home).

## Commits

| Cadence | Rule |
|---|---|
| Per wave locale | One commit per `(wave, locale)` or per wave if small |
| Message | `i18n({locale}): translate {wave} pages via {model}` |
| Never | Agent commits; parent only after gate |

## What we do **not** do

- Do not use Grok as preferred translator model (bench-excluded).
- Do not run 288 agents in one fan-out.
- Do not put apply/stamp inside every agent (parent owns apply for provenance).
- Do not skip scaffold (apply requires locale file).
- Do not treat medium draft as ship-ready without residual EN pass on critical paths.

## Quick start (operator)

```bash
cd /Users/ianzepp/work/faberlang/faberlang.dev

# 1) Emit full job matrix + W1 slice
python3 generator/scripts/translate-queue.py --write-manifest \
  docs/factory/multilingual-site/translate-jobs.json
python3 generator/scripts/translate-queue.py --wave W1 --list

# 2) Scaffold missing shells
python3 generator/scripts/translate-queue.py --scaffold --wave all

# 3) Build body-only prompts for a wave
python3 generator/scripts/translate-queue.py --wave W1 --write-prompts

# 4) Parent session: spawn ≤8 agents on pending W1 jobs (preferred models)
# 5) Parent: apply-body each success; structural gate; commit per locale
# 6) sync-report.py --locale th-TH  # etc.
```

## Open decisions (defaults if silent)

| Decision | Default |
|---|---|
| Re-translate existing 42 start/home pages? | **Yes** in W1 with preferred model (bench winners; old start may predate lock) |
| Title frontmatter translate? | **Yes** when applying (agent returns body only; parent may leave en title until residual pass, or include title line in contract later) |
| 404.md | Translate in W5 |
| Parallelism | Start **8**, raise to 12 if no 429s |

## Related

- `translation-bench/PREFERRED-MODELS.md` — models + effort law  
- `translation-bench/METHOD.md` — bench protocol  
- `PHASE-5-SYNC-TRANSLATE.md` — apply/stamp mechanics  
- `GOAL.md` — sync-translate is offline, reviewed, committed  
