# modulus<u8>

Unsigned 8-bit modular-word arithmetic and bit-pattern edges.

**Term** `modulus<u8>` · **Section** OPERATORS

## Syntax

```
modulus<u8>
```

## What this teaches

- Modular word contract — `wrapping<u8>` wraps on 8-bit overflow; edge cases wrap predictably.
- Bit-pattern edges — Shifting 1 ⇐ 8 wraps to 0; negating 1 wraps to 255.

## Common mistakes

- Expecting division or remainder by zero to produce a value rather than fail.

## MODULAR WORD CONTRACT

modulus<u8> is an unsigned 8-bit modular word. Addition, subtraction,
multiplication, negation, bitwise operations, and shifts use u8 wrapping.
Division and remainder by zero fail.

## Example

```fab
main {
    var wrapping<u8> max ← 255
    const wrapping<u8> one ← 1
    var wrapping<u8> zero ← 0
    const u8 converted ↤ one
    print max + one
    print zero - one
    print max * 2
    print -one
    print ¬zero
    print one ⇐ 8
    print max ⇒ 8
    print max ≻ zero
    max ↑
    zero ↓
    print max
    print zero
    const wrapping<u8> methodSum ← max.added(one)
    const wrapping<u8> methodShift ← max.shifted_left(8)
    var wrapping<u8> methodAcc ← 0
    methodAcc.add(one)
    methodAcc.shift_left(8)
    print converted
    print methodSum
    print methodShift
    print methodAcc
    const list<wrapping<u8>> words ← [one, max]
    print words.get(1) coalesce 0 ∷ wrapping<u8>
}
```

See also: [`int`](int.md), [`¬`](¬.md), [`⇐`](⇐.md), [`⇒`](⇒.md).

Fetch list: https://faberlang.dev/agents/index.md
