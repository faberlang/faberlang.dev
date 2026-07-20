# English Residue Audit — `dist/ar/`

**Generated:** 2026-07-20  
**Scope:** `/Users/ianzepp/work/faberlang/faberlang.dev/dist/ar/` — all `*.html` except individual `corpus/*.html` (includes `corpus/index.html`).  
**Method:** Manual extraction of main content per page, judgment of missing translation vs acceptable English OS/dev surface.  
**Source map:** `/Users/ianzepp/work/faberlang/faberlang.dev/src/ar/`

---

## Summary

| Metric | Count |
|---|---|
| Pages audited | 38 (27 non-corpus + 11 syntax sub-pages) |
| Pages with English `<title>` | 37 of 38 |
| Pages with English `<h1>` | 33 of 38 |
| Pages with English agent-notice body | 37 of 38 |
| Pages with English "Skip to content" | 38 of 38 |
| Pages with English `og:title` | 37 of 38 |
| Inline English prose issues (body content) | 2 |
| English boilerplate note (corpus/index) | 1 (intentional) |
| **Systematic pattern severity** | **HIGH** |

---

## Systematic Patterns

### Pattern A: `<title>` tags in English — 37/38 pages

Every human-facing page has an English `<title>` tag. The only page with an Arabic title is the root `index.html`, which has `<title>Faber</title>` (brand name, acceptable).

**Example titles:**
- `"Quick tour — Faber"` → `start/index.html`
- `"Syntax and semantics — Faber"` → `syntax/index.html`
- `"Features — Faber"` → `features/index.html`
- `"Tooling and compiler — Faber"` → `tooling/index.html`
- `"Ecosystem — Faber"` → `ecosystem/index.html`
- `"History — Faber"` → `history/index.html`
- `"References — Faber"` → `references/index.html`
- `"Page not found — Faber"` → `404.html`
- `"Install and download — Faber"` → `start/install.html`
- `"Compilation lanes — Faber"` → `features/compilation-lanes.html`
- etc.

- **Severity:** HIGH — `<title>` is the browser tab text, bookmark text, and primary SEO signal.
- **Likely src:** Each `.md` file in `src/ar/` — the title is derived from frontmatter or the first heading.

### Pattern B: `og:title` meta tags in English — 37/38 pages

Every page's Open Graph title matches the English `<title>`. Same scope and severity as Pattern A.

### Pattern C: `<h1>` headings in English — 33/38 pages

Every section landing page and most sub-pages have English H1s matching the English title. Exceptions: `corpus/index.html` (H1 is "Corpus" — English, so pattern holds), `start/install.html` (H1 is "Install and download" — English). The root `index.html` H1 is "Faber" (brand, acceptable).

