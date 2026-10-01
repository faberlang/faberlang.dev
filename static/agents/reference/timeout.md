# timeout

Sets a wall-clock timeout in seconds for a test modifier.

**Term** `temporis` · **Section** KEYWORDS

## Syntax

```
timeout <number>
```

## What this teaches

- Test timeout — `timeout` sets a wall-clock timeout (seconds) on `test` execution; a case still running past the deadline fails
- Test modifiers — combining timing with other test annotations

## Common mistakes

- confusing timeout (test timeout modifier) with tempus (time type)

## Grammar

```
testModifier :← 'temporis' integer
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test modifier (whitelist: temporis/temporis.fab).
```

## Example

```fab
test "timed case" timeout 5 {
    assert true
}
```

See also: [`bench`](bench.md), [`repeat`](repeat.md).

Fetch list: https://faberlang.dev/agents/index.md
