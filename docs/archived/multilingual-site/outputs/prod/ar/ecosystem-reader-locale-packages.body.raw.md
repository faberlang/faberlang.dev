كل بيئة قراءة غير لاتينية لديها حزمة Faber كاملة تحت
`examples/reader-locale/` مع مصدر مُعرَّب، وحالات اختبار تشخيصية،
وملف بيان `faber.toml`.

## الحزم المتاحة {#available-packages}

| البيئة | المسار | مثال مصدري |
|--------|------|---------------|
| th-TH | `examples/reader-locale/th-TH/` | `ฟังก์ชัน salve(ข้อความ nomen) → ข้อความ` |
| zh-Hans | `examples/reader-locale/zh-Hans/` | `函数 问候(文本 名字) → 文本` |
| zh-Hant | `examples/reader-locale/zh-Hant/` | `函式 問候(文字 名字) → 文字` |
| ar | `examples/reader-locale/ar/` | `دالة تحية(نص اسم) → نص` |
| hi | `examples/reader-locale/hi/` | `फलन नमस्कार(पाठ नाम) → पाठ` |
| vi | `examples/reader-locale/vi/` | `hàm chào(vănbản tên) → vănbản` |

## حالات الاختبار التشخيصية {#diagnostic-test-cases}

تتضمن كل حزمة حالات اختبار تثبت أن مسار المُصرِّف الكامل
يدرك البيئات المختلفة:

- `type-mismatch.fab` — تشخيصات أخطاء الأنواع المُعرَّبة
- `undefined-variable.fab` — أخطاء تحليل الأسماء المُعرَّبة
- `non-ascii-number.fab` — معالجة NFKC
- `keyword-suggestion.fab` — تلميحات "هل قصدت؟" المُعرَّبة
