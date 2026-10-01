# range

Selects numeric range iteration in an for loop.

**Term** `ab` · **Section** KEYWORDS

## Syntax

```
for range <range> <binding>
```

## What this teaches

- `for range` bounded range iteration — iterates over a numeric range with an optional step
- Step syntax — the `per <step>` clause controls stride within the range

## Common mistakes

- using the retired `range`/`ubi` collection pipeline DSL; use ordinary collection methods and closures instead

## Grammar

```
iteraStmt :← 'itera' 'ab' expr '‥' expr step? 'fixum' ident block
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Example

```fab
main {
    for range 0‥10 step 2 const i {
        print i
    }
}
```

See also: [`for`](for.md), [`from`](from.md), [`ref`](ref.md), [`per`](step.md), `range pipeline`.

Fetch list: https://faberlang.dev/agents/index.md
