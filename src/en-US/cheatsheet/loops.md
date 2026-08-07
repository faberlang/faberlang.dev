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

```faber
incipit {
    fixum lista<numerus> numeri ← [1, 2, 3]
    itera ex numeri fixum n {
        nota n
    }
}
```

## Over keys {#keys}

```faber
incipit {
    fixum tabula<textus, textus> persona ← { "nomen": "Marcus", "urbs": "Roma" }
    itera de persona fixum clavis {
        nota clavis, persona[clavis]
    }
}
```

The same mode gives you list indices, which is what you want when the position
matters as much as the value:

```faber
incipit {
    fixum lista<numerus> numeri ← [10, 20, 30]
    itera de numeri fixum index {
        nota index, numeri[index]
    }
}
```

## Over a range {#ranges}

`‥` builds a range. The lower bound is included, the upper bound is not.

```faber
incipit {
    itera ab 0‥3 fixum i {
        nota i
    }
}
```

`per` sets the step:

```faber
incipit {
    itera ab 0‥10 per 2 fixum i {
        nota i
    }
}
```

## While {#dum}

`dum` loops while a condition holds.

```faber
incipit {
    varia numerus i ← 0
    dum i < 3 {
        i ← i + 1
        nota i
    }
}
```

## Leaving early {#break}

`rumpe` breaks out; `perge` skips to the next iteration.

```faber
incipit {
    fixum lista<numerus> numeri ← [1, 2, 3, 4, 5]
    itera ex numeri fixum n {
        si n ≡ 2 ergo perge
        si n > 3 ergo rumpe
        nota n
    }
}
```

A loop can also carry its own error handler — see
[`cape` attaches to more than `fac`](/cheatsheet/errors.html#attachment).

Related: [Control flow](/cheatsheet/control-flow.html) ·
[Types and widths](/cheatsheet/types.html)
