# Faber Language Syntax

Use this skill when you need to write, read, or validate Faber source code
syntax, types, or semantics.

Version: `__DOCS_VERSION__`.

## Use When

- Writing any `.fab` source file.
- Reading an unfamiliar `.fab` file.
- Type-matching or resolving declarations.
- Verifying syntax against the local Faber toolchain.

## Canonical Choices

1. Treat `/contracts/__DOCS_VERSION__/grammar.ebnf` as a quarantined
   placeholder, not as syntax authority.
2. Use `faber check` for immediate syntax and type validation.
3. Use `faber format` to canonicalize layout before reviewing.
4. Use `faber parse`, `faber check`, and `faber explain` for executable syntax truth.
5. Current function examples use `functio`, lowercase type names such as
   `textus`, and the `redde` return keyword.
6. Provider route syntax is not a public support claim while route entries are
   empty.

## Key Constraints

- Do **not** invent syntax that `faber parse` or `faber check` rejects.
- Do **not** infer runtime behavior from emit-only target support.
- Do **not** assume Go/TypeScript syntax maps to Faber syntax.
- Variables are immutable by default.
- Do **not** infer provider routing from `ad` syntax; provider route entries
  are not published in this packet.
- The local product-lane draft is Rust native binaries. Public wording still
  needs release evidence.

## Related Skills

- `packages` — layout, manifests, imports.
- `effects` — `ad` source shape and provider-route claim boundary.
- `diagnostics` — error codes and repair.

## Links

- `/docs/__DOCS_VERSION__/language/index.md`
- `/contracts/__DOCS_VERSION__/grammar.ebnf` — quarantined placeholder
- `/contracts/__DOCS_VERSION__/keywords.json` — quarantined placeholder
- `/contracts/__DOCS_VERSION__/types.json` — quarantined placeholder
- `/contracts/__DOCS_VERSION__/operators.json`
