# Functions

A function names each parameter's type before the name, and names the return
type after `→`.

```faber locale=en
fn divide(int a, int b) → int ∪ none {
    if b ≡ 0 then return null
    return a / b
}

main {
    print divide(7, 2)
}
```

Detail pages:

- https://faberlang.dev/agents/functions/parameters.md — a parameter is `int a`, never `a: int`.

Fetch list: https://faberlang.dev/agents/index.md
