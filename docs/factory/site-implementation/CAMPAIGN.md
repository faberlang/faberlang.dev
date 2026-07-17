# Campaign: faberlang.dev Site Implementation

**Created**: 2026-07-16
**Repo**: `/Users/ianzepp/work/faberlang/faberlang.dev`
**Authority**: `CONTENT-PLAN.md` (architecture), `docs/factory/speculum-multilingual-site/goal.md` (Speculum goal)
**Posture**: Draft/maintain — this artifact routes stages; it does not implement code

## Summary

Build the faberlang.dev documentation site generator: a build system that turns
Markdown sources + corpus frontmatter into a correct, verified, multilingual
static site. The content plan has already settled all architectural decisions;
the campaign implements the framework, proves it at n=1, scales it to all
authored pages, then adds the generated corpus path.

## Problem

The repo has 23 drafted Markdown pages and 18 HTML pages (content reference
only), but no build system connects them into a site. The first attempt (18
hand-built HTML pages) failed architecturally: every page forked the design
system, no two `:root` blocks were identical, and class names were
presentational single letters redefined per file. The content plan diagnosed
this as a missing generator, not missing content. The transcode blocking
dependency has shipped (faber 1.1.0 canonical re-emission). The framework is
unblocked and is the next action.

## Desired End State

1. A site generator that consumes Markdown + frontmatter and emits static HTML
   with a closed set of named components and one shared stylesheet.
2. A fence extractor in CI that validates every code block via the `faber` CLI
   (lexes, compiles, rejects, or matches expected output).
3. All 23 existing Markdown pages rendered through the generator with correct
   heading anchors, fence contracts, and inline-span rendering.
4. The 18 HTML pages ported to Markdown (content preserved, markup discarded).
5. A corpus term-page generator that turns `examples/corpus/` frontmatter into
   ~167 canonical term pages per locale.
6. The Speculum Porta as the site entry point.
7. A getting-started/tutorial track with container-verified install
   instructions.
8. Multilingual generation using the shipped canonical transcode.

## Development Posture

- **Clean architecture, not compatibility.** The HTML pages are content
  reference only. Do not carry markup, class names, or inline styles across.
- **One stylesheet.** The design tokens from the homepage `:root` block become
  a single shared CSS file. The generator cannot write CSS.
- **Correctness by construction.** Generated corpus pages are a build target;
  they cannot drift because they are emitted from structured data.
- **CI as the staleness oracle.** The fence extractor is the load-bearing
  contract: when the language moves, examples break, CI flags the page.
- **No browser-time translation.** Transcode happens at generation time,
  materialized into git, so localized code is diffable.

## Implementation Workflow

Campaign stages lower to `delivery` for spec compilation, then `factory` for
implementation. Stages are ordered — each proves a contract the next stage
depends on.

## Scope Routing

| In-campaign | Split out |
|---|---|
| Generator build system, contracts, rendering, corpus generation, portal | Homebrew formula publication (blocks getting-started, not the generator) |
| Markdown annotation passes (anchors, fences) | Radix compiler changes (transcode shipped; further work is separate) |
| HTML→Markdown porting (content extraction) | cista.dev public registry (separate campaign) |

## Batching And Split Policy

| Stage | Posture | Rationale |
|---|---|---|
| Generator foundation | `discovery-first` | One small exploratory phase to pick technology and prove the pipeline, then batch |
| Annotate authored pages | `batch-by-default` | Same annotation contract applied uniformly once proven at n=1 |
| HTML→Markdown port | `batch-by-default` | Same extraction pattern for each page; content differs, process is identical |
| Corpus generation | `split-on-boundary` | Slice 2 (one term page) must prove `kind` handling before batch generation |
| Getting-started | `split-on-boundary` | Install page blocked on Homebrew formula publication |

## Ground Truth Researched

