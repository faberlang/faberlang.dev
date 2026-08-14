+++
translation_kind = "translated"

title = "Types and values"
section = "language"
order = 2
sources = [
  "radix/README.md (Core Type Surfaces, Numeric Widths, Tensors And Sparsa, GPU Core Types)",
  "radix/docs/design/numeric-type-sugar.md",
  "radix/docs/design/tensor-intrinsics.md",
  "radix/docs/design/lista-intrinsics.md",
  "radix/docs/design/comparison-operators.md",
  "faber/docs/EBNF.md",
  "examples/corpus/typi/",
  "examples/corpus/tensor/",
  "examples/corpus/lista/",
  "radix/README.md (Runtime binding vs structural definition, Language Orientation)",
  "examples/corpus/fixum/",
  "examples/corpus/sit/",
  "radix/README.md (Tensors And Sparsa)",
  "radix/docs/design/tabula-intrinsics.md",
  "examples/corpus/tabula/",
  "examples/corpus/sparsa/",
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "examples/corpus/literalia/",
  "examples/corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
  "radix/README.md (Nullability and Optionality)",
  "examples/corpus/nihil/",
  "examples/corpus/sponte/",
  "examples/corpus/nonnihil/",
  "radix/README.md (Conversion and Construction)",
  "radix/docs/design/conversio-valor.md",
  "radix/docs/design/failable-conversio.md",
]
+++

## Data types

Faber มีระบบชนิดข้อมูลแบบสถิตที่ให้ชนิดข้อมูลมาก่อน ทุกการประกาศจะวางชนิดข้อมูลไว้ก่อนชื่อ: `textus nomen` ไม่ใช่ `nomen: textus` ระบบชนิดข้อมูลครอบคลุมชนิดพื้นฐานแบบสเกลาร์ คอลเลกชันแบบเจเนริก ตัวเลขที่กำหนดขนาด เทนเซอร์ และชนิดรีจิสเตอร์สำหรับงาน GPU

### ชนิดข้อมูลพื้นฐาน {#primitive-types}

| ชนิดข้อมูล | บทบาท | ตัวอย่างลิเทอรัล |
|------|------|-----------------|
| `textus` | สตริง Unicode | `"Salve, munde"` |
| `ascii` | โทเค็นเครื่องแบบความยาวคงที่ | `'solum:lege'` |
| `numerus` | จำนวนเต็มมีเครื่องหมาย (ค่าเริ่มต้นคือ i64) | `42` |
| `fractus` | จำนวนทศนิยม (ค่าเริ่มต้นคือ f64) | `3.14` |
| `bivalens` | ค่าบูลีน | `verum`, `falsum` |
| `vacuum` | หน่วย / ไม่มีค่า | — |
| `nihil` | ค่า Null / ไม่มีอยู่ | `nihil` |
| `instans` | ระยะเวลา / จุดเวลาทันที | — |
| `json` | ค่า JSON ระหว่างคอมไพล์ | `{ "key": "value" }` |
| `octeti` | ลำดับไบต์ฐานสิบหก | \|00ff\| |

### ชนิดตัวเลขที่กำหนดขนาด {#sized-numeric-types}

`numerus` และ `fractus` มีความกว้างเริ่มต้น (i64 และ f64) และมีรูปแบบที่ระบุความกว้างได้อย่างชัดเจน:

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

สามารถใช้ชวเลขความกว้างในตำแหน่งชนิดข้อมูลได้: `i8` … `u64`, `f16`, `f32`, `f64` เทียบเท่ากับ `numerus<W>` / `fractus<W>`

### ชนิดข้อมูลที่รับค่า Null ได้ {#nullable-types}

ค่าที่รับ Null ได้ใช้ไวยากรณ์ยูเนียน `T ∪ nihil`:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio maybe() → textus ∪ nihil {
    redde nihil
}
```

Faber ไม่มีไวยากรณ์ `T?` หรือ `Option<T>` ยูเนียนนี้ระบุไว้อย่างชัดเจน

### นามแฝงชนิดข้อมูล {#type-aliases}

```faber
typus UserId = numerus
```

### เจเนริก {#generics}

ฟังก์ชัน นามแฝงชนิดข้อมูล `genus` และ `implendum` รับพารามิเตอร์ชนิดข้อมูลด้วยไวยากรณ์ `<T>`:

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

รองรับการระบุอาร์กิวเมนต์ชนิดข้อมูล ณ จุดเรียกใช้โดยตรง:

```faber
functio identitas<T>(T valor) → T { redde valor }

