# switch

Starts a value-based branch statement.

**Term** `elige` · **Section** KEYWORDS · **Also** `switch`, `choose`

## Syntax

```
switch <expression> <block>
```

## What this teaches

- Value-based branching — `switch <expr> { case <value> { ... } }` dispatches on a value (switch/choose pattern).
- Multiple types — `switch` works with string, int, and other comparable types.
- Multi-statement cases — each `case` block can have multiple statements.

## Common mistakes

- Non-exhaustive `switch` without `default` — unmatched values silently produce no output; use `default` for a default branch or cover all possible values.

## Grammar

```
eligeStmt :← 'elige' expr '{' casuClause* '}'
```

## Expected output

```
elige.expected
```

## Example

```fab
main {
    # Text matching
    const string condicio ← "agens"
    switch condicio {
        case "pendens" {
            print "exspectat..."
        }
        case "agens" {
            print "currit"
        }
        case "perfectum" {
            print "perfectum"
        }
    }

    # Numerus matching
    const int codex ← 200
    switch codex {
        case 200 {
            print "Recte"
        }
        case 404 {
            print "not inventum"
        }
        case 500 {
            print "error ministri"
        }
    }

    # Multiple statements per case
    const string modus ← "opera"
    switch modus {
        case "labor" {
            print "modus laboris"
            print "verba multa"
        }
        case "opera" {
            print "modus operis"
            print "opera parata"
        }
    }
}
```

See also: [`case`](case.md), [`default`](default.md).

Fetch list: https://faberlang.dev/agents/index.md
