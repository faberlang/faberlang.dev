# assert

Asserts that a condition is true at runtime.

**Term** `assert` · **Section** KEYWORDS

## Syntax

```
assert <expression> [panic <expression>]
```

## What this teaches

- Runtime assertions — `assert <condition>` validates invariants during program execution
- Custom messages — `assert <condition> panic "message"` adds descriptive diagnostic text on failure
- Testing category — assert is the primary assertion keyword for test and verification code

## Common mistakes

- using `assert` outside `test` or `describe` (WARN006); use `panic` for invariant violations in production code or move assertions into test blocks

## Grammar

```
adfirmaStmt :← 'adfirma' expr ('mori' expr)?
```

## Expected output

```
empty — adfirma only (adfirma.expected)
main {
    let int x ← 10
Simple assertion without message
    assert x ≻ 0
Assertion with custom message
    assert x ≡ 10 panic "x decem esse debet"
Multiple assertions
    let string nomen ← "Marcus"
    assert nomen ≡ "Marcus"
    assert nomen ≢ "" panic "nomen vacuum non sit"
Boolean assertions
    let bool viget ← true
    assert viget
    assert viget ≡ true panic "vigere debet"
}
```

## Example

```fab
test "assertions validate invariants" {
    let int x ← 10
    assert x ≻ 0
    assert x ≡ 10 panic "x decem esse debet"
    let string name ← "Marcus"
    assert name ≡ "Marcus"
    assert name ≢ "" panic "name void not let"
    let bool viget ← true
    assert viget
    assert viget ≡ true panic "vigere debet"
}
```

See also: [`test`](test.md), [`do`](do.md), [`catch`](catch.md).

Fetch list: https://faberlang.dev/agents/index.md
