## System prompt snippet (reader pack)

Emit Thai reader-locale Faber using Thai keywords for declarations, control flow, loops, returns, booleans, common primitive types, and lista/tabula collections. Keep Faber glyph syntax unchanged.

## Instructions

Translate the prose below from English to the target locale. Follow these rules:

- Translate prose only. Do NOT translate code fences.
- Preserve {#anchors} (heading anchors) exactly.
- Preserve markdown structure (headings, paragraphs, lists).
- Preserve table shapes (column count, alignment).
- Preserve links. Paths may stay absolute (/start/...) since the generator prefixes locale paths.
- Fences are shown as "<<<FENCE n>>>" markers. Leave these markers unchanged in your output.
- Return the full body text with markers in place.

## English source body (fences as <<<FENCE n>>>)

Write the smallest useful Faber program: a package entry point that formats a
string and prints it.

## Prerequisites {#prerequisites}

Complete [Install and download](/start/install.html) first. You should have a
`faber` binary on your `PATH` and a shell in a working directory where you can
create files.

## Create a package {#create-package}

<<<FENCE 0>>>

## Check it {#check}

<<<FENCE 1>>>

`faber check` runs the front end: lexing, parsing, type checking, and lowering
far enough to catch ordinary package mistakes without building a native binary.
If the command fails, read the diagnostic code first; Faber diagnostics are
intended to be stable search handles.

## Run it {#run}

<<<FENCE 2>>>

Expected output:

<<<FENCE 3>>>

## What you just used {#what-you-used}

| Source | Meaning |
|---|---|
| `functio salve(textus nomen) → textus` | Function named `salve`, type-first parameter, text return |
| `fixum textus msg ← ...` | Immutable binding |
| `"Salve, §!"(nomen)` | Format string with display interpolation |
| `redde msg` | Return |
| `incipit` | Package entry point |
| `nota m` | Print a note/output value |

## Locale proof {#locale-proof}

The program above is the canonical Latin reader rendering. Reader locales can
render the same semantic program with different keyword packs while preserving
glyphs and identifiers. Start with the full proof at
[Reader locale](/features/reader-locale.html) before writing non-Latin packages.

## Next {#next}

| Previous | Next |
|---|---|
| [Install and download](/start/install.html) | [Commands you will use](/start/commands.html) |


## Current locale body (fences as <<<FENCE n>>>)

เขียนโปรแกรม Faber ที่เล็กและมีประโยชน์ที่สุด: จุดเข้าของแพ็กเกจที่จัดรูปแบบสตริงแล้วพิมพ์ออก

## ข้อกำหนดเบื้องต้น {#prerequisites}

ทำตาม [ติดตั้งและดาวน์โหลด](/start/install.html) ให้เสร็จก่อน คุณควรมีไบนารี `faber` บน `PATH` และเชลล์ในไดเรกทอรีที่สร้างไฟล์ได้

## สร้างแพ็กเกจ {#create-package}

<<<FENCE 0>>>

## ตรวจสอบ {#check}

<<<FENCE 1>>>

`faber check` รันส่วนหน้า: lexing, parsing, type checking และการ lower ให้พอจับข้อผิดพลาดทั่วไปของแพ็กเกจโดยไม่สร้างไบนารีเนทีฟ หากคำสั่งล้มเหลว ให้อ่านรหัส diagnostic ก่อน — diagnostic ของ Faber ตั้งใจให้เป็นตัวค้นหาที่เสถียร

## รัน {#run}

<<<FENCE 2>>>

ผลลัพธ์ที่คาดหวัง:

<<<FENCE 3>>>

## สิ่งที่คุณเพิ่งใช้ {#what-you-used}

| ต้นทาง | ความหมาย |
|---|---|
| `functio salve(textus nomen) → textus` | ฟังก์ชันชื่อ `salve` พารามิเตอร์แบบ type-first คืนค่า textus |
| `fixum textus msg ← ...` | การผูกค่าแบบ immutable |
| `"Salve, §!"(nomen)` | สตริงรูปแบบพร้อมการแทรกค่าเพื่อแสดงผล |
| `redde msg` | คืนค่า |
| `incipit` | จุดเข้าแพ็กเกจ |
| `nota m` | พิมพ์ค่าหมายเหตุ/ผลลัพธ์ |

## หลักฐาน reader locale {#locale-proof}

โปรแกรมด้านบนคือการเรนเดอร์ reader แบบละตินมาตรฐาน Reader locale สามารถเรนเดอร์โปรแกรมความหมายเดียวกันด้วยชุดคำสำคัญต่างกัน โดยคง glyph และ identifier ไว้ ดูหลักฐานเต็มที่ [Reader locale](/features/reader-locale.html) ก่อนเขียนแพ็กเกจที่ไม่ใช่ละติน

## ถัดไป {#next}

| ก่อนหน้า | ถัดไป |
|---|---|
| [ติดตั้งและดาวน์โหลด](/start/install.html) | [คำสั่งที่คุณจะใช้](/start/commands.html) |


## Notes

Source file: /Users/ianzepp/work/faberlang/faberlang.dev/src/en-US/start/hello.md
Locale file: /Users/ianzepp/work/faberlang/faberlang.dev/src/th-TH/start/hello.md
