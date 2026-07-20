# Delivery: Phase 6 — Pilot locale th-TH (current slice)

## Scope

Translate end-to-end the **current** `th-TH` slice only:

- `src/th-TH/index.md`
- `src/th-TH/start/*` (6 files)

Not the full 48-page en-US tree.

## Done

- All 7 files have Thai prose; honesty banners removed
- Code fences preserved from en-US (validate-fences + visual check)
- Provenance stamped: `prose_hash`, `code_hash`, `source_commit`,
  `translation_kind = "translated"`
- `sync-report --locale th-TH` → **7 current**
- Full `build-site.sh` green; leakage reports 7 translated pages without
  notice; other locales still show honesty notices

## Method

1. `sync-translate --write-prompt` per file
2. Flash LLM draft bodies → `/tmp/th-pilot/*.body.md`
3. Apply + stamp; fix residual English headings/table labels
4. Rebuild dist + gates

## Gate

- [x] No fallback honesty banner on pilot HTML pages
- [x] Thai prose present in index + start/*
- [x] sync-report all current for th-TH slice
- [x] build-site green
