# English Residue Audit: `dist/th-TH/` (non-corpus pages)

Audit date: 2026-07-20
Scope: all `*.html` under `dist/th-TH/` except individual corpus pages.  
Source root: `src/th-TH/`

---

## Summary

**41 non-corpus HTML files** examined across 7 sections (index+404, start, features, history, references, syntax, tooling, ecosystem) plus `corpus/index.html`.

### Overall finding

Thai portal content is well-translated. The prose body text is Thai throughout the portal/start pages. However, **every prose section beyond `start/` has untranslated English `og:title` / `<title>` / `<h1>`** because those titles originate from a template layer that does not use Thai. This is a **systemic template issue**, not a per-page content gap.

---

## Findings Detail

### Class A — Systemic: English `<title>` / `og:title` / `<h1>` (39 of 41 pages)

Every page outside `start/` and the root `index.html` and `404.html` has an English `<title>` (and matching `<h1>`) that should be Thai.

| File | Current `<title>` / `<h1>` | Expected (Thai) |
|---|---|---|
| `features/index.html` | `Features — Faber` | `คุณสมบัติ — Faber` |
| `features/canonical-vs-sugar.html` | `Canonical vs sugar surfaces — Faber` | `รูปแบบมาตรฐานเทียบกับชูการ์ — Faber` |
| `features/commandments.html` | `Commandments — Faber` | `บัญญัติ — Faber` |
| `features/compilation-lanes.html` | `Compilation lanes — Faber` | `เลนการคอมไพล์ — Faber` |
| `features/frames.html` | `Capability calls and frames — Faber` | `การเรียกใช้ความสามารถและเฟรม — Faber` |
| `features/latin-and-glyphs.html` | `Latin vocabulary and structural glyphs — Faber` | `คำศัพท์ภาษาละตินและสัญลักษณ์ — Faber` |
| `features/reader-locale.html` | `Reader locale — Faber` | `ภาษาสำหรับผู้อ่าน — Faber` |
| `features/testing.html` | `Inline testing — Faber` | `การทดสอบในซอร์ส — Faber` |
| `history/index.html` | `History — Faber` | `ประวัติ — Faber` |
| `history/releases.html` | `Releases — Faber` | `รุ่นเผยแพร่ — Faber` |
| `references/index.html` | `References — Faber` | `เอกสารอ้างอิง — Faber` |
| `references/design-docs.html` | `Design documents — Faber` | `เอกสารการออกแบบ — Faber` |
| `references/ebnf.html` | `EBNF grammar — Faber` | `ไวยากรณ์ EBNF — Faber` |
| `references/repositories.html` | `Repositories — Faber` | `คลังโค้ด — Faber` |
| `syntax/index.html` | `Syntax and semantics — Faber` | `ไวยากรณ์และความหมาย — Faber` |
| `syntax/types.html` | `Data types — Faber` | `ชนิดข้อมูล — Faber` |
| `syntax/variables.html` | `Variables and binding — Faber` | `ตัวแปรและการผูกค่า — Faber` |
| `syntax/functions.html` | `Functions — Faber` | `ฟังก์ชัน — Faber` |
| `syntax/control-flow.html` | `Control flow — Faber` | `การควบคุมการไหล — Faber` |
| `syntax/strings.html` | `String and template literals — Faber` | `สตริงและเทมเพลตลิเทอรัล — Faber` |
| `syntax/collections.html` | `Collections — Faber` | `คอลเลกชัน — Faber` |
| `syntax/generics.html` | `Generics — Faber` | `เจเนอริก — Faber` |
| `syntax/errors.html` | `Error handling — Faber` | `การจัดการข้อผิดพลาด — Faber` |
| `syntax/nullability.html` | `Nullability and optionality — Faber` | `ค่าที่อาจไม่มีและทางเลือก — Faber` |
| `syntax/conversion.html` | `Conversion and construction — Faber` | `การแปลงและการสร้าง — Faber` |
| `syntax/glyphs.html` | `Glyphs and operators — Faber` | `อักขระและตัวดำเนินการ — Faber` |
| `tooling/index.html` | `Tooling and compiler — Faber` | `เครื่องมือและคอมไพเลอร์ — Faber` |
| `tooling/radix-compiler.html` | `Radix compiler — Faber` | `คอมไพเลอร์ Radix — Faber` |
| `tooling/faber-build-tool.html` | `Faber build tool — Faber` | `เครื่องมือสร้าง Faber — Faber` |
| `tooling/codegen-targets.html` | `Codegen targets — Faber` | `เป้าหมายการสร้างโค้ด — Faber` |
| `tooling/cista-package-manager.html` | `Cista package manager — Faber` | `ตัวจัดการแพ็กเกจ Cista — Faber` |
| `tooling/performance.html` | `Compiler performance — Faber` | `ประสิทธิภาพคอมไพเลอร์ — Faber` |
| `tooling/scripting.html` | `In-process scripting — Faber` | `สคริปต์ในโพรเซส — Faber` |
| `ecosystem/index.html` | `Ecosystem — Faber` | `ระบบนิเวศ — Faber` |
| `ecosystem/norma.html` | `Norma standard library — Faber` | `ไลบรารีมาตรฐาน Norma — Faber` |
| `ecosystem/triga.html` | `Triga graphics library — Faber` | `ไลบรารีกราฟิก Triga — Faber` |
| `ecosystem/corpus.html` | `Language corpus — Faber` | `คลังภาษา — Faber` |
| `ecosystem/ai-workbench.html` | `AI Workbench — Faber` | `AI Workbench — Faber` |
| `ecosystem/coreutils.html` | `Coreutils — Faber` | `Coreutils — Faber` |
| `ecosystem/reader-locale-packages.html` | `Reader-locale packages — Faber` | `แพ็กเกจภาษาสำหรับผู้อ่าน — Faber` |
| `corpus/index.html` | `Corpus — Faber` | `คลังภาษา — Faber` |

