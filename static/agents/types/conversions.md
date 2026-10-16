# Conversions

`↦` converts a value to another type. A float becomes an integer only when
the conversion names how it rounds: `via floor`, `via ceil`, `via trunc`, or
`via half_even`. `half_even` sends a tie to the even neighbour, so 2.5 is 2.

```faber locale=en
main {
    let f64 ratio ← 2.5
    let int down ← ratio ↦ int via floor
    let int up ← ratio ↦ int via ceil
    let int even ← ratio ↦ int via half_even
    let f64 back ← down ↦ f64
    print down
    print up
    print even
    print back
}
```

An integer becomes a float with a bare `↦`. A float `↦ int` with no `via` is
`SEM016` `float_to_integer_requires_rounding`:

```faber locale=en outcome=rejects
main {
    let f64 ratio ← 2.5
    let int n ← ratio ↦ int
    print n
}
```

Parent: https://faberlang.dev/agents/types.md
