+++
translation_kind = "translated"

title = "Repositories"
section = "references"
order = 3
sources = [
  "github.com/faberlang",
]


prose_hash = "sha256:1f00ec1ce77844348776b258be2b9246bf876b614a2849a0e8dcbb54a8dc82f0"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
Faber พัฒนาขึ้นในหลายรีโพซิทอรีภายใต้องค์กร `faberlang`

## รีโพซิทอรีสาธารณะ {#public-repositories}

| รีโพซิทอรี | คำอธิบาย |
|-----------|-------------|
| `faber` | CLI สำหรับผู้ใช้: ตรวจสอบ สร้าง รัน ทดสอบ จัดรูปแบบ และอธิบาย |
| `faber-runtime` | ชนิดข้อมูลรันไทม์หลัก (Valor, เทนเซอร์, เฟรม); ชื่อ crate คือ `faber` |
| `norma` | ซอร์สไลบรารีมาตรฐาน (โมดูล `norma:*`) |
| `triga` | ไลบรารีกราฟิก/เรขาคณิตเสริม |
| `cista` | ตัวจัดการแพ็กเกจและสโตร์ (อยู่ระหว่างการทดลอง) |
| `examples` | คลังตัวอย่างภาษา, coreutils, AI Workbench และแพ็กเกจ reader-locale |
| `faberlang.dev` | เว็บไซต์นี้ |

## รีโพซิทอรีส่วนตัว {#private-repositories}

| รีโพซิทอรี | คำอธิบาย |
|-----------|-------------|
| `radix` | คอมไพเลอร์: การวิเคราะห์คำศัพท์ การแยกวิเคราะห์ การวิเคราะห์ความหมาย HIR/MIR/AIR การวินิจฉัย และการสร้างโค้ด |

## รีโพซิทอรีแพลตฟอร์มโฮสต์ {#host-platform-repositories}

| รีโพซิทอรี | คำอธิบาย |
|-----------|-------------|
| `host-kernel-rs` | เราเตอร์แบบบาง: Frame, Conversation, การกระจายงานด้วยคำนำหน้า และข้อผิดพลาดแบบมีโครงสร้าง |
| `host-native-rs` | การเชื่อมต่อแบบเนทีฟ: worker และฮุก `register_providers` |
| `host-providers-rs` | การใช้งาน provider: solum, processus, consolum, tempus, aleator และ http |
