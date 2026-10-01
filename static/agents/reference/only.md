# only

Marks a test as the only test to run.

**Term** `solum` · **Section** KEYWORDS

## Syntax

```
only
```

## What this teaches

- Focused test execution — `only` marks a `test` to run in isolation, skipping all other tests in the suite
- Useful during development to run a single test without modifying the test runner configuration

## Common mistakes

- Confusing `only` (stdlib module) with `only_in` (environment-scoping keyword) — they serve different purposes.

## Grammar

```
testModifier :← 'solum'
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test modifier (whitelist: solum/solum.fab).
```

## Example

```fab
test "focus me" only {
    assert true
}
```

See also: [`skip`](skip.md), [`todo`](todo.md).

Fetch list: https://faberlang.dev/agents/index.md
