# while

Repeats a block while a condition remains true.

**Term** `dum` · **Section** KEYWORDS · **Also** `while`

## Syntax

```
while <condition> <block|ergo statement>
```

## What this teaches

- While loop — `while <condition> { <body> }` repeats a block as long as the condition is true.
- Loop variable mutation — mutable `var` bindings allow counter-based loop control.
- Ascending and descending loops — counting up from 0 or down from N until the condition is false.

## Common mistakes

- Using `break` or `continue` outside a loop — `continue` needs an enclosing loop (`while`, `for`, `do … while`) in the same function (SEM031); `break` also accepts a plain `do` block (SEM030).

## Grammar

```
loopStmt :← 'dum' expr '{' stmt* '}'
```

## Expected output

```
dum.expected
main {
Ascending counter: varia so the loop variable can mutate
    var int computus ← 0
    while computus ≺ 5 {
        print computus
        computus ← computus + 1
    }
Descending loop: condition becomes falsum at 0
    var int reliquum ← 3
    while reliquum ≻ 0 {
        print "reliquum: §"(reliquum)
        reliquum ← reliquum - 1
    }
    print "perfectum!"
}
```

## Example

```fab
test "while counts up to its condition" {
    var int computus ← 0
    while computus ≺ 5 {
        computus ← computus + 1
    }
    assert computus ≡ 5
}

test "while counts down to zero" {
    var int reliquum ← 3
    while reliquum ≻ 0 {
        reliquum ← reliquum - 1
    }
    assert reliquum ≡ 0
}
```

See also: [`if`](if.md), [`then`](then.md), [`do`](do.md).

Fetch list: https://faberlang.dev/agents/index.md