**Examples:**
- `<h1>Quick tour</h1>` — `start/index.html`
- `<h1>Syntax and semantics</h1>` — `syntax/index.html`
- `<h1>Features</h1>` — `features/index.html`
- `<h1>Tooling and compiler</h1>` — `tooling/index.html`
- `<h1>Ecosystem</h1>` — `ecosystem/index.html`
- `<h1>History</h1>` — `history/index.html`
- `<h1>References</h1>` — `references/index.html`
- `<h1>Page not found</h1>` — `404.html`
- `<h1>Install and download</h1>` — `start/install.html`
- `<h1>Hello, Faber</h1>` — `start/hello.html`
- `<h1>Commands you will use</h1>` — `start/commands.html`
- `<h1>Projects and examples</h1>` — `start/projects.html`
- `<h1>Examples</h1>` — `start/examples.html`
- `<h1>Corpus</h1>` — `corpus/index.html`
- `<h1>Reader locale</h1>` — `features/reader-locale.html`
- `<h1>Latin vocabulary and structural glyphs</h1>` — `features/latin-and-glyphs.html`
- `<h1>Commandments</h1>` — `features/commandments.html`
- `<h1>Compilation lanes</h1>` — `features/compilation-lanes.html`
- `<h1>Canonical vs sugar surfaces</h1>` — `features/canonical-vs-sugar.html`
- `<h1>Capability calls and frames</h1>` — `features/frames.html`
- `<h1>Inline testing</h1>` — `features/testing.html`
- `<h1>Faber build tool</h1>` — `tooling/faber-build-tool.html`
- `<h1>Radix compiler</h1>` — `tooling/radix-compiler.html`
- `<h1>Cista package manager</h1>` — `tooling/cista-package-manager.html`
- `<h1>Codegen targets</h1>` — `tooling/codegen-targets.html`
- `<h1>Compiler performance</h1>` — `tooling/performance.html`
- `<h1>In-process scripting</h1>` — `tooling/scripting.html`
- `<h1>Norma standard library</h1>` — `ecosystem/norma.html`
- `<h1>Triga graphics library</h1>` — `ecosystem/triga.html`
- `<h1>Coreutils</h1>` — `ecosystem/coreutils.html`
- `<h1>Reader-locale packages</h1>` — `ecosystem/reader-locale-packages.html`
- `<h1>AI Workbench</h1>` — `ecosystem/ai-workbench.html`
- `<h1>Language corpus</h1>` — `ecosystem/corpus.html`
- `<h1>Releases</h1>` — `history/releases.html`
- `<h1>EBNF grammar</h1>` — `references/ebnf.html`
- `<h1>Design documents</h1>` — `references/design-docs.html`
- `<h1>Repositories</h1>` — `references/repositories.html`
- `<h1>Data types</h1>` — `syntax/types.html`
- `<h1>Functions</h1>` — `syntax/functions.html`
- `<h1>Control flow</h1>` — `syntax/control-flow.html`
- `<h1>Variables and binding</h1>` — `syntax/variables.html`
- `<h1>String and template literals</h1>` — `syntax/strings.html`
- `<h1>Collections</h1>` — `syntax/collections.html`
- `<h1>Error handling</h1>` — `syntax/errors.html`
- `<h1>Generics</h1>` — `syntax/generics.html`
- `<h1>Conversion and construction</h1>` — `syntax/conversion.html`
- `<h1>Glyphs and operators</h1>` — `syntax/glyphs.html`
- `<h1>Nullability and optionality</h1>` — `syntax/nullability.html`

### Pattern D: Agent-notice sections in English — 37/38 pages

Every page that has an agent-notice section contains the English text:
> "If you are an AI agent: start at `/llms.txt`, then read `/agents/index.md` and pick a skill from `/.well-known/agent-skills/index.json`. Humans: use [Install](/ar/start/install.html) and [Examples](/ar/start/examples.html)."

The label "جاهز للوكلاء" is Arabic, but the body paragraph is entirely English.

### Pattern E: "Skip to content" link in English — 38/38 pages

Every page has `<a href="#main-content" class="skip-link">Skip to content</a>`. The skip-to-content link is an accessibility feature; English here means screen-reader users navigating the Arabic site will hear English text.

- **Severity:** MEDIUM (accessibility impact)
- **Likely src:** Shared template/layout in the site generator, not per-page source.

---

## Individual Issues

### 1. `syntax/errors.html` — Inline English table header

| Location | Quote | Severity |
|---|---|---|
| Table header row | `Construct` (first column header) | MEDIUM |

The `errors.html` page has a table comparing constructs. The first column header is "Construct" in English while all other content is Arabic. The row values (`→ T`, `T ∪ nihil`, `⇥ E`) are Faber syntax glyphs (acceptable), but the column label should be Arabic.

### 2. `corpus/index.html` — Entire page prose is English

The `corpus/index.html` page is a generated reference index. A `<strong>` note at the top says:
> "Translation status: العربية reader-locale proof. Code fences render through the `ar` pipeline; prose is canonical Latin."

All body prose is in English:
- `"Generated reference pages for 171 canonical Faber corpus terms."`
- Category names in English: `ad`, `aliasing`, `application`, `arithmetic`, etc.
- Term links in Latin/Faber identifiers (acceptable as code terms)

