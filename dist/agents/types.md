# Types

The type comes before the name.

```faber locale=en
main {
    let string name ← "Marcus"
    let i32 age ← 30
    let bool flag ← true
    print name
    print age
    print flag
}
```

Do not write `name: string`.

Detail pages:

- https://faberlang.dev/agents/types/widths.md — a width is a bare marker, `i32` or `f32`; `b8` to `b64` are raw bits.
- https://faberlang.dev/agents/types/null.md — a missing `i32` is `i32 ∪ none`, and the missing value is `null`.
- https://faberlang.dev/agents/types/collections.md — a list is `list<i32>`.
- https://faberlang.dev/agents/types/conversions.md — `↦` converts; a float to an integer names its rounding with `via`.

Fetch list: https://faberlang.dev/agents/index.md
