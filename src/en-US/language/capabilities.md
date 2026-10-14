+++
title = "Capabilities and frames"
section = "language"
order = 7
sources = []
+++

*The seam between Faber and every way an operating system can implement I/O.*

`ad` is Faber's low-level capability call primitive — the boundary
between Faber code and the outside world. It opens a typed conversation
(`sermo`) with a host resource identified by a route string, then
exchanges structured frames (`scrinium`) over directional half-streams.
The runtime dispatches each route to the native leaf that serves it, and that
leaf implements the actual I/O — filesystem, networking, console, time,
randomness, or anything else the OS can do.

## The `ad` primitive {#ad}

`ad` is a keyword, not a function. It opens an opaque conversation
with a route named by an `ascii` literal and optional opener data:

```text
# Simple materialized call: open, send opener, drain response
fixum textus content ← ad 'solum:lege' ("config.toml") ↦ textus

# Typed conversation handle for streaming interaction
fixum sermo s ← ad 'processus:exsequi' ("ls -la")
```

The route string follows a `prefix:verb` pattern. Dispatch matches on the
**prefix** — the leaf that owns a prefix handles all verbs under it:

```text
solum:lege   ─┐
solum:modum  ─┼─►  prefix "solum"  ──►  filesystem leaf
solum:vincula─┘
```

`ad` is not a foreign function interface. It does not call C
functions, load dynamic libraries, or embed inline assembly. It is a
structured message passing boundary: Faber sends typed frames and receives
typed frames, without knowing whether the answering side runs in-process,
delegates to a system call, or forwards to a remote host.

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

# Parse JSON from a file
fixum json data ← ad 'solum:lege' ("data.json") ↦ json
```

Materialization uses a type-directed collector: `↦ textus`
concatenates all inbound frames, `↦ json` parses the concatenated
payload, `↦ lista<T>` collects frames into a list.

## Native leaves {#providers}

Each effect family is served by a native leaf in the `faber-leaf` crate
(`radix/crates/faber-leaf`). The interpreter (`faber run`) and generated Rust
share it. Each leaf owns all verbs under its prefix:

| Leaf | Prefix | I/O domain |
|------|--------|------------|
| filesystem | `solum:*` | Read, write, metadata, directory operations |
| stdio | `consolum:*` | Console I/O: stdin, stdout, stderr |
| process | `processus:*` | Process execution, environment, working directory |
| clock | `tempus:*` | Time: now, monotonic, sleep |
| entropy | `aleator:*` | Randomness: floats, integers, bytes, uuid |
| tcp | `caelum:*` | TCP listen, connect, accept, read, write |
| http | `http:*` | HTTP client calls |
| websocket | `websocket:*` | WebSocket connect, accept, send, receive |

A route that no leaf serves is refused at run time. Faber code can also
answer a route itself with an `@ ad 'prefix:name'` handler on a top-level
function.

## Layer stack {#layers}

```text
Faber source:     ad 'solum:lege' (path) ↦ textus
Compiler:         sermo open + generic attach (no leaf crate names)
Runtime:          route lookup + conversation protocol
Leaf:             the filesystem leaf reads the file, returns content
```

The compiler emits generic dispatch — it never embeds leaf crate names into
generated code. Source names a route; the runtime decides which leaf answers
it.

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

functio exsequi(textus command) → textus {
    redde ad 'processus:exsequi' (command) ↦ textus
}
```

These wrapper functions provide type safety, documentation, and error
handling without hiding the fact that I/O crosses the `ad`
boundary. The Norma wrappers live under `radix/lib/norma/src/`.

## References {#references}

1. `radix/docs/design/frame-stream-types.md` — full spec for sermo, scrinium, status, meus, tuus
2. `radix/grammar/EBNF.md` — the `ad` expression and `@ ad` handlers (Capability Calls)
3. `radix/crates/faber-leaf/` — the native leaves
4. `radix/lib/norma/src/` — Norma wrappers over the routes
5. `radix/corpus/ad/` — sermo exempla files
