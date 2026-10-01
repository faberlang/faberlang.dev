# panic

Raises a fatal error or panic.

**Term** `mori` · **Section** KEYWORDS · **Also** `panic`

## Syntax

```
panic <expression>
```

## What this teaches

- fatal unrecoverable abort with `panic` — halts execution with an error message
- invariant checking — using `panic` for divisor and bounds checks

## Common mistakes

- Using panic for recoverable errors — use throw with ⇥ for recoverable failure paths instead.

## Grammar

```
abortStmt :← 'mori' expr
```

## Expected output

```
Happy-path division and lista access; mori paths are commented out.
```

## Example

```fab
fn divide(int a, int b) → float {
    # Use panic for invariant violations
    if b ≡ 0 {
        panic "divisio per nihilum"
    }
    return (a ↦ float) / (b ↦ float)
}

fn accipe(list<int> numeri, int index) → int {
    # Bounds check with panic
    if index ≺ 0 or index ≥ numeri.length() {
        panic "index extra fines"
    }
    return numeri[index]
}

main {
    # Happy path — panic branches not taken
    const float value ← divide(10, 2)
    # 5.0
    print "value: §"(value)

    # This would call panic:
    # const _ malum ← divide(10, 0)

    # Lista accessus
    const list<int> nums ← [1, 2, 3]
    const int lectum ← accipe(nums, 1)
    # 2
    print "value: §"(lectum)
}
```

See also: [`throw`](throw.md), [`then`](then.md).

Fetch list: https://faberlang.dev/agents/index.md
