# modulus<u32>

Unsigned 32-bit modular-word arithmetic and bit-pattern edges.

**Term** `modulus<u32>` · **Section** OPERATORS

## Syntax

```
modulus<u32>
```

## What this teaches

- Modular word contract — `wrapping<u32>` is an unsigned 32-bit word with wrapping arithmetic.
- Edge cases — Max + 1, zero - 1, and 1 ⇐ 32 demonstrate wrapping at the 32-bit boundary.

## Common mistakes

- Assuming modular word division or remainder by zero returns a value instead of failing.

## MODULAR WORD CONTRACT

modulus<u32> is an unsigned 32-bit modular word. Addition, subtraction,
multiplication, negation, bitwise operations, and shifts use u32 wrapping.
Division and remainder by zero fail.

## Example

```fab
main {
    var wrapping<u32> max ← 4294967295
    const wrapping<u32> one ← 1
    var wrapping<u32> zero ← 0
    const u32 converted ↤ one
    print max + one
    print zero - one
    print max * 2
    print -one
    print ¬zero
    print one ⇐ 32
    print max ⇒ 32
    print max ≻ zero
    max ↑
    zero ↓
    print max
    print zero
    const wrapping<u32> methodSum ← max.added(one)
    const wrapping<u32> methodShift ← max.shifted_left(32)
    var wrapping<u32> methodAcc ← 0
    methodAcc.add(one)
    methodAcc.shift_left(32)
    print converted
    print methodSum
    print methodShift
    print methodAcc
    const list<wrapping<u32>> words ← [one, max]
    print words.get(1) coalesce 0 ∷ wrapping<u32>
}
```

See also: [`int`](int.md), [`¬`](¬.md), [`⇐`](⇐.md), [`⇒`](⇒.md).

Fetch list: https://faberlang.dev/agents/index.md
