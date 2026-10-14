# Conversions

`↦` converts a value to another type. A float becomes an integer only when
the conversion names how it rounds: `via Floor`, `via Ceil`, `via Trunc`, or
`via HalfEven`. `HalfEven` sends a tie to the even neighbour, so 2.5 is 2.

```faber locale=en
main {
    const f64 ratio ← 2.5
    const int down ← ratio ↦ int via Floor
    const int up ← ratio ↦ int via Ceil
    const int even ← ratio ↦ int via HalfEven
    const f64 back ← down ↦ f64
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
    const f64 ratio ← 2.5
    const int n ← ratio ↦ int
    print n
}
```

Parent: https://faberlang.dev/agents/types.md
