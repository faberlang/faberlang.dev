# throw

Throws a recoverable error.

**Term** `iace` · **Section** KEYWORDS · **Also** `throw`

## Syntax

```
throw <expression>
```

## What this teaches

- Throws a recoverable error.
- Related keywords: ⇥, catch, panic, return

## Common mistakes

- Using `throw` without a `⇥` on the enclosing function or a `do { ... } catch err { ... }` wrapper — `throw` requires an error-handling context (SEM010).

## Grammar

```
throwStmt :← 'iace' expr
facStmt   :← 'fac' block catchClause?
```

## Expected output

```
Caught error messages from fac/cape recovery paths.
```

## Backend

```
Rust/Go lowering does not emit iace/cape yet — compile-only smoke.
```

## Example

```fab
main {
    # Bare throw with string payload
    do {
        throw "Something went wrong"
    }
    catch err {
        print "Caught:", err
    }

    # throw with interpolated message
    const int code ← 404
    do {
        throw "Error code: §"(code)
    }
    catch err {
        print "Caught:", err
    }

    # Conditional throw inside do — validation guard
    const int value ← -5
    do {
        if value ≺ 0 {
            throw "Value must be non-negative"
        }
        print "Value is valid"
    }
    catch err {
        print "Validation failed:", err
    }
}
```

See also: [`⇥`](⇥.md), [`catch`](catch.md), [`panic`](panic.md), [`return`](return.md).

Fetch list: https://faberlang.dev/agents/index.md
