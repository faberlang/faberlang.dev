# Production W5 — references/** + history/** + 404 · all locales

**Jobs:** 42 (7 pages × 6 locales)  
**Concurrency:** 8 headless Grok CLI · medium  
**Models:** preferred per PREFERRED-MODELS.md  

| Locale | Applied | Notes |
|---|---|---|
| th-TH | 7/7 | history/releases needed max-turns + file-write re-run (full 42 H3s) |
| zh-Hans | 7/7 | clean (releases on first successful retry) |
| zh-Hant | 7/7 | clean |
| ar | 7/7 | history/releases via file-write agent (max-turns 15) |
| hi | 7/7 | history/releases full re-run |
| vi | 7/7 | history/releases full re-run |

**Pages:** 404, history/index, history/releases, references/{design-docs,ebnf,index,repositories}

**sync-report:** each locale **`current: 48`** — full en-US matrix complete for all 6 locales.
