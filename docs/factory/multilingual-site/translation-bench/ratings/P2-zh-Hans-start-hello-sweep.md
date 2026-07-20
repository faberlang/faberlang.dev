# P2 model sweep — zh-Hans · start/hello (blind)

Four-model set. No pilot gold (zh-Hans start is English fallback only).

## Structural

| Model | Fences | Required anchors | Invented structure | EN section titles left | Table headers localized |
|---|---|---|---|---|---|
| gpt-5.6-luna-codex | PASS | PASS | no | no | partial (Source/Meaning/Previous/Next left EN) |
| deepseek-v4-pro | PASS | PASS | **YES** — extra H2 + `{#write-smallest-faber-program}` | no | partial |
| glm-5-2-zai | PASS | PASS | no | no | **yes** |
| grok-4.5 | PASS | PASS | no | no | **yes** |

## Rubric (1–5)

| Axis | luna | deepseek | glm | grok |
|---|---|---|---|---|
| Fidelity | 4 | **2** (invented heading/anchor) | **5** | 4 |
| Code integrity | 5 | 5 | 5 | 5 |
| Naturalness | 4 | 4 | **5** | 4 |
| Terminology | 4 | 3 | **4** | 3 |
| Register | 4 | 4 | **5** | 4 |
| **Mean** | **4.2** | **3.6** | **4.8** | **4.0** |

### Notes

- **glm-5-2-zai** — clean structure, full heading + table localization, natural instructional Chinese. Preferred for zh-Hans on this sample.
- **gpt-5.6-luna-codex** — strong prose; left some English table headers; “区域设置” is OS-locale flavored but readable.
- **grok-4.5** — recovered from Thai failure mode (Chinese headings present); mixes English “reader/Reader” in locale section.
- **deepseek-v4-pro** — invented an extra lead heading with a **new anchor** → hard structural fail for site docs.

## Ranking (zh-Hans · this page)

1. **`glm-5-2-zai`**
2. `gpt-5.6-luna-codex`
3. `grok-4.5`
4. `deepseek-v4-pro` (not preferred for zh-Hans without stricter structure rules)

## Preferred lock

**zh-Hans → `glm-5-2-zai`** (alternates: luna, grok).
