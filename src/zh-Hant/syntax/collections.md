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
Faber 有數種由編譯器擁有的集合型別。它們的標準方法定義於編譯器中，而非標準函式庫。

## Lista — 有序動態集合 {#lista}

```faber
fixum lista<numerus> empty ← vacua
fixum _ numbers ← [1, 2, 3, 4, 5]
fixum _ names ← ["Marcus", "Julia", "Gaius"]
fixum _ nested ← [[1, 2], [3, 4]]
```

使用 `sparge` 展開：

```faber
fixum _ a ← [1, 2, 3]
fixum _ b ← [4, 5, 6]
fixum _ combined ← [sparge a, sparge b]
fixum _ headed ← [0, sparge a, 99]
```

主要方法：`longitudo`、`accipe`、`appende`、`summa`、`primus`、`novissimus`。

## Tabula — 鍵值對映射 {#tabula}

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

## Tensor — 密集固定形狀緩衝區 {#tensor}

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

Tensor 語法糖（數值運算密集的程式碼）：

```faber
fixum tf32[] seed ← vacua
fixum tf32[4] lanes ← seed.strue([1.0, 2.0, 3.0, 4.0], [4])
```

主要方法：`forma`、`accipe`、`ponde`、`crea`、`structa`、`strue`，以及逐元素算術、矩陣乘法（`multiplicatio`）和歸約（`summa`、`productum`）。

## Sparsa — 稀疏固定形狀緩衝區 {#sparsa}

```faber
fixum sparsa<fractus<f32>, [2, 3]> sparse ← vacua
sparse.ponde([0, 1], 4.0)
sparse.ponde([1, 2], 9.0)

# accipe returns the stored value, here 4.0
nota sparse.accipe([0, 1])
# count of stored entries
nota sparse.nonnihil()
```

在密集與稀疏格式之間轉換：

```faber
fixum tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
fixum sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
fixum tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
```

## Cursors — 延遲串流 {#cursors}

`cursor<T>` 是延遲串流型別。它可以由集合迭代器、`tuus` 檢視或產生器函式建立。使用 `itera ex` 消費：

```faber
fixum _ items ← [1, 2, 3]
itera ex items fixum item {
    nota item
}
```

## Intervallum — 範圍 {#intervallum}

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

`‥` 表示不包含終點的範圍；`…` 表示包含終點的範圍。
