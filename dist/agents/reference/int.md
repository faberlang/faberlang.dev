# int

Primitive integer number type.

**Term** `numerus` · **Section** KEYWORDS · **Also** `integer`, `int`

## Syntax

```
int
```

## What this teaches

- Primitive integer number type.
- Related keywords: float, ↦

## Common mistakes

- Using `int` comparison methods on non-numeric types — `.abs()`, `.sign()`, `.minimum()`, `.maximum()` are numerus-only intrinsics.

## Grammar

```
valor.abs() | valor.sign()
valor.minimum(other) | valor.maximum(other)
Integer counterpart to fractus-comparatio.fab; Wasm tier Runnable.
```

## Expected output

```
Smoke asserts exit 0 only.
```

## Example

```fab
main {
    let int value ← -7
    let int absolutus ← value.abs()
    let int signum ← value.sign()
    let int minor ← value.minimum(3)
    let int maior ← value.maximum(3)
    print absolutus, signum, minor, maior
}
```

See also: [`float`](float.md), [`↦`](↦.md).

Fetch list: https://faberlang.dev/agents/index.md
