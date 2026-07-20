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
