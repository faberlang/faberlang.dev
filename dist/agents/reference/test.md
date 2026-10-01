# test

Defines a single test case.

**Term** `proba` · **Section** KEYWORDS · **Also** `test`, `it`

## Syntax

```
test <name> [modifiers] <block>
```

## What this teaches

- Individual test cases — `test` declares one test with a descriptive name and optional modifiers
- Tests live inside `describe` suites and contain `assert` assertions

## Common mistakes

- Using `assert` outside a `test`/`describe` test block — `assert` is deprecated in production code (WARN006).

## Grammar

```
testDecl :← 'proba' stringLit block
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test case (whitelist: proba/proba.fab). Cross-ref: probandum/probandum.fab.
```

## Example

```fab
test "arithmetic passes" tag "math" {
    assert 1 + 1 ≡ 2
}
```

See also: [`describe`](describe.md), [`assert`](assert.md), [`skip`](skip.md), [`todo`](todo.md).

Fetch list: https://faberlang.dev/agents/index.md