| Source | Authority | Verified |
|---|---|---|
| `CONTENT-PLAN.md` | Architecture decisions, component vocabulary, page inventory, machine contracts | Read in full; updated transcode status to shipped |
| `docs/factory/speculum-multilingual-site/goal.md` (git: 372bb21) | Speculum site goal, 12 goals, non-goals | Read from git history |
| `src/en-US/index.html` | Current homepage; design tokens in `:root`; inline styles; invalid code blocks (`//` comments) | Inspected |
| 23 Markdown files in `src/en-US/` | Content drafted; syntax (11), tooling (3), ecosystem (6), references (3) | Inventoried |
| 18 HTML files in `src/en-US/` | Content reference only; forked design system; single-letter class names | Inventoried |
| `faber emit -t faber --reader-locale=<X>` | Canonical transcode shipped (faber 1.1.0, radix cdafbb901) | Verified from git |
| `examples/corpus/` | 154 directories, 292 `.fab` files, 100% TOML frontmatter, 183 distinct terms, 167 canonical | From CONTENT-PLAN measurements |
| No build system exists | No package.json, Cargo.toml, Makefile, or generator script | Verified by filesystem inspection |

## Current State

| Track | State | Next action |
|---|---|---|
| Generator build system | **Built** — 8 modules, ~800 lines, `faber check` clean, **renders end-to-end** | Close Stage 1 (block-level Markdown conversion = Stage 2) |
| Authored Markdown pages | 23 drafted, unannotated | Blocked on Stage 2 gate |
| HTML pages (content debt) | **Cleared** — 0 HTML files remain; all content in Markdown | Stage 3 gate closed |
| Corpus page generator | **Batch built** — 167 canonical terms, 95 alias redirects, 45 category indexes, corpus hub rendered | Stage 5 residual triage (`tuus` fence, alias data collisions) |
| Portal (Speculum Porta) | Homepage HTML exists, not generated | Blocked on Stage 6 |
| Getting-started | Not started | Blocked on Homebrew formula |
| Multilingual generation | Transcode shipped; no locale sites generated | Blocked on Stage 7 |
| CI / fence extractor | **Built** (`scripts/validate-fences.sh`) — tested on types.md | Part of Stage 1 |

## Campaign Path

### Stage 1 — Generator Foundation and Slice 1

**Status**: ✅ gate closed (2026-07-16) — all deliverables met, 23 pages render
**Source**: `CONTENT-PLAN.md` §§ Core architecture, Machine contracts, Component vocabulary, Order
**Why now**: Everything depends on the generator existing. Slice 1 proves it at n=1.
**Lowers to**: `delivery` → `factory`
**Batching**: `discovery-first`
**Engineering log**: `generator/STAGE-1-LOG.md`

**Built** (2026-07-16):
- Generator technology decided: **Faber** (dogfooding). Eight modules, ~800 lines,
  passing `faber check` with zero errors. **Renders `syntax/types.md` (161 lines)
  in 0.8 seconds.** See Open Question 1 for rationale and learning record.
- `string_util.fab` — string search, split, trim, newline constant
- `frontmatter.fab` — TOML `+++` block parser → `Split{fields, body}`
- `fence.fab` — code fence extractor → `Fence{locale, modus, outcome, source, line}`
- `anchor.fab` — heading extractor with stable anchor IDs
- `types.fab` — core domain model (`Pagina`, `HtmlPagina`, `SiteManifest`)
- `html.fab` — HTML emitter with component vocabulary
- `main.fab` — entry point and path derivation

**Remaining**:
- [x] Inline span renderer (48-identifier keyword/type lookup table) — **built** (`span.fab`)
- [x] Fence validation CI script (shell wrapper calling `faber check`/`radix emit`) — **built** (`scripts/validate-fences.sh`)
- [x] Shared stylesheet extracted from homepage `:root` design tokens — **built** (`www/speculum.css`)
- [x] Wire `incipit` to read `syntax/types.md` and emit rendered HTML — **works** via shell wrapper; renders 161-line page in 0.8s

Deliverables (full list from content plan):
- ~~Generator technology picked~~ — Faber
- ~~Shared stylesheet from homepage `:root` design tokens~~ — **built** (`www/speculum.css`)
- Markdown → HTML pipeline with frontmatter parsing — **built**
- Component vocabulary (closed set from Decision 14) — **built** (html.fab)
- ~~Fence extractor (locale, mode, outcome)~~ — **built** (fence.fab)
- ~~CI script (validate via `faber` CLI)~~ — **built** (`scripts/validate-fences.sh`)
- ~~Heading anchor system (explicit stable IDs)~~ — **built** (anchor.fab)
- ~~Inline span renderer (48-identifier lookup)~~ — **built** (span.fab)
- ~~Render `syntax/types.md` end-to-end~~ — **working** (0.8s via compiled path + shell wrapper)

