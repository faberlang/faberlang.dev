+++
translation_kind = "translated"

title = "Language corpus"
section = "ecosystem"
order = 6
sources = [
  "examples/corpus/ (292 .fab files, 174 registry terms, index.toml)",
  "examples/corpus/README.md",
]


prose_hash = "sha256:6dab4295fafeea620e65bd30edcc6c810bc3f0b11cb8681aae63f79ecbe2be63"
code_hash = "sha256:fbdcbf8ce9cd3fdcb367022a7df1cdbd74fd62244d662a6a85229773e4910739"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
คลังข้อมูลภาษาฟาเบอร์คือพจนานุกรมภาษาสาธารณะ โดยมีไดเรกทอรีระดับบนสุดหนึ่งรายการต่อคีย์เวิร์ด กลุ่มโอเปอเรเตอร์ หรือพื้นผิวประเภทภาษาหนึ่งรายการ คลังข้อมูลนี้เป็นแหล่งพัฒนาสำหรับ `faber explain` และเป็นอินพุตหลักสำหรับเมทริกซ์การคอมไพล์หลายเป้าหมาย

## สถิติ {#stats}

- ไฟล์ตัวอย่าง `.fab` จำนวน 292 ไฟล์
- คำศัพท์ในรีจิสทรี `index.toml` จำนวน 174 รายการ
- ไดเรกทอรีคีย์เวิร์ดและแนวคิดประมาณ 135 รายการ

## โครงสร้าง {#layout}

```
corpus/
  functio/           # function keyword exemplars
  genus/             # record type exemplars
  si/                # conditional branch exemplars
  itera/             # iteration exemplars
  lista/ tabula/     # collection type exemplars
  tensor/ sparsa/    # tensor exemplars
  ad/                # capability call exemplars
  operatores/        # glyph / operator groups
  ...
  index.toml         # generated explain manifest
```

## รูปแบบไฟล์ {#file-format}

ไฟล์ `.fab` แต่ละไฟล์เริ่มต้นด้วยฟรอนต์แมตเทอร์ TOML ที่อธิบายคำศัพท์นั้น:

```toml
+++
term = "functio"
kind = "keyword"
category = "function"
canonical = true
summary = "Declares a named function or method."
syntax = "functio <name>(<params>) [modifiers] [→ <type>] [⇥ <error-type>] <block>"
aliases = ["function"]
related = ["→", "⇥", "redde", "sponte"]
+++

functio saluta() {
    nota "Salve, Mundus!"
}
```

## การใช้งาน {#usage}

```bash
faber explain functio       # show keyword reference
faber explain ≡             # show glyph reference
faber explain --search query # search across corpus
faber explain --list         # list all terms
```

## หมวดหมู่ {#categories}

คำศัพท์จัดเป็นหมวดหมู่ดังนี้: `function`, `control-flow`, `type`,
`collection`, `transfer`, `annotation`, `iteration`, `destructuring`,
`testing`, `cli`, `concept`, `operator-group`, `existing-home`
