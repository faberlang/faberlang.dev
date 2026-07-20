+++
translation_kind = "translated"

title = "Collections"
section = "syntax"
order = 7
sources = [
  "radix/README.md (Tensors And Sparsa)",
  "radix/docs/design/lista-intrinsics.md",
  "radix/docs/design/tabula-intrinsics.md",
  "radix/docs/design/tensor-intrinsics.md",
  "examples/corpus/lista/",
  "examples/corpus/tabula/",
  "examples/corpus/tensor/",
  "examples/corpus/sparsa/",
]


prose_hash = "sha256:a27f17bb659e59b09584d162f997eb5bba7534e0523767113e9d10559ae8e22d"
code_hash = "sha256:e9cb3fb1f45f7234d5ab43350f4d913db04eb58f4ee1854d59af1238e75ac07a"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber มีชนิดคอลเลกชันหลายชนิดที่คอมไพเลอร์เป็นผู้ดูแล เมธอดมาตรฐานของชนิดเหล่านี้อยู่ในคอมไพเลอร์ ไม่ได้อยู่ในไลบรารีมาตรฐาน

## Lista — คอลเลกชันแบบลำดับที่ปรับขนาดได้แบบไดนามิก {#lista}

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

## Tabula — แมปแบบคีย์-ค่า {#tabula}

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

## Tensor — บัฟเฟอร์หนาแน่นที่มีรูปร่างตายตัว {#tensor}

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

## Sparsa — บัฟเฟอร์เบาบางที่มีรูปร่างตายตัว {#sparsa}

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

## Cursors — สตรีมแบบประเมินค่าอย่างเลื่อนลอย {#cursors}

`cursor<T>` คือชนิดสตรีมแบบประเมินค่าอย่างเลื่อนลอย สร้างได้จากตัววนซ้ำของคอลเลกชัน
มุมมอง `tuus` หรือฟังก์ชันสร้างค่า ใช้งานผ่าน `itera ex`:

```faber
fixum _ items ← [1, 2, 3]
itera ex items fixum item {
    nota item
}
```

## Intervallum — ช่วงค่า {#intervallum}

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
