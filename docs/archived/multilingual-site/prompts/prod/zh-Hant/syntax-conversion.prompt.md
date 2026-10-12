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

Two important conversion operators, one for runtime and one for compile-time:

<<<FENCE 0>>>

## Runtime conversion — ↦ {#runtime-conversion}

Use `↦` for runtime conversion, especially parsing or coercion that may
fail. Supply inline recovery with `⇥`:

<<<FENCE 1>>>

Type-directed materialization:

<<<FENCE 2>>>

## Static ascription — ∷ {#static-ascription}

Use `∷` for explicit static type ascription. It is postfix and
target-type driven:

<<<FENCE 3>>>

## Nullish coalescing — vel {#nullish-coalescing}

Use `vel` for nullish coalescing when a value is `nihil`:

<<<FENCE 4>>>
