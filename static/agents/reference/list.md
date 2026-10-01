# list

Generic ordered collection type.

**Term** `lista` · **Section** KEYWORDS · **Also** `array`, `list`

## Syntax

```
list<T>
```

## What this teaches

- list literal syntax — `[elem, ...]` with typed empty collections using `empty`
- the `spread` operator — splicing one list into another literal
- basic access: `longitudo()` and indexed reads via `[n]`

## Common mistakes

- Using empty without an explicit type annotation — empty requires a declared collection type like list<T>.

## Grammar

```
listDecl :← ('varia' | 'fixum') 'lista<' type '>' ident '←' expr
listLit  :← '[' (expr | sparge)* ']'
```

## Expected output

```
Scalar longitudo() and indexed accipe only (lista.expected).
```

## Example

```fab
main {
    const list<int> vacuares ← empty
    const _ numeri ← [1, 2, 3, 4, 5]
    const _ nomina ← ["Marcus", "Julia", "Gaius"]
    const _ vexilla ← [true, false, true]
    const _ matrix ← [[1, 2], [3, 4], [5, 6]]
    const list<int> primum ← [1, 2, 3]
    const list<int> secundum ← [4, 5, 6]
    const _ coniuncta ← [spread primum, spread secundum]
    const _ aucta ← [0, spread primum, 99]
    print vacuares.length()
    print numeri.length()
    print numeri[0]
    print numeri[4]
    print nomina.length()
    print nomina[1]
    print vexilla[0]
    print vexilla[2]
    print matrix.length()
    print matrix[1][0]
    print coniuncta.length()
    print aucta.length()
    print aucta[0]
    print aucta[4]
}
```

See also: [`map`](map.md), [`set`](set.md), [`∷`](∷.md), [`for`](for.md).

Fetch list: https://faberlang.dev/agents/index.md
