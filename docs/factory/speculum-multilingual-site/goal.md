# Goal: Build the Speculum multilingual Faber documentation site

- Date: 2026-07-15
- Repository: `/Users/ianzepp/work/faberlang/faberlang.dev`
- Status: ready for delivery planning
- Primary design direction: Speculum
- Current release corpus target: Faber `1.0.0` development line

## Summary

Turn the current hand-assembled RC1 asset packet into a functional, generated,
multilingual documentation site whose architecture demonstrates Faber's reader
locale thesis. A visitor enters through the Speculum Porta, explicitly chooses a
supported reader locale, and receives versioned documentation in that locale:
prose, navigation, diagnostics, examples, and Faber source renderings all come
from one semantic document model and explicit locale artifacts rather than an
English site with translated chrome.

The implementation must assemble existing pieces instead of reinventing them:
Faber's `ReferencePack`/`Registry` supplies canonical language-reference content;
Radix `ReaderLocalePack` supplies locale-bound keywords, types, diagnostics, and
exemplar metadata; the website owns translated document prose, navigation,
rendering, search, and the generated route manifest; the existing public-packet
validator supplies the fail-closed leakage and contract discipline; and the Rust,
Cloudflare, and GitHub Pages adapters may serve only the same generated artifact.

The first useful proof is a local, deterministic Latin + Thai Speculum slice. It
must include the Porta and one real reference article, with explicit version and
locale URLs, genuinely localized prose/navigation, and a Faber snippet emitted
through a proven locale-rendering seam. Production publication remains separately
gated.

## Problem

The repository contains many of the ingredients for a credible public site, but
they are not connected into a site-generation system:

- `assets/` is a manually checked-in, English-shaped `1.0.0-rc.1` packet.
- `src/main.rs` manually duplicates every served route with `include_str!`.
- `src/bin/validate_public_packet.rs` duplicates version, route, origin, and
  policy constants and parses Rust source to infer the served asset set.
- The Cloudflare Worker serves the same static tree and performs textual
  placeholder substitution, but it has no locale model.
- A GitHub Pages workflow now independently copies `assets/` into `dist/` and
  publishes it on pushes to `main`, creating a second delivery direction that is
  not reconciled with the Worker contract.
- The public campaign and website plan still say implementation begins after the
  Faber 1.0 release closes, although Faber `1.0.0` is released and the local
  `faber` manifest is version `1.0.0`.
- Current website URLs, catalogs, sitemaps, and discovery links hard-code or
  substitute `1.0.0-rc.1`; changing one version variable does not create the
  corresponding physical route tree.
- There is no source manifest, docs generator, locale registry, HTML article
  renderer, human search index, canonical URL model, or localized route tree.
- No current generator consumes `ReferencePack` or `ReaderLocalePack`.
- Current Faber formatting validates localized input but emits canonical Latin;
  `faber emit -t faber --reader-locale=<X>` explicitly rejects localized Faber
  re-emission as deferred.
- ReaderPack data does not contain arbitrary documentation prose. It cannot by
  itself turn an English Markdown corpus into Thai, Chinese, Arabic, Hindi, or
  Vietnamese documentation.

The July 15 Faber research packet established the correct boundary but was never
synthesized into an implementation goal. Child audits completed and were marked
done, while no durable parent task required the Mind to produce an architecture
artifact or implementation handoff.

## Goals

1. Make Speculum the canonical website information architecture:
   - `/` is the Porta, not a marketing landing-page funnel;
   - the reader locale is a primary, explicit selection;
   - documentation is the site;
   - the up-axis locale matrix and down-axis target matrix share one component
     and policy vocabulary;
   - glyph blue remains reserved for invariant Faber glyphs.
2. Establish one generated site manifest as the canonical description of every
   public route, document, locale, version, content type, source authority,
   translation state, digest, and indexing policy.
3. Generate one immutable site artifact from pinned, explicit inputs. Human HTML,
   raw Markdown, `llms.txt`, skills, machine contracts, search indexes, sitemap,
   alternate-language metadata, and checksums must be projections of the same
   manifest and source snapshot.
