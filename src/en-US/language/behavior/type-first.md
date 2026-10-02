+++
title = "Types before names"
section = "language"
order = 11
sources = [
  "radix/docs/design/conversio-valor.md",
  "radix/corpus/conversio/",
]
+++

Faber puts the type before the name in every declaration — parameters, locals,
and fields alike. A variable is `f64 low`, never `low: f64`. A function is
`fn center() → f64`, with the return type after the arrow.

The choice is about what a reader learns first. The type tells you *what kind
of thing* this is; the name tells you *which one*. Reading shape before
binding also matches languages whose grammar runs from category to instance,
so a declaration scans the same way whether the keywords are English, Chinese
or Arabic.

There is one form to learn. A declaration is a type followed by a name, and it
is the same shape whether it is a parameter, a local, a field, or a return.

## Bindings are three words {#bindings}

| Word | Meaning |
|---|---|
| `const` | immutable binding — written once |
| `var` | mutable binding — reassignable |
| `let` | concise inferred immutable |

All three introduce a name with `←`. The word fixes whether the name may be
reassigned, not when the value exists.

## Absence and omission are different {#absence}

Faber keeps two ideas separate that many languages collapse into `T?` or
`Option<T>`:

- **Absence in a value** is a union: `int ∪ none`. The value domain includes
  the absence, and a function can return it.
- **Omission at a call site** is a post-name marker: `optional`. The slot may
  be left out; the type itself is unchanged.

Keeping them syntactic means a reader can tell *a value that may be missing*
from *an argument you need not pass* without reading the signature twice.

## Values do not convert by accident {#conversion}

A value has a type, and moving between types is written down. `∷` is a
compile-time ascription; `↦` is a runtime conversion that may fail. Numeric
families do not mix silently — the unbounded integer and a bounded cell meet at
an explicit `↦`, not at a hidden promotion. When a value can be absent or a
conversion can fail, the compiler makes you say so rather than guessing.

```faber
functio saturate(numerus x) → numerus {
    si x < 0 ergo redde 0
    si x > 255 ergo redde 255
    redde x
}

incipit {
    fixum numerus v ← saturate(300)
    fixum numerus ∪ nihil maybe ← nulla
    nota v
}
```

```text
$ faber run
255
```

`saturate` is declared before it is used, its parameter and return types are
written out, and `maybe`'s type is a union that includes `none`. The compiler
never infers a type that was genuinely left out; when information is missing it
reports the gap and stops. That is the rule that keeps the rest honest — if a
reader cannot tell what a symbol means from local source, the compiler does not
pretend it can.

[Types and values](/language/types.html) has the full inventory, including
collections, strings and numeric widths.
