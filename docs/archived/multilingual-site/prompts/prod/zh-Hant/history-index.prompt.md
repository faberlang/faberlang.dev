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

## Origins {#origins}

The first commit to the Radix compiler was made on **December 20, 2024**
as a Bun + TypeScript project with a single `docs/decisions.md` file. The
second commit codified five Architecture Decision Records that still shape
the language today.

**ADR-003**, titled "Case endings carry semantic meaning," established at
the very beginning that Latin morphology would be more than a
keyword-skin — the compiler would understand declension and conjugation
to infer program intent. The original case mappings were:

<<<FENCE 0>>>

The same document noted: *"Verb conjugation is a natural follow-on
question (future tense → async?)."* This seed grew into the modern
**morphologia** naming convention, where the standard library uses
conjugated Latin verb forms to signal sync vs async and mutate vs
copy-out — without requiring the compiler itself to understand Latin
grammar.

The project began in TypeScript, was later rewritten in Rust, and the
grammar was frozen for the 1.x line with edition 2026. The original five
ADRs (file extension `.fab`, error hints, case endings, recursive descent
parser, custom AST) are still visible in the git history.

## Releases {#releases}

Prebuilt CLI archives — current Faber release at the top, then every published
tag and binary from [faberlang/releases](https://github.com/faberlang/releases):

- **[Releases](/history/releases.html)** — download links and historical inventory
- **[Install and download](/start/install.html)** — PATH setup and first `faber check`
