+++
title = "Cheat sheet"
section = "cheatsheet"
order = 3
sources = []
+++

Short examples of how Faber is actually written. Every snippet on these pages
compiles — they are checked against the compiler on each build, not typed from
memory.

This is not the [corpus](/corpus/). The corpus is the exhaustive reference: one
page per keyword, every construct registered and measured. The cheat sheet is
the opposite shape — a handful of pages, each showing the two or three ways
people really write something.

## The feel of the language {#feel}

Three signals do most of the work. Types come before names, behaviour words are
Latin, and structure is carried by glyphs rather than punctuation soup.

```faber
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

`numerus a` — type first, then the name. `→` introduces the return type. `∪`
joins types into a union, so this returns a number *or* nothing. `≡` is
equality. `redde` returns.

A whole program, doing real work:

```faber
incipit {
    fixum lista<f32> valores ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    fixum tensor<f32, []> seed ← vacua
    fixum tensor<f32, [2, 3]> matrix ← seed.strue(valores, [2, 3])
    fixum f32 medium ← matrix.media()
    nota medium
}
```

`incipit` is the entry point. `fixum` binds a constant. `←` is the bind glyph —
assignment reads right-to-left into the name. `nota` prints.

## By topic {#topics}

| Page | What it covers |
|---|---|
| [Entry points](/cheatsheet/entry-points.html) | `incipit`, async entry, CLI arguments and annotations |
| [Bindings](/cheatsheet/bindings.html) | `fixum` vs `varia`, type holes, union holes |
| [Types and widths](/cheatsheet/types.html) | Numbers and their widths, lists, tables, tensors, vectors, and the sugar for each |
| [Generics](/cheatsheet/generics.html) | Generic functions, generic containers, `genus` |
| [Loops](/cheatsheet/loops.html) | `itera` over values, keys, and ranges; `dum` |
| [Control flow](/cheatsheet/control-flow.html) | `si` / `sin` / `secus`, `elige`, `discerne` over unions |
| [Errors and catching](/cheatsheet/errors.html) | The `⇥` error channel, `iace`, and `cape` on many block forms |
| [Conversions](/cheatsheet/conversions.html) | `↦` conversion, recovery with `⇥`, conversion vs casting |
| [Imports](/cheatsheet/imports.html) | Standard library, local files, aliasing, `publica` vs `privata` |
| [Reader locales](/cheatsheet/locales.html) | The same program in eight human languages, side by side |
| [Testing](/cheatsheet/testing.html) | `probandum`, `proba`, `adfirma`, tags, running tests |
| [Commands](/cheatsheet/commands.html) | The daily `faber` CLI loop |

## Keywords you will meet first {#keywords}

The twenty that carry most Faber source. Each links to the page that shows it
in use; the corpus has the exhaustive entry for every one.

| Keyword | Means | Shown on |
|---|---|---|
| `incipit` | Program entry point | [Entry points](/cheatsheet/entry-points.html) |
| `incipiet` | Async program entry point | [Entry points](/cheatsheet/entry-points.html) |
| `functio` | Declare a function | [Generics](/cheatsheet/generics.html) |
| `redde` | Return a value | [Control flow](/cheatsheet/control-flow.html) |
| `fixum` | Bind a constant | [Bindings](/cheatsheet/bindings.html) |
| `varia` | Bind a mutable variable | [Bindings](/cheatsheet/bindings.html) |
| `genus` | Declare a record type | [Generics](/cheatsheet/generics.html) |
| `typus` | Name an alias for a type | [Types and widths](/cheatsheet/types.html) |
| `si` | If | [Control flow](/cheatsheet/control-flow.html) |
| `sin` | Else-if | [Control flow](/cheatsheet/control-flow.html) |
| `secus` | Else | [Control flow](/cheatsheet/control-flow.html) |
| `elige` | Select over a value | [Control flow](/cheatsheet/control-flow.html) |
| `discerne` | Match over a union | [Control flow](/cheatsheet/control-flow.html) |
| `casu` | A case arm | [Control flow](/cheatsheet/control-flow.html) |
| `itera` | Iterate | [Loops](/cheatsheet/loops.html) |
| `dum` | While | [Loops](/cheatsheet/loops.html) |
| `iace` | Send a value down the error channel | [Errors and catching](/cheatsheet/errors.html) |
| `cape` | Catch from the error channel | [Errors and catching](/cheatsheet/errors.html) |
| `importa` | Import a module or item | [Imports](/cheatsheet/imports.html) |
| `proba` | Declare a test | [Testing](/cheatsheet/testing.html) |

## Glyphs {#glyphs}

| Glyph | Reads as |
|---|---|
| `←` | bind — put the value on the right into the name on the left |
| `→` | returns this type |
| `⇥` | …and may fail with this error type |
| `≡` | equals |
| `∪` | union of types |
| `↦` | convert to this type |
| `∴` | closure joint |
| `‥` | range, as in `0‥10` |

Full discussion: [Glyphs and Latin](/language/glyphs.html).
