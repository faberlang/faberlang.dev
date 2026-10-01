# require

Require a condition or throw a recoverable error.

**Term** `requirit` · **Section** KEYWORDS · **Also** `require`

## Syntax

```
require <expression> throw <expression>
```

## What this teaches

- Recoverable guard — `require <condition> throw <error>` throws into the function's ⇥ channel when the condition is false (en surface of `require`)
- Twin of `assert` — `assert` is fatal; `require` is catchable by `catch`
- Typed payload — the false-path expression is a `variant` with `causa`, the same shape used at constructor guard ladders

## Common mistakes

- Using `require` in a function without `⇥ E` — SEM010 `iace_requires_alternate_exit`, same as `throw`
- Treating `require` as a test-capability gate — it is a statement, not a named fixture on `test`

## Grammar

```
requiritStmt :← 'requirit' expr 'iace' expr
```

## Expected output

```
empty — success-path main only (requirit.expected)
```

## Example

```fab
union GuardError {
    Invalid { string causa }
}

fn guarded(int value) → int ⇥ GuardError {
    require value ≻ 0 throw variant Invalid { causa = "value must be positive" }
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

test "false path is recoverable" {
    do {
        const int dropped ← guarded(0)
        assert false panic "false path must throw"
    }
    catch err {
        # recovered — require entered ⇥ and catch intercepted it
    }
}
```

See also: [`assert`](assert.md), [`throw`](throw.md), [`catch`](catch.md), [`⇥`](⇥.md).

Fetch list: https://faberlang.dev/agents/index.md
