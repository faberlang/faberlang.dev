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

## Production effort (Luna)

Evidence: `ratings/P7-luna-medium-vs-xhigh.md` (same model, 5 locales,
`start/hello`, medium vs xhigh).

| Mode | Effort | Use |
|---|---|---|
| **Bulk / model bench / first draft** | **`medium`** | Default. Fair cost; medium already ranked highly. |
| **Optional polish pass** | **`xhigh`** | Publish-critical pages only. Yields local register/glossary polish, not a full rewrite. One clear win in P7: xhigh fixed residual English table chrome that medium left on zh-Hans. |
| **Manual residual pass** | human / checklist | Always allowed: second pass to strip leftover English snippets (table headers, nav labels, section titles) after any automated translate. Do not rely on effort alone for chrome hygiene. |

**Do not** raise bench default effort above medium for model-vs-model sweeps
(keeps cost and comparison fair). Prefer medium first draft → optional xhigh on
locked Luna locales → manual English-snippet sweep before ship.

Luna-locked locales today: **th-TH**, **hi**, **vi**, **zh-Hant**.
Other locales keep their preferred model at **medium** unless a later effort
sweep says otherwise.

## Notes

- Preference is **per language**, not global.
- Pilot gold exists only for th-TH start track; other locales rate structure +
  native quality without gold when none exists.
