# ref

Introduces borrowed iteration or borrowed parameters.

**Term** `de` · **Section** KEYWORDS

## Syntax

```
ref <expression>
```

## What this teaches

- Borrowed iteration — `for ref <expr> const <ident> { ... }` iterates over a collection without taking ownership.
- Tabula key iteration — iterating over map keys via borrowed iteration.
- Index iteration — iterating over list indices via `ref`.

## Common mistakes

- Passing a `ref` parameter to an `mut` or `from` position — mode mismatch; cannot pass a read-only reference where mutation or consumption is expected (SEM057).

## Grammar

```
forDeStmt :← 'itera' 'de' expr 'fixum' ident block
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Cross-ref: itera/de.fab.
```

## Example

```fab
main {
    const map<string, int> persona ← { "name": 1, "aetas": 30 }
    for ref persona const clavis {
        print clavis
    }
    const list<int, 3> numeri ← [10, 20, 30]
    for ref numeri const index {
        print index
    }
}
```

See also: [`from`](from.md), [`in`](mut.md).

Fetch list: https://faberlang.dev/agents/index.md
