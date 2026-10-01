# generator

Callable posture for synchronous stream (generator) functions.

**Term** `fiunt` · **Section** KEYWORDS · **Also** `generator`

## Syntax

```
fn name(…) generator → T
```

## What this teaches

- Preferred stream posture: `generator → T` yields `T` items.
- Yield with statement-initial `yield value` inside the body.

## Common mistakes

- Using `@ cursor` only when teaching preferred morphology — prefer `generator`.

## Grammar

```
callablePosture :← 'fiunt'
yieldStmt :← 'cede' expr
```

## Expected output

```
[1, 2]
```

## Example

```fab
fn stream() generator → int {
    yield 1
    yield 2
}

main {
    print stream()
}
```

See also: [`cursor`](cursor.md), [`yield`](yield.md), [`async_generator`](async_generator.md).

Fetch list: https://faberlang.dev/agents/index.md
