+++
translation_kind = "translated"

title = "Variables and binding"
section = "syntax"
order = 2
sources = [
  "radix/README.md (Runtime binding vs structural definition, Language Orientation)",
  "examples/corpus/fixum/",
  "examples/corpus/sit/",
]


prose_hash = "sha256:2e0180766e816022e87ea9eb6c8c531d30993227db9aa56c9224c9a98d3d984f"
code_hash = "sha256:122027c8f10ed33d224e3b23653279e91d19d9a17f432190340909eea5dd9ab3"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber มีคีย์เวิร์ดสำหรับตัวแปรสามแบบและมีสัญลักษณ์การกำหนดค่าโดยเฉพาะ ความแตกต่างสำคัญอยู่ระหว่าง `fixum` (เขียนได้ครั้งเดียว) กับ `varia` (กำหนดค่าใหม่ได้อย่างอิสระ) และระหว่าง `←` (ลำดับการทำงานขณะรันไทม์) กับ `=` (รูปแบบฟิลด์เชิงโครงสร้าง)

## fixum — การผูกค่าที่ไม่เปลี่ยนแปลง {#fixum-immutable-binding}

การผูกค่าด้วย `fixum` เขียนได้ครั้งเดียว สามารถประกาศพร้อมตัวกำหนดค่าเริ่มต้นหรือไม่มีก็ได้ หากประกาศโดยไม่มีตัวกำหนดค่าเริ่มต้น ต้องกำหนดค่าให้พอดีหนึ่งครั้งก่อนอ่านค่า การกำหนดค่าครั้งที่สองจะถูกปฏิเสธ

```faber
fixum numerus count ← 0
fixum textus name ← "Marcus"
fixum _ inferred ← [1, 2, 3]
```

การกำหนดค่าเริ่มต้นภายหลัง:

```faber
incipit {
    fixum numerus factor
    si verum {
        factor ← 10
    } secus {
        factor ← 100
    }
    nota factor
}
```

## varia — การผูกค่าที่เปลี่ยนแปลงได้ {#varia-mutable-binding}

การผูกค่าด้วย `varia` สามารถกำหนดค่าใหม่ได้อย่างอิสระ:

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

## sit — รูปแบบย่อของการผูกค่าคงที่แบบอนุมานชนิด {#sit-inferred-immutable-sugar}

`sit` เป็นรูปแบบย่อของ `fixum _` — การผูกค่าที่ไม่เปลี่ยนแปลงซึ่งอนุมานชนิดข้อมูล:

```faber
incipit {
    sit salve ← "Salve"
    sit nomen ← "Marcus"
    sit x ← 42

    # Deferred form
    sit label
    label ← "deferred"
}
```

## การผูกค่าขณะรันไทม์เทียบกับการกำหนดโครงสร้าง {#runtime-binding-vs-structural-definition}

Faber แยกสิ่งที่ภาษาส่วนใหญ่มักรวมไว้ภายใต้ `=` ออกเป็นสองความหมาย:

| สัญลักษณ์ | บทบาท | ใช้สำหรับ |
|-------|------|---------|
| `←` | ลำดับการทำงานขณะรันไทม์ | การผูกค่าเริ่มต้น การกำหนดค่าใหม่ การเปลี่ยนแปลงค่า |
| `=` | รูปแบบเชิงโครงสร้าง | ชื่อฟิลด์ภายในลิเทอรัลและเมทาดาทา |

```faber
genus Point {
    numerus x
    numerus y
}

incipit {
    # Runtime: ← attaches a value to a name at execution time
    varia numerus count ← 0
    varia textus label ← "ready"
    count ← count + 1

    # Structural: = defines field values inside a type literal
    fixum _ p ← Point {
        x = 10,
        y = 20
    }
}
```

## การดึงฟิลด์ด้วย ex {#ex-field-extraction}

`ex` ใช้ดึงฟิลด์จากค่าออกมาเป็นการผูกค่าในขอบเขตภายใน:

```faber
genus Persona {
    textus nomen
    numerus aetas
}

incipit {
    fixum _ p ← Persona { nomen = "Marcus", aetas = 30 }
    ex p fixum nomen, aetas
    # prints "Marcus"
    nota nomen
}
```

## การเพิ่มและลดค่าต่อท้าย {#postfix-increment-and-decrement}

`⊕` และ `⊖` เป็นคำสั่งเพิ่มหรือลดค่าต่อท้ายสำหรับตำแหน่ง `numerus` ที่เปลี่ยนแปลงได้ คำสั่งเหล่านี้ใช้ได้เฉพาะในรูปคำสั่งเท่านั้น — ไม่มีค่าผลลัพธ์แบบนิพจน์ และไม่มีรูปนำหน้า:

```faber
incipit {
    varia numerus i ← 0
    # i becomes 1
    i ⊕
    # i becomes 0
    i ⊖
}
```
