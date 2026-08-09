+++
title = "Types and widths"
section = "cheatsheet"
order = 36
sources = []
+++

Types come before names. `textus nomen`, never `nomen: textus`.

## Everyday types {#everyday}

```faber
functio nihil_agit() → vacuum {
    nota "done"
}

incipit {
    fixum textus nomen ← "Marcus"
    fixum numerus aetas ← 30
    fixum bivalens ready ← verum
    fixum lista<numerus> empty ← vacua
    fixum numerus ∪ nihil missing ← nihil
    nota nomen, aetas, ready, empty, missing
    nihil_agit()
}
```

| Type | Is |
|---|---|
| `textus` | text |
| `numerus` | a number, default width |
| `bivalens` | true / false — `verum` / `falsum` |
| `vacuum` | the return type of a function that yields no value |
| `nihil` | absence — the other half of an optional |

Do not confuse `vacuum` with `vacua`. `vacuum` is a *type*, used as a return
annotation. `vacua` is a *value*: the empty collection, which is why it seeds
lists and tensors above. Binding `vacua` to something that is not a collection
is a compile error.

## Numeric widths {#widths}

`numerus` is the general number. When the width matters, name it directly —
these are the same family, spelled precisely.

```faber
incipit {
    fixum i32 signed ← -7
    fixum u8 byte ← 255
    fixum f64 wide ← 1.5
    nota signed, byte, wide
}
```

| Family | Widths |
|---|---|
| Signed | `i8` `i16` `i32` `i64` |
| Unsigned | `u8` `u16` `u32` `u64` |
| Floating | `f16` `f32` `f64` |

## Lists and tables {#collections}

```faber
incipit {
    fixum lista<numerus> numeri ← [1, 2, 3]
    fixum tabula<textus, numerus> aetates ← { "Marcus": 30, "Julia": 28 }

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

```faber
incipit {
    fixum lista<numerus ∪ textus> mixed ← [1, "two", 3]
    fixum _ inferred ← [1, 2, 3]
    nota mixed, inferred
}
```

## Tensors {#tensors}

A tensor carries an element type and a shape. `vacua` seeds an empty one;
`strue` builds a shaped tensor from flat values.

```faber
incipit {
    fixum lista<f32> flat ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    fixum tensor<f32, []> seed ← vacua
    fixum tensor<f32, [2, 3]> m ← seed.strue(flat, [2, 3])
    nota m.media()
}
```

### Shape sugar {#tensor-sugar}

`tf32[2, 3]` is sugar for `tensor<f32, [2, 3]>` — same type, shorter to read in
a signature.

```faber
functio medium(tf32[2, 3] m) → f32 {
    redde m.media()
}

incipit {
    fixum lista<f32> flat ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    fixum tf32[] seed ← vacua
    fixum tf32[2, 3] m ← seed.strue(flat, [2, 3])
    nota medium(m)
}
```

## Vectors {#vectors}

`vector<T, N>` is a fixed-width vector, with `vf32[N]` as its sugar. Build one
by converting a literal — the conversion is what fixes the width.

```faber
incipit {
    fixum vf32[4] v ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
    nota v
}
```

## Naming a type {#typus}

`typus` gives a type another name.

```faber
typus Nomen = textus
typus Puncta = lista<numerus>

incipit {
    fixum Nomen n ← "Marcus"
    fixum Puncta p ← [1, 2, 3]
    nota n, p
}
```

## Records {#genus}

`genus` declares a record. Fields are type-first, like everything else.

```faber
genus Persona {
    textus nomen
    numerus aetas
}

incipit {
    fixum _ p ← Persona { nomen = "Marcus", aetas = 30 }
    nota p.nomen, p.aetas
}
```

Related: [Bindings](/cheatsheet/bindings.html) ·
[Conversions](/cheatsheet/conversions.html) ·
[Types and values](/language/types.html)
