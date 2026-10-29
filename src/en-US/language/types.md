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
  "faber/docs/EBNF.md",
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
| `i32` | Signed integer | `42` |
| `f64` | Floating-point | `3.14` |
| `bivalens` | Boolean | `verum`, `falsum` |
| `vacuum` | Unit / no value | — |
| `nihil` | Null / absent (the null value is `nulla`) | `nulla` |
| `instans` | Duration / time instant | — |
| `json` | Compile-time JSON value | `{ "key": "value" }` |
| `lista<b8>` (en `list<b8>`) | Byte string: a run of raw bytes. There is no separate byte word (the old `octeti` / `bytes` is retired) | \|00ff\| |

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
the element of a byte string: `|00ff|` is a `lista<b8>` (en `list<b8>`). There is no byte
type: eight raw bits are `b8`, an eight-bit number is `u8`, and a run of bytes
is `list<b8>`.

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

The conversion runs both ways between a bits type and a number of the same
width: `n ↦ b32` for a `u32` or `i32`, and back with `↦ u32`. A width that
does not match is `SEM016 bits_conversion_width_mismatch`, and a literal
negative shift count is `SEM010 shift_count_negative`. Converting into `f16`
or `bf16` rounds to that format at the store.

```faber locale=en
main {
    let u32 n ← 7
    let b32 bits ← n ↦ b32
    let u32 back ← bits ↦ u32
    print bits, back

    let f16 h ← 0.1 ↦ f16
    print h ↦ f64

    let b8 flags ← 0xf0
    print flags ⇒ 4
}
```

This prints `0x00000007 7`, then `0.0999755859375` (the nearest `f16` to
0.1), then `0x0f`.

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

### Interfaces {#interfaces}

An `interface` (la `implendum`) is a contract of methods, and a `class` that
says `implements` (la `implet`) must keep it. The compiler checks the
contract: a missing method is `SEM010 implet_missing_method`, and a method
whose signature differs from the contract's is
`SEM010 implet_method_signature_mismatch`.

```faber locale=en
interface Shape {
    fn area() → f64
}

class Square implements Shape {
    let f64 side

    fn area() → f64 {
        return self.side * self.side
    }
}

main {
    let Square sq ← Square { side = 3.0 }
    print sq.area()
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
| `ratio<label: T, …>` | Labeled record value (en `record`) | `{ label = value }` |
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

Access markers (`ref`, `mut`, `own`, `copy`; Latin `de`, `varia`, `penes`,
`exemplum`) can appear on types in parameter positions to indicate how a value
is passed. A parameter with no marker is `ref`:

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
    sit _ t ← consume(own s)
}
```

The call site repeats the `mut` and `own` markers (Latin `varia` and
`penes`): `duplica(varia n)`, `consume(own s)`. Leaving one off is
`SEM057 call_marker_missing`. A parameter with no marker is `ref`: the function
may read it and may not write it.

### Comparison policy {#comparison-policy}

| Operator | Family | Behaviour |
|----------|--------|-----------|
| `≡`, `≢` | Exact equality | Identical types required; `nulla` bypass |
| `≅`, `≇` | Promoted exact equality | Numeric widths join, then exact compare |
| `≈`, `≉` | Fuzzy equality | Tolerance match — `isclose` defaults (rel_tol 1e-09); numeric operands only |
| `≺`, `≤`, `≻`, `≥` | Ordering | Numeric, instant, scalar text; ASCII `<` and `>` are generic delimiters, not comparisons |
| `intra` | Range containment | Numeric in range |
| `inter` | Collection membership | Element in collection |

## Variables and binding

Four binding words say how a name is bound, and a dedicated glyph attaches a
value. The key distinctions are between a fixed name and a writable one, and
between `←` (runtime flow) and `=` (structural field shape).

| English | Latin | Meaning |
|---------|-------|---------|
| `let T x ← e` | `sit` | a fixed name |
| `mut T x ← e` | `varia` | re-pointable and writable |
| `ref T x ← e` | `de` | re-pointable and read-only |
| `const T X = e` | `fixum` | a compile-time fact, set with `=` |

Every binding word writes its type slot. There is no short form: `let x ← 3`
is `PARSE010 binding_type_slot_required`. Write the type, `let int x ← 3`, or
write `_` to have it inferred, `let _ x ← 3`.

### let (sit) — a fixed name {#let-fixed-name}

A `let` binding cannot be assigned again once it is set. It may be declared
with or without an initializer; if declared without, it must be assigned
exactly once before reading. A second assignment is
`SEM020 immutable_second_assignment`.

