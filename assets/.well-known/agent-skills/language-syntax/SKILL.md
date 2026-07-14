# Faber Language Syntax

Use this skill when you need to write, read, or validate Faber source code
syntax, types, or semantics.

Version: `__DOCS_VERSION__`.

## Use When

- Writing any `.fb` source file.
- Reading an unfamiliar `.fb` file.
- Type-matching or resolving declarations.
- Verifying syntax against the grammar contract.

## Canonical Choices

1. Prefer the draft **grammar contract** at
   `/contracts/__DOCS_VERSION__/grammar.ebnf`. Never invent productions not in
   the grammar.
2. Use `faber check` for immediate syntax and type validation.
3. Use `faber format` to canonicalize layout before reviewing.
4. Types are declared with `type Name = …`. Generics use `<T>`.
5. Functions use `fn name(args) -> RetType { … }`.
6. Effects are declared via the `ad` keyword and route to host providers.

## Key Constraints

- Do **not** invent syntax. If it is not in the grammar EBNF, it does not exist.
- Do **not** infer runtime behavior from emit-only target support.
- Do **not** assume Go/TypeScript syntax maps to Faber syntax.
- Variables are immutable by default.
- The local product-lane draft is Rust native binaries. Public wording still
  needs release evidence.

## Related Skills

- `packages` — layout, manifests, imports.
- `effects` — `ad` routing and providers.
- `diagnostics` — error codes and repair.

## Links

- `/docs/__DOCS_VERSION__/language/index.md`
- `/contracts/__DOCS_VERSION__/grammar.ebnf`
- `/contracts/__DOCS_VERSION__/keywords.json`
- `/contracts/__DOCS_VERSION__/types.json`
- `/contracts/__DOCS_VERSION__/operators.json`
