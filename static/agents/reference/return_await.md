# return_await

Awaits a promise and returns its success value from a async body.

**Term** `reddet` · **Section** KEYWORDS · **Also** `return_await`

## Syntax

```
return_await future
```

## What this teaches

- Await and return from a `async` function only (`return_await future`).

## Example

```fab
fn interior() async → int {
    return 9
}

fn exterior() async → int {
    return_await interior()
}

async_main {
    await_const int v ← exterior()
    print v
}
```

See also: [`await_const`](await_const.md), [`await`](await.md), [`async`](async.md), [`return`](return.md).

Fetch list: https://faberlang.dev/agents/index.md
