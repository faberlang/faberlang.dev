# Faber Language Reference Preview

Grammar, types, semantics.

Version: `__DOCS_VERSION__`.

Status: local reference draft. The grammar, keyword, and type contract routes
are quarantined in this packet; they are not approved syntax exports.

## Grammar

The grammar contract route for this packet is served at
`/contracts/__DOCS_VERSION__/grammar.ebnf`, but it is intentionally
quarantined. Use the local Faber toolchain (`faber parse`, `faber check`, and
`faber explain`) as the executable truth source for this private-preview packet.

Current file and declaration facts that are locally checked:

- **Package:** a collection of modules under a `faber.toml`.
- **Module file:** a `.fab` file.
- **Function keyword:** `functio`.
- **Return keyword:** `redde`.
- **Entrypoint keyword:** `incipit`.

## Types

The approved public type contract is not exported in this packet. A minimal
syntax-checked function shape is:

```faber
functio saluta(textus nomen) → textus {
    redde "salve"
}
```

See `/contracts/__DOCS_VERSION__/types.json` for the quarantined type-contract
placeholder.

## Functions

Function examples in this packet are parse-checked only. Do not infer full type
semantics or closure behavior from this local reference draft.

## Effects

Declarative effect route syntax appears in source, but provider route entries
are not published in this packet.

See `/docs/__DOCS_VERSION__/effects/index.md` for the current effect boundary.
This packet does not publish provider route entries or provider selection
rules.

## Constraints

- Do not treat quarantined contracts as approved syntax references.
- Do not invent syntax that `faber parse` or `faber check` does not accept.
- The local product-lane draft is Rust native binaries. Public wording still
  needs release evidence.
- Other targets may have syntax or emit support without runtime execution.

## Related

- `/contracts/__DOCS_VERSION__/grammar.ebnf` — quarantined grammar placeholder.
- `/contracts/__DOCS_VERSION__/keywords.json` — quarantined keyword placeholder.
- `/contracts/__DOCS_VERSION__/types.json` — quarantined type placeholder.
- `/contracts/__DOCS_VERSION__/operators.json` — operator precedence.
- `/docs/__DOCS_VERSION__/effects/index.md` — effect system and providers.
