# from

Extracts fields from a value into local bindings.

**Term** `ex` · **Section** KEYWORDS

## Syntax

```
from <expression> <fixum|varia> <field> [, ...] [rest <ident>]
```

## What this teaches

- Field extraction — `from <expr> const <field>, ...` extracts named fields from class records into local scope.
- Multiple field extraction — extract several fields from a single expression in one statement.

## Common mistakes

- Mode mismatch — passing a `ref` (read-only) parameter to an `from` (consume) position, or extracting a field that doesn't exist on the target type.

## Grammar

```
extractStmt :← 'ex' expr bindingList
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Cross-ref: destructura/objectum.fab, itera/ex.fab (itera ex mode).
```

## Example

```fab
class Persona {
    var string name
    var int aetas
}

main {
    const _ p ← Persona { name = "Marcus", aetas = 30 }
    from p const name, aetas
    print name
    print aetas
}
```

See also: [`ref`](ref.md), [`as`](as.md), [`rest`](rest.md).

Fetch list: https://faberlang.dev/agents/index.md
