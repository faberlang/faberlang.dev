# English Residue Audit — `dist/zh-Hans/`

**Audit date:** 2026-07-20  
**Scope:** All `*.html` in `dist/zh-Hans/` except individual corpus term pages (e.g. `corpus/ab.html`, `corpus/and.html`, etc.). Includes `corpus/index.html`, `corpus/category/*.html`, `404.html`, plus all top-level section pages.  
**Source reference:** `src/zh-Hans/`  
**Method:** Manual review of every in-scope file. Classifies visible prose, headings, titles, skip-links, and agent-facing text as **BAD** (should be Simplified Chinese) or **OK** (CLI paths, brand, glyphs, code, intentional Latin Faber samples, natural technical loans).

---

## Summary

Every single page in `dist/zh-Hans/` contains English residue. The issues fall into **8 repeating patterns** that appear across the entire site, plus a cluster of **severe pages** with large amounts of untranslated English prose.

| Severity | Count | Description |
|----------|-------|-------------|
| **Pattern (all pages)** | 8 patterns | Recurring on every in-scope HTML file |
| **Severe pages** | 5 pages | Large blocks of English prose (corpus index, corpus categories, 404) |
| **Moderate pages** | ~30 pages | English `<h1>` headings and `<title>` labels but Chinese body prose |

---

## Repeating Patterns (All Pages)

### P1. English `<h1>` headings (visible page title)

Every page has an English `<h1>` that should be Simplified Chinese.

| File | Current `<h1>` | Expected (approx) |
|------|----------------|-------------------|
| `index.html` | `Faber` | `Faber` (brand — OK) |
| `404.html` | `Page not found` | `找不到页面` |
| `features/index.html` | `Features` | `特性` |
| `features/canonical-vs-sugar.html` | `Canonical vs sugar surfaces` | `规范形式与语法糖` |
| `features/commandments.html` | `Commandments` | `戒律` |
| `features/compilation-lanes.html` | `Compilation lanes` | `编译通道` |
| `features/frames.html` | `Capability calls and frames` | `能力调用与帧` |
| `features/latin-and-glyphs.html` | `Latin vocabulary and structural glyphs` | `拉丁词汇与结构字形` |
| `features/reader-locale.html` | `Reader locale` | `读者区域` |
| `features/testing.html` | `Inline testing` | `内联测试` |
| `start/index.html` | `Quick tour` | `快速导览` |
| `start/install.html` | `Install and download` | `安装与下载` |
| `start/hello.html` | `Hello, Faber` | `你好，Faber` |
| `start/commands.html` | `Commands you will use` | `命令` |
| `start/projects.html` | `Projects and examples` | `项目与示例` |
| `start/examples.html` | `Examples` | `示例` |
| `syntax/index.html` | `Syntax and semantics` | `语法与语义` |
| `tooling/index.html` | `Tooling and compiler` | `工具链与编译器` |
| `ecosystem/index.html` | `Ecosystem` | `生态系统` |
| `ecosystem/norma.html` | `Norma standard library` | `Norma 标准库` |
| `ecosystem/corpus.html` | `Language corpus` | `语言语料库` |
| `ecosystem/ai-workbench.html` | `AI Workbench` | `AI 工作台` |
| `ecosystem/coreutils.html` | `Coreutils` | `Coreutils` |
| `ecosystem/triga.html` | `Triga graphics library` | `Triga 图形库` |
| `ecosystem/reader-locale-packages.html` | `Reader-locale packages` | `读者区域包` |
| `history/index.html` | `History` | `历史` |
| `history/releases.html` | `Releases` | `发行版` |
| `references/index.html` | `References` | `参考` |
| `references/ebnf.html` | `EBNF grammar` | `EBNF 语法` |
| `references/design-docs.html` | `Design documents` | `设计文档` |
| `references/repositories.html` | `Repositories` | `代码库` |
| `corpus/index.html` | `Corpus` | `语料库` |
| `corpus/category/*.html` | `Corpus: {category}` | `语料库：{类别}` |

### P2. English `<title>` tags

