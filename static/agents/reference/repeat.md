# repeat

Runs a test N times and passes only if every run passes.

**Term** `repeat` · **Section** KEYWORDS

## Syntax

```
repeat <number>
```

## What this teaches

- `repeat <N>` runs the test case N times and passes only if every run passes; it does not retry until one run passes.
- Declared as a test modifier on `test`

## Common mistakes

- Treating `repeat` as retry-until-pass — all N runs must pass.
- Confusing `repeat` (test repetition modifier) with `for` (loop iterator) or `do`/`while` (loop constructs).

## Grammar

```
testModifier :← 'repete' integer
```

## Backend

```
declaration-only test modifier (whitelist: repete/repete.fab).
```

## EXPECTED RUNNER OUTCOME

`faber test corpus/repeat/repeat.fab` runs the passing case twice; it passes
only when both executions pass.

## Example

```fab
test "two passing runs" repeat 2 {
    assert true
}
```

See also: [`flaky`](flaky.md).

Fetch list: https://faberlang.dev/agents/index.md
