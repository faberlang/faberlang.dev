# is

Tests whether a value's runtime type is a given type.

**Term** `est` · **Section** KEYWORDS

## Syntax

```
<expression> est <type>
```

## What this teaches

- Type checking — `<expr> est <type>` tests a value's runtime variant tag without extraction.
- Null checking — `<expr> est null` tests the null type (the null value is `null`).
- Negation — `<expr> is not <type>` negates the type check.
- Chaining — `is` composes with `and` and parenthesized expressions.

## Common mistakes

- Using `is` to compare values — its right-hand side is always a type; use `≡` (or `≠`) for value comparison: `<expr> ≡ true`, `<expr> ≡ false`.

## Grammar

```
typeCheckExpr :← expr 'est' type
```

## Expected output

```
est.expected
```

## Example

```fab
fn explora(any x) → string {
    if x is none then return "nihil est"
    return "aliud est"
}

fn explora_bivalens(bool x) → string {
    if x ≡ true then return "verum est"
    if x ≡ false then return "falsum est"
    return "aliud est"
}

main {
    # Null checking with est
    const int ∪ none forsitan ← null
    const _ nihil_est ← forsitan is none
    print nihil_est

    # Boolean true comparison with ≡
    const _ enabled ← true
    const _ verum_est ← enabled ≡ true
    print verum_est

    # Boolean false comparison with ≡
    const _ disabled ← false
    const _ falsum_est ← disabled ≡ false
    print falsum_est

    # Chained with logical operators
    const string ∪ none nomen ← null
    const _ defectum_debet ← nomen is none and enabled ≡ true
    print defectum_debet

    # Parenthesized for clarity
    const _ utraque_nihil ← forsitan is none and nomen is none
    print utraque_nihil

    # Dynamic ignotum dispatch for nihil and exact boolean checks on bivalens
    print explora(null)
    print explora_bivalens(true)
    print explora(42)

    # --- Variant checks against concrete types ---
    #
    # `est <type>` tests a valor's runtime variant tag directly, without
    # attempting extraction. The inner type parameters of lista/tabula are
    # not checked (width and element types are erased at Valor boxing time
    # by design — see docs/factory/est-variant-check/goal.md).

    const value name ← "faber" ↦ value
    const value quantitas ← 42 ↦ value
    const value notae ← ["a", "b"] ↦ value
    const value active ← true ↦ value
    const value proportio ← 1.5 ↦ value
    assert name is string
    assert quantitas is int
    assert notae is list<value>
    assert active is bool
    assert proportio is float
    assert quantitas not is string
    assert name not is int
}
```

See also: [`is not`](non est.md), [`≡`](≡.md).

Fetch list: https://faberlang.dev/agents/index.md
