# flaky

Rejected by faber test because flaky retries are not executed.

**Term** `flaky` · **Section** KEYWORDS

## Syntax

```
flaky <number>
```

## What this teaches

- `faber test` rejects a case with `flaky <N>` before executing its body. The runner does not execute flaky retries.
- `flaky` is not an allow-failure modifier and does not retry a case.

## Common mistakes

- Expecting `flaky <N>` to allow failure or retry a test — `faber test` rejects it because flaky retries are not implemented.

## Grammar

```
testModifier :← 'fragilis' integer
```

## Backend

```
declaration-only test modifier (whitelist: fragilis/fragilis.fab).
```

## EXPECTED RUNNER OUTCOME

`faber test corpus/flaky/flaky.fab` rejects this case; its body is
not executed. The failure explains that flaky retries are not executed.

## Example

```fab
test "flaky is rejected" flaky 1 {
    assert true
}
```

Fetch list: https://faberlang.dev/agents/index.md
