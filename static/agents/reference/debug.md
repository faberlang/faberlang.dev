# debug

Writes a debug value to standard output.

**Term** `vide` · **Section** KEYWORDS

## Syntax

```
debug <expression>
```

## What this teaches

- Diagnostic output — `debug` for inspection-style debugging, distinct from `print` and `warn`
- Output variety — Faber provides multiple output functions for different purposes

## Common mistakes

- confusing debug (diagnostic output) with test (test block) or assert (assertion) — debug is for inspection, not validation

## Grammar

```
outputStmt :← 'vide' expr
```

## Expected output

```
vide-style diagnostic: "inspecta"
```

## Example

```fab
main {
    debug "inspecta"
}
```

See also: [`write`](write.md), [`warn`](warn.md).

Fetch list: https://faberlang.dev/agents/index.md
