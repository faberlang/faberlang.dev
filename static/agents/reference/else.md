# else

Runs the fallback branch when preceding conditional branches do not match.

**Term** `secus` · **Section** KEYWORDS · **Also** `else`, `otherwise`

## Syntax

```
else <block>
```

## What this teaches

- Conditional fallback — `else` provides the else/otherwise branch that runs when no preceding `if` or `elif` condition matched
- Always comes last in an if-else chain; takes a block body

## Common mistakes

- Writing `else if` instead of the canonical `elif` for else-if branches — `else` must always be final.

## Grammar

```
elseClause :← 'secus' block
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Cross-ref: si/secus.fab.
```

## Example

```fab
main {
    const int hour ← 23
    if hour ≺ 12 {
        print "morning"
    }
    else {
        print "afternoon-or-later"
    }
}
```

See also: [`if`](if.md), [`elif`](elif.md).

Fetch list: https://faberlang.dev/agents/index.md
