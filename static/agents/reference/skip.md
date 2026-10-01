# skip

Marks a test case as skipped with a reason.

**Term** `omitte` · **Section** KEYWORDS · **Also** `skip`

## Syntax

```
test <name> skip <reason> <block>
```

## What this teaches

- Test skipping — `skip` marks a test case to be skipped, with a required reason string.
- Test modifiers — Tests can be modified with `skip` to temporarily disable them.

## Common mistakes

- Confusing skip (test skip) with pass (no-op) — skip marks a test as skipped, pass is an empty statement.

## Grammar

```
testModifier :← 'omitte' stringLit
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test modifier (whitelist: omitte/omitte.fab).
```

## Example

```fab
test "database connection" skip "blocked" {
    assert false
}
```

See also: [`test`](test.md), [`todo`](todo.md).

Fetch list: https://faberlang.dev/agents/index.md
