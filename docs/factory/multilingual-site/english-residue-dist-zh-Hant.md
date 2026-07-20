# English Residue Audit — dist/zh-Hant/

**Generated:** 2026-07-20

**Scope:** All `*.html` in `dist/zh-Hant/` except individual corpus pages (corpus/index.html included). 49 non-corpus pages + 404 + index + corpus/index.html audited.

**Source root:** `src/zh-Hant/*.md`

---

## Summary

All 49 generated pages contain English residue. Three categories:

| Category | Affected pages | Root cause |
|---|---|---|
| Global: `Skip to content` | All 49 pages | Template default (`speculum.css` framework) |
| Global: `<title>` / `<h1>` / `og:title` | All 49 content pages | `title` frontmatter field in `src/zh-Hant/*.md` is English, never localized |
| Agent-notice paragraph | `index.html`, `404.html` | Inline English prose in template/content |

Corpus index also has English `description`/`og:description` and prose body (`"Generated reference pages for 171 canonical Faber corpus terms."`), which is self-declared canonical Latin per its own status note.

---

## Findings Table

### Global: All 49 Pages

| Field | English text | Location |
|---|---|---|
| `class="skip-link"` | `Skip to content` | All pages — accessibility skip link |
| `og:title` | English page title + ` — Faber` | All pages — Open Graph meta tag |
| `<title>` | English page title + ` — Faber` | All pages — browser title bar |
| `<h1>` | English page heading | All pages — top-level heading |

---

### Page-by-Page

#### 404.html
| Element | English residue | Suggested Traditional Chinese |
|---|---|---|
| `<title>` | `Page not found — Faber` | `找不到頁面 — Faber` |
| `<h1>` | `Page not found` | `找不到頁面` |
| `<og:title>` | `Page not found — Faber` | `找不到頁面 — Faber` |
| agent-notice | `If you are an AI agent: start at /llms.txt... Humans: use Install and Examples.` | 整段需譯為繁中 |
| skip-link | `Skip to content` | `跳至內容` |

#### index.html
| Element | English residue | Suggested Traditional Chinese |
|---|---|---|
| agent-notice | `If you are an AI agent: start at /llms.txt... Humans: use Install and Examples.` | 整段需譯為繁中 |
| skip-link | `Skip to content` | `跳至內容` |

#### start/install.html
| Element | English residue |
|---|---|
| `<title>` | `Install and download — Faber` |
| `<h1>` | `Install and download` |
| `og:title` | `Install and download — Faber` |
| skip-link | `Skip to content` |

#### start/commands.html
| Element | English residue |
|---|---|
| `<title>` | `Commands you will use — Faber` |
| `<h1>` | `Commands you will use` |
| `og:title` | `Commands you will use — Faber` |
| skip-link | `Skip to content` |

#### start/examples.html
| Element | English residue |
|---|---|
| `<title>` | `Examples — Faber` |
| `<h1>` | `Examples` |
| `og:title` | `Examples — Faber` |
| skip-link | `Skip to content` |

#### start/hello.html
| Element | English residue |
|---|---|
| `<title>` | `Hello, Faber — Faber` |
| `<h1>` | `Hello, Faber` |
| `og:title` | `Hello, Faber — Faber` |
| skip-link | `Skip to content` |

#### start/index.html
| Element | English residue |
|---|---|
| `<title>` | `Quick tour — Faber` |
| `<h1>` | `Quick tour` |
| `og:title` | `Quick tour — Faber` |
| skip-link | `Skip to content` |

#### start/projects.html
| Element | English residue |
|---|---|
| `<title>` | `Projects and examples — Faber` |
| `<h1>` | `Projects and examples` |
| `og:title` | `Projects and examples — Faber` |
| skip-link | `Skip to content` |

#### features/index.html
| Element | English residue |
|---|---|
| `<title>` | `Features — Faber` |
| `<h1>` | `Features` |
| `og:title` | `Features — Faber` |
| skip-link | `Skip to content` |

#### features/commandments.html
| Element | English residue |
|---|---|
| `<title>` | `Commandments — Faber` |
| `<h1>` | `Commandments` |
| `og:title` | `Commandments — Faber` |
| skip-link | `Skip to content` |

