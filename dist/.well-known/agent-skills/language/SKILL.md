---
name: "language"
description: "Write and review Faber source: type-first declarations, Latin keywords, glyphs, nullability, comments, and HIR-as-truth."
---

# Faber language shape

## Use this skill when

- writing or reviewing `.fab` source
- translating an idea from another language into Faber
- explaining diagnostics or teaching the grammar signals

## Authority

Meaning lives in **HIR**. Keyword locales and codegen targets are renderings.
Do not privilege English-like syntax that does not exist in Faber.

## Signals (required)

| Signal | Rule |
|---|---|
| Type-first | `textus nomen`, `numerus x` — type before name |
| Functions | `functio name(params) → Ret { … }` |
| Bind | `←` |
| Equality | `≡` |
| Compact branch | `si cond ∴ body` |
| Return | `redde expr` |
| Nullable | `T ∪ nihil` |
| Comments | `#` on its own line only — never `//` |

## Minimal example

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## Anti-patterns

- Type-after-name (`nomen: textus`) as primary style
- `//` or `/* */` comments
- Inventing `?T` as the only nullability story without `∪ nihil`
- C-style `return` keyword instead of `redde`

## Canonical docs (English tree)

- Syntax hub: https://faberlang.dev/en-US/syntax/
- Types: https://faberlang.dev/en-US/syntax/types.html
- Functions: https://faberlang.dev/en-US/syntax/functions.html
- Nullability: https://faberlang.dev/en-US/syntax/nullability.html
- Glyphs: https://faberlang.dev/en-US/syntax/glyphs.html
- Features (Latin + glyphs): https://faberlang.dev/en-US/features/latin-and-glyphs.html
- Corpus lookup: https://faberlang.dev/en-US/corpus/
- Language portal: https://faberlang.dev/

## Related skills

- `packages`
- `corpus`
- `examples`