4. Use Faber `ReferencePack`/`Registry` as the canonical structured language
   reference source instead of scraping `faber explain` terminal output or
   maintaining a second hand-written reference index.
5. Use validated Radix `ReaderLocalePack` artifacts for localized keyword/type
   spellings, diagnostic templates, explicit fallback reporting, LLM/exemplar
   references, and locale metadata. Do not duplicate those tables in website
   JavaScript or content files.
6. Add an explicit locale-owned documentation layer for prose, navigation,
   titles, descriptions, accessibility labels, and terminology that ReaderPacks
   do not contain. Every translation unit must have a stable semantic document
   and message identifier tied to canonical source content.
7. Add or consume a real localized Faber re-emission seam so code snippets on a
   selected-locale page use that reader locale while preserving semantics,
   identifiers, string literals, invariant glyphs, and visible Latin fallback.
   Do not hand-substitute keyword strings in the website generator.
8. Serve stable version + locale identities. Locale and Faber release version are
   independent axes.
9. Preserve plain text and agent-first discovery as first-class outputs while
   adding complete human HTML navigation and search.
10. Make the generated artifact fail closed on private-source leakage, stale
    claims, missing routes, missing translations, invalid localized snippets,
    broken links, digest drift, and deployment-adapter divergence.
11. Reconcile the Rust, Cloudflare, and GitHub Pages paths so there is one
    canonical generated artifact and no adapter-specific content truth.
12. Produce a local functional proof before any public deployment, DNS, route,
    analytics, or announcement decision.

## Non-goals

- Rewriting the Radix compiler or general Faber documentation architecture inside
  the website repository.
- Treating ReaderPack TOML as a complete natural-language prose corpus.
- Runtime LLM translation, runtime model calls, or request-time generation of
  documentation.
- Implicit `Accept-Language` redirects as the canonical locale-selection model.
- Inventing locale vocabulary or completing partial packs merely to make the
  website appear complete.
- Translating identifiers, string literals, package IDs such as `norma:*`, stable
  diagnostic codes, contract keys, URLs, or backend/provider names.
- Claiming every installed locale pack has complete documentation coverage.
- Completing stdlib gloss overlays or measured LLM emission fidelity unless a
  selected delivery slice explicitly requires them.
- Turning the site into a marketing funnel, testimonial page, SaaS control plane,
  package registry, or hosted compiler.
- Publishing, pushing, changing DNS, attaching a Cloudflare route, enabling
  analytics, announcing externally, or changing provider/account configuration.
- Preserving the manually duplicated RC1 route tables as a second supported build
  path after generated-manifest cutover.

## Ground truth researched

### Website repository

- `assets/`: current manually assembled English `1.0.0-rc.1` public packet,
  including versioned Markdown docs, machine contracts, skills, discovery files,
  reports, CSS, homepage HTML, robots, and sitemap.
- `src/main.rs`: Rust/Axum preview adapter with a manual `BTreeMap` of
  `include_str!` assets, root Markdown negotiation, discovery `Link`, and textual
  origin/version substitution.
- `src/bin/validate_public_packet.rs`: strong fail-closed checks for required
  routes, leakage, content claims, links, media types, digests, checksums, skills,
  provenance, and served-document truth; currently coupled to duplicated constants
  and source-text route discovery.
- `cloudflare-worker/src/index.js`, `wrangler.jsonc`, `package.json`: validated
  Cloudflare Static Assets adapter with Worker-first behavior, but no locale or
  generated-manifest contract.
- `.github/workflows/deploy-pages.yml`: push-triggered GitHub Pages publication of
  copied `assets/`, including placeholder replacement. This is a real deployment
  mechanism and must not remain an unexamined parallel production authority.
- `docs/CAMPAIGN.md`: public-surface campaign; Stage 2 still says queued after the
  Faber 1.0 RC closeout.
- `docs/AGENT-FIRST-DOCUMENTATION-WEBSITE-PLAN.md`: agent-first route and content
  model; useful requirements, but its queue/dependency statement is stale and it
  predates the Speculum locale architecture.
- `docs/stage-1-public-contract-matrix.md`: claim and leakage boundaries for the
  local public packet.