**Gate**: `syntax/types.md` renders as a complete HTML page with correct
styling, validated fences, stable anchors, and rendered inline spans. The
homepage code block lex bug is caught by the fence extractor.

**Status — 2026-07-16**: **Stage 1 gate closed.** All deliverables met:

- `syntax/types.md` renders as complete HTML: 10 headings with anchor IDs,
  4 tables, 9 code blocks, 10 paragraphs, inline span classification — in
  under 1 second.
- All 9 code fences in types.md pass validation (`radix check`).
- All 23 authored Markdown pages render successfully with zero failures.
- Shared stylesheet (`www/speculum.css`) with all design tokens.
- Block-level Markdown converter (headings, paragraphs, tables, lists, code
  blocks, bold, HTML escaping) — 19 proba tests, all passing.
- Heading anchor system (`{#id}` syntax → `id` attribute, explicit IDs only).
- Fence validation CI script (`scripts/validate-fences.sh`).

**Remaining work** (Stage 2 scope, not Stage 1 blockers):
- Add explicit `{#anchor}` IDs to headings on the other 22 pages
- Annotate fence outcomes (locale/mode/outcome) where not default
- Run fence validator across all 23 pages and fix content bugs

### Stage 2 — Annotate Authored Pages

**Status**: ✅ gate closed (2026-07-16) — all pages annotated, all fences pass
**Source**: `CONTENT-PLAN.md` §§ Machine contracts, Inline code spans, Heading anchors
**Why now**: Stage 1 proved the contracts; now apply them uniformly.
**Lowers to**: `factory`
**Batching**: `batch-by-default`
**Depends on**: Stage 1 gate

Deliverables:
- Add explicit heading anchors to all 107 `##` headings across 23 Markdown files
- Annotate pinned fences with locale (only `reader-locale` page has non-Latin pinned blocks)
- Annotate fence outcomes (compiles / rejects / output-matches) where not default
- Inline spans need no annotation — lookup-based by design
- Render all 23 pages through the generator

**Gate**: All 23 Markdown pages render through the generator with validated
fences and stable anchors. CI passes on all extracted fences.

**Status — 2026-07-16**: **Stage 2 gate closed.**

- **Heading anchors**: All `##` and `###` headings across all 23 pages now
  carry explicit `{#id}` kebab-case anchor IDs (146 total).
- **Fence validation**: 72 code fences across 12 pages, 72 pass / 0 fail.
  Fixed 42 content bugs: `//` comments → `#`, function declarations without
  bodies, undefined variables/types, pseudo-code placeholders.
- **All 23 pages render** successfully through the generator.

### Stage 3 — Port HTML Pages to Markdown

**Status**: ✅ gate closed (2026-07-16) — all HTML deleted, 40 pages live
**Source**: `CONTENT-PLAN.md` § Page inventory (Features, Tooling stubs, Hubs)
**Why now**: Content exists in HTML; it must move to Markdown before the HTML is deleted.
**Lowers to**: `factory`
**Batching**: `batch-by-default`
**Depends on**: Stage 2

Deliverables:
- ~~Port 8 feature pages~~ — 7 feature pages ported (reader-locale,
  compilation-lanes, frames, testing, canonical-vs-sugar, commandments,
  latin-and-glyphs) from HTML to Markdown
- ~~Port 3 tooling stubs~~ — faber-build-tool, radix-compiler,
  cista-package-manager ported with real content
- ~~Write missing hub pages~~ — 6 hub pages written (features/index,
  tooling/index, syntax/index, ecosystem/index, references/index,
  history/index)
- ~~Write homepage Markdown~~ — index.md replaces custom index.html
- ~~Delete all HTML files~~ — 18 HTML files deleted, zero remain
- ~~Render ported pages through the generator~~ — 40/40 pages render, 0 failures
- ~~Deploy pipeline wired~~ — build-site.sh batch render + deploy-pages.yml
  workflow restored; pushed to main; live at faberlang.dev

**Gate**: ~~Zero HTML content files remain. All content renders through the
generator. No inline styles, no per-page `:root` blocks, no forked design
systems.~~ **Closed.** 0 HTML files. 40 pages rendered. One stylesheet.
81/81 fences pass. Site live at https://faberlang.dev.

