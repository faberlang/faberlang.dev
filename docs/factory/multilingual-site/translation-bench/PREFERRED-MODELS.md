# Preferred translation models by target language

Updated as bench phases complete. Prefer these for site prose unless a later
sweep overturns the result.

| Target (`site_locale`) | Preferred model | Alternates (volume) | Evidence | Status |
|---|---|---|---|---|
| **th-TH** | **`gpt-5.6-luna-codex`** | `deepseek-v4-pro`, `glm-5-2-zai` | P0+P1 `start/hello` blind | **locked for now** |
| **zh-Hans** | **`glm-5-2-zai`** | `gpt-5.6-luna-codex`, `deepseek-v4-pro` | P2 `start/hello` blind | **locked for now** |
| **zh-Hant** | **`gpt-5.6-luna-codex`** | `deepseek-v4-pro`, `glm-5-2-zai` | P6 5-page staggered (15 agents) | **locked for now** |
| **ar** | **`deepseek-v4-pro`** | `gpt-5.6-luna-codex`, `glm-5-2-zai` | P3 5-page start packet (20 agents) | **locked for now** |
| **hi** | **`gpt-5.6-luna-codex`** | `deepseek-v4-pro`, `glm-5-2-zai` | P4 5-page staggered (20 agents) | **locked for now** |
| **vi** | **`gpt-5.6-luna-codex`** | `glm-5-2-zai`, `deepseek-v4-pro` | P5 5-page staggered (15 agents; Grok cut) | **locked for now** |

## Default model set (P5+)

Three models only:

1. `gpt-5.6-luna-codex`
2. `deepseek-v4-pro`
3. `glm-5-2-zai`

**Excluded from further sweeps:**
- `kimi-k2p7-code-fireworks` — Fireworks unhealthy at pilot
- `grok-4.5` — consistently bottom-ranked (th/zh/ar/hi); high latency
  (often 3–5× slower than peers). Historical outputs kept under `outputs/`
  for audit; do not launch new Grok jobs for this bench.

## Notes

- Preference is **per language**, not global.
- Pilot gold exists only for th-TH start track; other locales rate structure +
  native quality without gold when none exists.