- `docs/deployment/cloudflare-workers.md`: local Worker seam and external gates;
  not deployment authority.
- `README.md`: accurately calls the current surface a local preview and does not
  prove public deployment.

### Faber and Radix

- `faber/Cargo.toml`: current public CLI version is `1.0.0`.
- `faber/src/reference.rs`: `ReferencePack::load_from` validates a reference root
  and `build_registry` produces a deterministic structured `Registry` with
  canonical/legacy terms, summaries, syntax, examples, aliases, related terms,
  Markdown bodies, provenance, and version metadata.
- `examples/corpus/index.toml` and associated exempla: public reference-pack source
  consumed by Faber; preferred over private compiler prose for public language
  examples.
- `radix/crates/radix/src/reader_locale.rs`: live `ReaderLocalePack` schema v1,
  aliases, inheritance, explicit Latin fallback, keyword/type bindings,
  diagnostics, validation, and LLM artifacts.
- `radix/stdlib/reader/*/pack.toml`: installed `la`, `th-TH`, `zh-Hans`,
  `zh-Hant`, `ar`, `hi`, and `vi` packs.
- `radix/docs/design/reader-locale.md`: authoritative current status: phases 0–5
  shipped; localized Faber re-emission, stdlib glosses, measured LLM fidelity,
  and multilingual documentation generation remain partial/proposed.
- `faber/src/package/reader.rs`: package/CLI locale selection and pack loading.
- `faber/src/commands/format.rs`: `--reader-locale` currently requires canonical
  mode and emits Latin canonical Faber.
- `faber/src/commands/emit.rs`: localized Faber output explicitly remains deferred.
- `radix/crates/radix/src/diagnostics/render.rs`: pack-owned diagnostics and bidi
  source-display behavior.

### Product direction and recovered research

- `/Users/ianzepp/design-ideas/directions/07-speculum/SPEC.md`: canonical visual
  and information-architecture direction. Its historical statement that packs do
  not ship is stale; its architecture and design rules remain authoritative.
- `faber-porta.html` and `faber-articulus.html`: layout/reference mockups, not
  source code to copy and not implementation truth.
- Faber Vivi reports dated 2026-07-15:
  - ReaderPack substrate is shipped but the Speculum docs generator does not
    exist.
  - `ReferencePack` and `ReaderLocalePack` are distinct sources that must be
    joined deliberately.
  - Current assets have no locale routing, HTML docs, search, `hreflang`,
    canonical metadata, or locale-aware cache contract.
  - Explicit locale paths and build-time static generation are the safest first
    architecture.
  - A manifest-driven generated export is the smallest clean migration from the
    current hand-maintained packet.

## Reference packet

Before implementation, inspect these files in this order:

1. `/Users/ianzepp/design-ideas/directions/07-speculum/SPEC.md`
   - Product and visual invariant.
2. `docs/factory/speculum-multilingual-site/goal.md`
   - Goal boundary and current status.
3. `docs/AGENT-FIRST-DOCUMENTATION-WEBSITE-PLAN.md`
   - Agent-first corpus, discovery, and public/private requirements.
4. `docs/stage-1-public-contract-matrix.md`
   - Claim, leakage, and public-source gates.
5. `assets/contracts/1.0.0-rc.1/documents.json` and current `assets/` tree
   - Existing packet shape to migrate, not preserve as architecture.
6. `src/main.rs`, `src/bin/validate_public_packet.rs`,
   `cloudflare-worker/src/index.js`, and `.github/workflows/deploy-pages.yml`
   - Current adapter and duplicated-truth surfaces.
7. `../faber/src/reference.rs`
   - Canonical structured language-reference seam.
8. `../examples/corpus/index.toml`
   - Public exempla/reference source.
9. `../radix/docs/design/reader-locale.md`
   - Reader locale status and required semantics.
10. `../radix/crates/radix/src/reader_locale.rs` and
    `../radix/stdlib/reader/{la,th-TH}/pack.toml`
    - Pack schema and first-proof locale data.
11. `../faber/src/commands/{format,emit}.rs`
    - Current localized re-emission gap.
