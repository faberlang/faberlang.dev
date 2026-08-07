+++
title = "Design notes"
section = "reference"
order = 3
sources = [
  "radix/docs/design/README.md",
]
+++

## Commandments

*Nine rules that make Faber feel like Faber.*

These are the design laws that define Faber's character. Syntax can evolve and
features can be added, but changes should preserve these principles. A program
that violates them may be valid Faber, but it does not feel like Faber.

The commandments apply at every level — from the grammar itself down to how
standard library APIs are named. They are the reason a reader can identify
Faber source at a glance, regardless of which human language the keywords are
rendered in or which target backend the code compiles to.

### I. Types before names {#i-types-before-names}

Declarations read from shape to binding. The type comes first because the
reader needs to know *what kind of thing* this is before the name
tells them *which* thing. This aligns with languages whose
grammatical order reads from category to instance — Chinese, Hindi, Arabic
— and produces declarations that scan uniformly.

```text
# Type before name in every declaration
textus nomen
numerus aetas
functio salve(textus name) → textus
```

### II. Mechanical over magical {#ii-mechanical-over-magical}

The same construct should mean the same thing everywhere. If a reader needs
distant context to know what a symbol does, the syntax is suspect. Faber
prefers explicit, local reasoning — the declaration site carries enough
information to understand what will happen at the use site.

```faber
# The meaning of a call is determined by the function's signature,
# not by invisible trait resolution or implicit conversions.
functio duplica(numerus n) → numerus {
    redde n * 2
}
```

### III. Glyphs carry structure {#iii-glyphs-carry-structure}

Structural and operator meaning uses glyphs, not words: `←`
for binding, `→` for return type, `⇥`
for error exit, `ergo` for compact statement body,
`≡` for equality, `∪` for union
types. Glyphs are universal — they never localise and never change meaning
across renderings. A Thai reader and a French reader see the same glyphs,
even if the keywords around them differ.

### IV. Latin carries behaviour {#iv-latin-carries-behaviour}

Words are for declarations, statements, lifecycle, and behavioural intent:
`functio`, `genus`, `fixum`,
`varia`, `redde`, `cape`.
These are bindable through reader-locale packs — they are the vocabulary,
not the grammar. The Latin choice is not about Latin superiority; it is
about picking *one* consistent classical source so that all keywords
belong to the same register and no keyword is privileged by being the
language the implementation was written in.

### V. Conjugation carries time and flow {#v-conjugation-carries-time-and-flow}

When the same root logic can run synchronously, asynchronously, or as a
generator, the conjugated form of the verb should carry that execution mode.
Ownership pairs — mutate vs copy-out — use related forms of the same stem.
This is the morphologia principle. The standard library (Norma) follows this
convention for all method names: `lege` (sync read) vs
`leget` (async read), `adde` (mutate in place) vs
`addita` (return new copy). The compiler does not enforce or
derive conjugations — it is a naming policy, not a language feature.

### VI. One sign, one job {#vi-one-sign-one-job}

A glyph or keyword may have exact aliases, but it should not carry unrelated
meanings. Aliases must point back to one canonical concept. This is the
principle that drives Faber's split between `←`
(runtime binding) and `=` (structural field shape) — most
languages collapse both into `=`, but that overloading hides
whether a line is a data-flow operation or a type-level definition.

```text
# ← is always runtime flow
fixum numerus count ← 0
count ← count + 1

# = is always structural shape inside Type { }
fixum _ p ← Point {
    x = 10,
    y = 20
}
```

### VII. Runtime flow is explicit {#vii-runtime-flow-is-explicit}

Runtime binding, reassignment, and mutation use `←`;
structural definition uses `=`. A reader scanning source can see
every data-flow operation immediately: every `←` is a
runtime event. There is no syntactic ambiguity about whether a particular
`=` means "store into this variable" or "define this field."

### VIII. Absence is typed {#viii-absence-is-typed}

Nullable value types are written as unions: `T ∪ nihil`. Optional
declaration slots use post-name markers: `sponte`. These are
distinct concepts — *a value that may be absent* vs *a slot the
caller may omit* — and Faber keeps them syntactically separate rather
than collapsing both into `T?` or `Option<T>`.

```text
# Absence in a value: T ∪ nihil
functio find(textus key) → numerus ∪ nihil

# Omission at declaration: sponte
functio connect(textus host, numerus port sponte) → vacuum
```

