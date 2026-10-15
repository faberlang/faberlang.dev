+++
title = "Reader locales"
section = "locales"
order = 6
sources = [
  "examples/reader-locale/ (6 locale packages with localized Faber source)",
  "locale/ (8 installed reader packs)",
]
+++

Reader locale is a property of the compiler, not a translation of this site.
English is the one maintained prose language; a reader locale changes the
**code surface** — the keywords, type names, and diagnostic text the compiler
reads and writes. The retired `/{locale}/` URL trees redirect here and to the
English pages. This page is the hub of that feature; the pages below carry the
reference data.

| Page | What it holds |
|---|---|
| [Keyword reference](/language/locales/keywords.html) | index of the per-language mapping pages, plus the pack legend |
| [Locale examples](/language/locales/examples.html) | one program shown in all eight surfaces |
| [Diagnostics by locale](/language/locales/diagnostics.html) | one compiler failure printed in each language |
| [Latin](/language/locales/la.html) · [العربية](/language/locales/ar.html) · [हिन्दी](/language/locales/hi.html) · [ไทย](/language/locales/th-TH.html) · [Tiếng Việt](/language/locales/vi.html) · [简体中文](/language/locales/zh-Hans.html) · [繁體中文](/language/locales/zh-Hant.html) | per-language mapping (English \| Latin \| language), native name, and script notes |

The reference tables are generated from the eight reader packs themselves, so
they cannot drift from the compiler by hand.

## Reader locale

Reader locale is Faber's system for rendering source code, compiler diagnostics,
and language keywords in the reader's human language — without forking the
semantics. A Thai programmer can read and write Faber source with Thai keywords,
receive compiler errors in Thai, and collaborate through the same HIR as a Latin
or Chinese user. The mechanism that localises code from Latin to Thai is the
same mechanism that emits code to Rust: `HIR → surface` — neither is
privileged.

### Problem {#problem}

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

### How it works {#how}

A reader-locale pack maps Faber keywords, primitive type spellings, and
diagnostic templates into a target language. Packs are TOML files; the tables
that carry the vocabulary are:

- `[keywords]` — maps keyword names to their localised spellings
- `[types]` — maps primitive type names to localised spellings
- `[diagnostics.*]` — maps diagnostic codes to localised message templates
- `[llm]` — system prompt snippets and exemplars for LLM code generation

The compiler validates packs against a generated Latin scaffold — every keyword
and type must have a defined spelling or explicitly inherit from Latin.
Missing rows produce visible fallback rather than silent gaps.

Select a locale at the command line or in `faber.toml`:

```text
faber check --locale th-TH program.fab
```

```toml
# faber.toml
[locale]
locale = "zh-Hans"
```

The message language for diagnostics is independent of the code locale and is
selected with `--diagnostics-locale <locale>`.

#### What localises and what does not {#what-localises}

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
it is never the only form the code can take. `faber convert --to la`
re-emits a file on the Latin surface.

### Shipped packs {#locales}

Eight packs ship with the compiler today:

| Code | Language | Script | Status |
|---|---|---|---|
| `en` | English | Latin | **Base surface** |
| `la` | Latina (Latin) | Latin | **Identity pack** |
| `th-TH` | ไทย | Thai | **Reference proof** |
| `zh-Hans` | 简体中文 | Simplified Chinese | Coverage proof |
| `zh-Hant` | 繁體中文 | Traditional Chinese | Coverage proof |
| `ar` | العربية | Arabic | Coverage proof |
| `hi` | हिन्दी | Devanagari | Coverage proof |
| `vi` | Tiếng Việt | Vietnamese (Latin) | Coverage proof |

`en` is the English reader surface — English keywords map to themselves,
like `la` maps Latin to itself — and was renamed from the old `llm` pack in
the 2026-08 locale rename. The reference locales below remain the
**collective architectural stress** set; `en` and `la` do not stress the
substrate because they are the base surfaces:

| Locale | Access | Architectural stress |
|---|---|---|
| `th-TH` | High | Spaceless script — the tokeniser stress test |
| `zh-Hans` / `zh-Hant` | Very high | Paired keywords; sibling pack inheritance; NFKC width collapse |
| `ar` | High | Right-to-left; bidi isolation in diagnostics |
| `hi` | Very high | Matra/virama clusters; Indic numerals |
| `vi` | High | Heavy diacritics on Latin script; NFKC edge cases |

