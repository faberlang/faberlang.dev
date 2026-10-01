+++
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
| `⇥` | Alternate exit — error-channel type |
| `⊥` | Default — inline value used when a conversion fails (`↦ int ⊥ 0`) |
| `∴` | Lambda joint — connects closure body to signature (`(a, b) → T ∴ a + b`) |

### Type shape {#type-shape}

| Glyph | Meaning |
|-------|---------|
| `∷` | Static type ascription (compile-time cast) |
| `↦` | Runtime conversion (can-fail parse/coerce) |
| `∪` | Inline union type (`T ∪ none`) |

### Comparison {#comparison}

| Glyph | Meaning |
|-------|---------|
| `≡` `≠` | Exact equality and inequality |
| `≅` `≇` | Promoted exact equality — same value, compatible numeric types |
| `<` `>` `≤` `≥` | Ordering |
| `≈` `≉` | Fuzzy equality — tolerance match with `isclose` defaults |

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
| `⊕` `⊖` | Postfix increment/decrement statements (mutable int only) |

Both are assignment. They differ in **when** the value is decided.

`←` stores a value at execution time: bindings, reassignment, mutation. `=`
attaches a value the compiler already knows — field shape inside a literal,
declaration metadata, annotation fields. Most languages spell both with `=`
and leave the reader to infer which is meant; Faber splits them, so the glyph
itself tells you whether anything happens at runtime.

```faber
genus Punctum {
    fixum numerus x
    fixum numerus y
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
| `"` | `string` | Line string |
| `«` `»` | `string` | Block string (guillemets) |
| `` ` `` | `forma` | Captured template |
| `|` | `bytes` | Hex literal |
| `§` | template hole | Placeholder inside `"…"`, `«…»`, `` `…` `` |

### Punctuation {#punctuation}

| Glyph | Role |
|-------|------|
| `(` `)` | Grouping and call |
| `{` `}` | Block, class literal, or JSON document |
| `[` `]` | List literal and indexing |
| `.` | Member access |
| `,` | Separator |
| `;` | Statement separator |
| `:` | JSON field separator |
| `=` | Structural field shape (not runtime assignment) |
| `@` | Annotation marker |
| `#` | Line comment |

## Vocabulary and structural glyphs

*Three signal choices that make Faber source recognisable at a glance.*

Faber makes three deliberate signal choices that work together to produce source
with stable grammatical shape. A reader can see the semantic role of every
construct before knowing which target backend the code will be compiled to.

### The three signals {#three}

| Signal | Examples | Role |
|--------|----------|------|
| Type-first declarations | `string name`, `int age` | Shape reads toward binding — type, then name. |
| Behavioural words | `fn`, `class`, `if`, `return`, `const` | Declarations, statements, lifecycle, and behavioural intent. |
| Structural glyphs | `← → ∴ ≡ ∪ ⇥` | Value flow, type flow, and structural joints — universal, never localise. |

These three are designed to be mutually reinforcing. A reader who knows Faber in
one locale can read it in any locale because the glyphs and structure never change.
A reader who knows the Rust backend can still recognise the Faber source because
the keyword vocabulary and type-first order produce a distinct visual register.

### Type-first declarations {#type-first}

Faber puts the type before the name in every declaration. This is the opposite of
mainstream C-family syntax, and it is deliberate:

| Construct | C-family habit | Faber |
|-----------|----------------|-------|
| Variable | `int count = 0` | `int count ← 0` |
| Function | `fn greet(name: String) → String` | `fn salve(string nomen) → string` |
| Parameter | `(String name)` | `(string nomen)` |

Type-first declarations mean the shape of data is the first thing the reader sees.
This aligns naturally with languages that read left-to-right for semantic breadth
— Chinese, Hindi, and Arabic declarations follow the same order.

```faber
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nulla
    redde a / b
}
```

### The behavioural vocabulary {#latin}

Faber gives every construct that has behavioural or grammatical shape a word.
The English reader surface is what the tables below show; the compiler's
canonical corpus keeps the same vocabulary under Latin spellings, which
`faber convert --to la` prints — a small, regular set drawn from a single
classical source rather than the mixed etymologies of most programming
languages.

#### Declarations {#declarations}

| Keyword | Role | Approximate equivalent |
|---------|------|------------------------|
| `fn` | Declares a named function or method | `def`, `function` |
| `class` | Declares a concrete type with fields | `class`, `struct` |
| `interface` | Declares a behavioural contract | `interface`, `trait` |
| `type` | Declares a type alias | `typedef`, `type` |
| `union` | Declares a tagged union | `enum`, `sum type` |

#### Bindings and transfer {#bindings-and-transfer}

| Keyword | Role | Approximate equivalent |
|---------|------|------------------------|
| `const` | Immutable binding (write-once) | `const`, `final` |
| `var` | Mutable binding | `let mut`, `var` |
| `let` | Concise inferred immutable | `val`, `auto` |
| `return` | Return a value from a function | `return` |
| `throw` | Throw on the error channel | `throw`, `raise` |
| `panic` | Deferred — behaviour not yet expressible | `unimplemented!`, `todo` |

#### Control flow {#control-flow}

| Keyword | Role | Approximate equivalent |
|---------|------|------------------------|
| `if` | Conditional branch | `if` |
| `elif` | Else-if branch | `else if` |
| `else` | Else branch | `else` |
| `while` | While loop | `while` |
| `for` | Iteration (values, keys, or range) | `for` |
| `switch` | Pattern-match (first arm wins) | `match`, `switch` |
| `do` | Try block with error recovery | `try`, `do` |
| `catch` | Error handler for do | `catch` |

