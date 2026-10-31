+++
title = "Tensor computation"
section = "language"
order = 8
sources = []
+++

*Reductions, ordered scans, edge policies, kernels, and the blocks that group device work.*

A tensor or matrix folds to a value with `reduce via`, and to a tensor of
running values with `scan via`. Both walk the elements in row-major order and
bind each element to a name. A `kernel` is a function that runs on a device. The
device blocks at the end of this page, `do all` and `do device`, group kernel
launches so that a fault is reported once.

The examples run with `faber run`. The kernel examples need a device route:
add `--device cpu` (or `--device reference` for plain sequential code) when you
run a package that calls a kernel.

## Reductions {#reduce}

`reduce via <op> from <tensor>` folds every element into one value. The
operators are `sum`, `product`, `max`, `min`, `argmax`, `argmin`, `all`,
`any`, `count` and `first`. The operators `sum`, `product`, `max` and `min` need
no body. `count`, `all`, `any` and `first` take a body, `let s { return … }`,
that returns the predicate for each element. `at [i]` binds the
coordinates of the element under test.

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

This prints `18.0` and `2`. A reduction source is a tensor or a matrix. A list
keeps its methods, `all`, `any` and `find`, instead.

## First match {#first}

`reduce via first` selects the first element, in row-major order, for which
the predicate holds. The result is always `T ∪ none`, even over a source that
cannot be empty: no match, or an empty source, gives `none`.

```faber locale=en
fn pick(tf32[3] xs) → f32 ∪ none {
    return reduce via first from xs let x { return x ≻ 2.0 }
}

fn pick_cell(tf32[2, 2] m) → f32 ∪ none {
    return reduce via first from m at [i, j] let x { return x ≻ 1.0 }
}

main {
    let tf32[3] xs ← [1.0, 5.0, 3.0] ↦ tf32[3]
    print pick(xs)
    let tf32[3] low ← [1.0, 0.5, 2.0] ↦ tf32[3]
    print pick(low)
    let list<f32> flat ← [0.5, 2.0, 3.0, 4.0]
    let tf32[2, 2] m ← flat ↦ tf32[2, 2]
    print pick_cell(m)
}
```

This prints `5.0`, `none` and `2.0`. Two properties surprise people who
expect an early exit:

- The predicate runs on **every** element, including the ones after the first
  match. Selection is "first live in row-major order", not a search that stops.
  A predicate that fails after the match still fails; the error is never turned
  into `none`.
- The result is the element, not its index. Read the coordinates with `at`
  inside the predicate if you need them.

`first` takes no `per` grouping and no `coalesce` identity of its own. Put
`coalesce` on the whole expression to default the optional result. On a list,
`xs.find(predicate)` is the first-match method: it walks left to right and
stops at the first match.

Since 1.17, `reduce via first` is the only first-match form. The dedicated
`primus_quem` expression with its `ubi` predicate is retired.

## Grouped reductions {#per}

`per key` groups the terms into buckets and gives a result tensor instead of a
scalar. The key is evaluated for every element, with its coordinates in scope,
and must be an integer: it names the bucket the term lands in. The bucket
extents come from the result type, which you write on the function or binding.

```faber locale=en
fn per_bucket(tf32[6] weights, tensor<int, [6]> rows) → tf32[3] {
    return reduce via sum from weights at [i] per rows[i] let s { return s }
}

fn per_cell(tf32[2, 2, 3] cube) → tf32[2, 2] {
    return reduce via sum from cube at [i, j, k] per [i, j] let s { return s }
}

main {
    let list<f32> loose ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    let tf32[6] weights ← loose ↦ tf32[6]
    let tensor<int, [6]> rows ← [0, 0, 1, 1, 0, 1] ↦ tensor<int, [6]>
    print per_bucket(weights, rows)
    let list<f32> deep ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    let tf32[2, 2, 3] cube ← deep ↦ tf32[2, 2, 3]
    print per_cell(cube)
}
```

This prints `[8.0, 13.0, 0.0]` and `[6.0, 15.0, 24.0, 33.0]`. A bucket that no
term reaches keeps the operator's identity: `0.0` for `sum`, `0` for `count`.

The key has two forms:

- A **bare key**, `per rows[i]`, is one key and a rank-one result. A bare key is
  a single unary expression. `per rows[i] + 1` is a parse error;
  write `per (rows[i] + 1)`. A bare key stops before `coalesce`, so a
  following `coalesce` identity belongs to the reduction.
- A **bracketed list**, `per [i, j]`, has one key per axis of the result, so
  the key count must equal the result rank. The list is written out as
  `[k0, k1, …]`; a key list held in a variable, an empty list or a spread is
  refused. Inside the list a key is one scalar expression: read one key tensor
  per axis, as in `per [rows[i], cols[i]]`.

Grouped `max` and `min` need a `coalesce` identity for empty buckets. Grouped
`argmax` and `argmin` are refused by name. Among the generated targets, the
Rust, TypeScript and Go emitters and the runner support a multi-key group.

## Ordered scans {#scan}

