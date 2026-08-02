+++
translation_kind = "translated"

title = "Examples"
section = "examples"
order = 5
sources = [
  "examples/README.md",
  "examples/ai-workbench/",
  "examples/vivilite/",
  "examples/ai-workbench/ (README.md, package, harness)",
  "examples/coreutils/ (38 packages, README.md, campaign docs)",
  "examples/coreutils/packages/echo/src/main.fab",
]
+++

## ตัวอย่าง

แพ็กเกจ Faber จริง ไม่ใช่เพียงตัวอย่างแบบง่าย แหล่งโค้ดอยู่ในรีโพสาธารณะ [faberlang/examples](https://github.com/faberlang/examples) ใช้แหล่งข้อมูลเหล่านี้เมื่อคุณต้องการดูว่าแอปพลิเคชันมีโครงสร้างอย่างไร เชื่อมต่อ CLI อย่างไร หรือจัดระเบียบคลังภาษอยาางไร

### วิธีเรียกใช้ตัวอย่าง {#how-to-run}

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

คำสั่งเริ่มต้นที่แน่นอนจะแตกต่างกันไปในแต่ละแพ็กเกจ โปรดอ่าน `README.md` ของแพ็กเกจนั้น

### แพ็กเกจแอปพลิเคชัน {#applications}

| แพ็กเกจ | บทบาท | เริ่มต้นที่นี่ |
|---|---|---|
| **AI Workbench** | CLI หลายคำสั่งสำหรับตรวจสอบรายการโมเดลในเครื่อง การทำ embeddings และเวิร์กโฟลว์การอนุมาน พร้อมการตรวจสอบ harness ด้วย Python | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · เว็บไซต์: [AI Workbench](/start/examples.html) |
| **ViviLite** | CLI mailspace ภายในเครื่องที่เขียนด้วย Faber สำหรับคำสั่งประสานงานของเอเจนต์ รองรับการจัดเก็บด้วยไฟล์และเลน SQLite เสริม | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | แคมเปญแอปพลิเคชันขนาดใหญ่ที่นำยูทิลิตีทั่วไปมาเขียนใหม่ พร้อม parity harness | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | ขั้นงานและสัญญาสำหรับเวิร์กโหลด GPU และระบบ | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | เดโมด้านสคริปต์และการเชื่อมต่อกับเคอร์เนล | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | แพ็กเกจตัวอย่างด้านระบบอัตโนมัติ | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | เดโมแพ็กภาษา locale สำหรับแมปคีย์เวิร์ดใหม่ | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | เนื้อหาทดลองเกี่ยวกับที่เก็บแพ็กเกจ | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

### คลังภาษาตัวอย่าง {#corpus}

ทรี **corpus** คือแหล่งอ้างอิงสำหรับคีย์เวิร์ดและโครงสร้างภาษา โดยมีหนึ่งไดเรกทอรีต่อหนึ่งโครงสร้าง และมีโปรแกรม `.fab` ขนาดเล็กจำนวนมาก ทรีนี้เป็นแหล่งข้อมูลหลักสำหรับหน้า [Corpus](/corpus/) ที่สร้างขึ้นบนเว็บไซต์

| พื้นผิว | URL |
|---|---|
| ทรีซอร์ส | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| เอกสารที่สร้างขึ้น | [/corpus/](/corpus/) |
| หมายเหตุระบบนิเวศ | [คลังภาษาตัวอย่าง](/libraries/corpus.html) |

### ทัวร์ stdlib {#stdlib}

ตัวอย่างไลบรารีมาตรฐานของ Norma อยู่ในรีโพ `norma` ไม่ได้อยู่ใต้ `examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` เมื่อมีไดเรกทอรีนี้
- เว็บไซต์: [Norma](/libraries/norma.html)

### ลำดับการเรียนรู้ที่แนะนำ {#order}

1. [ติดตั้ง](/start/install.html) CLI
2. อ่านคร่าว ๆ [ทัวร์สั้น](/start/) เพื่อทำความเข้าใจรูปแบบของภาษา
3. เปิดหน้าของ **corpus** สำหรับคีย์เวิร์ดที่คุณยังไม่รู้จัก ([ศูนย์รวม Corpus](/corpus/))
4. อ่าน **AI Workbench** หรือ **ViviLite** ตั้งแต่ต้นจนจบเพื่อทำความเข้าใจรูปแบบแอปพลิเคชัน
5. ใช้ [ไวยากรณ์](/language/) และ [เครื่องมือ](/toolchain/) เป็นข้อมูลอ้างอิงขณะแก้ไข

### เส้นทางสำหรับเอเจนต์ {#agent-path}

- สกิล: [examples](/.well-known/agent-skills/examples/SKILL.md)
- สกิล: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- ดัชนี: [`/llms.txt`](/llms.txt)

### ก่อนหน้า {#previous}

| ก่อนหน้า | ถัดไป |
|---|---|
| [โครงการและตัวอย่าง](/start/projects.html) | [ฟีเจอร์](/language/) |

## AI Workbench

AI Workbench เป็นแอปพลิเคชัน CLI ของ Faber สำหรับจัดทำรายการโมเดลภายในเครื่อง ตรวจสอบข้อมูลเมทาดาทา สร้างเวกเตอร์ฝังตัว จัดทำดัชนี และดำเนินเวิร์กโฟลว์การอนุมาน แอปพลิเคชันนี้สาธิตการใช้ Faber เพื่อสร้างแอปพลิเคชัน CLI แบบหลายคำสั่งที่มีขนาดใหญ่ขึ้น พร้อมการทำงานกับ I/O จริง การส่งออก JSON และการตรวจสอบด้วยชุดทดสอบ Python

### แพ็กเกจ {#package}

`examples/ai-workbench/packages/faber-ai/` พร้อมคำสั่งย่อยของ CLI:

- `model inspect` — สอบถามนามแฝงโมเดล เส้นทางการทำงาน และสถานะของโมเดลภายในเครื่อง
- `embed` — สร้างเวกเตอร์ฝังตัวจากอินพุตข้อความ

### คำสั่ง {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

### การตรวจสอบความถูกต้อง {#validation}

AI Workbench มีสคริปต์ชุดทดสอบ Python มากกว่า 20 รายการที่เปรียบเทียบผลลัพธ์จาก Faber กับแผนผังข้อมูลฟิกซ์เจอร์สำหรับรายการโมเดล การอนุมาน หลักฐานการใช้งาน GPU วงจรชีวิตเซสชัน และการนำแพ็กเกจกลับมาใช้ซ้ำ ซึ่งแสดงให้เห็นการตรวจสอบข้ามภาษาของไบนารี Faber ที่คอมไพล์แล้ว

## Coreutils

Faber นำ GNU coreutils กลับมาใช้งานใหม่เพื่อเป็นบทพิสูจน์ในเลนแอปพลิเคชัน โปรแกรม CLI เหล่านี้ทำงานได้จริง และแสดงให้เห็นว่า Faber สามารถสร้างไบนารีที่ทำงานร่วมกับ `argv`, `stdio`, รหัสทางออก และการทำงานกับ I/O ของโฮสต์ได้ โดยตรวจสอบความสอดคล้องกับยูทิลิตี GNU บนโฮสต์ผ่านชุดทดสอบความเท่าเทียม

### ยูทิลิตีที่พัฒนาแล้ว {#implemented-utilities}

**ขั้นที่ 1 — โครงร่างพื้นฐาน + true/false**  
`true`, `false`

**ขั้นที่ 2 — ตัวช่วยร่วมพื้นฐาน + การทดสอบแบบอินไลน์**  
`echo`, `basename`, `dirname`, `printf`, `seq`

**ขั้นที่ 3 — ส่วนย่อยของ stdin ที่อาจเป็นค่าว่าง**  
`cat`, `head`, `tail`, `wc`, `tac`, `uniq`, `fold`, `nl`, `expand`,  
`unexpand`, `sort`, `cut`, `grep`, `tr`, `tee`, `paste`

**สร้างโครงร่างแล้ว — ขั้นที่ 5 เป็นต้นไป**  
`rm`, `cp`, `mv`, `mkdir`, `touch`, `pwd`, `readlink`, `realpath`,  
`join`, `comm`, `od`, `cksum`, `split`, `yes`, `printenv`

### ตัวอย่าง — echo {#example--echo}

แพ็กเกจ `echo` แสดงรูปแบบการใช้งานของ Faber ที่ใช้ทั่วทั้ง coreutils ได้แก่ คำอธิบายประกอบ CLI การแยกวิเคราะห์ตัวเลือก การทดสอบแบบอินไลน์ด้วย `probandum`/`proba`/`adfirma` และโมดูลร่วมพื้นฐาน:

```faber locale=la
importa ex "norma:consolum" privata consolum

functio echo_textus(lista<textus> words) → textus {
    redde ""
}

functio echo_novam_lineam(lista<textus> words) → bivalens {
    redde falsum
}

probandum "echo formatting" tag "coreutils" {
    proba "empty operands" {
        adfirma echo_textus([]) ≡ ""
    }
    proba "-n suppresses newline" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }
}

@ cli "echo"
@ descriptio "GNU coreutils echo parity exemplum"
@ operandus ceteri textus words
incipit argumenta args {
    # ... CLI logic here
}
```

### การเรียกใช้ {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
