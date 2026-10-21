# false

Represents the false boolean value and can prefix a falsity check.

**Term** `falsum` · **Section** KEYWORDS

## Syntax

```
false [<expression>]
```

## What this teaches

- Represents the false boolean value and can prefix a falsity check.
- Related keywords: true, none

## Common mistakes

- Confusing `false` with `none` (la `none`) — `false` is a bool literal (false); `none` is the absent-member type, and its value is `null` (`null`).

## Grammar

```
literal :← 'falsum'
```

## Expected output

```
Scalar stdout smoke (see body).
main {
    let bool inactive ← false
    print inactive
}
```

## Example

```fab
test "false is the false literal" {
    let bool inactive ← false
    assert inactive ≡ false
    assert not inactive
}

test "false contrasts with true" {
    assert false ≢ true
    assert false ≡ false
}
```

See also: [`true`](true.md), [`none`](none.md).

Fetch list: https://faberlang.dev/agents/index.md
