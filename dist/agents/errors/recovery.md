# Recovery

`do` / `catch` is the local boundary around a `⇥` call. `catch` names the
error `err`. `trap { half(7) }` is the expression form: it gives a `trapped<R, T>`,
read with `match` over `case returned let value` and `case thrown let err`.

```faber locale=en
fn divide(int a, int b) → int ⇥ string {
    if b ≡ 0 {
        throw "division by zero"
    }
    return a / b
}

fn tutum(int a, int b) → int {
    do {
        return divide(a, b)
    }
    catch err {
        print err
        return 0
    }
}

main {
    print tutum(7, 2)
}
```

Parent: https://faberlang.dev/agents/errors.md
Next: https://faberlang.dev/agents/errors/guards.md
