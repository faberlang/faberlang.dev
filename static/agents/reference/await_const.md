# await_const

Awaits a promise and binds an immutable name.

**Term** `await_const` · **Section** KEYWORDS

## Syntax

```
await_const T name ← future
```

## What this teaches

- Await a `promise<T>` and bind the success value immutably.
- Valid in `async` / `async_generator` / `async_main` contexts.

## Grammar

```
awaitBind :← 'figendum' type? IDENT '←' expr
```

## Example

```fab
+++
locale = "la"
+++
fn responde() async → int {
    return 7
}

async_main {
    await_const int responsum ← responde()
    print responsum
}
```

See also: [`await_var`](await_var.md), [`await`](await.md), [`return_await`](return_await.md), [`async`](async.md), [`promise`](promise.md).

Fetch list: https://faberlang.dev/agents/index.md