Every page uses `English description — Faber` pattern. Examples:
- `<title>Page not found — Faber</title>`
- `<title>Features — Faber</title>`
- `<title>Canonical vs sugar surfaces — Faber</title>`
- `<title>Quick tour — Faber</title>`
- `<title>Corpus: function — Faber</title>`

### P3. `Skip to content` skip link (English)

Every page has:
```html
<a href="#main-content" class="skip-link">Skip to content</a>
```

### P4. Agent notice body (English prose)

Every page has a hidden/revealed agent notice section with English:
```
If you are an AI agent: start at /llms.txt, then read /agents/index.md
and pick a skill from /.well-known/agent-skills/. Humans: use Install and Examples.
```

### P5. Sidebar `Release 1.1.1` heading (English)

Every page in the sidebar has `Release 1.1.1` as a section heading. Should be `版本 1.1.1`.

### P6. Sidebar download labels (brand-adjacent English)

- `macOS arm64`
- `Linux x64`
- `全部发行版` — Chinese, OK
- `GitHub 组织` — Chinese, OK

### P7. Sidebar meta values (short English labels in specs table)

| Label | Chinese equivalent? |
|-------|---------------------|
| `packages` | `包` |
| `static · type-first` | `静态 · 类型优先` |
| `Rust → native` | `Rust → 原生` |
| `MIT` | `MIT` (OK — proper noun) |

### P8. `og:title` meta properties (English)

Every page has an `og:title` with an English value matching the `<title>`.

---

## Severe Pages (Large English Prose Blocks)

### S1. `404.html` — `<h1>Page not found</h1>`

The most visible English heading on the site. The content below has `# 404 — 找不到页面` in a `<p>` tag (appears to be a markdown rendering artifact) but the actual HTML `<h1>` is English.

### S2. `corpus/index.html` — Extensive English prose

The corpus index page has large English prose blocks that are **not** translated:

```html
<strong>Translation status:</strong> 简体中文 reader-locale proof.
Code fences render through the <code>zh-Hans</code> pipeline;
prose is canonical Latin.

<p>Generated reference pages for 171 canonical Faber corpus terms.</p>
<h2>Categories</h2>
...
<h2>Terms</h2>
```

The `<h2>Categories</h2>` and `<h2>Terms</h2>` headings are in English. While the site acknowledges this is intentional (`prose is canonical Latin`), from a zh-Hans reader's perspective the English prose is residue that should be translated.

### S3. `corpus/category/*.html` — English headings and prose on every category page (46 files)

Every category page has:
- `<h1>Corpus: {category}</h1>` — English
- `"Translation status: 简体中文 reader-locale proof..."` — English
- `<p># Corpus category: <code>{category}</code></p>` — English
- `<p>{N} canonical terms in this category.</p>` — English
- `<meta name="description">` in English: e.g. `"12 canonical terms in this category."`

This affects all 46 files in `corpus/category/`.

### S4. `history/releases.html` — Mixed content

While most headings and descriptions are translated, the page contains English in:
- Release labels and binary format descriptions that mix English platform names with Chinese context
- The phrase `_本清单为 GitHub Releases API 的快照。共 41 个标签，为本页面重新生成。_` is Chinese, OK
- But `**Faber** 标签是用户 CLI。**Radix** 标签是历史编译器 CLI 归档` — the labels "Faber" and "Radix" are brand names, OK
- Structure uses English platform labels per release table (e.g. `macOS arm64`, `Linux x64`)

### S5. `features/latin-and-glyphs.html` — Chinese code sample section

The "读者包片段" section at the bottom shows Chinese-localized code. However, the prose introduction and the code sample comments are mixed. This page also has English `<h1>`.

---

## Likely Source

The residue pattern suggests the HTML generation pipeline uses a shared template that inserts:

1. An English `<h1>` from the source document's frontmatter/title metadata (not translated per locale)
2. A static English skip-link
3. A static English agent-notice section
4. Sidebar content from a shared navigation template with some hardcoded English labels
5. The corpus pages are **generated** from corpus metadata where the prose (descriptions, headings) is authored in Latin/English and not run through a translation step for the zh-Hans output

The fix would require:
- A locale-aware title/heading pipeline (translate page titles per locale)
- Translated static strings for skip-link, agent-notice, sidebar headings
- A translation layer or content override for corpus-generated prose

