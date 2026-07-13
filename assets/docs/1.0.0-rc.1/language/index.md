# Faber Language Reference

Grammar, types, semantics.

Version: `__DOCS_VERSION__`.

## Grammar

The authoritative Faber grammar is published as a machine-readable EBNF contract
at `/contracts/__DOCS_VERSION__/grammar.ebnf`.

Key productions:

- **Package:** a collection of modules under a `faber.toml`.
- **Module:** a `.fb` file containing declarations.
- **Declaration:** `type`, `fn`, `import`, `ad`, or annotation.
- **Expression:** literal, variable, call, lambda, match, block.
- **Type:** primitive, generic, nominal, effect, or union.

## Types

Faber is statically typed with generics. Types are declared with `type`:

```
type Point = { x: Int, y: Int }
```

Builtin types include `Int`, `Float`, `String`, `Bool`, `List<T>`, and `Map<K,V>`.

See `/contracts/__DOCS_VERSION__/types.json` for the complete type contract.

## Functions

```
fn add(a: Int, b: Int) -> Int {
    a + b
}
```

Functions are first-class values. Closures capture their environment by
reference when the compiler can prove safety.

## Effects

Declarative effects use the `ad` keyword and route to host providers:

```
ad ConsoleWrite(msg: String)
```

See `/docs/__DOCS_VERSION__/effects/index.md` for the complete effect reference.

## Constraints

- Variables are immutable by default. Use `var` for mutable bindings.
- Do not invent syntax not in the grammar. If a production is absent, it does
  not exist.
- The supported product lane is Rust native binaries. Other targets may have
  syntax support but lack runtime execution.

## Related

- `/contracts/__DOCS_VERSION__/grammar.ebnf` — authoritative grammar.
- `/contracts/__DOCS_VERSION__/keywords.json` — reserved words.
- `/contracts/__DOCS_VERSION__/types.json` — type system contract.
- `/contracts/__DOCS_VERSION__/operators.json` — operator precedence.
- `/docs/__DOCS_VERSION__/effects/index.md` — effect system and providers.
