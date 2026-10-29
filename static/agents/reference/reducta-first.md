# reducta-first

First-match reduction: reduce via first from <tensor> let x { return <predicate> } yields the first live element (row-major) whose predicate holds, `none` for no match and empty sources.

**Term** `reducta-first` · **Section** CONCEPTS

## Syntax

```
reduce via first from <source> [at [coords]] let <binder> { return <predicate> }
```

## What this teaches

- `first` joins the reduction operators beside sum, product, max, min, argmax, argmin, all, any and count; the body is the predicate, exactly as for count, any and all
- `T ∪ none` — no match and an empty source give `none`, never an error; the result is optional even over a statically non-empty source
- total evaluation — the predicate runs for EVERY element, the ones after the first match included; selection is first-live in row-major order, never an early exit
- a predicate error rides the error channel and is never turned into `none`

## Common mistakes

- `reduce via first` over a `list` — a reduction source is a tensor or matrix
- expecting an index — the result is the element
- expecting early exit — the predicate still runs after the first match

## Example

```fab
+++
locale = "la"
+++
fn switch(tf32[3] xs) → float ∪ none {
    return reduce via first from xs let x { return x ≻ 2.0 }
}

# No-match — no live element yields `none`, never an error.
fn elige_nullum(tf32[2] xs) → float ∪ none {
    return reduce via first from xs let x { return x ≻ 9.0 }
}

# Empty source — a statically zero-extent tensor yields `none`.
fn elige_vacuum(tf32[0] xs) → float ∪ none {
    return reduce via first from xs let x { return x ≻ 0.0 }
}

# Matrix — row-major order; `at [i, j]` binds the coordinates.
fn elige_cellam(tf32[2, 2] m) → float ∪ none {
    return reduce via first from m at [i, j] let x { return x ≻ 1.0 }
}

main {
    let tf32[3] xs ← [1.0, 5.0, 3.0] ↦ tf32[3]
    print switch(xs)
    let tf32[2] ys ← [1.0, 2.0] ↦ tf32[2]
    print elige_nullum(ys)
    let tf32[0] vacua_tensor ← empty
    print elige_vacuum(vacua_tensor)
    let list<f32> flat ← [0.5, 2.0, 3.0, 4.0]
    let tf32[2, 2] m ← flat ↦ tf32[2, 2]
    print elige_cellam(m)
}
```

See also: [`none`](none.md), [`sum`](sum.md).

Fetch list: https://faberlang.dev/agents/index.md
