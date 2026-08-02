+++
translation_kind = "translated"

title = "Grammar"
section = "reference"
order = 1
sources = [
  "radix/EBNF.md",
]
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