> The vocabulary is **bindable** — it ships with the canonical pack but can be remapped through reader locale. A Thai programmer sees `ถ้า` for `if`; a Chinese programmer sees `函数` for `fn`. The vocabulary is not privileged; only the grammar is.

Keywords are **contextual**: since Radix v0.79.0 there is no global reserved
keyword table. The lexer emits identifiers for all words and the parser
recognizes a keyword by spelling in its grammar position. A word is only a
keyword in the slot where it is expected; everywhere else it is an ordinary
identifier — you can name a variable `if`, a function `fn`, or a
parameter `coalesce`. A small residual set (`catch`, `guard`, `for`, `yields`,
`throw`, `panic`, `assert`, `yield`, `main`, `async_main`, `import`, `from`)
is still globally reserved.

### Structural glyphs {#glyphs}

Where behavioural vocabulary uses your reader locale's words, structural meaning uses universal
glyphs. These never localise and never change their meaning across renderings.
They are the visual anchor that makes Faber source recognisable regardless of
which human language the keywords are rendered in.

#### Value flow {#value-flow}

| Glyph | Meaning |
|-------|---------|
| `←` | Runtime binding, reassignment, and mutation — the only assignment operator |
| `→` | Function return type declaration |
| `⇥` | Alternate exit: error-channel type |
| `⊥` | Default: inline value used when a conversion fails |
| `∴` | Lambda joint — connects a closure body to its signature |

#### Type shape {#type-shape}

| Glyph | Meaning |
|-------|---------|
| `∷` | Static type ascription — compile-time assertion about a value's type |
| `↦` | Runtime conversion — parsing or coercion that may fail |
| `∪` | Inline union type — connects two types (as in `T ∪ none`) |

#### Comparison and logic {#comparison-and-logic}

| Glyph | Meaning |
|-------|---------|
| `≡` `≠` `≢` | Exact equality and inequality — strict type match required |
| `≅` `≇` | Promoted exact equality — numeric widths join, then exact compare |
| `≈` `≉` | Fuzzy equality — tolerance match with `isclose` defaults |
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
is class field layout.

```faber
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
| Parameter type declaration | `name: String` | `string name` |
| Return type | `→ String`, `: String` | `→` `string` |
| Runtime assignment | `x = value` | `←` |
| Equality test | `==` | `≡` |
| Nullability | `T?`, `Option<T>` | `T ∪ none` |
| Branch + one statement | `if (cond) return x` | `if cond then return x` |
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

Sized numeric types have one canonical spelling: the bare width marker
(`i8` … `u64`, `d64`, `inf`, `f16`, `f32`, `f64`). The wrapped forms
`numerus<i32>` / `fractus<f32>` (en `int<i32>` / `float<f32>`) are the retired
spelling — the parser still reads them for now, but the formatter and the
diagnostics print the bare marker. The compact sugar families below build on
the markers. The choice between a container's long form and its sugar is
per-module, not per-repository — a CLI package may use long form everywhere,
while a tensor kernel module uses sugar:

| Sugar | Canonical form | Domain |
|-------|----------------|--------|
| `tf32`, `tf32[4]`, `ti64[2, 3]` | `tensor<f32, _>`, `tensor<f32, [4]>` | Dense tensor — `t` + width + optional shape |
| `sf32`, `sf32[2, 3]`, `si64[N]` | `sparsa<f32, _>`, `sparsa<f32, [2, 3]>` | Sparse tensor — `s` + width + optional shape |
| `mf32[4, 4]`, `mu32[3, 3]` | `matrix<f32, [4, 4]>` | Register-class matrix — `m` + width + shape |
| `lf32`, `lu32`, `li64` | `list<f32>`, `list<u32>` | List — `l` + width |

**General Faber (prefer long form):**

```faber
incipit {
    fixum lista<f32> values ← vacua
    fixum tensor<f32, [2, 3]> grid ← vacua
    fixum i32 narrow ← 7
}
```

**Numeric modules (prefer sugar):**

```faber
incipit {
    fixum lf32 values ← vacua
    fixum tf32[2, 3] grid ← vacua
    fixum i32 narrow ← 7
}
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
`@ option` for CLI option definitions or `@ future` for async functions
(legacy — prefer the `async` posture word in the signature slot).

**Canonical form:** a braced record with explicit field names:

```faber
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

```faber
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
- Canonical mode normalises container sugar to long form (`tf32[4]` → `tensor<f32, [4]>`) and annotations to braced records; width markers such as `i32` are already canonical
- Canonical mode emits `T ∪ none` for nullable unions, `optional` for optional parameters

### Design principle {#design-principle}

The canonical-vs-sugar pattern appears in multiple places because it is a
deliberate design principle, not a collection of one-off conveniences:

| Domain | Canonical | Sugar |
|--------|-----------|-------|
| Tensor types | `tensor<f32, [4]>` | `tf32[4]` |
| Annotations | `@ option { binding = verbose }` | `@ option verbose ...` |
| Formatting | `faber format --locale la` | `faber format` (author mode) |
| Reader locale | Latin (`la`) | Any locale pack |

The pattern serves two goals. First, it lowers the barrier to entry — new
users can write `tf32[4]` without typing
`tensor<f32, [4]>`. Second, it keeps the
canonical language unambiguous — when precision matters, the long form says
exactly what it means. The formatter bridges the two: authors write sugar,
reviewers can request canonical, and CI can enforce either.

### References {#references}

1. `radix/docs/design/numeric-type-sugar.md` — full sugar families, spelling preferences
2. `radix/docs/design/annotation-sugar.md` — dual-surface annotation model
3. `radix/docs/design/faber-canonical-surface.md` — author vs canonical format policy
4. `faber/docs/EBNF.md` — grammar tables for sugar forms
