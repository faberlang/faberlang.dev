# trapped

The result of a capture boundary: trap { ... } reifies the error channel into a value read by match.

**Term** `trapped` · **Section** TYPES

## Syntax

```
trapped<R, T>
```

## What this teaches

- trap { ... } runs its block and reifies the ⇥ error channel into a value instead of propagating it; the block's trailing expression is the success.
- Ruled shape (error model 2026-10-13, grammar/EBNF.md): the result is trapped<R, T>, variants returned { value: R } and thrown { error: T }, read with an ordinary match; R and T are separate slots.
- On the current compiler the boundary's result checks and runs as the union R ∪ E, so this program matches the members (case int / case string); the returned/thrown variant arms land with the trapped re-typing (need f9d8a611 follow-ups).
- trap catches only the ⇥ channel — panic stays fatal; the success and error types collapsing to one type is rejected (trap_union_collapsed).

## Common mistakes

- Expecting trap to catch panic or assert — it never does.
- Success and error of the same type — the value cannot tell them apart.
- Confusing trap with catch — catch is the statement-level handler that binds the payload; trap is the expression that yields the value.

## Example

```fab
fn half(int n) → int ⇥ string {
    if n % 2 ≢ 0 {
        throw "odd"
    }
    return n / 2
}

main {
    # trap { ... } turns the failable call's two exits into one value.
    let missed ← trap { half(7) }
    match missed {
        case int let value {
            print "returned §"(value)
        }
        case string let err {
            print "thrown §"(err)
        }
    }

    let made ← trap { half(8) }
    match made {
        case int let value {
            print "returned §"(value)
        }
        case string let err {
            print "thrown §"(err)
        }
    }
}
```

See also: [`match`](match.md), [`throw`](throw.md), [`catch`](catch.md).

Fetch list: https://faberlang.dev/agents/index.md
