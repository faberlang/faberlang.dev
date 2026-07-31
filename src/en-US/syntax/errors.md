+++
title = "Error handling"
section = "syntax"
order = 5
sources = [
  "radix/README.md (Return and Error Channels)",
  "radix/corpus/iace/",
  "radix/corpus/fac/",
  "radix/corpus/cape/",
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
    si x < 0 ergo redde 0
    redde x * 2
}
```

## Failable functions {#failable-functions}

Use `⇥` when a function can leave by an error channel:

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ergo iace "division by zero"
    redde a / b
}
```

## Throwing — iace {#throwing--iace}

`iace` sends a value on the error channel:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
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

## The alternate channel in async surfaces {#async-alternate}

The same `⇥ E` channel rides *inside* Faber's async types rather than as a
separate mechanism. A `fiet` function returns `promissum<T>` — the
infallible shorthand for `promissum<T ⇥ numquam>` — and `promissum<T ⇥ E>`
preserves the delayed alternate alongside the eventual value. Awaiting a
failable promise is itself a failable operation: the success value binds
inside a `fac` / `cape` boundary while the failure stays observable, exactly
like a failable sync call.

Async and sync streams carry the channel too: `fient → T ⇥ E` makes every
pull a promise that can yield, end, or fail (the first failure ends the
stream, handled by `itera ex`); `fiunt → T ⇥ E` makes the stream call itself
failable, recovered with `fac` / `cape`.

See [Functions — two-channel promises](/syntax/functions.html#two-channel-promises)
for the full treatment.

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
    si value < 0 ergo iace "negative value"
}
```

## Current status {#current-status}

`→`, `redde`, `⇥`, `iace`, and `fac` / `cape` are live grammar and checker
surfaces. Rust and Go lowering for full `⇥` / `iace` / `cape` runtime
behaviour is still a backend gap — these pass type-checking but do not
yet emit failable runtime code to all targets.