### IX. The compiler does not guess to hide missing information {#ix-compiler-does-not-guess}

Missing type information is an analysis problem to fix upstream, not a codegen
detail to paper over. The compiler never silently infers a type that the
programmer did not provide when the information is genuinely absent — it
reports the gap and stops. This is the rule that keeps Faber honest: if a
reader cannot determine what a symbol means from local source, the compiler
should not pretend it can.

### Purpose {#purpose}

The commandments exist to answer a question that comes up in every language
design discussion: "Is this change still Faber?" They are the invariant
check — not against a feature list, but against a character. A change that
violates a commandment may still be a good idea, but it should be recognised
as a departure from Faber's design character rather than a routine addition.

In practice, the commandments most often serve as review criteria for new
syntax proposals. A proposal that weakens "types before names" by adding a
name-first alternative, or blurs "one sign one job" by overloading a glyph,
must justify why Faber should bend its character for that feature.

## Design documents

The Radix repository contains authoritative design documents for how Faber
works as a language and compiler. They live under `radix/docs/design/`.

### Index {#index}

| Area | Files |
|------|-------|
| Targets and lowering | `target-capability-matrix.md`, `lowering-routes.md`, `semantic-ownership.md` |
| Types and sugar | `numeric-type-sugar.md`, `comparison-operators.md`, `annotation-sugar.md` |
| Collection intrinsics | `lista-intrinsics.md`, `tabula-intrinsics.md`, `tensor-intrinsics.md`, `numerus-intrinsics.md`, `fractus-intrinsics.md`, `textus-intrinsics.md`, `intervallum-intrinsics.md`, `instans-intrinsics.md`, `copia-intrinsics.md` |
| Conversion | `conversio-valor.md`, `failable-conversio.md` |
| Frames and effects | `frame-stream-types.md`, `host-provider-gateway.md` |
| Reader and format | `reader-locale.md`, `faber-canonical-surface.md` |
| Systems / AIR | `air-dialect.md`, `aiml-foundation.md`, `systems-shaped-values.md` |
| Tooling surface | `faber-scripting.md` |
| Naming debt | `mixed-case-naming-debt.md` |

### Stdlib design docs {#stdlib-design-docs}

The `radix/docs/stdlib/` directory contains:

| Doc | Role |
|-----|------|
| `morphologia.md` | Conjugation policy for all stdlib method names |
| `tensor-methods.md` | Tensor receiver method reference |
| `chorda-methods.md` | Chorda (text) method reference |
| `mathesis-methods.md` | Math method reference |
| `tempus-methods.md` | Time method reference |
| `stdlib-mechanical-verbs.md` | pange/solve/tempta trio policy |

## History

### Origins {#origins}

The first commit to the Radix compiler was made on **December 20, 2025**
as a Bun + TypeScript project with a single `docs/decisions.md` file. The
second commit codified five Architecture Decision Records that still shape
the language today.

**ADR-003**, titled "Case endings carry semantic meaning," established at
the very beginning that Latin morphology would be more than a
keyword-skin — the compiler would understand declension and conjugation
to infer program intent. The original case mappings were:

```text
Nominative  (subject)       →  return value, caller
Accusative  (direct object)  →  primary argument
Dative      (indirect obj.)  →  recipient, callback, destination
Genitive    (possession)     →  property access, "of" relationships
Ablative    (instrument)     →  dependencies, context, "using X"
```

The same document noted: *"Verb conjugation is a natural follow-on
question (future tense → async?)."* This seed grew into the modern
**morphologia** naming convention, where the standard library uses
conjugated Latin verb forms to signal sync vs async and mutate vs
copy-out — without requiring the compiler itself to understand Latin
grammar.

The project began in TypeScript, was later rewritten in Rust, and the
grammar was frozen for the 1.x line with edition 2026. The original five
ADRs (file extension `.fab`, error hints, case endings, recursive descent
parser, custom AST) are still visible in the git history.

### Releases {#releases}

Prebuilt CLI archives — current Faber release at the top, then every published
tag and binary from [faberlang/releases](https://github.com/faberlang/releases):

- **[Releases](/releases/)** — download links and historical inventory
- **[Install and download](/start/install.html)** — PATH setup and first `faber check`
