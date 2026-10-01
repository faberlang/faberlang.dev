# todo

Marks a test case as pending future work with a reason.

**Term** `futurum` · **Section** KEYWORDS · **Also** `todo`, `pending`

## Syntax

```
test <name> todo <reason> <block>
```

## What this teaches

- Marks a test case as pending future work with a reason.
- Related keywords: test, skip

## Common mistakes

- Using `todo` on tests that are actually implemented — `todo` marks pending work; active tests should omit this modifier.

## Grammar

```
testModifier :← 'futurum' stringLit
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test modifier (whitelist: futurum/futurum.fab).
```

## Example

```fab
test "async file operations" todo "needs async support" {
    assert true
}
```

See also: [`test`](test.md), [`skip`](skip.md).

Fetch list: https://faberlang.dev/agents/index.md
