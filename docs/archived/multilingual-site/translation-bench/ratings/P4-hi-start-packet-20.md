# P4 — Hindi (hi) · 5-page start packet · 20 agents (staggered)

**Locale:** `hi`  
**Packet:** `start/hello`, `commands`, `examples`, `projects`, `index`  
**Models × pages:** 4 × 5 = 20  
**Launch:** page batches of 4 models; pause between batches (not 20-wide fan-out)  
**Prompt hygiene:** English body only + separate `CONTRACT.md` (after first contaminated hello batch)

## Launch notes

| Item | Detail |
|---|---|
| Stagger | One page → 4 models → wait → next page |
| 429 | None this run |
| Prompt fix | First hello batch translated raw sync-translate chrome; discarded. Re-ran with body-only blinds |

## Structural

| Model | Fences / anchors | Full Hindi headings | Residual EN |
|---|---|---|---|
| gpt-5.6-luna-codex | PASS all 5 | PASS | Light tech loans OK |
| deepseek-v4-pro | PASS | PASS | Some EN link labels (examples nav) |
| glm-5-2-zai | PASS | PASS | Highly Sanskritized register |
| grok-4.5 | PASS | PASS | EN table headers on projects; mixed lead on examples |

## Rubric means (approx., equal page weights)

| Model | Packet mean | Notes |
|---|---|---|
| **gpt-5.6-luna-codex** | **4.6** | Best modern tech Hindi; even across pages |
| deepseek-v4-pro | 4.4 | Reliable; slightly stiffer |
| glm-5-2-zai | 4.1 | Formal/Sanskrit-heavy (`फलन`, `अभिकर्ता`) — less site-voice |
| grok-4.5 | 3.9 | EN table header leaks; code-mixed |

## Ranking (hi)

1. **`gpt-5.6-luna-codex`**
2. `deepseek-v4-pro`
3. `glm-5-2-zai`
4. `grok-4.5`

## Preferred lock

**hi → `gpt-5.6-luna-codex`**  
Alternates: `deepseek-v4-pro`, `glm-5-2-zai`.

## Process

Staggered launch avoided rate limits. Keep **body-only** blind files + external CONTRACT for all future languages.
