# do

Starts a scoped do-while style loop.

**Term** `fac` · **Section** KEYWORDS · **Also** `do`

## Syntax

```
do <block> [catch <name> <block>] [while <condition>]
```

## What this teaches

- Starts a scoped do-while style loop.
- Related keywords: while, catch, lambda, continue

## Common mistakes

- Using `catch` on a non-`do` block — `catch` only attaches to `do` statements, not arbitrary blocks.

## Grammar

```
facStmt :← 'fac' block 'cape' ident block
```

## Expected output

```
none — success path then simulated failure on attempt 2
```

## Backend

```
Rust/Go: fac/cape not yet emitted — compile-only smoke.
```

## Example

```fab
main {
    do {
        print "Block executed successfully"
    }
    catch err {
        print "Caught error: §"(err.nuntius)
    }

    # throw on second attempt; catch recovers and prints err.nuntius
    var int attempts ← 0
    do {
        attempts ← attempts + 1
        print "Attempt §"(attempts)
        if attempts ≡ 2 {
            throw "Simulated failure"
        }
    }
    catch err {
        print "Failed on attempt §: §"(attempts, err.nuntius)
    }
}
```

See also: [`while`](while.md), [`catch`](catch.md), [`lambda`](lambda.md), [`continue`](continue.md).

Fetch list: https://faberlang.dev/agents/index.md
