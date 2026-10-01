# Failable

`throw` sends a value on the `⇥` channel. The channel's type is the type of
that value.

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

Parent: https://faberlang.dev/agents/errors.md
Next: https://faberlang.dev/agents/errors/recovery.md
