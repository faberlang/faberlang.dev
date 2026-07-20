+++
translation_kind = "translated"

title = "Capability calls and frames"
section = "features"
order = 3
sources = []


prose_hash = "sha256:73113e85aed18df405d85a15f57dbf3cc159c46fc6619396ab03a18bcf29007f"
code_hash = "sha256:85216f4b5f4405e693c3b4f1e237565bc609da16172a0225ff18098fe6397ce4"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
*รอยต่อระหว่าง Faber กับทุกวิธีที่ระบบปฏิบัติการสามารถใช้เพื่อทำ I/O ได้*

`ad` คือ primitive สำหรับเรียกใช้ความสามารถระดับต่ำของ Faber ซึ่งเป็นขอบเขต
ระหว่างโค้ด Faber กับโลกภายนอก โดยจะเปิดบทสนทนาแบบมีชนิดข้อมูล
(`sermo`) กับทรัพยากรของโฮสต์ที่ระบุด้วยสตริงเส้นทาง จากนั้นแลกเปลี่ยน
เฟรมที่มีโครงสร้าง (`scrinium`) ผ่านสตรีมย่อยแบบกำหนดทิศทาง
เคอร์เนลของโฮสต์จะส่งแต่ละเส้นทางไปยัง crate ผู้ให้บริการที่ถอดเปลี่ยนได้
ซึ่งเป็นผู้ทำ I/O จริง เช่น ระบบไฟล์ เครือข่าย คอนโซล เวลา ความสุ่ม
หรือสิ่งอื่นใดที่ระบบปฏิบัติการทำได้

## primitive `ad` {#ad}

`ad` เป็นคีย์เวิร์ด ไม่ใช่ฟังก์ชัน โดยจะเปิดบทสนทนาแบบทึบแสง
ด้วยเส้นทางที่ระบุด้วยลิเทอรัล `ascii` และข้อมูลสำหรับเปิดที่เป็นตัวเลือก:

```text
# Simple materialized call: open, send opener, drain response
fixum textus content ← ad 'solum:lege' ("config.toml") ↦ textus

# Typed conversation handle for streaming interaction
fixum sermo s ← ad 'processus:curre' ("ls", ["-la"])
```

สตริงเส้นทางใช้รูปแบบ `prefix:verb` เคอร์เนลของโฮสต์จะจับคู่เฉพาะ
**prefix เท่านั้น** ส่วนผู้ให้บริการจะเป็นเจ้าของ verb ทั้งหมดภายใต้ prefix นั้น:

```text
solum:lege   ─┐
solum:modum  ─┼─►  prefix "solum"  ──►  solum provider crate
solum:vincula─┘
```

`ad` ไม่ใช่อินเทอร์เฟซสำหรับเรียกใช้ฟังก์ชันภายนอก ไม่ได้เรียกฟังก์ชัน C
โหลดไลบรารีแบบไดนามิก หรือฝังแอสเซมบลีแบบอินไลน์ แต่เป็นขอบเขตการส่ง
ข้อความที่มีโครงสร้าง: Faber ส่งเฟรมที่มีชนิดข้อมูลและรับเฟรมที่มีชนิดข้อมูล
โดยไม่จำเป็นต้องรู้ว่าผู้ให้บริการเขียนด้วย Rust ทำงานอยู่ในโปรเซสเดียวกัน
ส่งต่อไปยัง system call หรือส่งต่อไปยังโฮสต์ระยะไกล

## ชนิดของเฟรม {#types}

ชนิดข้อมูลห้าชนิดที่คอมไพเลอร์เป็นเจ้าของประกอบกันเป็นระบบเฟรม:

| ชนิด | บทบาท | ส่วนสำคัญ |
|------|------|-------------|
| `sermo` | แฮนเดิลบทสนทนา — การแลกเปลี่ยนสองทิศทางที่กำลังทำงานอยู่ | สร้างโดย `ad`; ระบายผ่าน `↦ T` หรือแยกเป็นมุมมอง |
| `scrinium<T>` | กล่องหุ้มเฟรม — ข้อความที่มีโครงสร้างหนึ่งข้อความในบทสนทนา | ฟิลด์: `id`, `call`, `status`, `data`, `created_ms`, `from`, `trace` |
| `status` | enum ที่ระบุสถานะวงจรชีวิต | `request`, `item`, `byte`, `bulk`, `done`, `error`, `cancel` |
| `meus<T>` | สตรีมย่อยขาออก — ส่งเฟรมไปยังผู้ให้บริการ | `da(T)`, `fini() → status` |
| `tuus<T>` | สตรีมย่อยขาเข้า — รับเฟรมจากผู้ให้บริการ | `accipe()`, `cursor()`, `exhauri()`, `fini()` |

### การใช้มุมมองแบบกำหนดทิศทาง {#using-directional-views}

