+++
title = "Types and values"
section = "language"
order = 2
sources = [
  "radix/README.md (Core Type Surfaces, Numeric Widths, Tensors And Sparsa, GPU Core Types)",
  "radix/docs/design/numeric-type-sugar.md",
  "radix/docs/design/tensor-intrinsics.md",
  "radix/docs/design/lista-intrinsics.md",
  "radix/docs/design/comparison-operators.md",
  "radix/EBNF.md",
  "radix/corpus/typi/",
  "radix/corpus/tensor/",
  "radix/corpus/lista/",
  "radix/README.md (Runtime binding vs structural definition, Language Orientation)",
  "radix/corpus/fixum/",
  "radix/corpus/sit/",
  "radix/README.md (Tensors And Sparsa)",
  "radix/docs/design/tabula-intrinsics.md",
  "radix/corpus/tabula/",
  "radix/corpus/sparsa/",
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "radix/corpus/literalia/",
  "radix/corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
  "radix/README.md (Nullability and Optionality)",
  "radix/corpus/nihil/",
  "radix/corpus/sponte/",
  "radix/README.md (Conversion and Construction)",
  "radix/docs/design/conversio-valor.md",
  "radix/docs/design/failable-conversio.md",
]
+++

## Data types

Faber has a static, type-first type system. Every declaration places the type
before the name — the `textus` comes first, then the identifier it names, not
the other way round. The type system covers
scalar primitives, generic collections, sized numerics, tensors, and GPU-facing
register types.

### Primitive types {#primitive-types}

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

### Sized numeric types {#sized-numeric-types}

`numerus` and `fractus` have default widths (i64 and f64) and explicit width
forms:

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

Width sugar is available in type position: `i8` … `u64`, `f16`, `f32`, `f64`
are equivalent to `numerus<W>` / `fractus<W>`.

### Nullable types {#nullable-types}

Nullable values use the union syntax `T ∪ nihil`:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio maybe() → textus ∪ nihil {
    redde nihil
}
```

There is no `T?` or `Option<T>` syntax in Faber. The union is explicit.

### Type aliases {#type-aliases}

```faber
typus UserId = numerus
```

### Generics {#generics}

Functions, type aliases, `genus`, and `implendum` accept type parameters with
`<T>` syntax:

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

Explicit call-site type arguments are supported:

```faber
functio identitas<T>(T datum) → T { redde datum }

fixum numerus seven ← identitas<numerus>(7)
```

### Collections {#collections}

| Type | Role | Sugar |
|------|------|-------|
| `lista<T>` | Ordered dynamic collection | `lf32`, `lu32` |
| `tabula<K, V>` | Key-value map | — |
| `tensor<T, Figura>` | Dense fixed-shape buffer | `tf32[4]`, `ti64[2,3]` |
| `sparsa<T, Figura>` | Sparse fixed-shape buffer | `sf32[4]`, `si64[2,3]` |
| `intervallum` | Range type | — |
| `copia<T>` | Unordered set | — |
| `cursor<T>` | Lazy stream | — |
| `promissum<T>` | Async finite result from `fiet` functions; `promissum<T ⇥ E>` carries a delayed alternate channel | — |

```faber
fixum lista<numerus> nums ← [1, 2, 3]
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

### Tensor types {#tensor-types}

`tensor<T, Figura>` is the dense fixed-shape container:

| Form | Meaning |
|------|---------|
| `tensor<T, Figura>` | Canonical spelling |
| `tensor<T, []>` | Rank-0 (scalar container) |
| `tensor<T, _>` | Shape inference hole |
| `tensor<T, [N]>` | Rank-1 vector |
| `tensor<T, [N, M]>` | Rank-2 matrix |

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> row ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← row[0]
```

### GPU core types {#gpu-core-types}

These are recognised by the systems lane for GPU and register work.
Package targets that lack hardware support reject them:

```faber
functio half(f16 x) → f16 { redde x }

