+++
title = "Bindings"
section = "cheatsheet"
order = 32
sources = []
+++

Binding a name to a value. `←` is the bind glyph: the value on the right goes
into the name on the left.

## Fixed or writable {#sit-varia}

`sit` binds a name once. `varia` binds a name you intend to change. `de` binds a
name that can be pointed elsewhere but never written through. `fixum` is
reserved for compile-time facts, written with `=`.

```faber locale-tabs
incipit {
    sit numerus limit ← 10
    varia numerus count ← 0

    count ← count + 1
    nota limit, count
}
```

Every binding word writes its type slot: `sit numerus limit ← 10`. There is no
short form, and `_` in the slot asks for inference (next section). Reassigning
a `sit` is a compile error, not a convention. Reach for `sit`
first and widen to `varia` only where the value genuinely moves.

## Type holes {#holes}

`_` is a type hole: the compiler infers one concrete type for the binding.

```faber locale-tabs
incipit {
    sit _ nomen ← "Marcus"
    sit _ numeri ← [1, 2, 3]
    nota nomen, numeri
}
```

The hole infers a type; it does not make the binding dynamic. `nomen` is
`textus` from this point on.

## Union types and holes {#union-holes}

An inline `A ∪ B` in type position names its union members explicitly. A
standalone `∪` is a *union* hole: the compiler infers a finite set of member
types rather than one.

```faber locale-tabs
incipit {
    sit numerus ∪ textus mixed ← 7
    sit lista<numerus ∪ textus> both ← [1, "two", 3]
    nota mixed, both
}
```

Read a union out with [`discerne`](/cheatsheet/control-flow.html#discerne),
which forces every arm to be handled.

## Optional values {#optional}

`T ∪ nihil` is the optional shape. It is an ordinary union whose other member
is nothing — Faber has no separate nullable syntax.

```faber locale-tabs
functio primum(lista<numerus> res) → numerus ∪ nihil {
    si res.longitudo() ≡ 0 ergo redde nulla
    redde res[0]
}

incipit {
    nota primum([1, 2, 3])
}
```

## Destructuring {#destructuring}

`ex` pulls named fields out of a record in one statement.

```faber locale-tabs
genus Punctum {
    sit numerus x
    sit numerus y
}

incipit {
    sit _ p ← Punctum { x = 1, y = 2 }
    ex p sit x, y
    nota x, y
}
```

Records are built with named fields in braces, not positional arguments — so
adding a field never silently reorders an existing call site.

Related: [Types and widths](/cheatsheet/types.html) ·
[Control flow](/cheatsheet/control-flow.html)
