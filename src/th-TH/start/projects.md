+++
translation_kind = "translated"

title = "โปรเจกต์และตัวอย่าง"
section = "projects"
order = 4
sources = []



prose_hash = "sha256:8a914c63394e5bd0bf08ccef737eb95ec4cfb7df1813f3475c78d6ef579fb14d"
code_hash = "sha256:08056868d41c8d2a2925beb910fea8adcf4ac708fa67559e5a160dd900429a06"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
หลังจาก hello-world แล้ว ให้เริ่มทำงานกับแพ็กเกจจริง Faber เป็นภาษาที่จัดโครงสร้างรอบแพ็กเกจ วิธีเรียนรู้ที่เร็วที่สุดคือค้นหาและอ่านแพ็กเกจที่มีอยู่ ซึ่งใช้ความสามารถของคอมไพเลอร์แบบเดียวกับที่คุณวางแผนจะใช้

## รีโพซิทอรีสาธารณะ {#repositories}

| รีโพซิทอรี | เริ่มที่นี่ | เหตุผล |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`, แพ็กเกจแอปพลิเคชัน และแทร็กต่าง ๆ | คอร์ปัสสาธารณะและตัวอย่างแอปพลิเคชัน |
| [`faberlang/norma`](https://github.com/faberlang/norma) | แพ็กเกจ `norma:*` | ซอร์สโค้ดไลบรารีมาตรฐาน |
| [`faberlang/faber`](https://github.com/faberlang/faber) | CLI wrapper | เครื่องมือบิลด์สำหรับผู้ใช้ |
| [`faberlang/cista`](https://github.com/faberlang/cista) | CLI/ไลบรารีของ package store | พื้นผิวการจัดการแพ็กเกจ |
| [`faberlang/triga`](https://github.com/faberlang/triga) | ซอร์ส `triga:*` | ไลบรารีกราฟิกและเรขาคณิต |

## โคลนเวิร์กสเปซสำหรับเรียนรู้ {#clone-workspace}

```bash
mkdir faber-learning
cd faber-learning
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

แพ็กเกจที่มีอิมพอร์ต `norma:*` จะใช้การอ้างอิงดีเพนเดนซีจาก Cista package store ที่บันทึกไว้ใน `faber.lock` ใช้ `FABER_LIBRARY_HOME` เฉพาะเมื่อคุณต้องการแทนที่ตัวแก้ไขไลบรารีในเครื่องโดยตั้งใจเพื่อพัฒนาไลบรารี

## อ่านตัวอย่างตามลำดับนี้ {#read-order}

1. [ทัวร์สั้น ๆ](/start/) เพื่อเรียนรู้ไวยากรณ์พื้นฐาน
2. [สวัสดี Faber](/start/hello.html) สำหรับแพ็กเกจเดียว
3. [คอร์ปัส](/corpus/) ซึ่งมีหนึ่งหน้าต่อหนึ่งคีย์เวิร์ดหรือโครงสร้าง
4. [ตัวอย่าง](/start/examples.html) สำหรับแอปพลิเคชันขนาดใหญ่ขึ้น
5. [เครื่องมือบิลด์ Faber](/tooling/faber-build-tool.html) สำหรับรายละเอียด CLI

## เวิร์กโฟลว์สำหรับเอเจนต์ {#agent-workflow}

เอเจนต์ไม่ควรอนุมานไวยากรณ์จากคำอธิบายเพียงอย่างเดียว ให้ใช้ machine surfaces แล้วตรวจสอบโค้ดที่สร้างขึ้น:

```bash
curl -fsSL https://faberlang.dev/llms.txt
faber check path/to/package
```

สำหรับงานแพ็กเกจ ให้ระบุรีโพซิทอรี พาธแพ็กเกจ คำสั่ง และโค้ดวินิจฉัยในรายงาน หากคุณแก้ไขเอกสารที่มีโค้ด Faber แบบ fenced ในเว็บไซต์นี้ ให้เรียกใช้ตัวตรวจสอบ fence ก่อนระบุว่าตัวอย่างยังคอมไพล์ได้

## สิ่งที่จะเรียนรู้ต่อจากแทร็กเริ่มต้น {#after-start}

| เป้าหมาย | อ่าน |
|---|---|
| เรียนรู้ไวยากรณ์ | [ไวยากรณ์](/syntax/) |
| ทำความเข้าใจ locale | [Reader locale](/features/reader-locale.html) |
| ใช้คอมไพเลอร์ | [เครื่องมือบิลด์ Faber](/tooling/faber-build-tool.html) และ [คอมไพเลอร์ Radix](/tooling/radix-compiler.html) |
| เรียกดูโครงสร้าง | [คอร์ปัส](/corpus/) |
| สร้างโปรแกรมด้วยไลบรารี | [ระบบนิเวศ](/ecosystem/) |

## ถัดไป {#next}

| ก่อนหน้า | ถัดไป |
|---|---|
| [คำสั่งที่คุณจะใช้](/start/commands.html) | [ตัวอย่าง](/start/examples.html) |
