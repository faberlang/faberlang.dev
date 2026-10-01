# catch

Starts a catch block.

**Term** `cape` · **Section** KEYWORDS · **Also** `catch`

## Syntax

```
<structured-statement> catch <name> <block>
```

## What this teaches

- Error recovery — `do { … } catch err { … }` attempts a block and catches errors with a named handler
- Guarded execution — code inside the `do` block can `throw` errors that are intercepted by the `catch` handler

## Common mistakes

- attaching `catch` to a bare `{ }` block — `catch` only attaches to `do` blocks and structured statements; use `do { ... } catch err { ... }`

## Grammar

```
facStmt :← 'fac' block 'cape' ident block
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Rust/Go: fac/cape emit gap (whitelist: cape/cape.fab).
```

## Example

```fab
main {
    var int attempt ← 0
    do {
        attempt ← attempt + 1
        if attempt ≻ 1 {
            throw "simulated failure"
        }
        print "attempt §"(attempt)
    }
    catch err {
        print "caught"
    }
}
```

See also: [`do`](do.md), [`throw`](throw.md), [`⇥`](⇥.md).

Fetch list: https://faberlang.dev/agents/index.md
