# null

Null literal and nullable union bindings.

**Term** `null` · **Section** LITERALS

## Syntax

```
none
```

## What this teaches

- the `null` value (la `null`) — the sole value of the `none` type (la `none`)
- nullable union types with `∪` — `T ∪ none` (la `T ∪ none`) for values that may be absent
- null checks with `is none` and `not is none` (la `is none` / `not is none`)

## Common mistakes

- Storing `null` without declaring the type as `T ∪ none` — the null value requires a nullable union type.

## Grammar

```
literal :← 'null'
unionType :← type '∪' 'none'
```

## Expected output

```
nihil, verum, 42
```

## Backend

```
Cross-ref nihil/nihil.fab.
```

## Example

```fab
fn maybe() → int ∪ none {
    return 42
}

main {
    let int ∪ none absent ← null
    print absent
    let bool nihilne ← absent is none
    print nihilne
    print maybe() not is none
}
```

See also: [`∪`](∪.md), [`optional`](optional.md), [`none`](none.md).

Fetch list: https://faberlang.dev/agents/index.md
