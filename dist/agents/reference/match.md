# match

Starts an exhaustive pattern match over a value or values.

**Term** `discerne` · **Section** KEYWORDS · **Also** `match`

## Syntax

```
match <subject> <block>
```

## What this teaches

- Exhaustive pattern matching — `match <value> { case ... }` matches against all variants of a union (tagged union).
- Variant destructuring — `case <Variant> const <field>, ...` destructures variant payload fields.
- Unit variants — variant without payload fields match by name alone.

## Common mistakes

- Non-exhaustive match — omitting a variant from `match` without a `default` catchall; every union variant must be covered (SEM040).

## Grammar

```
discerneStmt :← 'discerne' expr '{' casuClause* '}'
```

## Expected output

```
discerne exempla parata
discretio — tagged union / enum declaration
```

## Example

```fab
union Condicio {
    Agens,
    Iners,
    Pendens
}

union Nuntius {
    Pulsus {
        int x
        int y
    },
    Clavis {
        string clavis
    },
    Finis
}

# Simple case matching on unit variants (no payload)
fn nomina(Condicio s) → string {
    match s {
        case Agens {
            return "agens"
        }
        case Iners {
            return "iners"
        }
        case Pendens {
            return "pendens"
        }
    }
}

# case with const bindings destructures variant fields
fn tracta(Nuntius e) → none {
    match e {
        case Pulsus const x, y {
            print "pulsus: § §"(x, y)
        }
        case Clavis const clavis {
            print "clavis: §"(clavis)
        }
        case Finis {
            print "finis"
        }
    }
}

main {
    # nomina/tracta are defined for downstream exempla; smoke check only
    print "match exempla parata"
}
```

See also: [`union`](union.md), [`case`](case.md).

Fetch list: https://faberlang.dev/agents/index.md