```faber
incipit {
    sit numerus count ← 0
    sit textus name ← "Marcus"
    sit _ inferred ← [1, 2, 3]
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

### mut (varia) — a writable name {#mut-writable-name}

A `mut` binding can be assigned again, and its value can be written through the
name. The retired word for this was `var` (`PARSE010 var_retired`):

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

### Inferred types with `_` {#inferred-types}

`_` in the type slot asks the compiler to infer the type. It works with every
binding word, and with the deferred form, which is still written with the slot:

```faber
incipit {
    sit _ salve ← "Salve"
    sit _ nomen ← "Marcus"
    sit _ x ← 42

    # Deferred form
    sit _ label
    label ← "deferred"
}
```

A local may take the name of a value word such as `true`, `false` or `null`.
The binding shadows the value for the rest of its scope, and the compiler
warns `WARN021 value_literal_shadowing` instead of refusing it:

```faber locale=en
main {
    let string true ← "t"
    print true
}
```

This prints `t`.

### ref (de) and const (fixum) {#ref-and-const}

`ref` names a value that can be re-pointed but not written. It is the mode of a
bare parameter. `const` is no longer a run-time binding: it declares a
compile-time fact with `=`, never `←`. A run-time `const T x ← e` (Latin
`fixum`) is `PARSE010 runtime_const_retired`; write `let`.

```faber locale=en
const int LIMIT = 3

fn first(list<int> xs) → int {
    ref list<int> view ← xs
    return view[0]
}

