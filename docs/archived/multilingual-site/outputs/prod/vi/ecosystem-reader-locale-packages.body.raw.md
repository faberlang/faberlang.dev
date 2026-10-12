Mỗi locale đọc không phải tiếng Latinh có một gói Faber hoàn chỉnh trong
`examples/reader-locale/`, với mã nguồn đã bản địa hóa, các trường hợp kiểm thử
chẩn đoán và tệp kê khai `faber.toml`.

## Các gói khả dụng {#available-packages}

| Locale | Đường dẫn | Ví dụ mã nguồn |
|--------|------|---------------|
| th-TH | `examples/reader-locale/th-TH/` | `ฟังก์ชัน salve(ข้อความ nomen) → ข้อความ` |
| zh-Hans | `examples/reader-locale/zh-Hans/` | `函数 问候(文本 名字) → 文本` |
| zh-Hant | `examples/reader-locale/zh-Hant/` | `函式 問候(文字 名字) → 文字` |
| ar | `examples/reader-locale/ar/` | `دالة تحية(نص اسم) → نص` |
| hi | `examples/reader-locale/hi/` | `फलन नमस्कार(पाठ नाम) → पाठ` |
| vi | `examples/reader-locale/vi/` | `hàm chào(vănbản tên) → vănbản` |

## Các trường hợp kiểm thử chẩn đoán {#diagnostic-test-cases}

Mỗi gói bao gồm các trường hợp kiểm thử chứng minh toàn bộ pipeline biên dịch
nhận biết locale:

- `type-mismatch.fab` — chẩn đoán lỗi kiểu đã bản địa hóa
- `undefined-variable.fab` — lỗi phân giải tên đã bản địa hóa
- `non-ascii-number.fab` — xử lý NFKC
- `keyword-suggestion.fab` — gợi ý đã bản địa hóa dạng “ý bạn là?”
