+++
title = "ทัวร์ด่วน"
section = "start"
order = 0
sources = []
translation_kind = "translated"


prose_hash = "sha256:fb6f791ae0e9b73d0c92c2127726f558a2b845351779f80217616b8f55629ff0"
code_hash = "sha256:f9eb22ab8a2408fe0076d846dd4266cff4ded675ad8d63a5b2d9ee59c3e0156f"
source_commit = "ee93015caac71f7b89ddef8d9010ffbe22d6cd7e"
source_locale = "en-US"
+++
ห้านาทีสู่ภาพรวมของ Faber: ติดตั้ง CLI, อ่านฟังก์ชันหนึ่ง,
จากนั้นเปิดแพ็กเกจจริง สำหรับเส้นทางแบบเป็นลำดับ ให้ทำตาม: [ติดตั้ง](/start/install.html) →
[สวัสดี](/start/hello.html) → [คำสั่ง](/start/commands.html) →
[โปรเจกต์](/start/projects.html)

## 1. ติดตั้ง CLI {#install}

ดาวน์โหลดรุ่นปัจจุบัน (**1.1.1**) สำหรับแพลตฟอร์มของคุณจาก
[หน้า install](/start/install.html), ตรวจสอบ checksum ของไฟล์บีบอัด,
และนำไบนารี `faber-v1.1.1-<target-triple>/faber` ที่แตกแล้ว
ไปไว้บน `PATH` ของคุณ ยืนยัน:

```bash
faber --version
```

## 2. รูปร่างของฟังก์ชัน {#shape}

พารามิเตอร์แบบชนิดขึ้นก่อน, ชนิดคืนค่าเป็นกลิฟ, คำควบคุมภาษาละติน, ยูเนียนแบบ null ได้:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

| สัญญาณ | ความหมาย |
|---|---|
| `functio` | การประกาศฟังก์ชัน |
| `numerus a` | ชนิดขึ้นก่อน, ตามด้วยชื่อ |
| `→` | ชนิดคืนค่า |
| `∪ nihil` | ค่า null ได้ (`T ∪ nihil`) |
| `si … ∴` | กิ่งแบบกระชับ |
| `redde` | คืนค่า |

## 3. โครงสร้างแพ็กเกจ {#package}

แพ็กเกจคือไดเรกทอรีที่มี `faber.toml` และ `src/`:

```text
my-app/
  faber.toml
  src/
    main.fab
```

คำสั่งทั่วไป:

```bash
faber check my-app/
faber build my-app/ -t rust
faber run my-app/
faber test my-app/
```

รายละเอียด: [เครื่องมือ build ของ Faber](/tooling/faber-build-tool.html)

## 4. แอปพลิเคชันจริง {#applications}

อย่าหยุดแค่ hello-world ที่เก็บ **examples** สาธารณะมี CLI
แบบหลายคำสั่ง, mailspace ท้องถิ่น, งานติดตามปริมาณงาน GPU,
และคลังภาษาที่สมบูรณ์

| แพ็กเกจ | สิ่งที่แสดง |
|---|---|
| AI Workbench | CLI หลายคำสั่ง, ตรวจสอบโมเดล, embeddings |
| ViviLite | mailspace แบบเก็บในไฟล์ / CLI ประสานงานเอเจนต์ |
| coreutils | แคมเปญแอปพลิเคชันขนาดใหญ่ (harness เทียบเคียง) |
| gpu-workload | ระบบ / ระดับ GPU |
| corpus | หนึ่งไดเรกทอรีต่อโครงสร้างภาษา |

เรียกดูได้ที่ [หน้า examples](/start/examples.html)

## 5. ถ้าคุณเป็นเอเจนต์ {#agents}

1. อ่าน [`/llms.txt`](/llms.txt)
2. เปิด [`/agents/index.md`](/agents/index.md)
3. เลือกทักษะจาก [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json)

## เส้นทางเริ่มต้น {#start-track}

| ขั้นตอน | หน้า | ผลลัพธ์ |
|---|---|---|
| 1 | [ติดตั้งและดาวน์โหลด](/start/install.html) | ใส่ Faber 1.1.1 บน `PATH` และยืนยัน |
| 2 | [สวัสดี Faber](/start/hello.html) | สร้างและรัน `salve-munde` |
| 3 | [คำสั่งที่คุณจะใช้](/start/commands.html) | เรียนรู้ `check`, `build`, `run`, `test`, `explain` |
| 4 | [โปรเจกต์และตัวอย่าง](/start/projects.html) | ย้ายไปยังแพ็กเกจจริงและหน้าคลังภาษา |

## ถัดไป {#next}

| หัวข้อ | ลิงก์ |
|---|---|
| ติดตั้งและดาวน์โหลด | [ติดตั้ง](/start/install.html) |
| Hello, Faber | [สวัสดี](/start/hello.html) |
| คำสั่ง | [คำสั่ง](/start/commands.html) |
| โปรเจกต์ | [โปรเจกต์](/start/projects.html) |
| เอกสารอ้างอิงไวยากรณ์ | [ไวยากรณ์](/syntax/) |
| ฟีเจอร์ (locale, lanes) | [คุณสมบัติ](/features/) |
| ไลบรารีระบบนิเวศ | [ระบบนิเวศ](/ecosystem/) |
| คลังคำสำคัญ | [คลังภาษา](/corpus/) |
