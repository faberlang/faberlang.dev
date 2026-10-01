# break

Breaks out of the innermost loop.

**Term** `rumpe` · **Section** KEYWORDS · **Also** `break`

## Syntax

```
break
```

## What this teaches

- Loop control flow — `break` exits the innermost `while` or `for` loop immediately
- In nested loops, only the innermost loop is broken; outer loops continue executing

## Common mistakes

- Using `break` outside a breakable block — `while`, `for`, `do`, `send`, or `recv` (SEM030).

## Grammar

```
breakStmt :← 'rumpe'
```

## Expected output

```
0–4 (stops before 5), then nested pairs until interior hits 2.
```

## Example

```fab
main {
    # Break when reaching 5
    var int i ← 0
    while i ≺ 10 {
        if i ≡ 5 {
            break
        }
        print i
        i ← i + 1
    }

    # Break in nested loop
    var int exterior ← 0
    while exterior ≺ 3 {
        var int interior ← 0
        while interior ≺ 10 {
            if interior ≡ 2 {
                break
            }
            print "exterior←§, interior←§"(exterior, interior)
            interior ← interior + 1
        }
        exterior ← exterior + 1
    }
}
```

See also: [`continue`](continue.md), [`while`](while.md).

Fetch list: https://faberlang.dev/agents/index.md
