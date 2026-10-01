# Bits

The Bits conversion hint is an exact-width IEEE bitcast — u16↔f16, u16↔bf16, u32↔f32, u64↔f64 only — never a value conversion.

**Term** `Bits` · **Section** CONVERSIONS · **Also** `Bits hint`

## Syntax

```
u16|u32|u64 ↦ f16|bf16|f32|f64 via Bits and f16|bf16|f32|f64 ↦ u16|u32|u64 via Bits
```

## What this teaches

- Exact pairs only — u16 pairs with f16 and bf16, u32 with f32, u64 with f64; any other width pairing rejects at the semantic gate with `bits_pair_width_mismatch`
- Reinterpretation, not conversion — Bits copies the bit pattern verbatim; the same u16 payload is a different value through a plain `↦` than through `↦ … via Bits`
- bf16 is not f16 — bf16 is the top half of an f32 value, not an f16 representation, so bf16↔f16 remains an ordinary value conversion and is never a Bits row
- Both directions — integer↦float and float↦integer through the hint are admitted symmetrically

## Common mistakes

- cross-width pairing — `n ↦ f32 via Bits` from u16 rejects (bits_pair_width_mismatch)
- expecting a float source to be a Bits row — a plain float→float hop with the hint rejects; spell the integer bit pattern side instead

## Example

```fab
fn in_f16(u16 n) → f16 {
    return n ↦ f16 via Bits
}

fn ex_bf16(bf16 x) → u16 {
    return x ↦ u16 via Bits
}

fn in_f32(u32 n) → f32 {
    return n ↦ f32 via Bits
}

fn ex_f64(f64 x) → u64 {
    return x ↦ u64 via Bits
}

main {
    const u32 n ← 1065353216
    print in_f32(n)
}
```

See also: [`↦`](↦.md), [`float`](float.md), [`bytes`](bytes.md).

Fetch list: https://faberlang.dev/agents/index.md
