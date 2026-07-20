+++
title = "โปรเจกต์และตัวอย่าง"
section = "projects"
order = 4
sources = []
translation_kind = "translated"


prose_hash = "sha256:8a914c63394e5bd0bf08ccef737eb95ec4cfb7df1813f3475c78d6ef579fb14d"
code_hash = "sha256:08056868d41c8d2a2925beb910fea8adcf4ac708fa67559e5a160dd900429a06"
source_commit = "ee93015caac71f7b89ddef8d9010ffbe22d6cd7e"
source_locale = "en-US"
+++
หลังจาก hello-world แล้ว ให้ก้าวไปสู่แพ็กเกจจริง Faber เป็นภาษาเชิงแพ็กเกจ วิธีเรียนรู้ที่เร็วที่สุดคือตรวจสอบและอ่านแพ็กเกจที่มีอยู่ซึ่งใช้พื้นผิวคอมไพเลอร์เดียวกับที่คุณจะใช้งาน

## ที่เก็บสาธารณะ {#repositories}

| ที่เก็บ | Start here | Why |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`, application packages, tracks | คลังตัวอย่างสาธารณะและตัวอย่างแอปพลิเคชัน |
| [`faberlang/norma`](https://github.com/faberlang/norma) | `norma:*` packages | ซอร์สโค้ดไลบรารีมาตรฐาน |
| [`faberlang/faber`](https://github.com/faberlang/faber) | ตัวห่อ CLI | เครื่องมือ build สำหรับผู้ใช้ |
| [`faberlang/cista`](https://github.com/faberlang/cista) | CLI/lib ของ package-store | พื้นผิวการจัดการแพ็กเกจ |
| [`faberlang/triga`](https://github.com/faberlang/triga) | `triga:*` source | ไลบรารีกราฟิกและเรขาคณิต |

## โคลนพื้นที่เรียนรู้ {#clone-workspace}

```bash
mkdir faber-learning
cd faber-learning
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

แพ็กเกจที่นำเข้า `norma:*` จะแก้ไข dependencies จากที่เก็บแพ็กเกจ Cista ที่บันทึกไว้ใน `faber.lock` ให้ใช้ `FABER_LIBRARY_HOME` เฉพาะเมื่อคุณต้องการ override ตัวแก้ไข dependency ในเครื่องสำหรับการพัฒนาไลบรารีเท่านั้น

## อ่านตัวอย่างตามลำดับนี้ {#read-order}

1. [แนะนำอย่างรวดเร็ว](/start/) — สำหรับไวยากรณ์พื้นผิว
2. [สวัสดี Faber](/start/hello.html) — สำหรับแพ็กเกจเดียว
3. [คลังคำศัพท์](/corpus/) — สำหรับหนึ่งหน้าต่อคีย์เวิร์ดหรือโครงสร้าง
4. [ตัวอย่าง](/start/examples.html) — สำหรับแอปพลิเคชันขนาดใหญ่
5. [เครื่องมือ build Faber](/tooling/faber-build-tool.html) — สำหรับรายละเอียด CLI

## เวิร์กโฟลว์เอเจนต์ {#agent-workflow}

เอเจนต์ไม่ควรอนุมานไวยากรณ์จากคำอธิบายเพียงอย่างเดียว ให้ใช้พื้นผิวเครื่องแล้วตรวจสอบโค้ดที่สร้างขึ้น:

```bash
curl -fsSL https://faberlang.dev/llms.txt
faber check path/to/package
```

สำหรับงานแพ็กเกจ ให้อ้างอิง repo, path ของแพ็กเกจ, คำสั่ง, และรหัส diagnostic ในรายงาน หากคุณแก้ไขเอกสารที่มีโค้ด Faber ในเฟนซ์ในไซต์นี้ ให้รัน fence validator ก่อนยืนยันว่าตัวอย่างยังคงคอมไพล์ได้

## หลังแทร็กเริ่มต้น {#after-start}

| เป้าหมาย | อ่าน |
|---|---|
| เรียนรู้ไวยากรณ์ | [ไวยากรณ์](/syntax/) |
| เข้าใจ locale | [Reader locale](/features/reader-locale.html) |
| ใช้คอมไพเลอร์ | [Faber build tool](/tooling/faber-build-tool.html) และ [Radix compiler](/tooling/radix-compiler.html) |
| เรียกดูโครงสร้าง | [คลังภาษา](/corpus/) |
| สร้างด้วยไลบรารี | [ระบบนิเวศ](/ecosystem/) |

## ถัดไป {#next}

| ก่อนหน้า | ถัดไป |
|---|---|
| [คำสั่งที่คุณจะใช้](/start/commands.html) | [ตัวอย่าง](/start/examples.html) |
