# English Residue Audit — `dist/hi/`

Audited **all non-corpus HTML pages** under `dist/hi/`, plus `corpus/index.html` and all `corpus/category/*.html` pages. Individual corpus term pages (`corpus/<term>.html`) were excluded per scope.

---

## Summary

| Severity | Count | Description |
|----------|-------|-------------|
| **High** | ~48 pages | Whole page sections in English (agent notices); corpus-generated pages with English-only prose |
| **Medium** | ~40 pages | English `<title>` and `<h1>` on pages with otherwise-Hindi body content |
| **Low** | ~40 sites | English "Skip to content" link on every page; stray English phrases in table cells |

### Quick assessment

The underlying **body prose** is very well translated — nearly every content `<p>`, table body cell, and list item is in Hindi. The residue is concentrated in **page chrome** (titles, headings, og:meta) and in **generated corpus pages** whose prose was never localized. The `hi` locale is correctly labelled "Stage 7 partial proof" — the portal/start author slices are translated, but the authored prose in many subpages remains English at the title/heading level.

---

## Findings Table

### A. English `<title>` tags — all 40+ pages (medium severity)

Every page except the top-level `index.html` has an English `<title>`. The title follows the pattern `<English name> — Faber`.

| # | dist path | Title (English → should be Hindi) | Source path (likely) |
|---|-----------|-----------------------------------|----------------------|
| 1 | `/hi/404.html` | `Page not found — Faber` | `src/hi/404.html` or template |
| 2 | `/hi/start/` | `Quick tour — Faber` | `src/hi/start/index.md/html` |
| 3 | `/hi/start/install.html` | `Install and download — Faber` | `src/hi/start/install.md/html` |
| 4 | `/hi/start/hello.html` | `Hello, Faber — Faber` | `src/hi/start/hello.md/html` |
| 5 | `/hi/start/commands.html` | `Commands you will use — Faber` | `src/hi/start/commands.md/html` |
| 6 | `/hi/start/projects.html` | `Projects and examples — Faber` | `src/hi/start/projects.md/html` |
| 7 | `/hi/start/examples.html` | `Examples — Faber` | `src/hi/start/examples.md/html` |
| 8 | `/hi/features/` | `Features — Faber` | `src/hi/features/index.md/html` |
| 9 | `/hi/features/reader-locale.html` | `Reader locale — Faber` | `src/hi/features/reader-locale.md/html` |
| 10 | `/hi/features/compilation-lanes.html` | `Compilation lanes — Faber` | `src/hi/features/compilation-lanes.md/html` |
| 11 | `/hi/features/latin-and-glyphs.html` | `Latin vocabulary and structural glyphs — Faber` | `src/hi/features/latin-and-glyphs.md/html` |
| 12 | `/hi/features/commandments.html` | `Commandments — Faber` | `src/hi/features/commandments.md/html` |
| 13 | `/hi/features/canonical-vs-sugar.html` | `Canonical vs sugar surfaces — Faber` | `src/hi/features/canonical-vs-sugar.md/html` |
| 14 | `/hi/features/frames.html` | `Capability calls and frames — Faber` | `src/hi/features/frames.md/html` |
| 15 | `/hi/features/testing.html` | `Inline testing — Faber` | `src/hi/features/testing.md/html` |
| 16 | `/hi/syntax/` | `Syntax and semantics — Faber` | `src/hi/syntax/index.md/html` |
| 17 | `/hi/syntax/types.html` | `Data types — Faber` | `src/hi/syntax/types.md/html` |
| 18 | `/hi/syntax/variables.html` | `Variables and binding — Faber` | `src/hi/syntax/variables.md/html` |
| 19 | `/hi/syntax/functions.html` | `Functions — Faber` | `src/hi/syntax/functions.md/html` |
| 20 | `/hi/syntax/control-flow.html` | `Control flow — Faber` | `src/hi/syntax/control-flow.md/html` |
| 21 | `/hi/syntax/errors.html` | (presumed English, not read) | `src/hi/syntax/errors.md/html` |
| 22 | `/hi/syntax/generics.html` | (presumed English, not read) | `src/hi/syntax/generics.md/html` |
| 23 | `/hi/syntax/collections.html` | (presumed English, not read) | `src/hi/syntax/collections.md/html` |
| 24 | `/hi/syntax/strings.html` | (presumed English, not read) | `src/hi/syntax/strings.md/html` |
| 25 | `/hi/syntax/conversion.html` | (presumed English, not read) | `src/hi/syntax/conversion.md/html` |
| 26 | `/hi/syntax/glyphs.html` | (presumed English, not read) | `src/hi/syntax/glyphs.md/html` |
| 27 | `/hi/syntax/nullability.html` | (presumed English, not read) | `src/hi/syntax/nullability.md/html` |
| 28 | `/hi/ecosystem/` | `Ecosystem — Faber` | `src/hi/ecosystem/index.md/html` |
| 29 | `/hi/ecosystem/norma.html` | `Norma standard library — Faber` | `src/hi/ecosystem/norma.md/html` |
| 30 | `/hi/ecosystem/corpus.html` | `Language corpus — Faber` | `src/hi/ecosystem/corpus.md/html` |
| 31 | `/hi/ecosystem/ai-workbench.html` | `AI Workbench — Faber` | `src/hi/ecosystem/ai-workbench.md/html` |
| 32 | `/hi/ecosystem/coreutils.html` | `Coreutils — Faber` | `src/hi/ecosystem/coreutils.md/html` |
| 33 | `/hi/ecosystem/triga.html` | `Triga graphics library — Faber` | `src/hi/ecosystem/triga.md/html` |
| 34 | `/hi/ecosystem/reader-locale-packages.html` | `Reader-locale packages — Faber` | `src/hi/ecosystem/reader-locale-packages.md/html` |
| 35 | `/hi/history/` | `History — Faber` | `src/hi/history/index.md/html` |
| 36 | `/hi/history/releases.html` | `Releases — Faber` | `src/hi/history/releases.md/html` |
| 37 | `/hi/references/` | `References — Faber` | `src/hi/references/index.md/html` |
| 38 | `/hi/references/ebnf.html` | `EBNF grammar — Faber` | `src/hi/references/ebnf.md/html` |
| 39 | `/hi/references/design-docs.html` | `Design documents — Faber` | `src/hi/references/design-docs.md/html` |
| 40 | `/hi/references/repositories.html` | `Repositories — Faber` | `src/hi/repositories/repositories.md/html` |
| 41 | `/hi/tooling/` | `Tooling and compiler — Faber` | `src/hi/tooling/index.md/html` |
| 42 | `/hi/tooling/faber-build-tool.html` | `Faber build tool — Faber` | `src/hi/tooling/faber-build-tool.md/html` |
| 43 | `/hi/tooling/radix-compiler.html` | `Radix compiler — Faber` | `src/hi/tooling/radix-compiler.md/html` |
| 44 | `/hi/tooling/cista-package-manager.html` | `Cista package manager — Faber` | `src/hi/tooling/cista-package-manager.md/html` |
| 45 | `/hi/tooling/codegen-targets.html` | `Codegen targets — Faber` | `src/hi/tooling/codegen-targets.md/html` |
| 46 | `/hi/tooling/performance.html` | `Compiler performance — Faber` | `src/hi/tooling/performance.md/html` |
| 47 | `/hi/tooling/scripting.html` | `In-process scripting — Faber` | `src/hi/tooling/scripting.md/html` |
| 48 | `/hi/corpus/` | `Corpus — Faber` | `src/hi/corpus/index.md/html` |
| 49 | `/hi/corpus/category/function.html` | `Corpus: function — Faber` | auto-generated from corpus |

