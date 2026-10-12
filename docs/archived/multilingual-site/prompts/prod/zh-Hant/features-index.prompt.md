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

Faber's design rests on three signal choices: type-first declarations,
Latin behavioural vocabulary, and structural glyphs. These features
compound — each one reinforces the others to produce source that is
readable, checkable, and portable across execution lanes.

## Reader locale {#reader-locale}

The compiler is the translator. Reader locale packs allow the same
source to render in multiple natural languages without changing
semantics. [Read more →](/features/reader-locale.html)

## Compilation lanes {#compilation-lanes}

Faber lowers through three intermediate representations (HIR, MIR, AIR)
to multiple target backends including Rust runtime, WASM, TypeScript,
Go, and GPU/WGSL. [Read more →](/features/compilation-lanes.html)

## Latin vocabulary and glyphs {#latin-and-glyphs}

Types come before names. Latin words carry behaviour. Structural glyphs
carry value flow and type shape. The result reads like intent, not
mechanism. [Read more →](/features/latin-and-glyphs.html)

## Commandments {#commandments}

Nine design laws govern every language decision, from keyword choice to
error handling. These are the review criteria for new features.
[Read more →](/features/commandments.html)

## Canonical vs sugar {#canonical-vs-sugar}

Every sugar surface has a canonical expansion. The formatter can move
between them. Sugar is convenience; canonical is the contract.
[Read more →](/features/canonical-vs-sugar.html)

## Capability calls and frames {#frames}

The `ad` primitive provides capability-based dispatch. Frame types
define the I/O boundary between Faber code and host providers.
[Read more →](/features/frames.html)

## Inline testing {#testing}

Test suites live alongside source code using three keywords:
`probandum`, `proba`, and `adfirma`. No separate test binary needed.
[Read more →](/features/testing.html)
