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

- Confusing not (logical negation) with ≢ (inequality comparison) — not negates a boolean, ≢ compares two values.

## Grammar

```
unaryExpr :← 'non' expr
```

## Expected output

```
Scalar stdout smoke (see body).
main {
    let bool flag ← false
    let bool negated ← not flag
    print negated
}
```

## Example

```fab
test "not negates false" {
    let bool flag ← false
    let bool negated ← not flag
    assert negated
}

test "not negates true" {
    let bool flag ← true
    let bool negated ← not flag
    assert negated ≡ false
}

test "not applied twice returns the original" {
    let bool flag ← false
    let bool negated ← not flag
    let bool bis ← not negated
    assert bis ≡ false
}
```

See also: [`true`](true.md), [`false`](false.md).

Fetch list: https://faberlang.dev/agents/index.md
