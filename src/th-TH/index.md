+++
title = "แฟบเบอร์ (Faber) — ภาษาโปรแกรมเชิงแพ็กเกจ"
section = ""
order = 0
sources = []
translation_kind = "translated"


prose_hash = "sha256:e63352acf54515593d9aeccf392881d72018d55e6b21d6e1ddd5a3979bef91b8"
code_hash = "sha256:a02ba6ea46d65efd212b09e097d3240402bfe1d46f89b993e389cd53ca1a9c9e"
source_commit = "ee93015caac71f7b89ddef8d9010ffbe22d6cd7e"
source_locale = "en-US"
+++
**แฟบเบอร์ (Faber)** เป็นภาษาโปรแกรมเชิงแพ็กเกจ (package-oriented programming language) ที่ใช้คำศัพท์เชิงพฤติกรรมภาษาละติน (Latin behavioural vocabulary) ประกอบด้วยไวยากรณ์ปกติขนาดเล็ก และระบบชนิดแบบไทป์-เฟิร์สต์ (type-first) แบบสแตติก ซอร์สโค้ดถูกคอมไพล์ผ่านคอมไพเลอร์ราดิกซ์ (Radix) ไปเป็นภาษา Rust ที่ตรวจสอบได้และไบนารีแบบเนทีฟ คุณสมบัติทางสถาปัตยกรรมที่กำหนดภาษานี้คือ ความหมาย (meaning) อยู่ในแกนเชิงความหมาย — HIR (high-level intermediate representation) — แทนที่จะอยู่ในการแสดงผลรูปแบบใดรูปแบบหนึ่ง

ชื่อ Faber มาจากภาษาละตินที่แปลว่า *ผู้สร้าง* หรือ *ช่างฝีมือ* คอมไพเลอร์ชื่อราดิกซ์ (Radix) มาจากภาษาละตินที่แปลว่า *ราก* ภาษานี้พัฒนาโดย Ian Zepp และเผยแพร่ภายใต้สัญญาอนุญาต MIT

**มาใหม่หรือ?** เริ่มที่ [ติดตั้งและดาวน์โหลด](/start/install.html) จากนั้นทำแทร็คเริ่มต้นแบบเรียงลำดับ: [สวัสดี](/start/hello.html), [คำสั่ง](/start/commands.html), และ [โปรเจกต์](/start/projects.html)

## ดาวน์โหลด Faber 1.1.1 {#download}

รุ่นปัจจุบัน: **Faber 1.1.1** (แท็ก `faber-v1.1.1`) มีไฟล์ CLI เก็บถาวรที่ build ไว้ล่วงหน้าสำหรับ macOS และ Linux ให้นำไบนารี `faber-v1.1.1-<target-triple>/faber` ออกมาและวางไว้ใน `PATH` ของคุณ

