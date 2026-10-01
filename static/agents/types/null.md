# Null

A value that may be missing has the type `T ∪ none`. The missing value is
`null`.

```faber locale=en
main {
    const int ∪ none missing ← null
    print missing
}
```

Do not write `int?`.

Parent: https://faberlang.dev/agents/types.md
Next: https://faberlang.dev/agents/types/collections.md
