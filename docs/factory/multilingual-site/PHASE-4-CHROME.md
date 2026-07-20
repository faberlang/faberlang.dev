# Delivery: Phase 4 — Chrome catalog

## Goal

Localize the ~32 user-visible chrome strings in `html.fab` via
`generator/locales/{locale}/chrome.toml`. Gate: one locale sidebar shows
localized labels.

## Approach

1. Catalog files: flat TOML key = value for en-US (identity) and th-TH (draft Thai).
2. Injection: `inject-chrome.py` post-processes rendered HTML under
   `dist/{locale}/`, replacing English string values with catalog values for
   that locale. Paths/technical ids left untranslated.
3. Wire after locale render in `build-site.sh` (or once over dist before gates).

Cleaner long-term: thread chrome map into Faber generator. Phase 4 uses
post-process so chrome ships without expanding the Faber CLI surface mid-flight.

## Gate

Build with th-TH chrome applied; `dist/th-TH/index.html` contains Thai nav
label e.g. `เริ่มต้นใช้งาน` and not only English "Get started".

## Acceptance (2026-07-20)

### Delivered

| Artifact | Path |
|---|---|
| en-US chrome catalog | `generator/locales/en-US/chrome.toml` |
| th-TH chrome catalog | `generator/locales/th-TH/chrome.toml` |
| Injection script | `generator/scripts/inject-chrome.py` |
| Build wiring | `generator/scripts/build-site.sh` (step 9/10: chrome injection) |

### en-US chrome catalog

Sections: `sidebar_start` (8 keys), `sidebar_docs` (9 keys), `sidebar_agents` (5 keys),
`sidebar_release` (2 keys), `renderbar` (2 keys), `brand` (1 key), `agent_notice` (3 keys),
`side_meta` (4 keys), `footer` (1 key). Total: 35 keys.

All values are plain text (not HTML-escaped). The inject script uses
`html.escape()` at runtime to match rendered HTML entities (e.g. `&` → `&amp;`).

### th-TH chrome catalog

All 35 keys translated to Thai. Technical strings left untranslated:
- `macOS arm64`, `Linux x64`, `MIT` — already hardcoded in `html.fab`, not chrome keys
- Version number `1.1.1` — part of release section heading, not a chrome key

Required gate strings verified:
- `sidebar_start.heading` → `เริ่มต้นใช้งาน`
- `sidebar_start.install` → `ติดตั้งและดาวน์โหลด`
- `sidebar_docs.heading` → `เอกสารประกอบ`
- `sidebar_docs.overview` → `ภาพรวม`
- `sidebar_docs.syntax` → `ไวยากรณ์`
- `renderbar.install` → `ติดตั้ง`
- `brand.tagline` → `เอกสารภาษา`

### inject-chrome.py design

- Uses Python 3.11+ `tomllib` (stdlib) for TOML parsing
- Flattens TOML sections into dotted-key format (`sidebar_start.heading`)
- Loads both en-US and locale chrome catalogs
- Builds replacement map only where values differ between en-US and locale
- HTML-escapes both search and replacement values for matching against rendered HTML
- Sorts replacements by search string length descending (longest first) to prevent
  partial clobber (e.g. `Install` inside `Install &amp; download`)
- Walks `dist/{locale}/**/*.html` applying replacements per file
- Reports file and replacement counts

### build-site.sh wiring

Added chrome injection after post-processing (`strip-empty-sources` + `inject-skip-link`)
and before gates. Iterates all locale directories; runs `inject-chrome.py` only for
locales that have a `generator/locales/{site}/chrome.toml`.

### Edge cases

| Case | Behavior |
|---|---|
| No chrome.toml for locale | Skipped with info message; en-US is no-op |
| Key in en-US but not in locale | Skipped (no replacement) |
| Same value en-US ↔ locale | Skipped (no replacement needed) |
| HTML entity in string (`&`) | Handled via `html.escape()` |
| Substring collision | Longest search strings replaced first |
| Locale dir missing | Skipped with info message |

### Files changed

1. `generator/locales/en-US/chrome.toml` (created)
2. `generator/locales/th-TH/chrome.toml` (created)
3. `generator/scripts/inject-chrome.py` (created)
4. `generator/scripts/build-site.sh` (modified — wire chrome injection)

No HTML files or `html.fab` edited. Chrome injection is pure post-process.
