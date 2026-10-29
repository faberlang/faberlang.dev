# step

Sets the step for a range.

**Term** `step` · **Section** KEYWORDS

## Syntax

```
<range> step <expression>
```

## What this teaches

- Range stepping — `step <expr>` after a range specifies the increment between iterations.
- Custom step sizes — Unlike the default step of 1, `step 2` iterates over even numbers only.

## Common mistakes

- Confusing `step` (range step) with `continue` (continue) — they are unrelated keywords.

## Grammar

```
iterStmt :← 'itera' 'ab' expr '‥' expr 'per' expr binding block
```

## Expected output

```
0, 2, 4, 6 (step by 2 over 0‥8).
```

## Example

```fab
main {
    # i = 0, 2, 4, 6 (step by 2)
    for range 0‥8 step 2 let i {
        print i
    }
}
```

See also: [`before`](before.md), [`until`](until.md).

Fetch list: https://faberlang.dev/agents/index.md
