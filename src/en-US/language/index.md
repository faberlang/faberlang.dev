+++
title = "The Faber language"
section = "language"
order = 0
sources = []
+++

Everything you need to read Faber is on this page. The pages beneath it go
deeper on each part, but nothing here is a placeholder — if you read this far
and stop, you can read a Faber program.

## A whole program {#whole-program}

```faber
functio saturate(numerus x) → numerus {
    si x < 0 ergo redde 0
    si x > 255 ergo redde 255
    redde x
}

incipit {
    fixum numerus v ← saturate(300)
    nota v
}
```

That is a complete, compilable package entry point. Reading it left to right:

| Piece | What it is |
|---|---|
| `fn` | declares a function |
| `int x` | **the type comes before the name** — always, everywhere |
| `→ int` | the return type |
| `if … then` | a compact single-branch conditional |
| `return` | return |
| `main` | the program entry point |
| `const` | an immutable binding (`var` is the mutable one) |
| `←` | bind this value to that name |
| `print` | print |

## Type before name, always {#type-first}

This is the single rule that makes the rest of the grammar small:

```faber
incipit {
    # a declaration
    fixum numerus count ← 0
    # another
    fixum textus name ← "Marcus"
    # a generic
    fixum lista<numerus> scores ← [1, 2, 3]
    # a nullable
    fixum numerus ∪ nihil maybe ← nulla
    nota count, name, scores, maybe
}
```

There is no `name: type` form to learn. A declaration is a type followed by a
name, whether it is a parameter, a local, or a field. Bindings come in three
words: `const` is write-once, `var` is freely reassignable, and `let` is the
concise inferred immutable. See [Types and values](/language/types.html).

## Six glyphs, and what they mean {#glyphs}

Faber uses a small fixed set of symbols for structure. They never localize —
they are the same in every reader locale, which is what keeps a program
recognizable across languages.

| Glyph | Meaning |
|---|---|
| `←` | bind a value to a name |
| `→` | function return type |
| `∪` | union type, most often `T ∪ nihil` for nullable |
| `⇥` | alternate exit — the error channel |
| `∴` | closure joint, connecting a signature to its body |
| `≡` | equality |

Two more appear when you convert between types: `∷` for a compile-time
ascription and `↦` for a runtime conversion that can fail. Full table in
[Glyphs and Latin](/language/glyphs.html).

## The words you write, and the compiler's Latin {#latin}

The words in the program above — `fn`, `if`, `return`, `const`, `int` — are
the spellings an English reader writes; every page on this site teaches the
English reader surface. Latin is the compiler's canonical form: the identity
key programs are stored and exchanged under. `faber convert --to la` prints
any program in that canonical spelling, and
[reader locales](/language/reader-locales.html) render the same program in
seven other languages. The glyphs and the type-first shape survive every
rendering untouched — and identifiers like `saturate` are never translated.

## Where the rest lives {#deeper}

| Page | What it covers |
|---|---|
| [Types and values](/language/types.html) | primitives, collections, strings, nullability, conversion, bindings |
| [Functions and control flow](/language/functions.html) | parameters, returns, branching, loops, generics |
| [Errors and testing](/language/errors.html) | the `⇥` error channel, and inline `describe`/`test`/`assert` suites |
| [Glyphs and Latin](/language/glyphs.html) | the full glyph table, vocabulary rationale, canonical vs sugar |
| [Reader locales](/language/reader-locales.html) | how one program renders in eight surfaces |
| [Capabilities and frames](/language/capabilities.html) | `call` dispatch and the host I/O boundary |
