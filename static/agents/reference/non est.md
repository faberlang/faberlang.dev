# non est

Bitwise or and est-negation operators.

**Term** `non est` · **Section** OPERATORS

## Syntax

```
<expression> ∨ <expression> | <expression> not is <expression>
```

## What this teaches

- Bitwise or — `∨` combines bit flags; distinct from logical short-circuit `or` and `coalesce`.
- Negated est — `not is` (la `not is`) checks that a value's runtime type is not the given type, e.g. `x not is none`.

## Common mistakes

- Confusing ∨ (bitwise or) with or (exclusive or) or vel (inclusive or).

## Grammar

```
binaryExpr :← expr ('∨' | 'non' 'est') expr
```

## Expected output

```
14, verum, falsum
```

## Backend

```
Cross-ref boolean short-circuit: et/et.fab, aut/binarius.fab, vel/binarius.fab.
Negated est parses as `expr not is target`.
```

## Example

```fab
main {
    let _ vexilla ← 0b1010
    let _ persona ← 0b1100
    let _ velata ← vexilla ∨ persona
    # 14 (0b1110)
    print velata
    let string ∪ none praesens ← "salve"
    let string ∪ none absens ← null
    let bool habetValorem ← praesens not is none
    # true
    print habetValorem
    let bool caretValorem ← absens not is none
    # false
    print caretValorem
}
```

See also: [`∧`](∧.md), [`⊻`](⊻.md), [`¬`](¬.md), [`and`](and.md), [`or`](or.md), [`coalesce`](coalesce.md), [`is not`](non est.md), [`is`](is.md).

Fetch list: https://faberlang.dev/agents/index.md
