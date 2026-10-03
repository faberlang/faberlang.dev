# Widths

A width is a bare marker in type position. `i32` is a signed integer. `f32`
is a float. `∷` ascribes that width to a literal.

```faber locale=en
main {
    const i32 narrow ← 7 ∷ i32
    const f32 single ← 1.5 ∷ f32
    print narrow
    print single
}
```

Write the marker bare.

Parent: https://faberlang.dev/agents/types.md
Next: https://faberlang.dev/agents/types/null.md
