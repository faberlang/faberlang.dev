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

The Faber ecosystem includes a standard library (Norma), a graphics and
geometry library (Triga), a utility library (coreutils), reader locale
packages, and a growing corpus of examples.

## Norma standard library {#norma}

Core modules for I/O, collections, strings, math, and system interaction.
[Read more →](/ecosystem/norma.html)

## Triga graphics and geometry {#triga}

Vector math, matrices, transforms, and GPU-friendly geometric types.
[Read more →](/ecosystem/triga.html)

## Coreutils {#coreutils}

Everyday utility functions built on Norma. Demonstrates idiomatic Faber.
[Read more →](/ecosystem/coreutils.html)

## Reader locale packages {#reader-locale-packages}

TOML packs that map Faber keywords, types, and diagnostics to natural
language surfaces. [Read more →](/ecosystem/reader-locale-packages.html)

## AI workbench {#ai-workbench}

Tooling for LLM-assisted Faber development, including agent skills and
the diagnostics contract. [Read more →](/ecosystem/ai-workbench.html)

## Language corpus {#corpus}

The example corpus — 154 directories, 292 `.fab` files covering every
keyword, operator, and type. The source of truth for generated pages.
[Read more →](/ecosystem/corpus.html)