12. `docs/deployment/cloudflare-workers.md` and `wrangler.jsonc`
    - Existing deployment seam and external stop line.

Supporting read-only checks:

```bash
git status --short --branch
git log --oneline -20
cargo test --all-targets
cargo run --bin validate_public_packet
npm run cf:dry-run
```

Do not run external deployment or provider commands while establishing the local
implementation plan.

## Constraints and invariants

### Product and design

- Speculum is a reference work, not a campaign landing page. Documentation is the
  primary product surface.
- The Porta asks what the visitor reads. Locale selection is not hidden in a
  footer control.
- `--glyph` blue is reserved for invariant Faber glyphs (`← → ∴ ≡ ∪ ⇥`) and
  nothing else.
- Multi-script typography must use real script coverage. Code layout cannot
  depend on a universal monospace character grid.
- The locale matrix and target matrix use the same table component and policy
  verbs because they represent equivalent rendering axes.
- Capability and locale coverage claims must expose measured or evidenced status.
  Partial packs and fallback are visible, never cosmetically hidden.

### Content truth

- One semantic document ID has multiple locale renderings. Locale files do not
  fork document identity or Faber semantics.
- Reference content originates from public, versioned Faber/exempla artifacts.
  The website never recursively crawls private Radix docs.
- ReaderPacks bind compiler identities to human-facing spellings and diagnostics;
  they do not own arbitrary article prose.
- Locale prose is explicit source data with provenance and review state. Missing
  prose cannot silently fall back while being labeled translated.
- Generated source snippets must parse and preserve the same semantic facts as
  their canonical twin. Keyword substitution in website templates is forbidden.
- Comments and identifiers are not compiler-localized. Preserve them unless an
  explicitly reviewed content source provides localized alternatives.
- Stable diagnostic codes, route IDs, package names, and contract fields remain
  invariant across locales.

### URLs and selection

- Canonical human URL shape:
  `/docs/<faber-version>/<locale>/<document-slug>/`.
- Canonical raw Markdown shape:
  `/raw/<faber-version>/<locale>/<document-slug>.md`.
- `/` is the Porta and may use `Accept-Language` only as a non-authoritative hint;
  it must not silently redirect or change canonical content identity.
- Locale selection is explicit and durable in links.
- Version and locale are independent. A new Faber release does not create a new
  locale, and a locale update does not rewrite an immutable released corpus.
- A convenience `latest` alias must redirect to an explicit immutable version and
  must never become canonical or silently mutable under long cache lifetimes.
- Fallback to Latin must be labeled, counted, and represented in the generated
  manifest and UI.

### Architecture and generated truth

- Introduce one checked-in source manifest or manifest family declaring at least:
  release version/lane, source revisions, locale registry/default, document IDs,
  locale source/status, route, content role, translation state, public/private
  gate, and digest policy.
- The generator owns route expansion. Rust, Worker, Pages, sitemap, catalogs,
  search, and validators consume its output/manifest rather than independently
  listing routes.
- Generate into one disposable artifact directory, recommended `dist/`. Do not
  make generated output the editable source of truth.
- The current hand-maintained `assets/` route tree must either become generated
  output or be retired after cutover. It must not remain a parallel manual build.
- The generator must be deterministic and idempotent from pinned local inputs.
- Runtime translation and runtime model calls are forbidden. Publication artifacts
  are produced before deployment.
- Adapter-specific placeholder substitution must not invalidate published digests.
  Prefer build-time canonical origin/version expansion in immutable assets.

### Privacy, authority, and release

- Public output must not include private Radix paths, `.rs` implementation paths,
  factory ledgers, deferred IDs, local absolute paths, private fixtures, or claims
  based only on unreleased internals.
- A public repo is not permission to publish every locally generated artifact.
- Local implementation may add code, tests, docs, and generated fixtures.
- Push, Pages publication, Cloudflare deployment, routes, DNS, analytics, external
  translation services, provider calls, and announcements remain operator-gated.
- The push-triggered Pages workflow is an external-effect surface. Do not push a
  branch containing implementation work until its publication behavior and target
  are explicitly approved.

