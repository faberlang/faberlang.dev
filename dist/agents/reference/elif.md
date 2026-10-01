# elif

Adds an else-if branch after a previous if branch.

**Term** `sin` · **Section** KEYWORDS · **Also** `else if`

## Syntax

```
elif <condition> <block>
```

## What this teaches

- Standalone else-if — `elif` provides an intermediate conditional branch evaluated only when the preceding `if` condition was `false`
- Chains: `if { } elif { } else { }` for multi-way branching

## Common mistakes

- Writing `else if` instead of the canonical `elif` for else-if branches.

## Grammar

```
elseIfClause :← 'sin' expr block
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Cross-ref: si/sin.fab.
```

## Example

```fab
main {
    const int score ← 85
    if score ≥ 90 {
        print "excellent"
    }
    elif score ≥ 80 {
        print "good"
    }
    else {
        print "needs work"
    }
}
```

See also: [`if`](if.md), [`else`](else.md).

Fetch list: https://faberlang.dev/agents/index.md
