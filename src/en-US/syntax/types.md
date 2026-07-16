+++
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
+++

Faber has a static, type-first type system. Every declaration places the type
before the name: `textus nomen`, not `nomen: textus`. The type system covers
scalar primitives, generic collections, sized numerics, tensors, and GPU-facing
register types.

## Primitive types

| Type | Role | Example literal |
|------|------|-----------------|
| `textus` | Unicode string | `"Salve, munde"` |
| `ascii` | Fixed machine token | `'solum:lege'` |
| `numerus` | Signed integer (default i64) | `42` |
| `fractus` | Floating-point (default f64) | `3.14` |
| `bivalens` | Boolean | `verum`, `falsum` |
| `vacuum` | Unit / no value | — |
| `nihil` | Null / absent | `nihil` |
| `instans` | Duration / time instant | — |
| `json` | Compile-time JSON value | `{ "key": "value" }` |
| `octeti` | Hex byte sequence | \|00ff\| |

## Sized numeric types

`numerus` and `fractus` have default widths (i64 and f64) and explicit width
forms:

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

Width sugar is available in type position: `i8` … `u64`, `f16`, `f32`, `f64`
are equivalent to `numerus<W>` / `fractus<W>`.

## Nullable types

Nullable values use the union syntax `T ∪ nihil`:

```faber
functio find(textus key) → numerus ∪ nihil
functio maybe() → textus ∪ nihil
```

There is no `T?` or `Option<T>` syntax in Faber. The union is explicit.

## Type aliases

```faber
typus UserId = numerus
```

## Generics

Functions, type aliases, `genus`, and `implendum` accept type parameters with
`<T>` syntax:

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

Explicit call-site type arguments are supported:

```faber
fixum _ value ← identitas<numerus>(7)
```

## Collections

| Type | Role | Sugar |
|------|------|-------|
| `lista<T>` | Ordered dynamic collection | `lf32`, `lu32` |
| `tabula<K, V>` | Key-value map | — |
| `tensor<T, Figura>` | Dense fixed-shape buffer | `tf32[4]`, `ti64[2,3]` |
| `sparsa<T, Figura>` | Sparse fixed-shape buffer | `sf32[4]`, `si64[2,3]` |
| `intervallum` | Range type | — |
| `copia<T>` | Unordered set | — |
| `cursor<T>` | Lazy stream | — |

```faber
fixum lista<numerus> nums ← [1, 2, 3]
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

## Tensor types

`tensor<T, Figura>` is the dense fixed-shape container:

| Form | Meaning |
|------|---------|
| `tensor<T, Figura>` | Canonical spelling |
| `tensor<T, []>` | Rank-0 (scalar container) |
| `tensor<T, _>` | Shape inference hole |
| `tensor<T, [N]>` | Rank-1 vector |
| `tensor<T, [N, M]>` | Rank-2 matrix |

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

## GPU core types

These are recognised by the systems lane for GPU and register work.
Package targets that lack hardware support reject them:

```faber
functio half(f16 x) → f16 { redde x }

functio add(matrix<f32, [2, 2]> a, matrix<f32, [2, 2]> b) → matrix<f32, [2, 2]> {
    redde a.addita(b)
}

functio swap(atomic<i32> cell, i32 value) → i32 {
    redde cell.exchange(value)
}
```

## Borrow markers on types

Borrow markers (`de`, `in`, `ex`) can appear on types in parameter
positions to indicate how a value is passed:

```faber
functio imprime(de textus label) → vacuum  // shared borrow
functio duplica(in numerus value) → vacuum // mutable borrow
functio consume(ex textus buffer) → textus // move
```

## Comparison policy

| Operator | Family | Behaviour |
|----------|--------|-----------|
| `≡`, `≠` | Exact equality | Identical types required; `nihil` bypass |
| `≈`, `≉` | Numeric value equality | Numeric lattice only |
| `<`, `≤`, `>`, `≥` | Ordering | Numeric, instant, scalar text |
| `intra` | Range containment | Numeric in range |
| `inter` | Collection membership | Element in collection |
