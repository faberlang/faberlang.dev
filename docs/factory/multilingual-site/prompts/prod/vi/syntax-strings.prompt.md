You are a professional technical translator for the Faber documentation site.

# Contract — Vietnamese (vi). Natural technical Vietnamese developer docs.

Rules:
- Target locale: `vi`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Vietnamese reader-locale Faber using Vietnamese keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged and preserve Vietnamese tone marks.

## English source body

Faber uses delimiter semantics — each quote form means a different source
shape. They are not interchangeable synonyms.

## Literal forms {#literal-forms}

| Form | Type | Role |
|------|------|------|
| `'…'` | `ascii` | Fixed machine tokens; no `§`; no `(…)` |
| `"…"` | `textus` | Short Unicode line strings; `(…)` renders |
| `«…»` | `textus` | Block/multiline Unicode; `(…)` renders |
| `` `…` `` | `forma` | Captured templates; `(…)` captures |
| `{ … }` | `json` | Compile-time JSON document |
| `|…|` | `octeti` | Compile-time hex bytes |
| `[ … ]` | `lista<T>` | Faber list literal |

## String-template application {#string-template-application}

Faber formats text with string-template application: a `"…"` or `«…»`
literal with `§` holes, then parenthesised arguments:

<<<FENCE 0>>>

Key rules:
- `§` (U+00A7) is the template hole
- Positional holes: `§0`, `§1`, … for explicit ordering
- Trailing `!` selects display formatting: `"Salve, §!"(nomen)`
- The `(args)` suffix is template application, not a function call

## Block strings {#block-strings}

Multiline blocks use guillemets `«…»`:

<<<FENCE 1>>>

## Captured templates (forma) {#captured-templates}

Backtick templates capture text and parameters without rendering.
Safe for bound SQL/URL payloads:

<<<FENCE 2>>>

## Inline JSON {#inline-json}

A bare `{ … }` is inline JSON: a compile-time `json` document, not an
anonymous Faber object. Keys are quoted strings separated by `:`:

<<<FENCE 3>>>

For typed genus construction, use the type name and `=` field shape:

<<<FENCE 4>>>
