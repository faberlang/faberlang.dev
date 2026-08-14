+++
# This page discusses Latin keywords as Latin. Rendering them in
# the reader locale would turn its own examples into nonsense.
translate_spans = false
title = "Glyphs and Latin"
section = "language"
order = 5
sources = [
  "radix/README.md (Glyphs and Words)",
  "radix/corpus/operatores/",
  "radix/corpus/assignatio/",
  "faber/docs/EBNF.md",
]
+++

## Glyphs and operators

Faber uses glyphs where the symbol is structural. Below is the full inventory
of source glyphs recognised by the lexer.

### Value flow {#value-flow}

| Glyph | Meaning |
|-------|---------|
| `←` | Runtime binding, reassignment, and mutation |
| `=` | Compile-time assignment — values known while compiling |
| `→` | Function return type |
| `⇥` | Alternate exit — error-channel type or inline conversion recovery |
| `∴` | Clausura joint — connects closure body to signature (`(a, b) → T ∴ a + b`) |

### Type shape {#type-shape}

| Glyph | Meaning |
|-------|---------|
| `∷` | Static type ascription (compile-time cast) |
| `↦` | Runtime conversion (can-fail parse/coerce) |
| `∪` | Inline union type (`T ∪ nihil`) |

### Comparison {#comparison}

| Glyph | Meaning |
|-------|---------|
| `≡` `≠` | Exact equality and inequality |
| `<` `>` `≤` `≥` | Ordering |
| `≈` `≉` | Numeric value equality |

### Logical and bitwise {#logical-and-bitwise}

| Glyph | Meaning |
|-------|---------|
| `∧` `∨` `⊻` `¬` | And, or, xor, not |
| `⇐` `⇒` | Left and right bit shift |

### Assignment updates {#assignment-updates}

| Glyph | Meaning |
|-------|---------|
| `←` | Runtime assignment — the only assignment operator in expressions |
| `=` | Compile-time assignment — a value fixed and known while compiling |
| `⊕` `⊖` | Postfix increment/decrement statements (mutable numerus only) |

Both are assignment. They differ in **when** the value is decided.

`←` stores a value at execution time: bindings, reassignment, mutation. `=`
attaches a value the compiler already knows — field shape inside a literal,
declaration metadata, annotation fields. Most languages spell both with `=`
and leave the reader to infer which is meant; Faber splits them, so the glyph
itself tells you whether anything happens at runtime.

```faber
genus Punctum {
    numerus x
    numerus y
}

incipit {
    fixum _ p ← Punctum { x = 10, y = 20 }
    varia numerus count ← 0
    count ← count + 1
    nota p.x, count
}
```

`p ← …` runs. `x = 10` does not — it is the shape of the value being built,
settled before the program starts.

