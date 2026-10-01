# warn

Writes a warning message.

**Term** `mone` · **Section** KEYWORDS

## Syntax

```
warn <expression>
```

## What this teaches

- the `warn` keyword — emits a warning-style diagnostic (distinct from `print`/`debug`)
- diagnostic output categories — warn for warnings vs write/vide for other I/O

## Common mistakes

- Confusing warn (stderr warning) with print (diagnostic info) — warn emits warnings, print emits neutral informational output.

## Grammar

```
outputStmt :← 'mone' expr
```

## Expected output

```
mone-style warning diagnostic (single mone call).
```

## Example

```fab
main {
    warn "cave"
}
```

See also: [`write`](write.md), [`debug`](debug.md).

Fetch list: https://faberlang.dev/agents/index.md
