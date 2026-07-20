You are a professional technical translator for the Faber documentation site.

# Contract — Traditional Chinese (zh-Hant / 繁體). Traditional only, never Simplified.

Rules:
- Target locale: `zh-Hant`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Traditional Chinese reader-locale Faber using Traditional Chinese keywords where the pack overrides Simplified Chinese rows, while preserving universal Faber glyph syntax.

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
