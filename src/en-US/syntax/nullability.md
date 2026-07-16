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

## Nullable values — T ∪ nihil {#nullable-values}

Use `T ∪ nihil` when the value can be absent:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## Optional declaration slots — sponte {#optional-declaration-slots}

Use `sponte` after the name when a parameter or field may be omitted
by the caller or constructor:

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    textus email sponte
}
```

Borrow markers can combine with optional parameters:

```faber
functio process(de numerus depth sponte) → vacuum { }
```

## Non-null assertion — ! {#non-null-assertion}

Use `!.`, `![`, `!(` to assert a nullable value is not `nihil`:

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

A non-null assertion on `nihil` aborts at runtime.

## Nullish coalescing — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

## ignotum {#ignotum}

`ignotum` is the top-level unknown type for escape hatches and incomplete
knowledge. It is not a nullability mechanism.
