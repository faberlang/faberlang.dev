+++
title = "Norma standard library"
section = "ecosystem"
order = 1
sources = [
  "radix/README.md (Standard Library section)",
  "sibling norma/ repository",
  "norma/exempla/",
  "radix/docs/stdlib/morphologia.md",
]
+++

Norma is Faber's standard library. It provides flat Latin-named modules
accessed through `norma:*` paths. Stdlib declarations are Faber source
under the sibling `norma` repository.

## Modules

| Module | Domain |
|--------|--------|
| `norma:solum` | Filesystem operations |
| `norma:solum/path` | Pure pathname operations |
| `norma:http` | HTTP client |
| `norma:processus` | Process execution |
| `norma:consolum` | Console I/O (stdin, stdout, stderr) |
| `norma:json` | JSON parsing and serialisation |
| `norma:toml` | TOML parsing |
| `norma:yaml` | YAML parsing |
| `norma:valor` | Codec navigation |
| `norma:tensor` | Tensor bridge helpers |
| `norma:tempus` | Time and duration |
| `norma:aleator` | Randomness |

## Morphologia naming convention

Norma follows the morphologia policy for all method names. Latin verb
conjugation carries execution mode:

| Stem | Sync | Async | Meaning |
|------|------|-------|---------|
| `leg-` | `lege` | `leget` | Read |
| `scrib-` | `scribe` | `scribet` | Write |
| `quaer-` | — | `quaeret` | Query (finite) |
| `quaer-` | — | `quaerent` | Query (stream) |

Ownership pairs (mutate vs copy-out):

| Mutate | Copy-out | Meaning |
|--------|----------|---------|
| `adde` | `addita` | Add |
| `inverte` | `inversa` | Reverse |
| `filtra` | `filtrata` | Filter |

## Usage

```faber
importa ex "norma:solum" privata solum

functio legeConfig() → textus {
    redde solum.lege("config.toml")
}
```
