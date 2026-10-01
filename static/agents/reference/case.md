# case

Introduces a branch inside an switch or match statement.

**Term** `casu` · **Section** KEYWORDS · **Also** `case`

## Syntax

```
case <expression> <block>
```

## What this teaches

- Pattern matching arms — `case <expression> <block>` defines a branch in an `switch` match expression
- Default fallback — `default` provides the catch-all branch when no `case` pattern matches

## Common mistakes

- non-exhaustive match without a `default` catchall — every `switch` or `match` must cover all possibilities or add a `default` arm

## Grammar

```
casuClause :← 'casu' expr block
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Cross-ref: elige/elige.fab, discerne/discerne.fab.
```

## Example

```fab
main {
    const _ code ← 200
    switch code {
        case 200 {
            print "ok"
        }
        default {
            print "other"
        }
    }
}
```

See also: [`switch`](switch.md), [`match`](match.md).

Fetch list: https://faberlang.dev/agents/index.md
