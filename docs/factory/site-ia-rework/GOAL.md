# GOAL: site-ia-rework — task-oriented human navigation for faberlang.dev

**Status**: active — wave 1 dispatched 2026-10-02, six seats in flight (units 1–5)
**Created**: 2026-10-02
**Campaign:** `—`
**Source:** operator design session 2026-10-02 (sidebar IA, corpus reference model); follow-on to `site-implementation`
**Repos:** `faberlang.dev`
**Related:** `docs/factory/site-implementation/CAMPAIGN.md` (predecessor campaign), `radix/docs/factory/english-first-core/` (reader-default context)

---

## Invariant

A first-time human visitor can form an accurate picture of what Faber is —
look, capabilities, outputs — within a few clicks from any docs page, using a
sidebar organized by reader task; and every language term is reachable through
two orthogonal paths (concept tree and A–Z index) without relying on search.

## Problem

Observable in the repo and the rendered site (checked 2026-10-02):

- **Sidebar is production-shaped, flat, and duplicative.** `genera_sidebar` in
  `generator/src/html.fab` emits ~40 links in 7 flat groups organized by how
  the docs are produced (Language / Toolchain / Libraries / Reference) plus a
  grab-bag top block. "Target lanes" appears twice (top block and Toolchain).
  No nesting exists anywhere in the nav engine.
- **Grammar is unnavigable.** One generated page:
  `dist/en-US/reference/grammar.html` (1,434 rendered lines from a
  2,788-line Markdown source).
- **Corpus hub is two flat dumps.** `dist/en-US/corpus/index.html` lists
  "Categories" (~100 mechanical tag pages — `category/ad.html`,
  `category/aliasing.html`, …) and "Terms" as single long lists. The category
  layer recreates the flat-list problem one level down; a reader who knows the
  word (`match`) has no concept path to it.
- **Latin code on English pages.** `dist/en-US/corpus/match.html` carries an
  English title/slug but Latin `discerne` in the exempla code body. Reader
  projection covers slug, title, and prose spans; exempla code blocks render
  straight from the canonical Latin sources in `radix/corpus/`.
- **Targets are scattered.** Three surfaces: `targets/` (12 generated lane
  pages), `toolchain/target-matrix.html`, `toolchain/compiling.html`.
- **Version surfaces are stale.** Sidebar pins faber 1.6.0; release pages stop
  at faber 1.8.0 / radix 0.83.0. Operator states the compiler is at 1.11.0
  (2026-10-02).

## Proposal

Restructure the human site into five task buckets, in this sidebar order:

1. **The Language** — Overview, Behavior, Grammar (one link, large nested
   tree), Examples (light), Installation. The anchor bucket; the first few
   links are where a new human clicks to learn what the language is.
2. **By Target** — HIR (Rust, TypeScript, Go, …), MIR (Runner, LLVM, …),
   GPU (Metal). Full per-target feature tables plus captured panels of Faber
   compiled to that target. The grouping mirrors the compiler's real lowering
   families.
3. **By Locale** — the reader-locale feature tour: full keyword-mapping
   tables (one row per canonical key across all 8 packs), per-locale
   diagnostics examples, locale-tab example panels. Distinct from the
   `/{locale}/` translation mirrors, and labeled so the distinction reads
   ("Reader locales").
4. **Libraries** — Norma, Gradus, Triga, Tela, Inferentia, corpus. Already
   this shape; carries over.
5. **Releases** — per-platform download matrix (from release manifests) plus
   the per-version changelogs; refreshed through current faber.

Supporting decisions from the design session:

- **Overview reuses the landing panels.** The Overview page lives in the
  Markdown pipeline and inlines the captured panels from `generator/landing/`
  (`capture-landing-panels.sh` output), so landing and docs home stay in sync.
  Landing = the claim; Overview = the claim plus the shape of everything.
- **Behavior is authored, curated from existing material:** the `features/`
  essays (commandments, canonical-vs-sugar, frames, Latin-and-glyphs,
  reader-locale, compilation-lanes), `language/glyphs`, `reference/design`,
  and sibling design docs. The spine: glyph law (arrows are runtime, `=`/`:`
  are compile-time), type-first declarations, store-only numeric widths,
  sealed locale surfaces, packages-as-paradigm, mechanical focus.
- **Grammar tree is EBNF-derived.** Productions grouped into families
  (lexing, declarations, statements, expressions, types, …) from
  `faber/docs/EBNF.md` + `grammar/grammar.jsonl`, one drill-down page per
  family or production. Term pages come from the `faber explain` registry —
  the same source that already generates the agent reference tree.
- **Corpus is the term-reference layer, keyed to the grammar spine.** One
  term = one page (already true, 430 pages + alias redirects). Standard
  reference anatomy per page: breadcrumb (Reference › category › term),
  one-sentence semantics, exemplum with real output, related terms. Two
  orthogonal paths: curated concept tree + flat A–Z index. The ~100
  mechanical tag categories collapse into a small curated taxonomy
  (~5–9 buckets) via a mapping in corpus frontmatter. Search stays as the
  third path (alias-aware: `discerne` and `match` resolve to one page).
- **Exemplar code renders in the page's reader locale.** The
  `faber format --locale` transcode already powers locale-tabs panels; wire it
  into `render-corpus-batch.sh`. `.expected` outputs captured under the Latin
  locale need per-locale re-capture where diagnostics text appears.
