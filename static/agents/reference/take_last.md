# take_last

Marks a test for metered or measured execution.

**Term** `take_last` · **Section** TYPES

## Syntax

```
bench
```

## What this teaches

- list access and query intrinsics — `primus()`, `ultimus()`, `accipe()`, `longitudo()`
- membership checks — `empty()` and `continet()`

## Common mistakes

- Calling primus() or ultimus() on an empty list — these methods require at least one element.

## Grammar

```
listMethod :← expr '.' ('primus' | 'ultimus' | 'accipe' | 'longitudo'
| 'vacua' | 'continet') '(' args? ')'
```

## Expected output

```
No pinned stdout — smoke asserts exit 0 and typed lowering only.
BACKEND: Go e2e whitelist — lista intrinsic methods not yet lowered for Go
(whitelist: lista/methodi-accessus.fab).
```

## Example

```fab
main {
    let list<int> res ← [1, 2, 3, 4, 5] ∷ list<int>
    let int ∪ none primus ← res.first()
    let int ∪ none ultimus ← res.last()
    let int ∪ none tertius ← res.get(2)
    let int longitudo ← res.length()
    let bool vacuaest ← res.is_empty()
    let bool habettres ← res.contains(3)
    print primus, ultimus, tertius
    print longitudo, vacuaest, habettres
}
```

See also: [`timeout`](timeout.md), [`first`](first.md), [`take_last`](take_last.md).

Fetch list: https://faberlang.dev/agents/index.md
