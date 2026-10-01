# not

Negates a boolean expression.

**Term** `non` · **Section** KEYWORDS · **Also** `!`

## Syntax

```
not <expression>
```

## What this teaches

- the `not` keyword — unary boolean negation (equivalent to `!`)

## Common mistakes

- Confusing not (logical negation) with ≠ (inequality comparison) — not negates a boolean, ≠ compares two values.

## Grammar

```
unaryExpr :← 'non' expr
```

## Expected output

```
Scalar stdout smoke (see body).
main {
    const bool flag ← false
    const bool negated ← not flag
    print negated
}
```

## Example

```fab
test "not negates false" {
    const bool flag ← false
    const bool negated ← not flag
    assert negated
}

test "not negates true" {
    const bool flag ← true
    const bool negated ← not flag
    assert negated ≡ false
}

test "not applied twice returns the original" {
    const bool flag ← false
    const bool negated ← not flag
    const bool bis ← not negated
    assert bis ≡ false
}
```

See also: [`true`](true.md), [`false`](false.md).

Fetch list: https://faberlang.dev/agents/index.md
