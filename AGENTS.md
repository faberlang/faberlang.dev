# faberlang.dev — Agent Guide

## What this repo is

The faberlang.dev documentation site. Contains Markdown source pages, the
Speculum site generator (written in Faber), and the deployment pipeline for
the live website at https://faberlang.dev.

## Repository layout

```text
faberlang.dev/
  src/en-US/               English Markdown (sole prose authority)
  src/{locale}/            Per-locale Markdown (full-file copies; partial OK)
  static/                  Machine surfaces copied into dist/ as-is
    llms.txt               Agent index (start here for models)
    llms-full.txt          Expanded agent map
    agents/index.md        Agent learning path
    .well-known/agent-skills/  Skill catalog + SKILL.md guides
  generator/               Speculum site generator (Faber → Rust binary)
    locales.toml           Locale registry (reader_locale, native names)
    src/                   Faber modules
    www/speculum.css       Shared stylesheet (single source of truth)
    scripts/build-site.sh  Full site render + redirects + gates
    scripts/render.sh      Single-page render wrapper
    scripts/validate-fences.sh  CI fence validator
    faber.toml             Package config
  dist/                    Committed static site (GitHub Pages artifact root)
    en-US/…                English content (and all locales under {locale}/)
    index.html             Interim redirect → /en-US/ (portal is Phase 2)
    start/… etc.           Meta-refresh stubs → /en-US/… for old root URLs
  docs/factory/
    multilingual-site/     Stages 6–7 factory goal + delivery
    site-implementation/CAMPAIGN.md  Campaign stages and gate status
  CONTENT-PLAN.md          Architecture: generated vs authored content
  AGENTS.md                This file
```

## Deployment architecture

### DNS and serving

| Layer | Detail |
|---|---|
| **Domain** | `faberlang.dev` |
| **DNS** | GitHub Pages IPs (`185.199.108–111.153`) |
| **Server** | GitHub Pages |
| **Worker (dormant)** | Cloudflare Worker in `cloudflare-worker/` — not currently active; DNS points to GitHub Pages |

### Deploy workflow

The live site deploys from `origin/main` via GitHub Actions:

1. **Trigger:** Push to `main` branch
2. **Workflow file:** `.github/workflows/deploy-pages.yml`
3. **Build:** Copies `assets/` → `dist/`, substitutes `__PUBLIC_ORIGIN__` and `__DOCS_VERSION__` placeholders
4. **Artifact:** Uploads `dist/` as a GitHub Pages artifact
5. **Deploy:** `actions/deploy-pages@v4` publishes the artifact

### What is live today

The **origin/main** tip (`ee8a00e`) serves the RC1 preview site:

```text
assets/
  index.html         Homepage with hero, nav, feature sections
  index.css          Homepage stylesheet (inline design tokens)
  llms.txt           Agent primer (Markdown)
  docs/1.0.0-rc.1/   Versioned doc stubs (Markdown)
  contracts/         JSON contracts (keywords, types, targets, etc.)
  .well-known/       Agent skills, language catalog
  reports/           RC1 checklists, provenance
```

### What is live now (Stage 3 complete)

The site is generated from Markdown sources through the Speculum generator.
The deploy pipeline is:

1. **Local render:** `generator/scripts/build-site.sh` renders every
   `src/{locale}/` tree to `dist/{locale}/`, writes root meta-refresh
   stubs for retired English-at-root paths, and runs gates
2. **Commit:** `dist/` is committed to the repo (the generator requires
   the Faber compiler, which is not available in CI)
3. **Deploy:** Push to `main` triggers `.github/workflows/deploy-pages.yml`,
   which uploads `dist/` as a GitHub Pages artifact and deploys it

**URL scheme (Phase 1 / Decision 18a):** content lives at `/{locale}/…`
including English (`/en-US/…`). Root `/` currently redirects to `/en-US/`
until the language portal ships (Phase 2). Agent surfaces (`/llms.txt`,
`/agents/`, `/.well-known/`) stay locale-less at the site root.

**To update the live site after content changes:**