functio add(matrix<f32, [2, 2]> a, matrix<f32, [2, 2]> b) → matrix<f32, [2, 2]> {
    redde a.addita(b)
}

functio swap(atomic<i32> cell, i32 value) → i32 {
    redde cell.exchange(value)
}
```

### Borrow markers on types {#borrow-markers}

Borrow markers (`de`, `in`, `ex`) can appear on types in parameter
positions to indicate how a value is passed:

```faber locale=la
# shared borrow — caller retains ownership
functio imprime(de textus label) → vacuum { }

# mutable borrow — caller lends mutable access
functio duplica(in numerus value) → vacuum { }

# move — caller gives up ownership
functio consume(ex textus buffer) → textus {
    redde buffer
}
```

### Comparison policy {#comparison-policy}

| Operator | Family | Behaviour |
|----------|--------|-----------|
| `≡`, `≠` | Exact equality | Identical types required; `nihil` bypass |
| `≈`, `≉` | Numeric value equality | Numeric lattice only |
| `<`, `≤`, `>`, `≥` | Ordering | Numeric, instant, scalar text |
| `intra` | Range containment | Numeric in range |
| `inter` | Collection membership | Element in collection |

## Variables and binding

Faber has three variable keywords and a dedicated assignment glyph. The key
distinction is between `fixum` (write-once) and `varia` (freely reassignable),
and between `←` (runtime flow) and `=` (structural field shape).

### fixum — immutable binding {#fixum-immutable-binding}

`fixum` bindings are write-once. They may be declared with or without an
initializer; if declared without, they must be assigned exactly once before
reading. A second assignment is rejected.

```faber
fixum numerus count ← 0
fixum textus name ← "Marcus"
fixum _ inferred ← [1, 2, 3]
```

Deferred initialisation:

```faber
incipit {
    fixum numerus factor
    si verum {
        factor ← 10
    } secus {
        factor ← 100
    }
    nota factor
}
```

### varia — mutable binding {#varia-mutable-binding}

`varia` bindings are freely reassignable:

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

### sit — inferred immutable sugar {#sit-inferred-immutable-sugar}

`sit` is sugar for `fixum _` — an immutable binding with inferred type:

```faber
incipit {
    sit salve ← "Salve"
    sit nomen ← "Marcus"
    sit x ← 42

    # Deferred form
    sit label
    label ← "deferred"
}
```

### Runtime binding vs structural definition {#runtime-binding-vs-structural-definition}

Faber splits what most languages collapse into `=`:

| Glyph | Role | Use for |
|-------|------|---------|
| `←` | Runtime flow | Initial binding, reassignment, mutation |
| `=` | Structural shape | Field names inside literals and metadata |

```faber
genus Point {
    numerus x
    numerus y
}

incipit {
    # Runtime: ← attaches a value to a name at execution time
    varia numerus count ← 0
    varia textus label ← "ready"
    count ← count + 1

    # Structural: = defines field values inside a type literal
    fixum _ p ← Point {
        x = 10,
        y = 20
    }
}
```

### Ex field extraction {#ex-field-extraction}

`ex` extracts fields from a value into local bindings:

```faber
genus Persona {
    textus nomen
    numerus aetas
}

