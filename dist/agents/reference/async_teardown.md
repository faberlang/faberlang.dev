# async_teardown

Registers an async after-each test hook.

**Term** `postparabit` · **Section** KEYWORDS

## Syntax

```
async_teardown <block>
```

## What this teaches

- Async test hooks — `async_teardown` registers an async cleanup hook that runs after each test case.
- Async counterpart — Pairs with `async_setup` (async before-each) and mirrors `teardown` (sync after-each).

## Common mistakes

- Confusing `async_teardown` (async teardown) with `async_setup` (async setup) — they run at opposite ends of each test.

## Grammar

```
hookDecl :← 'postparabit' block
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test hook (whitelist: postparabit/postparabit.fab).
```

## Example

```fab
describe "async hooks" {
    async_teardown {
        print "after each async"
    }
    test "sample" {
        assert true
    }
}
```

See also: [`teardown`](teardown.md), [`async_setup`](async_setup.md).

Fetch list: https://faberlang.dev/agents/index.md
