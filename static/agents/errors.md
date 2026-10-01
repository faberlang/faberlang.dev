# Errors

`→` is the success channel. `⇥` is the recoverable error channel. A call to
a `⇥` function sits inside `do` / `catch`.

```faber locale=en
fn divide(int a, int b) → int ⇥ string {
    if b ≡ 0 {
        throw "division by zero"
    }
    return a / b
}

main {
    do {
        print divide(7, 2)
    }
    catch err {
        print err
    }
}
```

Detail pages:

- https://faberlang.dev/agents/errors/failable.md — `throw` sends a value on `⇥`.
- https://faberlang.dev/agents/errors/recovery.md — `do` / `catch` recovers around the call.
- https://faberlang.dev/agents/errors/guards.md — `require` throws when the condition fails; `reject` throws when it holds.

Fetch list: https://faberlang.dev/agents/index.md
