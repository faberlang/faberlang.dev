# reject

Reject a condition or throw a recoverable error.

**Term** `reice` · **Section** KEYWORDS · **Also** `reject`

## Syntax

```
reject <expression> throw <expression>
```

## What this teaches

- Reject guard — `reject <condition> throw <error>` throws into the function's ⇥ channel when the condition is true (en surface of `reject`)
- Boolean opposite of `require` — `require not (p) throw e` becomes `reject p throw e`; no hand-rolled negation
- Typed payload — the true-path expression is a `variant`, the same shape used at constructor guard ladders

## Common mistakes

- Using `reject` in a function without `⇥ E` — SEM010 `iace_requires_alternate_exit`, same as `throw`
- Reading `reject` as `require` — it fails when the condition HOLDS

## Grammar

```
reiceStmt :← 'reice' expr 'iace' expr
```

## Expected output

```
empty — success-path main only (reice.expected)
```

## Example

```fab
union GuardError {
    Invalid { string causa }
}

fn guarded(int value) → int ⇥ GuardError {
    reject value ≺ 0 throw variant Invalid { causa = "value must not be negative" }
    return value
}

main {
    do {
        const int ok ← guarded(1)
        assert ok ≡ 1
    }
    catch err {
        assert false panic "success path must not throw"
    }
}

test "true path is recoverable" {
    do {
        const int dropped ← guarded(-1)
        assert false panic "true path must throw"
    }
    catch err {
        # recovered — reject entered ⇥ and catch intercepted it
    }
}
```

See also: [`require`](require.md), [`assert`](assert.md), [`throw`](throw.md), [`catch`](catch.md), [`⇥`](⇥.md).

Fetch list: https://faberlang.dev/agents/index.md
