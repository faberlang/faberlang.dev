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

Faber uses glyphs where the symbol is structural. Below is the full inventory
of source glyphs recognised by the lexer.

## Value flow {#value-flow}

| Glyph | Meaning |
|-------|---------|
| `←` | Runtime binding, reassignment, and mutation |
| `→` | Function return type |
| `⇥` | Alternate exit — error-channel type or inline conversion recovery |
| `∴` | Compact therefore body (`si cond ∴ redde x`) |

## Type shape {#type-shape}

| Glyph | Meaning |
|-------|---------|
| `∷` | Static type ascription (compile-time cast) |
| `↦` | Runtime conversion (can-fail parse/coerce) |
| `∪` | Inline union type (`T ∪ nihil`) |

## Comparison {#comparison}

| Glyph | Meaning |
|-------|---------|
| `≡` `≠` | Exact equality and inequality |
| `<` `>` `≤` `≥` | Ordering |
| `≈` `≉` | Numeric value equality |

## Logical and bitwise {#logical-and-bitwise}

| Glyph | Meaning |
|-------|---------|
| `∧` `∨` `⊻` `¬` | And, or, xor, not |
| `⇐` `⇒` | Left and right bit shift |

## Assignment updates {#assignment-updates}

| Glyph | Meaning |
|-------|---------|
| `←` | The only assignment operator in expressions |
| `⊕` `⊖` | Postfix increment/decrement statements (mutable numerus only) |

## Optional chaining and non-null assertion {#optional-chaining-and-non-null-assertion}

| Glyph | Meaning |
|-------|---------|
| `?` `?.` `?[` `?(` | Optional chaining |
| `!` `!.` `![` `!(` | Non-null assertion |

## Ranges {#ranges}

| Glyph | Meaning |
|-------|---------|
| `‥` | Exclusive range endpoint |
| `…` | Inclusive range endpoint |

## Literal delimiters {#literal-delimiters}

| Glyph | Type | Role |
|-------|------|------|
| `'` | `ascii` | Fixed machine tokens |
| `"` | `textus` | Line string |
| `«` `»` | `textus` | Block string (guillemets) |
| `` ` `` | `forma` | Captured template |
| `|` | `octeti` | Hex literal |
| `§` | template hole | Placeholder inside `"…"`, `«…»`, `` `…` `` |

## Punctuation {#punctuation}

| Glyph | Role |
|-------|------|
| `(` `)` | Grouping and call |
| `{` `}` | Block, genus literal, or JSON document |
| `[` `]` | List literal and indexing |
| `.` | Member access |
| `,` | Separator |
| `;` | Statement separator |
| `:` | JSON field separator |
| `=` | Structural field shape (not runtime assignment) |
| `@` | Annotation marker |
| `#` | Line comment |
