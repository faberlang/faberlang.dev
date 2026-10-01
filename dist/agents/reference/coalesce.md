# coalesce

Provides a default when the left side is null.

**Term** `vel` · **Section** OPERATORS · **Also** `nullish coalescing`

## Syntax

```
<expression> vel <expression>
```

## What this teaches

- Nullish coalescing — `coalesce` supplies a fallback when the left operand is `none`
- Chaining — multiple `coalesce` expressions fall through until the first non-`none` value
- Short-circuit — like `and`/`or`, the right operand runs only when the left is `none`

## Common mistakes

- confusing vel (nullish coalescing, checks none only) with or (logical OR), or using vel for conversion recovery instead of ⇥

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
    const string ∪ none nomen ← null
    let ostensum ← nomen coalesce "ignotus"
"ignotus"
    print ostensum
With present value
    const string ∪ none adest ← "Marcus"
    let ostensum2 ← adest coalesce "ignotus"
"Marcus"
    print ostensum2
Difference from logical aut: vel only checks nihil
    let nihilum ← 0
    let vacuus ← ""
    let falsus2 ← false
vel preserves non-nihil values
0
    print nihilum coalesce 999
""
    print vacuus coalesce "defectum"
falsum
    print falsus2 coalesce true
    let alter ← nomen coalesce "defectum"
    print alter
Chaining
    const string ∪ none a ← null
    const string ∪ none b ← null
    const string ∪ none c ← "inventum"
    let primum ← ((a coalesce b) coalesce c) coalesce "nihil"
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
    const string ∪ none name ← null
    let ostensum ← name coalesce "ignotus"
    assert ostensum ≡ "ignotus"
}

test "vel preserves non-nihil values" {
    let nihilum ← 0
    let vacuus ← ""
    let falsus2 ← false
    assert nihilum coalesce 999 ≡ 0
    assert vacuus coalesce "defectum" ≡ ""
    assert falsus2 coalesce true ≡ false
}

test "vel chains to the first non-nihil value" {
    const string ∪ none a ← null
    const string ∪ none b ← null
    const string ∪ none c ← "inventum"
    let primum ← ((a coalesce b) coalesce c) coalesce "none"
    assert primum ≡ "inventum"
}
```

See also: [`none`](nihil.md).

Fetch list: https://faberlang.dev/agents/index.md
