# mut (varia)

Declares a mutable binding.

**Term** `varia` · **Section** KEYWORDS · **Also** `let`, `mutable`

## Syntax

```
mut <type|_> <pattern> [← <expression>]
```

## What this teaches

- Mutable bindings — `mut` for values that can be reassigned after declaration
- Immutable bindings — `const` and `let` for values that cannot be reassigned

## Common mistakes

- declaring mut when the binding is never reassigned — use const instead (WARN013)

## Grammar

```
bindingStmt :← ('varia' | 'fixum') type? ident '←' expr
```

## Expected output

```
0, 1, 11, "Salve, Mundus!", 30, "Vale"
```

## Example

```fab
main {
    # --- Mutable bindings with mut ---

    mut _ computus ← 0
    print computus

    computus ← 1
    print computus

    computus ← computus + 10
    print computus

    # --- Immutable bindings: const _ and let ---

    let salutatio ← "Salve, Mundus!"
    print salutatio

    # let compresses repeated const _ when chaining inferred locals
    let x ← 10
    let y ← 20
    let sum ← x + y
    print sum

    # --- Reassign only mut bindings ---

    mut _ nuntius ← "Salve"
    nuntius ← "Vale"
    print nuntius
}
```

See also: [`const`](const.md), [`←`](←.md), [`↑`](↑.md).

Fetch list: https://faberlang.dev/agents/index.md
