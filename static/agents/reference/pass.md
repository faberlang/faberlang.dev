# pass

Marks an explicit no-op statement.

**Term** `tacet` · **Section** KEYWORDS · **Also** `silent noop`

## Syntax

```
pass
```

## What this teaches

- Explicit no-op — `pass` as a deliberate empty statement, especially in control flow
- Musical rest metaphor — `pass` signals intentional absence of action

## Common mistakes

- using pass where logic is expected, which hides missing code; pass is also outside the v1 AIR pure subset

## Grammar

```
noopStmt :← 'tacet'
```

## Expected output

```
cond verum, finis (tacet.expected).
```

## Example

```fab
fn maybeNota(bool cond) → void {
    if cond {
        print "cond true"
    }
    else {
        # deliberate no-op in else branch
        pass
    }
}

main {
    # prints
    maybeNota(true)
    # pass — no output
    maybeNota(false)

    # condition false, so pass never runs
    if false then pass

    print "finis"
}
```

See also: [`then`](then.md), [`return`](return.md).

Fetch list: https://faberlang.dev/agents/index.md
