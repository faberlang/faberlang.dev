# Widths

A width is a bare marker in type position. `i32` is a signed integer. `f32`
is a float. `∷` ascribes that width to a literal.

```faber locale=en
main {
    let i32 narrow ← 7 ∷ i32
    let f32 single ← 1.5 ∷ f32
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
    let b8 mask ← 15
    let b8 high ← ¬mask
    let u8 count ← mask ↦ u8
    print high
    print count
}
```

A number of the same width converts to bits and back: `n ↦ b32` for a `u32`
or `i32`, then `bits ↦ u32`. A different width is `SEM016`
`bits_conversion_width_mismatch`.

Parent: https://faberlang.dev/agents/types.md
Next: https://faberlang.dev/agents/types/null.md
