# Returns

`return` leaves the function. A function whose return type is `void` uses a
bare `return`.

```faber locale=en
fn porta(int x) → int {
    if x ≺ 0 then return 0
    return x * 2
}

fn tace() → void {
    return
}

main {
    print porta(3)
    tace()
}
```

`≺` is less-than. The value after `→` is the type of every `return`.

Parent: https://faberlang.dev/agents/functions.md
Next: https://faberlang.dev/agents/functions/borrows.md