incipit {
    fixum _ p ← Persona { nomen = "Marcus", aetas = 30 }
    ex p fixum nomen, aetas
    # prints "Marcus"
    nota nomen
}
```

### Postfix increment and decrement {#postfix-increment-and-decrement}

`⊕` and `⊖` are postfix increment/decrement statements for mutable
`numerus` places. They are statement-only — no expression value, no
prefix forms:

```faber
incipit {
    varia numerus i ← 0
    # i becomes 1
    i ⊕
    # i becomes 0
    i ⊖
}
```

## Collections

Faber has several compiler-owned collection types. Their canonical methods
live in the compiler, not in the standard library.

### Lista — ordered dynamic collection {#lista}

```faber
fixum lista<numerus> empty ← vacua
fixum _ numbers ← [1, 2, 3, 4, 5]
fixum _ names ← ["Marcus", "Julia", "Gaius"]
fixum _ nested ← [[1, 2], [3, 4]]
```

Spread with `sparge`:

```faber
fixum _ a ← [1, 2, 3]
fixum _ b ← [4, 5, 6]
fixum _ combined ← [sparge a, sparge b]
fixum _ headed ← [0, sparge a, 99]
```

Key methods: `longitudo`, `accipe`, `appende`, `summa`, `primus`, `novissimus`.

### Tabula — key-value map {#tabula}

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

The `:` there is not map syntax. A bare `{ … }` is always
[inline JSON](#inline-json) — a compile-time `json` document whose keys are
quoted strings separated by `:`. Declaring the binding as a `tabula` ascribes
that document to a map type, which lowers it to a real constant map.

Faber's own key-value shape uses `=`, and it is only available on a named
type: `Point { x = 10 }`. There is no anonymous `{ key = expr }` object —
writing one is a parse error, not a second spelling of the line above.

For a map you build up rather than declare whole, start from `vacua` and
assign by key:

```faber
incipit {
    varia tabula<textus, numerus> puncta ← vacua
    puncta["alpha"] ← 1
    puncta["beta"] ← 2
    nota puncta.longitudo()
}
```

### Tensor — dense fixed-shape buffer {#tensor}

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> row ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← row[0]
```

Tensor sugar (numeric-heavy code):

```faber
fixum tf32[] seed ← vacua
fixum tf32[4] lanes ← seed.strue([1.0, 2.0, 3.0, 4.0], [4])
```

Key methods: `forma`, `accipe`, `ponde`, `crea`, `structa`, `strue`, plus
elementwise arithmetic, matrix multiplication (`multiplicatio`), and
reductions (`summa`, `productum`).

### Sparsa — sparse fixed-shape buffer {#sparsa}

```faber
fixum sparsa<fractus<f32>, [2, 3]> sparse ← vacua
sparse.ponde([0, 1], 4.0)
sparse.ponde([1, 2], 9.0)

# accipe returns the stored value, here 4.0
nota sparse.accipe([0, 1])
# count of stored entries
nota sparse.nonnihil()
```

Conversion between dense and sparse:

```faber
fixum tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
fixum sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
fixum tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
```

### Cursors — lazy streams {#cursors}

`cursor<T>` is a lazy stream type. Created from collection iterators,
tuus views, or generator functions. Consumed via `itera ex`:

```faber
fixum _ items ← [1, 2, 3]
itera ex items fixum item {
    nota item
}
```

