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

A failing check prints each diagnostic as a block (diagnostics are on by
default since 1.17): the code and slug, the phase, the file, the span, the
source line, the message and a `help` sentence. After the last block, one
`explain:` line names the `faber explain` query for the first error that has an
entry:

```text
error[SEM010:expression_type_mismatch] analysis src/main.fab
phase: analysis
file: src/main.fab
span: 25..29
source:     let int x ← "no"
message: expression type mismatch
help: provide a value of the required type, or convert it with `↦` when supported
explain: faber explain SEM010.expression_type_mismatch
```

`faber check --no-diagnostics` gives the compact form, one line per diagnostic
carrying its code and slug, with no message, help or footer:

```text
error[SEM010:expression_type_mismatch]: src/main.fab:2
```

`--no-diagnostics` is accepted by `check`, `build`, `run`, `test`, `emit`,
`format` and `convert`. The old `--diagnostics` flag is gone from all of them.
JSON output and exit codes are the same in both forms.

`--diagnostics-locale zh-Hans` sets the language of the message and the help
text, independently of the source file's own locale. The code and the slug
stay ASCII.

`faber explain` looks a code up on its own, and `--json` makes the answer
machine-readable:

```bash
faber explain SEM010
faber explain SEM010 --json
```

`faber explain SEM010` reports `type mismatch` with the help `make the
expression type match the expected type`; `faber explain
SEM010.expression_type_mismatch` is the entry for this exact failure. `--json`
returns `{code, locale, message, help}`.

Fetch list: https://faberlang.dev/agents/index.md
