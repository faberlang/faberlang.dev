# readonly

Marks a function as non-mutating.

**Term** `immutata` · **Section** KEYWORDS

## Syntax

```
fn <name>(...) readonly → <type>
```

## What this teaches

- Marks a function as non-mutating.
- Related keywords: throws

## Common mistakes

- Mutating state inside an `readonly` function — `readonly` is a non-mutation contract; modifying `mut` parameters or external state breaks the contract.

## Grammar

```
funcModifier :← 'immutata'
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only function modifier (whitelist: immutata/immutata.fab).
```

## Example

```fab
fn inspecta() readonly → int {
    return 0
}
```

See also: [`throws`](throws.md).

Fetch list: https://faberlang.dev/agents/index.md
