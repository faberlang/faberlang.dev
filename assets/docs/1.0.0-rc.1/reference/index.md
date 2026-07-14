# Faber Reference

Version: `__DOCS_VERSION__`.

Status: local reference draft. The final public reference should be sourced
from the same corpus intended for in-tool language explanation.

## Current Contract Surfaces

| Contract | Route |
| --- | --- |
| Grammar | `/contracts/__DOCS_VERSION__/grammar.ebnf` (quarantined placeholder) |
| Keywords | `/contracts/__DOCS_VERSION__/keywords.json` (quarantined placeholder) |
| Types | `/contracts/__DOCS_VERSION__/types.json` (quarantined placeholder) |
| Operators | `/contracts/__DOCS_VERSION__/operators.json` |
| Diagnostics | `/contracts/__DOCS_VERSION__/diagnostics.json` |
| Target capabilities | `/contracts/__DOCS_VERSION__/targets.json` |

## Reference Rules

- Prefer versioned routes.
- Treat empty or placeholder contract fields as export blockers, not evidence.
- Do not use quarantined grammar, keyword, or type placeholders as syntax
  authority.
- Use `faber parse`, `faber check`, and `faber explain` as the local
  executable truth source for this private-preview packet.
- Keep examples close to their diagnostics or grammar rules.
- Keep package, target, and external-project reference material separate from
  the core language reference.

## Public Gate

Before publication, the public contract export must replace placeholders,
document digests must be real, and the reference must pass drift checks against
the tool-facing corpus.
