# lambda

Declares or explains an inline closure expression; compact ∴ syntax is preferred for new code.

**Term** `clausura` · **Section** KEYWORDS

## Syntax

```
<type> <name> [→ <type>] [⇥ <error-type>] ∴ <expression|fac-block>
```

## What this teaches

- Closure basics — `∴` (therefore) introduces a closure body after the parameter list
- Compact syntax — the `∴` form is preferred over block-delimited closures for simple expressions

## Common mistakes

- confusing `∴` (lambda joint for compact closures) with `then` (single-statement body joint for `if`, `while`, `case`) — they are not interchangeable

## Grammar

```
closureExpr :← paramList '∴' expr
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Cross-ref: clausa/clausa.fab.
```

## Example

```fab
main {
    const (int) → int dupla ← int x ∴ x * 2
    print dupla(5)
    const (int, int) → int sum ← (int a, int b) → int ∴ a + b
    print sum(2, 3)
}
```

See also: [`∴`](∴.md), [`fn`](fn.md), [`do`](do.md), [`catch`](catch.md), [`yield`](yield.md).

Fetch list: https://faberlang.dev/agents/index.md
