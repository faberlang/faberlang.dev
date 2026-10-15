+++
title = "Types and widths"
section = "cheatsheet"
order = 36
sources = []
+++

Types come before names. `textus nomen`, never `nomen: textus`.

## Everyday types {#everyday}

```faber locale-tabs
functio nihil_agit() → vacuum {
    nota "done"
}

incipit {
    sit textus nomen ← "Marcus"
    sit i32 aetas ← 30
    sit bivalens ready ← verum
    sit lista<numerus> empty ← vacua
    sit numerus ∪ nihil missing ← nulla
    nota nomen, aetas, ready, empty, missing
    nihil_agit()
}
```

| Type | Is |
|---|---|
| `textus` | text |
| `i32` | a signed integer |
| `bivalens` | true / false — `verum` / `falsum` |
| `vacuum` | the return type of a function that yields no value |
| `nihil` | absence — the other half of an optional |

Do not confuse `vacuum` with `vacua`. `vacuum` is a *type*, used as a return
annotation. `vacua` is a *value*: the empty collection, which is why it seeds
lists and tensors above. Binding `vacua` to something that is not a collection
is a compile error.

## Numeric widths {#widths}

Name the width in type position. These are the numeric types and the raw-bit
types — the same list as
[Math in the ether](/language/behavior/numeric-widths.html).

```faber locale-tabs
incipit {
    sit i32 signed ← -7
    sit u8 byte ← 255
    sit f64 wide ← 1.5
    nota signed, byte, wide
}
```

| Family | Widths |
|---|---|
| Signed | `i8` `i16` `i32` `i64` |
| Unsigned | `u8` `u16` `u32` `u64` |
| Decimal | `d64` |
| Unbounded integer | `inf` |
| Floating | `f16` `bf16` `f32` `f64` |
| Raw bits | `b8` `b16` `b32` `b64` |

Raw bits are not numbers. A `b8` takes bit operators at its own width and has no
arithmetic; `x + x` on a `b8` is rejected (`SEM011 bits_arithmetic_refused`), and
a number converts to it only with an explicit `↦` from a number of the same
width (`u8 ↦ b8`), never from a bare literal.

## Lists and tables {#collections}

```faber locale-tabs
incipit {
    sit lista<numerus> numeri ← [1, 2, 3]
    sit tabula<textus, numerus> aetates ← { "Marcus": 30, "Julia": 28 }

    nota numeri[0]
    nota aetates["Marcus"]
    nota numeri.longitudo()
}
```

`lista<T>` holds many of one type. A `tabula` maps keys to values — the
`{ "key": value }` form above is [inline JSON](/language/types.html#inline-json)
ascribed to a map type, not a separate map literal, which is why it uses `:`
where Faber's typed construction uses `=`. Both take
[type holes](/cheatsheet/bindings.html#holes) and unions as their parameters:

```faber locale-tabs
incipit {
    sit lista<numerus ∪ textus> mixed ← [1, "two", 3]
    sit inferred ← [1, 2, 3]
    nota mixed, inferred
}
```

## Tensors {#tensors}

A tensor carries an element type and a shape. A flat list converts to a
shaped tensor with `↦` (`flat ↦ tf32[2, 3]`); `vacua` is the empty collection.

```faber locale-tabs
incipit {
    sit lista<f32> flat ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    sit tensor<f32, [2, 3]> m ← flat ↦ tensor<f32, [2, 3]>
    nota m.media()
}
```

### Shape sugar {#tensor-sugar}

`tf32[2, 3]` is sugar for `tensor<f32, [2, 3]>` — same type, shorter to read in
a signature.

```faber locale-tabs
functio medium(tf32[2, 3] m) → f32 {
    redde m.media()
}

incipit {
    sit lista<f32> flat ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    sit tf32[2, 3] m ← flat ↦ tf32[2, 3]
    nota medium(m)
}
```

## Vectors {#vectors}

`vector<T, N>` is a fixed-width vector, with `vf32[N]` as its sugar. Build one
by converting a literal — the conversion is what fixes the width.

```faber locale-tabs
incipit {
    sit vf32[4] v ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
    nota v
}
```

## Naming a type {#typus}

`typus` gives a type another name.

```faber locale-tabs
typus Nomen = textus
typus Puncta = lista<numerus>

incipit {
    sit Nomen n ← "Marcus"
    sit Puncta p ← [1, 2, 3]
    nota n, p
}
```

## Records {#genus}

`genus` declares a record. Fields are type-first, like everything else.

```faber locale-tabs
genus Persona {
    sit textus nomen
    sit numerus aetas
}

incipit {
    sit p ← Persona { nomen = "Marcus", aetas = 30 }
    nota p.nomen, p.aetas
}
```

Related: [Bindings](/cheatsheet/bindings.html) ·
[Conversions](/cheatsheet/conversions.html) ·
[Types and values](/language/types.html)
