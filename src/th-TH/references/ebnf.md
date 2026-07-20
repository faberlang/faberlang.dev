+++
translation_kind = "translated"

title = "EBNF grammar"
section = "references"
order = 1
sources = [
  "radix/EBNF.md",
]


prose_hash = "sha256:901fe46feace9eaea92780fc259f6ae17c168dba45fe1ff9c0ee95e8c4858ea2"
code_hash = "sha256:4f0d91b053057a4ac78a57bb7ecb6914b647b3bd8c5855e3696e48f2c32fc265"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
ไวยากรณ์ Faber ฉบับมาตรฐานกำหนดไว้ในรีโพซิทอรี Radix ที่
`radix/EBNF.md` ซึ่งเป็นแหล่งอ้างอิงอย่างเป็นทางการสำหรับไวยากรณ์ภาษาทั้งหมด

ไวยากรณ์ครอบคลุม:

- โครงสร้างเชิงคำศัพท์ (อักขระพิเศษ คีย์เวิร์ด ลิเทอรัล และคอมเมนต์)
- การประกาศ (`functio`, `genus`, `implendum`, `typus`, `discretio`, `ordo`)
- คำสั่ง (การผูกค่า การควบคุมการไหล การคืนค่า และการวนซ้ำ)
- นิพจน์ (การเรียกใช้ ตัวดำเนินการ การแปลงค่า และลิเทอรัล)
- คำกำกับ (`@` syntax)
- คำกำกับ CLI (`@ cli`, `@ optio`, `@ operandus`, `@ imperium`)
- นิพจน์ชนิดข้อมูล (ชนิดพื้นฐาน เจเนอริก และรูปแบบย่อ)
- ระบบโมดูล (`importa`)

```ebnf
(* excerpt: function declaration *)
funcDecl = 'functio' ident genericParams? '(' paramList ')' ('→' type)? ('⇥' type)? block;
block    = '{' stmt* '}';
```
