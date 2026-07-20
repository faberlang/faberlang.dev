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
แต่ละภาษาสำหรับผู้อ่านที่ไม่ใช่ภาษาละตินจะมีแพ็กเกจ Faber แบบสมบูรณ์อยู่ภายใต้
`examples/reader-locale/` โดยมีซอร์สที่แปลเป็นภาษาท้องถิ่น กรณีทดสอบการวินิจฉัย
และไฟล์แมนนิเฟสต์ `faber.toml`

แพ็กเกจที่มีให้ใช้งาน {#available-packages}

| ภาษา | เส้นทาง | ตัวอย่างซอร์ส |
|--------|------|---------------|
| th-TH | `examples/reader-locale/th-TH/` | `ฟังก์ชัน salve(ข้อความ nomen) → ข้อความ` |
| zh-Hans | `examples/reader-locale/zh-Hans/` | `函数 问候(文本 名字) → 文本` |
| zh-Hant | `examples/reader-locale/zh-Hant/` | `函式 問候(文字 名字) → 文字` |
| ar | `examples/reader-locale/ar/` | `دالة تحية(نص اسم) → نص` |
| hi | `examples/reader-locale/hi/` | `फलन नमस्कार(पाठ नाम) → पाठ` |
| vi | `examples/reader-locale/vi/` | `hàm chào(vănbản tên) → vănbản` |

กรณีทดสอบการวินิจฉัย {#diagnostic-test-cases}

แต่ละแพ็กเกจมีกรณีทดสอบที่ยืนยันว่ากระบวนการคอมไพเลอร์ทั้งหมดรองรับภาษาแต่ละภาษา:

- `type-mismatch.fab` — ข้อผิดพลาดด้านชนิดข้อมูลที่แปลเป็นภาษาท้องถิ่น
- `undefined-variable.fab` — ข้อผิดพลาดการแก้ชื่อที่แปลเป็นภาษาท้องถิ่น
- `non-ascii-number.fab` — การจัดการ NFKC
- `keyword-suggestion.fab` — คำแนะนำ “คุณหมายถึง?” ที่แปลเป็นภาษาท้องถิ่น
