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
- https://faberlang.dev/agents/functions/returns.md — `return` sends a value; a `void` function uses a bare `return`.
- https://faberlang.dev/agents/functions/borrows.md — `ref`, `mut`, and `own` sit before the parameter type.
- https://faberlang.dev/agents/functions/async.md — `async` before `→`, awaited from `async_main`.
- https://faberlang.dev/agents/functions/entry.md — `main args` is the command-line entry.

Fetch list: https://faberlang.dev/agents/index.md
