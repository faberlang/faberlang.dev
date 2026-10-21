# none

The absent-member type: none (la none) is the type, null (la null) is its value.

**Term** `nihil` · **Section** KEYWORDS

## Syntax

```
T ∪ none | null
```

## What this teaches

- the type — `none` (la `none`) is the absent member of a nullable union `T ∪ none` (la `T ∪ none`)
- the value — `null` (la `null`) is the null value; `none` is never a value (SEM001 name_not_value)
- the check — `x is none` (la `is none`) tests the none type; `is` with the `null` value literal is refused (PARSE040 est_value_literal_names_equality)

## Common mistakes

- Putting the null value literal in a type position — PARSE040 null_value_in_type_position; the nullable union is `T ∪ none`.

## Grammar

```
literal :← 'null'
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Example

```fab
main {
    let none nothing ← null
    print nothing
}
```

See also: [`∪`](∪.md), [`optional`](optional.md).

Fetch list: https://faberlang.dev/agents/index.md
