# P3 — Arabic (ar) · 5-page start packet · 20 agents

**Locale:** `ar`  
**Packet:** `start/hello`, `commands`, `examples`, `projects`, `index`  
**Models (×5 pages = 20):** `gpt-5.6-luna-codex`, `deepseek-v4-pro`, `glm-5-2-zai`, `grok-4.5`  
**Mode:** blind; parallel subagents  
**Gold:** none (ar start is English fallback only)

## Ops notes

| Event | Detail |
|---|---|
| Parallel launch | 20 agents fired together |
| Rate limit | 1× `glm-5-2-zai` · `start-index` → HTTP 429; **retried OK** |
| Kimi | not in set |

## Structural summary (by model × page)

Legend: ✓ pass · ~ minor · ✗ hard issue

| Page | luna | deepseek | glm | grok |
|---|---|---|---|---|
| hello | ✓ | ✓ | ✓ | ✓ |
| commands | ✓ | ✓ | ✓ | ~ EN lead para left |
| examples | ✓ | ✓ | ✓ | ✓ |
| projects | ✓ | ✓ | ~ name garble “فaber” | ✓ |
| index | ✗ translated **prompt Notes/contract** into body | ✓ | ✓ (retry) | ✓ |

All models preserved fence markers and required `{#anchors}` on scored pages (except luna index contamination).

## Rubric means (equal page weights; 1–5)

Approximate judgment pass (structure + Arabic naturalness + term discipline):

| Model | hello | commands | examples | projects | index | **Packet mean** |
|---|---|---|---|---|---|---|
| **gpt-5.6-luna-codex** | 4.6 | **4.8** | **4.7** | **4.6** | **2.0** | **4.1** |
| **deepseek-v4-pro** | 4.4 | 4.5 | 4.5 | 4.4 | **4.5** | **4.5** |
| **glm-5-2-zai** | 4.3 | 4.4 | 4.3 | 3.8 | 4.3 | **4.2** |
| **grok-4.5** | 4.4 | 3.5 | 4.4 | 4.4 | 4.3 | **4.2** |

### Callouts

**deepseek-v4-pro — preferred for ar on this packet**  
- Even quality across all five pages; no instruction-leak; no invented anchors.  
- Clear MSA technical register; tables fully localized.

**gpt-5.6-luna-codex**  
- Best single-page work on commands/examples when clean.  
- **index** included Arabic translation of the *prompt’s Notes/Output contract* → hard fail that page. Needs stricter “stop after last real section” or strip Notes from files agents read.  
- Packet mean pulled down by index only; still excellent for 4/5 pages.

**glm-5-2-zai**  
- Solid; 429 under 20-wide fanout (retry worked).  
- Occasional brand garble (Latin/Arabic mix on “Faber”).

**grok-4.5**  
- Better than Thai (Arabic headings present).  
- **commands** left English opening paragraph — residual EN leak mode.

## Ranking (ar · this packet)

1. **`deepseek-v4-pro`** — most reliable across all five pages  
2. `gpt-5.6-luna-codex` — highest peak quality; fix prompt hygiene for long packets  
3. `glm-5-2-zai` / `grok-4.5` — usable; watch rate limits / EN leaks  

## Preferred lock

**ar → `deepseek-v4-pro`**  
Alternates: `gpt-5.6-luna-codex` (with prompt scrub), `glm-5-2-zai`.

## Process lessons (20-wide)

1. Fan-out hits provider 429 — plan retries for tail jobs.  
2. Blind prompt files must not append Notes after English body if models may translate the whole file; put contracts **above** the English body or outside the file agents read.  
3. Language-dependent winners confirmed again (luna ≠ deepseek ≠ glm).

## Follow-ups

- Re-run luna `start-index` alone after scrubbing Notes from blind prompt.  
- Optionally store full bodies under `outputs/ar/` for archival (large).  
- Next locale: `hi` or `vi` or `zh-Hant` with same 20-wide pattern.
