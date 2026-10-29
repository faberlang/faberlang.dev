# trapping<W, lo‥hi>

A range as the second argument of trapping: a store inside the range keeps its value, a store outside it traps.

**Term** `trapping<W, lo‥hi>` · **Section** OPERATORS

## Syntax

```
trapping<i32, -2‥3>
```

## What this teaches

- A bare integer type is `trapping` over its whole width; a range narrows the cells it accepts. `trapping<i32, -2‥3>` holds -2 to 2: a cell for a step, an offset or an index that must stay in bounds.
- A value in the range is stored as is. One outside it traps at the store (see `ranged-trapping-trap`); nothing is clamped or wrapped.
- Arithmetic is exact. `dy + dz` can leave the range and prints exactly; only a store into a ranged cell checks it.
- A ranged cell reads as its width: it passes where an `i32` is wanted, and it widens into a cell with a wider range without a check.
- `u8` is the same type as `trapping<u8, 0…255>`.

## Common mistakes

- Expecting a trap in the middle of an expression — the range is checked where a value is stored into the cell, not where it is computed.
- Writing a range on a float width — `trapping<f32, 0‥8>` is refused.

## Example

```fab
fn offset(trapping<i32, -2‥3> dy) → int {
    return dy
}

fn grow(trapping<u8, 0‥10> small) → trapping<u8, 0‥20> {
    return small
}

main {
    let i32 d ← 2
    let trapping<i32, -2‥3> dy ← d
    let i32 e ← -2
    let trapping<i32, -2‥3> dz ← e
    print dy
    print dz
    # Exact arithmetic: 4 is outside -2‥3 and prints as 4; nothing is stored.
    print dy + dy
    # A ranged cell reads as its width.
    let i32 back ← dy
    print back
    print offset(-2)
    # The inclusive glyph holds its high end.
    let trapping<u8, 1…5> top ← 5
    print top
    # Widening a range needs no check.
    let trapping<u8, 0‥20> larger ← grow(7)
    print larger
    # A ranged cell indexes a list: it can only name a slot inside its range.
    let list<int> xs ← [10, 20, 30, 40]
    let trapping<u8, 0‥4> ix ← 2
    print xs[ix]
    # The whole-width range is the bare type.
    let trapping<u8, 0…255> same ← 200
    let u8 plain ← same
    print plain
}
```

See also: [`saturating<W, lo‥hi>`](saturating<W, lo‥hi>.md), [`wrapping<W, lo‥hi>`](wrapping<W, lo‥hi>.md), [`‥`](‥.md), [`…`](….md).

Fetch list: https://faberlang.dev/agents/index.md
