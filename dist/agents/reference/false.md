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

- Confusing `false` with `none` — `false` is a bool literal (false); `none` is the null/absent sentinel.

## Grammar

```
literal :← 'falsum'
```

## Expected output

```
Scalar stdout smoke (see body).
main {
    const bool inactive ← false
    print inactive
}
```

## Example

```fab
test "false is the false literal" {
    const bool inactive ← false
    assert inactive ≡ false
    assert not inactive
}

test "false contrasts with true" {
    assert false ≠ true
    assert false ≡ false
}
```

See also: [`true`](true.md), [`none`](nihil.md).

Fetch list: https://faberlang.dev/agents/index.md
