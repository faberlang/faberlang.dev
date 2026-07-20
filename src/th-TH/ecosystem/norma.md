+++
translation_kind = "translated"

title = "Norma standard library"
section = "ecosystem"
order = 1
sources = [
  "radix/README.md (Standard Library section)",
  "sibling norma/ repository",
  "norma/exempla/",
  "radix/docs/stdlib/morphologia.md",
]


prose_hash = "sha256:f333d0ee78b78e5ad3ebfb1bfdda0a4069a9b7daf3579d8c55d6b83c668be833"
code_hash = "sha256:0ef63774f36a5e950889dcae691b2a9c5add05fe03c89c061ba60d829195f2ff"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Norma คือไลบรารีมาตรฐานของ Faber ไลบรารีนี้มีโมดูลชื่อภาษาละตินแบบแบน ซึ่งเข้าถึงผ่านพาธ `norma:*` การประกาศของไลบรารีมาตรฐานเป็นซอร์ส Faber ที่อยู่ในรีโพซิทอรี `norma` ซึ่งอยู่เคียงข้างกัน

## โมดูล {#modules}

| โมดูล | ขอบเขตการทำงาน |
|--------|--------|
| `norma:solum` | การดำเนินการกับระบบไฟล์ |
| `norma:solum/path` | การดำเนินการกับพาธแบบบริสุทธิ์ |
| `norma:http` | ไคลเอ็นต์ HTTP |
| `norma:processus` | การเรียกใช้กระบวนการ |
| `norma:consolum` | อินพุตและเอาต์พุตคอนโซล (stdin, stdout, stderr) |
| `norma:json` | การแยกวิเคราะห์และการทำให้เป็นอนุกรม JSON |
| `norma:toml` | การแยกวิเคราะห์ TOML |
| `norma:yaml` | การแยกวิเคราะห์ YAML |
| `norma:valor` | การนำทางในโคเดก |
| `norma:tensor` | ตัวช่วยเชื่อมต่อเทนเซอร์ |
| `norma:tempus` | เวลาและช่วงเวลา |
| `norma:aleator` | ค่าที่สุ่ม |

## หลักเกณฑ์การตั้งชื่อแบบ Morphologia {#morphologia-naming-convention}

Norma ปฏิบัติตามนโยบาย `morphologia` สำหรับชื่อเมธอดทั้งหมด การผันกริยาภาษาละตินใช้ระบุโหมดการทำงาน:

| รากคำ | ซิงโครนัส | อะซิงโครนัส | ความหมาย |
|------|------|---------|---------|
| `leg-` | `lege` | `leget` | อ่าน |
| `scrib-` | `scribe` | `scribet` | เขียน |
| `quaer-` | — | `quaeret` | คิวรี (ส่งคืนผลลัพธ์) |
| `quaer-` | — | `quaerent` | คิวรี (สตรีม) |

คู่การเป็นเจ้าของ (กลายพันธุ์เทียบกับคัดลอกออก):

| กลายพันธุ์ | คัดลอกออก | ความหมาย |
|---------|---------|---------|
| `adde` | `addita` | เพิ่ม |
| `inverte` | `inversa` | กลับลำดับ |
| `filtra` | `filtrata` | กรอง |

## การใช้งาน {#usage}

```faber locale=la
importa ex "norma:solum" privata solum

functio legeConfig() → textus {
    redde solum.lege("config.toml")
}
```
