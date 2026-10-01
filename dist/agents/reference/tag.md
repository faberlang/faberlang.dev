# tag

Attaches a test tag string.

**Term** `tag` · **Section** KEYWORDS

## Syntax

```
tag <string>
```

## What this teaches

- Test tagging — using `tag` to attach metadata strings to `test` blocks
- Test filtering — tags enable selective test execution by category

## Common mistakes

- attaching duplicate tags or using tag on a non-probandum block

## Grammar

```
testModifier :← 'tag' stringLit
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test modifier (whitelist: tag/tag.fab).
```

## Example

```fab
test "tagged case" tag "focus" {
    assert true
}
```

See also: [`only`](only.md), [`timeout`](timeout.md).

Fetch list: https://faberlang.dev/agents/index.md
