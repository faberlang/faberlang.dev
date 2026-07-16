+++
title = "Variables and binding"
section = "syntax"
order = 2
sources = [
  "radix/README.md (Runtime binding vs structural definition, Language Orientation)",
  "examples/corpus/fixum/",
  "examples/corpus/sit/",
]
+++

Faber has three variable keywords and a dedicated assignment glyph. The key
distinction is between `fixum` (write-once) and `varia` (freely reassignable),
and between `←` (runtime flow) and `=` (structural field shape).

## fixum — immutable binding

`fixum` bindings are write-once. They may be declared with or without an
initializer; if declared without, they must be assigned exactly once before
reading. A second assignment is rejected.

```faber
fixum numerus count ← 0
fixum textus name ← "Marcus"
fixum _ inferred ← [1, 2, 3]
```

Deferred initialisation:

```faber
fixum numerus factor
si compact {
    factor ← 10
} secus {
    factor ← 100
}
```

## varia — mutable binding

`varia` bindings are freely reassignable:

```faber
varia numerus count ← 0
count ← count + 1
count ← count * 2
```

## sit — inferred immutable sugar

`sit` is sugar for `fixum _` — an immutable binding with inferred type:

```faber
sit salve ← "Salve"
sit nomen ← "Marcus"
sit x ← 42

// Deferred form
sit label
label ← "deferred"
```

## Runtime binding vs structural definition

Faber splits what most languages collapse into `=`:

| Glyph | Role | Use for |
|-------|------|---------|
| `←` | Runtime flow | Initial binding, reassignment, mutation |
| `=` | Structural shape | Field names inside literals and metadata |

```faber
// Runtime: ← attaches a value to a name at execution time
fixum numerus count ← 0
varia textus label ← "ready"
count ← count + 1

// Structural: = defines field values inside a type literal
fixum _ p ← Point {
    x = 10,
    y = 20
}
```

## Ex field extraction

`ex` extracts fields from a value into local bindings:

```faber
genus Persona { textus nomen; numerus aetas }

fixum _ p ← Persona { nomen = "Marcus", aetas = 30 }
ex p fixum nomen, aetas
nota nomen  // "Marcus"
```

## Postfix increment and decrement

`⊕` and `⊖` are postfix increment/decrement statements for mutable
`numerus` places. They are statement-only — no expression value, no
prefix forms:

```faber
varia numerus i ← 0
i ⊕  // i becomes 1
i ⊖  // i becomes 0
```
