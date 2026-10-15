+++
title = "Types and values"
section = "language"
order = 2
sources = [
  "radix/README.md (Core Type Surfaces, Numeric Widths, Tensors And Sparsa, GPU Core Types)",
  "docs/design/numeric-type-sugar.md",
  "docs/design/tensor-intrinsics.md",
  "docs/design/lista-intrinsics.md",
  "docs/design/comparison-operators.md",
  "faber/docs/EBNF.md",
  "corpus/typi/",
  "corpus/tensor/",
  "corpus/lista/",
  "radix/README.md (Runtime binding vs structural definition, Language Orientation)",
  "corpus/fixum/",
  "corpus/sit/",
  "radix/README.md (Tensors And Sparsa)",
  "docs/design/tabula-intrinsics.md",
  "corpus/tabula/",
  "corpus/sparsa/",
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "corpus/literalia/",
  "corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
  "radix/README.md (Nullability and Optionality)",
  "corpus/nihil/",
  "corpus/sponte/",
  "radix/README.md (Conversion and Construction)",
  "docs/design/conversio-valor.md",
  "docs/design/failable-conversio.md",
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
| `i32` | Signed integer | `42` |
| `f64` | Floating-point | `3.14` |
| `bivalens` | Boolean | `verum`, `falsum` |
| `vacuum` | Unit / no value | — |
| `nihil` | Null / absent (the null value is `nulla`) | `nulla` |
| `instans` | Duration / time instant | — |
| `json` | Compile-time JSON value | `{ "key": "value" }` |
| `octeti` (en `bytes`) | Byte string, exactly `lista<b8>` (en `list<b8>`) | \|00ff\| |

### Sized numeric types {#sized-numeric-types}

Write the width in type position. These are the numeric types — the same
list as [Math in the ether](/language/behavior/numeric-widths.html):

| Family | Widths |
|--------|--------|
| Signed | `i8` `i16` `i32` `i64` |
| Unsigned | `u8` `u16` `u32` `u64` |
| Decimal | `d64` |
| Unbounded integer | `inf` |
| Floating | `f16` `bf16` `f32` `f64` |

```faber locale-tabs
incipit {
    sit i32 narrow ← 7 ∷ i32
    sit u64 wide ← 255 ∷ u64
    sit f32 single ← 1.5 ∷ f32
}
```

The bare width marker is the type.

### Raw bits {#raw-bits}

The markers `b8`, `b16`, `b32` and `b64` are raw bits, not numbers, so they
are not in the table above. A `b8` is exactly eight bits, and a `b8` is also
the element of a byte string: `|00ff|` is a `lista<b8>` (en `bytes`).

Raw bits take the bit operators `∧ ∨ ⊻ ¬ ⇐ ⇒` and nothing else. Each operation
acts at the type's own width: a left shift drops bits off the top, and a shift
by the full width or more gives all zeros. There is no arithmetic
(`SEM011 bits_arithmetic_refused`) and no mixing with numbers or with another
width. To read the bits as a number, convert to the same-width numeric type
with `↦`.

```faber
incipit {
    sit b8 flags ← 0xF0 ∷ b8
    sit b8 low ← flags ⇒ 4
    sit b8 both ← flags ∨ low
    sit u8 count ← both ↦ u8
    nota both, count
}
```

### Nullable types {#nullable-types}

Nullable values use the union syntax `T ∪ nihil`:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nulla
}

