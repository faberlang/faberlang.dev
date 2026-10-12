每個非拉丁字母讀者地區都在
`examples/reader-locale/` 下擁有完整的 Faber 套件，其中包含在地化原始碼、診斷測試案例，以及 `faber.toml` manifest。

## 可用套件 {#available-packages}

| 地區 | 路徑 | 原始碼範例 |
|--------|------|---------------|
| th-TH | `examples/reader-locale/th-TH/` | `ฟังก์ชัน salve(ข้อความ nomen) → ข้อความ` |
| zh-Hans | `examples/reader-locale/zh-Hans/` | `函数 问候(文本 名字) → 文本` |
| zh-Hant | `examples/reader-locale/zh-Hant/` | `函式 問候(文字 名字) → 文字` |
| ar | `examples/reader-locale/ar/` | `دالة تحية(نص اسم) → نص` |
| hi | `examples/reader-locale/hi/` | `फलन नमस्कार(पाठ नाम) → पाठ` |
| vi | `examples/reader-locale/vi/` | `hàm chào(vănbản tên) → vănbản` |

## 診斷測試案例 {#diagnostic-test-cases}

每個套件都包含測試案例，用來證明完整的編譯器管線具備地區感知能力：

- `type-mismatch.fab` — 在地化的型別錯誤診斷
- `undefined-variable.fab` — 在地化的名稱解析錯誤
- `non-ascii-number.fab` — NFKC 處理
- `keyword-suggestion.fab` — 在地化的「你是不是要找？」提示
