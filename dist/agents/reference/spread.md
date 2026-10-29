# spread

Spreads an array or collection literal into its surrounding expression.

**Term** `spread` · **Section** KEYWORDS · **Also** `...`

## Syntax

```
spread <expression>
```

## What this teaches

- Spread syntax — how to splice a collection into a list literal or function call
- Collection composition — building larger expressions by expanding collections inline

## Common mistakes

- confusing spread (splice) with appende, or using spread on a non-collection expression

## Grammar

```
spargeExpr :← 'sparge' expr
```

## Expected output

```
1, 2, 3, 4 (expanded list elements).
```

## Example

```fab
main {
    let list<int> media ← [2, 3]
    # → [1, 2, 3, 4]
    let list<int> numeri ← [1, spread media, 4]
    for from numeri let n {
        print n
    }
}
```

See also: [`list`](list.md).

Fetch list: https://faberlang.dev/agents/index.md
