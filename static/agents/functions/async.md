# Async

`async` sits before `→`. The function returns a promise. The entry that
awaits is `async_main`, and `await_const` binds the value.

```faber locale=en
fn responde() async → int {
    return 42
}

async_main {
    await_const int responsum ← responde()
    print responsum
}
```

Parent: https://faberlang.dev/agents/functions.md
Next: https://faberlang.dev/agents/functions/entry.md