## Architecture direction

### Source and projection flow

```text
Pinned public Faber release facts
  ├── Faber ReferencePack / Registry
  ├── public examples corpus
  ├── released capability + diagnostic contracts
  └── release/version metadata

Validated ReaderLocalePack artifacts
  ├── keyword/type spellings
  ├── diagnostics and named arguments
  ├── explicit Latin fallback facts
  ├── locale metadata
  └── exemplar/prompt references

Website-owned document sources
  ├── semantic document specifications
  ├── locale prose/navigation catalogs
  ├── translation status and provenance
  └── Speculum templates/tokens/components

Localized Faber renderer
  └── semantic source/HIR + ReaderLocalePack -> localized Faber snippet

                    ↓

Deterministic website generator
  ├── joins semantic docs + reference registry + locale catalogs
  ├── validates localized snippets and canonical twins
  ├── renders Porta and article HTML
  ├── renders raw Markdown and agent skills
  ├── builds per-locale search and discovery data
  ├── emits route/content/digest manifest
  └── emits one immutable `dist/` artifact

                    ↓

Thin adapters over exactly `dist/`
  ├── local Rust preview
  ├── Cloudflare Worker Static Assets
  └── optional GitHub Pages preview/static host
```

### Canonical ownership

| Concern | Owner |
| --- | --- |
| Semantic language reference and exempla | Faber `ReferencePack`/`Registry` + public `examples` corpus |
| Keyword/type/diagnostic locale bindings | Radix `ReaderLocalePack` artifacts |
| Localized Faber source emission | Faber/Radix formatting or rendering seam; not website string substitution |
| Article identity, prose translations, navigation, IA, templates | `faberlang.dev` source tree |
| Route/version/locale expansion and generated catalogs | `faberlang.dev` generator + site manifest |
| Public/private export and claim gates | website validator consuming generated manifest and pinned provenance |
| Local preview | Rust adapter over generated `dist/` |
| Edge/static publication | one selected adapter over generated `dist/`; choice required before release |

### Document model

A document is not a Markdown filepath. It is a semantic record with a stable ID,
for example `language.functions`, containing:

- canonical title/summary and reference-registry links;
- ordered semantic sections and source facts;
- examples identified by public corpus ID;
- related constructs and stable diagnostic IDs;
- release applicability and status;
- per-locale prose/navigation rendering records;
- per-locale translation state: `complete`, `partial`, `latin-fallback`, or
  `not-public`;
- provenance and content digest inputs.

The exact serialization belongs in delivery planning, but it must be declarative,
reviewable, deterministic, and separate from generated HTML/Markdown.

### Locale rendering

For each `(release, locale, document)` tuple, the generator:

1. loads the canonical semantic document;
2. loads the matching locale prose/navigation catalog;
3. loads the validated `ReaderLocalePack`;
4. resolves reference terms and examples through `Registry`;
5. obtains localized Faber snippets through the upstream renderer;
6. records every fallback token/section explicitly;
7. renders HTML and raw Markdown from the same document projection;
8. validates internal links, `lang`, `dir`, bidi isolation, alternate links,
   search metadata, and digests;
9. emits one manifest row used by all delivery adapters.

No locale may be marked complete solely because an installed ReaderPack exists.

### Human and machine surfaces

Human surface:

- Porta at `/`;
- HTML articles under canonical versioned locale URLs;
- persistent rendering bar;
- per-locale navigation and search;
- visible fallback indicators;
- canonical/alternate metadata and accessible language/direction handling.

Machine surface:

- concise root `llms.txt` plus explicit locale primers;
- raw Markdown for every public article;
- locale/version document catalogs with digests and translation state;
- agent-skill index generated from the same source manifest;
- released contracts and checksums;
- no implication that `llms-full.txt` is a complete corpus unless it is actually
  generated as one.

### Delivery adapters

The build artifact is canonical; adapters are replaceable.

- Rust must stop manually enumerating content routes. It should serve generated
  files/manifest data for local preview and preserve required HTTP behavior.
