# P6 — Traditional Chinese (zh-Hant) · 5-page start packet · 3-model set

**Locale:** `zh-Hant` (繁體中文)  
**Packet:** `start/hello`, `commands`, `examples`, `projects`, `index`  
**Models × pages:** 3 × 5 = **15**  
**Excluded:** `grok-4.5`, `kimi-k2p7-code-fireworks`  
**Prompt:** body-only blinds + `CONTRACT.md` + `launch-*.md.txt` (explicit 繁體 / no 简体)

## Structural

| Model | Fences | Anchors | Chrome / hard fails | Note |
|---|---|---|---|---|
| **gpt-5.6-luna-codex** | PASS all 5 | PASS all 5 | None | Full 繁體 headings; clean body |
| deepseek-v4-pro | PASS | FAIL hello + projects (`{#anchors}` leak) | Launch chrome on hello + projects | Clean commands/examples/index |
| glm-5-2-zai | PASS | FAIL projects | **projects left in English** (prompt chrome heads) | EN Check/Build/Run on commands |

## Rubric means (approx., equal page weights)

| Model | Packet mean | Notes |
|---|---|---|
| **gpt-5.6-luna-codex** | **4.6** | Best natural TW-style tech 繁體; consistent localization |
| deepseek-v4-pro | 3.6 | Strong when clean; chrome contamination costs two pages |
| glm-5-2-zai | 3.2 | examples/index OK; commands EN titles; projects hard-fail |

## Ranking (zh-Hant)

1. **`gpt-5.6-luna-codex`**
2. `deepseek-v4-pro`
3. `glm-5-2-zai`

## Preferred lock

**zh-Hant → `gpt-5.6-luna-codex`**  
Alternates: `deepseek-v4-pro`, `glm-5-2-zai`.

## Contrast with zh-Hans

| Locale | Preferred | Note |
|---|---|---|
| zh-Hans | `glm-5-2-zai` | P2 hello sweep |
| zh-Hant | `gpt-5.6-luna-codex` | P6 full packet — do **not** reuse Hans winner blindly |

## Process

3-model staggered batches; no Grok. Simplified leakage heuristic found no 简体-only character flood on scored clean pages.
