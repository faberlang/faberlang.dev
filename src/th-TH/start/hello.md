+++
translation_kind = "translated"

title = "สวัสดี Faber"
section = "hello"
order = 2
sources = []




prose_hash = "sha256:3a78129bf3787f7c726e39104c95fe9bde78855c4a9f63650410c5cef9610067"
code_hash = "sha256:1ee50be729b09d1bfba27a1f994ef4d1a47c73a645764f9d5986c9bab1aecfb8"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
เขียนโปรแกรม Faber ที่มีประโยชน์ในขนาดเล็กที่สุด: จุดเริ่มต้นของแพ็กเกจที่จัดรูปแบบสตริงและพิมพ์ผลลัพธ์

## ข้อกำหนดเบื้องต้น {#prerequisites}

ทำ [ติดตั้งและดาวน์โหลด](/start/install.html) ให้เสร็จก่อน คุณควรมีไบนารี
`faber` อยู่ใน `PATH` และมีเชลล์ที่ทำงานอยู่ในไดเรกทอรีซึ่งคุณสามารถสร้างไฟล์ได้

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

## ตรวจสอบแพ็กเกจ {#check}

```bash
faber check .
```

`faber check` จะเรียกใช้ส่วนหน้าของคอมไพเลอร์ ได้แก่ การวิเคราะห์โทเค็น
การแยกวิเคราะห์ การตรวจสอบชนิด และการลดรูปในระดับที่เพียงพอสำหรับตรวจจับ
ข้อผิดพลาดทั่วไปของแพ็กเกจ โดยไม่ต้องสร้างไบนารีเนทีฟ

หากคำสั่งล้มเหลว ให้อ่านรหัสการวินิจฉัยก่อน การวินิจฉัยของ Faber ออกแบบมาให้
ใช้เป็นคำค้นหาอ้างอิงที่มีความเสถียร

## เรียกใช้แพ็กเกจ {#run}

```bash
faber run .
```

ผลลัพธ์ที่คาดหวัง:

```text
Salve, munde!
```

## สิ่งที่คุณเพิ่งใช้ {#what-you-used}

| แหล่งที่มา | ความหมาย |
|---|---|
| `functio salve(textus nomen) → textus` | ฟังก์ชันชื่อ `salve` พารามิเตอร์แบบชนิดนำหน้า และคืนค่าเป็นข้อความ |
| `fixum textus msg ← ...` | การผูกค่าที่เปลี่ยนแปลงไม่ได้ |
| `"Salve, §!"(nomen)` | สตริงรูปแบบที่มีการแทรกค่าที่แสดงผลได้ |
| `redde msg` | คืนค่า |
| `incipit` | จุดเริ่มต้นของแพ็กเกจ |
| `nota m` | พิมพ์ค่าโน้ตหรือเอาต์พุต |

## การพิสูจน์โลแคล {#locale-proof}

โปรแกรมข้างต้นคือการแสดงผลสำหรับผู้อ่านภาษาละตินที่เป็นมาตรฐาน โลแคลของ
ผู้อ่านสามารถแสดงโปรแกรมเชิงความหมายเดียวกันด้วยชุดคีย์เวิร์ดที่แตกต่างกัน
โดยยังคงรักษาสัญลักษณ์และตัวระบุไว้เหมือนเดิม ดูข้อพิสูจน์ฉบับเต็มได้ที่
[โลแคลของผู้อ่าน](/features/reader-locale.html) ก่อนเขียนแพ็กเกจที่ไม่ใช่
ภาษาละติน

## ถัดไป {#next}

| ก่อนหน้า | ถัดไป |
|---|---|
| [ติดตั้งและดาวน์โหลด](/start/install.html) | [คำสั่งที่คุณจะใช้](/start/commands.html) |
