# saturating<W, lo‥hi>

A range as the second argument of saturating: a store clamps into the range, not only into the width.

**Term** `saturating<W, lo‥hi>` · **Section** OPERATORS

## Syntax

```
saturating<u32, 0‥8>
```

## What this teaches

- A range is the second argument of the store policy: the width stays explicit and the range refines it. `‥` is half open (`0‥8` holds 0 to 7), `…` is inclusive (`1…5` holds 1 to 5). Both ends are always written.
- Clamp at the store — a value past either end lands on that end, exactly like `saturating<u8>` clamps at the width.
- Exact arithmetic — `a + b` is an exact number; only the store into a ranged cell applies the range. Converting between ranges is a store too.
- `∞` and `-∞` write "no bound on this side": `-∞‥8` has no low end.
- `saturating<u8>` is the same type as `saturating<u8, 0…255>`.

## Common mistakes

- Writing `u8<0‥8>` — the policy word is mandatory with a range.
- Writing `0…` — both ends are always written; use `0…∞` for "no high end".
- Mixing policy families — `saturating<u32, 0‥8> + wrapping<u32, 0‥8>` is an error; convert with `↦`.

## Example

```fab
main {
    # The high end of a half-open range is not held: 20 lands on 7.
    let saturating<u32, 0‥8> a ← 20
    let saturating<u32, 0‥8> b ← 3
    print a
    print b
    # Arithmetic is exact; the range applies once, at the store.
    print a + b
    let saturating<u32, 0‥8> c ← a + b
    print c
    mut saturating<u32, 0‥8> level ← 6
    level ↑
    level ↑
    print level
    level ↓
    level ↓
    level ↓
    level ↓
    level ↓
    level ↓
    level ↓
    level ↓
    print level
    # Inclusive range and a signed width.
    let saturating<i16, -5…5> tilt ← -9
    print tilt
    # No bound on one side.
    let saturating<i32, -∞‥8> ceiling ← 99
    let saturating<u32, 4‥∞> floor ← 1
    print ceiling
    print floor
    # An int enters a saturating cell through `↦`.
    let int n ← 100
    let saturating<u32, 0‥8> fromInt ← n ↦ saturating<u32, 0‥8>
    print fromInt
    # Narrowing a range is a store: the destination range applies.
    let saturating<u32, 0‥20> wide ← 15
    let saturating<u32, 0‥10> narrow ← wide
    print narrow
    # The whole-width range is the existing spelling: one type, no conversion.
    let saturating<u8> plain ← 300
    let saturating<u8, 0…255> same ← plain
    print same
}
```

See also: [`trapping<W, lo‥hi>`](trapping<W, lo‥hi>.md), [`wrapping<W, lo‥hi>`](wrapping<W, lo‥hi>.md), [`‥`](‥.md), [`…`](….md).

Fetch list: https://faberlang.dev/agents/index.md
