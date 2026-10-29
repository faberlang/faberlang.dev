# rest

Collects remaining parameters, operands, or extracted fields.

**Term** `rest` · **Section** KEYWORDS

## Syntax

```
rest <type> <name>
```

## What this teaches

- Rest parameters — `rest <type> <name>` in a function signature collects all remaining arguments into a list
- Variadic functions — `rest list<int> numeri` enables summing an arbitrary number of numeric arguments

## Common mistakes

- confusing `rest` (rest parameter collecting remaining args into a list) with `empty` (an empty collection initializer)

## Grammar

```
param :← 'ceteri' type ident
```

## Expected output

```
none
```

## Example

```fab
fn sum(rest list<int> numeri) → int {
    mut _ total ← 0

    for from numeri let n {
        total ← total + n
    }

    return total
}

main {
    # rest receives the whole list
    print sum([1, 2, 3, 4])
}
```

See also: [`fn`](fn.md), [`operand`](operand.md), [`from`](from.md).

Fetch list: https://faberlang.dev/agents/index.md
