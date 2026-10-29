# sum

Sequential sum-reduce expression: reduce via sum from <tensor> at [i] let s.

**Term** `sum` · **Section** CONCEPTS

## Syntax

```
reduce via sum from <source> at [coords] let <binder> { return <term> }
```

## What this teaches

- Sequential fold — `reduce via sum from` lowers to a MIR fold over the tensor's at iteration arm: a `+` accumulator seeded at zero, one term per element, `return` inside the body yields the term value.
- Identity term — `return s` is the sequential spelling of `a.sum()`; the printed pair matches under the numeric tolerance contract.
- Transformed term — the body may compute any numeric scalar term from the bound element (here `s + 1.0` per lane).

## Common mistakes

- non-scalar terms — the term must be a numeric scalar (float/numerus)
- the distributed `thread` spelling is admitted only inside `@ kernel` kernels (v1)

## Example

```fab
+++
locale = "la"
+++
fn identity(tensor<f32, [8]> a) → f32 {
    return reduce via sum from a at [i] let s { return s }
}

fn shifted(tensor<f32, [8]> a) → f32 {
    return reduce via sum from a at [i] let s {
        mut f32 t ← s
        t ← t + 1.0
        return t
    }
}

main {
    let list<f32> flat ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
        let tf32[8] a ← flat ↦ tf32[8]

    let f32 per_summam ← a.summa()
    let f32 plicatum ← identity(a)
    let f32 summam_totam ← shifted(a)

    print per_summam
    print plicatum
    print summam_totam
}
```

See also: [`tensor`](tensor.md), [`thread`](thread.md).

Fetch list: https://faberlang.dev/agents/index.md
