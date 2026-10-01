# if

Starts a conditional branch that runs when its condition is true.

**Term** `si` · **Section** KEYWORDS · **Also** `if`

## Syntax

```
if <condition> <block>
```

## What this teaches

- Basic conditional execution — `if <condition> { body }` runs the body only when the condition evaluates to `true`
- Multiple independent `if` blocks can be chained; each evaluates its own condition independently

## Common mistakes

- Using a non-`bool` expression as the `if` condition (SEM011), or using `∴` instead of `then` for a single-statement body.

## Grammar

```
ifStmt :← 'si' expr block
```

## Expected output

```
x maior quam 5, Adult, Can vote (si.expected).
main {
Simple truthy branch — only the first condition matches
    const int x ← 10
    if x ≻ 5 {
        print "x maior quam 5"
    }
    if x ≻ 20 {
skipped: 10 ≯ 20
        print "x maior quam 20"
    }
Block body: multiple statements run together when condition holds
    const int aetas ← 25
    if aetas ≥ 18 {
        print "Adult"
        print "Can vote"
    }
}
```

## Example

```fab
test "if runs its body on a true condition" {
    const int x ← 10
    var bool maior ← false
    if x ≻ 5 {
        maior ← true
    }
    assert maior
}

test "if skips its body on a false condition" {
    const int x ← 10
    var bool maior ← false
    if x ≻ 20 {
        maior ← true
    }
    assert not maior
}

test "if block body runs every statement" {
    const int aetas ← 25
    var int gradus ← 0
    if aetas ≥ 18 {
        gradus ← gradus + 1
        gradus ← gradus + 1
    }
    assert gradus ≡ 2
}
```

See also: [`elif`](elif.md), [`else`](else.md), [`then`](then.md).

Fetch list: https://faberlang.dev/agents/index.md
