# map

Generic key/value map type.

**Term** `tabula` · **Section** KEYWORDS · **Also** `map`, `dictionary`

## Syntax

```
map<K,V>
```

## What this teaches

- Map declaration — `map<K,V>` with bracket syntax for keyed access
- Map literals — empty map via `empty`, then populating with index assignment

## Common mistakes

- using bracket syntax with a key type that doesn't match the map declaration, or inserting duplicate keys

## Grammar

```
mapDecl :← 'varia' 'tabula<' type ',' type '>' ident '←' expr
mapAcc  :← expr '[' expr ']'
```

## Expected output

```
longitudo() plus keyed lookups for alpha/beta/gamma (tabula.expected).
```

## Example

```fab
main {
    var map<string, int> puncta ← empty
    puncta["alpha"] ← 1
    puncta["beta"] ← 2
    puncta["gamma"] ← 3
    print puncta.length()
    print puncta["alpha"]
    print puncta["beta"]
    print puncta["gamma"]
}
```

See also: [`list`](list.md), [`set`](set.md), [`∷`](∷.md), [`for`](for.md).

Fetch list: https://faberlang.dev/agents/index.md
