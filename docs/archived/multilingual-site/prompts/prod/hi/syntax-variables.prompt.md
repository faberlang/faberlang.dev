You are a professional technical translator for the Faber documentation site.

# Contract — Hindi (hi / Devanagari). Natural modern tech Hindi.

Rules:
- Target locale: `hi`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Hindi reader-locale Faber using Hindi keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged.

## English source body

Faber has three variable keywords and a dedicated assignment glyph. The key
distinction is between `fixum` (write-once) and `varia` (freely reassignable),
and between `←` (runtime flow) and `=` (structural field shape).

## fixum — immutable binding {#fixum-immutable-binding}

`fixum` bindings are write-once. They may be declared with or without an
initializer; if declared without, they must be assigned exactly once before
reading. A second assignment is rejected.

<<<FENCE 0>>>

Deferred initialisation:

<<<FENCE 1>>>

## varia — mutable binding {#varia-mutable-binding}

`varia` bindings are freely reassignable:

<<<FENCE 2>>>

## sit — inferred immutable sugar {#sit-inferred-immutable-sugar}

`sit` is sugar for `fixum _` — an immutable binding with inferred type:

<<<FENCE 3>>>

## Runtime binding vs structural definition {#runtime-binding-vs-structural-definition}

Faber splits what most languages collapse into `=`:

| Glyph | Role | Use for |
|-------|------|---------|
| `←` | Runtime flow | Initial binding, reassignment, mutation |
| `=` | Structural shape | Field names inside literals and metadata |

<<<FENCE 4>>>

## Ex field extraction {#ex-field-extraction}

`ex` extracts fields from a value into local bindings:

<<<FENCE 5>>>

## Postfix increment and decrement {#postfix-increment-and-decrement}

`⊕` and `⊖` are postfix increment/decrement statements for mutable
`numerus` places. They are statement-only — no expression value, no
prefix forms:

<<<FENCE 6>>>