### Stage 4 — Corpus Term Page Generator (Slice 2)

**Status**: ✅ gate closed (2026-07-16) — bounded proof page and alias bridge render end-to-end
**Source**: `CONTENT-PLAN.md` §§ Generated — Corpus, The corpus is not flat
**Why now**: ~90% of the eventual site goes through this code path. It is the
highest-risk stage and must prove `kind` handling before batch generation.
**Lowers to**: `delivery` → `factory`
**Batching**: `split-on-boundary`
**Depends on**: Stage 1 (generator foundation)

Deliverables:
- [x] Corpus frontmatter reader: parse `examples/corpus/**/*.fab` + `.expected`
  records in `generator/src/corpus.fab`; filesystem traversal stays in the
  shell boundary.
- [x] Term-page template: `summary` → lead, `syntax` → inline syntax,
  `category` → section, `related[]` → cross-links, `.fab` → samples,
  `.expected` → output, and `kind` → fence outcome.
- [x] `kind` policy: canonical examples are page candidates; `legacy`, `smoke`,
  and `existing-home` are not promoted by the bounded selector; explicit
  `reject` examples are supporting samples and render with `outcome=rejects`.
  Other non-canonical examples remain supporting data for the Stage 5 manifest.
- [x] Alias story: aliases on a canonical example emit static HTML bridges
  with a refresh link and `rel=canonical`; the bridge has one canonical
  destination and does not add runtime negotiation.
- [x] Multiple examples per term: the tensor proof carries its canonical
  declaration and an explicit rejecting arithmetic example.
- [ ] Category indexes: `corpus/category/{category}` from frontmatter (Stage 5).
- [x] Render one canonical term page end-to-end as proof (`dist/corpus/tensor.html`).

**Gate**: **Closed.** `tensor` renders with frontmatter-driven content,
multiple examples, rejecting fence handling, and cross-links. The generated
proof Markdown contains two transcluded fences; `validate-fences.sh` reports
2 passed / 0 failed. `functio` additionally proves an alias bridge at
`dist/corpus/function.html`.

### Stage 5 — Corpus Generation at Scale

**Status**: implemented with residuals (2026-07-17) — 348 pages render
**Source**: `CONTENT-PLAN.md` § Generated — Corpus
**Why now**: Stage 4 proved the code path; now generate all pages.
**Lowers to**: `factory`
**Batching**: `batch-by-default`
**Depends on**: Stage 4 gate

Deliverables:
- [x] Generate all 167 canonical term pages
- [x] Generate alias redirects where the alias has a unique static path — 95 redirects generated
- [x] Generate category indexes — 45 category pages generated
- [x] Generate corpus hub page at `/corpus/`
- [x] CI/fence validation run over generated term Markdown; residual filed below

**Gate**: Closed after residual triage (2026-07-17). The site renders 354
HTML pages after Stage 6: 46 authored pages, 167 corpus term pages, 95 alias
redirects, 45 category indexes, and 1 corpus hub. Generated-fence validation for
the focused `tuus` proof now reports 1 passed / 0 failed / 0 skipped; authored
fence validation reports 82 passed / 0 failed / 0 skipped.

**Residual disposition — 2026-07-17**: `/corpus/tuus.html` now compiles in the
standalone fence validator: `examples/corpus/ad/sermo-tuus.fab` uses the
placeholder type `_` for the `ad` conversation binding instead of naming the
compiler-owned `sermo` type directly. `closure` and `lambda` now have one
canonical owner, `clausa`; `clausura` no longer declares those aliases. The only
remaining alias residual is `string`, because it is a canonical term path and
therefore cannot also be emitted as an alias redirect to `textus` without
overwriting the canonical page.


### Publication (corpus campaign milestone)

**Status**: published 2026-07-17 — `origin/main` at `c1dcb68` (Stage 4+5 corpus).
**How**: `git push origin main` → `.github/workflows/deploy-pages.yml` → GitHub Pages (`https://faberlang.dev`).
**Scope published**: authored pages + 167 corpus terms + aliases + category indexes + hub (348 pages total in build).
**Residuals open at publication time**: Stage 5 fence residual (`tuus` / SEM008); Stages 6–8 (portal, multilingual, LLM surface) were still planned and were not required for that publish.

