# Factory ledger — multilingual site

**Goal:** `docs/factory/multilingual-site/GOAL.md`  
**Authority:** `CONTENT-PLAN.md` Decision 18 (18a–18e); Stages 6–7 of site-implementation campaign  
**Repo:** `faberlang.dev` (this tree)  
**Started:** 2026-07-20

## Vision readiness

| Field | Status |
|---|---|
| Goal boundary | Clear — portal-at-root + LLM-assisted prose sync; pilot `th-TH` current slice |
| Non-goals | Explicit — no build-time translation, no overlays, no new locales, no emit fix |
| Ground truth | Researched in GOAL.md against generator + slices |
| Invariants | Decision 2/8/14/17/18; generator minimal; code via `faber emit` only |
| Acceptance | Listed in GOAL.md |
| Stop conditions | Listed; no production deploy without operator auth |
| Verdict | **READY** — proceed to production |

## Production units (from GOAL phases)

| ID | Unit | Status | Delivery spec |
|---|---|---|---|
| U1 | URL migration + dual locale + `locales.toml` | **done** | `PHASE-1-URL-MIGRATION.md` |
| U2 | Locale-less portal generator at `/` | **next** | — |
| U3 | Provenance + `sync-report` oracle | pending | — |
| U4 | Chrome catalog (`locales/{locale}/chrome.toml`) | pending | — |
| U5 | `sync-translate` LLM differential | pending | — |
| U6 | Pilot locale `th-TH` (`index` + `start/*`) | pending | — |

## Repo boundaries

- **In scope:** `faberlang.dev` only (`generator/`, `src/`, `dist/`, `docs/factory/multilingual-site/`)
- **Out of scope this run:** radix emit comment-stripping; new reader packs; agent surfaces localization
- **Release:** Phase 1 is deploy-sensitive; commit + regenerate `dist/` OK on branch/main tip; **do not push/deploy** without operator authorization

## Completed units

### U1 — URL migration (2026-07-20)

- `generator/locales.toml` + `locales_registry.py`
- Dual locale: `Pagina.site_locale` / `reader_locale`; `link_prefix.fab`
- Content under `dist/{locale}/`; English at `/en-US/`
- 359 meta-refresh stubs for retired root English paths; `/` → `/en-US/` interim
- Gates green: link check (en-US + stubs), leakage, sitemap, canonical
- `build-site.sh` full build: 2626 HTML pages

## Deferred findings

- Partial non-en locales still have chrome links to missing section paths
  (`/th-TH/features/` etc.). Link gate excludes non-en by default until
  fallback materialization or full coverage. Phase 2 portal may surface
  coverage; full-section fallback is follow-on.
- `render-corpus-batch.sh` still rebuilds generator per locale (slow). Optimize later.
- Author-mode emit comment stripping still open (GOAL open question).

## Commits this factory run

_(filled at closeout)_
