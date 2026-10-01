# const

Declares an immutable binding.

**Term** `fixum` · **Section** KEYWORDS · **Also** `const`, `immutable`

## Syntax

```
const <type|_> <pattern> [← <expression>]
```

## What this teaches

- Declares an immutable binding.
- Related keywords: var, let, ←

## Common mistakes

- Reassigning a `const` binding after initialization — `const` is immutable; use `var` for mutable bindings (SEM020) or defer init with a single later assignment.

## Grammar

```
varDecl := ('fixum' | 'varia') typeAnnotation IDENTIFIER ('←' expression)?
```

## Expected output

```
fixum.expected (Salve, Marcus! / 7 / 30 / 300)
```

## Immediate init

const int count ← 0
const _ name ← "Marcus"
Deferred init (write-once): declare without ←, assign exactly once later, then
freeze. The definite-assignment pass rejects reads before that assignment and
any second assignment.
const int pending
pending ← 42
`let x` is sugar for `const _ x` in both immediate and deferred shapes; see
let/sit.fab for the compact inferred spelling.

## Example

```fab
fn scale(bool compact, int base) → int {
    const int factor
    if compact {
        factor ← 10
    }
    else {
        factor ← 100
    }
    return base * factor
}

test "const immediate init" {
    const string name ← "Marcus"
    const string salve ← "Salve, §!"(name)
    assert name ≡ "Marcus"
    assert salve ≡ "Salve, Marcus!"
}

test "const deferred init writes once" {
    const int pending
    pending ← 7
    assert pending ≡ 7
}

test "const factor selected per branch" {
    assert scale(true, 3) ≡ 30
    assert scale(false, 3) ≡ 300
}

main {
    const string name ← "Marcus"
    const string salve ← "Salve, §!"(name)
    print salve
    const int pending
    pending ← 7
    print pending
    print scale(true, 3)
    print scale(false, 3)
}
```

See also: [`var`](var.md), [`let`](let.md), [`←`](←.md).

Fetch list: https://faberlang.dev/agents/index.md
