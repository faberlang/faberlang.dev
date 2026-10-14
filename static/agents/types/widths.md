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

`b8`, `b16`, `b32` and `b64` are raw bits, not numbers. A `b8` is exactly
eight bits, so `⇐`, `⇒`, `∧`, `∨`, `⊻` and `¬` act at that width. There is no
arithmetic on bits, and no mixing with a number or another width: `x + x` is
`SEM011` `bits_arithmetic_refused`. A number comes out with `↦` to the
same-width type.

```faber locale=en
main {
    const b8 mask ← 15
    const b8 high ← ¬mask
    const u8 count ← mask ↦ u8
    print high
    print count
}
```

Parent: https://faberlang.dev/agents/types.md
Next: https://faberlang.dev/agents/types/null.md