| แพลตฟอร์ม | ไฟล์เก็บถาวร | เช็คซัม |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [faber-v1.1.1-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

ตัวอย่างการติดตั้งด่วน (macOS arm64):

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv faber-v1.1.1-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

บันทึกประจำรุ่นและทรัพยากรทั้งหมด: [github.com/faberlang/releases · faber-v1.1.1](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1)
คำแนะนำทีละขั้นตอน: [คู่มือการติดตั้ง](/start/install.html) รายการประวัติทั้งหมด: [รุ่นที่เผยแพร่](/history/releases.html)

| | |
|---|---|
| **กระบวนทัศน์** | เชิงแพ็กเกจ; การจัดลำดับความหมาย |
| **ระบบชนิด** | สแตติก, ไทป์-เฟิร์สต์; nullable ผ่าน `T ∪ nihil` |
| **สัญลักษณ์** | `← → ∴ ≡ ∪ ⇥` |
| **ออกแบบโดย** | Ian Zepp |
| **เปิดตัวครั้งแรก** | 2024 |
| **คอมไพเลอร์** | Radix (Rust) |
| **เลน** | แอปพลิเคชัน (HIR) · ระบบ (MIR) |
| **เป้าหมายหลัก** | Rust → ไบนารีแบบเนทีฟ |
| **ภาษาโลแคลผู้อ่าน** | 7 ภาษาที่จัดส่ง (la, ar, hi, vi, th-TH, zh-Hans, zh-Hant) |
| **ไลบรารีมาตรฐาน** | Norma (`norma:*`) |
| **สัญญาอนุญาต** | MIT |

## เริ่มต้นที่นี่ {#start-here}

| เส้นทาง | สำหรับใคร | อะไร |
|---|---|---|
| [ติดตั้ง](/start/install.html) | มนุษย์ | ดาวน์โหลด, PATH, `faber check` ครั้งแรก |
| [สวัสดี](/start/hello.html) | มนุษย์ | สร้างและรัน `salve-munde` |
| [คำสั่ง](/start/commands.html) | มนุษย์ + เอเจนต์ | ลูป CLI ประจำวัน: check, build, run, test, explain |
| [โปรเจกต์](/start/projects.html) | มนุษย์ + เอเจนต์ | ย้ายจาก hello-world สู่แพ็กเกจจริง |
| [ทัวร์ด่วน](/start/) | มนุษย์ | รูปร่างภาษาในห้านาที |
| [ตัวอย่าง](/start/examples.html) | มนุษย์ + เอเจนต์ | แพ็กเกจจริง: แอป CLI, เมลสเปซ, GPU, คอร์ปัส |
| [`/llms.txt`](/llms.txt) | เอเจนต์ | ดัชนีสำหรับเครื่อง — เริ่มที่นี่หากคุณเป็นโมเดล |
| [คู่มือเอเจนต์](/agents/index.md) | เอเจนต์ | วิธีเรียนรู้ Faber และจัดส่งแพ็กเกจ |
| [ทักษะเอเจนต์](/.well-known/agent-skills/index.json) | เอเจนต์ | คู่มือทักษะเฉพาะด้าน (ติดตั้ง, ภาษา, ตัวอย่าง, …) |

## สถานะพอร์ทัล {#portal-status}

หน้านี้ `/` คือ Speculum Porta สำหรับไซตภาษาอังกฤษ: จุดเข้าที่ไม่มีโลแคลซึ่งนำทางผู้ใช้ไปยังหน้า install/start, นำทางเอเจนต์ไปยังพื้นผิวสำหรับเครื่อง และระบุสถานะชุดโลแคลโดยไม่ต้องเจรจาผ่านเบราว์เซอร์ Stage 7 เป็นการพิสูจน์แบบหลายโลแคลบางส่วน ไม่ใช่ไซตที่แปลเสร็จสมบูรณ์: เฉพาะ `th-TH`, `zh-Hans`, `zh-Hant`, `vi`, `ar`, และ `hi` เท่านั้นที่มีพอร์ทัล/start ที่เขียนและสร้างขึ้น พร้อมหน้าแบบคอร์ปัสที่สร้างขึ้น แต่ร้อยแก้วที่เขียนยังคงถอยกลับเป็นภาษาอังกฤษ

| โลแคล | สถานะ | หมายเหตุ |
|---|---|---|
| `la` | ไซตจริงที่ใช้งานจริง | ไซตภาษาอังกฤษ/ละตินที่สร้างเต็มรูปแบบ |
| `th-TH` | Stage 7 พิสูจน์บางส่วน | พอร์ทัล/start slice ที่เขียนบวกคอร์ปัสที่สร้างขึ้น; ร้อยแก้วภาษาอังกฤษถอยกลับ; เอกสารที่เขียนเต็มรออยู่ |
| `zh-Hans` | Stage 7 พิสูจน์บางส่วน | พอร์ทัล/start slice ที่เขียนบวกคอร์ปัสที่สร้างขึ้น; ร้อยแก้วภาษาอังกฤษถอยกลับ; เอกสารที่เขียนเต็มรออยู่ |
| `vi` | Stage 7 พิสูจน์บางส่วน | พอร์ทัล/start slice ที่เขียนบวกคอร์ปัสที่สร้างขึ้น; ร้อยแก้วภาษาอังกฤษถอยกลับ; เอกสารที่เขียนเต็มรออยู่ |
| `zh-Hant` | Stage 7 พิสูจน์บางส่วน | พอร์ทัล/start slice ที่เขียนบวกคอร์ปัสที่สร้างขึ้น; ร้อยแก้วภาษาอังกฤษถอยกลับ; เอกสารที่เขียนเต็มรออยู่ |
| `ar` | Stage 7 พิสูจน์บางส่วน | พอร์ทัล/start slice ที่เขียนบวกคอร์ปัสที่สร้างขึ้น; ร้อยแก้วภาษาอังกฤษถอยกลับ; เอกสารที่เขียนเต็มรออยู่ |
| `hi` | Stage 7 พิสูจน์บางส่วน | พอร์ทัล/start slice ที่เขียนบวกคอร์ปัสที่สร้างขึ้น; ร้อยแก้วภาษาอังกฤษถอยกลับ; เอกสารที่เขียนเต็มรออยู่ |

ตัวอย่างจริงในภาษาละติน:

```faber
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
```

ดู [ภาษาโลแคลผู้อ่าน](/features/reader-locale.html) สำหรับโปรแกรมเชิงความหมายเดียวกันที่แสดงผ่านชุดภาษาไทย จีนตัวย่อ จีนตัวเต็ม อาหรับ ฮินดี และเวียดนาม

## ภาพรวม {#overview}

Faber ออกแบบรอบแนวคิดหลัก: intermediate representation คือความจริง และไม่มีเป้าหมายหรือพื้นผิวภาษามนุษย์ใดได้รับสิทธิพิเศษ โปรแกรม Faber ที่เขียนด้วยคีย์เวิร์ดภาษาละตินสามารถแสดงผลเป็นคีย์เวิร์ดภาษาไทย อาหรับ หรือจีนผ่านกลไกเดียวกับที่แสดงผลเป็น Rust, Go หรือ WebAssembly — เพราะ HIR คือผู้มีอำนาจ และทุกเอาต์พุตคือ *การแสดงผล* ของมัน

ภาษานี้เลือกสัญญาณสามอย่างที่ทำงานร่วมกันอย่างจงใจ:

- **การประกาศแบบไทป์-เฟิร์สต์** — รูปร่างอ่านไปทางการผูก: `textus nomen` ไม่ใช่ `nomen: textus`
- **คำศัพท์เชิงพฤติกรรมภาษาละติน** — การประกาศ คำสั่ง และวงจรชีวิต: `functio`, `genus`, `fixum`, `redde`, `si`
- **สัญลักษณ์เชิงโครงสร้าง** — การไหลของค่าและจุดเชื่อมชนิด: `←` (ผูก), `→` (ชนิดส่งกลับ), `∴` (Branch แบบกระชับ), `≡` (ความเท่ากัน), `∪` (ยูเนียน)

ผลลัพธ์คือซอร์สที่มีรูปร่างทางไวยากรณ์ที่เสถียร ซึ่งสามารถตรวจสอบ แปลง และลดระดับโดยไม่สูญเสียความรู้สึกถึงเจตนาของผู้เขียน

## เอกสาร {#documentation}

| หมวด | คำอธิบาย |
|---|---|
| [ประวัติ](/history/) | เส้นเวลาการพัฒนา อิทธิพล และประวัติรุ่นที่เผยแพร่ |
| [รุ่นที่เผยแพร่](/history/releases.html) | ดาวน์โหลด Faber ล่าสุด พร้อมทุกแท็กและไบนารีที่เผยแพร่ |
| [คุณสมบัติ](/features/) | ภาษาโลแคลผู้อ่าน, เลนการคอมไพล์, คำศัพท์ละติน, ระบบสัญลักษณ์, หลักการออกแบบ |
| [ไวยากรณ์](/syntax/) | เอกสารอ้างอิงครบถ้วน: ชนิด, ฟังก์ชัน, การควบคุมไหล, ข้อผิดพลาด, เจเนอริก, คอลเล็กชัน |
| [เครื่องมือ](/tooling/) | ท่อคอมไพเลอร์ Radix, Faber CLI, เป้าหมายโค้ดเจน, การเขียนสคริปต์ |
| [นิเวศ](/ecosystem/) | Norma, Cista, Triga, coreutils, AI Workbench, คอร์ปัส |
| [คอร์ปัส](/corpus/) | หน้าคีย์เวิร์ดและโครงสร้างที่สร้างจากคอร์ปัสสาธารณะ |
| [เอกสารอ้างอิง](/references/) | ไวยากรณ์ EBNF, เอกสารออกแบบ, พื้นที่เก็บ |

## ตัวอย่างด่วน {#quick-example}

ฟังก์ชันง่าย ๆ ที่แสดงรูปแบบหลักของ Faber — พารามิเตอร์แบบไทป์-เฟิร์สต์, ชนิดส่งกลับแบบสัญลักษณ์, ยูเนียน nullable, คำควบคุมภาษาละติน:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## การแสดงผลสด {#live-rendering}

ฟังก์ชัน divide ข้างต้นแสดงผลด้วยชุดภาษาละตินโดยค่าเริ่มต้น คอมไพเลอร์สามารถแสดงผลโปรแกรมเดียวกันในเจ็ดภาษาโลแคลผู้อ่าน — ไทย, จีนตัวย่อ, จีนตัวเต็ม, อาหรับ, ฮินดี, เวียดนาม — โดยแต่ละภาษาจะแมปคีย์เวิร์ดและชนิดไปยังภาษานั้น ในขณะที่สัญลักษณ์และตัวระบุยังคงไม่เปลี่ยนแปลง นี่ไม่ใช่ชั้นการแปลที่ใช้กับหน้าเพจ แต่เป็นกลไกเดียวกับที่คอมไพเลอร์ใช้ในการผลิตซอร์สที่แปลเป็นภาษาท้องถิ่น

ดูเอกสาร [ภาษาโลแคลผู้อ่าน](/features/reader-locale.html) สำหรับการอภิปรายเต็มรูปแบบ

## พื้นที่เก็บ {#repositories}

| พื้นที่เก็บ | บทบาท |
|---|---|
| [faberlang/faber](https://github.com/faberlang/faber) | CLI ผู้ใช้สาธารณะ |
| [faberlang/releases](https://github.com/faberlang/releases) | ทรัพยากร CLI รุ่นที่แท็ก |
| [faberlang/faber-runtime](https://github.com/faberlang/faber-runtime) | ชนิดรันไทม์สำหรับ Rust ที่สร้างขึ้น |
| [faberlang/norma](https://github.com/faberlang/norma) | ซอร์สไลบรารีมาตรฐาน |
| [faberlang/cista](https://github.com/faberlang/cista) | CLI/ไลบรารีร้านค้าแพ็กเกจ |
| [faberlang/triga](https://github.com/faberlang/triga) | ไลบรารีกราฟิกส์ / เรขาคณิต |
| [faberlang/examples](https://github.com/faberlang/examples) | คอร์ปัส, แทร็ค, แพ็กเกจแอปพลิเคชัน |
| [faberlang/faberlang.dev](https://github.com/faberlang/faberlang.dev) | ไซตเอกสารนี้ |