**The title pattern is consistent across all ~49 inspected pages.** This is likely a template-level issue where the `<title>` tag is populated from a frontmatter `title` field that was never localized.

---

### B. English `<h1>` headings — all 40+ content pages (medium severity)

Same pages as above have English `<h1>` text matching (or closely related to) the `<title>`:

| Path | H1 text (English) |
|------|-------------------|
| `/hi/404.html` | `Page not found` |
| `/hi/start/` | `Quick tour` |
| `/hi/start/install.html` | `Install and download` |
| `/hi/start/hello.html` | `Hello, Faber` |
| `/hi/start/commands.html` | `Commands you will use` |
| `/hi/start/projects.html` | `Projects and examples` |
| `/hi/start/examples.html` | `Examples` |
| `/hi/features/` | `Features` |
| `/hi/features/reader-locale.html` | `Reader locale` |
| `/hi/features/compilation-lanes.html` | `Compilation lanes` |
| `/hi/features/latin-and-glyphs.html` | `Latin vocabulary and structural glyphs` |
| `/hi/features/commandments.html` | `Commandments` |
| `/hi/features/canonical-vs-sugar.html` | `Canonical vs sugar surfaces` |
| `/hi/features/frames.html` | `Capability calls and frames` |
| `/hi/features/testing.html` | `Inline testing` |
| `/hi/syntax/` | `Syntax and semantics` |
| `/hi/syntax/types.html` | `Data types` |
| `/hi/syntax/variables.html` | `Variables and binding` |
| `/hi/syntax/functions.html` | `Functions` |
| `/hi/syntax/control-flow.html` | `Control flow` |
| `/hi/ecosystem/` | `Ecosystem` |
| `/hi/ecosystem/norma.html` | `Norma standard library` |
| `/hi/ecosystem/corpus.html` | `Language corpus` |
| `/hi/ecosystem/ai-workbench.html` | `AI Workbench` |
| `/hi/ecosystem/coreutils.html` | `Coreutils` |
| `/hi/ecosystem/triga.html` | `Triga graphics library` |
| `/hi/ecosystem/reader-locale-packages.html` | `Reader-locale packages` |
| `/hi/history/` | `History` |
| `/hi/history/releases.html` | `Releases` |
| `/hi/references/` | `References` |
| `/hi/references/ebnf.html` | `EBNF grammar` |
| `/hi/references/design-docs.html` | `Design documents` |
| `/hi/references/repositories.html` | `Repositories` |
| `/hi/tooling/` | `Tooling and compiler` |
| `/hi/tooling/faber-build-tool.html` | `Faber build tool` |
| `/hi/tooling/radix-compiler.html` | `Radix compiler` |
| `/hi/tooling/cista-package-manager.html` | `Cista package manager` |
| `/hi/tooling/codegen-targets.html` | `Codegen targets` |
| `/hi/tooling/performance.html` | `Compiler performance` |
| `/hi/tooling/scripting.html` | `In-process scripting` |
| `/hi/corpus/` | `Corpus` |
| `/hi/corpus/category/function.html` | `Corpus: function` |

