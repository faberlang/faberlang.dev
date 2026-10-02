# set

Generic set collection type.

**Term** `copia` · **Section** KEYWORDS · **Also** `set`

## Syntax

```
set<T>
```

## What this teaches

- Generic set collection type.
- Related keywords: list, map, ∈

## Common mistakes

- Using `set<T>` without an explicit type — `empty` requires an explicit type annotation like `set<numerus>` (SEM014).

## Grammar

```
copia.add(x) | copia.has(x) | copia.delete(x)
copia.length() | copia.is_empty()
copia<T> is a set-like collection; vacua with copia<T> creates an empty set.
```

## Expected output

```
Smoke asserts exit 0 only.
BACKEND: Go e2e whitelist — copia method surface not yet lowered for Go.
```

## Example

```fab
main {
    var set<int> numeri ← empty
    numeri.add(1)
    numeri.add(2)
    numeri.add(3)
    const bool habetduo ← numeri.has(2)
    const bool remotus ← numeri.delete(3)
    const int longitudo ← numeri.length()
    const bool vacuaest ← numeri.is_empty()
    print habetduo, remotus, longitudo, vacuaest
}
```

See also: [`list`](list.md), [`map`](map.md), [`∈`](∈.md).

Fetch list: https://faberlang.dev/agents/index.md
