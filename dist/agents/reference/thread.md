# thread

Distributed sum-reduce kernel admit: sum from … at [i] thread f const s { return <term> } inside @ kernel.

**Term** `filum` · **Section** CONCEPTS

## Syntax

```
sum from <tf32[32]> at [i] thread f const s { return <term> }
```

## What this teaches

- Declared distributed sum — the `thread` spelling lowers to the DistributedSum plan entry: cyclic per-lane term-body fold with exactly one lane collective at group exit (Metal simd_sum, CUDA redux.sync, WGSL shared-memory tree) and a broadcast result.
- Term body — per-lane scalar computation with exactly one valued `return`; local mutation of term-local bindings is allowed.
- Alignment — the source length must be a multiple of the 32-lane width in v1; K = 32 here. Tails (K % 32 ≠ 0) decline at admission.
- Sequential spelling — omit `thread` for the portable host-lane fold (see summa.fab for the identity-term oracle pair).

## Common mistakes

- `thread` outside a `@ kernel` kernel — declines (see summa-decline.fab)
- non-scalar terms — the term must be a numeric scalar (float/numerus family)

## Example

```fab
@ kernel
@ public { }
fn column_dot(tensor<f32, [32]> a, tensor<f32, [1]> out) → void {
    const f32 total ← sum from a at [i] thread f const s {
        var f32 t ← s * 1.4140625
        return t
    }
    out[0] ← total
}
```

See also: [`sum`](sum.md), [`thread`](thread.md), [`tensor`](tensor.md).

Fetch list: https://faberlang.dev/agents/index.md
