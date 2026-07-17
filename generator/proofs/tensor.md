+++
title = "tensor"
section = "corpus"
sources = ["examples/corpus/tensor/decl.fab"]
+++

tensor<T, Figura> declaration shell with rank-0 vacua.

**Syntax:** `tensor<T, Figura> | tensor<T, []>`

## Category

`collection`

## Related

- [tensor](/corpus/tensor.html)
- [lista](/corpus/lista.html)


## Examples

### examples/corpus/tensor/decl.fab (canonical · type)

tensor<T, Figura> declaration shell with rank-0 vacua.
```faber outcome=compiles
# tensor — declaration shell for tensor<T, Figura>
#
# tensor<T, []> name ← vacua
# functio f(tensor<T, []> value) → tensor<T, []>
#
# GRAMMAR:
#   type :← 'tensor' '<' type ',' shape '>'
#
# EXPECTED OUTPUT:
#   Rank-0 tensor longitudo after round-trip identity call.

functio identity(tensor<fractus<f32>, []> value) → tensor<fractus<f32>, []> {
    redde value
}

incipit {
    fixum tensor<fractus<f32>, []> empty ← vacua
    fixum tensor<fractus<f32>, []> roundtrip ← identity(empty)

    nota roundtrip.longitudo()
}
```
**Expected output:**

```
0

```

### examples/corpus/tensor/arithmetic-reject.fab (supporting · reject)

Tensor arithmetic rejects non-numeric elements and mixed numeric widths.
```faber outcome=rejects
# tensor arithmetic reject cases — expected compile failure
#
# WHY: documents the typecheck contract for elementwise tensor arithmetic.
# Both cases must reject:
#   1. tensor<textus, …> — non-numeric element (numeric gate).
#   2. numerus<i32> + numerus<i64> — mixed width is a ↦ conversio problem,
#      never silent promotion at the kernel.
#
# This exemplum intentionally fails to compile; it is registered in the
# per-backend EXPECTED_FAILURES lists.

incipit {
    fixum tensor<textus, [2]> words_a ← vacua
    fixum tensor<textus, [2]> words_b ← vacua
    fixum tensor<textus, [2]> words_sum ← words_a.addita(words_b)
    nota words_sum.longitudo()

    fixum tensor<numerus<i32>, [2]> i32_a ← vacua
    fixum tensor<numerus<i64>, [2]> i64_b ← vacua
    fixum tensor<numerus<i32>, [2]> mixed ← i32_a.addita(i64_b)
    nota mixed.longitudo()
}
```
**Expected:** compilation rejects this example.