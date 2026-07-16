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

## Conditional branching {#conditional-branching}

### si / sin / secus {#si-sin-secus}

```faber
incipit {
    fixum _ condition ← verum
    si condition {
        # truthy branch
        nota "matched"
    }
}
```

With else-if and else:

```faber
incipit {
    fixum _ score ← 85
    si score ≥ 90 {
        nota "A"
    } sin score ≥ 80 {
        nota "B"
    } secus {
        nota "C"
    }
}
```

### Compact branch with ∴ {#compact-branch-with}

A single-statement branch body uses `∴` (or its alias `ergo`):

```faber
functio classify(numerus b, bivalens ready, numerus value) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    si ready ∴ redde value
    redde nihil
}
```

## Iteration {#iteration}

### Values — itera ex {#values-itera-ex}

```faber
functio inveni(lista<numerus> items, numerus target) → numerus ∪ nihil {
    itera ex items fixum item {
        si item ≡ target ∴ redde item
    }
    redde nihil
}
```

### Keys — itera de {#keys-itera-de}

```faber
incipit {
    fixum _ tabula ← { "unus": 1, "duo": 2 }
    itera de tabula fixum key {
        nota key
    }
}
```

### Range — itera ab {#range-itera-ab}

```faber
itera ab 0‥10 fixum i {
    nota i
}
```

## While loops {#while-loops}

```faber
incipit {
    fixum _ condition ← verum
    dum condition {
        # body
        tacet
    }
}
```

## Guard sections — custodi {#guard-sections-custodi}

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

## Pattern matching — elige {#pattern-matching-elige}

`elige` selects the first matching arm:

```faber
functio describe(numerus value) → textus {
    elige value {
        casu 1 { redde "one" }
        casu 2 { redde "two" }
        ceterum { redde "many" }
    }
}
```

## Tagged union matching — discerne {#tagged-union-matching-discerne}

`discerne` exhaustively matches `discretio` variants:

```faber
discretio Exitus {
    Bonum { textus nuntius },
    Malum { textus causa }
}

functio refer(Exitus eventus) → textus {
    discerne eventus {
        casu Bonum fixum nuntius { redde nuntius }
        casu Malum fixum causa { redde "Error: §"(causa) }
    }
}
```

## Try blocks — fac / cape {#try-blocks-fac-cape}

`fac` opens a block that may throw, and `cape` recovers:

```faber
functio divide(numerus a, numerus b) → numerus {
    redde a / b
}

functio tutus(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    } cape err {
        mone err
        redde 0
    }
}
```
