# thread

Distributed reduce via sum from … thread kernel inside @ kernel.

**Term** `thread` · **Section** CONCEPTS

## Syntax

```
reduce via sum from <tf32[32]> at [i] thread f let s { return <term> }
```

## What this teaches

- Declared distributed sum — `reduce via sum from … thread …` lowers to the DistributedSum plan entry: cyclic per-lane term-body fold with exactly one lane collective at group exit (Metal simd_sum, CUDA redux.sync, WGSL shared-memory tree) and a broadcast result.
- Term body — per-lane scalar computation with exactly one valued `return`; local mutation of term-local bindings is allowed.
- Bounds-checked lane-strided traversal handles a partial final group; K = 33 below exercises the guarded tail without adding padded lanes.
- Sequential spelling — omit `thread` for the portable host-lane fold (see summa.fab for the identity-term oracle pair).

## Common mistakes

- `thread` outside a `@ kernel` kernel — declines (see summa-decline.fab)
- non-scalar terms — the term must be a numeric scalar (float/numerus family)

## Example

```fab
+++ toml
locale = "la"
+++ faber
@ public
kernel column_dot(tensor<f32, [33]> a, mut tensor<f32, [1]> out) → void {
    let f32 total ← reduce via sum from a at [i] thread f let s {
        mut f32 t ← s * 1.4140625
        return t
    }
    out[0] ← total
}
```

See also: [`sum`](sum.md), [`thread`](thread.md), [`tensor`](tensor.md).

Fetch list: https://faberlang.dev/agents/index.md
