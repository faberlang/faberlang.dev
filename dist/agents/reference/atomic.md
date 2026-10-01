# atomic

atomic<i32> operations are storage-sensitive compiler-owned methods.

**Term** `atomic` · **Section** TYPES

## Syntax

```
atomic<i32> | atomic<u32>
```

## What this teaches

- atomic<i32> operations are storage-sensitive compiler-owned methods.
- Related keywords: int

## Common mistakes

- Calling non-atomic methods on an `atomic<T>` — operations like `.load()`, `.store()`, `.exchange()` are compiler-owned and storage-sensitive.

## Grammar

```
type :← 'atomic' '<' ('i32' | 'u32') '>'
```

## Expected output

```
none; this is a semantic/MIR systems-lane typecheck example.
```

## Backend

```
Package and probe targets reject until atomic storage ABI lowering exists.
```

## Example

```fab
fn atomic_ops(mut atomic<i32> cell, i32 value) → bool {
    const i32 loaded ← cell.load()
    cell.store(value)
    const i32 old ← cell.exchange(loaded)
    return cell.compare_exchange(old, value)
}
```

See also: [`int`](int.md).

Fetch list: https://faberlang.dev/agents/index.md
