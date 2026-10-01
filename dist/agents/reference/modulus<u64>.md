# modulus<u64>

Unsigned 64-bit modular-word arithmetic and bit-pattern edges.

**Term** `modulus<u64>` · **Section** OPERATORS

## Syntax

```
modulus<u64>
```

## What this teaches

- Modular word contract — `wrapping<u64>` wraps on overflow; demonstrates max + 1, zero - 1.
- Carrier-mix equality — Conversions and arithmetic results compare by value across carriers.

## Common mistakes

- Assuming 64-bit modular words trap on overflow like checked int types.

## MODULAR WORD CONTRACT

modulus<u64> is an unsigned 64-bit modular word. Addition, subtraction,
multiplication, negation, bitwise operations, and shifts use u64 wrapping.
Division and remainder by zero fail.

## Example

```fab
main {
    var wrapping<u64> max ← 18446744073709551615
    const wrapping<u64> one ← 1
    var wrapping<u64> zero ← 0
    const u64 converted ↤ one
    print max + one
    print zero - one
    print max * 2
    print -one
    print ¬zero
    print one ⇐ 64
    print max ⇒ 64
    print max ≻ zero

    # Carrier-mix equality: conversions and arithmetic results compare by
    # value against literals (review regression).
    const wrapping<u64> uno ↤ 1
    print one ≡ uno
    print one ≡ one + 0
    max ↑
    zero ↓
    print max
    print zero
    const wrapping<u64> methodSum ← max.added(one)
    const wrapping<u64> methodShift ← max.shifted_left(64)
    var wrapping<u64> methodAcc ← 0
    methodAcc.add(one)
    methodAcc.shift_left(64)
    print converted
    print methodSum
    print methodShift
    print methodAcc
    const list<wrapping<u64>> words ← [one, max]
    print words.get(1) coalesce 0 ∷ wrapping<u64>
    var list<wrapping<u64>> sorted ← [18446744073709551615, 3, 10, 2]
    sorted.sort()
    print sorted
}
```

See also: [`int`](int.md), [`¬`](¬.md), [`⇐`](⇐.md), [`⇒`](⇒.md).

Fetch list: https://faberlang.dev/agents/index.md
