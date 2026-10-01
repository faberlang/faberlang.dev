# future

Compatibility annotation for asynchronous posture.

**Term** `futura` · **Section** ANNOTATIONS

## Syntax

```
@ future
```

## What this teaches

- Preferred async posture — write `async` for a finite async function.
- Compatibility annotation — `@ future` remains accepted and preserved as the legacy spelling for async posture.
- Related keywords: cursor, await_const, await

## Common mistakes

- Calling an async function and forgetting to consume the promise with `await_const`, `await_var`, `return_await`, or `await`.

## Grammar

```
annotatedFunc :← '@' 'futura' funcDecl
callablePosture :← 'fiet'
```

## Expected output

```
none — Rust async runtime whitelist (compile-only in harness)
```

## Backend

```
Rust async runtime not linked in exempla harness (whitelist: futura/futura.fab).
```

## Example

```fab
@ future { }
fn responde() → int {
    return 42
}

async_main {
    # await_const awaits the promise and binds the resolved value
    await_const int responsum ← responde()
    print responsum
}
```

See also: [`cursor`](cursor.md), [`await_const`](await_const.md), [`await`](await.md).

Fetch list: https://faberlang.dev/agents/index.md
