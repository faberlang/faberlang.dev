+++
title = "Error handling"
section = "syntax"
order = 5
sources = [
  "radix/README.md (Return and Error Channels)",
  "examples/corpus/iace/",
  "examples/corpus/fac/",
  "examples/corpus/cape/",
  "radix/docs/design/failable-conversio.md",
]
+++

Faber separates three related ideas that many languages collapse into one
shape:

| Construct | Meaning |
|-----------|---------|
| `→ T` | Normal success return channel |
| `T ∪ nihil` | Absence in the success value domain |
| `⇥ E` | Recoverable alternate-exit channel for errors |

## Normal return {#normal-return}

```faber
functio porta(numerus x) → numerus {
    si x < 0 ∴ redde 0
    redde x * 2
}
```

## Failable functions {#failable-functions}

Use `⇥` when a function can leave by an error channel:

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ∴ iace "division by zero"
    redde a / b
}
```

## Throwing — iace {#throwing--iace}

`iace` sends a value on the error channel:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ∴ iace "negative value"
}
```

## Recovery — fac / cape {#recovery--fac--cape}

Callers recover locally with a `fac` block and a `cape` handler:

```faber
functio divide(numerus a, numerus b) → numerus {
    si b ≡ 0 {
        redde 0
    }
    redde a / b
}

functio tutum(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    }
    cape err {
        mone err
        redde 0
    }
}
```

A direct failable call is not an ordinary expression. Place calls to
`→ T ⇥ E` functions inside an active `fac` / `cape` boundary.

## Inline conversion recovery {#inline-conversion-recovery}

`⇥` can also specify an inline recovery value on `↦` conversions:

```faber
fixum textus raw ← "42"
fixum _ n ← raw ↦ numerus ⇥ 0
```

## Effect-only failable {#effectonly-failable}

For functions that error but do not return a success value, omit `→ T`:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ∴ iace "negative value"
}
```

## Current status {#current-status}

`→`, `redde`, `⇥`, `iace`, and `fac` / `cape` are live grammar and checker
surfaces. Rust and Go lowering for full `⇥` / `iace` / `cape` runtime
behaviour is still a backend gap — these pass type-checking but do not
yet emit failable runtime code to all targets.
