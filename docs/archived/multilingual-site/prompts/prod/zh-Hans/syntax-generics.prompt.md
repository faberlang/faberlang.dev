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

Functions, type aliases, `genus`, and `implendum` accept type parameters
with `<T>` syntax.

## Generic functions {#generic-functions}

<<<FENCE 0>>>

## Explicit call-site type arguments {#explicit-callsite-type-arguments}

<<<FENCE 1>>>

## Generic genus {#generic-genus}

<<<FENCE 2>>>

## Size parameters {#size-parameters}

`magnitudo` declares a size/index parameter in generic parameter lists:

<<<FENCE 3>>>
