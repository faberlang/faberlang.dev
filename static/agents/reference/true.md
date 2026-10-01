# true

Represents the true boolean value and can prefix a truthiness check.

**Term** `verum` · **Section** KEYWORDS

## Syntax

```
true [<expression>]
```

## What this teaches

- Boolean literal — `true` as the canonical `true` value for `bool` type
- Truthiness prefix — `true` can prefix an expression for explicit truthiness checking

## Common mistakes

- confusing true (the true literal) with not none (a null check) — true is a boolean value, not a presence test

## Grammar

```
literal :← 'verum'
```

## Expected output

```
Scalar stdout smoke (see body).
main {
    const bool active ← true
    print active
}
```

## Example

```fab
test "true is the true literal" {
    const bool active ← true
    assert active
    assert active ≡ true
}

test "true stands alone as a truthy condition" {
    assert true
}
```

See also: [`false`](false.md), [`none`](nihil.md).

Fetch list: https://faberlang.dev/agents/index.md
