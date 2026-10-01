# async_setup

Registers an async before-each test hook.

**Term** `praeparabit` · **Section** KEYWORDS

## Syntax

```
async_setup <block>
```

## What this teaches

- Async test setup — `async_setup` registers an async block that runs before each test case, used when setup involves I/O or future-based operations
- Async counterpart of `setup`; paired with `async_teardown` for async setup/teardown

## Common mistakes

- Confusing `async_setup` (async setup) with `async_teardown` (async teardown) — they run at opposite ends of each test.

## Grammar

```
hookDecl :← 'praeparabit' block
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test hook (whitelist: praeparabit/praeparabit.fab).
```

## Example

```fab
describe "async hooks" {
    async_setup {
        print "before each async"
    }
    test "sample" {
        assert true
    }
}
```

See also: [`setup`](setup.md), [`async_teardown`](async_teardown.md).

Fetch list: https://faberlang.dev/agents/index.md
