+++
translation_kind = "translated"

title = "Data types"
section = "syntax"
order = 1
sources = [
  "radix/README.md (Core Type Surfaces, Numeric Widths, Tensors And Sparsa, GPU Core Types)",
  "radix/docs/design/numeric-type-sugar.md",
  "radix/docs/design/tensor-intrinsics.md",
  "radix/docs/design/lista-intrinsics.md",
  "radix/docs/design/comparison-operators.md",
  "radix/EBNF.md",
  "examples/corpus/typi/",
  "examples/corpus/tensor/",
  "examples/corpus/lista/",
]


prose_hash = "sha256:b3f22d05ed3eb8bbc5d3322fd71f7677a77ba9909b6c80f1cfa00455320e7de5"
code_hash = "sha256:c2351c4cdd58a84dd89c4adc956cce28ce5d7a3db572eae85b44d4a6dbb5d48a"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber มีระบบชนิดข้อมูลแบบสถิตที่ให้ชนิดข้อมูลมาก่อน ทุกการประกาศจะวางชนิดข้อมูลไว้ก่อนชื่อ: `textus nomen` ไม่ใช่ `nomen: textus` ระบบชนิดข้อมูลครอบคลุมชนิดพื้นฐานแบบสเกลาร์ คอลเลกชันแบบเจเนริก ตัวเลขที่กำหนดขนาด เทนเซอร์ และชนิดรีจิสเตอร์สำหรับงาน GPU

## ชนิดข้อมูลพื้นฐาน {#primitive-types}

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

## ชนิดตัวเลขที่กำหนดขนาด {#sized-numeric-types}

`numerus` และ `fractus` มีความกว้างเริ่มต้น (i64 และ f64) และมีรูปแบบที่ระบุความกว้างได้อย่างชัดเจน:

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

สามารถใช้ชวเลขความกว้างในตำแหน่งชนิดข้อมูลได้: `i8` … `u64`, `f16`, `f32`, `f64` เทียบเท่ากับ `numerus<W>` / `fractus<W>`

## ชนิดข้อมูลที่รับค่า Null ได้ {#nullable-types}

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

## นามแฝงชนิดข้อมูล {#type-aliases}

```faber
typus UserId = numerus
```

## เจเนริก {#generics}

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

## คอลเลกชัน {#collections}

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

## ชนิดเทนเซอร์ {#tensor-types}

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

## ชนิดข้อมูลแกนหลักสำหรับ GPU {#gpu-core-types}

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

## เครื่องหมายการยืมบนชนิดข้อมูล {#borrow-markers}

เครื่องหมายการยืม (`de`, `in`, `ex`) สามารถปรากฏบนชนิดข้อมูลในตำแหน่งพารามิเตอร์ เพื่อระบุวิธีส่งค่า:

```faber
# shared borrow — caller retains ownership
functio imprime(de textus label) → vacuum { }

# mutable borrow — caller lends mutable access
functio duplica(in numerus value) → vacuum { }

# move — caller gives up ownership
functio consume(ex textus buffer) → textus {
    redde buffer
}
```

## นโยบายการเปรียบเทียบ {#comparison-policy}

| ตัวดำเนินการ | กลุ่ม | พฤติกรรม |
|----------|--------|-----------|
| `≡`, `≠` | ความเท่ากันแบบตรงกันทุกประการ | ต้องใช้ชนิดข้อมูลเดียวกัน; `nihil` เป็นข้อยกเว้น |
| `≈`, `≉` | ความเท่ากันของค่าเชิงตัวเลข | ใช้ได้เฉพาะลำดับชั้นชนิดตัวเลข |
| `<`, `≤`, `>`, `≥` | การเรียงลำดับ | ใช้กับตัวเลข จุดเวลา และข้อความสเกลาร์ |
| `intra` | การมีค่าอยู่ในช่วง | ตัวเลขอยู่ในช่วง |
| `inter` | การเป็นสมาชิกของคอลเลกชัน | องค์ประกอบอยู่ในคอลเลกชัน |
