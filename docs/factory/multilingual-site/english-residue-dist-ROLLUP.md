# English residue rollup — non-English `dist/` pages

**Date:** 2026-07-20  
**Scope:** Generated HTML under `dist/{ar,hi,th-TH,vi,zh-Hans,zh-Hant}/`  
**Method:** Parallel Flash audits (one agent per locale) + parent verification of `title` frontmatter and main-content ASCII density.

Per-locale reports:

| Locale | Report |
|--------|--------|
| hi | `english-residue-dist-hi.md` |
| ar | `english-residue-dist-ar.md` |
| th-TH | `english-residue-dist-th-TH.md` |
| vi | `english-residue-dist-vi.md` |
| zh-Hans | `english-residue-dist-zh-Hans.md` |
| zh-Hant | `english-residue-dist-zh-Hant.md` |
| mechanical pre-scan | `english-residue-mechanical.json` |

---

## Executive judgment

**Authored body prose is largely translated.** Across all six locales, paragraph/table/list content under `start/`, `syntax/`, `features/`, `tooling/`, `ecosystem/`, etc. is in the target language.

**English residue is mostly systemic chrome**, not scattered untranslated paragraphs. Fixing a few generators/templates collapses hundreds of page-level findings.

**Latin Faber keywords in code fences are expected** (canonical surface / corpus policy). That is not treated as missing translation here.

---

## Pattern A — English `title` frontmatter → `<title>`, `<h1>`, `og:title`

**Verified in source.** Sample (all non-en locales unless noted):

| Path | `title` frontmatter | Body H1 often localized? |
|------|---------------------|---------------------------|
| `src/*/start/index.md` | mostly `"Quick tour"` (th-TH has `"ทัวร์ด่วน"`) | varies |
| `src/*/features/index.md` | `"Features"` | body translated |
| `src/*/syntax/control-flow.md` | `"Control flow"` | body translated |
| `src/*/404.md` | `"Page not found"` | body H1 localized (e.g. Hindi `# 404 — पृष्ठ नहीं मिला`) |

SSG uses frontmatter `title` for chrome H1/title, so the English title wins even when the Markdown body has a localized heading.

**Fix locus:** localize `title = "..."` in every `src/<locale>/**/*.md`, then rebuild. One field per page fixes three English surfaces.

**Scale:** ~40–46 authored pages × 6 locales.

---

## Pattern B — Shared layout strings (every page)

Hardcoded English in the site generator/template (see `generator/…` agent-notice builders):

| String | Surfaces |
|--------|----------|
| `Skip to content` | skip-link on every page |
| `If you are an AI agent: start at /llms.txt…` | agent-notice body (every page or home/404) |
| `Machine documentation` | nav `aria-label` |
| `keyword…` / `Search keywords` | search box |

**Fix locus:** locale table / i18n partial in the generator, not per-page Markdown.

**Note:** Agent-facing English may be *intentional* policy. If so, keep it but confine it to agent chrome and translate the human skip-link/search labels.

---

## Pattern C — Corpus generator (high volume, known policy)

| Surface | Residue | Notes |
|---------|---------|-------|
| `corpus/index.html` | English intro, `Categories` / `Terms`, meta description | per locale |
| `corpus/category/*.html` (~46 each) | `Corpus: {name}`, “N canonical terms…”, “prose is canonical Latin” | ~98% ASCII main text |
| Individual term pages | out of agent scope; same pipeline | code Latin by design |

Status lines already say “reader-locale proof” / “prose is canonical Latin”. Treat as **generator debt** if product wants localized corpus chrome; **not** as failed prose translation of authored docs.

---

## Pattern D — Isolated content issues (locale-specific)

Agents also flagged occasional one-offs (verify before bulk work):

- **ar:** table header “Construct” on `syntax/errors.html`
- **vi:** some pages where English title dominates the opening of main (`Data types`, `Commands you will use`)
- **th-TH / zh-Hans:** history/releases and references pages with mixed English H1 + localized body

These map back to the same `title` field more often than to untranslated body paragraphs.

---

## What we are *not* flagging (per operator guidance)

- CLI examples (`faber check`, shell)
- Paths / repos (`faberlang/examples`, `faber.toml`)
- Brand names (Faber, Radix, Norma, Cista, Triga)
- Glyphs and intentional Latin keyword samples
- OS/package surface English where the platform is English

---

## Recommended fix batches (priority)

| Pri | Batch | Effort | Blast radius |
|-----|-------|--------|--------------|
| 1 | Localize frontmatter `title` for all `src/{ar,hi,th-TH,vi,zh-Hans,zh-Hant}/**/*.md` | mechanical + LLM titles | all authored page chrome |
| 2 | Generator i18n: skip-link, search labels, optional agent-notice | small code change | every page |
| 3 | 404 title alignment (frontmatter already wrong; body often OK) | subset of #1 | 404 |
| 4 | Corpus generator strings (index + category chrome only) | generator | ~50 pages × 6 locales |
| 5 | Spot-fix table headers / residual body English from per-locale reports | small | few pages |

---

## Parent verification notes

- `title` frontmatter really is still English on representative pages (except th-TH `start/index.md`).
- Body H1 in 404 sources is already localized while `title` is not — confirms chrome vs body split.
- High ASCII density on corpus category pages is real and generator-wide.
- Authored section pages are not “English with a few translated words”; residue is title/chrome-first.

---

## Next step options (not done)

1. Batch-localize `title` frontmatter only (Flash × 6 locales).
2. Generator string i18n PR for skip-link / search / agent-notice.
3. Decide corpus chrome policy: keep Latin-canonical notice, or localize chrome around Latin code.
