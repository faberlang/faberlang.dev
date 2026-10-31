# trapped

The result of a capture boundary: trap { ... } reifies the error channel into a value read by match.

**Term** `trapped` · **Section** TYPES

## Syntax

```
trapped<R, T>
```

## What this teaches

- trap { ... } runs its block and reifies the ⇥ error channel into a value instead of propagating it; the block's trailing expression is the success.
- Ruled shape (error model 2026-10-13, grammar/EBNF.md): the result is trapped<R, T>, variants returned { value: R } and thrown { error: T }, read with an ordinary match.
- R and T are separate slots, so a string success with a string error is legal — the variants carry the discrimination, not the types.
- trap catches only the ⇥ channel — panic stays fatal.

## Common mistakes

- Expecting trap to catch panic or assert — it never does.
- Matching the member types (case int / case string) — the result is the tagged trapped<R, T>, so the arms name the variants returned and thrown.
- Confusing trap with catch — catch is the statement-level handler that binds the payload; trap is the expression that yields the value.

## Example

```fab
fn half(int n) → int ⇥ string {
    if n % 2 ≢ 0 {
        throw "odd"
    }
    return n / 2
}

# R ≡ T: legal, because the slots are separate and the variants tell them apart.
fn twin() → string ⇥ string {
    return "value"
}

main {
    # trap { ... } turns the failable call's two exits into one value.
    let _ missed ← trap { half(7) }
    match missed {
        case returned let value {
            print "returned §"(value)
        }
        case thrown let err {
            print "thrown §"(err)
        }
    }

    let _ made ← trap { half(8) }
    match made {
        case returned let value {
            print "returned §"(value)
        }
        case thrown let err {
            print "thrown §"(err)
        }
    }

    # A string success with a string error: legal, the arms still discriminate.
    let _ twinned ← trap { twin() }
    match twinned {
        case returned let value {
            print "twin returned §"(value)
        }
        case thrown let error {
            print "twin thrown §"(error)
        }
    }
}
```

See also: [`match`](match.md), [`throw`](throw.md), [`catch`](catch.md).

Fetch list: https://faberlang.dev/agents/index.md
