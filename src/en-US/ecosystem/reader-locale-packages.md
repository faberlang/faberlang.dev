+++
title = "Reader-locale packages"
section = "ecosystem"
order = 5
sources = [
  "examples/reader-locale/ (6 locale packages with localized Faber source)",
]
+++

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
