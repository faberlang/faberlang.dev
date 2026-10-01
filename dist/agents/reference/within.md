# within

Checks whether a value lies within a range.

**Term** `intra` · **Section** KEYWORDS

## Syntax

```
<expression> within <range>
```

## What this teaches

- Checks whether a value lies within a range.
- Related keywords: between

## Common mistakes

- Confusing `within` (range containment) with `between` (collection membership) — `within` checks numeric intervals; `between` checks set membership.

## Grammar

```
rangeMembership :← expr 'intra' rangeExpr
```

## Expected output

```
none — stdout not pinned for this exemplum.
```

## Example

```fab
const int aetas = 25

# Basic within with ‥ operator (exclusive end)
if aetas within 0‥100 {
    print "aetas within fines est"
}

# within with … (inclusive end)
if aetas within 18…65 {
    print "aetas laboris"
}

# within with before (explicit exclusive)
if aetas within 0 before 18 {
    print "minor"
}

main {
    print "exempla within"
}
```

See also: [`between`](between.md).

Fetch list: https://faberlang.dev/agents/index.md
