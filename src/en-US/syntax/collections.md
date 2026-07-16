+++
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
+++

Faber has several compiler-owned collection types. Their canonical methods
live in the compiler, not in the standard library.

## Lista — ordered dynamic collection

```faber
fixum lista<numerus> empty ← vacua
fixum _ numbers ← [1, 2, 3, 4, 5]
fixum _ names ← ["Marcus", "Julia", "Gaius"]
fixum _ nested ← [[1, 2], [3, 4]]
```

Spread with `sparge`:

```faber
fixum _ a ← [1, 2, 3]
fixum _ b ← [4, 5, 6]
fixum _ combined ← [sparge a, sparge b]
fixum _ headed ← [0, sparge a, 99]
```

Key methods: `longitudo`, `accipe`, `appende`, `summa`, `primus`, `novissimus`.

## Tabula — key-value map

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

## Tensor — dense fixed-shape buffer

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

Tensor sugar (numeric-heavy code):

```faber
fixum tf32[4] lanes ← [1.0, 2.0, 3.0, 4.0] ↦ tf32[4]
```

Key methods: `forma`, `accipe`, `ponde`, `crea`, `structa`, `strue`, plus
elementwise arithmetic, matrix multiplication (`multiplicatio`), and
reductions (`summa`, `productum`).

## Sparsa — sparse fixed-shape buffer

```faber
fixum sparsa<fractus<f32>, [2, 3]> sparse ← vacua
sparse.ponde([0, 1], 4.0)
sparse.ponde([1, 2], 9.0)

nota sparse.accipe([0, 1])  // 4.0
nota sparse.nonnihil()      // count of stored entries
```

Conversion between dense and sparse:

```faber
fixum tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
fixum sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
fixum tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
```

## Cursors — lazy streams

`cursor<T>` is a lazy stream type. Created from collection iterators,
tuus views, or generator functions. Consumed via `itera ex`:

```faber
itera ex items.cursor() fixum item {
    nota item
}
```

## Intervallum — ranges

```faber
itera ab 0‥5 fixum i { ... }  // 0, 1, 2, 3, 4
itera ab 0…5 fixum i { ... }  // 0, 1, 2, 3, 4, 5
```

`‥` is exclusive range endpoint; `…` is inclusive.
