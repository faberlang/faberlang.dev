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

Reader locale is Faber's system for rendering source code, compiler diagnostics,
and language keywords in the reader's human language — without forking the
semantics. A Thai programmer can read and write Faber source with Thai keywords,
receive compiler errors in Thai, and collaborate through the same HIR as a Latin
or Chinese user. The mechanism that localises code from Latin to Thai is the
same mechanism that emits code to Rust: `HIR → surface` — neither is
privileged.

## Problem {#problem}

Large language models have localised the **conversation** around programming —
a Thai computer scientist can ask an LLM for help in Thai — but not the durable
**artifact**. The generated code, APIs, compiler errors, and documentation
remain English-shaped. English proficiency becomes a gate to computer science,
not merely to conversation.

Reader locale is the design response: the language a human uses to *understand*
Faber — source, diagnostics, and optionally stdlib spellings — without English as
a prerequisite. It is not application internationalisation (complete string-matrix
coverage). It is reader dialect support: opt-in, partial packs over a semantic core
that does not fork.

> **Product thesis:** English should not be the required review language for
> software intent. LLMs have localised the conversation around programming;
> reader locale localises the durable artifact.

## How it works {#how}

A reader-locale pack maps Faber keywords, primitive type spellings, and
diagnostic templates into a target language. Packs are TOML files with three
tables:

- `[keywords]` — maps keyword names to their localised spellings
- `[types]` — maps primitive type names to localised spellings
- `[diagnostics.*]` — maps diagnostic codes to localised message templates
- `[llm]` — system prompt snippets and exemplars for LLM code generation

The compiler validates packs against a generated Latin scaffold — every keyword
and type must have a defined spelling or explicitly inherit from Latin.
Missing rows produce visible fallback rather than silent gaps.

Select a locale at the command line or in `faber.toml`:

<<<FENCE 0>>>

<<<FENCE 1>>>

### What localises and what does not {#what-localises}

| Layer | In the HIR? | Behaviour |
|---|---|---|
| Keywords, types, paired phrases | Yes | Lossless across all renderings |
| Glyphs `← → ∴ ≡ ∪ ⇥` | Yes (invariant) | Identical in every rendering |
| Type-first structure | Yes | Identical in every rendering |
| Numerals | — | ASCII only in all locales |
| Comments | No | Out of compiler scope; LLM-mediated, opt-in |
| Identifier names | No | Preserved byte-for-byte |
| Stdlib spellings | No | Per-locale overlay |

The critical architectural guarantee: any locale surface can become any other,
including Latin, at any time. A localised Faber file is never a trap because
it is never the only form the code can take. `faber format --canonical`
is exactly `faber format --reader-locale=la`.

## Shipped packs {#locales}

Seven packs ship with Radix today:

| Code | Language | Script | Status |
|---|---|---|---|
| `la` | Latina (Latin) | Latin | **Canonical** |
| `th-TH` | ไทย | Thai | **Reference proof** |
| `zh-Hans` | 简体中文 | Simplified Chinese | Coverage proof |
| `zh-Hant` | 繁體中文 | Traditional Chinese | Coverage proof |
| `ar` | العربية | Arabic | Coverage proof |
| `hi` | हिन्दी | Devanagari | Coverage proof |
| `vi` | Tiếng Việt | Vietnamese (Latin) | Coverage proof |

The five reference locales are chosen for **collective architectural
stress** — together they force every Unicode and emission problem the substrate
must survive. Four use non-Latin scripts; Vietnamese is the Latin-script
control case:

| Locale | Access | Architectural stress |
|---|---|---|
| `th-TH` | High | Spaceless script — the tokeniser stress test |
| `zh-Hans` / `zh-Hant` | Very high | Paired keywords; sibling pack inheritance; NFKC width collapse |
| `ar` | High | Right-to-left; bidi isolation in diagnostics |
| `hi` | Very high | Matra/virama clusters; Indic numerals |
| `vi` | High | Heavy diacritics on Latin script; NFKC edge cases |

*The reference set is chosen for architectural coverage, not population. Population alone would prove nothing the substrate did not already handle.*

## Localised source examples {#examples}

Each of the six non-canonical locales has a complete Faber package under
`examples/reader-locale/` with localised source, diagnostic test
cases, and a `faber.toml` manifest. The same `greet`
program rendered across all shipped locales:

**Latin** `la` — *canonical*

<<<FENCE 2>>>

The canonical rendering. `faber format --canonical` is exactly
`faber format --reader-locale=la`. Latin keywords map to themselves;
type names are the canonical spellings.

**ไทย** `th-TH` — *reference proof*

<<<FENCE 3>>>

