# Check

`faber check` rejects a string stored into an `int`. The diagnostics on
this line are `SEM010` `expression_type_mismatch` and
`initializer_annotation_mismatch`.

```faber locale=en outcome=rejects
main {
    let int x ← "no"
}
```

```bash
faber check .
```

A failing check prints, for each diagnostic, a line carrying its code and slug
and the source line (the path is printed as resolved, here shortened):

```text
error[SEM010:expression_type_mismatch]: src/main.fab:2
  |     let int x ← "no"
```

`faber check --diagnostics` expands each one into a block with the phase, the
file, the span, the source line, and a `help` sentence:

```text
error[SEM010:expression_type_mismatch] analysis src/main.fab: expression type mismatch
phase: analysis
file: src/main.fab
span: 25..29
source:      let int x ← "no"
help: make the expression type match the expected type
```

`--diagnostics-locale zh-Hans` sets the language of the message and the help
text, independently of the source file's own locale. The code and the slug
stay ASCII.

`faber explain` looks a code up on its own, and `--json` makes the answer
machine-readable:

```bash
faber explain SEM010
faber explain SEM010 --json
```

`faber explain SEM010` says `type mismatch` and gives the help
`make the expression type match the expected type`. `--json` returns
`{query, code, locale, message, help}`.

Fetch list: https://faberlang.dev/agents/index.md
