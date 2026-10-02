# Unit 5 receipt — By Locale / reader locales (seat …bc9e0, deepseek-flash)

Merged: `c3cd35893` + `be307073f` → main merge `3db2202ce` (2026-10-02).

- `capture-locale-diagnostics.sh` + 8 committed captures (same LEX001 error
  rendered per reader locale) under `generator/locale-captures/`.
- `generate-locale-reference.py`: renders the section from the same pack
  join as `generate-agent-locales.py` (`agent_locales` import). Pages:
  `keywords.md` (full canonical × 8 mapping), one page per locale
  (en/la/ar/hi/th-TH/vi/zh-Hans/zh-Hant), `diagnostics.md`,
  `examples.md` (reads committed locale-tabs cache; never regenerates).
- Hub: `src/en-US/language/reader-locales.md` reworked (URL stable,
  `section` → `locales`), states the mirror-vs-feature distinction.
- All keyword tables are fixed-width blocks in ```text fences — the en
  projection would otherwise rewrite table content (e.g. `nihil`→`none`).
  Verified zero-byte diff through both projection passes.

## Nav entries (By Locale group — suggested label "Reader locales")

- Reader locales → `/language/reader-locales.html` (section `locales`)
- Keyword reference → `/language/locales/keywords.html`
- Locale examples → `/language/locales/examples.html`
- Diagnostics by locale → `/language/locales/diagnostics.html`
- Per-locale pages (en, la, ar, hi, th-TH, vi, zh-Hans, zh-Hant) link from
  the hub, not the sidebar.

Proposed `[sidebar_locales]` chrome tables for all 7 locales supplied in
the seat report (heading/hub/keywords/examples/diagnostics).

## Wiring (parent applies, step 0b, after generate-agent-locales.py)

```bash
    if [ -d "${WORKSPACE_DIR}/radix/locale" ]; then
        "${SCRIPT_DIR}/capture-locale-diagnostics.sh" || echo "  capture skipped"
        "$PYTHON" "${SCRIPT_DIR}/generate-locale-reference.py" \
            --packs "${WORKSPACE_DIR}/radix/locale"
    fi
```

## Residuals

- Same faber-1.10 rebuild block as other seats; rendering verified with the
  prebuilt speculum-gen (needs ABSOLUTE source path — relative panics).
- Pre-existing: `radix check --locale=<non-la>` fails pack validation in
  both checkouts → `src/en-US/localization.md` locale= fences fail
  validate-fences today. Compiler-side; note for radix.
- Tables could become real Markdown tables if `/language/locales/**` is
  later exempted in `project_reader_terms.py`.
- `examples.md` pins locale-tabs cache key `0aca787373d25281`; re-pin if
  the source fence changes.
