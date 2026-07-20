You are a professional technical translator for the Faber documentation site.

# Contract — Arabic (ar). Natural technical Arabic; preserve RTL prose quality.

Rules:
- Target locale: `ar`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Arabic reader-locale Faber using Arabic keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged and keep source in logical order.

## English source body

Faber separates three related ideas that many languages collapse into one
shape:

| Construct | Meaning |
|-----------|---------|
| `→ T` | Normal success return channel |
| `T ∪ nihil` | Absence in the success value domain |
| `⇥ E` | Recoverable alternate-exit channel for errors |

## Normal return {#normal-return}

<<<FENCE 0>>>

## Failable functions {#failable-functions}

Use `⇥` when a function can leave by an error channel:

<<<FENCE 1>>>

## Throwing — iace {#throwing--iace}

`iace` sends a value on the error channel:

<<<FENCE 2>>>

## Recovery — fac / cape {#recovery--fac--cape}

Callers recover locally with a `fac` block and a `cape` handler:

<<<FENCE 3>>>

A direct failable call is not an ordinary expression. Place calls to
`→ T ⇥ E` functions inside an active `fac` / `cape` boundary.

## Inline conversion recovery {#inline-conversion-recovery}

`⇥` can also specify an inline recovery value on `↦` conversions:

<<<FENCE 4>>>

## Effect-only failable {#effectonly-failable}

For functions that error but do not return a success value, omit `→ T`:

<<<FENCE 5>>>

## Current status {#current-status}

`→`, `redde`, `⇥`, `iace`, and `fac` / `cape` are live grammar and checker
surfaces. Rust and Go lowering for full `⇥` / `iace` / `cape` runtime
behaviour is still a backend gap — these pass type-checking but do not
yet emit failable runtime code to all targets.