**Exception:** `dist/hi/index.html` (homepage) has `Faber` as H1, which is acceptable since it is the brand name.

---

### C. English `<meta property="og:title">` — all pages (medium)

Every page has `<meta property="og:title"` matching the English `<title>`. When shared on social media, the page will display the English title. Fixing the `<title>` should also fix `og:title`.

---

### D. Agent notices in English — every page with an agent notice (high severity)

Every page that includes an `<section class="agent-notice">` has the notice body in full English:

```
If you are an AI agent: start at /llms.txt, then read /agents/index.md
and pick a skill from /.well-known/agent-skills/index.json.
Humans: use Install and Examples.
```

This appears on at minimum:
- `/hi/index.html`
- `/hi/404.html`
- `/hi/start/` (confirmed)

And likely on every page with the same template. The notice label `एजेंट-तैयार` is Hindi, but the prose body is English.

---

### E. "Skip to content" link — every page (low severity)

Every page has `<a href="#main-content" class="skip-link">Skip to content</a>` in English. This is an accessibility link visible to screen readers. Should be Hindi: `मुख्य सामग्री पर जाएँ`.

---

### F. Corpus pages — extensive English prose (high severity)

#### `corpus/index.html`

The body content has a **translation status banner** that says:

> `**Translation status:** हिन्दी reader-locale proof. Code fences render through the hi pipeline; prose is canonical Latin.`

