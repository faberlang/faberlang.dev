# continue

Continues with the next loop iteration.

**Term** `perge` · **Section** KEYWORDS · **Also** `continue`

## Syntax

```
continue
```

## What this teaches

- Loop control — `continue` skips the rest of the current iteration and proceeds to the next.
- Nested loops — In nested loops, `continue` applies to the innermost loop.

## Common mistakes

- Using `continue` outside a loop — `continue` is only valid inside `while` or `for` (SEM031).

## Grammar

```
continueStmt :← 'perge'
```

## Expected output

```
Odd integers 1–9, then nested pairs skipping interior == 3.
```

## Example

```fab
main {
    # Skip even numbers
    var int i ← 0
    while i ≺ 10 {
        i ← i + 1
        if i % 2 ≡ 0 {
            continue
        }
        print i
    }

    # Continue in nested loop
    var int exterior ← 0
    while exterior ≺ 3 {
        var int interior ← 0
        while interior ≺ 5 {
            interior ← interior + 1
            if interior ≡ 3 {
                continue
            }
            print "exterior←§, interior←§"(exterior, interior)
        }
        exterior ← exterior + 1
    }
}
```

See also: [`break`](break.md), [`while`](while.md).

Fetch list: https://faberlang.dev/agents/index.md
