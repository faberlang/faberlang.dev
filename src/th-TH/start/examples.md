+++
title = "ตัวอย่าง"
section = "examples"
order = 2
sources = [
  "examples/README.md",
  "examples/ai-workbench/",
  "examples/vivilite/",
]
translation_kind = "translated"


prose_hash = "sha256:fe9855413a019d0aebf6228e219c1fab4b694d7fa3fd7d7f7cacab4def2f3700"
code_hash = "sha256:7fce5618203f2537ec7b775252d4ce66501a659a385973e9ec6cc1414c49e9e6"
source_commit = "ee93015caac71f7b89ddef8d9010ffbe22d6cd7e"
source_locale = "en-US"
+++
แพ็กเกจ Faber จริง — ไม่ใช่ตัวอย่างโค้ดแบบสั้นๆ ซอร์สอยู่ที่พื้นที่เก็บข้อมูลสาธารณะ
[faberlang/examples](https://github.com/faberlang/examples)
ใช้แพ็กเกจเหล่านี้เมื่อคุณต้องการดูว่าแอปพลิเคชันมีโครงสร้างอย่างไร CLI ต่อสายอย่างไร
หรือคลังภาษาจัดระเบียบอย่างไร

## วิธีรันตัวอย่าง {#how-to-run}

```bash
# CLI on PATH (see Install)
faber --version

# Clone examples
git clone https://github.com/faberlang/examples.git

# Type-check a package; dependencies resolve through faber.lock
# and the Cista package store.
faber check examples/ai-workbench/packages/faber-ai

# Build / run / test when the package supports it
faber build examples/ai-workbench/packages/faber-ai -t rust
faber test examples/ai-workbench/packages/faber-ai
```

คำสั่งเริ่มต้นที่แน่นอนแตกต่างกันไปตามแต่ละแพ็กเกจ — โปรดอ่าน `README.md` ของแต่ละแพ็กเกจ

## แพ็กเกจแอปพลิเคชัน {#applications}

| แพ็กเกจ | บทบาท | เริ่มที่ |
|---|---|---|
| **AI Workbench** | CLI หลายคำสั่งสำหรับงานสินค้าคงคลังโมเดลท้องถิ่น เอมเบ็ดดิง และเวิร์กโฟลว์การอนุมาน; การตรวจสอบความถูกต้องของ Python harness | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · site: [AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | CLI เมลสเปซท้องถิ่นแบบ Faber ดั้งเดิม (file-backed + SQLite lane เพิ่มเติม) สำหรับคำสั่งประสานงานเอเยนต์ | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | แคมเปญแอปพลิเคชันขนาดใหญ่ที่นำยูทิลิตี้ทั่วไปกลับมาใช้ใหม่พร้อม harness สำหรับเทียบเคียง | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | ขั้นและสัญญาสำหรับงาน GPU / ระบบ | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | การสาธิตการเขียนสคริปต์และส่วนติดต่อเคอร์เนล | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | แพ็กเกจร่างงานอัตโนมัติ | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | การสาธิตชุด locale สำหรับการแมปคำสำคัญใหม่ | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | สื่อทดลองเกี่ยวกับ package-store | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## คลังภาษา {#corpus}

โครงสร้าง **corpus** คือข้อมูลอ้างอิงคำสำคัญและคอนสตรัคต์: หนึ่งไดเรกทอรี
ต่อหนึ่งคอนสตรัคต์ มีโปรแกรม `.fab` ขนาดเล็กจำนวนมาก เป็นแหล่งความจริงของ
หน้า [คลังภาษา](/corpus/) ที่สร้างขึ้นบนไซต์นี้

| พื้นผิว | URL |
|---|---|
| ต้นไม้ซอร์ส | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| เอกสารที่สร้าง | [/corpus/](/corpus/) |
| บันทึกระบบนิเวศ | [คลังภาษา](/ecosystem/corpus.html) |

## ทัวร์ Stdlib {#stdlib}

Norma มาตรฐานคลังภาษา (standard-library exempla) อยู่ในพื้นที่เก็บข้อมูล **norma** ไม่ได้อยู่ใน
`examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` (ถ้ามี)
- Site: [Norma](/ecosystem/norma.html)

## ลำดับการเรียนรู้ที่แนะนำ {#order}

1. [ติดตั้ง](/start/install.html) CLI
2. อ่านคร่าวๆ [ทัวร์ด่วน](/start/) เพื่อดูรูปร่างภาษา
3. เปิดหน้า **corpus** สำหรับคำสำคัญใดๆ ที่คุณไม่รู้จัก ([Corpus hub](/corpus/))
4. อ่าน **AI Workbench** หรือ **ViviLite** แบบครบวงจรเพื่อดูรูปร่างแอปพลิเคชัน
5. ใช้ [ไวยากรณ์](/syntax/) และ [Tooling](/tooling/) เป็นข้อมูลอ้างอิงขณะแก้ไข

## เส้นทางเอเยนต์ {#agent-path}

- Skill: [examples](/.well-known/agent-skills/examples/SKILL.md)
- Skill: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- Index: [`/llms.txt`](/llms.txt)

## ก่อนหน้า {#previous}

| ก่อนหน้า | ถัดไป |
|---|---|
| [โปรเจกต์และตัวอย่าง](/start/projects.html) | [คุณสมบัติ](/features/) |
