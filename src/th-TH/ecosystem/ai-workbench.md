+++
translation_kind = "translated"

title = "AI Workbench"
section = "ecosystem"
order = 4
sources = [
  "examples/ai-workbench/ (README.md, package, harness)",
]


prose_hash = "sha256:3a8940d1ee168b9bdf75f40f70ce5e5eb6b6446f47510df9c3511b2d4d1bef33"
code_hash = "sha256:dc8f04249d6a95c65b63ba0ccd58c402d6f8ed47a96bc15da4b6ad844922d007"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
AI Workbench เป็นแอปพลิเคชัน CLI ของ Faber สำหรับจัดทำรายการโมเดลภายในเครื่อง ตรวจสอบข้อมูลเมทาดาทา สร้างเวกเตอร์ฝังตัว จัดทำดัชนี และดำเนินเวิร์กโฟลว์การอนุมาน แอปพลิเคชันนี้สาธิตการใช้ Faber เพื่อสร้างแอปพลิเคชัน CLI แบบหลายคำสั่งที่มีขนาดใหญ่ขึ้น พร้อมการทำงานกับ I/O จริง การส่งออก JSON และการตรวจสอบด้วยชุดทดสอบ Python

## แพ็กเกจ {#package}

`examples/ai-workbench/packages/faber-ai/` พร้อมคำสั่งย่อยของ CLI:

- `model inspect` — สอบถามนามแฝงโมเดล เส้นทางการทำงาน และสถานะของโมเดลภายในเครื่อง
- `embed` — สร้างเวกเตอร์ฝังตัวจากอินพุตข้อความ

## คำสั่ง {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

## การตรวจสอบความถูกต้อง {#validation}

AI Workbench มีสคริปต์ชุดทดสอบ Python มากกว่า 20 รายการที่เปรียบเทียบผลลัพธ์จาก Faber กับแผนผังข้อมูลฟิกซ์เจอร์สำหรับรายการโมเดล การอนุมาน หลักฐานการใช้งาน GPU วงจรชีวิตเซสชัน และการนำแพ็กเกจกลับมาใช้ซ้ำ ซึ่งแสดงให้เห็นการตรวจสอบข้ามภาษาของไบนารี Faber ที่คอมไพล์แล้ว