Generator *functions* declare their stream posture in the signature slot:
`fiunt` is a synchronous stream and `fient` an asynchronous stream; the body
yields values with `cede` (see [Functions — async and streams](/language/functions.html#async-and-streams)).

### Intervallum — ranges {#intervallum}

```faber
# exclusive range: 0, 1, 2, 3, 4
itera ab 0‥5 fixum i {
    nota i
}
# inclusive range: 0, 1, 2, 3, 4, 5
itera ab 0…5 fixum i {
    nota i
}
```

`‥` is exclusive range endpoint; `…` is inclusive.

## String and template literals

Faber uses delimiter semantics — each quote form means a different source
shape. They are not interchangeable synonyms.

### Literal forms {#literal-forms}

| Form | Type | Role |
|------|------|------|
| `'…'` | `ascii` | Fixed machine tokens; no `§`; no `(…)` |
| `"…"` | `textus` | Short Unicode line strings; `(…)` renders |
| `«…»` | `textus` | Block/multiline Unicode; `(…)` renders |
| `` `…` `` | `forma` | Captured templates; `(…)` captures |
| `{ … }` | `json` | Compile-time JSON document |
| `|…|` | `octeti` | Compile-time hex bytes |
| `[ … ]` | `lista<T>` | Faber list literal |

### String-template application {#string-template-application}

Faber formats text with string-template application: a `"…"` or `«…»`
literal with `§` holes, then parenthesised arguments:

```faber
functio greet(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}

fixum numerus pagina ← 3
fixum numerus totum ← 10
fixum textus code ← "200"
fixum textus label ← "OK"

fixum _ msg ← "Page § of §"(pagina, totum)
fixum _ block ← «status: § (§)»(code, label)
```

Key rules:
- `§` (U+00A7) is the template hole
- Positional holes: `§0`, `§1`, … for explicit ordering
- Trailing `!` selects display formatting: `"Salve, §!"(nomen)`
- The `(args)` suffix is template application, not a function call

### Block strings {#block-strings}

Multiline blocks use guillemets `«…»`:

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

Guillemets are the only block-string spelling since Radix v0.79.0 — the
retired `"""` and `❝…❞` spellings fail as ordinary lex errors.

### Captured templates (forma) {#captured-templates}

Backtick templates capture text and parameters without rendering.
Safe for bound SQL/URL payloads:

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

### Inline JSON {#inline-json}

A bare `{ … }` is inline JSON: a compile-time `json` document, not an
anonymous Faber object. Keys are quoted strings separated by `:`. Values are
JSON constants only — no variable references, no Faber expressions. Ascribing
one to a [`tabula`](#tabula) lowers it to a real constant map; `↦ valor`
widens it to the dynamic carrier instead:

```faber
fixum _ empty ← {}
fixum _ user ← { "name": "Marcus", "age": 30, "active": true }
fixum _ nested ← { "meta": { "version": 1 }, "tags": ["alpha", "beta"] }
```

For typed genus construction, use the type name and `=` field shape:

```faber
genus Point {
    numerus x
    numerus y
}
fixum _ p ← Point { x = 10, y = 20 }
```

## Nullability and optionality

Faber distinguishes absence in a value from optional provision at a
declaration site.

### Nullable values — T ∪ nihil {#nullable-values}

Use `T ∪ nihil` when the value can be absent:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

### Optional declaration slots — sponte {#optional-declaration-slots}

Use `sponte` after the name when a parameter or field may be omitted
by the caller or constructor:

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    textus email sponte
}
```

Borrow markers can combine with optional parameters:

```faber
functio process(de numerus depth sponte) → vacuum { }
```

### Non-null assertion — ! {#non-null-assertion}

Use `!.`, `![`, `!(` to assert a nullable value is not `nihil`:

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

A non-null assertion on `nihil` aborts at runtime.

### Nullish coalescing — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

### ignotum {#ignotum}

`ignotum` is the top-level unknown type for escape hatches and incomplete
knowledge. It is not a nullability mechanism.

## Conversion and construction

Two important conversion operators, one for runtime and one for compile-time:

```faber
# runtime conversion
fixum _ parsed ← "42" ↦ numerus
# static ascription
fixum numerus count ← 7
fixum _ text ← count ∷ textus
```

### Runtime conversion — ↦ {#runtime-conversion}

Use `↦` for runtime conversion, especially parsing or coercion that may
fail. Supply inline recovery with `⇥`:

```faber
fixum textus input ← "9"
fixum _ n ← "42" ↦ numerus
fixum _ safe ← input ↦ numerus ⇥ 0
```

Type-directed materialization:

```faber
fixum textus path ← "/etc/hosts"
fixum _ lanes ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
fixum _ body ← ad 'solum:lege' (path) ↦ textus
```

### Static ascription — ∷ {#static-ascription}

Use `∷` for explicit static type ascription. It is postfix and
target-type driven:

```faber
fixum numerus count ← 7
fixum _ x ← 7 ∷ numerus<i32>
fixum _ text ← count ∷ textus
```

### Nullish coalescing — vel {#nullish-coalescing}

Use `vel` for nullish coalescing when a value is `nihil`:

```faber
fixum textus ∪ nihil provided_name ← nihil
fixum _ name ← provided_name vel "default"
```