#### features/canonical-vs-sugar.html
| Element | English residue |
|---|---|
| `<title>` | `Canonical vs sugar surfaces — Faber` |
| `<h1>` | `Canonical vs sugar surfaces` |
| `og:title` | `Canonical vs sugar surfaces — Faber` |
| skip-link | `Skip to content` |

#### features/compilation-lanes.html
| Element | English residue |
|---|---|
| `<title>` | `Compilation lanes — Faber` |
| `<h1>` | `Compilation lanes` |
| `og:title` | `Compilation lanes — Faber` |
| skip-link | `Skip to content` |

#### features/frames.html
| Element | English residue |
|---|---|
| `<title>` | `Capability calls and frames — Faber` |
| `<h1>` | `Capability calls and frames` |
| `og:title` | `Capability calls and frames — Faber` |
| skip-link | `Skip to content` |

#### features/latin-and-glyphs.html
| Element | English residue |
|---|---|
| `<title>` | `Latin vocabulary and structural glyphs — Faber` |
| `<h1>` | `Latin vocabulary and structural glyphs` |
| `og:title` | `Latin vocabulary and structural glyphs — Faber` |
| skip-link | `Skip to content` |

#### features/reader-locale.html
| Element | English residue |
|---|---|
| `<title>` | `Reader locale — Faber` |
| `<h1>` | `Reader locale` |
| `og:title` | `Reader locale — Faber` |
| skip-link | `Skip to content` |

#### features/testing.html
| Element | English residue |
|---|---|
| `<title>` | `Inline testing — Faber` |
| `<h1>` | `Inline testing` |
| `og:title` | `Inline testing — Faber` |
| skip-link | `Skip to content` |

#### syntax/index.html
| Element | English residue |
|---|---|
| `<title>` | `Syntax and semantics — Faber` |
| `<h1>` | `Syntax and semantics` |
| `og:title` | `Syntax and semantics — Faber` |
| skip-link | `Skip to content` |

#### syntax/collections.html
| Element | English residue |
|---|---|
| `<title>` | `Collections — Faber` |
| `<h1>` | `Collections` |
| `og:title` | `Collections — Faber` |
| skip-link | `Skip to content` |

#### syntax/control-flow.html
| Element | English residue |
|---|---|
| `<title>` | `Control flow — Faber` |
| `<h1>` | `Control flow` |
| `og:title` | `Control flow — Faber` |
| skip-link | `Skip to content` |

#### syntax/conversion.html
| Element | English residue |
|---|---|
| `<title>` | `Conversion and construction — Faber` |
| `<h1>` | `Conversion and construction` |
| `og:title` | `Conversion and construction — Faber` |
| skip-link | `Skip to content` |

#### syntax/errors.html
| Element | English residue |
|---|---|
| `<title>` | `Error handling — Faber` |
| `<h1>` | `Error handling` |
| `og:title` | `Error handling — Faber` |
| skip-link | `Skip to content` |

#### syntax/functions.html
| Element | English residue |
|---|---|
| `<title>` | `Functions — Faber` |
| `<h1>` | `Functions` |
| `og:title` | `Functions — Faber` |
| skip-link | `Skip to content` |

#### syntax/generics.html
| Element | English residue |
|---|---|
| `<title>` | `Generics — Faber` |
| `<h1>` | `Generics` |
| `og:title` | `Generics — Faber` |
| skip-link | `Skip to content` |

#### syntax/glyphs.html
| Element | English residue |
|---|---|
| `<title>` | `Glyphs and operators — Faber` |
| `<h1>` | `Glyphs and operators` |
| `og:title` | `Glyphs and operators — Faber` |
| skip-link | `Skip to content` |

#### syntax/nullability.html
| Element | English residue |
|---|---|
| `<title>` | `Nullability and optionality — Faber` |
| `<h1>` | `Nullability and optionality` |
| `og:title` | `Nullability and optionality — Faber` |
| skip-link | `Skip to content` |

#### syntax/strings.html
| Element | English residue |
|---|---|
| `<title>` | `String and template literals — Faber` |
| `<h1>` | `String and template literals` |
| `og:title` | `String and template literals — Faber` |
| skip-link | `Skip to content` |

