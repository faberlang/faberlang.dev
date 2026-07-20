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

The Faber language corpus is the public language dictionary: one top-level
directory per keyword, operator group, or language type surface. It is the
development source for `faber explain` and the primary input for
multi-target compile matrices.

## Stats {#stats}

- 292 `.fab` exemplar files
- 174 registry terms in `index.toml`
- ~135 keyword and concept directories

## Layout {#layout}

<<<FENCE 0>>>

## File format {#file-format}

Each `.fab` file begins with TOML frontmatter describing the term:

<<<FENCE 1>>>

## Usage {#usage}

<<<FENCE 2>>>

## Categories {#categories}

Terms are organised by category: `function`, `control-flow`, `type`,
`collection`, `transfer`, `annotation`, `iteration`, `destructuring`,
`testing`, `cli`, `concept`, `operator-group`, `existing-home`.
