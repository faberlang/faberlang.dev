+++
translation_kind = "translated"

title = "Coreutils"
section = "ecosystem"
order = 3
sources = [
  "examples/coreutils/ (38 packages, README.md, campaign docs)",
  "examples/coreutils/packages/echo/src/main.fab",
]


prose_hash = "sha256:b413d7a121a8c7e90239de4231360a6ce0ed3d98da0d5752cc0e5bb53490c34d"
code_hash = "sha256:738161c1d064c275b5fb317f3dd18f6cf674c347cbf6d95b5a3e5edcf69af505"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Faber นำ GNU coreutils กลับมาใช้งานใหม่เพื่อเป็นบทพิสูจน์ในเลนแอปพลิเคชัน โปรแกรม CLI เหล่านี้ทำงานได้จริง และแสดงให้เห็นว่า Faber สามารถสร้างไบนารีที่ทำงานร่วมกับ `argv`, `stdio`, รหัสทางออก และการทำงานกับ I/O ของโฮสต์ได้ โดยตรวจสอบความสอดคล้องกับยูทิลิตี GNU บนโฮสต์ผ่านชุดทดสอบความเท่าเทียม

## ยูทิลิตีที่พัฒนาแล้ว {#implemented-utilities}

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

## ตัวอย่าง — echo {#example--echo}

แพ็กเกจ `echo` แสดงรูปแบบการใช้งานของ Faber ที่ใช้ทั่วทั้ง coreutils ได้แก่ คำอธิบายประกอบ CLI การแยกวิเคราะห์ตัวเลือก การทดสอบแบบอินไลน์ด้วย `probandum`/`proba`/`adfirma` และโมดูลร่วมพื้นฐาน:

```faber locale=la
importa ex "norma:consolum" privata consolum
importa ex "../../../common/gnu/format" privata gnu_format

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

## การเรียกใช้ {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