`scan via <op>` keeps the running value at every position instead of one
final value. The result has the shape of the source: the element at `i` is the
reduction of the elements up to `i`. The operators are `sum`, `product`,
`max`, `min`, `all`, `any` and `count`.

A scan always names a lane binder, `thread lane`, and takes its element from
the `let` binding. `thread` is admitted only inside a [kernel](#kernel); a scan
anywhere else is `SEM010 scan_thread_requires_nucleum_kernel`. A kernel that
host code calls is also marked `@ public`.

```faber locale=en
@ public
kernel running(tf32[8] xs) → tf32[8] {
    return scan via sum from xs at [i] thread lane let v { return v }
}

@ public
kernel before(tf32[8] xs) → tf32[8] {
    return scan via sum total exclusive from xs at [i] thread lane let v { return v }
}

@ public
kernel by_parity(tf32[8] xs) → tf32[8] {
    return scan via sum from xs at [i] per i % 2 order desc thread lane let v { return v }
}

main {
    let tf32[8] xs ← [1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0] ↦ tf32[8]
    print running(xs)
    print before(xs)
    print by_parity(xs)
}
```

With `faber run --device reference` this prints:

```text
[1.0, 3.0, 6.0, 10.0, 11.0, 13.0, 16.0, 20.0]
[0.0, 1.0, 3.0, 6.0, 10.0, 11.0, 13.0, 16.0]
[8.0, 12.0, 7.0, 10.0, 4.0, 6.0, 3.0, 4.0]
```

The three optional clauses, in the order they are written:

| Clause | Effect |
|---|---|
| `total inclusive` / `total exclusive` | Inclusive (the default) includes the element itself in its prefix. Exclusive stops one element short, so the first position holds the operator's identity. |
| `per key` | Scans each group on its own. The key is any expression, as in `per i % 2`: elements with the same key form one ordered sequence. |
| `order desc` / `order asc` | Walks the prefix from the end instead of the start. A descending scan writes the mirrored prefix. |

Scans lower to the runner, Metal and CUDA. The scan operators are the
reduction operators that fold to a running value; `argmax`, `argmin` and
`first` are reductions only.

## Edge policies {#edge}

A shifted view reads cells that do not exist at the borders. An edge policy
says what those ghost cells hold. `.edge<clamp>()` repeats the border cell,
`.edge<reflect>()` mirrors across it, `.edge<wrap>()` wraps around, and
`coalesce` fills with a constant. In English the method word is `edge`; Latin
keeps `limes`, so `.limes<clamp>()` in an English file is an unknown method
(`SEM004`).

```faber locale=en
main {
    let tf32[3] base ← [1.0, 2.0, 3.0] ↦ tf32[3]
    let tf32[3] clamped ← base.shift([1]).edge<clamp>()
    let tf32[3] reflected ← base.shift([1]).edge<reflect>()
    let tf32[3] wrapped ← base.shift([1]).edge<wrap>()
    let tf32[3] filled ← base.shift([1]) coalesce 0.0
    print clamped.flatten()
    print reflected.flatten()
    print wrapped.flatten()
    print filled.flatten()
}
```

This prints `[2.0, 3.0, 3.0]`, `[2.0, 3.0, 2.0]`, `[2.0, 3.0, 1.0]` and
`[2.0, 3.0, 0.0]`.

## Kernels {#kernel}

`kernel` (Latin *nucleum*) declares a function that runs on a device. It takes the
place of `fn`. The optional mode word follows the parameter list, before the
return and error clauses:

```text
kernel name<T>(params) [relaxed|unsafe|fragment] [→ ret] [⇥ err] { … }
```

```faber locale=en
@ public
kernel scale(tf32[4] a, f32 k) → tf32[4] {
    return a * k
}

@ public
kernel scale_fast(tf32[4] a, f32 k) relaxed → tf32[4] {
    return a * k
}

kernel double(f32 x) fragment → f32 {
    return x * 2.0
}
```

`relaxed` and `unsafe` are the [safety tiers](/toolchain/cli.html#kernel-tiers).
`fragment` marks a helper that composes into a kernel: it is not an entry, and it
takes the tier of the kernel that uses it. Other annotations, such as `@ public`,
stand above the head.

The older form stays accepted, with the same meaning: `@ kernel` above an `fn`,
with `@ kernel relaxed`, `@ kernel unsafe` and `@ kernel fragment` for the modes.
One declaration takes one form. Both together is `PARSE018 nucleum_double_head`,
and `@ conversion` on a `kernel` head is `PARSE018 conversio_kernel_head`,
because a conversion is a host function. `kernel` is claimed only where a
declaration can start, so it stays an ordinary name elsewhere.

### Argument exclusivity {#kernel-exclusivity}

A kernel's arguments are device buffers, all live for the whole launch. Since
1.18 a writable argument, one passed `mut` or `own`, may not overlap any other
argument of the call. The rule is about storage, not order: the same tensor
twice, a `←` alias of it, and a view of it are all one overlap, whichever side
the writable argument is written on.

```faber locale=en outcome=rejects
@ public
kernel axpy(mut tf32[3] y, tf32[3] x) → void {
    y ⇇ x
}

main {
    mut tf32[3] t ← [1.0, 2.0, 3.0] ↦ tf32[3]
    axpy(mut t, t)
}
```

This is `SEM057 kernel_argument_overlap`. When a view is one side of the pair
the same call is `SEM057 tensor_view_read_only`. Read-only arguments may overlap
freely. To pass a value that must not overlap, bind an independent copy, or call
`materialize()` on a view first:

```faber locale=en
@ public
kernel axpy(mut tf32[3] y, tf32[3] x) → void {
    y ⇇ x
}

main {
    mut tf32[3] t ← [1.0, 2.0, 3.0] ↦ tf32[3]
    let tf32[3] snapshot ← copy t
    axpy(mut t, snapshot)
}
```

### Scratch rows {#scratch-rows}

Since 1.18 a lane may fill its own row of a scratch tensor, `scratch[[i, j]]`,
where `i` is the lane's coordinate and `j` is a `for range` binder inside the
lane. The flattened form `h[[i * pitch + j]]` is admitted too, when the range
proves that `j` stays below the pitch. A write that could reach another lane's
row stays refused (`SEM010 filum_independence_unproven`).

```faber locale=en
@ public
kernel row_totals(tf32[4, 3] w, mut tf32[4, 3] scratch, mut tf32[4] totals) → void {
    for from totals at [i] thread lane let unused {
        mut f32 total ← 0.0
        for range 0‥3 let j {
            scratch[[i, j]] ← w[[i, j]] * 2.0
            total ← total + w[[i, j]]
        }
        totals[[i]] ← total
    }
}
```

## Grouping device work: `do all` and `do device` {#device-regions}

A kernel can fail. A kernel that declares `⇥ string` reports on the error
channel, and on a device many lanes can fail at once. The lowest lane's error is
the one delivered, and delivery is a choice the block makes:

| Block | Where a kernel fault reaches `catch` |
|---|---|
| `do { … }` | Ordinary delivery, as for any failable call. |
| `do all { … }` | **Once, when the block exits**, however many launches ran. |
| `do device { … }` | The same, and the body is also checked as a device-resident region. |

```faber locale=en
@ public
kernel scale(tensor<f32, [4]> src, mut tensor<f32, [4]> dst) → void ⇥ string {
    for from src at [i] thread lane let v {
        if v ≺ 0.0 {
            throw "negative lane"
        }
        dst[[i]] ← v * 2.0
    }
}

main {
    let tensor<f32, [4]> src ← [1.0, -2.0, 3.0, -4.0] ↦ tensor<f32, [4]>
    mut tensor<f32, [4]> dst ← tf32[4] {}
    do all {
        scale(src, mut dst)
        scale(src, mut dst)
    }
    catch err {
        print err
    }
    print "done"
}
```

With `faber run --device cpu` this prints `negative lane` once and then `done`,
although two launches faulted. Reading a faulted output on the host inside the
block delivers the fault at that read.

`do device` marks the block as a **device-resident region**. The body may hold
kernel launches, `for range` loops and `if` conditions over captured scalars,
and `mut` scalar state, and nothing else. The checker refuses the rest by name:

| Written in the region | Diagnostic |
|---|---|
| A host call or a host effect such as `print` | `nucleum_host_call`, `nucleum_host_effect` |
| A tensor allocated inside | `nucleum_region_alloc_not_built` |
| A condition, bound or scalar store that reads a value computed on the device | `nucleum_region_device_read_not_built` |
| A `for…thread lane` loop written directly in the block | `nucleum_region_lane_loop_not_built` |
| A `return`, `break` or `continue` leaving the block | `nucleum_block_exit_crosses_boundary` |
| A nested `do device` | `fac_machina_nested` |

```faber locale=en
@ public
kernel bump(tensor<f32, [4]> dom, mut tensor<f32, [4]> t, i32 step) → void {
    for from dom at [i] thread lane let v {
        t[[i]] ← v + (step ↦ f32)
    }
}

main {
    mut tensor<f32, [4]> t ← tf32[4] {}
    let tensor<f32, [4]> z ← tf32[4] {}
    do device {
        for range 0‥8 let k {
            bump(z, mut t, k ↦ i32)
            if k % 2 ≡ 0 then bump(z, mut t, 1)
        }
    }
    catch err {
        print err
    }
}
```

A region is checked, not compiled differently: it executes exactly as
`do all`. `faber check --device cpu` (or `metal`, `cuda`) builds the device
image without running it and prints one `INFO001` line per region with its
inputs, in-outs, launches per iteration and host syncs. For the program
above:

```text
device region at line 12: inputs [z: tensor<f32, [4]>]; in-outs [t: tensor<f32, [4]>]; launches per iteration 1 (up to 2), 0 outside the loop; 0 host syncs
```

Only the handler stays outside the region: it receives faults and `⇥` errors
once, at the block's exit.

Related: [Types and values](/language/types.html#tensor) for the tensor types,
[Errors and testing](/language/errors.html) for `do { } catch`, and the
[GPU target](/targets/gpu.html) for what the device emitters produce.
