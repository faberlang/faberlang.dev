+++
translation_kind = "translated"

title = "ทัวร์ด่วน"
section = "start"
order = 0
sources = []



prose_hash = "sha256:fb6f791ae0e9b73d0c92c2127726f558a2b845351779f80217616b8f55629ff0"
code_hash = "sha256:f9eb22ab8a2408fe0076d846dd4266cff4ded675ad8d63a5b2d9ee59c3e0156f"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
ห้านาทีเพื่อทำความรู้จักโครงสร้างของ Faber: ติดตั้ง CLI อ่านฟังก์ชันหนึ่งรายการ แล้วเปิดดูแพ็กเกจจริง สำหรับเส้นทางแบบเป็นลำดับ ให้ทำตามนี้: [ติดตั้ง](/start/install.html) → [Hello](/start/hello.html) → [คำสั่ง](/start/commands.html) → [โปรเจกต์](/start/projects.html)

## 1. ติดตั้ง CLI {#install}

ดาวน์โหลดรุ่นปัจจุบัน (**1.1.1**) สำหรับแพลตฟอร์มของคุณจาก[หน้าติดตั้ง](/start/install.html) ตรวจสอบ checksum ของไฟล์เก็บถาวร แล้วนำไบนารี `faber` ที่แยกออกจาก `faber-v1.1.1-<target-triple>/faber` ไปไว้ใน `PATH` ของคุณ ยืนยันด้วยคำสั่ง:

```bash
faber --version
```

## 2. โครงสร้างของฟังก์ชัน {#shape}

พารามิเตอร์แบบระบุชนิดก่อน ชนิดผลลัพธ์แบบ glyph คำควบคุมภาษาละติน และยูเนียนที่เป็นค่าว่างได้:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

| สัญญาณ | ความหมาย |
|---|---|
| `functio` | การประกาศฟังก์ชัน |
| `numerus a` | ระบุชนิดก่อน แล้วจึงระบุชื่อ |
| `→` | ชนิดผลลัพธ์ |
| `∪ nihil` | ค่าว่างได้ (`T ∪ nihil`) |
| `si … ∴` | แขนงแบบย่อ |
| `redde` | คืนค่า |

## 3. โครงสร้างแพ็กเกจ {#package}

แพ็กเกจคือไดเรกทอรีที่มี `faber.toml` และ `src/`:

```text
my-app/
  faber.toml
  src/
    main.fab
```

คำสั่งที่ใช้บ่อย:

```bash
faber check my-app/
faber build my-app/ -t rust
faber run my-app/
faber test my-app/
```

รายละเอียดเพิ่มเติม: [เครื่องมือ build ของ Faber](/tooling/faber-build-tool.html)

## 4. แอปพลิเคชันจริง {#applications}

อย่าหยุดอยู่แค่ hello-world รีโพซิทอรี **examples** สาธารณะมี CLI ที่รองรับหลายคำสั่ง mailspace ภายในเครื่อง แทร็กงาน GPU และคลังโค้ดภาษาฉบับเต็ม

| แพ็กเกจ | สิ่งที่แสดงให้เห็น |
|---|---|
| AI Workbench | CLI หลายคำสั่ง การตรวจสอบโมเดล และ embeddings |
| ViviLite | CLI สำหรับ mailspace ที่เก็บข้อมูลเป็นไฟล์ / การประสานงานระหว่างเอเจนต์ |
| coreutils | แคมเปญแอปพลิเคชันขนาดใหญ่ขึ้น (parity harnesses) |
| gpu-workload | ระบบ / ขั้นของ GPU |
| corpus | หนึ่งไดเรกทอรีต่อโครงสร้างภาษาแต่ละรายการ |

ดูแพ็กเกจเหล่านี้ได้ที่[หน้าตัวอย่าง](/start/examples.html)

## 5. หากคุณเป็นเอเจนต์ {#agents}

1. อ่าน [`/llms.txt`](/llms.txt)
2. เปิด [`/agents/index.md`](/agents/index.md)
3. เลือกสกิลจาก [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json)

## เส้นทางเริ่มต้น {#start-track}

| ขั้นตอน | หน้า | ผลลัพธ์ |
|---|---|---|
| 1 | [ติดตั้งและดาวน์โหลด](/start/install.html) | วาง Faber 1.1.1 ไว้ใน `PATH` และตรวจสอบการติดตั้ง |
| 2 | [Hello, Faber](/start/hello.html) | สร้างและเรียกใช้ `salve-munde` |
| 3 | [คำสั่งที่คุณจะใช้](/start/commands.html) | เรียนรู้ `check`, `build`, `run`, `test`, `explain` |
| 4 | [โปรเจกต์และตัวอย่าง](/start/projects.html) | เริ่มทำงานกับแพ็กเกจจริงและหน้า corpus |

## ถัดไป {#next}

| หัวข้อ | ลิงก์ |
|---|---|
| ติดตั้งและดาวน์โหลด | [ติดตั้ง](/start/install.html) |
| Hello, Faber | [Hello](/start/hello.html) |
| คำสั่ง | [คำสั่ง](/start/commands.html) |
| โปรเจกต์ | [โปรเจกต์](/start/projects.html) |
| เอกสารอ้างอิงไวยากรณ์ | [ไวยากรณ์](/syntax/) |
| ฟีเจอร์ (locale, lane) | [ฟีเจอร์](/features/) |
| ไลบรารีในระบบนิเวศ | [ระบบนิเวศ](/ecosystem/) |
| คลังคำสำคัญ | [Corpus](/corpus/) |
