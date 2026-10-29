# mut

Declares a mutable binding.

**Term** `mut` · **Section** KEYWORDS · **Also** `let`, `mutable`

## Syntax

```
mut <type|_> <pattern> [← <expression>]
```

## What this teaches

- Mutable bindings — `mut` for values that can be reassigned after declaration
- Write-once bindings — `let` for values that cannot be reassigned

## Common mistakes

- declaring mut when the binding is never reassigned — use let instead (WARN013)

## Grammar

```
bindingStmt :← ('varia' | 'sit') type? ident '←' expr
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

    # --- Write-once bindings: let ---

    let _ salutatio ← "Salve, Mundus!"
    print salutatio

    # let infers the type of each local
    let _ x ← 10
    let _ y ← 20
    let _ sum ← x + y
    print sum

    # --- Reassign only mut bindings ---

    mut _ nuntius ← "Salve"
    nuntius ← "Vale"
    print nuntius
}
```

See also: [`const`](const.md), [`←`](←.md), [`↑`](↑.md).

Fetch list: https://faberlang.dev/agents/index.md