- Cloudflare must serve the same generated directory. Worker logic should be
  limited to behavior that static hosting cannot provide, such as health,
  discovery headers, and negotiated root representation.
- GitHub Pages may serve a static preview only if its inability to reproduce
  Worker headers/negotiation is explicit. It must not silently become a second
  production contract.
- Before publication, select one canonical production path and disable or clearly
  scope any competing push-triggered deployment.

## Supporting skills

- `$faber`: verify live ReaderPack, ReferencePack, formatting, corpus, and release
  behavior before implementing cross-repo seams.
- `$goal-check`: cold-read this goal before factory execution.
- `$delivery`: compile the first Latin + Thai vertical proof into a repo-aware,
  cross-repo delivery spec.
- `$factory`: execute implementation phases with review and commits.
- `$zombie-docs`: retire stale RC1/queued-after-release and stale Speculum pack
  status claims as implementation advances.
- `$red-green`: establish the generator, locale rendering, and adapter contract
  through executable acceptance tests.
- `$correctness`: review source authority, fallback truth, route/digest behavior,
  and cross-locale semantic equivalence.
- `$docs`: maintain contributor, translation, build, and deployment documentation
  after the architecture exists.

## Implementation shape

### Milestone 1 — Manifest-driven Latin site cutover

Create the smallest generator and manifest that can reproduce a useful subset of
the current site for Faber `1.0.0`:

- Porta with honest locale status;
- one canonical reference article;
- Latin HTML and raw Markdown;
- route/content/digest manifest;
- generated `llms.txt`, sitemap entry, and document catalog;
- local Rust preview serving generated output;
- validator reading generated manifest rather than parsing route lists from Rust
  source.

This milestone proves generated truth and retires manual route duplication for the
selected slice. It does not claim multilingual completion.

### Milestone 2 — Latin + Thai vertical Speculum proof

Add one complete Thai rendering of the same article:

- reviewed Thai prose and navigation from explicit locale source;
- localized diagnostics/terminology from `th-TH` ReaderPack;
- one localized Faber code snippet produced by the upstream renderer;
- Latin semantic twin verification;
- explicit fallback count and UI;
- `/docs/1.0.0/la/<slug>/` and `/docs/1.0.0/th-TH/<slug>/` HTML;
- matching raw Markdown, alternate links, `lang`/`dir`, catalog, sitemap, and
  search-index entries;
- Porta and rendering bar switch between the two stable routes.

If localized Faber re-emission is not yet available, this milestone remains
blocked at that exact dependency. Do not weaken it to hand-substituted keywords
or silently Latin code on a supposedly complete Thai page.

### Milestone 3 — Site-wide generated corpus

Once the vertical proof is accepted:

- migrate the selected public Faber 1.0 documentation families into semantic
  document sources;
- generate accessible HTML, raw Markdown, search, skills, catalogs, contracts,
  sitemap, and checksums;
- expand locale coverage only where prose and snippet evidence meet the published
  status;
- retire manual `assets/` editing and duplicated route/version constants;
- reconcile Rust, Worker, and Pages adapters against the generated artifact.

### Later

- Additional complete locale corpora.
- Stdlib gloss overlays.
- Measured model emission-fidelity studies.
- Community translation workflow and review tooling.
- Additional release versions and even-major LTS lock metadata.
- Public deployment and launch after separate authorization.

## Release posture

Decision: **release preparation only; publication is gated**.

The goal may produce a locally complete Faber `1.0.0` site artifact and a precise
publication packet. It does not authorize:

- pushing commits that trigger GitHub Pages;
- selecting GitHub Pages or Cloudflare as production;
- deploying a Worker;
- enabling a Pages environment;
- attaching `faberlang.dev`;
- changing DNS, routes, TLS, analytics, or provider variables;
- announcing the site.

Before publication, the delivery/factory process must present:

- exact source commit and generated artifact digest;
- chosen canonical deployment adapter;
- current public-site/Pages/Cloudflare inventory;
- route and domain mutation proposal;
- rollback target and procedure;
- production verification checklist;
- explicit operator authorization.

No version/tag decision is implied for compiler/runtime repos by this website
goal. Website content must accurately label Faber 1 as an odd-major development
line and must not imply language lock.