functio maybe() → textus ∪ nihil {
    redde nulla
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

```faber locale=en
fn identitas<T>(T valor) → T {
    return valor
}

fn primum<T>(list<T> res) → T ∪ none {
    return res.first()
}
```

Explicit call-site type arguments are supported:

```faber locale-tabs
functio identitas<T>(T datum) → T { redde datum }

incipit {
    sit numerus seven ← identitas<numerus>(7)
}
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
incipit {
    sit lista<numerus> nums ← [1, 2, 3]
    sit tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
}
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
incipit {
    sit tensor<f32, []> scalar ← vacua
    sit tensor<numerus, [4]> row ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
    sit numerus ∪ nihil first ← row[0]
}
```

### GPU core types {#gpu-core-types}

These are recognised by the systems lane for GPU and register work.
Package targets that lack hardware support reject them:

```faber locale=en
fn half(f16 x) → f16 { return x }

fn add(matrix<f32, [2, 2]> a, matrix<f32, [2, 2]> b) → matrix<f32, [2, 2]> {
    return a.added(b)
}

fn swap(mut atomic<i32> cell, i32 value) → i32 {
    return cell.exchange(value)
}
```

### Borrow markers on types {#borrow-markers}

Borrow markers (`de`, `varia`, `own`) can appear on types in parameter
positions to indicate how a value is passed:

```faber
# shared borrow — caller retains ownership
functio imprime(de textus label) → vacuum { }

# mutable borrow — caller lends mutable access
functio duplica(varia numerus value) → vacuum { value ← value + 1 }

# move — caller gives up ownership
functio consume(own textus buffer) → textus {
    redde buffer
}

incipit {
    varia numerus n ← 1
    sit textus s ← "salve"

    imprime(s)
    duplica(varia n)
    sit t ← consume(own s)
}
```

The call site repeats the `varia` and `own` markers (en `mut` and `own`):
`duplica(varia n)`, `consume(own s)`. Leaving one off is
`SEM057 call_marker_missing`. A parameter with no marker is read-only.

### Comparison policy {#comparison-policy}

| Operator | Family | Behaviour |
|----------|--------|-----------|
| `≡`, `≢` | Exact equality | Identical types required; `nulla` bypass |
| `≅`, `≇` | Promoted exact equality | Numeric widths join, then exact compare |
| `≈`, `≉` | Fuzzy equality | Tolerance match — `isclose` defaults (rel_tol 1e-09); numeric operands only |
| `≺`, `≤`, `≻`, `≥` | Ordering | Numeric, instant, scalar text; ASCII `<` and `>` are generic delimiters, not comparisons |
| `∈`, `∉` | Membership | Element of a collection or range; never over text (use `contains`) |

## Variables and binding

Faber has three binding words and a dedicated assignment glyph. The key
distinction is between `sit` (write-once) and `varia` (freely reassignable),
and between `←` (runtime flow) and `=` (compile-time fact). `fixum` states a
compile-time fact only: `fixum numerus LIMITE = 255`.

### sit — fixed binding {#sit-fixed-binding}

`sit` bindings are write-once. They may be declared with or without an
initializer; if declared without, they must be assigned exactly once before
reading. A second assignment is rejected.

```faber
incipit {
    sit numerus count ← 0
    sit textus name ← "Marcus"
    sit inferred ← [1, 2, 3]
}
```

Deferred initialisation:

```faber
incipit {
    sit numerus factor
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

### Inferred type {#sit-inferred-type}

Leave the type off and `sit` infers it — a fixed binding with an inferred type:

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
    sit numerus x
    sit numerus y
}

incipit {
    # Runtime: ← attaches a value to a name at execution time
    varia numerus count ← 0
    varia textus label ← "ready"
    count ← count + 1

    # Structural: = defines field values inside a type literal
    sit p ← Point {
        x = 10,
        y = 20
    }
}
```

### Field extraction (`from`) {#ex-field-extraction}

`ex` extracts fields from a value into local bindings:

```faber
genus Persona {
    sit textus nomen
    sit numerus aetas
}

incipit {
    sit p ← Persona { nomen = "Marcus", aetas = 30 }
    ex p sit nomen, aetas
    # prints "Marcus"
    nota nomen
}
```

### Mutable numeric updates {#postfix-increment-and-decrement}

Use binary `+` and `-` with runtime assignment `←` to update mutable
`numerus` places, or the postfix statements `↑` and `↓`, which add or subtract
one. Postfix `↑` and `↓` are statements, not expressions: they cannot appear
inside a larger expression, and the operand must be a mutable `numerus` place:

```faber
incipit {
    varia numerus i ← 0
    # i becomes 1
    i ← i + 1
    # i becomes 2
    i ↑
    # i becomes 1
    i ↓
    nota i
}
```

## Collections

Faber has several compiler-owned collection types. Their canonical methods
live in the compiler, not in the standard library.

### Lista — ordered dynamic collection {#lista}

```faber
incipit {
    sit lista<numerus> empty ← vacua
    sit numbers ← [1, 2, 3, 4, 5]
    sit names ← ["Marcus", "Julia", "Gaius"]
    sit nested ← [[1, 2], [3, 4]]
}
```

Spread with `sparge`:

```faber
incipit {
    sit lista<numerus> a ← [1, 2, 3]
    sit lista<numerus> b ← [4, 5, 6]
    sit combined ← [sparge a, sparge b]
    sit headed ← [0, sparge a, 99]
}
```

Key methods: `length`, `get`, `append`, `sum`, `first`, `last`.

### Tabula — key-value map {#tabula}

```faber
incipit {
    sit tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
}
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

```faber locale=en
main {
    mut map<string, int> puncta ← empty
    puncta["alpha"] ← 1
    puncta["beta"] ← 2
    print puncta.length()
}
```

### Tensor — dense fixed-shape buffer {#tensor}

```faber
incipit {
    sit tensor<f32, []> scalar ← vacua
    sit tensor<numerus, [4]> row ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
    sit numerus ∪ nihil first ← row[0]
}
```

Tensor sugar (numeric-heavy code):

```faber locale=en
main {
    let tf32[4] lanes ← [1.0, 2.0, 3.0, 4.0] ↦ tf32[4]
}
```

Key methods: `reshape`, `get`, `set`, `create`, `tensor.structa` (Latin
namespace lookup, not a receiver method), plus elementwise
`added`/`subtracted`/`multiplied`/`divided`/`negate`, matrix multiplication
(`matmul`), and reductions (`sum`, `mean`).

### Sparsa — sparse fixed-shape buffer {#sparsa}

```faber locale=en
main {
    mut sparsa<f32, [2, 3]> sparse ← empty
    sparse.set([0, 1], 4.0)
    sparse.set([1, 2], 9.0)

    # get returns the stored value, here 4.0
    print sparse.get([0, 1])
    # count of stored entries
    print sparse.count_nonzero()
}
```

Conversion between dense and sparse:

```faber
incipit {
    sit tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
    sit sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
    sit tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
}
```

### Cursors — lazy streams {#cursors}

`cursor<T>` is a lazy stream type. Created from collection iterators,
`tuus` views, or generator functions. Consumed via `itera ex`:

```faber
incipit {
    sit items ← [1, 2, 3]
    itera ex items sit item {
        nota item
    }
}
```

Generator *functions* declare their stream posture in the signature slot:
`fiunt` is a synchronous stream and `fient` an asynchronous stream; the body
yields values with `cede` (see [Functions — async and streams](/language/functions.html#async-and-streams)).

### Intervallum — ranges {#intervallum}

```faber
# exclusive range: 0, 1, 2, 3, 4
itera ab 0‥5 sit i {
    nota i
}
# inclusive range: 0, 1, 2, 3, 4, 5
itera ab 0…5 sit i {
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
| `\|…\|` | `lista<b8>` (en `bytes`) | Compile-time hex bytes |
| `regex /…/` | `regex` | Inline pattern literal; raw body, `\/` writes a slash |
| `_ /…/` | `regex` | The same literal where the cell gives the type |
| `[ … ]` | `lista<T>` | Faber list literal |

### String-template application {#string-template-application}

Faber formats text with string-template application: a `"…"` or `«…»`
literal with `§` holes, then parenthesised arguments:

```faber
functio greet(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}

incipit {
    sit numerus pagina ← 3
    sit numerus totum ← 10
    sit textus code ← "200"
    sit textus label ← "OK"

    sit msg ← "Page § of §"(pagina, totum)
    sit block ← «status: § (§)»(code, label)
    sit again ← "§1 of §0, §1"(pagina, totum)
}
```

Key rules:
- `§` (U+00A7) is the template hole
- Numbered holes: `§N` selects argument N, counting from 0, and may repeat.
  `"§1 of §0, §1"(a, b)` reads `b`, then `a`, then `b` again
- A numbered template needs max(N)+1 values, and every index below the highest
  must be read by some hole; a gap is `SEM008 template_hole_index_gap`
- Trailing `!` selects display formatting: `"Salve, §!"(nomen)`
- The `(args)` suffix is template application, not a function call

### Block strings {#block-strings}

Multiline blocks use guillemets `«…»`:

```faber
incipit {
    sit sql ← «
        select id, email
        from accounts
    »
}
```

Guillemets are the only block-string spelling — the
retired `"""` and `❝…❞` spellings fail as ordinary lex errors.

### Captured templates (forma) {#captured-templates}

Backtick templates capture text and parameters without rendering.
Safe for bound SQL/URL payloads:

```faber
incipit {
    sit numerus user_id ← 42
    sit query ← `select * from users where id = §`(user_id)
}
```

### Inline JSON {#inline-json}

A bare `{ … }` is inline JSON: a compile-time `json` document, not an
anonymous Faber object. Keys are quoted strings separated by `:`. Values are
JSON constants only — no variable references, no Faber expressions. Ascribing
one to a [`tabula`](#tabula) lowers it to a real constant map; `↦ valor`
widens it to the dynamic carrier instead:

```faber
incipit {
    sit json blank ← {}
    sit user ← { "name": "Marcus", "age": 30, "active": true }
    sit nested ← { "meta": { "version": 1 }, "tags": ["alpha", "beta"] }
}
```

For typed genus construction, use the type name and `=` field shape:

```faber
genus Point {
    sit numerus x
    sit numerus y
}
incipit {
    sit p ← Point { x = 10, y = 20 }
}
```

## Nullability and optionality

Faber distinguishes absence in a value from optional provision at a
declaration site.

### Nullable values — T ∪ nihil {#nullable-values}

Use `T ∪ nihil` when the value can be absent:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nulla
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nulla
    redde a / b
}
```

### Optional declaration slots — sponte {#optional-declaration-slots}

Use `sponte` after the name when a parameter or field may be omitted
by the caller or constructor:

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    sit textus email sponte
}
```

Borrow markers can combine with optional parameters:

```faber
functio process(de numerus depth sponte) → vacuum { }
```

### Non-null assertion — ! {#non-null-assertion}

Use `!.`, `![`, `!(` to assert a nullable value is not `nulla`:

```faber
genus Box { sit numerus ∪ nihil val }
incipit {
    sit Box ∪ nihil maybe_name ← Box { val = 7 }
    sit name ← maybe_name!.val
}
```

A non-null assertion on `nulla` aborts at runtime.

### Nullish coalescing — vel {#nullish-coalescing}

```faber
incipit {
    sit textus ∪ nihil provided ← nulla
    sit name ← provided vel "default"
}
```

### ignotum {#ignotum}

`ignotum` is the top-level unknown type for escape hatches and incomplete
knowledge. It is not a nullability mechanism.

## Conversion and construction

Two important conversion operators, one for runtime and one for compile-time:

```faber
incipit {
    # runtime conversion
    sit parsed ← "42" ↦ numerus ⊥ 0
    # static ascription
    sit numerus count ← 7
    sit text ← count ∷ textus
}
```

### Runtime conversion — ↦ {#runtime-conversion}

Use `↦` for runtime conversion, especially parsing or coercion that may
fail. Supply an inline default with `⊥`:

```faber
incipit {
    sit textus input ← "9"
    sit n ← "42" ↦ numerus ⊥ 0
    sit safe ← input ↦ numerus ⊥ 0
}
```

Type-directed materialization:

```faber
incipit {
    sit textus path ← "/etc/hosts"
    sit lanes ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
    sit body ← ad 'solum:lege' (path) ↦ textus
}
```

### Static ascription — ∷ {#static-ascription}

Use `∷` for explicit static type ascription. It is postfix and
target-type driven:

```faber
incipit {
    sit numerus count ← 7
    sit x ← 7 ∷ i32
    sit text ← count ∷ textus
}
```
