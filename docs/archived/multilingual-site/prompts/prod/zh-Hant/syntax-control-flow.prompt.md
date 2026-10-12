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

## Conditional branching {#conditional-branching}

### si / sin / secus {#si-sin-secus}

<<<FENCE 0>>>

With else-if and else:

<<<FENCE 1>>>

### Compact branch with ∴ {#compact-branch-with}

A single-statement branch body uses `∴` (or its alias `ergo`):

<<<FENCE 2>>>

## Iteration {#iteration}

### Values — itera ex {#values-itera-ex}

<<<FENCE 3>>>

### Keys — itera de {#keys-itera-de}

<<<FENCE 4>>>

### Range — itera ab {#range-itera-ab}

<<<FENCE 5>>>

## While loops {#while-loops}

<<<FENCE 6>>>

## Guard sections — custodi {#guard-sections-custodi}

`custodi` groups early-exit checks before a function's main body.
Each `si` clause is a sequential guard:

<<<FENCE 7>>>

`custodi` is not breakable in v1 — it is a guard rail, not a loop.

## Pattern matching — elige {#pattern-matching-elige}

`elige` selects the first matching arm:

<<<FENCE 8>>>

## Tagged union matching — discerne {#tagged-union-matching-discerne}

`discerne` exhaustively matches `discretio` variants:

<<<FENCE 9>>>

## Try blocks — fac / cape {#try-blocks-fac-cape}

`fac` opens a block that may throw, and `cape` recovers:

<<<FENCE 10>>>