---

## Findings Table

| # | File | Residue | Type | Likely Source |
|---|------|---------|------|---------------|
| 1 | `404.html` | `<h1>Page not found</h1>` | Visible heading | Template: untranslated title |
| 2 | `404.html` | `<title>Page not found — Faber</title>` | Page title | Template: untranslated metadata |
| 3 | `corpus/index.html` | `<h1>Corpus</h1>` | Visible heading | Template: generated page heading |
| 4 | `corpus/index.html` | `Generated reference pages for 171 canonical Faber corpus terms.` | English prose | Generator: prose not translated |
| 5 | `corpus/index.html` | `<h2>Categories</h2>` + `<h2>Terms</h2>` | English headings | Generator: section headings not translated |
| 6 | `corpus/category/function.html` | `<h1>Corpus: function</h1>` | Visible heading | Generator: category name in English |
| 7 | `corpus/category/*.html` (46 files) | `"{N} canonical terms in this category."` | English prose | Generator: prose not translated |
| 8 | `corpus/category/*.html` (46 files) | `"Translation status: ... prose is canonical Latin."` | English prose | Generator: status notice not translated |
| 9 | All files | `<a ...>Skip to content</a>` | Skip link | Template: hardcoded English |
| 10 | All files | Agent notice `"If you are an AI agent..."` | English prose | Template: hardcoded English |
| 11 | All files | `<h1>` in English (30+ files) | Visible heading | Template/source: title not localized |
| 12 | All files | `<title>` in English (30+ files) | Page title | Template/source: metadata not localized |
| 13 | All files | Sidebar `Release 1.1.1` | Navigation label | Template: hardcoded English |
| 14 | All files | Sidebar `macOS arm64` / `Linux x64` | Navigation label | Template: hardcoded English |
| 15 | All files | Sidebar meta `packages`, `static · type-first`, `Rust → native` | Navigation data | Template: key-value labels |
| 16 | All files | `og:title` in English (30+ files) | Meta property | Template: derived from `<title>` |
| 17 | All files | `<meta name="description">` in English for some pages | Meta description | Source: description not localized |

---

## Top 10 Most Impactful Findings

1. **`404.html: <h1>Page not found</h1>`** — Most visible English heading on the site. Every 404 page renders this prominently in the main content area.

2. **`corpus/index.html: "Generated reference pages for 171 canonical Faber corpus terms."`** — Full English sentence on the corpus landing page.

3. **`corpus/index.html: <h2>Categories</h2> + <h2>Terms</h2>`** — English section headings on the corpus index.

4. **`corpus/category/*.html: "{N} canonical terms in this category."`** — English prose on all 46 category pages.

5. **`corpus/category/*.html: "Corpus: {category}"` headings** — English visible headings on all 46 category pages.

6. **All content pages: English `<h1>` headings** — Every section page title is English instead of Chinese (30+ files).

7. **All pages: English `<title>` tags** — Browser tab/window titles in English (30+ files).

8. **All pages: English agent‑notice prose** — Every page has a multi‑sentence English block in the agent notice section.

9. **All pages: "Skip to content" skip link** — Accessibility text visible to screen-reader and keyboard users.

10. **All pages: Sidebar "Release 1.1.1"** — Navigation label visible on every page in the sidebar.

---

## Notes

- **Brand terms** (`Faber`, `Radix`, `Norma`, `Cista`, `Triga`, `GitHub`, `MIT`, `CLI`, `PATH`, `JSON`, `TOML`, `YAML`, `GPU`, `WASM`, `LLVM`, `WGSL`, etc.) are considered **OK** — these are proper nouns or standard technical acronyms.
- **Code examples** (Faber source code, shell commands, code fences with `functio`, `incipit`, etc.) are **OK** — these are Faber language samples, not prose.
- **Glyphs** (`←`, `→`, `∴`, `≡`, `∪`, etc.) are **OK** — they are language symbols, not English.
- **The corpus pages explicitly state** "prose is canonical Latin" — this is a known architectural choice, but from a zh-Hans reader perspective the English headings and descriptions are untranslated residue.
- **No commits were made.** This is a report only.
