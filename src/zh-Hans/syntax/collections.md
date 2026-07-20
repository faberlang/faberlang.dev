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
Faber 拥有多种由编译器内置的集合类型。其规范方法位于编译器中，而非标准库中。

## Lista — 有序动态集合 {#lista}

```faber
fixum lista<numerus> empty ← vacua
fixum _ numbers ← [1, 2, 3, 4, 5]
fixum _ names ← ["Marcus", "Julia", "Gaius"]
fixum _ nested ← [[1, 2], [3, 4]]
```

使用 `sparge` 展开：

```faber
fixum _ a ← [1, 2, 3]
fixum _ b ← [4, 5, 6]
fixum _ combined ← [sparge a, sparge b]
fixum _ headed ← [0, sparge a, 99]
```

关键方法：`longitudo`、`accipe`、`appende`、`summa`、`primus`、`novissimus`。

## Tabula — 键值映射 {#tabula}

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

## Tensor — 密集定形缓冲区 {#tensor}

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

Tensor 语法糖（用于数值密集型代码）：

```faber
fixum tf32[] seed ← vacua
fixum tf32[4] lanes ← seed.strue([1.0, 2.0, 3.0, 4.0], [4])
```

关键方法：`forma`、`accipe`、`ponde`、`crea`、`structa`、`strue`，以及逐元素算术、矩阵乘法（`multiplicatio`）和归约（`summa`、`productum`）。

## Sparsa — 稀疏定形缓冲区 {#sparsa}

```faber
fixum sparsa<fractus<f32>, [2, 3]> sparse ← vacua
sparse.ponde([0, 1], 4.0)
sparse.ponde([1, 2], 9.0)

# accipe returns the stored value, here 4.0
nota sparse.accipe([0, 1])
# count of stored entries
nota sparse.nonnihil()
```

密集与稀疏之间的转换：

```faber
fixum tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
fixum sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
fixum tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
```

## 游标 — 惰性流 {#cursors}

`cursor<T>` 是一种惰性流类型。可由集合迭代器、tuus 视图或生成器函数创建。通过 `itera ex` 消费：

```faber
fixum _ items ← [1, 2, 3]
itera ex items fixum item {
    nota item
}
```

## Intervallum — 范围 {#intervallum}

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

`‥` 是排他范围的端点；`…` 是包含端点。
