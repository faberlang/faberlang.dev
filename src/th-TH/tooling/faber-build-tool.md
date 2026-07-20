+++
translation_kind = "translated"

title = "Faber build tool"
section = "tooling"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
]


prose_hash = "sha256:5d8304941413ba003c019f0b1c43cd19e99ad0f25fa9b7a4ffadbc1327e8dfb6"
code_hash = "sha256:7657ec817fefbfb88c20a7b862970c668ebe2835de88c17eda584340fd2d6654"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
CLI `faber` เป็นจุดเริ่มต้นหลักสำหรับการสร้าง ตรวจสอบ รัน จัดรูปแบบ และทดสอบซอร์สโค้ด Faber โดยครอบ Radix compiler ไว้ในเครื่องมือสำหรับนักพัฒนาที่ใช้งานได้สะดวก

## คำสั่งหลัก {#core-commands}

| คำสั่ง | วัตถุประสงค์ |
|---|---|
| `faber build <path>` | คอมไพล์แพ็กเกจไปยังแบ็กเอนด์เป้าหมาย (ค่าเริ่มต้น: Rust) |
| `faber check <path>` | ตรวจสอบชนิดโดยไม่สร้างโค้ด |
| `faber run <path>` | สร้างและรันโปรแกรม |
| `faber test <path>` | รันชุดทดสอบ `proba` |
| `faber format <path>` | ใช้การจัดรูปแบบมาตรฐาน |
| `faber explain <code>` | อธิบายโค้ดวินิจฉัย |
| `faber emit <path>` | สร้างซอร์สโค้ดในรูปแบบเป้าหมาย |

## การสร้างแพ็กเกจ {#building}

```text
faber build my-package/ -t rust
```

แฟล็ก `-t` ใช้เลือกเป้าหมายการสร้างโค้ด เป้าหมายที่รองรับ ได้แก่ `rust` (ค่าเริ่มต้น), `wasm`, `typescript` และ `go`

## การตรวจสอบโดยไม่สร้างผลลัพธ์ {#checking}

```text
faber check my-package/
```

คำสั่งนี้จะรันกระบวนการส่วนหน้าทั้งหมด (lex → parse → typecheck → MIR lowering) โดยไม่สร้างไฟล์ผลลัพธ์ ใช้คำสั่งนี้ใน CI และการเชื่อมต่อกับเอดิเตอร์

## การรันทดสอบ {#testing-command}

```text
faber test my-package/
```

คอมไพล์ชุดทดสอบ `probandum` ทั้งหมดในแพ็กเกจเป็นฟังก์ชัน `#[test]` ของ Rust แล้วรันผ่าน Cargo การทดสอบแบบฝังอยู่ร่วมกับซอร์สโค้ดได้โดยตรง จึงไม่จำเป็นต้องมีไบนารีทดสอบแยกต่างหาก

## การจัดรูปแบบ {#formatting}

```text
faber format my-package/
```

ใช้ตัวจัดรูปแบบมาตรฐานของ Faber ตัวจัดรูปแบบจะบังคับใช้เลย์เอาต์ที่สอดคล้องกัน ได้แก่ การประกาศหนึ่งรายการต่อบรรทัด การเว้นวรรคตามมาตรฐาน และรูปแบบคีย์เวิร์ดที่เป็นมาตรฐาน

## การอธิบายผลการวินิจฉัย {#explaining}

```text
faber explain SEM001
```

แสดงคำอธิบายที่อ่านเข้าใจง่ายสำหรับโค้ดวินิจฉัยทุกแบบที่คอมไพเลอร์สามารถสร้างได้ เหมาะสำหรับเรียนรู้ความหมายของข้อผิดพลาดและวิธีแก้ไข
