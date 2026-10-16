# or

Combines boolean expressions with logical or.

**Term** `aut` · **Section** OPERATORS · **Also** `or`

## Syntax

```
<expression> or <expression>
```

## What this teaches

- Complete binary operator tour — arithmetic (`+ − * / %`), comparison (`≡ ≢ < >`), logic (`and or`), nullish coalescing (`coalesce`), ternary (`sic/secus`), and bitwise (`∧ ∨ ⊻ ⇐ ⇒`)
- Assignment patterns — explicit assignment (`←`) and postfix increment (`↑ ↓` statements)
- `let` — inferred write-once locals alongside explicitly typed ones

## Common mistakes

- confusing `≡` (equality comparison) with `=` (structural field init) or `←` (assignment) — each operator has a distinct role

## Grammar

```
binaryExpr :← expr (arithOp | cmpOp | logicOp | bitwiseOp) expr
Inferred result locals below use sit; typed locals state their type.
```

## Expected output

```
binarius.expected
main {
Arithmetica: + - * / %
    let int summa ← 10 + 5
    print summa
    let int differentia ← 10 - 5
    print differentia
    let _ productum ← 10 * 5
    print productum
    let _ quotiens ← 10 / 5
    print quotiens
    let _ reliquum ← 10 % 3
    print reliquum
Assignatio explicita (compound glyphs removed)
    mut int index ← 0
    index ← index + 10
    index ↑
    index ↓
    index ← index * 2
    print index
Comparationes
    let _ aequalis ← 10 ≡ 10
    print aequalis
    let _ diversus ← 10 ≢ 5
    print diversus
    let _ minor ← 5 ≺ 10
    print minor
    let _ maior ← 10 ≻ 5
    print maior
    let _ medius ← 0 ≺ 5 and 5 ≺ 10
    print medius
Logica
    let _ ambo ← true and true
    print ambo
    let _ alterutrum ← false or true
    print alterutrum
    let _ neutrum ← false and false
    print neutrum
    let _ short ← false and carum()
    print short
vel
    let string ∪ none nomen ← null
    let _ solutum ← nomen coalesce "defectum"
    print solutum
    let string ∪ none primum ← null
    let string ∪ none secundum ← null
    let string tertium ← "inventum"
    let _ inventum ← (primum coalesce secundum) coalesce tertium
    print inventum
✓ ✗ — value conditional, one level only
    let _ aetas ← 25
    let _ condicio ← aetas ≥ 18 ✓ "adultus" ✗ "minor"
    print condicio
    let _ puncta ← 85
    let _ gradus ← puncta ≥ 80 ✓ "B" ✗ "F"
    print gradus
Bit per bit
    let _ vexilla ← 0b1010
    let _ persona ← 0b1100
    let _ coniuncta ← vexilla ∧ persona
    print coniuncta
    let _ velata ← vexilla ∨ persona
    print velata
    let _ diversa ← vexilla ⊻ persona
    print diversa
Motus bit
    let _ sinistra ← 1 ⇐ 4
    print sinistra
    let _ dextra ← 16 ⇒ 2
    print dextra
    let _ persona_vacua ← vexilla ∧ persona ≡ 0
    print persona_vacua
}
```

## Example

```fab
fn carum() → bool {
    print "hoc not videatur"
    return true
}
```

See also: [`et`](and.md), [`vel`](coalesce.md), [`⊻`](⊻.md).

Fetch list: https://faberlang.dev/agents/index.md
