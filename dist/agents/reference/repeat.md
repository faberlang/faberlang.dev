# repeat

Repeats a test a fixed number of times.

**Term** `repete` · **Section** KEYWORDS

## Syntax

```
repeat <number>
```

## What this teaches

- Test flakiness mitigation — `repeat <N>` runs a test case up to N times until it passes; useful for non-deterministic or flaky tests
- Declared as a test modifier on `test`

## Common mistakes

- Confusing `repeat` (test repetition modifier) with `for` (loop iterator) or `do`/`while` (loop constructs).

## Grammar

```
testModifier :← 'repete' integer
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test modifier (whitelist: repete/repete.fab).
```

## Example

```fab
test "flaky guard" repeat 2 {
    assert true
}
```

See also: [`flaky`](flaky.md).

Fetch list: https://faberlang.dev/agents/index.md
