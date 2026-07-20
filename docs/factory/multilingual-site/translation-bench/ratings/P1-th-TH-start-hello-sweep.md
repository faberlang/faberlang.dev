# P1 model sweep — th-TH · start/hello (blind)

Same packet and target as P0. Gold: pilot `src/th-TH/start/hello.md` (rating only).

## Models

| Model | Status | Notes |
|---|---|---|
| `deepseek-v4-pro` | scored | P0 + P1 |
| `glm-5-2-zai` | scored | |
| `gpt-5.6-luna-codex` | scored | |
| `grok-4.5` | scored | left **English section headings** |
| `kimi-k2p7-code-fireworks` | **SKIPPED** | Fireworks path down / hung; excluded per operator |

## Hard-fail / structural

| Model | Fences 0–3 | Anchors | Latin tokens | Thai script | Section titles Thai |
|---|---|---|---|---|---|
| deepseek-v4-pro | PASS | PASS | PASS | PASS | PASS |
| glm-5-2-zai | PASS | PASS | PASS | PASS | PASS |
| gpt-5.6-luna-codex | PASS | PASS | PASS | PASS | PASS |
| grok-4.5 | PASS | PASS | PASS | PASS | **FAIL** (all 7 English) |

## Rubric (1–5)

| Axis | deepseek-v4-pro | glm-5-2-zai | gpt-5.6-luna | grok-4.5 |
|---|---|---|---|---|
| Fidelity | 4 | 4 | **5** | 3 |
| Code integrity | **5** | **5** | **5** | **5** |
| Naturalness | 4 | 4 | **5** | 3 |
| Terminology | 4 | 4 | **4** | 3 |
| Register | 4 | 4 | **5** | 2 |
| **Equal-weight mean** | **4.2** | **4.2** | **4.8** | **3.2** |

### Notes by model

**gpt-5.6-luna-codex (leader for th-TH on this page)**  
- Full Thai headings; polished instructional voice close to pilot.  
- Link labels localized (`ติดตั้งและดาวน์โหลด`) while paths stay absolute — matches pilot style.  
- Minor line-wrapping in paragraphs only; structure intact.  
- “โลแคลของผู้อ่าน” for Reader locale is reasonable; slightly calque but clear.

**deepseek-v4-pro**  
- Strong structure; more English parenthetical glosses on compiler stages (lexing/parsing).  
- Slightly more formal/explanatory than pilot; still publishable with light edit.

**glm-5-2-zai**  
- Very close to deepseek quality; solid Thai headings.  
- Semi-colons and denser sentences; “โลเคล” spelling variant.  
- Publishable; prefer luna if choosing one.

**grok-4.5**  
- Prose body OK, but **left English heading text** (`## Prerequisites`, etc.) while keeping `{#anchors}` — hard fail for “feels localized” and worse SEO/nav scan.  
- Link **labels** also left in English (`[Install and download]`).  
- Would need a second pass or stricter prompt (“translate heading text, not only body”).

## Ranking (this packet + th-TH only)

1. **gpt-5.6-luna-codex** — preferred default for Thai site prose on this sample  
2. **deepseek-v4-pro** / **glm-5-2-zai** — tie; good volume alternatives  
3. **grok-4.5** — not preferred for th-TH without prompt hardening  
4. **kimi-k2p7-code-fireworks** — unavailable this run  

## Do not over-generalize

- One page, one language. Arabic/Chinese/Hindi may reorder this list.  
- Volume cost: if luna is expensive, deepseek/glm are acceptable with review.  
- Next: either (a) expand packet to 3–5 pages with luna vs deepseek, or (b) same packet for a second target (e.g. `zh-Hans`).

## Exclusions going forward

- **Do not schedule `kimi-k2p7-code-fireworks`** until Fireworks path is confirmed healthy.
