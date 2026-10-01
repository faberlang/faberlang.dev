# sum

Sequential sum-reduce expression: sum from <tensor> at [i] const s { return <term> }.

**Term** `summa` · **Section** CONCEPTS

## Syntax

```
sum from <source> at [coords] const <binder> { return <term> }
```

## What this teaches

- Sequential fold — `sum from` lowers to a MIR fold over the tensor's at iteration arm: a `+` accumulator seeded at zero, one term per element, `return` inside the body yields the term value.
- Identity term — `return s` is the sequential spelling of `a.summa()`; the printed pair matches under the numeric tolerance contract.
- Transformed term — the body may compute any numeric scalar term from the bound element (here `s + 1.0` per lane).

## Common mistakes

- non-scalar terms — the term must be a numeric scalar (float/numerus)
- the distributed `thread` spelling is admitted only inside `@ kernel` kernels (v1)

## Example

```fab
fn identity(tensor<f32, [8]> a) → f32 {
    return sum from a at [i] const s { return s }
}

fn shifted(tensor<f32, [8]> a) → f32 {
    return sum from a at [i] const s {
        var f32 t ← s
        t ← t + 1.0
        return t
    }
}

main {
    const list<f32> flat ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    const tf32[] seed ← empty
    const tf32[8] a ← seed.strue(flat, [8])

    const f32 per_summam ← a.summa()
    const f32 plicatum ← identity(a)
    const f32 summam_totam ← shifted(a)

    print per_summam
    print plicatum
    print summam_totam
}
```

See also: [`tensor`](tensor.md), [`thread`](thread.md).

Fetch list: https://faberlang.dev/agents/index.md
