# vector

vector type declarations: long form and vf32 sugar.

**Term** `vector` · **Section** TYPES

## Syntax

```
vector<T, N> | vf32[N]
```

## What this teaches

- Vector declaration — `vector<T, N>` long form and `vf32[N]` sugar syntax
- Register type — vectors are fixed-width register types, different from collection tensors

## Common mistakes

- confusing vector<T, N> (register type) with tensor<T, [N]> (collection type) — vector is a GPU register, not a collection

## Example

```fab
fn takes(vector<f32, 4> v, vf32[4] w) → int {
    return 0
}

fn declSmoke() → int {
    return 0
}
```

Fetch list: https://faberlang.dev/agents/index.md
