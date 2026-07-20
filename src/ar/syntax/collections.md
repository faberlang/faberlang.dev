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
لدى Faber عدة أنواع مجموعات مملوكة للمترجم. طرائقها القانونية
موجودة في المترجم، وليس في المكتبة القياسية.

## Lista — مجموعة ديناميكية مرتبة {#lista}

```faber
fixum lista<numerus> empty ← vacua
fixum _ numbers ← [1, 2, 3, 4, 5]
fixum _ names ← ["Marcus", "Julia", "Gaius"]
fixum _ nested ← [[1, 2], [3, 4]]
```

النشر باستخدام `sparge`:

```faber
fixum _ a ← [1, 2, 3]
fixum _ b ← [4, 5, 6]
fixum _ combined ← [sparge a, sparge b]
fixum _ headed ← [0, sparge a, 99]
```

الطرائق الرئيسية: `longitudo`، `accipe`، `appende`، `summa`، `primus`، `novissimus`.

## Tabula — خريطة مفتاح-قيمة {#tabula}

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

## Tensor — مصفوفة كثيفة ثابتة الشكل {#tensor}

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

تبسيط Tensor (للأكواد ذات الحسابات العددية الكثيفة):

```faber
fixum tf32[] seed ← vacua
fixum tf32[4] lanes ← seed.strue([1.0, 2.0, 3.0, 4.0], [4])
```

الطرائق الرئيسية: `forma`، `accipe`، `ponde`، `crea`، `structa`، `strue`،
بالإضافة إلى الحساب العنصري، وضرب المصفوفات (`multiplicatio`)،
والاختزالات (`summa`، `productum`).

## Sparsa — مصفوفة متفرقة ثابتة الشكل {#sparsa}

```faber
fixum sparsa<fractus<f32>, [2, 3]> sparse ← vacua
sparse.ponde([0, 1], 4.0)
sparse.ponde([1, 2], 9.0)

# accipe returns the stored value, here 4.0
nota sparse.accipe([0, 1])
# count of stored entries
nota sparse.nonnihil()
```

التحويل بين الكثيف والمتفرق:

```faber
fixum tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
fixum sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
fixum tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
```

## Cursors — تيارات كسولة {#cursors}

`cursor<T>` هو نوع تيار كسول. يُنشأ من مكررات المجموعات،
أو مناظير tuus، أو دوال مولدة. يُستهلك عبر `itera ex`:

```faber
fixum _ items ← [1, 2, 3]
itera ex items fixum item {
    nota item
}
```

## Intervallum — نطاقات {#intervallum}

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

`‥` هو حد نطاق حصري؛ `…` هو حد شامل.
