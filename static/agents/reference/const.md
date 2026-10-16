# const

Declares an immutable binding.

**Term** `fixum` · **Section** KEYWORDS · **Also** `const`, `immutable`

## Syntax

```
const <type|_> <pattern> [← <expression>]
```

## What this teaches

- Declares an immutable binding.
- Related keywords: mut, let, ←

## Common mistakes

- Reassigning a `let` binding after initialization — `let` is write-once; use `mut` for mutable bindings (SEM020) or defer init with a single later assignment.

## Grammar

```
varDecl := ('sit' | 'varia') typeAnnotation IDENTIFIER ('←' expression)?
```

## Expected output

```
fixum.expected (Salve, Marcus! / 7 / 30 / 300)
```

## Immediate init

let int count ← 0
let name ← "Marcus"
Deferred init (write-once): declare without ←, assign exactly once later, then
freeze. The definite-assignment pass rejects reads before that assignment and
any second assignment.
let int pending
pending ← 42
`let x` infers the type in both immediate and deferred shapes; see
let/sit.fab for the compact inferred spelling. `const` itself now states a
compile-time constant (`const T X = e`).

## Example

```fab
fn scale(bool compact, int base) → int {
    let int factor
    if compact {
        factor ← 10
    }
    else {
        factor ← 100
    }
    return base * factor
}

test "const immediate init" {
    let string name ← "Marcus"
    let string salve ← "Salve, §!"(name)
    assert name ≡ "Marcus"
    assert salve ≡ "Salve, Marcus!"
}

test "const deferred init writes once" {
    let int pending
    pending ← 7
    assert pending ≡ 7
}

test "const factor selected per branch" {
    assert scale(true, 3) ≡ 30
    assert scale(false, 3) ≡ 300
}

main {
    let string name ← "Marcus"
    let string salve ← "Salve, §!"(name)
    print salve
    let int pending
    pending ← 7
    print pending
    print scale(true, 3)
    print scale(false, 3)
}
```

See also: [`mut`](varia.md), [`let`](let.md), [`←`](←.md).

Fetch list: https://faberlang.dev/agents/index.md
