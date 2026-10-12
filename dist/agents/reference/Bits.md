# Bits

The Bits conversion hint is retired: a bit pattern is a b16, b32 or b64 value, and ↦ bN reads or writes it — u16↔f16, u16↔bf16, u32↔f32, u64↔f64 only.

**Term** `Bits` · **Section** CONVERSIONS · **Also** `Bits hint`

## Syntax

```
u16|u32|u64 ↦ b16|b32|b64 ↦ f16|bf16|f32|f64 and f16|bf16|f32|f64 ↦ b16|b32|b64 ↦ u16|u32|u64
```

## What this teaches

- The rule, once — from a number, `↦` converts the value; from bits, `↦` to a same-width type reads those bits as that type
- A number holding a pattern says so in one step — `u16 ↦ b16 ↦ f16`; a float to its pattern is `x ↦ b16` (b32, b64 by width)
- Exact pairs only — b16 pairs with f16 and bf16, b32 with f32, b64 with f64; any other width pairing rejects at the semantic gate with `bits_conversion_width_mismatch`
- bf16 is not f16 — bf16 is the top half of an f32 value, not an f16 representation, so bf16↔f16 remains an ordinary value conversion
- Both directions — integer↦pattern↦float and float↦pattern↦integer are admitted symmetrically

## Common mistakes

- `via Bits` — retired; it is `conversio_via_bits_retired` and its help names the `↦ bN` replacement
- cross-width pairing — `n ↦ b16 ↦ f32` from u16 rejects (bits_conversion_width_mismatch)

## Example

```fab
fn in_f16(u16 n) → f16 {
    return n ↦ b16 ↦ f16
}

fn ex_bf16(bf16 x) → u16 {
    return x ↦ b16 ↦ u16
}

fn in_f32(u32 n) → f32 {
    return n ↦ b32 ↦ f32
}

fn ex_f64(f64 x) → u64 {
    return x ↦ b64 ↦ u64
}

main {
    const u32 n ← 1065353216
    print in_f32(n)
}
```

See also: [`↦`](↦.md), [`float`](float.md), [`bytes`](bytes.md).

Fetch list: https://faberlang.dev/agents/index.md
