+++
translation_kind = "translated"

title = "History"
section = "history"
order = 0
sources = []


prose_hash = "sha256:99390038c112db9d79c728a21f5bc2c804af48f6de648df7e6ff6f2f0bc32a99"
code_hash = "sha256:8cfe9c845ef9a1247454bc890937eafa78a38164428679c7a6981c3c8cf3b9c4"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
## จุดกำเนิด {#origins}

คอมมิตแรกของคอมไพเลอร์ Radix เกิดขึ้นเมื่อ **20 ธันวาคม 2024**
ในรูปแบบโปรเจกต์ Bun + TypeScript ที่มีไฟล์ `docs/decisions.md` เพียงไฟล์เดียว
คอมมิตที่สองได้กำหนดบันทึกการตัดสินใจด้านสถาปัตยกรรม (Architecture Decision Records)
ไว้ห้ารายการ ซึ่งยังคงกำหนดทิศทางของภาษาในปัจจุบัน

**ADR-003** ซึ่งมีชื่อว่า "การลงท้ายของคำบ่งบอกความหมายเชิงอรรถศาสตร์"
ได้วางหลักไว้ตั้งแต่เริ่มต้นว่า สัณฐานวิทยาของภาษาละตินจะมีบทบาทมากกว่า
การเป็นเพียงผิวหน้าของคีย์เวิร์ด — คอมไพเลอร์จะเข้าใจการผันคำนามและการผันกริยา
เพื่ออนุมานเจตนาของโปรแกรม การจับคู่รูปแบบกรณีดั้งเดิมมีดังนี้:

```text
Nominative  (subject)       →  return value, caller
Accusative  (direct object)  →  primary argument
Dative      (indirect obj.)  →  recipient, callback, destination
Genitive    (possession)     →  property access, "of" relationships
Ablative    (instrument)     →  dependencies, context, "using X"
```

เอกสารฉบับเดียวกันยังระบุว่า: *"คำถามถัดไปตามธรรมชาติคือการผันกริยา
(อนาคตกาล → async?)"* เมล็ดพันธุ์นี้เติบโตเป็นหลักการตั้งชื่อ
`morphologia` ในปัจจุบัน โดยไลบรารีมาตรฐานใช้รูปกริยาภาษาละตินที่ผันแล้ว
เพื่อสื่อว่าเป็นการทำงานแบบ sync หรือ async และเป็นการกลายค่าเดิมหรือ
การคัดลอกผลลัพธ์ออกมา — โดยไม่กำหนดให้คอมไพเลอร์ต้องเข้าใจไวยากรณ์ภาษาละตินเอง

โครงการเริ่มต้นด้วย TypeScript จากนั้นจึงเขียนใหม่ด้วย Rust และตรึงไวยากรณ์ไว้
สำหรับสายรุ่น 1.x โดยใช้เอดิชัน 2026 ADR ดั้งเดิมทั้งห้ารายการ
(นามสกุลไฟล์ `.fab`, คำแนะนำข้อผิดพลาด, การลงท้ายของคำตามกรณี,
ตัวแยกวิเคราะห์แบบ recursive descent และ AST แบบกำหนดเอง)
ยังคงมองเห็นได้ในประวัติ git

## รุ่นเผยแพร่ {#releases}

ไฟล์ CLI ที่สร้างไว้ล่วงหน้า — รุ่น Faber ปัจจุบันอยู่ด้านบน
ตามด้วยแท็กและไบนารีที่เผยแพร่แล้วทั้งหมดจาก
[faberlang/releases](https://github.com/faberlang/releases):

- **[รุ่นเผยแพร่](/history/releases.html)** — ลิงก์ดาวน์โหลดและรายการประวัติ
- **[ติดตั้งและดาวน์โหลด](/start/install.html)** — การตั้งค่า PATH และการรัน `faber check` ครั้งแรก