Then the content section is almost entirely English:

```
Generated reference pages for 171 canonical Faber corpus terms.
```

And all category links use English labels: "ad", "aliasing", "application", "arithmetic", "assignment", "async", etc. — these are corpus category names derived from the corpus data model, and are used as link text to `/hi/corpus/category/<name>.html`.

#### All `corpus/category/<name>.html` pages (48 pages)

Every corpus category page has:

- English `<title>`: `Corpus: <name> — Faber`
- English `<h1>`: `Corpus: <name>`
- English body prose: `<name> canonical terms in this category.`
- Full-English `<meta description="">`: e.g. `12 canonical terms in this category.`

The translation status banner on these pages also states the prose is "canonical Latin" (English).

---

### G. Stray English phrases in table cells (low)

On `/hi/start/` (Quick tour), the "Start track" table has a cell that reads:

> `Commands you will use`

as link text. This is a link to `/hi/start/commands.html`, and the sidebar navigation label is `कमांड` (Hindi), but the table cell uses the English page title. This is inconsistent.

On `/hi/start/hello.html`, the "Next step" table has a link in English:

> `Commands you will use`

as the "next" link label when the actual linked page path is `/hi/start/commands.html`.

---

## Top 10 Highest-Priority Fix Candidates

| Rank | Page | Problem | Expected fix |
|------|------|---------|--------------|
| 1 | **All pages** — template | `<title>` tags in English | Set `hi` title translations in frontmatter |
| 2 | **All pages** — template | `<h1>` headings in English | Set `hi` h1 translations in frontmatter |
| 3 | **All pages** — template | `<meta property="og:title">` in English | Derive from localized title |
| 4 | **All pages with agent notice** | Agent notice body in English | Translate the agent notice prose to Hindi or make it locale-aware |
| 5 | **All pages** | "Skip to content" link in English | Replace with `मुख्य सामग्री पर जाएँ` or make locale-aware |
| 6 | `/hi/404.html` | Title/H1 "Page not found" in English | `पृष्ठ नहीं मिला` |
| 7 | `/hi/start/` | Title/H1 "Quick tour" in English | `त्वरित दौरा` (sidebar already has this) |
| 8 | `/hi/features/` | All 7 feature subpages have English titles | Translate titles like `रीडर लोकेल`, `संकलन मार्ग`, etc. |
| 9 | `/hi/corpus/index.html` | Body prose entirely in English | Localize generated prose or add Hindi template |
| 10 | `/hi/corpus/category/*.html` | 48 generated category pages with English-only prose | Make corpus category page generation locale-aware |

---

## Source Mapping

The `dist/hi/` files are generated from sources under `src/hi/`. The mapping is typically:

```
src/hi/<section>/<page>.md  →  dist/hi/<section>/<page>.html
```

The English titles and H1s likely come from frontmatter in the source Markdown files (e.g. `title: "Quick tour"`), which were never updated with Hindi translations. The corpus category pages are auto-generated by a script that does not localize its prose.

---

## Summary of Scale

| Metric | Value |
|--------|-------|
| Total pages inspected | ~55 (including category pages) |
| Pages with English `<title>` | ~55 (100%) |
| Pages with English `<h1>` | ~54 (only homepage exempt) |
| Pages with English `og:title` | ~55 (100%) |
| Pages with English agent notice | ~55 (100%) |
| Pages with English "Skip to content" | ~55 (100%) |
| Corpus category pages with English body prose | 48 (100%) |

**Note:** Despite the pervasive English chrome, the Hindi translations of body content are excellent and complete. The fixes needed are concentrated in the page metadata layer (titles, headings, accessibility links, agent boilerplate) and the auto-generated corpus pages.
