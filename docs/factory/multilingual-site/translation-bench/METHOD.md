# Translation model bench — method

**Goal.** Choose preferred LLM(s) for site prose translation, with target
language as a first-class dimension.

## Protocol

1. **Packet** — fixed set of English Markdown pages (or one page for a trial).
2. **Prompt** — built from `sync-translate.py --write-prompt` (reader pack
   snippet + fence markers). For blind trials, strip “Current locale body”.
3. **Target** — one site locale per trial (e.g. `th-TH`).
4. **Models** — from Grok Build subagent model list; one model per run.
5. **Output** — translated body only; fence markers preserved.
6. **Rating** — human or auditor scores (see rubric). Store under `outputs/`
   and `ratings/`.

## Rubric (1–5 each; higher better)

| Axis | 5 means |
|---|---|
| **Fidelity** | Same facts, links, anchors, tables; no invented steps |
| **Code integrity** | All `<<<FENCE n>>>` intact; no translated fence contents |
| **Naturalness** | Native-quality target prose, not calque English |
| **Terminology** | Stable Faber/tech terms (or consistent choices) |
| **Register** | Matches site voice (direct STE-like technical English → equivalent) |

**Hard fails (score 0 overall):** missing fences, changed `{#anchors}`,
translated code, broken table shape, missing sections.

## Phases

| Phase | Scope |
|---|---|
| **P0 method proof** | 1 page, 1 target, 1 model |
| **P1 model sweep** | Same packet + target, N models in parallel |
| **P2 language matrix** | Best candidates × additional targets |

## P0 defaults

| Field | Value |
|---|---|
| Page | `start/hello.md` |
| Target | `th-TH` |
| Gold | pilot `src/th-TH/start/hello.md` (rating only; not in blind prompt) |
| First model | `deepseek-v4-pro` |
| Thai preferred | **`gpt-5.6-luna-codex`** (see PREFERRED-MODELS.md) |
| Default set (3) | `gpt-5.6-luna-codex`, `deepseek-v4-pro`, `glm-5-2-zai` |
| Excluded | `kimi-k2p7-code-fireworks` (Fireworks); `grok-4.5` (rank + latency) |

## Layout

```text
translation-bench/
  METHOD.md
  packet/           English sources (+ optional gold)
  prompts/          Generated prompts
  outputs/          {model}__{locale}__{page}.md
  ratings/          score sheets
```