fixum numerus value ← identitas<numerus>(7)
```

### คอลเลกชัน {#collections}

| ชนิดข้อมูล | บทบาท | ชวเลข |
|------|------|-------|
| `lista<T>` | คอลเลกชันแบบเรียงลำดับที่ปรับขนาดได้ | `lf32`, `lu32` |
| `tabula<K, V>` | แมปคีย์-ค่า | — |
| `tensor<T, Figura>` | บัฟเฟอร์หนาแน่นที่มีรูปร่างคงที่ | `tf32[4]`, `ti64[2,3]` |
| `sparsa<T, Figura>` | บัฟเฟอร์กระจัดกระจายที่มีรูปร่างคงที่ | `sf32[4]`, `si64[2,3]` |
| `intervallum` | ชนิดช่วง | — |
| `copia<T>` | เซตที่ไม่เรียงลำดับ | — |
| `cursor<T>` | สตรีมแบบขี้เกียจ | — |

```faber
fixum lista<numerus> nums ← [1, 2, 3]
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

### ชนิดเทนเซอร์ {#tensor-types}

`tensor<T, Figura>` คือคอนเทนเนอร์หนาแน่นที่มีรูปร่างคงที่:

| รูปแบบ | ความหมาย |
|---------|---------|
| `tensor<T, Figura>` | รูปแบบมาตรฐาน |
| `tensor<T, []>` | แรงก์ 0 (คอนเทนเนอร์สเกลาร์) |
| `tensor<T, _>` | ช่องสำหรับอนุมานรูปร่าง |
| `tensor<T, [N]>` | เวกเตอร์แรงก์ 1 |
| `tensor<T, [N, M]>` | เมทริกซ์แรงก์ 2 |

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

### ชนิดข้อมูลแกนหลักสำหรับ GPU {#gpu-core-types}

ระบบเลนสำหรับงาน GPU และรีจิสเตอร์จะรู้จักชนิดข้อมูลเหล่านี้ แพ็กเกจเป้าหมายที่ไม่รองรับฮาร์ดแวร์จะปฏิเสธชนิดข้อมูลเหล่านี้:

```faber
functio half(f16 x) → f16 { redde x }

functio add(matrix<f32, [2, 2]> a, matrix<f32, [2, 2]> b) → matrix<f32, [2, 2]> {
    redde a.addita(b)
}

functio swap(atomic<i32> cell, i32 value) → i32 {
    redde cell.exchange(value)
}
```

### เครื่องหมายการยืมบนชนิดข้อมูล {#borrow-markers}

เครื่องหมายการยืม (`de`, `in`, `ex`) สามารถปรากฏบนชนิดข้อมูลในตำแหน่งพารามิเตอร์ เพื่อระบุวิธีส่งค่า:

```faber locale=la
# shared borrow — caller retains ownership
functio imprime(de textus label) → vacuum { }

# mutable borrow — caller lends mutable access
functio duplica(in numerus value) → vacuum { }

# move — caller gives up ownership
functio consume(ex textus buffer) → textus {
    redde buffer
}
```

### นโยบายการเปรียบเทียบ {#comparison-policy}

| ตัวดำเนินการ | กลุ่ม | พฤติกรรม |
|----------|--------|-----------|
| `≡`, `≠` | ความเท่ากันแบบตรงกันทุกประการ | ต้องใช้ชนิดข้อมูลเดียวกัน; `nihil` เป็นข้อยกเว้น |
| `≈`, `≉` | ความเท่ากันของค่าเชิงตัวเลข | ใช้ได้เฉพาะลำดับชั้นชนิดตัวเลข |
| `<`, `≤`, `>`, `≥` | การเรียงลำดับ | ใช้กับตัวเลข จุดเวลา และข้อความสเกลาร์ |
| `intra` | การมีค่าอยู่ในช่วง | ตัวเลขอยู่ในช่วง |
| `inter` | การเป็นสมาชิกของคอลเลกชัน | องค์ประกอบอยู่ในคอลเลกชัน |

## Variables and binding

Faber มีคีย์เวิร์ดสำหรับตัวแปรสามแบบและมีสัญลักษณ์การกำหนดค่าโดยเฉพาะ ความแตกต่างสำคัญอยู่ระหว่าง `fixum` (เขียนได้ครั้งเดียว) กับ `varia` (กำหนดค่าใหม่ได้อย่างอิสระ) และระหว่าง `←` (ลำดับการทำงานขณะรันไทม์) กับ `=` (รูปแบบฟิลด์เชิงโครงสร้าง)

### fixum — การผูกค่าที่ไม่เปลี่ยนแปลง {#fixum-immutable-binding}

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

### varia — การผูกค่าที่เปลี่ยนแปลงได้ {#varia-mutable-binding}

การผูกค่าด้วย `varia` สามารถกำหนดค่าใหม่ได้อย่างอิสระ:

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

### sit — รูปแบบย่อของการผูกค่าคงที่แบบอนุมานชนิด {#sit-inferred-immutable-sugar}

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

