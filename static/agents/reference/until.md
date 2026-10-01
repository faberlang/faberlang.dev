# until

Creates an inclusive range with a Latin keyword.

**Term** `usque` · **Section** KEYWORDS

## Syntax

```
<expression> until <expression>
```

## What this teaches

- Inclusive range — `range <initium> until <finis>` iterates including both endpoints
- Range iteration — combining `for` with `until` for bounded loops

## Common mistakes

- confusing until (inclusive range bound) with while (loop) or intervallum (range type)

## Grammar

```
iterStmt :← 'itera' 'ab' expr 'usque' expr binding block
```

## Expected output

```
0, 1, 2, 3 (inclusive range through finis).
```

## Example

```fab
main {
    # i = 0, 1, 2, 3 (includes 3)
    for range 0 until 3 const i {
        print i
    }
}
```

See also: [`before`](before.md), [`…`](….md).

Fetch list: https://faberlang.dev/agents/index.md
