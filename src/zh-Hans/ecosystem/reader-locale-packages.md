+++
translation_kind = "translated"

title = "Reader-locale packages"
section = "ecosystem"
order = 5
sources = [
  "examples/reader-locale/ (6 locale packages with localized Faber source)",
]


prose_hash = "sha256:6bd7229133950cf7c39c68da663bf20641b651d4d1d87a8a91adae1ad3253eeb"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
每个非拉丁读者区域都有一个完整的 Faber 包，位于 `examples/reader-locale/` 下，其中包含本地化源代码、诊断测试用例以及一个 `faber.toml` 清单。

## 可用包 {#available-packages}

| 区域 | 路径 | 源代码示例 |
|--------|------|---------------|
| th-TH | `examples/reader-locale/th-TH/` | `ฟังก์ชัน salve(ข้อความ nomen) → ข้อความ` |
| zh-Hans | `examples/reader-locale/zh-Hans/` | `函数 问候(文本 名字) → 文本` |
| zh-Hant | `examples/reader-locale/zh-Hant/` | `函式 問候(文字 名字) → 文字` |
| ar | `examples/reader-locale/ar/` | `دالة تحية(نص اسم) → نص` |
| hi | `examples/reader-locale/hi/` | `फलन नमस्कार(पाठ नाम) → पाठ` |
| vi | `examples/reader-locale/vi/` | `hàm chào(vănbản tên) → vănbản` |

## 诊断测试用例 {#diagnostic-test-cases}

每个包都包含测试用例，用以证明完整的编译器管道具有区域感知能力：

- `type-mismatch.fab` — 本地化类型错误诊断
- `undefined-variable.fab` — 本地化名称解析错误
- `non-ascii-number.fab` — NFKC 处理
- `keyword-suggestion.fab` — 本地化的“您是指？”提示
