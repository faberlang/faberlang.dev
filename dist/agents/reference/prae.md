# prae

Angle-bracket generic parameters on functions and declarations.

**Term** `prae` · **Section** CONCEPTS

## Syntax

```
fn name<T>(...) | class Name<T, magnitudo N>
```

## What this teaches

- Type parameters — Functions and types can accept angle-bracket generic parameters like `<T>`.
- Magnitudo parameters — Compile-time integer parameters use the `size` keyword.

## Common mistakes

- Forgetting that `size` declares a compile-time integer generic parameter — regular types use bare `<T>` syntax.

## Grammar

```
genericParams :← '<' (ident | 'magnitudo' ident) (',' (ident | 'magnitudo' ident))* '>'
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only generic surface (whitelist: prae/prae.fab). Cross-ref: generic/generic.fab.
```

## Example

```fab
fn identitas<T>(T value) → T {
    return value
}

fn primum<T>(list<T> res) → T ∪ none {
    return res.first()
}
```

See also: [`type`](type.md), [`fn`](fn.md).

Fetch list: https://faberlang.dev/agents/index.md
