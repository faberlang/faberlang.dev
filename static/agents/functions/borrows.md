# Borrows

The marker sits before the parameter type. `ref` reads, `mut` writes back to
the caller, and `own` consumes the value.

```faber locale=en
fn imprime(ref string label) → void {
    print label
}

fn duplica(mut int value) → void {
    value ← value * 2
}

fn consume(own string buffer) → string {
    return buffer
}

main {
    imprime("hi")
    var int n ← 3
    duplica(n)
    print n
    print consume("buf")
}
```

`duplica(n)` leaves `n` as 6. Do not write the marker after the type.

Parent: https://faberlang.dev/agents/functions.md
Next: https://faberlang.dev/agents/functions/async.md
