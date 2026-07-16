+++
title = "Conversion and construction"
section = "syntax"
order = 9
sources = [
  "radix/README.md (Conversion and Construction)",
  "radix/docs/design/conversio-valor.md",
  "radix/docs/design/failable-conversio.md",
]
+++

Two important conversion operators, one for runtime and one for compile-time:

```faber
fixum _ parsed ← "42" ↦ numerus       // runtime conversion
fixum _ text ← value ∷ textus          // static ascription
```

## Runtime conversion — ↦

Use `↦` for runtime conversion, especially parsing or coercion that may
fail. Supply inline recovery with `⇥`:

```faber
fixum _ n ← "42" ↦ numerus
fixum _ safe ← input ↦ numerus ⇥ 0
```

Type-directed materialization:

```faber
fixum _ lanes ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
fixum _ body ← ad 'solum:lege' (path) ↦ textus
```

## Static ascription — ∷

Use `∷` for explicit static type ascription. It is postfix and
target-type driven:

```faber
fixum _ x ← 7 ∷ numerus<i32>
fixum _ text ← value ∷ textus
```

## Nullish coalescing — vel

Use `vel` for nullish coalescing when a value is `nihil`:

```faber
fixum _ name ← provided_name vel "default"
```
