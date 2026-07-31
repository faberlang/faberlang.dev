+++
title = "Norma standard library"
section = "ecosystem"
order = 1
sources = [
  "radix/README.md (Standard Library section)",
  "sibling norma/ repository",
  "norma/exempla/",
  "radix/docs/stdlib/morphologia.md",
  "radix/docs/stdlib/caelum-module-structure.md",
]
+++

Norma is Faber's standard library. It provides Latin-named modules accessed
through `norma:*` paths, with nested `norma:parent/child` submodule paths for
shared types and facades. Stdlib declarations are Faber source under the
sibling `norma` repository. Norma is a platform default — apps use it without
declaring it in `faber.toml` `[dependencies]`.

Modules marked **native** ship real Faber bodies today; **deferred** modules
are declared with `mori` stubs pending implementation; **target** modules are
committed in target form and do not compile yet.

## Modules {#modules}

| Module | Domain | Status |
|--------|--------|--------|
| `norma:aleator` | Entropy and randomness | native |
| `norma:arca` | Database device (postgres/mysql/sqlite) | deferred |
| `norma:caelum` | Network sockets (TCP/UDP) | deferred |
| `norma:chorda` | Text and cord operations, UTF-8 mechanical trio | native |
| `norma:codex` | Encoding and decoding (base64, hex, URL) | deferred |
| `norma:consolum` | Console I/O (stdin, stdout, stderr) | native |
| `norma:crypta` | Cryptography (hash, HMAC, cipher, sign) | partial |
| `norma:csv` | CSV wire format | native |
| `norma:fila` | Double-ended queue | target |
| `norma:http` | HTTP client and server | deferred |
| `norma:json` | JSON parsing and serialisation | native |
| `norma:mathesis` | Scalar math catalog | native |
| `norma:model` | Model metadata (safetensors/GGUF) | partial |
| `norma:nuncius` | IPC (shared memory, ports, sync primitives) | deferred |
| `norma:optimizer` | SGD optimizer steps | native |
| `norma:ordinata` | Key-ordered map | target |
| `norma:pressura` | Compression (gzip/deflate/brotli/zstd) | deferred |
| `norma:processus` | Process execution and environment | native |
| `norma:solum` | Filesystem operations | native |
| `norma:solum/path` | Pure pathname operations | native |
| `norma:tempus` | Time and duration | partial |
| `norma:tensor` | Tensor bridge helpers | native |
| `norma:thesaurus` | Cache and pub/sub | deferred |
| `norma:toml` | TOML parsing and serialisation | deferred |
| `norma:valor` | Codec-agnostic value-tree navigation | native |
| `norma:vector` | Vector register intrinsics | native |
| `norma:yaml` | YAML parsing and serialisation | deferred |

### Nested submodules {#nested-submodules}

Shared types and facades live under a parent module — every `.fab` file in a
subdirectory is a separately importable module:

| Import | Role |
|--------|------|
| `norma:caelum/terminus` | TCP endpoint type (`Terminus`) |
| `norma:caelum/connexus` | Connected socket type (`Connexus`) |
| `norma:caelum/auscultator` | TCP listener type (`Auscultator`) |
| `norma:json/pange` | JSON serialize facade |
| `norma:json/solve` | JSON parse facade |
| `norma:json/cursor` | Parser cursor type (`Resultus`) |
| `norma:json/lexica` | Shared lexical floor (internal) |

## Morphologia naming convention {#morphologia-naming-convention}

Norma follows the morphologia policy for all method names. Latin verb
conjugation carries execution mode; number carries flow. Two axes compose:
**time × flow** (sync/async × finite/stream) and **ownership** (mutate vs
copy-out).

Callable posture is a signature slot: bare means synchronous finite,
`fiet` an asynchronous finite function, `fiunt` a synchronous stream,
`fient` an asynchronous stream. `@ futura` / `@ cursor` remain accepted
compatibility spellings, but the posture words are the canonical surface.

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

Async finite verbs return `promissum<T>`; async streams yield values through
`cede`. The `pange` / `solve` / `tempta` mechanical trio covers wire encode /
decode across `json`, `toml`, `yaml`, `csv`, and `chorda`.

## Usage {#usage}

```faber
importa ex "norma:solum" privata solum

functio legeConfig() → textus {
    redde solum.lege("config.toml")
}
```

Test code can live beside product source in colocated `*.proba` files —
discovered only by `faber test`, never importable, and excluded from Cista
package snapshots.