#### syntax/types.html
| Element | English residue |
|---|---|
| `<title>` | `Data types — Faber` |
| `<h1>` | `Data types` |
| `og:title` | `Data types — Faber` |
| skip-link | `Skip to content` |

#### syntax/variables.html
| Element | English residue |
|---|---|
| `<title>` | `Variables and binding — Faber` |
| `<h1>` | `Variables and binding` |
| `og:title` | `Variables and binding — Faber` |
| skip-link | `Skip to content` |

#### tooling/index.html
| Element | English residue |
|---|---|
| `<title>` | `Tooling and compiler — Faber` |
| `<h1>` | `Tooling and compiler` |
| `og:title` | `Tooling and compiler — Faber` |
| skip-link | `Skip to content` |

#### tooling/cista-package-manager.html
| Element | English residue |
|---|---|
| `<title>` | `Cista package manager — Faber` |
| `<h1>` | `Cista package manager` |
| `og:title` | `Cista package manager — Faber` |
| skip-link | `Skip to content` |

#### tooling/codegen-targets.html
| Element | English residue |
|---|---|
| `<title>` | `Codegen targets — Faber` |
| `<h1>` | `Codegen targets` |
| `og:title` | `Codegen targets — Faber` |
| skip-link | `Skip to content` |

#### tooling/faber-build-tool.html
| Element | English residue |
|---|---|
| `<title>` | `Faber build tool — Faber` |
| `<h1>` | `Faber build tool` |
| `og:title` | `Faber build tool — Faber` |
| skip-link | `Skip to content` |

#### tooling/performance.html
| Element | English residue |
|---|---|
| `<title>` | `Compiler performance — Faber` |
| `<h1>` | `Compiler performance` |
| `og:title` | `Compiler performance — Faber` |
| skip-link | `Skip to content` |

#### tooling/radix-compiler.html
| Element | English residue |
|---|---|
| `<title>` | `Radix compiler — Faber` |
| `<h1>` | `Radix compiler` |
| `og:title` | `Radix compiler — Faber` |
| skip-link | `Skip to content` |

#### tooling/scripting.html
| Element | English residue |
|---|---|
| `<title>` | `In-process scripting — Faber` |
| `<h1>` | `In-process scripting` |
| `og:title` | `In-process scripting — Faber` |
| skip-link | `Skip to content` |

#### ecosystem/index.html
| Element | English residue |
|---|---|
| `<title>` | `Ecosystem — Faber` |
| `<h1>` | `Ecosystem` |
| `og:title` | `Ecosystem — Faber` |
| skip-link | `Skip to content` |

#### ecosystem/ai-workbench.html
| Element | English residue |
|---|---|
| `<title>` | `AI Workbench — Faber` |
| `<h1>` | `AI Workbench` |
| `og:title` | `AI Workbench — Faber` |
| skip-link | `Skip to content` |

#### ecosystem/coreutils.html
| Element | English residue |
|---|---|
| `<title>` | `Coreutils — Faber` |
| `<h1>` | `Coreutils` |
| `og:title` | `Coreutils — Faber` |
| skip-link | `Skip to content` |

#### ecosystem/corpus.html
| Element | English residue |
|---|---|
| `<title>` | `Language corpus — Faber` |
| `<h1>` | `Language corpus` |
| `og:title` | `Language corpus — Faber` |
| skip-link | `Skip to content` |

#### ecosystem/norma.html
| Element | English residue |
|---|---|
| `<title>` | `Norma standard library — Faber` |
| `<h1>` | `Norma standard library` |
| `og:title` | `Norma standard library — Faber` |
| skip-link | `Skip to content` |

#### ecosystem/reader-locale-packages.html
| Element | English residue |
|---|---|
| `<title>` | `Reader locale packages — Faber` |
| `<h1>` | `Reader locale packages` |
| `og:title` | `Reader locale packages — Faber` |
| skip-link | `Skip to content` |

#### ecosystem/triga.html
| Element | English residue |
|---|---|
| `<title>` | `Triga graphics library — Faber` |
| `<h1>` | `Triga graphics library` |
| `og:title` | `Triga graphics library — Faber` |
| skip-link | `Skip to content` |

#### history/index.html
| Element | English residue |
|---|---|
| `<title>` | `History — Faber` |
| `<h1>` | `History` |
| `og:title` | `History — Faber` |
| skip-link | `Skip to content` |

