# return

Returns a value from a function.

**Term** `redde` · **Section** KEYWORDS · **Also** `return`

## Syntax

```
return <expression>
```

## What this teaches

- Function return — `return <expression>` returns a value from a `fn`, and bare `return` returns `void`
- Early returns with `if <cond> then return <expr>` for guard clauses

## Common mistakes

- Using `return` outside a function body — `return` is only valid inside `fn` declarations (SEM032).

## Grammar

```
returnStmt :← 'redde' expr?
```

## Expected output

```
30, Salve, Munde, 42, 0, 20
```

## Example

```fab
fn adde(int a, int b) → int {
    return a + b
}

fn saluta(string name) → string {
    return "Salve, " + name
}

fn duoetquadraginta() → int {
    return 42
}

fn tace() → void {
    # bare return for void return type
    return
}

fn porta(int x) → int {
    if x ≺ 0 {
        # early return on negative input
        return 0
    }
    return x * 2
}

main {
    print adde(10, 20)
    print saluta("Munde")
    print duoetquadraginta()
    tace()
    print porta(-5)
    print porta(10)
}
```

See also: [`→`](→.md), [`⇥`](⇥.md), [`then`](then.md), [`throw`](throw.md), [`pass`](pass.md).

Fetch list: https://faberlang.dev/agents/index.md
