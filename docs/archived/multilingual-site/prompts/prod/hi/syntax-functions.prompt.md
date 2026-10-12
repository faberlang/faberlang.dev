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

Functions in Faber are declared with `functio`, using type-first parameter
syntax and a glyph return type.

## Basic syntax {#basic-syntax}

<<<FENCE 0>>>

With an error channel:

<<<FENCE 1>>>

## Examples {#examples}

<<<FENCE 2>>>

## Return values {#return-values}

Use `redde` for normal returns:

<<<FENCE 3>>>

Bare `redde` for `vacuum` return type:

<<<FENCE 4>>>

## Borrowing and mutability (de, in, ex) {#borrowing-and-mutability}

Faber marks how a value is passed with short prepositions on parameters:

| Marker | Intent | Typical Rust lowering |
|--------|--------|----------------------|
| *(none)* | Owned value | `T` by value |
| `de` | Shared borrow (read-only) | `&T` |
| `in` | Mutable borrow | `&mut T` |
| `ex` | Consume (move into callee) | `T` by move |

<<<FENCE 5>>>

The same words (`de`, `ex`) are reused in other constructs — do not read
every `ex` as "consume":

| Surface | Role |
|---------|------|
| `de textus name` on parameter | Shared borrow |
| `in numerus count` on parameter | Mutable borrow |
| `ex textus buffer` on parameter | Move into callee |
| `itera ex items fixum item` | Iterate values |
| `itera de tabula fixum key` | Iterate keys |
| `ex source fixum x, ceteri rest` | Destructure fields |
| `importa ex "path"` | Import from module |

## Entry point {#entry-point}

The program entry point is `incipit`:

<<<FENCE 6>>>

## CLI entry point {#cli-entry-point}

For CLI programs, `incipit argumenta` receives parsed command arguments:

<<<FENCE 7>>>

## Passing mode — `sponte` {#passing-mode-sponte}

`sponte` marks a parameter that may be omitted by the caller:

<<<FENCE 8>>>
