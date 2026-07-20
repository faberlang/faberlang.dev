+++
translation_kind = "translated"

title = "ตัวอย่าง"
section = "examples"
order = 2
sources = [
  "examples/README.md",
  "examples/ai-workbench/",
  "examples/vivilite/",
]



prose_hash = "sha256:fe9855413a019d0aebf6228e219c1fab4b694d7fa3fd7d7f7cacab4def2f3700"
code_hash = "sha256:7fce5618203f2537ec7b775252d4ce66501a659a385973e9ec6cc1414c49e9e6"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
แพ็กเกจ Faber จริง ไม่ใช่เพียงตัวอย่างแบบง่าย แหล่งโค้ดอยู่ในรีโพสาธารณะ [faberlang/examples](https://github.com/faberlang/examples) ใช้แหล่งข้อมูลเหล่านี้เมื่อคุณต้องการดูว่าแอปพลิเคชันมีโครงสร้างอย่างไร เชื่อมต่อ CLI อย่างไร หรือจัดระเบียบคลังภาษอยาางไร

## วิธีเรียกใช้ตัวอย่าง {#how-to-run}

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

## แพ็กเกจแอปพลิเคชัน {#applications}

| แพ็กเกจ | บทบาท | เริ่มต้นที่นี่ |
|---|---|---|
| **AI Workbench** | CLI หลายคำสั่งสำหรับตรวจสอบรายการโมเดลในเครื่อง การทำ embeddings และเวิร์กโฟลว์การอนุมาน พร้อมการตรวจสอบ harness ด้วย Python | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · เว็บไซต์: [AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | CLI mailspace ภายในเครื่องที่เขียนด้วย Faber สำหรับคำสั่งประสานงานของเอเจนต์ รองรับการจัดเก็บด้วยไฟล์และเลน SQLite เสริม | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | แคมเปญแอปพลิเคชันขนาดใหญ่ที่นำยูทิลิตีทั่วไปมาเขียนใหม่ พร้อม parity harness | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | ขั้นงานและสัญญาสำหรับเวิร์กโหลด GPU และระบบ | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | เดโมด้านสคริปต์และการเชื่อมต่อกับเคอร์เนล | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | แพ็กเกจตัวอย่างด้านระบบอัตโนมัติ | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | เดโมแพ็กภาษา locale สำหรับแมปคีย์เวิร์ดใหม่ | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | เนื้อหาทดลองเกี่ยวกับที่เก็บแพ็กเกจ | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## คลังภาษาตัวอย่าง {#corpus}

ทรี **corpus** คือแหล่งอ้างอิงสำหรับคีย์เวิร์ดและโครงสร้างภาษา โดยมีหนึ่งไดเรกทอรีต่อหนึ่งโครงสร้าง และมีโปรแกรม `.fab` ขนาดเล็กจำนวนมาก ทรีนี้เป็นแหล่งข้อมูลหลักสำหรับหน้า [Corpus](/corpus/) ที่สร้างขึ้นบนเว็บไซต์

| พื้นผิว | URL |
|---|---|
| ทรีซอร์ส | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| เอกสารที่สร้างขึ้น | [/corpus/](/corpus/) |
| หมายเหตุระบบนิเวศ | [คลังภาษาตัวอย่าง](/ecosystem/corpus.html) |

## ทัวร์ stdlib {#stdlib}

ตัวอย่างไลบรารีมาตรฐานของ Norma อยู่ในรีโพ `norma` ไม่ได้อยู่ใต้ `examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` เมื่อมีไดเรกทอรีนี้
- เว็บไซต์: [Norma](/ecosystem/norma.html)

## ลำดับการเรียนรู้ที่แนะนำ {#order}

1. [ติดตั้ง](/start/install.html) CLI
2. อ่านคร่าว ๆ [ทัวร์สั้น](/start/) เพื่อทำความเข้าใจรูปแบบของภาษา
3. เปิดหน้าของ **corpus** สำหรับคีย์เวิร์ดที่คุณยังไม่รู้จัก ([ศูนย์รวม Corpus](/corpus/))
4. อ่าน **AI Workbench** หรือ **ViviLite** ตั้งแต่ต้นจนจบเพื่อทำความเข้าใจรูปแบบแอปพลิเคชัน
5. ใช้ [ไวยากรณ์](/syntax/) และ [เครื่องมือ](/tooling/) เป็นข้อมูลอ้างอิงขณะแก้ไข

## เส้นทางสำหรับเอเจนต์ {#agent-path}

- สกิล: [examples](/.well-known/agent-skills/examples/SKILL.md)
- สกิล: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- ดัชนี: [`/llms.txt`](/llms.txt)

## ก่อนหน้า {#previous}

| ก่อนหน้า | ถัดไป |
|---|---|
| [โครงการและตัวอย่าง](/start/projects.html) | [ฟีเจอร์](/features/) |
