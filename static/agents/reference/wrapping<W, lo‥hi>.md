# wrapping<W, lo‥hi>

A range as the second argument of wrapping: a store wraps around the range, offset by its low end.

**Term** `wrapping<W, lo‥hi>` · **Section** OPERATORS

## Syntax

```
wrapping<u32, 0‥5>
```

## What this teaches

- The store reduces modulo the size of the range and offsets by the low end, so a ring of five slots is `wrapping<u32, 0‥5>`: 5 lands on 0, 7 on 2.
- A range that does not start at zero wraps around its own span: `wrapping<u8, 3‥9>` holds 3 to 8, so 12 lands on 6 and 2 on 8.
- Below the low end wraps up from the high end — a counter stepping down from 0 lands on the top slot, not on a negative number.
- Arithmetic is exact. `k + 1` is an exact number; only the store into a ranged cell wraps it.

## Common mistakes

- Expecting `wrapping<u8, 3‥9>` to wrap at 256 — it wraps at its own range.
- Expecting the wrap to happen per operation — `(a + b) / 2` is exact, and the range applies once, where the result is stored.

## Example

```fab
main {
    # Constants wrap into [0, 5).
    let wrapping<u32, 0‥5> w ← 12
    print w
    # A counter around a ring of five slots.
    mut wrapping<u32, 0‥5> k ← 0
    k ← k + 1
    k ← k + 1
    k ← k + 1
    k ← k + 1
    k ← k + 1
    k ← k + 1
    print k
    # The range need not start at zero: offset by the low end.
    let wrapping<u8, 3‥9> hi ← 12
    let wrapping<u8, 3‥9> lo ← 2
    print hi
    print lo
    # Stepping below the low end wraps up from the top.
    mut wrapping<u32, 0‥3> ring ← 2
    ring ↑
    ring ↑
    print ring
    ring ↓
    ring ↓
    ring ↓
    print ring
    # Signed width, negative low end: [-2, 3).
    let wrapping<i32, -2‥3> wi ← 100
    print wi
    # The wrap happens at the store, not in the middle of an expression.
    let wrapping<u32, 0‥7> m ← 6
    print m * 3 - 1
    let wrapping<u32, 0‥7> stored ← m * 3 - 1
    print stored
    # An int enters a wrapping cell through `↦`.
    let int n ← 100
    let wrapping<u32, 0‥5> fromInt ← n ↦ wrapping<u32, 0‥5>
    print fromInt
}
```

See also: [`saturating<W, lo‥hi>`](saturating<W, lo‥hi>.md), [`trapping<W, lo‥hi>`](trapping<W, lo‥hi>.md), [`‥`](‥.md), [`…`](….md).

Fetch list: https://faberlang.dev/agents/index.md