Notes:
- `ai-workbench.html` and `coreutils.html` use English product names — acceptable as proper nouns.
- `404.html` has English `<title>Page not found — Faber</title>` and `<h1>Page not found</h1>`.

### Class B — Systemic: Agent-notice block English (40 of 41 pages)

Every page has this block in the `agent-notice` section:

```html
<section class="agent-notice" aria-label="Agent-facing notice">
  <span class="agent-notice-label">พร้อมสำหรับเอเจนต์</span>
  <div class="agent-notice-body">
    <p>If you are an AI agent: start at <a href="/llms.txt"><code>/llms.txt</code></a>,
    then read <a href="/agents/index.md"><code>/agents/index.md</code></a>
    and pick a skill from <a href="/.well-known/agent-skills/index.json"><code>/.well-known/agent-skills/</code></a>.
    Humans: use <a href="/th-TH/start/install.html">Install</a>
    and <a href="/th-TH/start/examples.html">Examples</a>.</p>
  </div>
</section>
```

The paragraph text is entirely English. The section label `พร้อมสำหรับเอเจนต์` ("Ready for agents") is Thai, but the body prose is not. This appears on **every single page** except possibly corpus pages.

### Class C — Systemic: `Skip to content` accessibility link (41 of 41 pages)

Every page has:

```html
<a href="#main-content" class="skip-link">Skip to content</a>
```

This should be `ข้ามไปยังเนื้อหาหลัก` or similar.

### Class D — Specific: `404.html` key elements

```html
<title>Page not found — Faber</title>
<h1>Page not found</h1>
```

Both should be Thai: `ไม่พบหน้า — Faber` and `ไม่พบหน้า`.

### Class E — Specific: `corpus/index.html` prose block

```html
<h1>Corpus</h1>
<p><strong>Translation status:</strong> ภาษาไทย reader-locale proof.
Code fences render through the <code>th-TH</code> pipeline; prose is canonical Latin.</p>
```

Then:

```html
<p># Corpus</p>
<p>Generated reference pages for 171 canonical Faber corpus terms.</p>
```

Both the heading and the body paragraph are English. The "Translation status" note declares this as intentional, but the `og:title` and `<title>` are still English.

---

## Top 10 Priorities by User Impact

| # | File | Issue | Impact |
|---|---|---|---|
| 1 | `404.html` | `<title>` + `<h1>` English | Every broken-link experience shows English |
| 2 | `features/index.html` | Index page title English | Top-level section index shows English |
| 3 | `features/reader-locale.html` | Title English — ironic for a page about locale | Most visible feature page |
| 4 | `syntax/index.html` | Title English | Primary navigation target for learners |
| 5 | `syntax/types.html` | Title English | Most-linked syntax subpage |
| 6 | `ecosystem/index.html` | Title English | High-traffic section index |
| 7 | `history/releases.html` | Title English | Download/release page |
| 8 | `tooling/faber-build-tool.html` | Title English | CLI tool documentation |
| 9 | `corpus/index.html` | Title + body English | Cross-linking from all pages |
| 10 | ALL pages | Agent-notice body is English prose | Repeated on every page view |

---

## Source of the Problem

The Markdown source files in `src/th-TH/` are well-translated. The English titles and the agent-notice block are generated by the **site template/renderer** (`faberlang.dev` site generator), which falls back to English (canonical Latin) for:

1. Page `<title>` / `og:title` generation
2. `h1` heading generation from page frontmatter
3. Agent-notice block (static template partial)
4. `Skip to content` accessibility link (static template partial)

These four template constructs are not sourced from the Thai Markdown content.

---

## How to Fix

1. **Title/heading template**: Modify the site renderer to accept locale-aware titles from each page's frontmatter (e.g., `og_title`, `h1_title` fields in the YAML frontmatter) rather than deriving them from the canonical Latin page title.

2. **Agent-notice partial**: Replace the English paragraph with a locale-aware block. For `th-TH`, use a Thai translation of the agent-notice prose.

3. **`Skip to content`**: Replace the hardcoded English string in the base template with a locale-aware lookup.

4. **`404.html`**: Add locale-specific `<title>` and `<h1>` values to the 404 template.

5. **`corpus/index.html`**: Either provide a Thai `og:title` / `<title>`, or accept the canonical-Latin note as a known limitation (the prose note already says "prose is canonical Latin").
