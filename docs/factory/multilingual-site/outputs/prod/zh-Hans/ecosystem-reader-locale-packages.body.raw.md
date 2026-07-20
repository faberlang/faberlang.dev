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
