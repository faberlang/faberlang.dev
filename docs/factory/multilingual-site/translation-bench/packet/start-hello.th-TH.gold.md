+++
title = "สวัสดี Faber"
section = "hello"
order = 2
sources = []

translation_kind = "translated"


prose_hash = "sha256:3a78129bf3787f7c726e39104c95fe9bde78855c4a9f63650410c5cef9610067"
code_hash = "sha256:1ee50be729b09d1bfba27a1f994ef4d1a47c73a645764f9d5986c9bab1aecfb8"
source_commit = "ee93015caac71f7b89ddef8d9010ffbe22d6cd7e"
source_locale = "en-US"
+++
เขียนโปรแกรม Faber ที่เล็กและมีประโยชน์ที่สุด: จุดเข้าของแพ็กเกจที่จัดรูปแบบสตริงแล้วพิมพ์ออก

## ข้อกำหนดเบื้องต้น {#prerequisites}

ทำตาม [ติดตั้งและดาวน์โหลด](/start/install.html) ให้เสร็จก่อน คุณควรมีไบนารี `faber` บน `PATH` และเชลล์ในไดเรกทอรีที่สร้างไฟล์ได้

## สร้างแพ็กเกจ {#create-package}

```bash
mkdir salve-munde
cd salve-munde
mkdir src
cat > faber.toml <<'EOF'
[package]
name = "salve-munde"
version = "0.1.0"
EOF
cat > src/main.fab <<'EOF'
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
EOF
```

## ตรวจสอบ {#check}

```bash
faber check .
```

`faber check` รันส่วนหน้า: lexing, parsing, type checking และการ lower ให้พอจับข้อผิดพลาดทั่วไปของแพ็กเกจโดยไม่สร้างไบนารีเนทีฟ หากคำสั่งล้มเหลว ให้อ่านรหัส diagnostic ก่อน — diagnostic ของ Faber ตั้งใจให้เป็นตัวค้นหาที่เสถียร

## รัน {#run}

```bash
faber run .
```

ผลลัพธ์ที่คาดหวัง:

```text
Salve, munde!
```

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
