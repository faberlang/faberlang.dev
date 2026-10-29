# Tensors

A tensor or matrix folds to a value with `reduce via`. The operators are `sum`,
`product`, `max`, `min`, `argmax`, `argmin`, `all`, `any`, `count` and `first`.
A predicate operator takes a body, and `at [i]` binds the coordinates.

```faber locale=en
fn total(tf32[4] a) → f32 {
    return reduce via product from a
}

fn big(tf32[4] a) → int {
    return reduce via count from a at [i] let s { return s ≻ 2.0 }
}

main {
    let list<f32> flat ← [3.0, 1.0, 3.0, 2.0]
    let tf32[4] a ← flat ↦ tf32[4]
    print total(a)
    print big(a)
}
```

`reduce via first` selects the first element, in row-major order, whose
predicate holds. The result is always `T ∪ none`. The predicate runs on every
element, including those after the first match. A list uses `xs.find(predicate)`
instead, which stops at the first match. The old `primus_quem` and `ubi` form
is retired.

```faber locale=en
fn pick(tf32[3] xs) → f32 ∪ none {
    return reduce via first from xs let x { return x ≻ 2.0 }
}

main {
    let tf32[3] xs ← [1.0, 5.0, 3.0] ↦ tf32[3]
    print pick(xs)
}
```

`per key` groups the terms into buckets and gives a result tensor. The key is an
integer. A bare key is one unary expression (`per rows[i]`; parenthesize
anything wider), and `per [i, j]` gives one key per result axis.

```faber locale=en
fn per_bucket(tf32[6] weights, tensor<int, [6]> rows) → tf32[3] {
    return reduce via sum from weights at [i] per rows[i] let s { return s }
}

main {
    let list<f32> loose ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    let tf32[6] weights ← loose ↦ tf32[6]
    let tensor<int, [6]> rows ← [0, 0, 1, 1, 0, 1] ↦ tensor<int, [6]>
    print per_bucket(weights, rows)
}
```

`scan via` keeps the running value at every position. It needs `thread lane`,
which is legal only in a `@ kernel` function. `total exclusive` stops one
element short, `per key` scans each group on its own, and `order desc` walks
from the end. A kernel that host code calls is also `@ public`.

```faber locale=en
@ kernel
@ public
fn running(tf32[8] xs) → tf32[8] {
    return scan via sum total exclusive from xs at [i] per i % 2 order desc thread lane let v { return v }
}

main {
    let tf32[8] xs ← [1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0] ↦ tf32[8]
    print running(xs)
}
```

An edge policy says what a shifted view holds at the border. In English it is
`.edge<clamp>()`, `.edge<reflect>()` or `.edge<wrap>()`, and `coalesce` fills
with a constant. Latin keeps `limes`; `.limes<clamp>()` in an English file is an
unknown method.

```faber locale=en
main {
    let tf32[3] base ← [1.0, 2.0, 3.0] ↦ tf32[3]
    let tf32[3] clamped ← base.shift([1]).edge<clamp>()
    print clamped.flatten()
}
```

Next: https://faberlang.dev/agents/device.md

Fetch list: https://faberlang.dev/agents/index.md
