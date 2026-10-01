# Check

`faber check` rejects a string stored into an `int`. The diagnostics on
this line are `SEM010` `expression_type_mismatch` and
`initializer_annotation_mismatch`.

```faber locale=en outcome=rejects
main {
    const int x ← "no"
}
```

```bash
faber check .
faber explain SEM010
```

`faber explain SEM010` says the expression type does not match the
expected type.

Fetch list: https://faberlang.dev/agents/index.md