### Stage 6 — Portal and Getting Started

**Status**: implemented with residuals (2026-07-17) — portal + start track render
**Source**: `CONTENT-PLAN.md` §§ Portal, Getting started, Missing sections (O10)
**Why now**: The reference site is complete; add the on-ramp.
**Lowers to**: `delivery` → `factory`
**Batching**: `split-on-boundary`
**Depends on**: Stage 5

Deliverables:
- [x] Speculum Porta: locale-less entry point at `/`, locale ring, honest pack
  status, `salve-munde` living sample across locales. Implemented as generated
  `src/en-US/index.md` content: `/` routes humans to the start track, agents to
  machine surfaces, and marks non-English reader packs as shipped source
  renderings with full localized site generation deferred to Stage 7.
- [x] Getting-started tutorial track: `start/install`, `start/hello`,
  `start/commands`, `start/projects` — sequenced with `next`/`prev` links and
  rendered into `dist/start/*.html`.
- [ ] Container-verified install CI: run quickstart end-to-end in a clean
  container. Residual: Homebrew/package-manager verification is not authoritative
  while formula publication may lag the repo release; install docs explicitly use
  Faber 1.1.1 release archives.
- [x] Onramp banner: homepage → `start/install`, with track links for hello,
  commands, and projects.

**Gate**: Implemented with one exact residual. Portal renders with locale pack
status and a validating `salve-munde` sample. Getting-started track renders and
links through the generated sidebar. Full container-verified install CI remains
open until package-manager/formula publication catches up to the release archive
path documented by the page.

**Validation — 2026-07-17**:
- `bash generator/scripts/validate-fences.sh src/en-US` — 82 passed / 0 failed /
  0 skipped.
- `bash generator/scripts/build-site.sh` — 354 HTML pages, 9 static machine files.
- Build smoke includes `dist/index.html` and `dist/start/install.html`; new pages
  `dist/start/hello.html`, `dist/start/commands.html`, and
  `dist/start/projects.html` render.

### Stage 7 — Multilingual Generation

**Status**: partial multi-locale proof implemented (`th-TH`, `zh-Hans`, `vi`,
`ar`, and `hi` portal/start fallback slices plus generated corpus artifacts);
full Stage 7 remains open.
**Source**: `CONTENT-PLAN.md` §§ Multilingual pipeline, Output reader formatting (shipped)
**Why now**: English site is complete; transcode is shipped.
**Lowers to**: `delivery` → `factory`
**Batching**: `split-on-boundary` (per locale)
**Depends on**: Stage 5, Stage 6

Deliverables:
- [ ] Locale site generation: `src/{locale}/` structure for each of 7 locales
  with full authored-doc coverage.
- [x] Partial proof locales: `th-TH`, `zh-Hans`, `vi`, `ar`, and `hi`
  materialize the portal/start authored slice (`index.md` and `start/*`) plus
  generated corpus/category/alias pages during the build.
- [x] Canonical transcode seam: render fluid example code blocks through
  `faber emit --reader-locale=<X>` at generation time.
- [x] Translation provenance: English source SHA-256 recorded in proof-slice
  frontmatter.
- [x] Fallback: untranslated proof pages fall back to `en-US/` prose with a
  visible banner.
- [ ] LLM prose translation pipeline: use pack `[llm]` section prompts.
- [ ] Complete non-English authored-doc generation for any locale.

**Gate**: One non-English locale (e.g., `th-TH`) fully generated with
transcoded code blocks and translated prose. **Not closed**: current work is a
five-locale fallback slice, not a full locale site.

**Multi-locale partial proof (2026-07-17)**:
- `src/th-TH/`, `src/zh-Hans/`, `src/vi/`, `src/ar/`, and `src/hi/` now
  materialize the portal/start authored slice (`index.md` and `start/*`) with
  fallback prose banners and English source SHA-256 provenance in frontmatter.
- `generator/scripts/build-site.sh` discovers non-English `src/{locale}/`
  directories during the normal build and renders them under
  `dist/{locale}/`.
- Non-Latin builds pass fluid Faber fences through
  `generator/scripts/localize-markdown.py`, which invokes
  `faber emit -t faber --reader-locale=<locale>` before Speculum renders
  HTML. Pinned/reject fences remain authored.
