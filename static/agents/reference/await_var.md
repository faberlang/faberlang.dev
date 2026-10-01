# await_var

Awaits a promise and binds a mutable name.

**Term** `variandum` · **Section** KEYWORDS · **Also** `await_var`

## Syntax

```
await_var T name ← future
```

## What this teaches

- Await a `promise<T>` and bind the success value mutably.

## Example

```fab
fn responde() async → int {
    return 3
}

async_main {
    await_var int responsum ← responde()
    responsum ← responsum + 1
    print responsum
}
```

See also: [`await_const`](await_const.md), [`await`](await.md), [`async`](async.md), [`promise`](promise.md).

Fetch list: https://faberlang.dev/agents/index.md
