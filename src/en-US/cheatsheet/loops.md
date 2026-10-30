+++
title = "Loops"
section = "cheatsheet"
order = 35
sources = []
+++

`itera` iterates. The word after it is the **mode** — what kind of traversal
this is — and it is required, so a loop always says what it walks.

| Mode | Walks |
|---|---|
| `ex` | the values of a collection |
| `de` | the keys of a table, or the indices of a list |
| `ab` | a numeric range |

## Over values {#values}

```faber locale-tabs
incipit {
    sit lista<numerus> numeri ← [1, 2, 3]
    itera ex numeri sit n {
        nota n
    }
}
```

### In lockstep {#lockstep}

`ex` also accepts a comma series: give it N collections and N name binders,
and the loop walks them all in lockstep — one shared index, one value from
each list per turn:

```faber locale-tabs
incipit {
    sit lista<textus> nomina ← ["Alia", "Brunus"]
    sit lista<numerus> aetates ← [34, 27]

    itera ex nomina, aetates apud [i] sit nomen, aetas {
        nota i, nomen, aetas
    }
}
```

`apud` (English `at`) names the shared index. The sources are listas, the
binders are plain names, and the first source owns the length: if a later
list is shorter, the loop stops with a runtime error rather than silently
truncating to the minimum.

## Over keys {#keys}

```faber locale-tabs
incipit {
    sit tabula<textus, textus> persona ← { "nomen": "Marcus", "urbs": "Roma" }
    itera de persona sit clavis {
        nota clavis, persona[clavis]
    }
}
```

The same mode gives you list indices, which is what you want when the position
matters as much as the value:

```faber locale-tabs
incipit {
    sit lista<numerus> numeri ← [10, 20, 30]
    itera de numeri sit index {
        nota index, numeri[index]
    }
}
```

## Over a range {#ranges}

`‥` builds a range. The lower bound is included, the upper bound is not.

```faber locale-tabs
incipit {
    itera ab 0 ‥ 3 sit i {
        nota i
    }
}
```

`per` sets the step:

```faber locale-tabs
incipit {
    itera ab 0 ‥ 10 per 2 sit i {
        nota i
    }
}
```

A range is also a value. Store it, print it, and walk it later; the English
type word is `range<int>`.

```faber locale-tabs
incipit {
    sit intervallum<numerus> r ← 0 ‥ 3
    nota r
    itera ab r sit i {
        nota i
    }
}
```

A stored range can carry a step, and the step is part of its type:
`let range<int, 2> evens ← 0 … 10 step 2` walks `0, 2, … 10`, and
`evens.length()` is `6`. See [ranges](/language/types.html#intervallum).

## While {#dum}

`dum` loops while a condition holds.

```faber locale-tabs
incipit {
    varia numerus i ← 0
    dum i ≺ 3 {
        i ← i + 1
        nota i
    }
}
```

## Leaving early {#break}

`rumpe` breaks out; `perge` skips to the next iteration.

```faber locale-tabs
incipit {
    sit lista<numerus> numeri ← [1, 2, 3, 4, 5]
    itera ex numeri sit n {
        si n ≡ 2 ergo perge
        si n ≻ 3 ergo rumpe
        nota n
    }
}
```

A loop can also carry its own error handler — see
[`cape` attaches to more than `fac`](/cheatsheet/errors.html#attachment).

## Thread loops {#thread}

A loop marked `thread` (la `filum`) runs its iterations as independent lanes:
`for from src at [i, j] thread lane let v { … }`. Because the lanes run
independently, one lane cannot stop the others. `continue` skips the rest of
this lane, but `break` is `SEM010 break_in_thread_body` and a plain `return` is
`SEM010 return_in_thread_body`. To use a lane's own stores, write only that
lane's coordinate; a loop whose independence the compiler cannot prove is
`SEM010 filum_independence_unproven`.

`return thread` (la `redde filum`) ends the current lane from any depth of the
lane body's own blocks. It takes no value, because lanes deliver results
through their stores. Anywhere else it is refused: outside a thread loop
(`SEM010 return_thread_outside_lane`), with a value
(`SEM010 return_thread_with_value`), or inside a nested closure or reduction
body (`SEM010 return_thread_in_nested_body`).

```faber locale=en
kernel lane_exit(tensor<f32, [4]> values) → void {
    for from values at [i] thread lane let value {
        return thread
    }
}
```

```faber locale=en outcome=rejects
fn run() → void {
    return thread
}

main {
    run()
}
```

Known issue in 1.18: `return thread` is checked but not yet compiled. The code
generators and the lowering to the runner's form refuse it by name
(`return_thread_lowering_pending`), so a program that uses it passes `faber
check` and stops at `faber check --lower`, `faber build` and `faber run`. The
formatter keeps it as written.

Related: [Control flow](/cheatsheet/control-flow.html) ·
[Types and widths](/cheatsheet/types.html)
