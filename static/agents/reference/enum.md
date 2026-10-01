# enum

Declares an enumeration.

**Term** `ordo` · **Section** KEYWORDS · **Also** `enum`

## Syntax

```
enum <name> <block>
```

## What this teaches

- Enumeration declaration — `enum <Name> { member, ... }` declares a set of ordered, named constants.
- Discriminant values — Members can have explicit numeric values with `= <number>`.
- Pattern matching — `switch` with `case` branches selects on enum variants.

## Common mistakes

- Confusing enum (enum with named constants) with union (tagged union with payloads) — enum members carry no data.

## Grammar

```
ordoDecl :← 'ordo' ident '{' ordoMember (',' ordoMember)* '}'
```

## Expected output

```
rubrum
actum
```

## Example

```fab
enum Color {
    rubrum,
    viridis,
    caeruleum
}

enum Condicio {
    pendens = 0,
    actum = 1,
    finitum = 2
}

main {
    # Using enum values: members are qualified by their enum name
    const Color color ← Color.rubrum
    const Condicio condicio ← Condicio.actum

    # Select by enum
    switch color {
        case Color.rubrum {
            print "rubrum"
        }
        case Color.viridis {
            print "viridis"
        }
        case Color.caeruleum {
            print "caeruleum"
        }
    }

    # Select by enum with numeric values
    switch condicio {
        case Condicio.pendens {
            print "pendens"
        }
        case Condicio.actum {
            print "actum"
        }
        case Condicio.finitum {
            print "finitum"
        }
    }
}
```

See also: [`union`](union.md).

Fetch list: https://faberlang.dev/agents/index.md
