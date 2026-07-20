+++
title = "คำสั่งที่คุณจะใช้"
section = "commands"
order = 3
sources = []
translation_kind = "translated"


prose_hash = "sha256:0e56e02cfc5bc616178712a8ff6e3d914b95257913dbd22db2e8e8aac3c0e72e"
code_hash = "sha256:adf615632f084c7edf7f1f0dfc205ee4912e8b497b19c9c96167bf9b97e443cc"
source_commit = "ee93015caac71f7b89ddef8d9010ffbe22d6cd7e"
source_locale = "en-US"
+++
หน้านี้เป็นแผนผัง CLI เชิงปฏิบัติสำหรับสัปดาห์แรกของการทำงานกับ Faber ใช้เป็นดัชนีคำสั่ง จากนั้นเปิดหน้า [Faber build tool](/tooling/faber-build-tool.html) ฉบับละเอียดเมื่อคุณต้องการรายละเอียดเกี่ยวกับแฟล็กและไปป์ไลน์ของคอมไพเลอร์

## ลูปประจำวัน {#daily-loop}

| คำสั่ง | Use it for |
|---|---|
| `faber check <package>` | ตรวจส่วนหน้าแบบเร็ว: lex, parse, type check, lower |
| `faber build <package> -t rust` | สร้างโปรเจกต์ Rust เพื่อรีวิวหรือคอมไพล์เนทีฟ |
| `faber run <package>` | บิลด์และรันแพ็กเกจแอปพลิเคชัน |
| `faber test <package>` | รันเทสต์เมื่อแพ็กเกจกำหนดพื้นผิวทดสอบ |
| `faber explain <code>` | อ่านคำอธิบาย diagnostic ที่เสถียร |

เริ่มต้นด้วย `check` เป็นคำสั่งที่เบาที่สุดและเป็นคำสั่งที่ตัวแทนควรเรียกใช้ก่อนเสนอว่าโค้ดที่สร้างขึ้นเป็น Faber ที่ถูกต้อง

## ตรวจสอบ {#check}

```bash
faber check .
faber check examples/ai-workbench/packages/faber-ai
```

การตรวจสอบที่ผ่านหมายความว่าแพ็คเกจนั้นเป็นที่ยอมรับในเชิงวากยสัมพันธ์และเชิงความหมายสำหรับส่วนหน้าของคอมไพเลอร์ แต่ไม่ได้หมายความว่าห่วงโซ่เครื่องมือเนทีฟขั้นสุดท้ายถูกเรียกใช้งานแล้ว

## บิลด์ {#build}

```bash
faber build . -t rust
```

เป้าหมาย Rust นั้นสามารถตรวจสอบได้โดยเจตนา Rust ที่ถูกสร้างขึ้นเป็นสิ่งประดิษฐ์ของคอมไพเลอร์ ไม่ใช่แหล่งความจริง แก้ไขแพ็คเกจ Faber และสร้างใหม่แทนที่จะแก้ไข Rust ที่ถูกปล่อยออกมาด้วยมือ

## รัน {#run}

```bash
faber run .
```

ใช้ `run` สำหรับแพ็คเกจแอปพลิเคชันที่มีจุดเริ่มต้น `incipit` แพ็คเกจที่เป็นไลบรารีอย่างเดียวควรตรวจสอบและทดสอบแทน

## อธิบาย diagnostic {#explain}

```bash
faber explain SEM001
faber explain LEX006
```

ตระกูลการวินิจฉัยเป็นตัวบ่งชี้ที่เสถียร: `LEX` สำหรับข้อผิดพลาดทางศัพท์, `PAR` สำหรับข้อผิดพลาดของตัวแยกวิเคราะห์, `SEM` สำหรับข้อผิดพลาดทางความหมาย/ชนิด ในเอกสารและรายงานของตัวแทน ให้อ้างอิงรหัสการวินิจฉัยแทนการถอดความข้อผิดพลาดของคอมไพเลอร์อย่างคร่าว ๆ

## คำสั่ง reader-locale {#reader-locale}

```bash
faber format --reader-locale=la path/to/file.fab
faber format --reader-locale=th-TH path/to/file.fab
faber emit -t faber --reader-locale=zh-Hans path/to/file.fab
```

ผลลัพธ์ reader locale เป็นการเรนเดอร์โมเดลเชิงความหมายของคอมไพเลอร์ ไม่ใช่ชั้นการแปลในขณะเรียกดูผ่านเบราว์เซอร์ งานโลแคลควรทำหลังจากแพ็คเกจผ่านการตรวจสอบในรูปแบบบัญญัติ

## ถัดไป {#next}

| ก่อนหน้า | ถัดไป |
|---|---|
| [สวัสดี Faber](/start/hello.html) | [โปรเจกต์และตัวอย่าง](/start/projects.html) |
