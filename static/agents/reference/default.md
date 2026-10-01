# default

Starts the default branch of an switch or match statement.

**Term** `ceterum` · **Section** KEYWORDS · **Also** `default`

## Syntax

```
default <block>
```

## What this teaches

- Default arm — `default <block>` is the catch-all branch in an `switch` or `match` match expression
- Fallback handling — when no `case` pattern matches, execution falls through to the `default` block

## Common mistakes

- using `default` with `match all` — `all` forbids catchall arms and requires listing every variant explicitly (SEM044)

## Grammar

```
defaultClause :← 'ceterum' block
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Cross-ref: elige/ceterum.fab.
```

## Example

```fab
main {
    const _ tag ← "z"
    switch tag {
        case "a" { print "a" }
        default { print "default" }
    }
}
```

See also: [`switch`](switch.md), [`match`](match.md).

Fetch list: https://faberlang.dev/agents/index.md
