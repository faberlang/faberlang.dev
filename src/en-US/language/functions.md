+++
title = "Functions and control flow"
section = "language"
order = 3
sources = [
  "radix/README.md (Language Orientation, Borrowing and Mutability, How Faber Feels)",
  "radix/corpus/functio/",
  "radix/corpus/de/",
  "radix/corpus/in/",
  "radix/corpus/ex/",
  "radix/corpus/fiet/",
  "radix/corpus/fiunt/",
  "radix/corpus/fient/",
  "radix/corpus/cede/",
  "radix/corpus/promissum/",
  "radix/docs/design/semantic-ownership.md",
  "radix/README.md (Control Flow Shape, Canonical Surface)",
  "radix/corpus/si/",
  "radix/corpus/itera/",
  "radix/corpus/dum/",
  "radix/corpus/custodi/",
  "radix/corpus/discerne/",
  "radix/corpus/elige/",
  "radix/README.md (Type and Size Generics)",
  "radix/corpus/generic/",
  "radix/corpus/functio/generic-call-type-args.fab",
]
+++

## Functions

Functions in Faber are declared with `functio`, using type-first parameter
syntax and a glyph return type.

### Basic syntax {#basic-syntax}

```faber
functio twice(numerus n) → numerus {
    redde n
}
```

With an error channel:

```faber
functio parse(textus input) → numerus ⇥ textus {
    redde 0
}
```

### Examples {#examples}

```faber
# No parameters, no return
functio saluta() {
    nota "Salve, Mundus!"
}

# Parameter, no explicit return
functio dic(textus verbum) {
    nota verbum
}

# Parameter and return type
functio duplica(numerus n) → numerus {
    redde n * 2
}

# Multiple parameters
functio adde(numerus a, numerus b) → numerus {
    redde a + b
}
```

### Return values {#return-values}

Use `redde` for normal returns:

```faber
functio porta(numerus x) → numerus {
    si x ≺ 0 ergo redde 0
    redde x * 2
}
```

Bare `redde` for `vacuum` return type:

```faber
functio tace() → vacuum {
    redde
}
```

### Async and streams {#async-and-streams}

Callable posture is a signature slot after modifiers and before `→` / `⇥`
or the body. A bare function is synchronous finite; the posture words
declare the execution mode:

| Posture | Meaning | Typical return |
|---------|---------|----------------|
| *(none)* | Synchronous finite | `T` |
| `fiet` | Asynchronous finite | `promissum<T>` or `promissum<T ⇥ E>` |
| `fiunt` | Synchronous stream (yields via `cede`) | cursor values, optionally `⇥ E` |
| `fient` | Asynchronous stream (yields via `cede`) | async cursor values, optionally `⇥ E` |

```faber
# Async finite — returns a promise
functio responde() fiet → numerus {
    redde 42
}

# Synchronous stream — yields values
functio stream() fiunt → numerus {
    cede 1
    cede 2
}
```

Await forms bind or consume the eventual value:

| Form | Role |
|------|------|
| `figendum T x ← future` | Await-bind immutable |
| `variandum T x ← future` | Await-bind mutable |
| `reddet future` | Await-return (`fiet` functions only) |
| `tacebit future` | Await and discard |
| `cede value` | Yield a value (`fiunt` / `fient` only) |

```faber
functio responde() fiet → numerus {
    redde 42
}

incipiet {
    figendum numerus responsum ← responde()
    tacebit responde()
    nota "done"
}
```

`promissum<T>` is infallible shorthand for `promissum<T ⇥ numquam>`;
`promissum<T ⇥ E>` preserves an alternate error channel. Infallible widens
to failable; failable does not narrow.

The `@ futura` and `@ cursor` annotations remain accepted compatibility
spellings, but the posture words above are the canonical surface — prefer
`fiet` over `@ futura`, and `fiunt` / `fient` over `@ cursor`.

#### Two-channel promises {#two-channel-promises}

A `fiet` function returns a `promissum` — but the promise carries **both**
channels, not just the eventual value. `promissum<T>` is the infallible
form: shorthand for `promissum<T ⇥ numquam>`. `promissum<T ⇥ E>` keeps the
**delayed alternate channel** alongside the success value, so a failable
async call fails exactly like a failable sync call — the error is delivered
with the result, not through a separate callback, channel, or thrown
exception. Awaiting a failable promise is itself a failable operation, so it
happens inside a `fac` / `cape` boundary:

