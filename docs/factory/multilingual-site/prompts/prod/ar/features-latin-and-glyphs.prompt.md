You are a professional technical translator for the Faber documentation site.

# Contract — Arabic (ar). Natural technical Arabic; preserve RTL prose quality.

Rules:
- Target locale: `ar`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Arabic reader-locale Faber using Arabic keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged and keep source in logical order.

## English source body

*Three signal choices that make Faber source recognisable at a glance.*

Faber makes three deliberate signal choices that work together to produce source
with stable grammatical shape. A reader can see the semantic role of every
construct before knowing which target backend the code will be compiled to.

## The three signals {#three}

| Signal | Examples | Role |
|--------|----------|------|
| Type-first declarations | `textus nomen`, `numerus aetas` | Shape reads toward binding — type, then name. |
| Latin behavioural words | `functio`, `genus`, `si`, `redde`, `fixum` | Declarations, statements, lifecycle, and behavioural intent. |
| Structural glyphs | `← → ∴ ≡ ∪ ⇥` | Value flow, type flow, and structural joints — universal, never localise. |

These three are designed to be mutually reinforcing. A reader who knows Faber in
one locale can read it in any locale because the glyphs and structure never change.
A reader who knows the Rust backend can still recognise the Faber source because
the Latin keywords and type-first order produce a distinct visual register.

## Type-first declarations {#type-first}

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

<<<FENCE 0>>>

## Latin behavioural vocabulary {#latin}

Faber uses Latin words for every construct that has behavioural or grammatical
shape. The vocabulary is small and regular, drawn from a single classical source
rather than the mixed etymologies of most programming languages.

### Declarations {#declarations}

| Keyword | Role | Approximate equivalent |
|---------|------|------------------------|
| `functio` | Declares a named function or method | `fn`, `def`, `function` |
| `genus` | Declares a concrete type with fields | `class`, `struct` |
| `implendum` | Declares a behavioural contract | `interface`, `trait` |
| `typus` | Declares a type alias | `typedef`, `type` |
| `discretio` | Declares a tagged union | `enum`, `sum type` |

### Bindings and transfer {#bindings-and-transfer}

| Keyword | Role | Approximate equivalent |
|---------|------|------------------------|
| `fixum` | Immutable binding (write-once) | `let`, `const` |
| `varia` | Mutable binding | `let mut`, `var` |
| `sit` | Concise inferred immutable | `let` (inferred) |
| `redde` | Return a value from a function | `return` |
| `iace` | Throw on the error channel | `throw`, `raise` |
| `mori` | Deferred — behaviour not yet expressible | `unimplemented!`, `todo` |

### Control flow {#control-flow}

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

## Structural glyphs {#glyphs}

Where behavioural vocabulary uses Latin words, structural meaning uses universal
glyphs. These never localise and never change their meaning across renderings.
They are the visual anchor that makes Faber source recognisable regardless of
which human language the keywords are rendered in.

### Value flow {#value-flow}

| Glyph | Meaning |
|-------|---------|
| `←` | Runtime binding, reassignment, and mutation — the only assignment operator |
| `→` | Function return type declaration |
| `⇥` | Alternate exit: error-channel type or inline conversion recovery |
| `∴` | Compact therefore body — introduces a single-statement branch body |

### Type shape {#type-shape}

| Glyph | Meaning |
|-------|---------|
| `∷` | Static type ascription — compile-time assertion about a value's type |
| `↦` | Runtime conversion — parsing or coercion that may fail |
| `∪` | Inline union type — connects two types (as in `T ∪ nihil`) |

### Comparison and logic {#comparison-and-logic}

| Glyph | Meaning |
|-------|---------|
| `≡` `≠` | Exact equality and inequality — strict type match required |
| `<` `>` `≤` `≥` | Ordering comparisons |
| `∧` `∨` `⊻` `¬` | Logical and bitwise: and, or, xor, not |

### The binding convention matters {#the-binding-convention-matters}

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

<<<FENCE 1>>>

## Compared to mainstream languages {#compare}

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
| Branch + one statement | `if (cond) return x` | `si cond ∴ redde x` |
| Type cast | `(T)value`, `value as T` | `value ∷ T` |
| Conversion (may fail) | `try_into()` | `value ↦ T` |

## References {#references}

1. EBNF grammar — full glyph and keyword inventory
2. examples/corpus/ — language corpus with 292 exemplar files across all keywords
3. examples/corpus/operatores/ — operator and glyph exemplars
4. Commandments — the nine design laws that preserve these signals