- **Nav engine becomes a tree.** Hierarchical renderer in `html.fab`
  (replacing flat `nav_list` calls), active-path expansion, per-locale labels
  in `generator/locales/*/chrome.toml`, styles in the single stylesheet.
  Collapse via `<details>/<summary>` so no-JS pages stay fully navigable.
- **Moved URLs get meta-refresh stubs** (existing pattern for retired root
  paths), then sitemap/canonical regeneration and the link/leakage gates.
- **Honest target list.** No CUDA or Swift pages until lanes exist: today's
  lanes are rust, ts, go, llvm-text, metal-text, wasm-text, wgsl-text,
  runner, plus hir/mir/gpu overview lanes.

### Non-goals

- Agent surfaces stay untouched: `static/agents/`, `/llms.txt`,
  `/.well-known/` keep their locale-less contract and are never merged into
  the human IA.
- The landing page generator (`generate-landing.py`) is not rebuilt; Overview
  consumes its captured panels.
- No new JavaScript beyond the existing progressive enhancers; tree collapse
  is CSS/native semantics only.
- Full translation of the six partial locale mirrors is out of scope; their
  structure follows en-US, prose may lag.
- No new target lane pages (CUDA, Swift) until the compiler ships them.

## Units (lowering sketch — refine via `$delivery`)

| Unit | Scope | Depends on | Hand evidence |
| --- | --- | --- | --- |
| 0 | Baseline tag `site-v1.6.0` on pre-rework HEAD | — | done at goal creation |
| 1 | Tree nav engine: hierarchical renderer in `html.fab`, active-path, chrome.toml labels (7 locales), CSS, no-JS collapse | 0 | none |
| 2 | The Language bucket: Overview (panel include step in `build-site.sh`), Behavior slice (curated from `features/`), Grammar single-link, light Examples, Installation; redirects for moved pages | 1 | none |
| 3 | Reference spine: grammar-tree emitter (EBNF families), curated category map, term-page anatomy (breadcrumb + one-sentence semantics), A–Z index, exempla transcode in `render-corpus-batch.sh` (+ expected-output capture) | 1 | none |
| 4 | By Target: consolidate `targets/` + target-matrix under HIR/MIR/GPU, captured `faber emit` panels per target, releases refresh through faber 1.11.0 + sidebar pin update | 1 | none |
| 5 | By Locale: human keyword tables from the pack join (same join as `generate-agent-locales.py`), per-locale diagnostics captures, examples from locale-tabs cache | 1 | none |
| 6 | Migration closeout: redirect audit for every moved URL, locale mirrors adopt the new IA, full re-render, all gates green, search indexes regenerated | 2, 3, 4, 5 | none |

Units 2–5 are parallelizable after 1. Each stage ships a complete site.

## Validation

- `bash generator/scripts/build-site.sh` — full render + fail-closed gates
  (internal links, leakage, sitemap, canonical).
- `generator/scripts/validate-fences.sh src/en-US` after any fence edit.
- Redirect coverage: every pre-rework URL in `dist/` at tag `site-v1.6.0`
  either still resolves or carries a meta-refresh stub (scriptable diff of
  URL sets old vs new).
- Corpus locale check: `dist/en-US/corpus/match.html` code body shows reader
  spelling (`match`), `dist/la`-canonical exempla unaffected on Latin surfaces.
- Browser verification per repo rule: exercise the tree nav collapsed and
  expanded, no-JS, desktop + mobile widths, on Grammar tree, corpus term, and
  By Target pages.

## Delivery checklist

| Check | Enforced by |
| --- | --- |
| Faber fences still pass radix check | `validate-fences.sh` |
| Locale-tab panels regenerated after cheat-sheet/examples fence edits | `locale-tabs.py render` + committed cache |
| Diagrams regenerated after mermaid edits | `diagrams.py render` + committed cache |
| No inline styles; all CSS in `generator/www/speculum.css` | review |
| Every moved URL has a redirect stub | link gate + URL-set diff |
| `dist/` committed with sources on each landing push | deploy workflow |

## Ledger

| Unit | Status | Seat | Receipt | Notes |
| --- | --- | --- | --- | --- |
| 0 — baseline tag | done | — | tag `site-v1.6.0` | 2026-10-02 |
| 1 — tree nav engine | in flight | seat …bd47b (zai-glm-5.3-flash) | — | prerequisite for all buckets |
| 2 — The Language | in flight | seat …c8d2b (deepseek-flash) | — | respawned off dead qwen slug |
| 3a — grammar tree | in flight | seat …586c (deepseek-flash) | — | split from 3; respawned off qwen |
| 3b — corpus reference | in flight | seat …e1b5 (zai-glm-5.3-flash) | — | taxonomy + anatomy + transcode |
| 4 — By Target | in flight | seat …a3e39 (deepseek-flash) | — | incl. releases refresh to 1.11.0 |
| 5 — By Locale | in flight | seat …bc9e0 (deepseek-flash) | — | respawned off dead qwen slug |
| 6 — migration closeout | pending | — | — | gates + redirects last; injector parent-owned |

## Open questions

1. **Cheat sheet placement** — default: quick link inside The Language bucket.
2. **Locale mirror timing** — default: mirrors adopt the new IA (paths move
   with the same mapping, redirects for all) in unit 6 rather than lagging on
   the old shape; revisit if translation load says otherwise.
3. **Redirect retirement** — default: meta-refresh stubs stay indefinitely
   (static and cheap). Revisit if maintenance cost appears.
4. **`faber explain` registry as term-page source** — default: human term
   pages render from the same registry that feeds the agent reference tree;
   corpus exempla stay the example layer. Confirm shape in unit 3 lowering.
