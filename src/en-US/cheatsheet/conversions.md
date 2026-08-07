+++
title = "Conversions"
section = "cheatsheet"
order = 37
sources = []
+++

`↦` converts a value to another type at runtime. It parses, coerces, and can
fail — which is exactly what distinguishes it from casting.

## Converting {#converting}

```faber
incipit {
    fixum numerus n ← "42" ↦ numerus
    fixum textus s ← 42 ↦ textus
    fixum f64 f ← "3.14159" ↦ f64
    nota n, s, f
}
```

## Recovery on failure {#recovery}

`⇥` after a conversion supplies the value to use when it fails. Without it, a
failed conversion travels down the [error channel](/cheatsheet/errors.html).

```faber
incipit {
    fixum numerus good ← "42" ↦ numerus ⇥ 0
    fixum numerus bad ← "not a number" ↦ numerus ⇥ 0
    nota good, bad
}
```

This is the same glyph as the error channel in a function signature, doing the
same job in miniature: *this may fail, and here is the other path*.

## Chaining {#chaining}

Conversions apply left to right.

```faber
incipit {
    fixum textus roundtrip ← "42" ↦ numerus ↦ textus
    nota roundtrip
}
```

## Converting to a width {#widths}

The target can name a precise width, not just a family.

```faber
incipit {
    fixum i32 narrow ← "255" ↦ i32
    fixum f32 single ← "1.5" ↦ f32
    nota narrow, single
}
```

## Conversion is not casting {#not-casting}

| | Conversion `↦` | Casting |
|---|---|---|
| When | Runtime | Compile time |
| Can fail | Yes — that is why `⇥` exists | No |
| Means | "Parse or coerce this into that" | "I already know this is that" |

A conversion does work: it reads `"42"` and produces a number, and it has to
cope with `"banana"`. A cast asserts something to the compiler and produces no
runtime behaviour. If a value might not be what you claim, you want `↦` and a
recovery, not a cast.

Related: [Types and widths](/cheatsheet/types.html) ·
[Errors and catching](/cheatsheet/errors.html)
