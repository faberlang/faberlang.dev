+++
title = "Bindings"
section = "cheatsheet"
order = 32
sources = []
+++

Binding a name to a value. `←` is the bind glyph: the value on the right goes
into the name on the left.

## Constant or variable {#fixum-varia}

`fixum` binds once. `varia` binds a name you intend to change.

```faber
incipit {
    fixum numerus limit ← 10
    varia numerus count ← 0

    count ← count + 1
    nota limit, count
}
```

Reassigning a `fixum` is a compile error, not a convention. Reach for `fixum`
first and widen to `varia` only where the value genuinely moves.

## Type holes {#holes}

`_` is a type hole: the compiler infers one concrete type for the binding.

```faber
incipit {
    fixum _ nomen ← "Marcus"
    fixum _ numeri ← [1, 2, 3]
    nota nomen, numeri
}
```

The hole infers a type; it does not make the binding dynamic. `nomen` is
`textus` from this point on.

## Union holes {#union-holes}

`∪` in type position is a *union* hole — the binding admits a finite set of
types rather than one.

```faber
incipit {
    fixum numerus ∪ textus mixed ← 7
    fixum lista<numerus ∪ textus> both ← [1, "two", 3]
    nota mixed, both
}
```

Read a union out with [`discerne`](/cheatsheet/control-flow.html#discerne),
which forces every arm to be handled.

## Optional values {#optional}

`T ∪ nihil` is the optional shape. It is an ordinary union whose other member
is nothing — Faber has no separate nullable syntax.

```faber
functio primum(lista<numerus> res) → numerus ∪ nihil {
    si res.longitudo() ≡ 0 ergo redde nihil
    redde res[0]
}

incipit {
    nota primum([1, 2, 3])
}
```

## Destructuring {#destructuring}

`ex` pulls named fields out of a record in one statement.

```faber
genus Punctum {
    numerus x
    numerus y
}

incipit {
    fixum _ p ← Punctum { x = 1, y = 2 }
    ex p fixum x, y
    nota x, y
}
```

Records are built with named fields in braces, not positional arguments — so
adding a field never silently reorders an existing call site.

Related: [Types and widths](/cheatsheet/types.html) ·
[Control flow](/cheatsheet/control-flow.html)
