+++
title = "Generics"
section = "cheatsheet"
order = 39
sources = []
+++

## Generic functions {#functions}

Type parameters go in angle brackets after the name.

```faber
functio identitas<T>(T valor) → T {
    redde valor
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

```faber
functio primum<T>(lista<T> res) → T ∪ nihil {
    si res.longitudo() ≡ 0 ergo redde nihil
    redde res[0]
}

incipit {
    nota primum([1, 2, 3])
}
```

## Generic containers {#containers}

The built-in collections are generic already.

```faber
incipit {
    fixum lista<textus> nomina ← ["Marcus", "Julia"]
    fixum tabula<textus, numerus> aetates ← { "Marcus": 30 }
    nota nomina, aetates
}
```

## Records {#genus}

`genus` declares a record type with type-first fields.

```faber
genus Persona {
    textus nomen
    numerus aetas
}

functio descriptio(Persona p) → textus {
    redde p.nomen
}

incipit {
    fixum _ p ← Persona { nomen = "Marcus", aetas = 30 }
    nota descriptio(p)
}
```

## Functions on a record {#methods}

A `genus` can carry functions alongside its fields.

```faber
genus Punctum {
    numerus x
    numerus y

    functio summa() → numerus {
        redde ego.x + ego.y
    }
}

incipit {
    fixum _ p ← Punctum { x = 1, y = 2 }
    nota p.summa()
}
```

`ego` — "I" — is the receiver, what other languages spell `this` or `self`.

Related: [Types and widths](/cheatsheet/types.html) ·
[Functions and flow](/language/functions.html)
