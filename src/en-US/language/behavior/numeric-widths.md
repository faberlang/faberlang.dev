+++
title = "Math in the ether"
section = "language"
order = 12
sources = [
  "radix/docs/design/numeric-model.md",
]
+++

Faber treats a number's width the way measurement treats a value: it has no
width until it is observed. A value is observed when it is stored into a cell
or converted into one. Until then, no boundary applies to it.

So arithmetic runs unbounded — or as bare IEEE for floats — and a width limit
is applied **once**, at the store or the conversion. Nothing clamps, traps,
saturates or wraps per operation. In `(100 + 200) / 2` the sum, 300, does not
fit a `u8`, but nothing is checked there: the expression evaluates to 150, and
only the store into a `u8` cell is checked, where 150 fits.

The policy belongs to the cell, not to the arithmetic. An integer cell is one
of three:

| Cell | On store or conversion |
|---|---|
| `saturating<u8>` | clamps to the cell's range |
| `wrapping<u8>` | reduces modulo the cell's width |
| `trapping<u8>` | errors when the value does not fit |

`inf` is the integer that stays unbounded after it is stored. A value that
does not fit a fixed-width cell does not become `inf` by itself: the cell
still applies its policy, and a bounded intermediate that leaves the 64-bit
range traps. Write `inf` on a slot, or put an `inf` operand in the
expression, and the unbounded width takes over — any integer width widens
into it, and a store into an `inf` cell is never a size check.

Float cells follow the same rule: a bare `f64` and a `saturating<f64>` both
give ±infinity on overflow, because there is no maximum finite value to clamp
to; only a `trapping<f64>` cell errors, and only when a non-finite value is
stored or converted into it.

## What it looks like {#shape}

The same unbounded sum is stored into cells with different policies:

```faber
incipit {
    fixum numerus a ← 200
    fixum numerus b ← 100
    fixum numerus exact ← (a + b) / 2
    nota exact
    fixum saturatus<u8> sat ← (a + b) ↦ saturatus<u8>
    nota sat
    fixum modulus<u8> wrap ← (a + b) ↦ modulus<u8>
    nota wrap
}
```

```text
$ faber run
150
255
44
```

`(a + b)` is 300 in the ether, and `(a + b) / 2` is exactly 150 — the
unbounded `int` keeps it. The limits appear only where the value becomes a
`u8`: the sum saturates to 255 in a `saturating` cell, and reduces to 44 in a
`wrapping` cell.

A `trapping` cell turns the same overflow into an error at the store:

```faber
incipit {
    fixum numerus big ← 300
    fixum exactus<u8> cell ← big ↦ exactus<u8>
    nota cell
}
```

```text
$ faber run
error: numerus to numerus conversion out of range
```

## Why it works this way {#why}

The rule buys predictability. A reader can look at an expression and reason
about it as arithmetic, without carrying the widths of every operand in their
head or wondering where an implicit reduction happens. The one place a boundary
can bite is the one place the source names it: the store, or the `↦`.

It also composes with the rest of the language. Because numeric families do not
mix silently, an operation between two different numeric types is an explicit
conversion — which is exactly the point where a policy would be applied. A
`saturating` or `wrapping` cell cannot fail on conversion, so the conversion
needs no default and no error channel; a `trapping` cell is where an
out-of-range store is reported. See [Types and values](/language/types.html)
for the cell types themselves.

Every numeric width, the overflow policies it accepts, and the policy a bare
marker uses:

| Width | Policies | Bare default |
|---|---|---|
| `i8` | `trapping`, `wrapping`, `saturating` | `trapping` |
| `i16` | `trapping`, `wrapping`, `saturating` | `trapping` |
| `i32` | `trapping`, `wrapping`, `saturating` | `trapping` |
| `i64` | `trapping`, `wrapping`, `saturating` | `trapping` |
| `u8` | `trapping`, `wrapping`, `saturating` | `trapping` |
| `u16` | `trapping`, `wrapping`, `saturating` | `trapping` |
| `u32` | `trapping`, `wrapping`, `saturating` | `trapping` |
| `u64` | `trapping`, `wrapping`, `saturating` | `trapping` |
| `d64` | `trapping` | `trapping` |
| `inf` | `trapping`, `wrapping`, `saturating` — one type | unbounded |
| `f16` | `trapping`, `saturating` | `saturating` |
| `bf16` | `trapping`, `saturating` | `saturating` |
| `f32` | `trapping`, `saturating` | `saturating` |
| `f64` | `trapping`, `saturating` | `saturating` |
