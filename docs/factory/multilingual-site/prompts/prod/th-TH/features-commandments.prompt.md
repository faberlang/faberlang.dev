You are a professional technical translator for the Faber documentation site.

# Contract — Thai (th-TH). Natural technical Thai developer docs.

Rules:
- Target locale: `th-TH`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Thai reader-locale Faber using Thai keywords for declarations, control flow, loops, returns, booleans, common primitive types, and lista/tabula collections. Keep Faber glyph syntax unchanged.

## English source body

*Nine rules that make Faber feel like Faber.*

These are the design laws that define Faber's character. Syntax can evolve and
features can be added, but changes should preserve these principles. A program
that violates them may be valid Faber, but it does not feel like Faber.

The commandments apply at every level — from the grammar itself down to how
standard library APIs are named. They are the reason a reader can identify
Faber source at a glance, regardless of which human language the keywords are
rendered in or which target backend the code compiles to.

## I. Types before names {#i-types-before-names}

Declarations read from shape to binding. The type comes first because the
reader needs to know *what kind of thing* this is before the name
tells them *which* thing. This aligns with languages whose
grammatical order reads from category to instance — Chinese, Hindi, Arabic
— and produces declarations that scan uniformly.

<<<FENCE 0>>>

## II. Mechanical over magical {#ii-mechanical-over-magical}

The same construct should mean the same thing everywhere. If a reader needs
distant context to know what a symbol does, the syntax is suspect. Faber
prefers explicit, local reasoning — the declaration site carries enough
information to understand what will happen at the use site.

<<<FENCE 1>>>

## III. Glyphs carry structure {#iii-glyphs-carry-structure}

Structural and operator meaning uses glyphs, not words: `←`
for binding, `→` for return type, `⇥`
for error exit, `∴` for compact branch body,
`≡` for equality, `∪` for union
types. Glyphs are universal — they never localise and never change meaning
across renderings. A Thai reader and a French reader see the same glyphs,
even if the keywords around them differ.

## IV. Latin carries behaviour {#iv-latin-carries-behaviour}

Words are for declarations, statements, lifecycle, and behavioural intent:
`functio`, `genus`, `fixum`,
`varia`, `redde`, `cape`.
These are bindable through reader-locale packs — they are the vocabulary,
not the grammar. The Latin choice is not about Latin superiority; it is
about picking *one* consistent classical source so that all keywords
belong to the same register and no keyword is privileged by being the
language the implementation was written in.

## V. Conjugation carries time and flow {#v-conjugation-carries-time-and-flow}

When the same root logic can run synchronously, asynchronously, or as a
generator, the conjugated form of the verb should carry that execution mode.
Ownership pairs — mutate vs copy-out — use related forms of the same stem.
This is the morphologia principle. The standard library (Norma) follows this
convention for all method names: `lege` (sync read) vs
`leget` (async read), `adde` (mutate in place) vs
`addita` (return new copy). The compiler does not enforce or
derive conjugations — it is a naming policy, not a language feature.

## VI. One sign, one job {#vi-one-sign-one-job}

A glyph or keyword may have exact aliases, but it should not carry unrelated
meanings. Aliases must point back to one canonical concept. This is the
principle that drives Faber's split between `←`
(runtime binding) and `=` (structural field shape) — most
languages collapse both into `=`, but that overloading hides
whether a line is a data-flow operation or a type-level definition.

<<<FENCE 2>>>

## VII. Runtime flow is explicit {#vii-runtime-flow-is-explicit}

Runtime binding, reassignment, and mutation use `←`;
structural definition uses `=`. A reader scanning source can see
every data-flow operation immediately: every `←` is a
runtime event. There is no syntactic ambiguity about whether a particular
`=` means "store into this variable" or "define this field."

## VIII. Absence is typed {#viii-absence-is-typed}

Nullable value types are written as unions: `T ∪ nihil`. Optional
declaration slots use post-name markers: `sponte`. These are
distinct concepts — *a value that may be absent* vs *a slot the
caller may omit* — and Faber keeps them syntactically separate rather
than collapsing both into `T?` or `Option<T>`.

<<<FENCE 3>>>

## IX. The compiler does not guess to hide missing information {#ix-compiler-does-not-guess}

Missing type information is an analysis problem to fix upstream, not a codegen
detail to paper over. The compiler never silently infers a type that the
programmer did not provide when the information is genuinely absent — it
reports the gap and stops. This is the rule that keeps Faber honest: if a
reader cannot determine what a symbol means from local source, the compiler
should not pretend it can.

## Purpose {#purpose}

The commandments exist to answer a question that comes up in every language
design discussion: "Is this change still Faber?" They are the invariant
check — not against a feature list, but against a character. A change that
violates a commandment may still be a good idea, but it should be recognised
as a departure from Faber's design character rather than a routine addition.

In practice, the commandments most often serve as review criteria for new
syntax proposals. A proposal that weakens "types before names" by adding a
name-first alternative, or blurs "one sign one job" by overloading a glyph,
must justify why Faber should bend its character for that feature.
