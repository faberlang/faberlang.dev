# Goal: Multilingual site — portal at root + LLM-assisted prose sync

## Summary

Make faberlang.dev genuinely multilingual: a locale-less language portal at `/`,
English content relocated to `/en-US/`, and an LLM-assisted differential pipeline
that keeps per-locale prose translations synchronized with the English source.
Translation is always a separate, human-reviewed, on-demand step — never
generator-time. Code fences auto-transcode through the reader pack; prose
provenance is tracked by content hash so drift is visible, not silent.

Authority: `CONTENT-PLAN.md` Decision 18 (18a–18e). Completes Stages 6 (portal)
and 7 (multilingual) of `docs/factory/site-implementation/CAMPAIGN.md`.

## Problem

- The site's reason to exist is that readers should use Faber in their own
  language, but the website itself only offers English prose. Today's locale
  slices are fallback copies — English prose + transcoded code + an honesty
  banner. The multilingual philosophy stops at the code.
- `/` renders the English homepage. There is no language chooser, so the
  thesis is invisible on arrival.
- Prose provenance (`source_hash`) exists in frontmatter but is already stale
  and its hashing basis is undocumented: none of full-file / body / prose
  SHA-256 of the current `src/en-US/index.md` matches the value recorded in the
  locale slices. English has drifted from every locale slice with nothing
  noticing. There is no operated sync; the 3-step bootstrap in `CONTENT-PLAN.md`
  describes a one-shot fork, not the recurring merge multilingual sites need.

## Goals

- A locale-less language portal at `/` (Decision 16), generated from the locale
  directory list, each language shown in its own script with a code sample.
- English content relocated under `/en-US/`; retired root URLs redirect via
  `<meta http-equiv="refresh">` stubs so inbound links do not 404.
- A per-locale prose storage and sync model: full-file-per-locale, two-hash
  provenance (`prose_hash` + `code_hash` + `source_commit`), LLM-assisted
  differential re-translation fenced from code (Decision 18).
- A `sync-report` oracle that flags stale locale pages, and a `sync-translate`
  step that drafts LLM updates for human review.
- One pilot locale (`th-TH`) — its **current** slice (`index` + `start/*`, the 7
  files that exist today) — fully translated end-to-end to prove the loop closes.
  Mirroring `th-TH` across all 48 `en-US` pages is follow-on scale work, not the
  pilot.
- Chrome/nav strings (~32 in `html.fab`) localized via a per-locale catalog.

## Non-goals

- Auto-translating prose at build time (generator-time translation).
  Translation is always a separate, human-reviewed, on-demand step.
- Block-level prose overlays or prose transclusion (rejected in 18c).
- Translating the generated corpus term pages' prose. They are canonical Latin
  by construction; only their code fences localize, which already works.
- Localizing the agent surfaces (`/llms.txt`, `/agents/`). Separate concern.
- Adding locales beyond the six already shipped
  (`th-TH`, `zh-Hans`, `zh-Hant`, `vi`, `ar`, `hi`).
- Solving the `faber emit` canonical-path comment-stripping limitation. It is
  an open question, not a goal; documented or worked around, not fixed here.

## Ground Truth Researched

- `generator/src/html.fab`: all page chrome generated here; ~32 hardcoded
  English nav/meta strings; `<html lang=pag.locale>` uses a single locale value
  for both lang attribute and transcode.
- `generator/src/markdown.fab`: minimal block parser (h2/h3, paragraphs, pipe
  tables, flat `ul`, fences, inline code/bold/italic/links). No directives or
  transclusion yet.
- `generator/src/types.fab`: `Pagina` carries one `locale` field used for both
  lang and transcode — must split into site-locale + reader-locale.
- `generator/scripts/build-site.sh`: locale fan-out by directory presence;
  en-US renders to root with `locale=la`; others to `dist/{locale}/`. Smoke
  checks assert English-at-root paths.
- `generator/scripts/localize-markdown.py`: code-fence transcode via
  `faber emit --reader-locale`; fluid fences only; pinned/reject left authored.
- `generator/scripts/check-leakage-gate.py`: honesty gate; locale pages must
  carry a "Translation status" notice unless redirected.
- `generator/scripts/render-corpus-batch.sh`: holds a hardcoded
  `LOCALE_NAMES` dict (Thai, Simplified Chinese, …) — display metadata that
  belongs in the locale registry.
- `src/th-TH/index.md` vs `src/en-US/index.md`: locale file = en-US copy +
  `translation_kind`/`source_locale`/`source_hash` frontmatter + honesty
  banner; body prose identical English.
- `CONTENT-PLAN.md` Decisions 2, 8, 15, 16 + "Multilingual pipeline" § +
  "Correction: step 1 is a fork": single content-hash provenance already
  described; portal at `/` already designed but unbuilt; the `[llm]` pack
  prompt is already written and must be reused.
