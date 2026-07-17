# faberlang.dev — Agent Guide

## What this repo is

The faberlang.dev documentation site. Contains Markdown source pages, the
Speculum site generator (written in Faber), and the deployment pipeline for
the live website at https://faberlang.dev.

## Repository layout

```text
faberlang.dev/
  src/en-US/               Markdown content pages (23 authored)
    syntax/                11 syntax reference pages
    tooling/               3 tooling pages
    ecosystem/             6 ecosystem pages
    references/            3 reference pages
    *.html                 Legacy HTML pages (content reference only)
  generator/               Speculum site generator (Faber → Rust binary)
    src/                   9 Faber modules (~1200 lines)
    www/speculum.css       Shared stylesheet (single source of truth)
    scripts/render.sh      Build + render wrapper (bridges file I/O gap)
    scripts/validate-fences.sh  CI fence validator
    faber.toml             Package config
  docs/factory/
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

1. **Local render:** `generator/scripts/build-site.sh` renders all `.md`
   files in `src/en-US/` to `dist/` as static HTML + CSS
2. **Commit:** `dist/` is committed to the repo (the generator requires
   the Faber compiler, which is not available in CI)
3. **Deploy:** Push to `main` triggers `.github/workflows/deploy-pages.yml`,
   which uploads `dist/` as a GitHub Pages artifact and deploys it

**To update the live site after content changes:**

```bash
# 1. Render all pages
bash generator/scripts/build-site.sh

# 2. Commit both source and rendered output
git add src/ dist/
git commit -m "content: update pages"
git push origin main
```

The push triggers the deploy automatically. GitHub Pages typically updates
within 1-2 minutes.

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
# Render a single page
generator/scripts/render.sh src/en-US/syntax/types.md la /speculum.css output.html

# Validate all code fences
generator/scripts/validate-fences.sh
```

`render.sh` bridges two temporary compiler gaps (argumenta codegen and
PKG001 package resolution) by building to Rust, patching `main.rs` to
inject file I/O, then compiling and running.

### Binary versions

- `faber` 1.1.0
- `radix` 0.38.0 (includes `db34b98` textus character access)

## Campaign stages

| Stage | Status | Summary |
|---|---|---|
| 1 — Generator foundation | ✅ Closed | 9 modules, `faber check` clean, renders end-to-end |
| 2 — Annotate authored pages | ✅ Closed | 72/72 fences pass, 146 heading anchors, all 23 pages render |
| 3 — Port HTML to Markdown | ✅ Closed | 0 HTML files remain, 40 pages live, deploy pipeline wired |
| 4 — Corpus generation | Implemented with residuals | 167 canonical pages, 95 alias redirects, 45 category indexes, corpus hub |
| 5 — Portal + getting-started | Pending | Speculum Porta entry point, install/tutorial track |
| 6 — Multilingual | Pending | Canonical transcode per locale |

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
