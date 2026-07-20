# English Residue Audit: `dist/vi/`

**Date:** 2026-07-20
**Scope:** All `*.html` under `dist/vi/` except individual corpus term pages (corpus/index.html is included). Source: `src/vi/`.
**Method:** Read all 47 files in scope line-by-line.

---

## Summary

**46 of 47 files** contain English text where Vietnamese is expected. The Vietnamese prose body is well-translated; the residue is concentrated in the title/heading system, shared UI chrome, and the generated corpus index.

Two systemic patterns account for ~90 % of the residue:

1. **Page titles and H1s** — The Markdown `title` frontmatter field in `src/vi/*.md` is English. The SSG uses it for `<title>`, `<h1>`, and `og:title`. The Vietnamese `# Header` in the Markdown body is either omitted from the `<h1>` slot or rendered as a plain `<p>` inside `.content`.
2. **Shared UI chrome** — `skip-link`, `aria-label` attributes, `placeholder` text, and the agent-notice body paragraph are English strings in the template/layout layer.

---

## Findings Table

| # | Pattern | Files affected | English text | Vietnamese expected | Source |
|---|---|---|---|---|---|
| 1 | `<title>` tag | 46 | `"Features — Faber"`, `"History — Faber"`, etc. | `"Tính năng — Faber"`, `"Lịch sử — Faber"`, etc. | `src/vi/*.md` frontmatter `title` |
| 2 | `<h1>` heading | 46 | `"Features"`, `"History"`, `"Ecosystem"`, etc. | `"Tính năng"`, `"Lịch sử"`, `"Hệ sinh thái"`, etc. | Same as above |
| 3 | `og:title` meta | 46 | Same as `<title>` | Same as `<title>` fix | Same as above |
| 4 | Skip link | 47 | `"Skip to content"` | `"Chuyển đến nội dung chính"` | Template/layout |
| 5 | Nav `aria-label` | 47 | `"Machine documentation"` | `"Tài liệu máy"` | Template/layout |
| 6 | Search `placeholder` | 47 | `"keyword..."` | `"từ khóa..."` | Template/layout |
| 7 | Search `aria-label` | 47 | `"Search keywords"` | `"Tìm kiếm từ khóa"` | Template/layout |
| 8 | Agent-notice body | 47 | `"If you are an AI agent: start at /llms.txt..."` | Vietnamese equivalent | Shared partial |
| 9 | corpus/index.html `og:description` | 1 | `"Generated reference pages for 171 canonical Faber corpus terms."` | Vietnamese description | Corpus generator |
| 10 | corpus/index.html `<meta description>` | 1 | Same | Vietnamese description | Corpus generator |
| 11 | corpus/index.html translation note | 1 | `"Translation status: Tiếng Việt reader-locale proof..."` | Vietnamese | Corpus template |
| 12 | corpus/index.html `.content` headings | 1 | `<h2>Categories</h2>`, `<h2>Terms</h2>` | `<h2>Danh mục</h2>`, `<h2>Thuật ngữ</h2>` | Corpus generator |
| 13 | corpus/index.html intro sentence | 1 | `"Generated reference pages for 171 canonical Faber corpus terms."` | Vietnamese | Corpus generator |

---

## Top 10 Items by Impact

### 1. Title frontmatter — all authored pages (44 files)

The `title` field in `src/vi/*.md` controls `<title>`, `<h1>`, and `og:title`. Changing this one value per file fixes three English residues at once.

**Example diff for `src/vi/features/index.md`:**
```diff
-title = "Features"
+title = "Tính năng"
```

**Example diff for `src/vi/404.md`:**
```diff
-title = "Page not found"
+title = "Không tìm thấy trang"
```

All 44 authored files need this change. The brand name `Faber` in the title suffix (`— Faber`) is intentional Latin and should stay.

### 2. `Skip to content` link — all 47 files

The `skip-link` anchor text is English in every page.

**Example from dist/vi/index.html, line ~13:**
```html
<a href="#main-content" class="skip-link">Skip to content</a>
```
Should be `Chuyển đến nội dung chính` or `Bỏ qua nội dung`.

### 3. `aria-label="Machine documentation"` — all 47 files

The machine-links nav bar aria-label is English.

### 4. Agent-notice body — all 47 files

The body of the `.agent-notice` section is a block of English prose pointing agents to `/llms.txt`, `/agents/index.md`, and agent skills.

**Example from dist/vi/index.html, line ~30:**
```html
<p>If you are an AI agent: start at <a href="/llms.txt"><code>/llms.txt</code></a>,
then read <a href="/agents/index.md"><code>/agents/index.md</code></a> and pick a skill...</p>
```

The label above it (`Sẵn sàng cho tác nhân`) is correctly Vietnamese.

### 5. corpus/index.html — English `<meta>` description and `og:description`

```html
<meta name="description" content="Generated reference pages for 171 canonical Faber corpus terms.">
<meta property="og:description" content="Generated reference pages for 171 canonical Faber corpus terms.">
```
These should be Vietnamese, e.g. `"Các trang tham khảo được tạo cho 171 thuật ngữ chính tắc của corpus Faber."`

### 6. corpus/index.html — Translation status note (English prose)

Inside the `.content` area, above the page title:
```html
<p><strong>Translation status:</strong> Tiếng Việt reader-locale proof. Code fences render through the <code>vi</code> pipeline; prose is canonical Latin.</p>
```
This is English-to-user text on a Vietnamese page.

### 7. corpus/index.html — <h2>Categories</h2>

Inside `.content`:
```html
<h2>Categories</h2>
```
Should be `Danh mục`.

### 8. corpus/index.html — <h2>Terms</h2>

```html
<h2>Terms</h2>
```
Should be `Thuật ngữ`.

### 9. corpus/index.html — Intro paragraph

Inside `.content`:
```html
<p>Generated reference pages for 171 canonical Faber corpus terms.</p>
```
Should be Vietnamese.

### 10. Search placeholder + aria-label — all 47 files

```html
<input type="search" placeholder="keyword..." aria-label="Search keywords" ...>
```
Should be `placeholder="từ khóa..."` and `aria-label="Tìm kiếm từ khóa"`.

---

## Notes

- **CLI/paths/brand:** The name `Faber`, paths like `/llms.txt`, `/agents/index.md`, commands like `faber check`, package names like `norma:*`, and code fences containing Faber source code are correct as-is.
- **corpus category slugs** (e.g. `ad`, `aliasing`, `application` in the category list): These are technical identifiers, not English prose. They are OK as-is.
- **Translation quality:** The Vietnamese prose body in all authored pages appears complete and well-translated. The English residue is in structural elements (title, H1, UI chrome, meta tags), not in the article body content.
- **Root cause hypothesis:** The SSG template separates `title` (frontmatter → `<h1>`) from the Markdown body content. The frontmatter was not localized when the body was translated.

## Files with no English residue

Only **corpus/individual term pages** (e.g. `corpus/functio.html`, `corpus/si.html`, etc.) were excluded from scope per the task definition. Every page within scope has at least one instance of English residue.