## Exit strategy

Decision: included.

- Generated output is disposable and reproducible from pinned source inputs.
- Locale publication is manifest-controlled; an incomplete or invalid locale can
  be removed from public routing without deleting its source work.
- The Porta must display only locales admitted by the generated release manifest.
- Each immutable release+locale route can be rolled back by restoring the prior
  generated artifact and adapter deployment.
- The convenience `latest` alias can be repointed independently; immutable routes
  remain unchanged.
- Adapter code is thin and replaceable because it does not own content truth.
- If localized rendering proves unsafe, keep Latin generated docs live locally and
  leave the affected locale `not-public`; do not fall back to the manual RC1 tree
  as a permanent second architecture.

## Acceptance criteria

### Architecture and source truth

- One declarative manifest identifies every generated public document by release,
  locale, semantic ID, route, content role, translation status, source authority,
  and digest policy.
- The build consumes only explicit pinned inputs and does not recursively crawl
  sibling/private repositories.
- `ReferencePack`/`Registry` supplies canonical reference entries and exempla.
- `ReaderLocalePack` supplies locale keyword/type/diagnostic bindings without
  website-maintained duplicate tables.
- Locale prose/navigation sources are explicit and separately reviewable.
- The generated artifact is reproducible and idempotent.

### Functional site

- `/` renders the Speculum Porta with honest locale status and no marketing funnel.
- Selecting Latin or Thai leads to stable canonical version+locale URLs.
- At least one reference article exists in complete Latin and Thai renderings.
- Both renderings contain localized prose/navigation and share the same semantic
  document identity.
- The Thai page contains a Faber snippet emitted through the locale-rendering seam,
  not website string substitution.
- Latin and Thai snippets prove semantic equivalence through an agreed compiler/HIR
  or canonical-twin check.
- Fallback is visible, counted, and represented in the generated manifest.
- HTML includes correct `lang`, direction/bidi behavior, canonical URLs, alternate
  locale links, keyboard-visible focus, and a skip path.
- Raw Markdown and agent discovery remain usable without JavaScript.
- Per-locale search returns only admitted documents from the selected locale or
  explicitly labeled fallback results.

### Generated contract and adapters

- Human HTML, raw Markdown, `llms.txt`, skills, search, catalogs, sitemap, and
  checksums are generated from one manifest/source snapshot.
- Rust no longer manually enumerates selected generated content routes.
- Validator route coverage comes from generated manifest data rather than parsing
  `src/main.rs` source text.
- Cloudflare and Pages consume the same generated artifact when enabled.
- Adapter output contains no unresolved origin/version placeholders and published
  digest semantics match served bytes.
- A chosen canonical production adapter is documented before any release; the
  other adapter is explicitly preview-only, disabled, or removed.

### Honesty and safety

- No output leaks private Radix paths, factory content, local absolute paths,
  internal deferred IDs, or unsupported product claims.
- No locale is labeled complete merely because a ReaderPack exists.
- The site states Faber `1.0.0` is an odd-major development release, not a
  language-locked LTS release.
- Missing translations, partial packs, unsupported snippets, and deferred
  capabilities fail closed or appear as explicit fallback/partial status.
- Local completion makes no claim of public deployment.

## Validation

Required local gates after implementation slices select exact commands:

```bash
# Website repository
git diff --check
cargo test --all-targets
cargo run --bin validate_public_packet

# Generated artifact determinism
rm -rf /tmp/faber-site-a /tmp/faber-site-b
<site-build-command> --output /tmp/faber-site-a
<site-build-command> --output /tmp/faber-site-b
diff -ru /tmp/faber-site-a /tmp/faber-site-b

# Cloudflare packaging only; no deploy
npm ci --ignore-scripts
npm run cf:dry-run
```

Cross-repo proof for the Latin + Thai vertical slice must include focused current
commands selected by delivery planning for:

- `ReaderLocalePack` load/completeness;
- `ReferencePack::build_registry`;
- localized snippet parse/render;
- Latin/Thai semantic-twin equivalence;
- explicit fallback diagnostics;
- generated website route and link integrity.

