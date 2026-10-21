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
    sit numerus n ← "42" ↦ numerus
    sit textus s ← 42 ↦ textus
    sit f64 f ← "3.14159" ↦ f64
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
    sit f64 x ← 2.5
    sit f64 y ← 3.5
    sit f64 z ← -2.5
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
    sit f64 x ← 2.5
    sit numerus n ← x ↦ numerus
    nota n
}
```

## Recovery on failure {#recovery}

`⊥` after a conversion supplies the value to use when it fails. Without it, a
failed conversion travels down the [error channel](/cheatsheet/errors.html).

```faber locale-tabs
incipit {
    sit numerus good ← "42" ↦ numerus ⊥ 0
    sit numerus bad ← "not a number" ↦ numerus ⊥ 0
    nota good, bad
}
```

`⊥` is not the error channel. `⇥` only ever names the error type a function may
fail with; `⊥` only ever holds a value. Read `⊥ 0` as *on failure, 0*.

## Chaining {#chaining}

Conversions apply left to right.

```faber locale-tabs
incipit {
    sit textus roundtrip ← "42" ↦ numerus ↦ textus
    nota roundtrip
}
```

## Converting to a width {#widths}

The target can name a precise width, not just a family.

```faber locale-tabs
incipit {
    sit i32 narrow ← "255" ↦ i32
    sit f32 single ← "1.5" ↦ f32
    nota narrow, single
}
```

## Bits and half floats {#bits}

A number converts to raw bits of the same width and back. Converting into
`f16` or `bf16` rounds to that format at the store.

```faber locale-tabs
incipit {
    sit u32 n ← 255
    sit b32 bits ← n ↦ b32
    sit f16 half ← 0.1 ↦ f16
    nota bits, bits ↦ u32, half ↦ f64
}
```

This prints `0x000000ff 255 0.0999755859375`. A width that does not match,
such as `u16 ↦ b32`, is `SEM016 bits_conversion_width_mismatch`.

## Conversion is not casting {#not-casting}

| | Conversion `↦` | Casting |
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
