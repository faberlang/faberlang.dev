+++
title = "Keyword reference"
section = "locales"
order = 1
sources = [
  "radix/locale/<locale>/pack.toml",
]
# This page is about the vocabulary itself; the reader-span pass would
# otherwise translate the reference it exists to show.
translate_spans = false
+++

Every Faber keyword, primitive type, and intrinsic has one pack key (a Latin spelling) and one spelling per reader pack. This page indexes the mapping pages generated from those packs; read any row across to translate one term.

English is the page language and a base surface: English keywords map to the English word, so its reader spelling is also what an English reader writes. Every mapping page therefore leads with the English column, and English carries no separate page. The Latin column is the pack key — the compiler's internal identity, one locale among eight rather than a privileged one: rendering to English and rendering to Thai are the same operation.

The full eight-pack join stays machine-facing at [/agents/locales.md](/agents/locales.md); rows the packs do not all declare are listed there, not on the human pages.

## Mapping pages {#pages}

| Page | Locale | Columns |
|---|---|---|
| [Latina (Latin)](/language/locales/la.html) | `la` | Latin · English |
| [العربية (Arabic)](/language/locales/ar.html) | `ar` | English · Latin · العربية |
| [हिन्दी (Hindi)](/language/locales/hi.html) | `hi` | English · Latin · हिन्दी |
| [ไทย (Thai)](/language/locales/th-TH.html) | `th-TH` | English · Latin · ไทย |
| [Tiếng Việt (Vietnamese)](/language/locales/vi.html) | `vi` | English · Latin · Tiếng Việt |
| [简体中文 (Simplified Chinese)](/language/locales/zh-Hans.html) | `zh-Hans` | English · Latin · 简体中文 |
| [繁體中文 (Traditional Chinese)](/language/locales/zh-Hant.html) | `zh-Hant` | English · Latin · 繁體中文 |
| [Diagnostics by locale](/language/locales/diagnostics.html) | — | one failure, every pack |
| [Locale examples](/language/locales/examples.html) | — | one program, eight surfaces |

The tables on those pages are generated from the packs themselves and cannot drift from the compiler by hand. A blank cell is a pack that declares no spelling for that term.

The eight installed packs:

| Code | Native name | Script | Direction |
|---|---|---|---|
| `en` | English | Latin | left-to-right |
| `la` | Latina | Latin | left-to-right |
| `ar` | العربية | Arabic | right-to-left |
| `hi` | हिन्दी | Devanagari | left-to-right |
| `th-TH` | ไทย | Thai | left-to-right |
| `vi` | Tiếng Việt | Latin (Vietnamese) | left-to-right |
| `zh-Hans` | 简体中文 | Han (Simplified) | left-to-right |
| `zh-Hant` | 繁體中文 | Han (Traditional) | left-to-right |

---

[All reader locales](/language/reader-locales.html)
