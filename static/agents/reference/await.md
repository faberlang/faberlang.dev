# await

Awaits a promise and discards the success value.

**Term** `tacebit` · **Section** KEYWORDS · **Also** `await`

## Syntax

```
await future
```

## What this teaches

- Await any success type `T` and discard the resolved value.
- Prefer when side effects matter and the success payload is unused.

## Grammar

```
awaitDiscard :← 'tacebit' expr
```

## Example

```fab
fn responde() async → int {
    return 1
}

async_main {
    await responde()
    print "done"
}
```

See also: [`await_const`](await_const.md), [`return_await`](return_await.md), [`async`](async.md), [`promise`](promise.md).

Fetch list: https://faberlang.dev/agents/index.md
