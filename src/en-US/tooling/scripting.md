+++
title = "In-process scripting"
section = "tooling"
order = 3
sources = [
  "radix/docs/design/faber-scripting.md",
]
+++

Alongside the compiled Rust path, Faber supports in-process interpreted
execution through the MIR stepper.

## Usage {#usage}

```bash
faber run --interpret script.fab
```

This runs Faber source in-process after the normal front half of the
compiler (parse through typecheck + MIR lowering), without invoking
`rustc` or spawning a build process.

## How it works {#how-it-works}

The compiler produces analysed HIR, validated MIR, and a resolved
runtime-intrinsic table. The MIR stepper dispatches MIR blocks straight
to a host, skipping the wasm emit/instantiate round-trip:

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck
                                                      ↓
                                                 MIR lowering
                                                      ↓
                                              MIR stepper + Host
```

## Latency {#latency}

The scripting path runs the same linear frontend as the compiled path,
plus stepper time proportional to what the script actually executes:

| Phase | Cost |
|-------|------|
| Frontend (100-line script) | ~0.6 ms |
| MIR stepping | Proportional to executed statements |

The stepper never invokes `rustc` or spawns a process, so startup is
fast enough to feel like a shell script.

## Limitations {#limitations}

- The MIR stepper does not support all host I/O routes that the compiled
  path does — some `norma:*` wrappers remain compiled-only
- The stepper is a MIR-native diagnostic/reference executor, not a
  production runtime for deployed applications
- Package compilation through Cargo remains the primary product path
