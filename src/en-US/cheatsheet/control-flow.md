+++
title = "Control flow"
section = "cheatsheet"
order = 34
sources = []
+++

## Branching {#branching}

`si` / `sin` / `secus` — if, else-if, else.

```faber
incipit {
    fixum numerus n ← 2

    si n ≡ 1 {
        nota "one"
    } sin n ≡ 2 {
        nota "two"
    } secus {
        nota "many"
    }
}
```

## One-line branch {#ergo}

`ergo` takes a single statement instead of a block. Useful for guards.

```faber
functio abs(numerus n) → numerus {
    si n < 0 ergo redde 0 - n
    redde n
}

incipit {
    nota abs(-5)
}
```

## Selecting over a value {#elige}

`elige` picks an arm by value. `ceterum` is the fallback.

```faber
incipit {
    fixum numerus n ← 2

    elige n {
        casu 1 { nota "one" }
        casu 2 { nota "two" }
        ceterum { nota "many" }
    }
}
```

## Matching a union {#discerne}

`discerne` matches over a union-typed value. This is how a
[union hole](/cheatsheet/bindings.html#union-holes) gets read back out.

```faber
incipit {
    fixum numerus ∪ textus signum ← 7

    discerne signum {
        casu 7 { nota "the number seven" }
        casu "x" { nota "the letter x" }
        ceterum { nota "something else" }
    }
}
```

The difference from `elige` is intent: `elige` chooses among values of one
type, `discerne` discriminates among the members of a union.

## Returning {#redde}

`redde` returns a value. A function with no `→` returns nothing and needs no
`redde`.

```faber
functio duplica(numerus n) → numerus {
    redde n * 2
}

functio saluta(textus nomen) {
    nota nomen
}

incipit {
    nota duplica(21)
    saluta("Marcus")
}
```

To exit by the *error* channel instead, see
[Errors and catching](/cheatsheet/errors.html).

Related: [Loops](/cheatsheet/loops.html) ·
[Functions and flow](/language/functions.html)
