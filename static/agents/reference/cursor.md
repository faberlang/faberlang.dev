# cursor

Compatibility annotation for stream/generator posture.

**Term** `cursor` · **Section** KEYWORDS

## Syntax

```
@ cursor
```

## What this teaches

- Preferred stream posture — write `generator` for a synchronous stream or `async_generator` for an asynchronous stream.
- Compatibility annotation — `@ cursor` remains accepted and preserved as the legacy spelling for stream/generator posture.

## Common mistakes

- Using `yield` outside a stream body — `yield` is valid only inside `generator` or `async_generator` bodies, including compatible `@ cursor` declarations.

## Grammar

```
annotation :← '@' 'cursor'
callablePosture :← 'fiunt' | 'fient'
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Cross-ref: futura/futura.fab, itera/cursor-iteratio.fab; Go whitelist: cursor/cursor.fab.
```

## Example

```fab
@ cursor { }
fn stream() → int {
    yield 1
    yield 2
}

main {
    print stream()
}
```

See also: [`generator`](generator.md), [`async_generator`](async_generator.md), [`yield`](yield.md).

Fetch list: https://faberlang.dev/agents/index.md
