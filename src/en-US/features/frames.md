+++
title = "Capability calls and frames"
section = "features"
order = 3
sources = []
+++

*The seam between Faber and every way an operating system can implement I/O.*

`ad` is Faber's low-level capability call primitive — the boundary
between Faber code and the outside world. It opens a typed conversation
(`sermo`) with a host resource identified by a route string, then
exchanges structured frames (`scrinium`) over directional half-streams.
The host kernel dispatches each route to a pluggable provider crate, which
implements the actual I/O — filesystem, networking, console, time, randomness,
or anything else the OS can do.

## The `ad` primitive {#ad}

`ad` is a keyword, not a function. It opens an opaque conversation
with a route named by an `ascii` literal and optional opener data:

```text
# Simple materialized call: open, send opener, drain response
fixum textus content ← ad 'solum:lege' ("config.toml") ↦ textus

# Typed conversation handle for streaming interaction
fixum sermo s ← ad 'processus:curre' ("ls", ["-la"])
```

The route string follows a `prefix:verb` pattern. The host kernel
matches on the **prefix only** — the provider owns all verbs under that
prefix:

```text
solum:lege   ─┐
solum:modum  ─┼─►  prefix "solum"  ──►  solum provider crate
solum:vincula─┘
```

`ad` is not a foreign function interface. It does not call C
functions, load dynamic libraries, or embed inline assembly. It is a
structured message passing boundary: Faber sends typed frames and receives
typed frames, without knowing whether the provider is implemented in Rust,
runs in-process, delegates to a system call, or forwards to a remote host.

## Frame types {#types}

Five compiler-owned types form the frame system:

| Type | Role | Key surface |
|------|------|-------------|
| `sermo` | Conversation handle — an in-flight bidirectional exchange | Created by `ad`; drained via `↦ T` or split into views |
| `scrinium<T>` | Frame envelope — one structured message in a conversation | Fields: `id`, `call`, `status`, `data`, `created_ms`, `from`, `trace` |
| `status` | Lifecycle marker enum | `request`, `item`, `byte`, `bulk`, `done`, `error`, `cancel` |
| `meus<T>` | Outbound half-stream — send frames to the provider | `da(T)`, `fini() → status` |
| `tuus<T>` | Inbound half-stream — receive frames from the provider | `accipe()`, `cursor()`, `exhauri()`, `fini()` |

### Using directional views {#using-directional-views}

```text
# Open a conversation, get directional views
fixum sermo s ← ad 'solum:scribe' ("output.txt")
fixum meus<textus> out ← s.meus<textus>()
fixum tuus<textus> input ← s.tuus<textus>()

# Send content frames
out.da("line one")
out.da("line two")
out.fini()

# Read response frames
itera ex input.cursor() fixum frame {
    nota frame.data
}
fixum status inbound ← input.fini()
```

### Simple materialization {#simple-materialization}

For the common case — open, send opener, drain all response frames into one
value — `sermo ↦ T` collapses the conversation:

```text
# Read a file: open + drain into textus
fixum textus body ← ad 'solum:lege' ("config.toml") ↦ textus

# Parse JSON from an HTTP response
fixum json data ← ad 'http:peti' ("https://api.example.com/data") ↦ json
```

Materialization uses a type-directed collector: `↦ textus`
concatenates all inbound frames, `↦ json` parses the concatenated
payload, `↦ lista<T>` collects frames into a list.

## Host providers {#providers}

Effect families are implemented as separate provider crates under
`faberlang/host-providers-rs`. Each provider owns all verbs under
its prefix:

| Provider | Prefix | I/O domain |
|----------|--------|------------|
| `solum` | `solum:*` | Filesystem: read, write, metadata, directory operations |
| `processus` | `processus:*` | Process execution: spawn, pipe, exit codes |
| `consolum` | `consolum:*` | Console I/O: stdin, stdout, stderr |
| `tempus` | `tempus:*` | Time: now, sleep, timers |
| `aleator` | `aleator:*` | Randomness: entropy, distributions |
| `http` | `http:*` | HTTP client (Tier D, when landed) |

