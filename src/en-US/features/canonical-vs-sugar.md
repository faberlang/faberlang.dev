+++
title = "Canonical vs sugar surfaces"
section = "features"
order = 6
sources = []
+++

*Multiple parseable surfaces, one semantic shape.*

A recurring pattern in Faber's design: the language defines **one canonical
spelling** for each construct, but accepts multiple **sugar spellings**
that are semantically identical. The compiler does not prefer one over the
other — both parse to the same AST node. The formatter decides which spelling
to emit based on context and mode.

> **The rule:** Sugar spellings are semantically identical to long form.
> Multiple surfaces parse to the same `HirAnnotation` or type node.
> `faber format --canonical` prefers canonical spellings; author
> mode preserves the sugar the author wrote.

## Numeric type sugar {#numeric-type-sugar}

Numeric types have long-form canonical spellings and compact sugar forms.
The choice is per-module, not per-repository — a CLI package may use long
form everywhere, while a tensor kernel module uses sugar:

| Sugar | Canonical form | Domain |
|-------|----------------|--------|
| `f32`, `f64`, `i32`, `u64` | `fractus<f32>`, `numerus<i32>` | Width markers — scalar numeric types |
| `tf32`, `tf32[4]`, `ti64[2, 3]` | `tensor<f32, _>`, `tensor<f32, [4]>` | Dense tensor — `t` + width + optional shape |
| `sf32`, `sf32[2, 3]`, `si64[N]` | `sparsa<f32, _>`, `sparsa<f32, [2, 3]>` | Sparse tensor — `s` + width + optional shape |
| `mf32[4, 4]`, `mu32[3, 3]` | `matrix<f32, [4, 4]>` | Register-class matrix — `m` + width + shape |
| `lf32`, `lu32`, `li64` | `lista<f32>`, `lista<u32>` | List — `l` + width |
| `f16` | `fractus<f16>` | Half-float width marker (semantic/layout only) |

**General Faber (prefer long form):**

```faber
fixum lista<f32> values ← vacua
fixum tensor<f32, [2, 3]> grid ← vacua
fixum numerus<i32> narrow ← 7
```

**Numeric modules (prefer sugar):**

```faber
fixum lf32 values ← vacua
fixum tf32[2, 3] grid ← vacua
fixum i32 narrow ← 7
```

Sugar is **type-position only**. Value identifiers named `f32`,
`tf32`, or `mf32` are unchanged — the compiler only
interprets these as sugar when they appear in type positions. A file that
consistently uses sugar should say so once at the top:

```faber
# STYLE: numeric sugar (tf32, mf32, sf32, lf32, lu32)
```

## Annotation sugar {#annotation-sugar}

Faber annotations follow the same dual-surface model as numeric types.
Annotations are compiler-owned metadata attached to declarations — like
`@ optio` for CLI option definitions or `@ futura`
for async functions.

**Canonical form:** a braced record with explicit field names:

```text
@ optio {
    binding = verbose,
    brevis = "v",
    longum = "verbose",
    typus = bivalens,
    ubique = verum,
    descriptio = "Enable verbose output"
}
```

**Sugar form:** positional arguments and named aliases:

```text
@ optio verbose brevis "v" longum "verbose" typus bivalens ubique descriptio "Enable verbose output"
```

Both forms produce the same `HirAnnotation` record. The canonical
form is explicit and self-documenting; the sugar form is concise for
frequently-used annotations where the field order is well-known.
`faber format --canonical` prefers braced records; author mode
preserves the author's chosen form.

## Author vs canonical formatting {#author-vs-canonical-formatting}

The `faber format` command operates in two modes that mirror the
canonical-vs-sugar principle:

| Mode | Command | Input | Output |
|------|---------|-------|--------|
| Author | `faber format` | Parsed AST + leading trivia | Faber source preserving `#` comments, blank lines, and sugar spellings |
| Canonical | `faber format --canonical` | Analysed HIR + `TypeTable` | Normalised Faber — no comments, canonical spellings, no sugar |

Both modes run through the compiler's full front half (lex, parse, analyse
for canonical). Invalid source produces compiler diagnostics — the formatter
does not silently format broken input.

Key rules for both modes:

- Four-space indentation
- Stroustrup braces: opening `{` on the same line as the controlling header
- Author mode preserves the *presence* of blank lines but collapses runs of more than one
- Author mode does not insert blank lines the source did not contain
- Canonical mode normalises type spellings to long form, tensor sugar to canonical, annotations to braced records
- Canonical mode emits `T ∪ nihil` for nullable unions, `sponte` for optional parameters

## Design principle {#design-principle}

The canonical-vs-sugar pattern appears in multiple places because it is a
deliberate design principle, not a collection of one-off conveniences:

| Domain | Canonical | Sugar |
|--------|-----------|-------|
| Numeric types | `numerus<i32>` | `i32` |
| Tensor types | `tensor<f32, [4]>` | `tf32[4]` |
| Annotations | `@ optio { binding = verbose }` | `@ optio verbose ...` |
| Formatting | `faber format --canonical` | `faber format` (author mode) |
| Reader locale | Latin (`la`) | Any locale pack |

The pattern serves two goals. First, it lowers the barrier to entry — new
users can write `tf32[4]` without typing
`tensor<fractus<f32>, [4]>`. Second, it keeps the
canonical language unambiguous — when precision matters, the long form says
exactly what it means. The formatter bridges the two: authors write sugar,
reviewers can request canonical, and CI can enforce either.

## References {#references}

1. `radix/docs/design/numeric-type-sugar.md` — full sugar families, spelling preferences
2. `radix/docs/design/annotation-sugar.md` — dual-surface annotation model
3. `radix/docs/design/faber-canonical-surface.md` — author vs canonical format policy
4. `radix/EBNF.md` — grammar tables for sugar forms
