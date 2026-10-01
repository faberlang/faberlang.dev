# Parameters

Each parameter is a type, then a name. The return type follows `→`.

```faber locale=en
fn divide(int a, int b) → int ∪ none {
    if b ≡ 0 then return null
    return a / b
}

main {
    print divide(7, 2)
}
```

Do not write:

- `a: int`
- `int?`

A missing value is the type `int ∪ none`. The value itself is `null`.

Parent: https://faberlang.dev/agents/functions.md
