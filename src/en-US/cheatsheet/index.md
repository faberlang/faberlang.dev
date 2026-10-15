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

Three signals do most of the work. Types come before names, keywords are plain
words in the reader's own language (English here; Latin is one of eight reader
locales), and structure is carried by glyphs rather than punctuation soup.

```faber locale-tabs
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nulla
    redde a / b
}
```

`int a` — type first, then the name. `→` introduces the return type. `∪`
joins types into a union, so this returns a number *or* nothing. `≡` is
equality. `return` returns.

A whole program, doing real work:

```faber locale-tabs
incipit {
    sit lista<f32> valores ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    sit tensor<f32, [2, 3]> matrix ← valores ↦ tensor<f32, [2, 3]>
    sit f32 medium ← matrix.media()
    nota medium
}
```

`main` is the entry point. `let` binds a name once. `←` is the bind glyph —
assignment reads right-to-left into the name. `print` prints.

## By topic {#topics}

| Page | What it covers |
|---|---|
| [Entry points](/cheatsheet/entry-points.html) | `main`, async entry, CLI arguments and annotations |
| [Bindings](/cheatsheet/bindings.html) | `let`, `mut` and `ref`, type holes, union holes |
| [Types and widths](/cheatsheet/types.html) | Numbers and their widths, lists, tables, tensors, vectors, and the sugar for each |
| [Generics](/cheatsheet/generics.html) | Generic functions, generic containers, `class` |
| [Loops](/cheatsheet/loops.html) | `for` over values, keys, and ranges; `while` |
| [Control flow](/cheatsheet/control-flow.html) | `if` / `elif` / `else`, `switch`, `match` over unions |
| [Errors and catching](/cheatsheet/errors.html) | The `⇥` error channel, `throw`, and `catch` on many block forms |
| [Conversions](/cheatsheet/conversions.html) | `↦` conversion, recovery with `⊥`, conversion vs casting |
| [Imports](/cheatsheet/imports.html) | Standard library, local files, aliasing, and `public` re-exports |
| [Reader locales](/localization.html) | The same program in eight human languages, side by side |
| [Testing](/cheatsheet/testing.html) | `describe`, `test`, `assert`, tags, running tests |
| [Commands](/cheatsheet/commands.html) | The daily `faber` CLI loop |

## Keywords you will meet first {#keywords}

The twenty that carry most Faber source. Each links to the page that shows it
in use; the corpus has the exhaustive entry for every one.

| Keyword | Means | Shown on |
|---|---|---|
| `main` | Program entry point | [Entry points](/cheatsheet/entry-points.html) |
| `async_main` | Async program entry point | [Entry points](/cheatsheet/entry-points.html) |
| `fn` | Declare a function | [Generics](/cheatsheet/generics.html) |
| `return` | Return a value | [Control flow](/cheatsheet/control-flow.html) |
| `let` | Bind a name once | [Bindings](/cheatsheet/bindings.html) |
| `mut` | Bind a writable name | [Bindings](/cheatsheet/bindings.html) |
| `class` | Declare a record type | [Generics](/cheatsheet/generics.html) |
| `type` | Name an alias for a type | [Types and widths](/cheatsheet/types.html) |
| `if` | If | [Control flow](/cheatsheet/control-flow.html) |
| `elif` | Else-if | [Control flow](/cheatsheet/control-flow.html) |
| `else` | Else | [Control flow](/cheatsheet/control-flow.html) |
| `switch` | Select over a value | [Control flow](/cheatsheet/control-flow.html) |
| `match` | Match over a union | [Control flow](/cheatsheet/control-flow.html) |
| `case` | A case arm | [Control flow](/cheatsheet/control-flow.html) |
| `for` | Iterate | [Loops](/cheatsheet/loops.html) |
| `while` | While | [Loops](/cheatsheet/loops.html) |
| `throw` | Send a value down the error channel | [Errors and catching](/cheatsheet/errors.html) |
| `catch` | Catch from the error channel | [Errors and catching](/cheatsheet/errors.html) |
| `import` | Import a module or item | [Imports](/cheatsheet/imports.html) |
| `test` | Declare a test | [Testing](/cheatsheet/testing.html) |

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

Full discussion: [Glyphs and keywords](/language/glyphs.html).
