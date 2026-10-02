# or

Combines boolean expressions with logical or.

**Term** `aut` · **Section** OPERATORS · **Also** `or`

## Syntax

```
<expression> or <expression>
```

## What this teaches

- Complete binary operator tour — arithmetic (`+ − * / %`), comparison (`≡ ≠ < >`), logic (`and or`), nullish coalescing (`coalesce`), ternary (`sic/secus`), and bitwise (`∧ ∨ ⊻ ⇐ ⇒`)
- Assignment patterns — explicit assignment (`←`) and postfix increment (`↑ ↓` statements)
- `let` sugar — compact inference syntax alongside explicit `const _` type inference

## Common mistakes

- confusing `≡` (equality comparison) with `=` (structural field init) or `←` (assignment) — each operator has a distinct role

## Grammar

```
binaryExpr :← expr (arithOp | cmpOp | logicOp | bitwiseOp) expr
Inferred result locals below mix fixum _ (explicit infer marker) with sit
(compact sugar) so both spellings stay visible in one tour.
```

## Expected output

```
binarius.expected
main {
Arithmetica: + - * / %
    const int summa ← 10 + 5
    print summa
    const int differentia ← 10 - 5
    print differentia
    let productum ← 10 * 5
    print productum
    let quotiens ← 10 / 5
    print quotiens
    let reliquum ← 10 % 3
    print reliquum
Assignatio explicita (compound glyphs removed)
    var int index ← 0
    index ← index + 10
    index ↑
    index ↓
    index ← index * 2
    print index
Comparationes
    let aequalis ← 10 ≡ 10
    print aequalis
    let diversus ← 10 ≠ 5
    print diversus
    let minor ← 5 ≺ 10
    print minor
    let maior ← 10 ≻ 5
    print maior
    let medius ← 0 ≺ 5 and 5 ≺ 10
    print medius
Logica
    let ambo ← true and true
    print ambo
    let alterutrum ← false or true
    print alterutrum
    let neutrum ← false and false
    print neutrum
    let short ← false and carum()
    print short
vel
    const string ∪ none nomen ← null
    let solutum ← nomen coalesce "defectum"
    print solutum
    const string ∪ none primum ← null
    const string ∪ none secundum ← null
    const string tertium ← "inventum"
    let inventum ← (primum coalesce secundum) coalesce tertium
    print inventum
✓ ✗ — value conditional, one level only
    let aetas ← 25
    let condicio ← aetas ≥ 18 ✓ "adultus" ✗ "minor"
    print condicio
    let puncta ← 85
    let gradus ← puncta ≥ 80 ✓ "B" ✗ "F"
    print gradus
Bit per bit
    let vexilla ← 0b1010
    let persona ← 0b1100
    let coniuncta ← vexilla ∧ persona
    print coniuncta
    let velata ← vexilla ∨ persona
    print velata
    let diversa ← vexilla ⊻ persona
    print diversa
Motus bit
    let sinistra ← 1 ⇐ 4
    print sinistra
    let dextra ← 16 ⇒ 2
    print dextra
    let persona_vacua ← vexilla ∧ persona ≡ 0
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
