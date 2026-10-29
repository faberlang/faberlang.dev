# coalesce

Provides a default when the left side holds `null`.

**Term** `coalesce` · **Section** OPERATORS · **Also** `nullish coalescing`

## Syntax

```
<expression> coalesce <expression>
```

## What this teaches

- Nullish coalescing — `coalesce` supplies a fallback when the left operand holds `null` (the `none` type's value)
- Chaining — multiple `coalesce` expressions fall through until the first non-`null` value
- Short-circuit — like `and`/`or`, the right operand runs only when the left holds `null`

## Common mistakes

- confusing vel (nullish coalescing, checks for `null` only) with or (logical OR), or using vel for conversion recovery instead of ⇥

## Grammar

```
coalesceExpr :← expr 'vel' expr
```

## Expected output

```
ignotus, Marcus, 0, false, defectum, inventum, 7, supplementum, 9 (vel.expected).
fn fortasse(bool adest) → int ∪ none {
    if adest { return 7 }
    return null
}
fn supplementum(int valor) → int {
    print "supplementum"
    return valor
}
main {
Basic nihil coalescing
    let string ∪ none nomen ← null
    let _ ostensum ← nomen coalesce "ignotus"
"ignotus"
    print ostensum
With present value
    let string ∪ none adest ← "Marcus"
    let _ ostensum2 ← adest coalesce "ignotus"
"Marcus"
    print ostensum2
Difference from logical aut: vel only checks nihil
    let _ nihilum ← 0
    let _ vacuus ← ""
    let _ falsus2 ← false
vel preserves non-nihil values
0
    print nihilum coalesce 999
""
    print vacuus coalesce "defectum"
falsum
    print falsus2 coalesce true
    let _ alter ← nomen coalesce "defectum"
    print alter
Chaining
    let string ∪ none a ← null
    let string ∪ none b ← null
    let string ∪ none c ← "inventum"
    let _ primum ← ((a coalesce b) coalesce c) coalesce "nihil"
"inventum"
    print primum
Short-circuit: the fallback runs only when the left side is nihil
7 (no "supplementum" line)
    print fortasse(true) coalesce supplementum(9)
"supplementum", then 9
    print fortasse(false) coalesce supplementum(9)
}
```

## Example

```fab
test "vel supplies a fallback for none" {
    let string ∪ none name ← null
    let _ ostensum ← name coalesce "ignotus"
    assert ostensum ≡ "ignotus"
}

test "vel preserves non-nihil values" {
    let _ nihilum ← 0
    let _ vacuus ← ""
    let _ falsus2 ← false
    assert nihilum coalesce 999 ≡ 0
    assert vacuus coalesce "defectum" ≡ ""
    assert falsus2 coalesce true ≡ false
}

test "vel chains to the first non-nihil value" {
    let string ∪ none a ← null
    let string ∪ none b ← null
    let string ∪ none c ← "inventum"
    let _ primum ← ((a coalesce b) coalesce c) coalesce "none"
    assert primum ≡ "inventum"
}
```

See also: [`none`](none.md).

Fetch list: https://faberlang.dev/agents/index.md