main {
    let int n ← 4
    mut int total ← 0
    total ← total + n
    print first([5, 6]), LIMIT, total
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
    sit _ p ← Point {
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
    sit _ p ← Persona { nomen = "Marcus", aetas = 30 }
    ex p sit nomen, aetas
    # prints "Marcus"
    nota nomen
}
```

### Mutable numeric updates {#postfix-increment-and-decrement}

Use binary `+` and `-` with runtime assignment `←` to update mutable
`numerus` places. Both operators take two operands; they are not postfix
statements:

```faber
incipit {
    varia numerus i ← 0
    # i becomes 1
    i ← i + 1
    # i becomes 0
    i ← i - 1
}
```

## Collections

Faber has several compiler-owned collection types. Their canonical methods
live in the compiler, not in the standard library.

### Lista — ordered dynamic collection {#lista}

```faber
incipit {
    sit lista<numerus> empty ← vacua
    sit _ numbers ← [1, 2, 3, 4, 5]
    sit _ names ← ["Marcus", "Julia", "Gaius"]
    sit _ nested ← [[1, 2], [3, 4]]
}
```

Spread with `sparge`:

```faber
incipit {
    sit lista<numerus> a ← [1, 2, 3]
    sit lista<numerus> b ← [4, 5, 6]
    sit _ combined ← [sparge a, sparge b]
    sit _ headed ← [0, sparge a, 99]
}
```

Key methods: `length`, `get`, `append`, `extend`, `find`, `sum`, `first`,
`last`, `take`, `slice`.

`xs.extend(ys)` appends every element of another list of the same element type,
in order and in place; the argument is read once first, so a list can extend
itself. `xs.find(T x ∴ predicate)` (la `reperta`) returns the first element
where the predicate holds as `T ∪ none`, calling the predicate left to right and
stopping at the first match. Since 1.17.

`take(n)` and `slice(a, b)` are checked windows. A window that runs past the
end of the list is reported, not clamped, so both are failable: outside
`main` the call needs a handler (a `⊥` recovery value, a `do { } catch`, or a
failable enclosing function), or it is `SEM011 failable_call_requires_handler`.
Inside `main` an unhandled failure ends the program with `take_out_of_range`
or `slice_out_of_range`.

```faber locale=en
fn head(list<int> xs, int n) → list<int> {
    return xs.take(n) ⊥ xs
}

main {
    let list<int> xs ← [1, 2, 3, 4, 5]
    print head(xs, 2)
    print head(xs, 9)
    print xs.slice(1, 3) ⊥ []
}
```

This prints `[1, 2]`, `[1, 2, 3, 4, 5]` and `[2, 3]`. Before 1.15 the second
call clamped silently; it now falls back to `xs` because the window failed.
The runner, Rust, TypeScript and Python all check windows this way (generated
TypeScript and Python clamped until 1.16).

### Bounded lists — `size` {#bounded-lists}

A list can carry a length limit in its type. The limit is written after `size`
(la `magnitudo`): `list<int, size 4>` holds at most four elements. A bare
`list<int, 4>` is retired by name (`SEM008 list_count_needs_size`), and so is a
bare `lo‥hi` range, which bounds a value rather than a count. The same rule
covers every bounded container: `vector<f32, size 4>` (the `vf32[4]` sugar is
unchanged), `queue<int, size 4>`, `stack<int, size 4>`, `string<size 8>` and
`ascii<size 8>` (`SEM008 vector_width_needs_size`, `SEM008 capacity_needs_size`).

A range after `size` bounds the length. `‥` leaves the upper bound out and `…`
includes it, so `list<int, size 2‥5>` holds two to four elements and
`list<int, size 1…∞>` is never empty: `first` and `last` return plain values.
Growing past the maximum or removing below the minimum reports on the error
channel. `list<int, size 3>` and `list<int, size 0…3>` are the same type.

A short list literal takes the capacity of the cell it is stored into, whether
the cell is a variable, a field or a call argument: `[1, 2]` stored into
`list<int, size 0…3>` is a list with room for three. A literal longer than the
maximum is refused by name.

```faber locale=en
main {
    # Never empty: first and last are plain ints.
    mut list<int, size 1…∞> xs ← [1, 2, 3]
    print xs.first()
    print xs.last()
    print xs.length()
    xs.append(4)
    print xs

    # Lengths 2 to 4: the fifth push does not fit.
    mut list<int, size 2‥5> ys ← [10, 20]
    do {
        ys.append(30)
        ys.append(40)
        ys.append(50)
        print "unreachable"
    }
    catch err {
        print "full: §"(err)
    }
    print ys

    # A short literal takes the cell's capacity.
    let list<int, size 0…3> pair ← [1, 2]
    print pair
}
```

This prints `1`, `3`, `3`, `[1, 2, 3, 4]`, then `full: list length range: push
past the maximum`, `[10, 20, 30, 40]` and `[1, 2]`.

### Tabula — key-value map {#tabula}

```faber
incipit {
    sit tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
}
```

The `:` there is not map syntax. A bare `{ … }` with quoted keys and `:` is
[inline JSON](#inline-json) — a compile-time `json` document. Declaring the
binding as a `tabula` ascribes that document to a map type, which lowers it to
a real constant map.

Faber's own key-value shape uses `=`: on a named type, `Point { x = 10 }`, or
with no type name as a [record](#record), `{ x = 10 }`. A record is a value
with labeled, read-only fields, not a map: it has no keys to look up at run
time.

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

### Records — labeled values {#record}

A record is a value made of labeled fields. The English type word is
`record` (Latin `ratio`). Fields are read by label, never by position, and a
record is not a class: two record types are the same when they have the same
labels with exactly the same field types, in any order.

A bare `{ label = value }` in a cell with no declared type is a record whose
fields take their default types; `record<*>` names that type. A record prints
like a class value without the type name, in the order the fields were
written. A destructuring `rest` binding of a typed record is a record of the
fields that were not named.

```faber locale=en
main {
    let record<x: f64, y: int> typed ← record<x: f64, y: int> { x = 1.5, y = 2 }
    let _ point ← { x = 1.5, y = 2 }
    print typed.x
    print point

    let {x, rest others} ← typed
    print x
    print others
}
```

This prints `1.5`, `{ x = 1.5, y = 2 }`, `1.5` and `{ y = 2 }`.

Records are values, so their fields are read-only. Writing through a field is
`SEM020 assignment_to_fixum_field`, even when the binding is `mut`; build a
new record, or use a class with a `mut` field.

```faber locale=en outcome=rejects
main {
    mut _ point ← { x = 1.5, y = 2 }
    point.x ← 3.0
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

A rank-1 tensor takes a range in brackets and gives that window as a new
tensor. A literal range that falls outside a literal shape is
`SEM011 index_provably_out_of_bounds`.

```faber locale=en
main {
    let tf32[6] v ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0] ↦ tf32[6]
    let tf32[3] mid ← v[1‥4]
    print mid
}
```

This prints `[2.0, 3.0, 4.0]`.

A matrix reads and writes one element by row and column with a double
bracket, `m[[row, col]]`, and the coordinates may be computed. The method
forms follow the three list reads: `m.get([r, c])` gives `none` for a
coordinate outside the shape, `m.at([r, c])` reports it on the error channel,
and `m.set([r, c], v)` stores. A literal coordinate that is provably outside
the shape is refused at compile time.

```faber locale=en
main {
    mut matrix<f32, [2, 2]> m ← [[1.0, 2.0], [3.0, 4.0]] ↦ matrix<f32, [2, 2]>
    let int row ← 1
    print m[[0, 1]]
    m[[row, 0]] ← 7.5
    print m.get([row, 5]) coalesce 0.0
    print m.at([row, 1]) ⊥ 0.0
    print m
}
```

This prints `2.0`, `0.0`, `4.0` and `[[1.0, 2.0], [7.5, 4.0]]`. A bracket
range on a vector or a matrix slices to a vector or a matrix, and `↦`
converts between tensors, vectors and matrices of the same shape.

Known issue in 1.17: element access runs on `faber run`, but generated Rust
does not compile it yet, and the TypeScript, Swift and LLVM targets refuse it
by name rather than approximate it.

Key methods: `reshape`, `get`, `set`, `create`, `tensor.structa` (Latin
namespace lookup, not a receiver method), plus elementwise
`added`/`subtract`/`multiply`/`divide`/`negate`, matrix multiplication
(`matmul`), and reductions (`sum`, `mean`).

### Sparsa — sparse fixed-shape buffer {#sparsa}

The English spelling is `sparse` (since 1.15; an English file that writes
the Latin `sparsa` is `PARSE040 wrong_locale_type`).

```faber locale=en
main {
    mut sparse<f32, [2, 3]> sparse ← empty
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
tuus views, or generator functions. Consumed via `itera ex`:

```faber
incipit {
    sit _ items ← [1, 2, 3]
    itera ex items sit item {
        nota item
    }
}
```

Generator *functions* declare their stream posture in the signature slot:
`fiunt` is a synchronous stream and `fient` an asynchronous stream; the body
yields values with `cede` (see [Functions — async and streams](/language/functions.html#async-and-streams)).

### Sinks — ⇜ {#sinks}

`Sink<T>` is the contract for "take one item". A class opts in with
`implements Sink<T>` and supplies `sink(T)` and `flush()`, both failable.
`s ⇜ x` is the operator form of `s.sink(x)`: the method reports a failed write
on the error channel, and the operator stops the program. The item must be
exactly the sink's `T`; there is no implicit conversion. The sink must be
writable, so a `let` sink is refused.

The contract is declared in the source file today (an import of `norma:sink`
checks but does not run yet):

```faber locale=en
@ radix contract "sinking"
interface Sink<T> {
    fn sink(T item) → void ⇥ string
    fn flush() → void ⇥ string
}

class Tally implements Sink<int> {
    mut int total = 0

    fn sink(int item) → void ⇥ string {
        self.total ← self.total + item
    }

    fn flush() → void ⇥ string {
    }
}

main {
    mut Tally tally ← Tally { total = 0 }
    tally.sink(3)
    tally ⇜ 4
    print tally.total
}
```

This prints `7`. Lists and sets are sinks too: `⇜` appends to a list
(duplicates kept) and adds a missing item to a set. On a bounded
`list<T, size N>` that is already full, `.sink(v)` reports.

```faber locale=en
main {
    mut list<string> log ← []
    log.append("begin")
    log ⇜ "step"
    log ⇜ "step"
    print log
}
```

This prints `["begin", "step", "step"]`; `log.append(v)` and `log ⇜ v` do the same thing here.

Known issue in 1.17: `⇜` runs on `faber run`, Rust and LLVM; the Go,
TypeScript, Swift, WebAssembly, Racket, Python and Cranelift targets refuse it
by name (`CODEGEN001`).

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

A range is also a value. The English type word is `range` (since 1.15; an
English file that writes the Latin `intervallum` is
`PARSE040 wrong_locale_type`). A range stored in a cell can be walked, and
printing it shows its construction:

```faber locale=en
main {
    let range<int> r ← 2‥5
    print r
    for range r let i {
        print i
    }
}
```

This prints `2‥5`, then `2`, `3` and `4`.

A stored range can carry a step (since 1.16). The step is part of the type:
`range<int>` has step 1, and `range<int, 2>` steps by 2. `length()` counts
only the members on the step, and `contains(v)` is true only for a value on
the step.

```faber locale=en
main {
    let range<int, 2> evens ← 0…10 step 2
    print evens.length()
    print evens.contains(4)
    print evens.contains(3)
}
```

This prints `6`, `true` and `false`. A stored step must be a positive integer
literal and the bounds must be integers; a step known only at run time stays
inline in `for range` and in bracket windows
(`SEM010 intervallum_value_step_unsupported` elsewhere). Operations that
cannot keep a step (`clamp`, `coercere`, `inter`, `union`) refuse a stepped
range by name rather than dropping the step.

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
| `\|…\|` | `lista<b8>` (en `list<b8>`) | Compile-time hex bytes |
| `regex /…/` | `regex` | Inline pattern literal; raw body, `\/` writes a slash (inside a class too: `[\/]`) |
| `_ /…/` | `regex` | The same literal where the cell gives the type |
| `[ … ]` | `lista<T>` | Faber list literal |

A bounded text cell such as `ascii<size N>` keeps text behaviour: `+` joins and
the ordering operators compare as text.

```faber locale=en
main {
    let ascii<size 8> a ← 'ab'
    let ascii<size 8> b ← 'cd'
    print a + b
    print a ≺ b
    print 'ab' ≥ 'cd'
}
```

This prints `abcd`, `true` and `false`.

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

    sit _ msg ← "Page § of §"(pagina, totum)
    sit _ block ← «status: § (§)»(code, label)
    sit _ again ← "§1 of §0, §1"(pagina, totum)
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

### Escapes {#escapes}

A string literal may escape only its own delimiter, the backslash, `n`, `t`, `r`
and `u{…}`. Any other escape is `LEX003 unknown_escape`; the old pass-through is
gone. Text that contains quotes can use guillemets, `«say "hi"»`, with no
escapes, and the lint `WARN034` suggests that rewrite.

### Block strings {#block-strings}

Multiline blocks use guillemets `«…»`:

```faber
incipit {
    sit _ sql ← «
        select id, email
        from accounts
    »
}
```

Guillemets are the only block-string spelling since Radix v0.79.0 — the
retired `"""` and `❝…❞` spellings fail as ordinary lex errors.

### Captured templates (forma) {#captured-templates}

Backtick templates capture text and parameters without rendering.
Safe for bound SQL/URL payloads:

```faber
incipit {
    sit numerus user_id ← 42
    sit _ query ← `select * from users where id = §`(user_id)
}
```

### Inline JSON {#inline-json}

A bare `{ … }` with quoted keys and `:` is inline JSON: a compile-time `json`
document. (With `label = value` fields it is a [record](#record) instead.)
Values are
JSON constants only — no variable references, no Faber expressions. Ascribing
one to a [`tabula`](#tabula) lowers it to a real constant map; `↦ valor`
widens it to the dynamic carrier instead:

```faber
incipit {
    sit json blank ← {}
    sit _ user ← { "name": "Marcus", "age": 30, "active": true }
    sit _ nested ← { "meta": { "version": 1 }, "tags": ["alpha", "beta"] }
}
```

For typed genus construction, use the type name and `=` field shape:

```faber
genus Point {
    sit numerus x
    sit numerus y
}
incipit {
    sit _ p ← Point { x = 10, y = 20 }
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
    sit _ name ← maybe_name!.val
}
```

A non-null assertion on `nulla` aborts at runtime.

### Nullish coalescing — vel {#nullish-coalescing}

```faber
incipit {
    sit textus ∪ nihil provided ← nulla
    sit _ name ← provided vel "default"
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
    sit _ parsed ← "42" ↦ numerus ⊥ 0
    # static ascription
    sit numerus count ← 7
    sit _ text ← count ∷ textus
}
```

### Runtime conversion — ↦ {#runtime-conversion}

Use `↦` for runtime conversion, especially parsing or coercion that may
fail. Supply an inline default with `⊥`:

```faber
incipit {
    sit textus input ← "9"
    sit _ n ← "42" ↦ numerus ⊥ 0
    sit _ safe ← input ↦ numerus ⊥ 0
}
```

Type-directed materialization:

```faber
incipit {
    sit textus path ← "/etc/hosts"
    sit _ lanes ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
    sit _ body ← ad 'solum:lege' (path) ↦ textus
}
```

Text converts to a boolean only when it is the code locale's word: in an
English file `"true" ↦ bool` and `"false" ↦ bool` succeed, and any other text
fails and takes the `⊥` value. Without a `⊥` the failure stops the program.
Every target agrees (since 1.16; Go, TypeScript, Swift, LLVM and Racket used to
test truthiness or emptiness instead).

```faber locale=en
main {
    print "true" ↦ bool ⊥ false
    print "yes" ↦ bool ⊥ false
}
```

This prints `true` and `false`.

Not every pair converts. Text does not convert to a list of characters with
`↦`; that is refused by name (`SEM016 textus_to_lista_unsupported`).

### Static ascription — ∷ {#static-ascription}

Use `∷` for explicit static type ascription. It is postfix and
target-type driven:

```faber
incipit {
    sit numerus count ← 7
    sit _ x ← 7 ∷ i32
    sit _ text ← count ∷ textus
}
```

### Nullish coalescing — vel {#nullish-coalescing}

Use `vel` for nullish coalescing when a value is `nulla`:

```faber
incipit {
    sit textus ∪ nihil provided_name ← nulla
    sit _ name ← provided_name vel "default"
}
```
