+++
title = "Norma — the standard library"
section = "libraries"
order = 1
sources = [
  "radix/README.md (Standard Library section)",
  "sibling norma/ repository",
  "norma/exempla/",
  "radix/docs/stdlib/morphologia.md",
  "radix/docs/stdlib/caelum-module-structure.md",
]
+++

Norma is Faber's standard library. It provides English-named modules accessed
through `norma:*` paths, with nested `norma:parent/child` submodule paths for
shared types and facades. Stdlib declarations are Faber source in the compiler
repository (`lib/norma/src/`) and are embedded in the `faber` binary. Norma is
a platform default — apps use it without declaring it in `faber.toml`
`[dependencies]`.

Module names are English: `norma:text`, `norma:fs`, `norma:console`. A Latin
spelling such as `norma:textus` is not a module name; it is rejected as
`PKG001 unknown_library_module`. Since 1.16 the check runs for every target
before any code is emitted, so an import of a module that does not exist
never passes `faber check`.

## Modules {#modules}

| Module | Domain |
|--------|--------|
| `norma:console` | Console I/O (stdin, stdout, stderr) |
| `norma:crypto` | Cryptography (hash, HMAC, cipher, sign) |
| `norma:csv` | CSV wire format |
| `norma:db` | SQLite connections, transactions and prepared writes ([below](#db)) |
| `norma:deque` | Double-ended queue |
| `norma:encoding` | Encoding and decoding (base64, hex, URL) |
| `norma:fault` | The I/O fault union (`IoFault`) |
| `norma:fs` | Filesystem operations |
| `norma:fs/path` | Pure pathname operations |
| `norma:http` | HTTP client and server |
| `norma:json` | JSON parsing and serialisation |
| `norma:math` | Scalar math catalog |
| `norma:net` | Network sockets (TCP) |
| `norma:order` | The ordering contract (`Orderable<T>`) |
| `norma:process` | Process execution and environment |
| `norma:random` | Entropy and randomness |
| `norma:sink` | The sinking contract (`Sink<T>`) and an in-memory `Collector`; checks but does not run yet ([Sinks](/language/types.html#sinks)) |
| `norma:sorted_map` | Key-ordered map |
| `norma:tensor` | Tensor bridge helpers |
| `norma:text` | Text and cord operations, UTF-8 `encode` / `decode` |
| `norma:time` | Time and duration |
| `norma:toml` | TOML parsing and serialisation |
| `norma:value` | Codec-agnostic value-tree navigation |
| `norma:vector` | Vector register intrinsics |
| `norma:websocket` | WebSocket client and HTTP-upgrade accept |

### Nested submodules {#nested-submodules}

Shared types and facades live under a parent module — every `.fab` file in a
subdirectory is a separately importable module:

| Import | Role |
|--------|------|
| `norma:net/endpoint` | TCP endpoint type (`Endpoint`) |
| `norma:net/connection` | Connected socket type (`Socket`) |
| `norma:net/listener` | TCP listener type (`Listener`) |
| `norma:json/serialize` | JSON serialize implementation |
| `norma:json/solve` | JSON parse implementation |
| `norma:json/cursor` | Parser cursor type (`ScanResult`) |
| `norma:json/lexer` | Shared lexical floor (internal) |
| `norma:http/headers` | HTTP header map |
| `norma:http/request` | Received HTTP request |
| `norma:http/response` | HTTP response |
| `norma:http/client` | HTTP client verbs |
| `norma:http/server` | HTTP/1.1 listener |
| `norma:http/chunked` | Chunked transfer codec |
| `norma:http/sse` | Server-sent events codec |

## Morphologia naming convention {#morphologia-naming-convention}

Norma follows the morphologia policy for all method names. Verb form carries
execution mode; number carries flow. Two axes compose:
**time × flow** (sync/async × finite/stream) and **ownership** (mutate vs
copy-out).

Callable posture is a signature slot: bare means synchronous finite,
`async` an asynchronous finite function, `generator` a synchronous stream,
`async_generator` an asynchronous stream. `@ future` / `@ cursor` remain
accepted compatibility spellings, but the posture words are the canonical
surface.

| Stem | Sync | Async | Meaning |
|------|------|-------|---------|
| `read-` | `read_file` | `read_file_async` | Read |
| `write-` | `write_file` | `write_file_async` | Write |
| `query-` | — | `query` | Query (finite) |
| `query-` | — | `query_stream` | Query (stream) |

Ownership pairs (mutate vs copy-out):

| Mutate | Copy-out | Meaning |
|--------|----------|---------|
| `add` | `added` | Add |
| `reverse` | `invert` | Reverse |
| `sort` | `sorted` | Sort |

Async finite verbs return `promise<T>`; async streams yield values through
`yield`. The mechanical trio covers wire encode / decode: `stringify` /
`parse` in `json`, `toml`, and `csv` (plus `try_parse` in `json` and `toml`),
and `encode` / `decode` / `try_decode` in `text`.

## Usage {#usage}

```faber locale=en
import from "norma:fs" fs
import from "norma:fault" fault

fn load_config() → string ⇥ fault.IoFault {
    return fs.read_file<string>("config.toml")
}
```

`read_file` is failable: its error channel is `fault.IoFault`, the union
of I/O fault kinds, so the caller handles it or passes it on.

For files that must never be left half-written, `norma:fs` has
`write_file_durably` and `write_bytes_durably`. They replace the file
atomically: a failure or an interruption leaves the previous complete file,
never a partial one.

## SQLite: `norma:db` {#db}

`norma:db` opens SQLite databases and writes to them through owned resources:
`Connection`, `Transaction` and `PreparedWrite`. It runs on the MIR runner and
generated Rust; other targets refuse it
(`SEM011 sermo_resource_target_unsupported`).

```faber locale=en
import from "norma:db" db

fn save(db.Connection connection, list<int> items) → void ⇥ db.DbFault {
    let db.Transaction transaction ← connection.begin("Immediate")
    let db.PreparedWrite insert ← transaction.prepare("INSERT INTO sample(value) VALUES (?1)")
    for from items let item {
        insert.execute([item ↦ value])
    }
    transaction.commit()
}

main {
    do {
        let db.Connection connection ← db.open(":memory:")
        connection.execute("CREATE TABLE sample (id INTEGER PRIMARY KEY, value INTEGER)", [])
        save(connection, [10, 20, 30])
        print connection.close() ⊥ false
    } catch fault {
        print fault.kind
    }
}
```

This prints `true`.

| Call | Result |
|---|---|
| `db.open(path)` | A `Connection`; `":memory:"` opens a private in-memory database |
| `connection.execute(sql, parameters)` | The number of rows changed |
| `connection.begin(mode)` | A `Transaction`; `mode` defaults to `"Deferred"` |
| `connection.prepare(sql)`, `transaction.prepare(sql)` | A reusable `PreparedWrite` |
| `writer.execute(parameters)` | The number of rows changed |
| `writer.execute_returning_id(parameters)` | An `InsertResult` with `rows_changed` and `returned_id`, from an explicit integer `RETURNING` column; transaction writers only |
| `transaction.commit()`, `transaction.rollback()` | Ends the transaction |
| `close()` | Closes the resource; a failable `bool` on `⇥ string` |

Parameters are always bound, as a `list<value>`. Everything but `close` reports
on `⇥ db.DbFault`, whose `kind` and `operation` say what failed; SQLite's own
codes are in `primary_code` and `extended_code`.

A resource lives in its scope. A transaction that was not committed rolls back
when it leaves scope, on a normal exit, an early `return` or an error. Retained
aliases share one native resource, so closing one closes them all, and using a
closed resource is a `Closed` fault. A resource cannot be duplicated: `copy` of a
`Connection`, or of anything holding one, is `SEM066`.

`norma:db` covers writes. Typed rows and cursors for reading results are not in
this module yet.

```faber locale=en
import from "norma:fs" fs
import from "norma:fault" fault

fn save_config(string text) → void ⇥ fault.IoFault {
    fs.write_file_durably("config.toml", text)
}
```

Test code can live beside product source in colocated `*.proba` files —
discovered only by `faber test`, never importable, and excluded from Cista
package snapshots.
