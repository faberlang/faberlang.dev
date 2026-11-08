# Kernels and device blocks

A kernel is a function that runs on a device. `kernel` takes the place of `fn`,
and a mode word, `relaxed`, `unsafe` or `fragment`, follows the parameter list.
Other annotations stand above the head. A kernel that host code calls is
`@ public`.

```faber locale=en
@ public
kernel scale(tf32[4] a, f32 k) relaxed → tf32[4] {
    return a * k
}
```

`@ kernel` above an `fn` stays accepted, and `faber format` keeps whichever head
it finds; `faber format --normalize-kernel-heads` rewrites it. Both on one
declaration is `PARSE018` `nucleum_double_head`. Write `kernel` in new code.

`f64` is legal in a kernel. The CPU device and CUDA run it natively; Metal and
WGSL refuse the kernel by name, and AMD refuses it until a native path is
verified. Nothing narrows `f64` silently, and `--device auto` does not pick the
CPU for it: pass `--device cpu`.

A writable kernel argument, `mut` or `own`, may not overlap another argument of
the call: the same tensor twice, a `←` alias, or a view of it. That is `SEM057`
`kernel_argument_overlap`, or `tensor_view_read_only` when a view is one side of
the pair. Read-only arguments may overlap. Bind `← copy t` or call
`materialize()` to pass independent storage.

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

`do batch { … }` runs its kernel launches under deferred fault delivery. A kernel
that declares `⇥ string` can fail on many lanes at once, and the handler
receives the lowest lane's error once, when the block exits, however many
launches ran.

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
    do batch {
        scale(src, mut dst)
        scale(src, mut dst)
    }
    catch err {
        print err
    }
    print "done"
}
```

`faber run --device cpu` prints `negative lane` once, then `done`. `do all` is
the legacy spelling of `do batch` and stays accepted.

`do device { … } catch err { … }` is `do batch` plus a check: the body is a
device-resident region. It may hold kernel launches, `for range` loops and `if`
conditions over captured scalars, and `mut` scalar state. A host call, a host
effect such as `print`, a tensor allocated inside, a condition that reads a
device-computed value, a lane loop written in the block, a `return`, `break` or
`continue` that leaves it, and a nested `do device` are each refused by name.
The region executes exactly as `do batch`.

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

`faber check --device cpu` (or `metal`, `cuda`) builds the device image without
running it and prints each region's inputs, in-outs, launches per iteration and
host syncs.

`do eligible { … }` grants device eligibility to its body and the functions it
calls synchronously; with `--device-mode eligible` analysis may admit proved
ordinary functions there. In 1.19 it checks and runs with ordinary `do` fault
timing, and does not yet place code on a device. A `do` takes one modifier
word; nest blocks to combine them.

Parent: https://faberlang.dev/agents/tensors.md

Fetch list: https://faberlang.dev/agents/index.md
