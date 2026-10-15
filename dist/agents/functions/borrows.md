# Borrows

The marker sits before the parameter type. `ref` reads, `mut` writes back to
the caller, and `own` consumes the value. A call repeats `mut` and `own`.

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
    mut int n ← 3
    duplica(mut n)
    print n
    print consume(own "buf")
}
```

`duplica(mut n)` leaves `n` as 6. A call that leaves the marker off is
`SEM057` `call_marker_missing`. Do not write the marker after the type.

A parameter with no marker is read-only, all the way down. A `mut` made from
it needs `copy`, and gets an independent value:

```faber locale=en
fn dupla(list<int> xs) → list<int> {
    mut list<int> ys ← copy xs
    ys ← [9]
    return ys
}

main {
    let list<int> a ← [1, 2]
    print dupla(a)
}
```

`mut list<int> ys ← xs` is `SEM065` `const_shared_into_var`.

Parent: https://faberlang.dev/agents/functions.md
Next: https://faberlang.dev/agents/functions/async.md