The access-wedge proof. Thai is a spaceless script — no inter-word boundaries —
making it the tokeniser stress test and the original architectural driver for
the reader-locale system. Every token boundary must be resolved by the lexer
through keyword matching alone.

**简体中文** `zh-Hans`

<<<FENCE 4>>>

Paired keywords (如果/否则 for si/secus) requiring pack keyword groups;
full/half-width punctuation; NFKC width collapse at lex entry. The hardest
LLM emission case due to CJK tokeniser boundaries. A sibling pack for
Traditional Chinese (zh-Hant) inherits and overrides zh-Hans roots.

**العربية** `ar`

<<<FENCE 5>>>

Right-to-left script embedded inside a logical-order LTR code block. Keywords
are wrapped in `<bdi>` (bidirectional isolation) in the
compiler's HTML diagnostic output to prevent RFO (right-follows-left)
distortion. The raw source uses Arabic script in logical order; the display
layer handles bidi presentation.

**हिन्दी** `hi`

<<<FENCE 6>>>

Devanagari script with matra/virama consonant clusters. Proves the path for
the wider Indic family — Bengali, Tamil, Telugu inherit the same shaping
infrastructure — though pack authoring for each remains separate work.
Indic numeral glyphs (०-९) are not accepted in numeric literals; ASCII
digits are preserved across all locales.

**Tiếng Việt** `vi`

<<<FENCE 7>>>

The control case: Latin-script but not English. Heavy diacritic load (ế, ệ, ả)
stresses NFKC edge cases in the lexer. Prevents an architecture that works on
exotic scripts but is unproven on Latin-with-diacritics. Identifiers use
Vietnamese words (chào, tên, lời_chào, thông_điệp), preserved byte-for-byte
by the compiler.

> The glyphs (`← → ∴ ≡ ∪ ⇥`),
> structural positions, and identifier names are **identical** across all six
> renderings above. Only the keywords and type names change. The HIR is exactly
> the same program — the compiler treats all six as equivalent. Rendering Faber
> to Thai is the same compiler operation as rendering it to Rust:
> `HIR → surface`, with neither privileged.

## Localised diagnostics {#diagnostics}

Diagnostics are **structured facts before prose**. Each diagnostic carries a
stable code (`LEX###`, `PARSE###`, `SEM###`,
`WARN###`) and named arguments; the pack owns the rendered template
text. This means the diagnostic renderer can emit messages in any locale without
changing the diagnostic infrastructure.

The reader-locale example packages include diagnostic test cases — type mismatches,
undefined variables, non-ASCII numbers — proving the full pipeline is locale-aware:

- `examples/reader-locale/vi/src/type-mismatch.fab`
- `examples/reader-locale/vi/src/undefined-variable.fab`
- `examples/reader-locale/vi/src/non-ascii-number.fab`
- `examples/reader-locale/vi/src/keyword-suggestion.fab`
- `examples/reader-locale/vi/src/keyword-edit-distance.fab`

Bidi isolation is built in: Arabic keywords inside logical-order LTR code blocks
are wrapped in `<bdi>` elements in HTML output, preventing the
RFO (right-follows-left) distortion that would otherwise make RTL runs unreadable.

## Status {#status}

| Layer | Status |
|---|---|
| Pack schema, aliases, inheritance, validation, diagnostics, LLM artifacts | **Shipped** |
| Pack-aware lexing, type resolution, manifest/CLI selection, visible fallback | **Shipped** |
| Pack-owned diagnostic rendering, `faber explain`, bidi-isolated display | **Shipped** |
| Canonical Faber formatting | **Shipped** |
| Localised Faber re-emission (`format --reader-locale`) | Partial |
| Stdlib gloss overlays, measured LLM emission fidelity, complete locale coverage | Deferred |
| Multilingual documentation generation | Proposed |

The substrate prerequisite — NFKC normalisation at lex entry — has landed.
Keyword tables, diagnostic named-args, the renderer, and pack delivery are
shipped. The north-star layers (localised re-emission, stdlib glosses, LLM
emission benchmarks, generated multilingual docs) remain explicitly partial
or deferred.

## References {#references}

1. `radix/docs/design/reader-locale.md` — full design document (69 KB)
2. `examples/reader-locale/` — 6 locale packages with localised source
3. `stdlib/reader/*/pack.toml` — 7 installed pack definitions
4. `radix/crates/radix/src/reader_locale.rs` — runtime implementation
5. `radix/docs/design/faber-canonical-surface.md` — canonical mode and `faber format`
6. `radix/docs/factory/lex-nfkc-normalization/` — NFKC prerequisite delivery
