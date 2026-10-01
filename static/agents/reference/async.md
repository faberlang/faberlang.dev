# async

Callable posture for asynchronous finite functions.

**Term** `fiet` · **Section** KEYWORDS · **Also** `async`

## Syntax

```
fn name(…) async → T
```

## What this teaches

- Preferred async posture word after the parameter list: `async → T`.
- Return type is observed as `promise<T>` at call sites.
- Consume with `await_const`, `await_var`, `return_await`, or `await`.

## Common mistakes

- Using bare `yield` to await — await is not yield; use await morphology.

## Grammar

```
callablePosture :← 'fiet'
```

## Expected output

```
42
```

## Example

```fab
fn responde() async → int {
    return 42
}

async_main {
    await_const _ responsum ← responde()
    print responsum
}
```

See also: [`future`](future.md), [`promise`](promise.md), [`await_const`](await_const.md), [`await`](await.md).

Fetch list: https://faberlang.dev/agents/index.md
