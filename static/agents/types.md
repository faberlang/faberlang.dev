# Types

The type comes before the name.

```faber locale=en
main {
    const string name ← "Marcus"
    const int age ← 30
    const bool flag ← true
    print name
    print age
    print flag
}
```

Do not write `name: string`.

Detail pages:

- https://faberlang.dev/agents/types/widths.md — a width is a bare marker, `i32` or `f32`.
- https://faberlang.dev/agents/types/null.md — a missing `int` is `int ∪ none`, and the missing value is `null`.
- https://faberlang.dev/agents/types/collections.md — a list is `list<int>`.

Fetch list: https://faberlang.dev/agents/index.md