### การผูกค่าขณะรันไทม์เทียบกับการกำหนดโครงสร้าง {#runtime-binding-vs-structural-definition}

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

### การดึงฟิลด์ด้วย ex {#ex-field-extraction}

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

### การเพิ่มและลดค่าต่อท้าย {#postfix-increment-and-decrement}

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

## Collections

Faber มีชนิดคอลเลกชันหลายชนิดที่คอมไพเลอร์เป็นผู้ดูแล เมธอดมาตรฐานของชนิดเหล่านี้อยู่ในคอมไพเลอร์ ไม่ได้อยู่ในไลบรารีมาตรฐาน

### Lista — คอลเลกชันแบบลำดับที่ปรับขนาดได้แบบไดนามิก {#lista}

```faber
fixum lista<numerus> empty ← vacua
fixum _ numbers ← [1, 2, 3, 4, 5]
fixum _ names ← ["Marcus", "Julia", "Gaius"]
fixum _ nested ← [[1, 2], [3, 4]]
```

การกระจายสมาชิกด้วย `sparge`:

```faber
fixum _ a ← [1, 2, 3]
fixum _ b ← [4, 5, 6]
fixum _ combined ← [sparge a, sparge b]
fixum _ headed ← [0, sparge a, 99]
```

เมธอดสำคัญ: `longitudo`, `accipe`, `appende`, `summa`, `primus`, `novissimus`

### Tabula — แมปแบบคีย์-ค่า {#tabula}

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

### Tensor — บัฟเฟอร์หนาแน่นที่มีรูปร่างตายตัว {#tensor}

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

ไวยากรณ์ย่อของ Tensor (สำหรับโค้ดที่เน้นการคำนวณเชิงตัวเลข):

```faber
fixum tf32[] seed ← vacua
fixum tf32[4] lanes ← seed.strue([1.0, 2.0, 3.0, 4.0], [4])
```

เมธอดสำคัญ: `forma`, `accipe`, `ponde`, `crea`, `structa`, `strue` รวมถึง
การคำนวณแบบสมาชิกต่อสมาชิก การคูณเมทริกซ์ (`multiplicatio`) และ
การลดรูปค่า (`summa`, `productum`)

### Sparsa — บัฟเฟอร์เบาบางที่มีรูปร่างตายตัว {#sparsa}

```faber
fixum sparsa<fractus<f32>, [2, 3]> sparse ← vacua
sparse.ponde([0, 1], 4.0)
sparse.ponde([1, 2], 9.0)

# accipe returns the stored value, here 4.0
nota sparse.accipe([0, 1])
# count of stored entries
nota sparse.nonnihil()
```

การแปลงระหว่างบัฟเฟอร์หนาแน่นและบัฟเฟอร์เบาบาง:

```faber
fixum tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
fixum sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
fixum tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
```

### Cursors — สตรีมแบบประเมินค่าอย่างเลื่อนลอย {#cursors}

`cursor<T>` คือชนิดสตรีมแบบประเมินค่าอย่างเลื่อนลอย สร้างได้จากตัววนซ้ำของคอลเลกชัน
มุมมอง `tuus` หรือฟังก์ชันสร้างค่า ใช้งานผ่าน `itera ex`:

```faber
fixum _ items ← [1, 2, 3]
itera ex items fixum item {
    nota item
}
```

### Intervallum — ช่วงค่า {#intervallum}

```faber
# exclusive range: 0, 1, 2, 3, 4
itera ab 0‥5 fixum i {
    nota i
}
# inclusive range: 0, 1, 2, 3, 4, 5
itera ab 0…5 fixum i {
    nota i
}
```

`‥` คือจุดสิ้นสุดของช่วงแบบไม่รวมค่า ส่วน `…` คือจุดสิ้นสุดของช่วงแบบรวมค่า

## String and template literals

Faber ใช้ความหมายของตัวคั่น โดยรูปแบบเครื่องหมายคำพูดแต่ละแบบหมายถึงรูปร่างของซอร์สโค้ดที่แตกต่างกัน รูปแบบเหล่านี้ไม่ใช่คำพ้องความหมายที่ใช้แทนกันได้

### รูปแบบลิเทอรัล {#literal-forms}

| รูปแบบ | ชนิด | บทบาท |
|------|------|------|
| `'…'` | `ascii` | โทเคนเครื่องจักรแบบคงที่ ไม่รองรับ `§` และไม่รองรับ `(…)` |
| `"…"` | `textus` | สตริง Unicode แบบบรรทัดสั้น โดย `(…)` จะทำการเรนเดอร์ |
| `«…»` | `textus` | Unicode แบบบล็อกหรือหลายบรรทัด โดย `(…)` จะทำการเรนเดอร์ |
| `` `…` `` | `forma` | เทมเพลตที่บันทึกไว้ โดย `(…)` จะจับค่า |
| `{ … }` | `json` | เอกสาร JSON ระหว่างคอมไพล์ |
| `|…|` | `octeti` | ไบต์ฐานสิบหกที่สร้างระหว่างคอมไพล์ |
| `[ … ]` | `lista<T>` | ลิเทอรัลลิสต์ของ Faber |

