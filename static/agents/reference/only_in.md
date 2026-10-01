# only_in

Restricts a test to a named environment or target.

**Term** `solum_in` · **Section** KEYWORDS

## Syntax

```
only_in <string> <string>
```

## What this teaches

- Environment scoping — `only_in "ci"` restricts a test to only run in the specified environment (e.g., CI, local)
- Useful for tests that depend on external infrastructure or specific runtime conditions

## Common mistakes

- Confusing `only_in` (environment-scoping keyword) with `only` (stdlib module / test modifier).

## Grammar

```
testModifier :← 'solum_in' stringLit
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test modifier (whitelist: solum-in/solum-in.fab).
```

## Example

```fab
test "ci only" only_in "ci" {
    assert true
}
```

Fetch list: https://faberlang.dev/agents/index.md
