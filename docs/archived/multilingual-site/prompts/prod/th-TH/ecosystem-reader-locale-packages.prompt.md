You are a professional technical translator for the Faber documentation site.

# Contract — Thai (th-TH). Natural technical Thai developer docs.

Rules:
- Target locale: `th-TH`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Thai reader-locale Faber using Thai keywords for declarations, control flow, loops, returns, booleans, common primitive types, and lista/tabula collections. Keep Faber glyph syntax unchanged.

## English source body

Each non-Latin reader locale has a complete Faber package under
`examples/reader-locale/` with localised source, diagnostic test cases,
and a `faber.toml` manifest.

## Available packages {#available-packages}

| Locale | Path | Source example |
|--------|------|---------------|
| th-TH | `examples/reader-locale/th-TH/` | `ฟังก์ชัน salve(ข้อความ nomen) → ข้อความ` |
| zh-Hans | `examples/reader-locale/zh-Hans/` | `函数 问候(文本 名字) → 文本` |
| zh-Hant | `examples/reader-locale/zh-Hant/` | `函式 問候(文字 名字) → 文字` |
| ar | `examples/reader-locale/ar/` | `دالة تحية(نص اسم) → نص` |
| hi | `examples/reader-locale/hi/` | `फलन नमस्कार(पाठ नाम) → पाठ` |
| vi | `examples/reader-locale/vi/` | `hàm chào(vănbản tên) → vănbản` |

## Diagnostic test cases {#diagnostic-test-cases}

Each package includes test cases proving the full compiler pipeline is
locale-aware:

- `type-mismatch.fab` — localised type error diagnostics
- `undefined-variable.fab` — localised name resolution errors
- `non-ascii-number.fab` — NFKC handling
- `keyword-suggestion.fab` — localised "did you mean?" hints
