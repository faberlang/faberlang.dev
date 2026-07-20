You are a professional technical translator for the Faber documentation site.

# Contract — Simplified Chinese (zh-Hans / 简体). Simplified characters only.

Rules:
- Target locale: `zh-Hans`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Simplified Chinese reader-locale Faber using Chinese keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged.

## English source body

Faber distinguishes absence in a value from optional provision at a
declaration site.

## Nullable values — T ∪ nihil {#nullable-values}

Use `T ∪ nihil` when the value can be absent:

<<<FENCE 0>>>

## Optional declaration slots — sponte {#optional-declaration-slots}

Use `sponte` after the name when a parameter or field may be omitted
by the caller or constructor:

<<<FENCE 1>>>

Borrow markers can combine with optional parameters:

<<<FENCE 2>>>

## Non-null assertion — ! {#non-null-assertion}

Use `!.`, `![`, `!(` to assert a nullable value is not `nihil`:

<<<FENCE 3>>>

A non-null assertion on `nihil` aborts at runtime.

## Nullish coalescing — vel {#nullish-coalescing}

<<<FENCE 4>>>

## ignotum {#ignotum}

`ignotum` is the top-level unknown type for escape hatches and incomplete
knowledge. It is not a nullability mechanism.
