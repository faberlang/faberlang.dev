# bool

Primitive types bool, void, and unknown.

**Term** `bivalens` · **Section** KEYWORDS

## Syntax

```
bool | void | unknown
```

## What this teaches

- Primitive types bool, void, and unknown.
- Related keywords: true, false, fn, ∷, void

## Common mistakes

- Using `unknown` where a concrete type is expected — `unknown` is the dynamic dispatch type; use `is` checks or match before extracting.

## Grammar

```
typeExpr :← 'bivalens' | 'vacuum' | 'ignotum'
```

## Expected output

```
ping, nihil est, verum est, aliud est
```

## Backend

```
Cross-ref vacuum/vacuum.fab for void returns; numerus/fractus/textus intrinseca files.
```

## Example

```fab
fn ping() → void {
    print "primitiva smoke"
}

fn describe(any value) → string {
    if value is none then return "none est"
    return "aliud est"
}

fn describe_boolean(bool value) → string {
    if value ≡ true then return "true est"
    return "aliud est"
}

main {
    ping()
    print describe(null)
    print describe_boolean(true)
    print describe(42)
}
```

See also: [`true`](true.md), [`false`](false.md), [`fn`](fn.md), [`∷`](∷.md), [`void`](void.md).

Fetch list: https://faberlang.dev/agents/index.md
