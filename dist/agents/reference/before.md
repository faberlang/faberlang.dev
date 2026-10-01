# before

Creates an exclusive range with a Latin keyword.

**Term** `ante` · **Section** KEYWORDS

## Syntax

```
<expression> before <expression>
```

## What this teaches

- Exclusive range iteration — `range <initium> before <finis>` iterates from initium up to (but not including) finis
- Range keyword pattern — `before` provides a natural-language alternative to symbolic range syntax

## Common mistakes

- confusing `before` (exclusive upper bound) with `until` (inclusive) — `0 before 4` yields 0,1,2,3 while `0 until 4` yields 0,1,2,3,4

## Grammar

```
iterStmt :← 'itera' 'ab' expr 'ante' expr binding '{' stmt* '}'
```

## Expected output

```
none
```

## Example

```fab
main {
    # i = 0, 1, 2, 3 (stops before 4)
    for range 0 before 4 const i {
        print i
    }
}
```

See also: [`until`](until.md), [`‥`](‥.md).

Fetch list: https://faberlang.dev/agents/index.md
