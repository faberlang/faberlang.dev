# P7 — Luna medium vs xhigh · 5 languages · `start/hello`

**Model:** `gpt-5.6-luna-codex` only  
**Page:** `start/hello` (same English body + contract style)  
**New runs:** **5 × xhigh** (one per language)  
**Baselines:** prior **medium** outputs from P0–P6 (plus hi medium restored same day — was missing on disk)

| Locale | Medium source | xhigh run |
|---|---|---|
| th-TH | P1 bench file | headless `--effort xhigh` |
| zh-Hans | P2 bench file | headless `--effort xhigh` |
| hi | restored headless `--effort medium` (same prompt as xhigh) | headless `--effort xhigh` |
| vi | P5 bench file | headless `--effort xhigh` |
| zh-Hant | P6 bench file | headless `--effort xhigh` |

**Agent budget:** 5 xhigh (+ 1 medium restore for hi only). Not 25.

## Structural (both efforts)

All 10 bodies: **4/4 fences**, anchors intact, no launch chrome. Hard-fail rate: **0**.

## Similarity (character SequenceMatcher)

| Locale | Identical? | Similarity | Approx. nature of delta |
|---|---|---|---|
| th-TH | no | **0.85** | densest rewrite; wording + heading specificity |
| zh-Hans | no | **0.89** | heading polish; **table chrome localized** at xhigh |
| hi | no | **0.90** | synonym / loanword swaps (cleanest A/B: same prompt day) |
| vi | no | **0.93** | light polish; slightly more explicit headings |
| zh-Hant | no | **0.94** | heading synonymy; small register tweaks |

No locale produced a wholesale rewrite. Effort change is **local lexical/register polish**, not a different translation strategy.

## Where xhigh looked better

| Locale | Signal |
|---|---|
| **zh-Hans** | Medium left `| Source \| Meaning |` and `| Previous \| Next |` in English; **xhigh fully localized** table headers/nav. Clear quality win. |
| **th-TH** | Headings more specific (`ตรวจสอบแพ็กเกจ`, `เรียกใช้แพ็กเกจ`); prose reflow more natural in places. |
| **vi** | Headings slightly more explicit (`Kiểm tra gói`, `Chạy chương trình`); minor glossary consistency. |
| **zh-Hant** | Mostly synonymy (`先決`→`先備`, `語系`→`地區設定`); neither clearly wrong. |

## Where xhigh was mixed / not clearly better

| Locale | Signal |
|---|---|
| **hi** | xhigh preferred more English-coded tech loans (`एंट्री पॉइंट`) vs medium’s more native `प्रवेश-बिंदु`. Site-voice preference is subjective; medium may read more “Hindi-first.” |
| **zh-Hant** | High similarity; changes are preference-level, not error fixes. |

## Caveats

1. **Medium baselines for th / zh-Hans / vi / zh-Hant** come from earlier subagent runs (also medium, but not the same headless harness / day). **hi** is the only true same-prompt same-day pair.
2. `start/hello` is short. Effort curve may be steeper on longer pages (examples/index).
3. Wall-clock for these headless xhigh shots was short (~30–40s parallel batch); do not treat that as “xhigh is free.”

## Conclusion

| Question | Answer |
|---|---|
| Does xhigh change the prose? | **Yes** — all 5 locales differ from medium. |
| Is it a steep quality jump? | **Not on this page.** ~0.85–0.94 similar; polish, not a new draft. |
| Worth xhigh for production? | **Yes for polish-sensitive ship** (esp. if medium leaves EN chrome, as zh-Hans medium did). **Medium remains strong** for volume. |
| Prefer default for Luna site work | **medium for bulk**; **xhigh for final pass / preferred-locale publish** of critical pages. |

## Recommendation

- Keep **medium** as the bench default for model-vs-model fairness and cost.
- For locked Luna locales (th-TH, hi, vi, zh-Hant), optional **xhigh final pass** on publish-critical pages.
- Do **not** expect xhigh to reverse a model ranking from medium (this test is same-model only).