```text
# Open a conversation, get directional views
fixum sermo s ← ad 'solum:scribe' ("output.txt")
fixum meus<textus> out ← s.meus<textus>()
fixum tuus<textus> input ← s.tuus<textus>()

# Send content frames
out.da("line one")
out.da("line two")
out.fini()

# Read response frames
itera ex input.cursor() fixum frame {
    nota frame.data
}
fixum status inbound ← input.fini()
```

### การทำให้เป็นค่าทั่วไป {#simple-materialization}

สำหรับกรณีทั่วไป — เปิด ส่งข้อมูลสำหรับเปิด และระบายเฟรมตอบกลับทั้งหมด
ลงในค่าเดียว — `sermo ↦ T` จะรวมบทสนทนาให้เสร็จในขั้นตอนเดียว:

```text
# Read a file: open + drain into textus
fixum textus body ← ad 'solum:lege' ("config.toml") ↦ textus

# Parse JSON from an HTTP response
fixum json data ← ad 'http:peti' ("https://api.example.com/data") ↦ json
```

การทำให้เป็นค่าใช้ตัวรวบรวมที่กำหนดตามชนิดข้อมูล: `↦ textus`
จะนำเฟรมขาเข้าทั้งหมดมาต่อกัน, `↦ json` จะแยกวิเคราะห์ payload
ที่ต่อกันแล้ว, ส่วน `↦ lista<T>` จะรวบรวมเฟรมเป็นรายการ

## ผู้ให้บริการของโฮสต์ {#providers}

กลุ่มผลกระทบถูกนำไปใช้งานเป็น crate ผู้ให้บริการแยกกันภายใต้
`faberlang/host-providers-rs` ผู้ให้บริการแต่ละรายเป็นเจ้าของ verb ทั้งหมด
ภายใต้ prefix ของตน:

| ผู้ให้บริการ | Prefix | ขอบเขต I/O |
|----------|------|------------|
| `solum` | `solum:*` | ระบบไฟล์: อ่าน เขียน เมทาดาทา และการดำเนินการกับไดเรกทอรี |
| `processus` | `processus:*` | การเรียกใช้โปรเซส: สร้าง เชื่อม pipe และรหัสการออก |
| `consolum` | `consolum:*` | I/O ของคอนโซล: stdin, stdout, stderr |
| `tempus` | `tempus:*` | เวลา: เวลาปัจจุบัน การหยุดรอ และตัวจับเวลา |
| `aleator` | `aleator:*` | ความสุ่ม: เอนโทรปี และการแจกแจง |
| `http` | `http:*` | ไคลเอนต์ HTTP (Tier D เมื่อรวมเข้าระบบแล้ว) |

ผู้ให้บริการเป็น crate แยกกันและมี dependency ของตนเอง — `solum`
จะไม่ดึง HTTP เข้ามา และ `http` จะไม่ดึงโค้ดระบบไฟล์เข้ามา
ผู้ให้บริการแต่ละรายส่งออกฟังก์ชัน `register()` ซึ่ง manifest ของโฮสต์
ที่สร้างขึ้นจะเรียกใช้เมื่อเริ่มต้นระบบ

## ชั้นสถาปัตยกรรม {#layers}

```text
Faber source:     ad 'solum:lege' (path) ↦ textus
Compiler:         sermo open + generic attach (no provider crate names)
Runtime:          HostDispatch + conversation protocol (faber-runtime)
Kernel:           route(frame) → provider for prefix
Provider:         solum provider reads file, returns content
```

คอมไพเลอร์จะสร้างโค้ด dispatch แบบทั่วไปเท่านั้น — จะไม่ฝังชื่อ crate
ผู้ให้บริการลงในโค้ดที่สร้างขึ้น รันไทม์จะจัดเตรียม `HostDispatch`
และโพรโทคอลของบทสนทนา เคอร์เนล (จาก `host-kernel-rs`) จะส่งเฟรม
ไปยังผู้ให้บริการที่ถูกต้องโดยพิจารณาจาก prefix ผู้ให้บริการ
(จาก `host-providers-rs`) จะทำ I/O จริง

ดังนั้นโค้ด Faber ที่สร้างขึ้นจึง **ไม่ผูกกับผู้ให้บริการ**
ไบนารีที่คอมไพล์แล้วเดียวกันสามารถลิงก์กับการใช้งานผู้ให้บริการที่ต่างกันได้
เช่น ผู้ให้บริการระบบไฟล์จริงสำหรับการใช้งานจริง หรือผู้ให้บริการจำลอง
สำหรับการทดสอบ โดยเปลี่ยน compile manifest

## Compile manifest {#manifest}

ผู้ให้บริการที่จะลิงก์จะถูกควบคุมโดย compile manifest ที่สร้างขึ้น
และตาราง `[dispatch]` ใน `faber.toml`:

