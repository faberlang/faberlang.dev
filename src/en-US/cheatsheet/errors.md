+++
title = "Errors and catching"
section = "cheatsheet"
order = 33
sources = []
+++

Faber does not throw errors the way most languages do. A failure travels back
through a **dedicated error channel**, declared in the signature and separate
from the return value. That one decision shapes everything on this page.

## The error channel {#channel}

`→` declares what a function returns. `⇥` declares what it may fail with.

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ergo iace "division by zero"
    redde a / b
}
```

Read it as: *returns a number, or fails with a textus*. The two channels are
independent — the success type is not widened, wrapped, or made optional to
accommodate failure. A caller reading the signature knows both shapes before
looking at the body.

`iace` sends a value down the error channel. It is not `redde`: it exits by the
other route.

## Catching {#cape}

`cape` binds whatever came down the error channel.

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ergo iace "division by zero"
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

incipit {
    nota tutum(10, 2)
    nota tutum(10, 0)
}
```

`tutum` has no `⇥` in its signature, and that is the point: it handles the
failure, so it cannot itself fail. The channel stops here.

## `cape` attaches to more than `fac` {#attachment}

This is the part that surprises people arriving from other languages. `cape` is
not the tail of a try statement — it attaches to **structured statements
generally**. A loop can carry its own handler:

```faber
incipit {
    fixum lista<textus> raw ← ["1", "two", "3"]
    itera ex raw fixum item {
        fixum numerus n ← item ↦ numerus
        nota n
    }
    cape err {
        mone err
    }
}
```

And so can a `dum` loop:

```faber
incipit {
    varia numerus i ← 0
    dum i < 3 {
        i ← i + 1
        si i ≡ 2 ergo iace "halfway"
    }
    cape err {
        mone err
    }
}
```

The handler belongs to the construct it follows. There is no separate `try`
keyword to wrap things in — `fac` is simply the bare block form for when you
want a handler and have no other statement to hang it on.

## Failing without a message {#propagate}

A function that declares `⇥` and does not catch propagates automatically —
callers must deal with it or declare their own channel.

```faber
functio parse(textus raw) → numerus ⇥ textus {
    si raw ≡ "" ergo iace "empty input"
    redde raw ↦ numerus ⇥ 0
}

functio duplum(textus raw) → numerus ⇥ textus {
    redde parse(raw) * 2
}

incipit {
    fac {
        nota duplum("21")
    }
    cape err {
        mone err
    }
}
```

`duplum` never mentions failure in its body. It declares the channel and lets
`parse`'s failure travel through.

## Errors as a parameter {#errata}

`errata` marks a parameter that carries an error value, for functions written
to receive one rather than produce it.

```faber
functio logga(textus context) errata textus → vacuum {
    mone context
}
```

Related: [Testing](/cheatsheet/testing.html) ·
[Conversions](/cheatsheet/conversions.html) for `⇥` in its other role, as
conversion recovery · [Errors and testing](/language/errors.html) for the full
treatment.