### การใช้เทมเพลตสตริง {#string-template-application}

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

### สตริงแบบบล็อก {#block-strings}

บล็อกหลายบรรทัดใช้เครื่องหมายกีโยแมต์ `«…»`:

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

### เทมเพลตที่บันทึกไว้ (forma) {#captured-templates}

เทมเพลตที่ใช้เครื่องหมายแบ็กทิกจะจับข้อความและพารามิเตอร์ไว้โดยไม่เรนเดอร์ เหมาะสำหรับเพย์โหลด SQL/URL ที่ผูกค่าอย่างปลอดภัย:

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

### JSON แบบอินไลน์ {#inline-json}

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

## Nullability and optionality

Faber แยกความแตกต่างระหว่างการไม่มีค่าในค่าหนึ่ง กับการระบุให้เป็นทางเลือก ณ จุดประกาศ

### ค่าที่อาจไม่มีค่า — T ∪ nihil {#nullable-values}

ใช้ `T ∪ nihil` เมื่อค่านั้นอาจไม่มีค่า:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

### ช่องประกาศที่เป็นทางเลือก — sponte {#optional-declaration-slots}

ใช้ `sponte` ต่อท้ายชื่อ เมื่อผู้เรียกใช้หรือคอนสตรักเตอร์อาจละเว้นพารามิเตอร์หรือฟิลด์นั้น:

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    textus email sponte
}
```

เครื่องหมายการยืมสามารถใช้ร่วมกับพารามิเตอร์ที่เป็นทางเลือกได้:

```faber
functio process(de numerus depth sponte) → vacuum { }
```

### การยืนยันว่าไม่เป็นค่าว่าง — ! {#non-null-assertion}

ใช้ `!.`, `![`, `!(` เพื่อยืนยันว่าค่าที่อาจไม่มีค่าไม่ใช่ `nihil`:

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

การยืนยันว่าไม่เป็นค่าว่างกับ `nihil` จะยุติการทำงานขณะรันไทม์

### การรวมค่าเมื่อเป็นค่าว่าง — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

### ignotum {#ignotum}

`ignotum` คือชนิดข้อมูลไม่ทราบค่าระดับบนสุดสำหรับทางออกชั่วคราวและกรณีที่ความรู้ยังไม่สมบูรณ์ ไม่ใช่กลไกสำหรับค่าที่อาจเป็นค่าว่าง

## Conversion and construction

ตัวดำเนินการแปลงที่สำคัญมีสองแบบ แบบหนึ่งใช้ขณะรันไทม์ และอีกแบบใช้ขณะคอมไพล์:

```faber
# runtime conversion
fixum _ parsed ← "42" ↦ numerus
# static ascription
fixum numerus value ← 7
fixum _ text ← value ∷ textus
```

### การแปลงขณะรันไทม์ — ↦ {#runtime-conversion}

ใช้ `↦` สำหรับการแปลงขณะรันไทม์ โดยเฉพาะการแปลงจากข้อความหรือการบังคับแปลงชนิดข้อมูลที่อาจล้มเหลว กำหนดการกู้คืนแบบอินไลน์ด้วย `⇥`:

```faber
fixum textus input ← "9"
fixum _ n ← "42" ↦ numerus
fixum _ safe ← input ↦ numerus ⇥ 0
```

การสร้างค่าตามชนิดข้อมูล:

```faber
fixum textus path ← "/etc/hosts"
fixum _ lanes ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
fixum _ body ← ad 'solum:lege' (path) ↦ textus
```

### การระบุชนิดข้อมูลแบบคงที่ — ∷ {#static-ascription}

ใช้ `∷` เพื่อระบุชนิดข้อมูลแบบคงที่อย่างชัดเจน ตัวดำเนินการนี้วางต่อท้าย และขับเคลื่อนด้วยชนิดข้อมูลเป้าหมาย:

```faber
fixum numerus value ← 7
fixum _ x ← 7 ∷ numerus<i32>
fixum _ text ← value ∷ textus
```

### การรวมค่าเมื่อเป็นค่าว่าง — `vel` {#nullish-coalescing}

ใช้ `vel` สำหรับการรวมค่าเมื่อค่าหนึ่งเป็น `nihil`:

```faber
fixum textus ∪ nihil provided_name ← nihil
fixum _ name ← provided_name vel "default"
```