```text
[target.rust]
host = "native"

[dispatch]
providers = ["solum", "processus", "consolum", "tempus", "aleator"]

[dispatch.providers.http]
enabled = true
```

ระหว่างการเขียนโปรแกรม หากไม่มีผู้ให้บริการ ระบบจะส่งคืนข้อผิดพลาดรันไทม์
`E_NO_ROUTE` ในโหมด strict (ในอนาคต) ทุก prefix ของ `ad` ในโปรแกรม
ต้องปรากฏอยู่ใน compile manifest และคอมไพเลอร์จะตรวจสอบว่า capability
manifest ของผู้ให้บริการครอบคลุมเส้นทางที่ใช้งานหรือไม่

## สถาปัตยกรรม {#architecture}

แพลตฟอร์มโฮสต์แบ่งออกเป็นสาม repository ในองค์กร
`faberlang`:

| Repository | บทบาท |
|------------|------|
| `host-kernel-rs` | เราเตอร์ขนาดเล็ก — เป็นเจ้าของ `Frame`, `Conversation`, วงจรชีวิตช่วงสิ้นสุด, การ dispatch ตาม prefix, ข้อผิดพลาดที่มีโครงสร้าง (`E_NO_ROUTE`) และการรวม capability manifest |
| `host-native-rs` | การเชื่อมต่อแบบ native — worker, hook เริ่มต้น `register_providers` และการผนวกรวม `host_register.rs` ที่สร้างขึ้น |
| `host-providers-rs` | การใช้งานผู้ให้บริการ — Cargo workspace ที่มี crate แยกตามกลุ่ม (`solum`, `processus` เป็นต้น) |

crate ผู้ให้บริการแต่ละรายเป็นเจ้าของ dependency แบบ native ของตนเอง
ผู้ให้บริการ `http` จะดึง `hyper` และ `tokio` เข้ามาเฉพาะเมื่อเปิดใช้ HTTP
ส่วนผู้ให้บริการ `solum` ใช้ API ไฟล์มาตรฐานโดยไม่มี dependency
ด้านเครือข่ายเพิ่มเติม

> **เส้นทางเดียวกัน ใช้ได้กับทุกโฮสต์** เนื่องจาก `ad` dispatch
> ด้วยสตริงเส้นทางและผู้ให้บริการสามารถถอดเปลี่ยนได้ ซอร์ส Faber เดียวกัน
> จึงสามารถกำหนดเป้าหมายเป็นไบนารี native (`host-native-rs`), รันไทม์ WASM
> (เคอร์เนลโฮสต์ในฐานะอะแดปเตอร์ Frame/Wasm) หรือโปรเซส TypeScript Node.js
> (`host-providers-ts`) ได้โดยไม่ต้องเปลี่ยนโค้ด Faber แม้แต่บรรทัดเดียว

## ตัวห่อหุ้มของ Norma {#stdlib}

โค้ด Faber ส่วนใหญ่ไม่ได้เรียก `ad` โดยตรง ไลบรารีมาตรฐาน Norma
จะห่อหุ้มเส้นทาง `ad` ที่ใช้ทั่วไปไว้ในฟังก์ชันที่มีชนิดข้อมูล:

```text
# Norma wraps ad in typed, reviewed functions
functio lege(textus via) → textus {
    redde ad 'solum:lege' (via) ↦ textus
}

functio scribe(textus via, textus content) → vacuum {
    fixum vacuum _ ← ad 'solum:scribe' (via, content) ↦ vacuum
}

functio curre(textus command, lista<textus> args) → textus {
    redde ad 'processus:curre' (command, args) ↦ textus
}
```

ฟังก์ชันตัวห่อหุ้มเหล่านี้ให้ความปลอดภัยด้านชนิดข้อมูล เอกสารประกอบ
และการจัดการข้อผิดพลาด โดยไม่ซ่อนข้อเท็จจริงที่ว่า I/O ข้ามขอบเขต
ของ `ad` ตัวห่อหุ้มของ Norma เป็นโอเพนซอร์สและอยู่ภายใต้
`norma/src/`

## เอกสารอ้างอิง {#references}

1. `radix/docs/design/frame-stream-types.md` — ข้อกำหนดฉบับเต็มของ sermo, scrinium, status, meus, tuus
2. `radix/docs/design/host-provider-gateway.md` — สถาปัตยกรรมเราเตอร์ขนาดเล็ก สัญญาของผู้ให้บริการ และ compile manifest
3. `faberlang/host-kernel-rs/` — การใช้งานเราเตอร์เคอร์เนล
4. `faberlang/host-native-rs/` — การเชื่อมต่อและการลงทะเบียนแบบ native
5. `faberlang/host-providers-rs/` — crate ผู้ให้บริการ (solum, processus, consolum, tempus, aleator, http)
6. `examples/corpus/ad/` — ไฟล์ตัวอย่าง sermo
