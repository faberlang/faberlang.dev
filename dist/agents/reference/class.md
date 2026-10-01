# class

Declares a concrete type with fields and methods.

**Term** `genus` · **Section** KEYWORDS · **Also** `class`, `struct`

## Syntax

```
class <name> [<type-params>] <block>
```

## What this teaches

- Declares a concrete type with fields and methods.
- Related keywords: interface, implements

## Common mistakes

- Using retired bare object literals (`{ key = expr }`) — use `GenusName { field = expr }` instead; bare `{ }` is now a JSON value literal.

## Grammar

```
genusDecl :← 'genus' ident '{' fieldDecl* '}'
instance  :← ident '{' fieldInit (',' fieldInit)* '}'
```

## Expected output

```
Field values for Punctum and Persona instances (defaults and overrides).
```

## Example

```fab
class Punctum {
    var int x
    var int y
}

class Persona {
    var string nomen
    # default when omitted at instantiation
    var int aetas = 0
    var bool activus = true
}

main {
    # Instantiate with all required fields
    const Punctum p ← Punctum { x = 10, y = 20 }
    print p.x
    print p.y

    # Instantiate with required + optional defaults
    const Persona marcus ← Persona { nomen = "Marcus" }
    print marcus.nomen
    # 0 from default
    print marcus.aetas
    # verum from default
    print marcus.activus

    # Override defaults explicitly
    const Persona julia ← Persona { nomen = "Julia", aetas = 25, activus = false }
    print julia.nomen
    print julia.aetas
    print julia.activus
}
```

See also: [`interface`](interface.md), [`implements`](implements.md).

Fetch list: https://faberlang.dev/agents/index.md