```faber
functio computa(numerus densitas) fiet → numerus ⇥ textus {
    si densitas ≺ 0 ergo iace "invalid input"
    redde 7
}

incipiet {
    fac {
        figendum numerus valor ← computa(3)
        nota valor
    }
    cape err {
        nota err
    }
}
```

The await forms bind or consume both channels: `figendum` / `variandum`
await-bind the success value, `reddet` re-emits the promise from an async
function, and `tacebit` awaits and discards either outcome.

#### Promises in streams {#promises-in-streams}

The two-channel shape composes with generators. An asynchronous stream may
declare `fient → T ⇥ E`: every pull is itself a promise that either yields
`T`, ends, or fails with `E`, and the first failure ends the stream.
Iteration with `itera ex` handles the channel:

```faber
functio poll() fient → numerus ⇥ textus {
    cede 1
    iace "link lost"
}

incipiet {
    itera ex poll() sit lectio {
        nota lectio
    }
}
```

A synchronous stream may also carry an alternate channel (`fiunt → T ⇥ E`);
the stream call is then failable, so the consuming code handles it with
`fac` / `cape`:

```faber
functio stream() fiunt → numerus ⇥ textus {
    cede 1
}

incipit {
    fac {
        itera ex stream() sit item {
            nota item
        }
    }
    cape err {
        nota err
    }
}
```

### Borrowing and mutability (ref, mut, from) {#borrowing-and-mutability}

Faber marks how a value is passed with short prepositions on parameters:

| Marker | Intent | Typical Rust lowering |
|--------|--------|----------------------|
| *(none)* | Read-only value (a bare parameter is `ref`) | `T` by value |
| `de` (en `ref`) | Shared borrow (read-only) | `&T` |
| `varia` (en `mut`) | Mutable borrow | `&mut T` |
| `own` | Consume (move into callee) | `T` by move |

```faber
# Shared borrow
functio imprime(de textus label) → vacuum {
    nota label
}

# Mutable borrow
functio duplica(varia numerus value) → vacuum {
    value ← value * 2
}

# Consume
functio consume(own textus buffer) → textus {
    redde buffer
}

# Unmarked: read-only
functio salve(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}

incipit {
    varia numerus n ← 4
    sit textus t ← "abc"
    imprime(t)
    duplica(varia n)
    nota consume(own t)
    nota salve("Marcus")
}
```