- Measurement: 48 en-US files, ~17,491 prose words (manual surface), ~3,657
  code-fence words (free, auto-transcoded), ~32 chrome strings.
- Hosting: GitHub Pages, bare `dist/` artifact upload, no `_redirects`;
  corpus alias pages already use `<meta http-equiv="refresh">`.
- Conversation (this session): portal-at-root accepted as the active path;
  English segment = `en-US` with code pack `la` (Latin is canonical);
  "manual" = LLM-assisted differential, human-reviewed, fenced from code.

## Reference Packet

Before editing, inspect:

- `CONTENT-PLAN.md` Decision 18 (this goal's authority) + Decisions 2/8/15/16:
  the architecture this must obey.
- `docs/factory/site-implementation/CAMPAIGN.md` Stages 6 and 7: what this
  completes and the residuals already recorded.
- `generator/src/html.fab`: chrome generation, the ~32 strings, the
  single-locale threading that must split.
- `generator/scripts/build-site.sh`: locale fan-out and smoke checks that
  assume English-at-root.
- `generator/scripts/{localize-markdown,check-leakage-gate,inject-canonical,generate-sitemap}.py`:
  the migration blast radius.
- `faber emit --reader-locale=<X>`: the code transcode seam; verify the
  canonical-path comment-stripping behavior.
- `examples/reader-locale/*/pack.toml`: the `[llm]` prompt, `inherits`, and
  `fallback` semantics the sync step must reuse.

## Constraints And Invariants

- The generator stays minimal (Decision 17): no render-time prose merging. All
  sync intelligence lives in separate, human-run tooling.
- Code fences always regenerate from `en-US` via `faber emit`; the LLM never
  touches code (Decision 8).
- Stable Latin slugs (Decision 2): paths are locale-invariant; only prose
  translates; `title` is free prose, never slugified.
- The generator cannot write CSS (Decision 14); one stylesheet.
- Prose translation is never build-time or automatic. Drift must stay visible
  (Decision 8): the oracle reports, the human commits; no silent regeneration.
- Shared-workspace rules: LLM drafts land on a branch/worktree, never dirtying
  the main checkout uncontrolled.
- The Faber Markdown comment rule (`#` only, own line) and fence validation
  (`validate-fences.sh`) hold for every locale file.
- Never merge to main without a deploy workflow (repo rule); the URL migration
  deploys in one push with redirect stubs.

## Architecture Direction

- **Portal at `/`** is locale-less and generated from the locale registry; it
  is not translated into a language, it renders all of them at once
  (Decision 16). Each entry shows the language in its own script plus a code
  sample drawn from the pack's `[llm] exemplars`.
- **URL scheme** is `/{locale}/...` for all content including English
  (`/en-US/...`). Retired root URLs redirect via meta-refresh stubs.
- **Two locale values per locale**, threaded through the build: `site_locale`
  (dir name → URL segment, `<html lang>`) and `reader_locale` (pack id →
  `faber emit`). They coincide everywhere except English
  (`en-US` prose + `la` code).
- **One locale registry** (`locales.toml`) maps each dir to its reader-locale
  override, its native display name and script, and status. Locale discovery
  stays dir-presence; the registry enriches it. It replaces the hardcoded
  `LOCALE_NAMES` dict in `render-corpus-batch.sh` and feeds the portal.
- **Prose storage** is full-file-per-locale. No overlays, no prose transclusion.
- **Provenance** is `prose_hash` + `code_hash` + `source_commit` per locale
  file, recorded in frontmatter.
- **Sync is two tools, not a build step**: `sync-report` (staleness oracle) and
  `sync-translate` (LLM differential draft). Neither runs at render time.

## Supporting Skills

- `delivery`: lower each implementation phase into a repo-aware spec before
  factory.
- `factory`: execute the phases (migration, portal, oracle, sync-translate,
  catalog).
- `consequences`: trace the URL-migration blast radius before executing it.
- `clean-break`: the URL migration is one-direction, no compat shim.
- `correctness` / `auditor`: review the sync-translate LLM boundary
  (code-fence isolation, structure preservation) before relying on it.
- `housekeeping`: keep `dist/` and gates consistent after the migration.

## Implementation Shape

- **Phase 1 — URL migration to portal-at-root (clean break):** relocate
  en-US to `/en-US/`; update internal links, `html.fab` hrefs, smoke checks,
  canonical/sitemap/leakage scripts; add redirect stubs; thread site-locale +
  reader-locale through the build; introduce `locales.toml`. Fixes
  `<html lang>`.
  *Gate:* full build + link check + leakage gate green; old URLs redirect.
- **Phase 2 — Portal generator:** locale-less `/` from the registry + each
  pack's code sample.
  *Gate:* portal lists all locales in their scripts; `/` no longer renders the
  English homepage.
- **Phase 3 — Provenance + oracle:** implement `prose_hash`/`code_hash`/
  `source_commit`; build `sync-report`.
  *Gate:* oracle reports the already-stale slices; zero false positives on
  example-only edits.
- **Phase 4 — Chrome catalog:** `locales/{locale}/chrome.toml` + `html.fab`
  lookup (a new generator input).
  *Gate:* one locale's sidebar renders localized.
- **Phase 5 — sync-translate (LLM differential):** fenced from code,
  structure-preserving, branch-based, human-reviewed; reuses the pack `[llm]`
  prompt.
  *Gate:* one stale file re-translated, reviewed, committed, staleness cleared,
  gates green.
- **Phase 6 — Pilot locale:** fully translate `th-TH`'s current slice
  (`index` + `start/*`) end-to-end. Not all 48 `en-US` pages — the pilot proves
  the loop, not the coverage.
  *Gate:* no English prose remains in the translated `th-TH/` files; honesty
  banner dropped for those pages, present for any untranslated ones; code fences
  locale-correct.

## Release Posture

Decision: release checkpoint required.

- The URL migration is a breaking change to a live site (faberlang.dev). It
  ships with redirect stubs so inbound links do not 404, and the deploy
  workflow publishes `dist/` with the new structure in one push.
- Operator authorization required for the deploy/push (repo rule: never merge
  to main without a deploy workflow).
- Record the migration in release notes / `dist/reports/`.

## Exit Strategy

Decision: included.

- Rollback = revert the migration commit and redeploy `dist/` at the prior tip.
  Redirect stubs make the URL change reversible without breaking inbound links
  during the rollback window.
- The sync tooling is additive; removing it leaves locale files as static
  copies (degraded but functional, matching today's state).
- If the LLM differential step proves unreliable, fall back to manual
  translation of flagged files. The oracle still works as a staleness report
  without the drafting step.

## Acceptance Criteria

- `/` renders a locale-less language portal; English content lives at
  `/en-US/`; retired root URLs redirect (no 404 on existing inbound paths).
- `<html lang>` reflects the prose language for every locale (English pages no
  longer `lang="la"`); reader-locale `la` still drives code transcoding on
  English pages.
- `sync-report` flags stale locale pages against current `en-US`, with zero
  false positives on example-only edits; it reports the already-stale slices as
  evidence.
- `sync-translate` produces a reviewed, committed locale-file update with code
  fences untouched by the LLM and all structure (`{#anchor}`, paths, table
  shapes) preserved; provenance bumped to current `en-US`.
- The pilot locale (`th-TH`) has no fallback English prose in its current slice
  (`index` + `start/*`); the honesty banner is absent for those translated pages
  and present for any untranslated ones.
- Full build (`build-site.sh`) is green: link check, leakage gate, fence
  validation, sitemap, canonical all pass.

## Validation

- `bash generator/scripts/build-site.sh` → green; smoke checks pass under the
  new `/en-US/` paths.
- `generator/scripts/check-internal-links.py dist` → 0 broken links, including
  redirect stubs resolving.
- `generator/scripts/check-leakage-gate.py dist` → PASS (notices present where
  required, absent where translated).
- `generator/scripts/validate-fences.sh src/th-TH` → passes for the pilot
  locale.
- Manual: visit `/` → see language chooser; pick Thai → Thai prose + Thai-keyword
  code; old URL `/start/install.html` → redirects to
  `/en-US/start/install.html`.
- Oracle: run `sync-report` → it lists `th-TH/index.md` (and others) as stale
  against current `en-US` (reproduces the drift found in research).

## Open Questions

- Does `faber emit --reader-locale` strip comments in fluid fences (the
  canonical-path limitation documented in `CONTENT-PLAN.md`)? If `en-US`
  teaching examples carry comments, they vanish in non-`la` locales. Must be
  resolved or documented before Phase 6. Not blocking Phases 1–5.
- Should the portal show per-locale coverage (e.g. "Thai: 7/48 pages
  translated")? Useful for honesty but couples the portal to the oracle. Defer;
  decide at Phase 2.

## Stop Conditions

- Stop if the URL migration cannot preserve inbound links (the redirect
  mechanism fails on GitHub Pages) — re-evaluate before deploying.
- Stop if `faber emit --reader-locale` cannot be relied on for code fences in a
  locale (compiler gap) — code localization is a prerequisite for prose
  localization of that locale.
- Stop if the LLM differential step cannot be reliably fenced from code or
  cannot preserve structure — fall back to manual translation and keep the
  oracle as a report only.
- Stop before any production deploy/push without operator authorization.
