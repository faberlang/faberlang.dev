# Null

A value that may be missing has the type `T ∪ none`. The missing value is
`null`.

```faber locale=en
main {
    const i32 ∪ none missing ← null
    print missing
}
```

Do not write `i32?`.

Parent: https://faberlang.dev/agents/types.md
Next: https://faberlang.dev/agents/types/collections.md