Worked through in full under
[The binding convention matters](#the-binding-convention-matters).

### Optional chaining and non-null assertion {#optional-chaining-and-non-null-assertion}

| Glyph | Meaning |
|-------|---------|
| `?` `?.` `?[` `?(` | Optional chaining |
| `!` `!.` `![` `!(` | Non-null assertion |

### Ranges {#ranges}

| Glyph | Meaning |
|-------|---------|
| `‥` | Exclusive range endpoint |
| `…` | Inclusive range endpoint |

### Literal delimiters {#literal-delimiters}

| Glyph | Type | Role |
|-------|------|------|
| `'` | `ascii` | Fixed machine tokens |
| `"` | `textus` | Line string |
| `«` `»` | `textus` | Block string (guillemets) |
| `` ` `` | `forma` | Captured template |
| `|` | `octeti` | Hex literal |
| `§` | template hole | Placeholder inside `"…"`, `«…»`, `` `…` `` |

### Punctuation {#punctuation}

| Glyph | Role |
|-------|------|
| `(` `)` | Grouping and call |
| `{` `}` | Block, genus literal, or JSON document |
| `[` `]` | List literal and indexing |
| `.` | Member access |
| `,` | Separator |
| `;` | Statement separator |
| `:` | JSON field separator |
| `=` | Structural field shape (not runtime assignment) |
| `@` | Annotation marker |
| `#` | Line comment |

## Latin vocabulary and structural glyphs

*Three signal choices that make Faber source recognisable at a glance.*

Faber makes three deliberate signal choices that work together to produce source
with stable grammatical shape. A reader can see the semantic role of every
construct before knowing which target backend the code will be compiled to.

### The three signals {#three}

| Signal | Examples | Role |
|--------|----------|------|
| Type-first declarations | `textus nomen`, `numerus aetas` | Shape reads toward binding — type, then name. |
| Latin behavioural words | `functio`, `genus`, `si`, `redde`, `fixum` | Declarations, statements, lifecycle, and behavioural intent. |
| Structural glyphs | `← → ∴ ≡ ∪ ⇥` | Value flow, type flow, and structural joints — universal, never localise. |

These three are designed to be mutually reinforcing. A reader who knows Faber in
one locale can read it in any locale because the glyphs and structure never change.
A reader who knows the Rust backend can still recognise the Faber source because
the Latin keywords and type-first order produce a distinct visual register.

### Type-first declarations {#type-first}

Faber puts the type before the name in every declaration. This is the opposite of
mainstream C-family syntax, and it is deliberate:

| Construct | C-family habit | Faber |
|-----------|----------------|-------|
| Variable | `int count = 0` | `numerus count ← 0` |
| Function | `fn greet(name: String) → String` | `functio salve(textus nomen) → textus` |
| Parameter | `(String name)` | `(textus nomen)` |

Type-first declarations mean the shape of data is the first thing the reader sees.
This aligns naturally with languages that read left-to-right for semantic breadth
— Chinese, Hindi, and Arabic declarations follow the same order.

```faber
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

### Latin behavioural vocabulary {#latin}

Faber uses Latin words for every construct that has behavioural or grammatical
shape. The vocabulary is small and regular, drawn from a single classical source
rather than the mixed etymologies of most programming languages.

#### Declarations {#declarations}

| Keyword | Role | Approximate equivalent |
|---------|------|------------------------|
| `functio` | Declares a named function or method | `fn`, `def`, `function` |
| `genus` | Declares a concrete type with fields | `class`, `struct` |
| `implendum` | Declares a behavioural contract | `interface`, `trait` |
| `typus` | Declares a type alias | `typedef`, `type` |
| `discretio` | Declares a tagged union | `enum`, `sum type` |

#### Bindings and transfer {#bindings-and-transfer}

| Keyword | Role | Approximate equivalent |
|---------|------|------------------------|
| `fixum` | Immutable binding (write-once) | `let`, `const` |
| `varia` | Mutable binding | `let mut`, `var` |
| `sit` | Concise inferred immutable | `let` (inferred) |
| `redde` | Return a value from a function | `return` |
| `iace` | Throw on the error channel | `throw`, `raise` |
| `mori` | Deferred — behaviour not yet expressible | `unimplemented!`, `todo` |

#### Control flow {#control-flow}

| Keyword | Role | Approximate equivalent |
|---------|------|------------------------|
| `si` | Conditional branch | `if` |
| `sin` | Else-if branch | `else if` |
| `secus` | Else branch | `else` |
| `dum` | While loop | `while` |
| `itera` | Iteration (values, keys, or range) | `for` |
| `elige` | Pattern-match (first arm wins) | `match`, `switch` |
| `fac` | Try block with error recovery | `try`, `do` |
| `cape` | Error handler for fac | `catch` |

> The Latin vocabulary is **bindable** — it ships with the canonical pack but can be remapped through reader locale. A Thai programmer sees `ถ้า` instead of `si`; a Chinese programmer sees `函数` instead of `functio`. The vocabulary is not privileged; only the grammar is.

Keywords are **contextual**: since Radix v0.79.0 there is no global reserved
keyword table. The lexer emits identifiers for all words and the parser
recognizes a keyword by spelling in its grammar position. A word is only a
keyword in the slot where it is expected; everywhere else it is an ordinary
identifier — you can name a variable `si`, a function `functio`, or a
parameter `vel`. A small residual set (`cape`, `custodi`, `itera`, `sic`,
`iace`, `mori`, `adfirma`, `cede`, `incipit`, `incipiet`, `importa`, `ex`)
is still globally reserved.

### Structural glyphs {#glyphs}

Where behavioural vocabulary uses Latin words, structural meaning uses universal
glyphs. These never localise and never change their meaning across renderings.
They are the visual anchor that makes Faber source recognisable regardless of
which human language the keywords are rendered in.

#### Value flow {#value-flow}

| Glyph | Meaning |
|-------|---------|
| `←` | Runtime binding, reassignment, and mutation — the only assignment operator |
| `→` | Function return type declaration |
| `⇥` | Alternate exit: error-channel type or inline conversion recovery |
| `∴` | Clausura joint — connects a closure body to its signature |

#### Type shape {#type-shape}

| Glyph | Meaning |
|-------|---------|
| `∷` | Static type ascription — compile-time assertion about a value's type |
| `↦` | Runtime conversion — parsing or coercion that may fail |
| `∪` | Inline union type — connects two types (as in `T ∪ nihil`) |

#### Comparison and logic {#comparison-and-logic}

| Glyph | Meaning |
|-------|---------|
| `≡` `≠` | Exact equality and inequality — strict type match required |
| `<` `>` `≤` `≥` | Ordering comparisons |
| `∧` `∨` `⊻` `¬` | Logical and bitwise: and, or, xor, not |

#### The binding convention matters {#the-binding-convention-matters}

One glyph choice deserves special attention because it is the most common
point of confusion for new readers:

| Glyph | Role | Use for |
|-------|------|---------|
| `←` | **Runtime flow** | Initial binding, reassignment, and mutation at execution time |
| `=` | **Structural shape** | Field names inside literals and declaration metadata — not runtime stores |

Most languages overload `=` for both "define this field in a type"
and "put a runtime value in this variable." Faber splits those jobs. Every
`←` is live data flow; every `=` inside `Type { … }`
is genus field layout.

```text
# Runtime binding: ← attaches a value to a name
fixum numerus count ← 0
varia textus label ← "ready"
count ← count + 1

# Structural shape: = defines field values inside a literal
fixum _ p ← Point {
    x = 10,
    y = 20
}
```

### Compared to mainstream languages {#compare}

The table below shows how common programming language patterns map to Faber's
three-signal system. The Faber column uses a different glyph or keyword for
each distinct semantic job — no overloading.

| Semantic job | Common in other languages | Faber |
|--------------|---------------------------|-------|
| Parameter type declaration | `name: String` | `textus nomen` |
| Return type | `→ String`, `: String` | `→` `textus` |
| Runtime assignment | `x = value` | `←` |
| Equality test | `==` | `≡` |
| Nullability | `T?`, `Option<T>` | `T ∪ nihil` |
| Branch + one statement | `if (cond) return x` | `si cond ergo redde x` |
| Type cast | `(T)value`, `value as T` | `value ∷ T` |
| Conversion (may fail) | `try_into()` | `value ↦ T` |

### References {#references}

1. EBNF grammar — full glyph and keyword inventory
2. radix/corpus/ — language corpus with 304 exemplar files across all keywords
3. radix/corpus/operatores/ — operator and glyph exemplars
4. Commandments — the nine design laws that preserve these signals

## Canonical vs sugar surfaces

*Multiple parseable surfaces, one semantic shape.*

A recurring pattern in Faber's design: the language defines **one canonical spelling** for each construct, but accepts multiple **sugar spellings**
that are semantically identical. The compiler does not prefer one over the
other — both parse to the same AST node. The formatter decides which spelling
to emit based on context and mode.

> **The rule:** Sugar spellings are semantically identical to long form.
> Multiple surfaces parse to the same `HirAnnotation` or type node.
> `faber format --locale la` re-emits canonical spellings; author
> mode preserves the sugar the author wrote.

### Numeric type sugar {#numeric-type-sugar}

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

### Annotation sugar {#annotation-sugar}

Faber annotations follow the same dual-surface model as numeric types.
Annotations are compiler-owned metadata attached to declarations — like
`@ optio` for CLI option definitions or `@ futura` for async functions
(legacy — prefer the `fiet` posture word in the signature slot).

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
`faber format --locale la` re-emits canonical braced records; author mode
preserves the author's chosen form.

### Author vs canonical formatting {#author-vs-canonical-formatting}

The `faber format` command operates in two modes that mirror the
canonical-vs-sugar principle:

| Mode | Command | Input | Output |
|------|---------|-------|--------|
| Author | `faber format` | Parsed AST + leading trivia | Faber source preserving `#` comments, blank lines, and sugar spellings |
| Canonical | `faber format --locale la` | Analysed HIR + `TypeTable` | Normalised Faber — no comments, canonical spellings, no sugar |

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

### Design principle {#design-principle}

The canonical-vs-sugar pattern appears in multiple places because it is a
deliberate design principle, not a collection of one-off conveniences:

| Domain | Canonical | Sugar |
|--------|-----------|-------|
| Numeric types | `numerus<i32>` | `i32` |
| Tensor types | `tensor<f32, [4]>` | `tf32[4]` |
| Annotations | `@ optio { binding = verbose }` | `@ optio verbose ...` |
| Formatting | `faber format --locale la` | `faber format` (author mode) |
| Reader locale | Latin (`la`) | Any locale pack |

The pattern serves two goals. First, it lowers the barrier to entry — new
users can write `tf32[4]` without typing
`tensor<fractus<f32>, [4]>`. Second, it keeps the
canonical language unambiguous — when precision matters, the long form says
exactly what it means. The formatter bridges the two: authors write sugar,
reviewers can request canonical, and CI can enforce either.

### References {#references}

1. `radix/docs/design/numeric-type-sugar.md` — full sugar families, spelling preferences
2. `radix/docs/design/annotation-sugar.md` — dual-surface annotation model
3. `radix/docs/design/faber-canonical-surface.md` — author vs canonical format policy
4. `faber/docs/EBNF.md` — grammar tables for sugar forms
