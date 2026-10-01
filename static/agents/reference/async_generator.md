# async_generator

Callable posture for asynchronous stream functions.

**Term** `fient` · **Section** KEYWORDS · **Also** `async_generator`

## Syntax

```
fn name(…) async_generator → T
```

## What this teaches

- Async stream posture: `async_generator → T` yields promised pulls of `T`.
- Yield with `yield`; consume the stream with `for from` inside an async body.

## Common mistakes

- Expecting every backend to lower `async_generator` — some fail closed until a channel/async-cursor carrier lands.

## Grammar

```
callablePosture :← 'fient'
```

## Backend

```
Product path is Rust async-cursor; other backends may fail closed.
```

## Example

```fab
fn stream() async_generator → int {
    yield 1
    yield 2
}

async_main {
    for from stream() const n {
        print n
    }
}
```

See also: [`generator`](generator.md), [`async`](async.md), [`yield`](yield.md).

Fetch list: https://faberlang.dev/agents/index.md
