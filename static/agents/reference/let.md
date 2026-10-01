# let

Declares an inferred immutable local.

**Term** `sit` · **Section** KEYWORDS

## Syntax

```
let <name> [← <expression>]
```

## What this teaches

- Immutable binding sugar — `let name` is a compact alternative to `const _ name` for inferred-type immutable locals
- Supports immediate init (`let x ← expr`) and deferred init (`let x` then `x ← expr` later)

## Common mistakes

- Confusing `let` (sugar for `const _`) with `var` — `let` creates an immutable binding.

## Grammar

```
sitDecl := 'sit' IDENTIFIER ('←' expression)?
```

## Expected output

```
sit.expected
```

## Immediate init

let name ← expr        -- compact sugar for const _ name ← expr

## Deferred init

let name               -- compact sugar for const _ name (assign once later)
name ← expr
Prefer let when a block chains several inferred locals; keep const _ when
teaching the explicit infer marker or mixing typed and inferred bindings.

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

    const _ idem ← nuntius
    print idem
}
```

See also: [`const`](const.md), [`var`](var.md), [`←`](←.md).

Fetch list: https://faberlang.dev/agents/index.md
