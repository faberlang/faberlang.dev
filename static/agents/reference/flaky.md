# flaky

Marks a test as fragile.

**Term** `fragilis` · **Section** KEYWORDS

## Syntax

```
flaky <number>
```

## What this teaches

- Marks a test as fragile.

## Common mistakes

- Marking a test as fragile without a reason — `flaky <number>` requires a numeric identifier for the failure-tracking system.

## Grammar

```
testModifier :← 'fragilis' integer
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test modifier (whitelist: fragilis/fragilis.fab).
```

## Example

```fab
test "fragile case" flaky 1 {
    assert true
}
```

Fetch list: https://faberlang.dev/agents/index.md
