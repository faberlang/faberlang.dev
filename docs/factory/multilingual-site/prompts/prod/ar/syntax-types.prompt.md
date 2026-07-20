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

Faber has a static, type-first type system. Every declaration places the type
before the name: `textus nomen`, not `nomen: textus`. The type system covers
scalar primitives, generic collections, sized numerics, tensors, and GPU-facing
register types.

## Primitive types {#primitive-types}

| Type | Role | Example literal |
|------|------|-----------------|
| `textus` | Unicode string | `"Salve, munde"` |
| `ascii` | Fixed machine token | `'solum:lege'` |
| `numerus` | Signed integer (default i64) | `42` |
| `fractus` | Floating-point (default f64) | `3.14` |
| `bivalens` | Boolean | `verum`, `falsum` |
| `vacuum` | Unit / no value | — |
| `nihil` | Null / absent | `nihil` |
| `instans` | Duration / time instant | — |
| `json` | Compile-time JSON value | `{ "key": "value" }` |
| `octeti` | Hex byte sequence | \|00ff\| |

## Sized numeric types {#sized-numeric-types}

`numerus` and `fractus` have default widths (i64 and f64) and explicit width
forms:

<<<FENCE 0>>>

Width sugar is available in type position: `i8` … `u64`, `f16`, `f32`, `f64`
are equivalent to `numerus<W>` / `fractus<W>`.

## Nullable types {#nullable-types}

Nullable values use the union syntax `T ∪ nihil`:

<<<FENCE 1>>>

There is no `T?` or `Option<T>` syntax in Faber. The union is explicit.

## Type aliases {#type-aliases}

<<<FENCE 2>>>

## Generics {#generics}

Functions, type aliases, `genus`, and `implendum` accept type parameters with
`<T>` syntax:

<<<FENCE 3>>>

Explicit call-site type arguments are supported:

<<<FENCE 4>>>

## Collections {#collections}

| Type | Role | Sugar |
|------|------|-------|
| `lista<T>` | Ordered dynamic collection | `lf32`, `lu32` |
| `tabula<K, V>` | Key-value map | — |
| `tensor<T, Figura>` | Dense fixed-shape buffer | `tf32[4]`, `ti64[2,3]` |
| `sparsa<T, Figura>` | Sparse fixed-shape buffer | `sf32[4]`, `si64[2,3]` |
| `intervallum` | Range type | — |
| `copia<T>` | Unordered set | — |
| `cursor<T>` | Lazy stream | — |

<<<FENCE 5>>>

## Tensor types {#tensor-types}

`tensor<T, Figura>` is the dense fixed-shape container:

| Form | Meaning |
|------|---------|
| `tensor<T, Figura>` | Canonical spelling |
| `tensor<T, []>` | Rank-0 (scalar container) |
| `tensor<T, _>` | Shape inference hole |
| `tensor<T, [N]>` | Rank-1 vector |
| `tensor<T, [N, M]>` | Rank-2 matrix |

<<<FENCE 6>>>

## GPU core types {#gpu-core-types}

These are recognised by the systems lane for GPU and register work.
Package targets that lack hardware support reject them:

<<<FENCE 7>>>

## Borrow markers on types {#borrow-markers}

Borrow markers (`de`, `in`, `ex`) can appear on types in parameter
positions to indicate how a value is passed:

<<<FENCE 8>>>

## Comparison policy {#comparison-policy}

| Operator | Family | Behaviour |
|----------|--------|-----------|
| `≡`, `≠` | Exact equality | Identical types required; `nihil` bypass |
| `≈`, `≉` | Numeric value equality | Numeric lattice only |
| `<`, `≤`, `>`, `≥` | Ordering | Numeric, instant, scalar text |
| `intra` | Range containment | Numeric in range |
| `inter` | Collection membership | Element in collection |
