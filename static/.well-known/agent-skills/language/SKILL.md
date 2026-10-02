---
name: "language"
description: "Write Faber in the English reader spelling. Start at the agent canon and follow its links."
---

# Faber language shape

## Use this skill when

- writing or reviewing `.fab` source
- translating an idea from another language into Faber
- explaining a diagnostic

## Authority

Fetch https://faberlang.dev/agents/index.md and follow only the links that page names. Those pages are the writing guide. The programs there are English.

Meaning lives in HIR. A reader locale is a rendering of that core. One source file uses one pack.

## Signals

| Signal | Rule |
|---|---|
| Type-first | `string name`, `int n` |
| Functions | `fn name(int a) → int` |
| Bind | `←` |
| Equality | `≡` |
| Return | `return` |
| Nullable | `int ∪ none`, and the missing value is `null` |
| Comments | a `#` line by itself |

## Do not write

- `name: T`
- `int?`
- `//`
- a `#` after code on the same line

## Programs

- https://faberlang.dev/agents/program.md
- https://faberlang.dev/agents/functions.md
- https://faberlang.dev/agents/types.md
- https://faberlang.dev/agents/errors.md
- https://faberlang.dev/agents/grammar.md

## Related

- skill: `packages`
- skill: `corpus`
- https://faberlang.dev/install.md
