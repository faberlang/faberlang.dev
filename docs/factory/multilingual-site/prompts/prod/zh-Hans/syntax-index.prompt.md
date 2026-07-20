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

Faber syntax is built on three principles: types before names, Latin
words for behaviour, and structural glyphs for value flow. Every
declaration reads as intent first, mechanism second.

## Data types {#types}

Type-first declarations, numeric widths, tensors, lists, and GPU core
types. [Read more →](/syntax/types.html)

## Variables {#variables}

Bindings use `←` for value flow. Mutability is explicit through `varia`.
[Read more →](/syntax/variables.html)

## Functions {#functions}

Functions declare parameter types before names. Return types follow the
arrow. [Read more →](/syntax/functions.html)

## Control flow {#control-flow}

`si`/`ceterum` for branching, `dum` for iteration, `perge`/`rumpe` for
loop control. [Read more →](/syntax/control-flow.html)

## Errors {#errors}

Errors are typed values, not exceptions. The `aut` type carries success
or failure. [Read more →](/syntax/errors.html)

## Generics {#generics}

Type parameters on functions and structures. Constraints through trait
bounds. [Read more →](/syntax/generics.html)

## Collections {#collections}

Lists (`lista`), maps, and tensors for structured data.
[Read more →](/syntax/collections.html)

## Strings {#strings}

The `textus` type, template literals, and string operations.
[Read more →](/syntax/strings.html)

## Conversion {#conversion}

The `conversio` system for explicit type conversions.
[Read more →](/syntax/conversion.html)

## Glyphs {#glyphs}

Structural glyph reference: `←`, `→`, `‥`, `≡`, `≢`, and more.
[Read more →](/syntax/glyphs.html)

## Nullability {#nullability}

Absence is typed. The `forsitan` type and nullable annotations.
[Read more →](/syntax/nullability.html)
