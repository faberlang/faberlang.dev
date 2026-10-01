# matrix

matrix<T, [R, C]> is a register-class type distinct from tensor.

**Term** `matrix` · **Section** TYPES

## Syntax

```
matrix<T, [R, C]> | mf32[R, C]
```

## What this teaches

- matrix<T, [R, C]> is a register-class type distinct from tensor.
- Related keywords: tensor, vector, f16

## Common mistakes

- Confusing `matrix` (register-class) with `tensor` (collection) — `matrix<T, [R, C]>` is a GPU register type, not a general-purpose tensor.

## Grammar

```
type :← 'matrix' '<' type ',' '[' natural ',' natural ']' '>'
```

## Expected output

```
none; this is a semantic/MIR systems-lane typecheck example.
```

## Backend

```
Package and probe targets reject until native register matrix backends exist.
```

## Example

```fab
fn keep_matrix(matrix<f32, [2, 2]> m) → matrix<f32, [2, 2]> {
    return m
}

fn add_matrix(mf32[2, 2] left, mf32[2, 2] right) → mf32[2, 2] {
    return left.added(right)
}
```

See also: [`tensor`](tensor.md), [`vector`](vector.md), [`f16`](f16.md).

Fetch list: https://faberlang.dev/agents/index.md
