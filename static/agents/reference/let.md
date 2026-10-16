# let

Declares an inferred immutable local.

**Term** `sit` · **Section** KEYWORDS

## Syntax

```
let <name> [← <expression>]
```

## What this teaches

- Write-once binding — `let name` declares an inferred-type local that is written once
- Supports immediate init (`let x ← expr`) and deferred init (`let x` then `x ← expr` later)

## Common mistakes

- Confusing `let` with `mut` — `let` creates a write-once binding.

## Grammar

```
sitDecl := 'sit' IDENTIFIER ('←' expression)?
```

## Expected output

```
sit.expected
```

## Immediate init

let name ← expr        -- inferred write-once local

## Deferred init

let name               -- deferred: assign once later
name ← expr
`let` infers the type; write `let T name ← expr` to state it. `const` is for
compile-time constants only.

## Example

```fab
main {
    let salve ← "Salve"
    let name ← "Marcus"
    let nuntius ← "§, §!"(salve, name)

    print nuntius

    let label
    label ← "deferred"
    print label

    let idem ← nuntius
    print idem
}
```

See also: [`const`](const.md), [`mut`](varia.md), [`←`](←.md).

Fetch list: https://faberlang.dev/agents/index.md
