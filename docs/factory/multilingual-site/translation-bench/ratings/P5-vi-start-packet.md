# P5 — Vietnamese (vi) · 5-page start packet · 3-model set (staggered)

**Locale:** `vi`  
**Packet:** `start/hello`, `commands`, `examples`, `projects`, `index`  
**Models × pages (scored):** 3 × 5 = **15**  
**Cut mid-run:** `grok-4.5` (not scored further)  
**Prompt:** English body only + external `CONTRACT.md` + `launch-*.md.txt`

## Process change (this phase)

| Change | Why |
|---|---|
| Drop **`grok-4.5`** from default set | Consistently last/near-last on th/zh/ar/hi; latency 3–5× peers (hello/commands often ~3–4 min vs ~20–80 s) |
| Score **3 models** only | `gpt-5.6-luna-codex`, `deepseek-v4-pro`, `glm-5-2-zai` |
| Historical Grok files | Keep under `outputs/vi/grok-4.5__*` for audit; no new Grok jobs |

## Structural

| Model | Fences / anchors | Full VI headings | Residual issues |
|---|---|---|---|
| **gpt-5.6-luna-codex** | PASS all 5 | Best (Check/Run localized on commands) | Light tech loans OK (`Build`, package names) |
| deepseek-v4-pro | FAIL examples (chrome + extra `{#anchors}`) | Mixed | EN section titles Check/Build/Run; examples includes translated launch chrome |
| glm-5-2-zai | PASS all 5 | Good | EN Check/Build/Run on commands; solid elsewhere |

## Rubric means (approx., equal page weights; hard-fail pulls examples down for deepseek)

| Model | Packet mean | Notes |
|---|---|---|
| **gpt-5.6-luna-codex** | **4.5** | Most consistent natural tech Vietnamese; best heading localization |
| glm-5-2-zai | 4.2 | Clean structure; slightly more calque / EN CLI headings |
| deepseek-v4-pro | 3.4 | Strong when clean; examples hard-fail (prompt chrome in body) |

## Ranking (vi)

1. **`gpt-5.6-luna-codex`**
2. `glm-5-2-zai`
3. `deepseek-v4-pro`

## Preferred lock

**vi → `gpt-5.6-luna-codex`**  
Alternates: `glm-5-2-zai`, `deepseek-v4-pro`.

## Timing notes (why Grok is out)

| Model | Typical page wall-clock (this run) |
|---|---|
| glm-5-2-zai | ~20–30 s |
| deepseek-v4-pro | ~40–65 s |
| gpt-5.6-luna-codex | ~40–85 s |
| grok-4.5 (pre-cut) | ~180–250 s |

## Next

- Optional: re-run deepseek examples only if volume alternate needed (not required for lock).
- Next open locale in PREFERRED-MODELS: **zh-Hant**.
