# yield

Yields one value from a generator.

**Term** `cede` · **Section** KEYWORDS · **Also** `yield`

## Syntax

```
yield <expression>
```

## What this teaches

- Yield — `yield <expression>` emits one item from a `generator` or `async_generator` callable
- Async values use `await_const`, `await_var`, `return_await`, or `await`; `yield` is not an await form

## Common mistakes

- using `yield` outside a generator body

## Grammar

```
yieldStmt :← 'cede' expr
```

## Expected output

```
[1, 2]
```

## Backend

```
Cursor stream materialization smoke.
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

See also: [`cursor`](cursor.md), [`generator`](generator.md), [`async_generator`](async_generator.md).

Fetch list: https://faberlang.dev/agents/index.md
