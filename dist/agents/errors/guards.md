# Guards

`require` throws when the condition fails. `reject` throws when the
condition holds. Both need a `⇥` channel on the function.

```faber locale=en
fn divide(int a, int b) → int ⇥ string {
    require b ≠ 0 throw "division by zero"
    return a / b
}

fn exige(int value) → int ⇥ string {
    reject value ≺ 0 throw "negative value"
    return value
}

main {
    do {
        print divide(7, 2)
        print exige(3)
    }
    catch err {
        print err
    }
}
```

Parent: https://faberlang.dev/agents/errors.md
