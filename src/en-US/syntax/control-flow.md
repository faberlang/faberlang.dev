+++
title = "Control flow"
section = "syntax"
order = 4
sources = [
  "radix/README.md (Control Flow Shape, Canonical Surface)",
  "examples/corpus/si/",
  "examples/corpus/itera/",
  "examples/corpus/dum/",
  "examples/corpus/custodi/",
  "examples/corpus/discerne/",
  "examples/corpus/elige/",
]
+++

## Conditional branching

### si / sin / secus

```faber
si condition {
    // truthy branch
}
```

With else-if and else:

```faber
si score ≥ 90 {
    nota "A"
} sin score ≥ 80 {
    nota "B"
} secus {
    nota "C"
}
```

### Compact branch with ∴

A single-statement branch body uses `∴` (or its alias `ergo`):

```faber
si b ≡ 0 ∴ redde nihil
si ready ∴ redde value
```

## Iteration

### Values — itera ex

```faber
itera ex items fixum item {
    si item ≡ target ∴ redde item
}
```

### Keys — itera de

```faber
itera de tabula fixum key {
    nota key
}
```

### Range — itera ab

```faber
itera ab 0‥10 fixum i {
    nota i
}
```

## While loops

```faber
dum condition {
    // body
}
```

## Guard sections — custodi

`custodi` groups early-exit checks before a function's main body.
Each `si` clause is a sequential guard:

```faber
functio divide(numerus a, numerus b) → numerus {
    custodi {
        si b ≡ 0 {
            redde 0
        }
    }
    redde a / b
}
```

`custodi` is not breakable in v1 — it is a guard rail, not a loop.

## Pattern matching — elige

`elige` selects the first matching arm:

```faber
elige value {
    si pattern → { ... }
    si pattern → { ... }
    secus → { ... }
}
```

## Tagged union matching — discerne

`discerne` exhaustively matches `discretio` variants:

```faber
discretio Exitus {
    Bonum { textus nuntius }
    Malum { textus causa }
}

functio refer(exitus) → textus {
    discerne exitus {
        Bonum { nuntius } → nuntius
        Malum { causa } → "Error: §"(causa)
    }
}
```

## Try blocks — fac / cape

`fac` opens a block that may throw, and `cape` recovers:

```faber
fac {
    redde divide(a, b)
}
cape err {
    mone err
    redde 0
}
```
