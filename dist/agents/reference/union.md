# union

Declares a tagged union with variant payloads.

**Term** `discretio` · **Section** KEYWORDS · **Also** `union`, `sum type`

## Syntax

```
union <name> [<type-params>] <block>
```

## What this teaches

- Tagged union declaration — `union <name> { <Variant> { fields }, ... }` declares a sum type with named variants.
- Payload variants — variants can carry named fields (like structs) or be unit variants with no payload.
- Multiple field variants — a variant can have many fields of different types.

## Common mistakes

- Confusing `union` with `class` — `union` is a tagged union with variants, not a record with fixed fields; use `match` (not field access) to unpack values.

## Grammar

```
discretioDecl :← 'discretio' ident '{' variantDecl* '}'
variant     :← ident ('{' fieldDecl (',' fieldDecl)* '}')?
```

## Expected output

```
discretiones paratae
Discretio with payload variants
```

## Example

```fab
union Exitus {
    Bonum {
        string nuntius
    },
    Malum {
        string causa
    }
}

# Discretio with mixed unit and payload variants
# (Finis is a unit variant — no payload fields)
union Actum {
    Pulsus {
        int x
        int y
    },
    Clavis {
        string clavis
    },
    Finis
}

# Discretio with many fields per variant
union Figura {
    Rectum {
        int x
        int y
        int latitudo
        int altitudo
    },
    Circulus {
        int cx
        int cy
        int radius
    },
    Punctum {
        int x
        int y
    }
}

main {
    print "discretiones paratae"
}
```

See also: [`enum`](enum.md), [`match`](match.md), [`variant`](variant.md).

Fetch list: https://faberlang.dev/agents/index.md