Manual local acceptance:

1. Start the local site against the generated artifact.
2. Open `/` and verify the Porta, locale grouping, glyph-only blue, keyboard
   navigation, and no marketing CTA treatment.
3. Select Latin and Thai.
4. Verify stable versioned URLs, rendering bar, localized prose/navigation,
   localized Faber snippet, invariant glyph positions, and visible fallback.
5. Verify direct refresh works on both canonical routes.
6. Verify raw Markdown and machine catalogs point to the same semantic documents.
7. Verify all internal links, alternate links, search results, and sitemap entries.
8. Verify no external provider, deployment, or public-host mutation occurred.

Review gates:

- Correctness review of semantic source authority, localized snippet equivalence,
  fallback handling, cache/digest behavior, and leakage checks.
- Accessibility review across Latin, Thai, Chinese sample glyph coverage, Arabic
  bidi sample content, reduced motion, keyboard focus, zoom/reflow, and screen
  reader order before broader locale publication.
- Goal completion review must compare the generated artifact against this goal,
  not merely report that current RC1 tests remain green.

## Open questions

These questions do not block Milestone 1 unless stated otherwise:

1. **Canonical public adapter:** Cloudflare Worker or GitHub Pages? This blocks
   publication, not local generator work. Cloudflare preserves HTTP negotiation
   and discovery headers; Pages is static and currently push-triggered.
2. **Localized Faber renderer ownership:** should the first stable API live in
   Radix `forma`, the public Faber CLI/library, or a public export tool? This
   blocks Milestone 2 and must be decided in its delivery spec.
3. **Locale prose format:** TOML/JSON message catalogs, structured Markdown, or a
   typed document DSL? Delivery must select one declarative format before content
   migration. It may not use generated HTML as source.
4. **Translation provenance:** human-authored, model-assisted then reviewed, or
   both? Every public locale needs an explicit status and reviewer/evidence field.
5. **Current public deployment inventory:** has the new GitHub Pages workflow
   successfully published, and is any current hostname already an external
   contract? Read-only inventory is required before route retirement or push.
6. **RC1 route migration:** if `1.0.0-rc.1` URLs are externally reachable, should
   they remain immutable historical routes or redirect to the final release?
   Decide from observed live evidence, not assumption.
7. **Latin versus English prose:** `la` names the canonical Faber source surface,
   but public explanatory prose may initially be English. The manifest must name
   these dimensions honestly rather than calling English prose “Latin.”
8. **Search implementation:** generated static index and minimal client search is
   the default; a hosted search provider requires separate privacy/spend/provider
   approval.

## Stop conditions

Stop and return for clarification or a new delivery boundary if:

- implementation starts by copying the Speculum mock HTML rather than deriving
  components and data contracts;
- the generator needs to scrape private Radix prose or recursively traverse the
  workspace;
- website code begins maintaining its own keyword/type/diagnostic translation
  tables;
- a Thai or other locale page is labeled complete while its prose or snippet is
  Latin/English without explicit fallback status;
- localized Faber source is produced by string replacement rather than a compiler
  or formatter rendering seam;
- runtime translation/model calls become necessary;
- generated routes, catalogs, sitemaps, and adapter route lists become independent
  sources of truth;
- the existing RC1 packet is preserved as a second manual build “for
  compatibility” without verified external-contract evidence;
- implementation would push to `main` and trigger Pages publication without
  explicit authority;
- work requires Cloudflare login, deployment, route/DNS mutation, analytics,
  external translation services, spend, credentials, or public communication;
- public claims outrun released Faber `1.0.0` behavior or current locale evidence;
- foreign worktree changes overlap the selected implementation files and cannot be
  safely isolated.

## First handoff

Lower **Milestone 1 — Manifest-driven Latin site cutover** through `$delivery`.
That delivery spec must choose the manifest/document serialization, generator
location, generated artifact directory, and exact migration boundary for
`assets/`, `src/main.rs`, the validator, and deployment adapters. It must preserve
the Milestone 2 dependency on a real localized Faber renderer rather than
weakening the multilingual product invariant.
