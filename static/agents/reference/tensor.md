# tensor

tensor<T, Figura> declaration shell with rank-0 empty.

**Term** `tensor` · **Section** TYPES

## Syntax

```
tensor<T, Figura> | tensor<T, []>
```

## What this teaches

- Tensor declaration — `tensor<T, Figura>` type syntax with `empty` as the empty initializer
- Identity functions — passing tensors through functions preserves shape and rank

## Common mistakes

- declaring tensor<T> without a Figura shape parameter — use tensor<T, Figura> with explicit dimensions

## Grammar

```
type :← 'tensor' '<' type ',' shape '>'
```

## Expected output

```
Rank-0 tensor longitudo after round-trip identity call.
```

## Example

```fab
fn identity(tensor<f32, []> value) → tensor<f32, []> {
    return value
}

main {
    const tensor<f32, []> empty ← empty
    const tensor<f32, []> roundtrip ← identity(empty)

    print roundtrip.length()
}
```

See also: [`tensor`](tensor.md), [`list`](list.md).

Fetch list: https://faberlang.dev/agents/index.md