Providers are separate crates with their own dependencies — `solum`
does not pull in HTTP, `http` does not pull in filesystem code.
Each provider exports a `register()` function that the generated
host manifest calls at startup.

## Layer stack {#layers}

```text
Faber source:     ad 'solum:lege' (path) ↦ textus
Compiler:         sermo open + generic attach (no provider crate names)
Runtime:          HostDispatch + conversation protocol (faber-runtime)
Kernel:           route(frame) → provider for prefix
Provider:         solum provider reads file, returns content
```

The compiler emits generic dispatch — it never embeds provider crate names
into generated code. The runtime provides `HostDispatch` and the
conversation protocol. The kernel (from `host-kernel-rs`) routes
frames to the correct provider based on prefix. The provider (from
`host-providers-rs`) performs the actual I/O.

This means generated Faber code is **provider-neutral**. The same compiled
binary can be linked against different provider implementations — a real
filesystem provider for production, a mock provider for testing — by changing
the compile manifest.

## Compile manifest {#manifest}

Which providers to link is controlled by the generated compile manifest and
the `faber.toml` `[dispatch]` table:

```text
[target.rust]
host = "native"

[dispatch]
providers = ["solum", "processus", "consolum", "tempus", "aleator"]

[dispatch.providers.http]
enabled = true
```

During authoring, missing providers produce a runtime `E_NO_ROUTE`
error. In strict mode (future), every `ad` prefix in the program
must appear in the compile manifest, and the compiler validates that the
provider's capability manifest covers the routes used.

## Architecture {#architecture}

The host platform is split across three repositories in the
`faberlang` organisation:

| Repository | Role |
|------------|------|
| `host-kernel-rs` | Thin router — owns `Frame`, `Conversation`, terminal lifecycle, prefix dispatch, structured errors (`E_NO_ROUTE`), capability manifest aggregation |
| `host-native-rs` | Native attach — workers, `register_providers` startup hook, generated `host_register.rs` integration |
| `host-providers-rs` | Provider implementations — Cargo workspace with per-family crates (`solum`, `processus`, etc.) |

Each provider crate owns its own native dependencies. The `http`
provider pulls in `hyper` and `tokio` only when HTTP
is enabled. The `solum` provider uses standard file APIs with no
additional network dependencies.

> **Same route, any host.** Because `ad` dispatches on route strings and providers are pluggable, the same Faber source can target a native binary (host-native-rs), a WASM runtime (host-kernel as a Frame/Wasm adapter), or a TypeScript Node.js process (host-providers-ts) without changing a single line of Faber code.

## Norma wrappers {#stdlib}

Most Faber code does not call `ad` directly. The Norma standard
library wraps common `ad` routes in typed functions:

```text
# Norma wraps ad in typed, reviewed functions
functio lege(textus via) → textus {
    redde ad 'solum:lege' (via) ↦ textus
}

functio scribe(textus via, textus content) → vacuum {
    fixum vacuum _ ← ad 'solum:scribe' (via, content) ↦ vacuum
}

functio curre(textus command, lista<textus> args) → textus {
    redde ad 'processus:curre' (command, args) ↦ textus
}
```

These wrapper functions provide type safety, documentation, and error
handling without hiding the fact that I/O crosses the `ad`
boundary. The Norma wrappers are open source and live under
`norma/src/`.

## References {#references}

1. `radix/docs/design/frame-stream-types.md` — full spec for sermo, scrinium, status, meus, tuus
2. `radix/docs/design/host-provider-gateway.md` — thin router architecture, provider contracts, compile manifest
3. `faberlang/host-kernel-rs/` — kernel router implementation
4. `faberlang/host-native-rs/` — native attach and registration
5. `faberlang/host-providers-rs/` — provider crates (solum, processus, consolum, tempus, aleator, http)
6. `examples/corpus/ad/` — sermo exempla files
