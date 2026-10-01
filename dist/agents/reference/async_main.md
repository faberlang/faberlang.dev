# async_main

Declares the asynchronous program entry point.

**Term** `incipiet` · **Section** KEYWORDS

## Syntax

```
async_main <block>
```

## What this teaches

- Declares the asynchronous program entry point.
- Related keywords: main, await_const, await

## Common mistakes

- Calling a `async` function without consuming its promise; use `await_const`, `await_var`, `return_await`, or `await` inside an `async_main`.

## Grammar

```
asyncEntry :← 'incipiet' block
```

## Expected output

```
none — Rust async runtime whitelist (compile-only in harness)
```

## Backend

```
Pairs with `fiet` and awaited bindings; contrast with incipit
(synchronous entry).
Helper async finite function
```

## Example

```fab
fn accipe() async → string {
    # Simulates async finite operation
    return "datum paratum"
}

fn metire(string datum) async → int {
    return datum.length()
}

# Futura entry point
async_main {
    print "async_main initium"

    # Await async functions with await_const
    await_const string datum ← accipe()
    print "acceptum: §"(datum)
    await_const int longitudo ← metire(datum)
    print "longitudo: §"(longitudo)
    print "opus perfectum"
}
```

See also: [`main`](main.md), [`await_const`](await_const.md), [`await`](await.md).

Fetch list: https://faberlang.dev/agents/index.md