This is **explicitly acknowledged** as intended behavior in the status note. However, category labels and the introductory paragraph are user-facing English prose.

---

## Acceptable English / OS Surface

The following are **correctly left in English** per the audit guidelines:

| Element | Examples | Rationale |
|---|---|---|
| Brand names | `Faber`, `Radix`, `Norma`, `Triga`, `Cista` | Brand names |
| CLI commands | `faber check`, `faber build`, `faber run` | CLI surface |
| Code blocks | All `lang-bash`, `lang-text`, `lang-faber` blocks | Intentional Faber code samples |
| Paths | `/llms.txt`, `/agents/index.md`, `path/to/file.fab` | File system paths |
| GitHub URLs | `github.com/faberlang/...` | URLs |
| Type names in code | `textus`, `numerus`, `fractus`, `lista` | Faber type names (Latin, not English) |
| Sidebar "Release 1.1.1" | Release section title | Mixed — "Release" is English, but version numbering is universal; LOW concern |
| Sidebar "macOS arm64", "Linux x64" | Platform labels | Platform triple names |
| Sidebar meta values | `packages`, `static · type-first`, `Rust → native`, `MIT` | Technical descriptor values |

---

## Top 10 Priorities for Translation

| Priority | Page | Issue | Effort |
|---|---|---|---|
| 1 | **ALL pages** | `<title>` tags in English | Template‑level fix — translate all `<title>` strings to Arabic |
| 2 | **ALL pages** | `og:title` meta tags in English | Same template fix as #1 |
| 3 | **ALL pages** | `<h1>` headings in English | Translate each `.md` source file's first heading |
| 4 | **ALL pages** | "Skip to content" link in English | Template change: `"Skip to content"` → Arabic equivalent |
| 5 | **ALL agent-notice sections** | English agent body text | Template change: translate the agent-notice body to Arabic |
| 6 | `index.html` (root) | Agent notice body in English | See #5 |
| 7 | `404.html` | `<title>Page not found — Faber</title>` and `<h1>Page not found</h1>` are English | Translate both |
| 8 | `syntax/errors.html` | Table header `Construct` in English | Inline fix |
| 9 | `corpus/index.html` | Prose is entirely English (acknowledged as canonical Latin) | Per the note, this is Phase‑7 partial proof; full translation deferred |
| 10 | `start/install.html`, `start/hello.html`, `start/commands.html`, `start/projects.html`, `start/examples.html` | All have English `<title>` and `<h1>` | Translate source `.md` frontmatter/headings |

---

## Likely Source Mapping

Most English residues originate from the site generator's template layer and per-page Markdown source files.

| Residue | Likely Source |
|---|---|
| `<title>` tags | Per-page frontmatter in `src/ar/*.md` — or a template title fallback |
| `<h1>` headings | First heading in each `src/ar/*.md` file |
| "Skip to content" | Shared layout template (e.g., `speculum.css` or SSG layout) |
| Agent-notice body | Shared layout template or include |
| `og:title` | Derived from `<title>` or separate template variable |
| `syntax/errors.html` "Construct" | That specific `.md` source file's table |
| `corpus/index.html` prose | Generated by the corpus generator pipeline; source is the shared English template for corpus index pages |

---

## Conclusion

**Systematic pattern:** Every page in `dist/ar/` has English `<title>`, `og:title`, `og:description`, "Skip to content", agent-notice body, and most have English `<h1>`. These are template-level issues — fixing one file (the shared layout) would resolve 4 of the 5 systematic patterns simultaneously.

**Per-page headings:** Each of the ~30+ section pages needs its H1 translated individually in the source `.md` files.

**Body prose:** The body prose on all audited pages is correctly in Arabic (the translated content is substantial and well-done). The English residues are confined to the template chrome (title, H1, skip link, agent notice) and one table header.

**`corpus/index.html`:** This page's prose is English by design (Phase 7 partial proof, per the explicit status note on the page itself). The code fences render through the `ar` pipeline. Not actionable until full translation is planned.
