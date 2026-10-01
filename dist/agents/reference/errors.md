# errors

Marks a function parameter or binding as carrying an error value.

**Term** `errata` · **Section** KEYWORDS

## Syntax

```
fn <name>(...) errors <ident> → <type>
```

## What this teaches

- Error channel parameter — `errors <type>` marks a function as having a typed error channel, enabling structured error handling.
- Declaration-only — currently a declaration-only modifier; the error channel is whitelisted for syntax validation and future codegen.

## Common mistakes

- Confusing errors with a ⊥ default — `errors` declares a typed error parameter on a function; `⊥` provides an inline default on conversion.

## Grammar

```
funcModifier :← 'errata' type
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only error channel (whitelist: errata/errata.fab).
```

## Example

```fab
fn parse(string raw) errors string → int {
    return 0
}
```

See also: [`⇥`](⇥.md), [`catch`](catch.md), [`throw`](throw.md).

Fetch list: https://faberlang.dev/agents/index.md