```bash
# 1. Render all pages (includes post-build gates, sitemap, canonical tags)
bash generator/scripts/build-site.sh

# 2. Commit both source and rendered output
git add src/ dist/ static/
git commit -m "content: update pages"
git push origin main
```

The push triggers the deploy automatically. GitHub Pages typically updates
within 1-2 minutes. The build halts on any gate failure (broken links,
leakage, missing discovery surfaces).

## Speculum generator

### How it works

The generator is a Faber package at `generator/` that compiles to a Rust
binary. It converts Markdown → HTML with:

- Block-level parsing (headings, paragraphs, tables, lists, code blocks)
- Inline span rendering (backtick code, bold)
- Heading anchors (`{#kebab-case-id}` syntax)
- Frontmatter extraction
- Shared stylesheet injection

### Render pipeline

```bash
# Full site build (renders all pages + corpus + locales + gates)
bash generator/scripts/build-site.sh

# Render a single page (site_locale, reader_locale)
generator/scripts/render.sh src/en-US/syntax/types.md en-US la /speculum.css output.html

# Validate all code fences
generator/scripts/validate-fences.sh src/en-US
```

`render.sh` builds the Speculum package to Rust, compiles it, and runs it.
Speculum reads and writes site files through `norma:solum`; `faber:*` remains
script-only rather than an application file-I/O path.

### Post-build validation scripts

`build-site.sh` runs these automatically as fail-closed gates on the top-level
build. They can also be run standalone:

| Script | Purpose | Exit |
|---|---|---|
| `check-internal-links.py` | Verifies every internal `href` target exists in `dist/` | 1 on broken links |
| `check-leakage-gate.py` | No English→locale nav leakage; all locale pages carry honesty notice | 1 on gap |
| `generate-sitemap.py` | Generates `dist/sitemap.xml` from HTML files (excludes locale dirs) | — |
| `inject-canonical.py` | Injects `<link rel="canonical">` into pages missing one | — |

The corpus renderer (`render-corpus-batch.sh`) also post-processes its output:
- Suppresses dead cross-reference links (converts to plain text)
- Injects "Translation status" notice on locale corpus pages (`locale != la`)

### Binary versions

- `faber` 1.1.0
- `radix` 0.38.0 (includes `db34b98` textus character access)

## Campaign stages

| Stage | Status | Summary |
|---|---|---|
| 1 — Generator foundation | ✅ Closed | 9 modules, `faber check` clean, renders end-to-end |
| 2 — Annotate authored pages | ✅ Closed | 72/72 fences pass, 146 heading anchors, all 23 pages render |
| 3 — Port HTML to Markdown | ✅ Closed | 0 HTML files remain, 40 pages live, deploy pipeline wired |
| 4 — Corpus slice | ✅ Closed | Proof term page + alias bridge rendered end-to-end |
| 5 — Corpus scale | Implemented with residuals | 167 canonical pages, 95 alias redirects, 45 category indexes, corpus hub |
| 6 — Portal + getting-started | Implemented with residuals | Speculum Porta entry point, install/tutorial track; container install CI still open |
| 7 — Multilingual | Partial proof | `th-TH`, `zh-Hans`, `zh-Hant`, `vi`, `ar`, and `hi` portal/start fallback slices plus generated corpus artifacts; full localized authored docs/prose still open |
| 8 — Generated LLM surface | ✅ Closed | `/llms.txt` generated from corpus frontmatter |

See `docs/factory/site-implementation/CAMPAIGN.md` for full detail.

## Rules for agents

- **Never merge to main without a deploy workflow.** The old workflow was
  deleted; merging without a replacement will blank the live site.
- **Never commit `generator/target/` or `.DS_Store`.** See `.gitignore`.
- **Faber comment rule:** `#` only, on its own line. No inline comments
  (`//` or trailing `#`). Violations throw `LEX006`/`LEX007`.
- **Code fences in Markdown must pass `radix check`.** Run
  `validate-fences.sh` after editing any Markdown with fenced Faber code.
- **One stylesheet.** All CSS lives in `generator/www/speculum.css`. The
  generator cannot write CSS. Do not inline styles in pages.
