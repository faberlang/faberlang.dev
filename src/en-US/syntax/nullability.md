+++
title = "Nullability and optionality"
section = "syntax"
order = 11
sources = [
  "radix/README.md (Nullability and Optionality)",
  "examples/corpus/nihil/",
  "examples/corpus/sponte/",
  "examples/corpus/nonnihil/",
]
+++

Faber distinguishes absence in a value from optional provision at a
declaration site.

## Nullable values — T ∪ nihil

Use `T ∪ nihil` when the value can be absent:

```faber
functio find(textus key) → numerus ∪ nihil

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## Optional declaration slots — sponte

Use `sponte` after the name when a parameter or field may be omitted
by the caller or constructor:

```faber
functio connect(textus host, numerus port sponte) → vacuum

genus User {
    textus email sponte
}
```

Borrow markers can combine with optional parameters:

```faber
functio process(de numerus depth sponte) → vacuum
```

## Non-null assertion — !

Use `!.`, `![`, `!(` to assert a nullable value is not `nihil`:

```faber
fixum textus name ← maybe_name!
```

A non-null assertion on `nihil` aborts at runtime.

## Nullish coalescing — vel

```faber
fixum _ name ← provided vel "default"
```

## ignotum

`ignotum` is the top-level unknown type for escape hatches and incomplete
knowledge. It is not a nullability mechanism.