#### history/releases.html
| Element | English residue |
|---|---|
| `<title>` | `Releases — Faber` |
| `<h1>` | `Releases` |
| `og:title` | `Releases — Faber` |
| skip-link | `Skip to content` |

#### references/index.html
| Element | English residue |
|---|---|
| `<title>` | `References — Faber` |
| `<h1>` | `References` |
| `og:title` | `References — Faber` |
| skip-link | `Skip to content` |

#### references/design-docs.html
| Element | English residue |
|---|---|
| `<title>` | `Design documents — Faber` |
| `<h1>` | `Design documents` |
| `og:title` | `Design documents — Faber` |
| skip-link | `Skip to content` |

#### references/ebnf.html
| Element | English residue |
|---|---|
| `<title>` | `EBNF grammar — Faber` |
| `<h1>` | `EBNF grammar` |
| `og:title` | `EBNF grammar — Faber` |
| skip-link | `Skip to content` |

#### references/repositories.html
| Element | English residue |
|---|---|
| `<title>` | `Repositories — Faber` |
| `<h1>` | `Repositories` |
| `og:title` | `Repositories — Faber` |
| skip-link | `Skip to content` |

#### corpus/index.html
| Element | English residue | Notes |
|---|---|---|
| `<meta description>` | `Generated reference pages for 171 canonical Faber corpus terms.` | Declared canonical Latin |
| `<og:description>` | `Generated reference pages for 171 canonical Faber corpus terms.` | Declared canonical Latin |
| `<title>` | `Corpus — Faber` | Should be localized |
| `<h1>` | `Corpus` | Should be localized |
| prose body | `Generated reference pages for 171 canonical Faber corpus terms.` | Declared canonical Latin |
| skip-link | `Skip to content` | Should be localized |

---

## Likely Source

The root cause is in the source Markdown files at `src/zh-Hant/*.md`. Each file has frontmatter with a `title` field that was never localized. Example (`src/zh-Hant/start/install.md`):

```toml
+++
translation_kind = "translated"

title = "Install and download"    # ← English, never localized
section = "install"
order = 1
sources = []
+++
```

The generator emits this `title` value into three places in the rendered HTML:
1. `<title>` browser title
2. `<h1>` page heading
3. `og:title` Open Graph meta tag

The `Skip to content` string is a static template default, likely in the site layout/system. The agent-notice English paragraph on `index.html` and `404.html` is inline prose that was never translated.

---

## Top 10 Most Visible Issues

1. **`Skip to content`** — appears on all 49 pages; accessibility text, most visible to screen-reader users
2. **`index.html` agent-notice** — home page, first impression; entire paragraph in English
3. **`404.html` `<title>`** — `"Page not found — Faber"` — browser title when page is missing
4. **`404.html` `<h1>`** — `"Page not found"` — main heading on error page
5. **`404.html` agent-notice** — same English paragraph as index.html
6. **`syntax/index.html` `<title>`** — `"Syntax and semantics — Faber"` — top-level syntax landing page
7. **`features/index.html` `<title>`** — `"Features — Faber"` — top-level features landing page
8. **`start/install.html` `<title>`** — `"Install and download — Faber"` — primary download page
9. **`start/index.html` `<title>`** — `"Quick tour — Faber"` — getting-started landing page
10. **`corpus/index.html` `<title>`** — `"Corpus — Faber"` — corpus landing page

---

## Notes

- **OK intentional:** CLI commands, code samples, technical terms (Faber, Radix, Cista, Triga, Norma), Latin keywords (`functio`, `redde`, etc.), glyphs (`←`, `→`, `∴`), brand name, repository URLs, `macOS arm64`, `Linux x64`, `MIT` — these are correct as-is.
- **OK per design:** Latin prose in code fences on `corpus/index.html` and individual corpus pages — per the corpus status note, this is canonical Latin rendered through the `zh-Hant` pipeline.
- **Fix scope:** The `title` field needs to be set to Traditional Chinese in all `src/zh-Hant/*.md` frontmatter (source), then regenerate. The `Skip to content` template string needs a locale-aware override. The agent-notice on `index.html` and `404.html` needs manual translation.
