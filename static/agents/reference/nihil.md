# nihil

Represents the null value and can prefix a null check.

**Term** `nihil` · **Section** KEYWORDS

## Syntax

```
none [<expression>]
```

## What this teaches

- the `none` keyword — used for null/none values

## Common mistakes

- Using none without ∪ in the type position — nullable types must be declared as T ∪ none.

## Grammar

```
literal :← 'nihil'
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Example

```fab
main {
    const none nothing ← null
    print nothing
}
```

See also: [`∪`](∪.md), [`optional`](optional.md).

Fetch list: https://faberlang.dev/agents/index.md
