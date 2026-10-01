# and

Combines boolean expressions with logical and.

**Term** `et` · **Section** OPERATORS · **Also** `and`

## Syntax

```
<expression> et <expression>
```

## What this teaches

- Logical AND — `<bivalens> and <bivalens>` combines two boolean operands with short-circuit evaluation.
- Short-circuit behavior — if the left operand is false, the right operand is not evaluated.

## Common mistakes

- Confusing `and` with `or` — `and` requires both operands to be bool (truthy); `or` requires at least one operand to be truthy.

## Grammar

```
binaryExpr :← expr 'et' expr
```

## Expected output

```
none
main {
left operand: verum
    const bool paratus ← true
right operand: verum
    const bool licet ← true
verum et verum → verum
    const bool currit ← paratus and licet
    print currit
}
```

## Example

```fab
test "and requires both operands" {
    assert (true and true) ≡ true
    assert (false and true) ≡ false
    assert (true and false) ≡ false
    assert (false and false) ≡ false
}

test "and mirrors the main smoke" {
    const bool paratus ← true
    const bool licet ← true
    const bool currit ← paratus and licet
    assert currit ≡ true
}
```

See also: [`or`](or.md), [`not`](not.md).

Fetch list: https://faberlang.dev/agents/index.md
