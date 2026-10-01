# then

Introduces a compact statement consequent.

**Term** `ergo` · **Section** OPERATORS · **Also** `ergo`, `therefore`

## Syntax

```
<head> then <statement>
```

## What this teaches

- Inline conditionals — `then` replaces a single-statement block body on `if` and `else` branches
- `if <cond> then <stmt> else then <stmt>` forms a two-way one-liner without braces

## Common mistakes

- TODO: chaining multiple statements after `then` (it accepts only one statement)

## Grammar

```
ifStmt :← 'si' expr 'ergo' stmt ('secus' 'ergo' stmt)?
```

## Expected output

```
Validation and grading lines for sample x, aetas, and puncta values.
```

## Example

```fab
main {
    # then replaces a one-statement block body
    const _ x ← 10

    if x ≻ 5 then print "x magnum est"

    # else then pairs else with a single consequent
    const _ aetas ← 25
    if aetas ≥ 18 then print "adultus"
    else then print "minor"

    # Two-way one-liner (85 < 90 → "not A")
    const _ puncta ← 85
    if puncta ≥ 90 then print "A"
    else then print "not A"

    # bool condition used directly
    const _ valet ← true
    if valet then print "Recte"
}
```

See also: [`if`](if.md), [`while`](while.md), [`lambda`](lambda.md), [`return`](return.md), [`pass`](pass.md), [`then`](then.md).

Fetch list: https://faberlang.dev/agents/index.md