- Validation evidence: `bash generator/scripts/validate-fences.sh src/th-TH`,
  `bash generator/scripts/validate-fences.sh src/zh-Hans`,
  `bash generator/scripts/validate-fences.sh src/vi`,
  `bash generator/scripts/validate-fences.sh src/ar`, and
  `bash generator/scripts/validate-fences.sh src/hi` pass;
  `bash generator/scripts/build-site.sh` renders the locale slices under
  `dist/th-TH/`, `dist/zh-Hans/`, `dist/vi/`, `dist/ar/`, and `dist/hi/`.

**Residuals**:
- Thai, Simplified Chinese, Vietnamese, Arabic, and Hindi prose are fallback
  English for this slice; full prose translation remains open.
- The proof locales do not yet include the full authored docs, translated prose,
  or complete localized navigation; generated corpus, alias redirects, and
  category indexes are present in `dist/{locale}/` as build artifacts.
- `zh-Hant` reader pack ships, but no site slice is generated for it yet.
- The installed `faber emit --reader-locale=<locale>` path currently preserves
  Latin fallback spelling for English-authored fluid fences while emitting
  `READER001` warnings. The site build calls the canonical seam, but visible
  localized keyword rendering still depends on compiler-side fallback
  re-emission.

### Stage 8 — Generated LLM Surface

**Status**: closed (`Stage 8` generated LLM surface landed)
**Source**: `CONTENT-PLAN.md` § Generated — LLM surface
**Why now**: The corpus frontmatter is already a language reference in the
shape an LLM wants.
**Lowers to**: `factory`
**Batching**: `batch-by-default`
**Depends on**: Stage 5

Deliverables:
- [x] `llms.txt` generated from corpus frontmatter during `build-site.sh`.
- [x] Generated surface reports 183 distinct frontmatter terms, 167 canonical
  term pages, 98 alias spellings, category/kind indexes, canonical records with
  summary, syntax signature, aliases, relation graph, source path, and corpus URL.
- [x] The previous authored `static/llms.txt` path was removed; `dist/llms.txt`
  is the build artifact.

**Gate**: **Closed.** `/llms.txt` is regenerated by the site build and serves a
complete corpus-frontmatter language reference.

**Validation evidence**:
- `bash generator/scripts/validate-fences.sh src` → 83 passed / 0 failed / 0 skipped.
- `bash generator/scripts/build-site.sh` → 669 HTML pages, 9 static machine files,
  with smoke checks for the generated `/llms.txt` corpus reference and 183-term count.

**Residuals**:
- Corpus batch still reports the pre-existing alias residual count (`alias_residuals: 1`);
  Stage 8 surfaces the alias map it can derive from current frontmatter and does not
  resolve the underlying corpus alias collision.

## Dependency Rules

| Rule | Detail |
|---|---|
| Stage 1 → all | Generator must exist before any rendering work |
| Stage 1 → Stage 4 | Corpus generator shares the same foundation |
| Stage 2 → Stage 3 | Annotation contract must be proven before porting HTML |
| Stage 4 gate → Stage 5 | `kind` handling must be proven before batch corpus generation |
| Stage 5 → Stage 7 | English corpus must be complete before multilingual |
| External: Homebrew | Getting-started install page needs a 1.1.0+ formula to pass container check |
| External: Deployment | Production publication (DNS, Cloudflare, GitHub Pages) is separately gated |

## First Useful Milestones

| Milestone | Stage | Visible result |
|---|---|---|
| Generator foundation | Stage 1 | ✅ 8 modules type-check clean (2026-07-16) |
| ~~Stepper supports struct fields~~ | Stage 1 | Resolved for compiled path (DEFER-115 fixed `bb19ceb4c`) |
| ~~Textus char access performance~~ | Stage 1 | ✅ Resolved (`db34b9891`); renders 161-line page in 0.8s |
| ~~First rendered page~~ | Stage 1 | ✅ `syntax/types.md` renders as styled HTML (2026-07-16) |
| All authored content live | Stage 2+3 | 23+8 pages rendered, HTML debt cleared |
| First corpus page | Stage 4 | One term page generated from frontmatter |
| Full corpus | Stage 5 | ~167 term pages live |
| On-ramp exists | Stage 6 | Portal + tutorial track |
| First non-English locale | Stage 7 | Thai site with transcoded code |

