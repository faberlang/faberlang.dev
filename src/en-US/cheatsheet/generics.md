+++
title = "Generics"
section = "cheatsheet"
order = 39
sources = []
+++

## Generic functions {#functions}

Type parameters go in angle brackets after the name.

```faber locale-tabs
functio identitas<T>(T datum) → T {
    redde datum
}

incipit {
    nota identitas("Marcus")
    nota identitas(42)
}
```

The same function serves both calls. `T` is fixed per call site, not erased to
a dynamic value.

## Generic with a union return {#union-return}

Type parameters compose with unions, which is how "maybe nothing" is expressed
generically.

```faber locale-tabs
functio primum<T>(lista<T> res) → T ∪ nihil {
    si res.longitudo() ≡ 0 ergo redde nulla
    redde res[0]
}

incipit {
    nota primum([1, 2, 3])
}
```

## Generic containers {#containers}

The built-in collections are generic already.

```faber locale-tabs
incipit {
    sit lista<textus> nomina ← ["Marcus", "Julia"]
    sit tabula<textus, numerus> aetates ← { "Marcus": 30 }
    nota nomina, aetates
}
```

## Records {#genus}

`genus` declares a record type with type-first fields.

```faber locale-tabs
genus Persona {
    sit textus nomen
    sit numerus aetas
}

functio descriptio(Persona p) → textus {
    redde p.nomen
}

incipit {
    sit p ← Persona { nomen = "Marcus", aetas = 30 }
    nota descriptio(p)
}
```

## Functions on a record {#methods}

A `genus` can carry functions alongside its fields.

```faber locale-tabs
genus Punctum {
    sit numerus x
    sit numerus y

    functio summa() → numerus {
        redde ego.x + ego.y
    }
}

incipit {
    sit p ← Punctum { x = 1, y = 2 }
    nota p.summa()
}
```

`self` is the receiver, what other languages spell `this`.

Related: [Types and widths](/cheatsheet/types.html) ·
[Functions and flow](/language/functions.html)
