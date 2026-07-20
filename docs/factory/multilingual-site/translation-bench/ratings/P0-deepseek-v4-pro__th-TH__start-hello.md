# P0 rating — deepseek-v4-pro · th-TH · start/hello

| Field | Value |
|---|---|
| Phase | P0 method proof |
| Model | `deepseek-v4-pro` |
| Target | `th-TH` |
| Packet | `start/hello.md` (blind; gold not in prompt) |
| Subagent | `019f8050-1656-7600-99e7-933c08c75e62` |
| Duration | ~26s |
| Gold | pilot `src/th-TH/start/hello.md` |

## Hard-fail checks

| Check | Result |
|---|---|
| All `<<<FENCE 0..3>>>` present | **PASS** |
| Anchors unchanged | **PASS** (`{#prerequisites}` … `{#next}`) |
| No frontmatter / no preamble | **PASS** |
| Table shape | **PASS** (2-col source table + next nav) |
| Latin Faber tokens in Source column | **PASS** |

## Rubric (1–5)

| Axis | Score | Notes |
|---|---|---|
| Fidelity | **4** | Same structure and meaning. Slight wording drift vs gold (e.g. “เล็กที่สุดแต่ใช้งานได้จริง” vs pilot “เล็กและมีประโยชน์ที่สุด”). Link label choices differ but paths intact. |
| Code integrity | **5** | All fence markers exact; no fence body leakage. |
| Naturalness | **4** | Fluent Thai tech prose. Parenthetical English glosses for lexing/parsing/type checking are helpful for Thai devs. |
| Terminology | **4** | Good consistency. “โลแคล” for locale is calque-y vs pilot “reader locale” handling; still readable. Keeps `faber`, PATH, diagnostic concept. |
| Register | **4** | Direct instructional voice matches site. |

**Weighted overall (equal weights): 4.2 / 5**

## Gold comparison (spot)

| Spot | Pilot gold | Model |
|---|---|---|
| Lead | เขียนโปรแกรม Faber ที่เล็กและมีประโยชน์ที่สุด… | เขียนโปรแกรม Faber ที่เล็กที่สุดแต่ใช้งานได้จริง… |
| Prerequisites heading | ข้อกำหนดเบื้องต้น | same |
| Check section | ผสม English tech terms lightly | more explicit Thai+English glosses for compiler stages |
| Locale section title | หลักฐาน reader locale | ข้อพิสูจน์ด้านโลแคล (weaker term choice) |

Neither is “wrong”; pilot reads slightly more polished / site-native.

## Method proof verdict

**SUCCESS.** Pipeline works:

1. Packet + `sync-translate` prompt shape  
2. Blind prompt (no gold contamination)  
3. Subagent with explicit model slug  
4. Structured output + rubric rating  

Ready for **P1 model sweep** (same packet + target, multiple models).

## Issues to fix before P1

1. **Pack `[llm]` snippet** says “Emit Thai reader-locale Faber keywords” — confuses prose jobs. P1 prompt should keep the clarifying note (or a prose-only system block).
2. Optional: score **terminology** against a small glossary (Install, Reader locale, diagnostic) for inter-rater stability.
