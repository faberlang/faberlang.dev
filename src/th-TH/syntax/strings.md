+++
translation_kind = "translated"

title = "String and template literals"
section = "syntax"
order = 8
sources = [
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "examples/corpus/literalia/",
  "examples/corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
]


prose_hash = "sha256:61bc93552e4a6ccc2a3a51453c146c31eee8331c6e82a3b17de5bc70f4ce24b0"
code_hash = "sha256:e7cba6e75a702466f92ecdbaa2c9d777b027a09a7f1b0414387cc746376d3075"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber ใช้ความหมายของตัวคั่น โดยรูปแบบเครื่องหมายคำพูดแต่ละแบบหมายถึงรูปร่างของซอร์สโค้ดที่แตกต่างกัน รูปแบบเหล่านี้ไม่ใช่คำพ้องความหมายที่ใช้แทนกันได้

## รูปแบบลิเทอรัล {#literal-forms}

| รูปแบบ | ชนิด | บทบาท |
|------|------|------|
| `'…'` | `ascii` | โทเคนเครื่องจักรแบบคงที่ ไม่รองรับ `§` และไม่รองรับ `(…)` |
| `"…"` | `textus` | สตริง Unicode แบบบรรทัดสั้น โดย `(…)` จะทำการเรนเดอร์ |
| `«…»` | `textus` | Unicode แบบบล็อกหรือหลายบรรทัด โดย `(…)` จะทำการเรนเดอร์ |
| `` `…` `` | `forma` | เทมเพลตที่บันทึกไว้ โดย `(…)` จะจับค่า |
| `{ … }` | `json` | เอกสาร JSON ระหว่างคอมไพล์ |
| `|…|` | `octeti` | ไบต์ฐานสิบหกที่สร้างระหว่างคอมไพล์ |
| `[ … ]` | `lista<T>` | ลิเทอรัลลิสต์ของ Faber |

## การใช้เทมเพลตสตริง {#string-template-application}

Faber จัดรูปแบบข้อความด้วยการใช้เทมเพลตสตริง โดยใช้ลิเทอรัล `"…"` หรือ `«…»` ที่มีช่อง `§` แล้วตามด้วยอาร์กิวเมนต์ในวงเล็บ:

```faber
functio greet(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}

fixum numerus pagina ← 3
fixum numerus totum ← 10
fixum textus code ← "200"
fixum textus label ← "OK"

fixum _ msg ← "Page § of §"(pagina, totum)
fixum _ block ← «status: § (§)»(code, label)
```

กฎสำคัญ:

- `§` (U+00A7) คือช่องของเทมเพลต
- ช่องแบบระบุตำแหน่งใช้ `§0`, `§1`, … เพื่อกำหนดลำดับอย่างชัดเจน
- `!` ท้ายช่องเลือกการจัดรูปแบบเพื่อแสดงผล: `"Salve, §!"(nomen)`
- ส่วนต่อท้าย `(args)` คือการใช้เทมเพลต ไม่ใช่การเรียกฟังก์ชัน

## สตริงแบบบล็อก {#block-strings}

บล็อกหลายบรรทัดใช้เครื่องหมายกีโยแมต์ `«…»`:

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

## เทมเพลตที่บันทึกไว้ (forma) {#captured-templates}

เทมเพลตที่ใช้เครื่องหมายแบ็กทิกจะจับข้อความและพารามิเตอร์ไว้โดยไม่เรนเดอร์ เหมาะสำหรับเพย์โหลด SQL/URL ที่ผูกค่าอย่างปลอดภัย:

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

## JSON แบบอินไลน์ {#inline-json}

`{ … }` เปล่าคือ JSON แบบอินไลน์ ซึ่งเป็นเอกสาร `json` ที่สร้างระหว่างคอมไพล์ ไม่ใช่ออบเจ็กต์ Faber แบบไม่ระบุชนิด คีย์ต้องเป็นสตริงที่ใส่เครื่องหมายคำพูด และคั่นด้วย `:`:

```faber
fixum _ empty ← {}
fixum _ user ← { "name": "Marcus", "age": 30, "active": true }
fixum _ nested ← { "meta": { "version": 1 }, "tags": ["alpha", "beta"] }
```

สำหรับการสร้าง `genus` แบบระบุชนิด ให้ใช้ชื่อชนิดและรูปแบบฟิลด์ที่มี `=`:

```faber
genus Point {
    numerus x
    numerus y
}
fixum _ p ← Point { x = 10, y = 20 }
```
