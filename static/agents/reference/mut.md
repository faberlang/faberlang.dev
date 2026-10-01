# mut

Marks a mutable borrowed parameter.

**Term** `in` · **Section** KEYWORDS

## Syntax

```
in <type> <name>
```

## What this teaches

- Marks a mutable borrowed parameter.
- Related keywords: ref, from

## Common mistakes

- Mode mismatch — passing a `ref` (read-only) value to an `mut` position, or using `mut` to mutate a parameter declared as `ref` (SEM057).

## Grammar

```
paramMode :← 'in' type
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Cross-ref: functio/in-ex.fab.
```

## Example

```fab
fn sum(mut list<int> values) → int {
    return values.sum()
}

main {
    const _ xs ← [1, 2, 3]
    print sum(xs)
}
```

See also: [`ref`](ref.md), [`from`](from.md).

Fetch list: https://faberlang.dev/agents/index.md