## Acceptance Criteria

This campaign artifact is accepted when:
- All stages are routed (each has a source, gate, and next action)
- No stage implements code from the top-level artifact
- Stale claims are retired (transcode blocking dependency updated)
- Batching posture is declared per stage
- Dependencies and external gates are explicit

Campaign is **complete** when:
- The site generator produces a full English site (authored + corpus + portal +
  getting-started) with CI-validated fences
- At least one non-English locale is generated
- No HTML content files remain; all content is Markdown or generated

## Validation

| Check | How |
|---|---|
| Fences lex/compile/reject | CI extracts every fence, validates via `faber` CLI |
| Heading anchors stable | Generator asserts explicit IDs, never auto-slugifies |
| Inline spans correct | 48-identifier lookup; 24 of 347 distinct spans map, rest invariant |
| Corpus pages correct by construction | Generated from frontmatter; wrong page = failing test |
| No design system drift | One stylesheet; hash `:root` block; CI checks no inline styles |
| Transcode round-trip | `faber emit` → re-parse → equivalent HIR |
| Install instructions honest | Container CI runs quickstart end-to-end |

## Open Questions

1. **Generator technology — DECIDED: Faber.** The site generator is written in
   Faber itself, dogfooding the language. `faber check` runs the full front end
   (lex → parse → typecheck → MIR lowering) and validates the generator code
   against the type system. Core logic (structs, functions, collections, string
   operations) type-checks today.

   **Learning record** (from Stage 1, see `generator/STAGE-1-LOG.md`):
   - Multi-line strings use `«»` (guillemets), not `"""..."""`. Template
     interpolation is `"§ §"(a, b)`, not `{x}`.
   - `"\n"` escape sequences work (DEFER-066 resolved after factory/stdlib merge).
   - Functions annotated `@ privata` are module-internal and cannot be imported
     cross-module. Omit `@ privata` to export.
   - Import syntax: `importa ex "./path" privata * ut alias`.
   - Type-first parameters: `f(textus name)`, not `f(name: textus)`.
   - `ordo` is the enum keyword — cannot be used as a field name (use `positio`).
   - Map access returns `valor`; cast with `fields[key] ↦ textus`.
   - Boolean assignment needs parens: `← (verum)`, not `← verum`.

   **Execution path**: `faber build -t rust` now works (DEFER-115 fixed in
   `bb19ceb4c`). The generator compiles to a working Rust binary. The MIR
   stepper (`faber run --interpret`) is still blocked on struct field projection
   support, but the compiled path is the primary execution route for the
   generator.

2. **`kind` values → pages** — Which of the 17 `kind` values in corpus
   frontmatter become standalone pages? `legacy`, `smoke`, `existing-home` are
   probably not pages. This is a Stage 4 decision.

3. **Comments in `.fab` files** — Three options from the content plan: (a)
   suppress in-code comments, promote to frontmatter `summary`; (b) accept
   English comments in localized code; (c) LLM translates into code blocks.
   This is a Stage 4/7 decision.

4. **Site is reference-only or reference-plus-on-ramp?** — The content plan
   leans toward including the getting-started track (Decision 16/17), but notes
   this is still open. The campaign includes it; it can be descoped.

## Stop Conditions

- Pause if the generator technology choice requires operator input (Stage 1) —
  **resolved**: Faber chosen, foundation built
- Pause if the MIR stepper struct-field blocker requires external fix (Stage 1) —
  **resolved for compiled path**: DEFER-115 fixed; stepper still blocked but not gating
- ~~Pause if naive O(n²) string performance prevents practical execution (Stage 1)~~ —
  **resolved**: `db34b9891` adds zero-allocation `textus[i]` scalar indexing
- Pause if the `argumenta` codegen gap blocks package CLI arguments (Stage 1) —
  **non-blocking for site file I/O**: package file access uses `norma:solum`;
  PKG001 only blocks `faber:*`, which remains script-only
- Pause if Homebrew formula publication is needed for getting-started (Stage 6)
- Pause if production deployment decisions arise (DNS, Cloudflare, analytics) —
  these are operator-gated, not campaign-gated
- Pause if a corpus `kind` handling decision requires operator input (Stage 4)
