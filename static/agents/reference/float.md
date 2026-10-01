# float

Primitive floating-point number type.

**Term** `fractus` · **Section** KEYWORDS · **Also** `float`

## Syntax

```
float
```

## What this teaches

- Primitive floating-point number type.
- Related keywords: int, ↦

## Common mistakes

- Using `≡` for direct floating-point equality — float equality is unreliable due to precision; use `.approx()` for tolerance-based comparison.

## Grammar

```
valor.abs() | valor.sign()
valor.minimum(other) | valor.maximum(other)
Mirrors numerus-methodi.fab for floating-point; Wasm tier Runnable.
```

## Expected output

```
Smoke asserts exit 0 only.
```

## Example

```fab
main {
    const float value ← -3.75
    const float absolutus ← value.abs()
    const float signum ← value.sign()
    const float minor ← value.minimum(2.5)
    const float maior ← value.maximum(2.5)
    print absolutus, signum, minor, maior
}
```

See also: [`int`](int.md), [`↦`](↦.md).

Fetch list: https://faberlang.dev/agents/index.md
