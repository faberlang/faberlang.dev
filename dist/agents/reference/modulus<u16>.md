# modulus<u16>

Unsigned 16-bit modular-word arithmetic and bit-pattern edges.

**Term** `modulus<u16>` · **Section** OPERATORS

## Syntax

```
modulus<u16>
```

## What this teaches

- Modular word contract — `wrapping<u16>` wraps on overflow for add, sub, mul, neg, and shifts.
- Edge cases — Max + 1, zero - 1, and shifts beyond bit width demonstrate wrapping behavior.

## Common mistakes

- Assuming modular words trap on overflow like checked int does.

## MODULAR WORD CONTRACT

modulus<u16> is an unsigned 16-bit modular word. Addition, subtraction,
multiplication, negation, bitwise operations, and shifts use u16 wrapping.
Division and remainder by zero fail.

## Example

```fab
main {
    var wrapping<u16> max ← 65535
    const wrapping<u16> one ← 1
    var wrapping<u16> zero ← 0
    const u16 converted ↤ one
    const wrapping<u16> ring1 ← max + one
    print ring1
    const wrapping<u16> ring2 ← zero - one
    print ring2
    const wrapping<u16> ring3 ← max * 2
    print ring3
    const wrapping<u16> ring4 ← -one
    print ring4
    const wrapping<u16> ring5 ← ¬zero
    print ring5
    const wrapping<u16> ring6 ← one ⇐ 16
    print ring6
    print max ⇒ 16
    print max ≻ zero
    max ↑
    zero ↓
    print max
    print zero
    const wrapping<u16> methodSum ← max.added(one)
    const wrapping<u16> methodShift ← max.shifted_left(16)
    var wrapping<u16> methodAcc ← 0
    methodAcc.add(one)
    methodAcc.shift_left(16)
    print converted
    print methodSum
    print methodShift
    print methodAcc
    const list<wrapping<u16>> words ← [one, max]
    print words.get(1) coalesce 0 ∷ wrapping<u16>
}
```

See also: [`int`](int.md), [`¬`](¬.md), [`⇐`](⇐.md), [`⇒`](⇒.md).

Fetch list: https://faberlang.dev/agents/index.md
