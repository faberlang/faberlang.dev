# between

Checks whether a value appears in a collection.

**Term** `inter` · **Section** KEYWORDS

## Syntax

```
<expression> between <collection>
```

## What this teaches

- Checks whether a value appears in a collection.
- Related keywords: within

## Common mistakes

- Using `between` with a non-collection right operand — `between` checks membership in a list, map, or set, not a scalar comparison.

## Grammar

```
membershipExpr :← expr 'inter' expr
```

## Expected output

```
none — stdout not pinned for this exemplum.
```

## Example

```fab
main {
    const string condicio ← "agens"
    const int aetas ← 21

    # Basic between with string list
    if condicio between ["pendens", "agens", "pausa"] {
        print "condicio valida"
    }

    # between with numeric list
    if aetas between [18, 21, 65] {
        print "aetas insignis"
    }
    print "exempla between"
}
```

See also: [`within`](within.md).

Fetch list: https://faberlang.dev/agents/index.md