*The reference set is chosen for architectural coverage, not population. Population alone would prove nothing the substrate did not already handle.*

### Localised source examples {#examples}

Each of the six reference locales has a complete Faber package under
`examples/reader-locale/` with localised source, diagnostic test
cases, and a `faber.toml` manifest. The same program rendered in the two
base surfaces — English (this page's reader locale) and Latin —
then the six packaged locale surfaces below:

**English** `en` — *base surface*

```faber
functio salve(textus nomen) → textus {
    sit textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    sit textus m ← salve("munde")
    nota m
}
```

The surface an English reader writes: `fn`, `let`, `string`, `return`,
`main`, `print` — the spellings every page on this site teaches.

**Latin** `la` — *identity pack*

```faber locale=la
functio salve(textus nomen) → textus {
    sit textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    sit textus m ← salve("munde")
    nota m
}
```

The identity pack: its words are the pack keys, so Latin keywords map to
themselves. `faber convert --to la` re-emits a file on this surface.

**ไทย** `th-TH` — *reference proof*

```text
ฟังก์ชัน salve(ข้อความ nomen) → ข้อความ {
    คงที่ ข้อความ msg ← "Salve, §!"(nomen)
    คืน msg
}

เริ่ม {
    คงที่ ข้อความ m ← salve("munde")
    บันทึก m
}
```

The access-wedge proof. Thai is a spaceless script — no inter-word boundaries —
making it the tokeniser stress test and the original architectural driver for
the reader-locale system. Every token boundary must be resolved by the lexer
through keyword matching alone.

**简体中文** `zh-Hans`

```text
函数 salve(文本 nomen) → 文本 {
    常量 文本 msg ← "Salve, §!"(nomen)
    返回 msg
}

入口 {
    常量 文本 m ← salve("munde")
    显示 m
}
```

Paired keywords (如果/否则 for si/secus) requiring pack keyword groups;
full/half-width punctuation; NFKC width collapse at lex entry. The hardest
LLM emission case due to CJK tokeniser boundaries. A sibling pack for
Traditional Chinese (zh-Hant) inherits and overrides zh-Hans roots.

**العربية** `ar`

```text
دالة salve(نص nomen) → نص {
    ثابت نص msg ← "Salve, §!"(nomen)
    أعد msg
}

بداية {
    ثابت نص m ← salve("munde")
    اعرض m
}
```

Right-to-left script embedded inside a logical-order LTR code block. Keywords
are wrapped in `<bdi>` (bidirectional isolation) in the
compiler's HTML diagnostic output to prevent RFO (right-follows-left)
distortion. The raw source uses Arabic script in logical order; the display
layer handles bidi presentation.

**हिन्दी** `hi`

```text
फलन salve(पाठ nomen) → पाठ {
    स्थिर पाठ msg ← "Salve, §!"(nomen)
    लौटाओ msg
}

आरंभ {
    स्थिर पाठ m ← salve("munde")
    दिखाओ m
}
```

Devanagari script with matra/virama consonant clusters. Proves the path for
the wider Indic family — Bengali, Tamil, Telugu inherit the same shaping
infrastructure — though pack authoring for each remains separate work.
Indic numeral glyphs (०-९) are not accepted in numeric literals; ASCII
digits are preserved across all locales.

**Tiếng Việt** `vi`

```text
hàm salve(văn_bản nomen) → văn_bản {
    hằng văn_bản msg ← "Salve, §!"(nomen)
    trả msg
}

bắt_đầu {
    hằng văn_bản m ← salve("munde")
    ghi_chú m
}
```

The control case: Latin-script but not English. Heavy diacritic load (ế, ệ, ả)
stresses NFKC edge cases in the lexer. Prevents an architecture that works on
exotic scripts but is unproven on Latin-with-diacritics. Identifiers, including
ones written in Vietnamese, are preserved byte-for-byte by the compiler.

> The glyphs (`← → ∴ ≡ ∪ ⇥`),
> structural positions, and identifier names are **identical** across all six
> renderings above. Only the keywords and type names change. The HIR is exactly
> the same program — the compiler treats all six as equivalent. Rendering Faber
> to Thai is the same compiler operation as rendering it to Rust:
> `HIR → surface`, with neither privileged.

### Localised diagnostics {#diagnostics}

Diagnostics are **structured facts before prose**. Each diagnostic carries a
stable code (`LEX###`, `LOCALE###`, `PARSE###`, `SEM###`,
`WARN###`) and named arguments; the pack owns the rendered template
text. This means the diagnostic renderer can emit messages in any locale without
changing the diagnostic infrastructure.

The reader-locale example packages include diagnostic test cases — type mismatches,
undefined variables, non-ASCII numbers — proving the full pipeline is locale-aware:

- `examples/reader-locale/vi/faults/type-mismatch.fab`
- `examples/reader-locale/vi/faults/undefined-variable.fab`
- `examples/reader-locale/vi/faults/non-ascii-number.fab`
- `examples/reader-locale/vi/faults/keyword-suggestion.fab`
- `examples/reader-locale/vi/faults/keyword-edit-distance.fab`

Bidi isolation is built in: Arabic keywords inside logical-order LTR code blocks
are wrapped in `<bdi>` elements in HTML output, preventing the
RFO (right-follows-left) distortion that would otherwise make RTL runs unreadable.

### Status {#status}

| Layer | Status |
|---|---|
| Pack schema, aliases, inheritance, validation, diagnostics, LLM artifacts | **Shipped** |
| Pack-aware lexing, type resolution, manifest/CLI selection, visible fallback | **Shipped** |
| Pack-owned diagnostic rendering, `faber explain`, bidi-isolated display | **Shipped** |
| Faber formatting (`faber format`) | **Shipped** |
| Localised Faber re-emission (`convert --to <locale>`) | **Shipped** |
| Stdlib gloss overlays, measured LLM emission fidelity, complete locale coverage | Deferred |
| Multilingual documentation generation | Proposed |

The substrate prerequisite — NFKC normalisation at lex entry — has landed.
Keyword tables, diagnostic named-args, the renderer, and pack delivery are
shipped. The north-star layers (localised re-emission, stdlib glosses, LLM
emission benchmarks, generated multilingual docs) remain explicitly partial
or deferred.

### References {#references}

1. `docs/design/reader-locale.md` — full design document
2. `examples/reader-locale/` — 6 locale packages with localised source
3. `locale/*/pack.toml` — 8 installed pack definitions
4. `crates/radix-module/src/locale.rs` — runtime implementation
5. `docs/design/faber-canonical-surface.md` — the formatter and the re-emitter
6. `radix/docs/archived/lex-nfkc-normalization/` — NFKC prerequisite delivery

## Reader-locale packages

Each non-Latin reader locale has a complete Faber package under
`examples/reader-locale/` with localised source, diagnostic test cases,
and a `faber.toml` manifest.

### Available packages {#available-packages}

| Locale | Path | Source example |
|--------|------|---------------|
| th-TH | `examples/reader-locale/th-TH/` | `ฟังก์ชัน salve(ข้อความ nomen) → ข้อความ` |
| zh-Hans | `examples/reader-locale/zh-Hans/` | `函数 salve(文本 nomen) → 文本` |
| zh-Hant | `examples/reader-locale/zh-Hant/` | `函式 salve(文字 nomen) → 文字` |
| ar | `examples/reader-locale/ar/` | `دالة salve(نص nomen) → نص` |
| hi | `examples/reader-locale/hi/` | `फलन salve(पाठ nomen) → पाठ` |
| vi | `examples/reader-locale/vi/` | `hàm salve(văn_bản nomen) → văn_bản` |

### Diagnostic test cases {#diagnostic-test-cases}

Each package includes test cases proving the full compiler pipeline is
locale-aware:

- `type-mismatch.fab` — localised type error diagnostics
- `undefined-variable.fab` — localised name resolution errors
- `non-ascii-number.fab` — NFKC handling
- `keyword-suggestion.fab` — localised "did you mean?" hints