An unmarked parameter is read-only all the way down: it cannot be assigned to,
and sharing a list parameter into a writable binding (`mut list<int> ys ← xs`)
is `SEM065 const_shared_into_var`. A writable copy is written
`mut list<int> ys ← copy xs`. Since 1.18 `copy` is refused for a value that
reaches something with identity, such as a channel or a `Closable` class: see [what `copy` will not duplicate](/language/types.html#copy-resources).
`varia` (en `mut`) and `own` are repeated at the call site, as in `duplica(varia n)` and `consume(own t)`; leaving the marker off
is `SEM057 call_marker_missing`. A `de` argument takes no call-site marker.

The same words (`de`, `ex`) are reused in other constructs — do not read
every `ex` as "consume":

| Surface | Role |
|---------|------|
| `de textus name` on parameter | Shared borrow |
| `varia numerus count` on parameter | Mutable borrow |
| `own textus buffer` on parameter | Move into callee |
| `itera ex items sit item` | Iterate values |
| `itera de tabula sit key` | Iterate keys |
| `ex source sit x, ceteri rest` | Destructure fields |
| `importa ex "path"` | Import from module |

### Entry point {#entry-point}

The program entry point is `incipit`:

```faber
incipit {
    nota "ingressus"
}
```

`incipiet` is the async entry point — the body may await (`figendum`,
`variandum`, `reddet`, `tacebit`) and call `fiet` / `fient` functions.

### CLI entry point {#cli-entry-point}

For CLI programs, `incipit argumenta` receives parsed command arguments:

```faber
@ cli "echo"
@ descriptio "Prints text"
@ operandus ceteri textus words
incipit argumenta args {
    itera ex args.words sit word {
        nota word
    }
}
```

### Passing mode — `sponte` {#passing-mode-sponte}

`sponte` marks a parameter that may be omitted by the caller:

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```

## Control flow

### Conditional branching {#conditional-branching}

#### si / sin / secus {#si-sin-secus}

```faber
incipit {
    sit _ condition ← verum
    si condition {
        # truthy branch
        nota "matched"
    }
}
```

With else-if and else:

```faber
incipit {
    sit _ score ← 85
    si score ≥ 90 {
        nota "A"
    } sin score ≥ 80 {
        nota "B"
    } secus {
        nota "C"
    }
}
```

#### Compact branch with ergo {#compact-branch-with-ergo}

A single-statement branch body uses `ergo`:

```faber
functio classify(numerus b, bivalens ready, numerus value) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nulla
    si ready ergo redde value
    redde nulla
}
```

### Iteration {#iteration}

#### Values — itera ex {#values-itera-ex}

```faber
functio inveni(lista<numerus> items, numerus target) → numerus ∪ nihil {
    itera ex items sit item {
        si item ≡ target ergo redde item
    }
    redde nulla
}
```

#### Keys — itera de {#keys-itera-de}

```faber
incipit {
    sit tabula<textus, numerus> tabula ← { "unus": 1, "duo": 2 }
    itera de tabula sit key {
        nota key
    }
}
```

#### Range — itera ab {#range-itera-ab}

```faber
itera ab 0 ‥ 10 sit i {
    nota i
}
```

### While loops {#while-loops}

```faber
incipit {
    sit _ condition ← verum
    dum condition {
        # body
        tacet
    }
}
```

### Guard sections — custodi {#guard-sections-custodi}

`custodi` groups early-exit checks before a function's main body.
Each `si` clause is a sequential guard:

```faber
functio divide(numerus a, numerus b) → numerus {
    custodi {
        si b ≡ 0 {
            redde 0
        }
    }
    redde a / b
}
```

`custodi` is not breakable in v1 — it is a guard rail, not a loop.

### Pattern matching — elige {#pattern-matching-elige}

`elige` selects the first matching arm:

```faber
functio describe(numerus value) → textus {
    elige value {
        casu 1 { redde "one" }
        casu 2 { redde "two" }
        ceterum { redde "many" }
    }
}
```

### Tagged union matching — discerne {#tagged-union-matching-discerne}

`discerne` exhaustively matches `discretio` variants:

```faber
discretio Exitus {
    Bonum { textus nuntius },
    Malum { textus causa }
}

functio refer(Exitus eventus) → textus {
    discerne eventus {
        casu Bonum sit nuntius { redde nuntius }
        casu Malum sit causa { redde "Error: §"(causa) }
    }
}
```

### Try blocks — fac / cape {#try-blocks-fac-cape}

`fac` opens a block that may throw, and `cape` recovers:

```faber
functio divide(numerus a, numerus b) → numerus {
    redde a / b
}

functio tutus(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    } cape err {
        mone err
        redde 0
    }
}
```

## Generics

Functions, type aliases, `genus`, and `implendum` accept type parameters
with `<T>` syntax.

### Generic functions {#generic-functions}

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

### Explicit call-site type arguments {#explicit-callsite-type-arguments}

```faber
functio identitas<T>(T valor) → T { redde valor }

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde nulla
}

incipit {
    sit _ seven ← identitas<numerus>(7)
    sit _ maybe ← primum<numerus>([seven])
}
```

### Generic genus {#generic-genus}

```faber
genus Par<T> {
    sit T primus
    sit T secundus
}
```

### Size parameters {#size-parameters}

`magnitudo` declares a size parameter in generic parameter lists, bound by the bounded collection it appears in. The collection spells its capacity with the same marker, `lista<T, magnitudo N>`; a bare `lista<T, N>` is retired:

```faber
functio longitudo<T, magnitudo N>(lista<T, magnitudo N> xs) → numerus {
    redde xs.longitudo()
}
```

A call that names a size argument writes the marker too, as the signature declares the parameter (`f<int, size 4>(x)` in English); a bare natural there is `SEM057 size_marker_required`.
