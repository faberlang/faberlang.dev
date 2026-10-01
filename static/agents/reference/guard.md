# guard

Groups early-exit guard checks before the main body of a function.

**Term** `custodi` · **Section** KEYWORDS · **Also** `guard`

## Syntax

```
guard <block>
```

## What this teaches

- Guard blocks — `guard { if <conditio> { <exitus> } }` groups early-exit checks before a function's main logic.
- Separation of concerns — guard blocks keep preconditions clearly separated from the main body.
- Multiple guards — multiple `if` conditions in one guard block, each with its own exit path.

## Common mistakes

- Using `guard` outside a function — guard blocks are only valid inside fn bodies.

## Grammar

```
custodiStmt :← 'custodi' '{' stmt* '}'
```

## Expected output

```
Division, clamping, and range-validation scalar results.
```

## Example

```fab
fn divide(int a, int b) → int {
    guard {
        if b ≡ 0 {
            return 0
        }
    }
    return a / b
}

fn tracta(int x) → int {
    guard {
        if x ≺ 0 {
            return -1
        }
        if x ≻ 100 {
            return -1
        }
    }

    # Main logic, clearly separated from guard
    return x * 2
}

fn stringe(int value, int minimum, int maximum) → int {
    guard {
        if minimum ≻ value {
            return minimum
        }
        if maximum ≺ value {
            return maximum
        }
    }
    return value
}

main {
    # Guard returns 0 instead of dividing by zero
    print divide(10, 2)
    print divide(10, 0)

    # Out-of-range inputs short-circuit to -1
    print tracta(50)
    print tracta(-10)
    print tracta(150)
    print stringe(5, 0, 10)
    print stringe(-5, 0, 10)
    print stringe(15, 0, 10)
}
```

See also: [`if`](if.md), [`return`](return.md).

Fetch list: https://faberlang.dev/agents/index.md
