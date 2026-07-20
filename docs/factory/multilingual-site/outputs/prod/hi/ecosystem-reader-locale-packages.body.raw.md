हर गैर-लैटिन रीडर लोकेल के लिए `examples/reader-locale/` के अंतर्गत एक पूरा Faber पैकेज उपलब्ध है। इसमें स्थानीयकृत स्रोत, डायग्नोस्टिक परीक्षण मामले और `faber.toml` मेनिफेस्ट शामिल हैं।

## उपलब्ध पैकेज {#available-packages}

| लोकेल | पथ | स्रोत उदाहरण |
|--------|------|---------------|
| th-TH | `examples/reader-locale/th-TH/` | `ฟังก์ชัน salve(ข้อความ nomen) → ข้อความ` |
| zh-Hans | `examples/reader-locale/zh-Hans/` | `函数 问候(文本 名字) → 文本` |
| zh-Hant | `examples/reader-locale/zh-Hant/` | `函式 問候(文字 名字) → 文字` |
| ar | `examples/reader-locale/ar/` | `دالة تحية(نص اسم) → نص` |
| hi | `examples/reader-locale/hi/` | `फलन नमस्कार(पाठ नाम) → पाठ` |
| vi | `examples/reader-locale/vi/` | `hàm chào(vănbản tên) → vănbản` |

## डायग्नोस्टिक परीक्षण मामले {#diagnostic-test-cases}

हर पैकेज में ऐसे परीक्षण मामले शामिल हैं जो यह प्रमाणित करते हैं कि पूरा कंपाइलर पाइपलाइन लोकेल के अनुसार काम करता है:

- `type-mismatch.fab` — स्थानीयकृत प्रकार-असंगति डायग्नोस्टिक्स
- `undefined-variable.fab` — स्थानीयकृत नाम-समाधान त्रुटियाँ
- `non-ascii-number.fab` — NFKC हैंडलिंग
- `keyword-suggestion.fab` — स्थानीयकृत “क्या आपका मतलब यह था?” संकेत
