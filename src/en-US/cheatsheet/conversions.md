+++
title = "Conversions"
section = "cheatsheet"
order = 37
sources = []
+++

`↦` converts a value to another type at runtime. It parses, coerces, and can
fail — which is exactly what distinguishes it from casting.

## Converting {#converting}

```faber locale-tabs
incipit {
    fixum numerus n ← "42" ↦ numerus
    fixum textus s ← 42 ↦ textus
    fixum f64 f ← "3.14159" ↦ f64
    nota n, s, f
}
```

## Float to integer {#rounding}

An integer becomes a float with a plain `↦`. A float becomes an integer only
with a rounding word, because the compiler will not pick one for you. A bare
`x ↦ numerus` on a float is `SEM016 float_to_integer_requires_rounding`.

The words follow `via`: `floor` rounds toward negative infinity, `ceil` toward
positive infinity, `trunc` toward zero, and `half_even` to the nearest integer,
with ties going to the even neighbour.

```faber
incipit {
    fixum f64 x ← 2.5
    fixum f64 y ← 3.5
    fixum f64 z ← -2.5
    nota x ↦ numerus via floor
    nota x ↦ numerus via ceil
    nota x ↦ numerus via half_even
    nota y ↦ numerus via half_even
    nota z ↦ numerus via trunc
    nota z ↦ numerus via floor
}
```

```text
$ faber run
2
3
2
4
-2
-3
```

`⌊2.5⌉` is the same nearest-even rounding written as a bracket: it is 2, and
`⌊3.5⌉` is 4. Leaving the word off is an error:

```faber outcome=rejects
incipit {
    fixum f64 x ← 2.5
    fixum numerus n ← x ↦ numerus
    nota n
}
```

## Recovery on failure {#recovery}

`⊥` after a conversion supplies the value to use when it fails. Without it, a
failed conversion travels down the [error channel](/cheatsheet/errors.html).

```faber locale-tabs
incipit {
    fixum numerus good ← "42" ↦ numerus ⊥ 0
    fixum numerus bad ← "not a number" ↦ numerus ⊥ 0
    nota good, bad
}
```

`⊥` is not the error channel. `⇥` only ever names the error type a function may
fail with; `⊥` only ever holds a value. Read `⊥ 0` as *on failure, 0*.

## Chaining {#chaining}

Conversions apply left to right.

```faber locale-tabs
incipit {
    fixum textus roundtrip ← "42" ↦ numerus ↦ textus
    nota roundtrip
}
```

## Converting to a width {#widths}

The target can name a precise width, not just a family.

```faber locale-tabs
incipit {
    fixum i32 narrow ← "255" ↦ i32
    fixum f32 single ← "1.5" ↦ f32
    nota narrow, single
}
```

## Conversion is not casting {#not-casting}

| | Conversion `↦` | Casting `∷` |
|---|---|---|
| When | Runtime | Compile time |
| Can fail | Yes — that is why `⊥` and the error channel exist | No |
| Means | "Parse or coerce this into that" | "I already know this is that" |

A conversion does work: it reads `"42"` and produces a number, and it has to
cope with `"banana"`. A cast asserts something to the compiler and produces no
runtime behaviour. If a value might not be what you claim, you want `↦` and a
recovery, not a cast.

Related: [Types and widths](/cheatsheet/types.html) ·
[Errors and catching](/cheatsheet/errors.html)
