+++
title = "Coreutils"
section = "ecosystem"
order = 3
sources = [
  "examples/coreutils/ (38 packages, README.md, campaign docs)",
  "examples/coreutils/packages/echo/src/main.fab",
]
+++

Faber reimplements GNU coreutils as application-lane proof. These are real
CLI programs demonstrating Faber building working binaries with argv, stdio,
exit codes, and host I/O, verified against host GNU utilities via a parity
harness.

## Implemented utilities {#implemented-utilities}

**Stage 1 — scaffold + true/false**
`true`, `false`

**Stage 2 — shared common helpers + inline tests**
`echo`, `basename`, `dirname`, `printf`, `seq`

**Stage 3 — nullable-stdin slices**
`cat`, `head`, `tail`, `wc`, `tac`, `uniq`, `fold`, `nl`, `expand`,
`unexpand`, `sort`, `cut`, `grep`, `tr`, `tee`, `paste`

**Scaffolded — Stage 5+**
`rm`, `cp`, `mv`, `mkdir`, `touch`, `pwd`, `readlink`, `realpath`,
`join`, `comm`, `od`, `cksum`, `split`, `yes`, `printenv`

## Example — echo {#example--echo}

The `echo` package demonstrates Faber patterns used throughout coreutils:
CLI annotations, option parsing, inline tests with `probandum`/`proba`/`adfirma`,
and shared common modules:

```faber
importa ex "norma:consolum" privata consolum
importa ex "../../../common/gnu/format" privata gnu_format

functio echo_textus(lista<textus> words) → textus {
    redde ""
}

functio echo_novam_lineam(lista<textus> words) → bivalens {
    redde falsum
}

probandum "echo formatting" tag "coreutils" {
    proba "empty operands" {
        adfirma echo_textus([]) ≡ ""
    }
    proba "-n suppresses newline" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }
}

@ cli "echo"
@ descriptio "GNU coreutils echo parity exemplum"
@ operandus ceteri textus words
incipit argumenta args {
    # ... CLI logic here
}
```

## Running {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
