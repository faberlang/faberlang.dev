You are a professional technical translator for the Faber documentation site.

# Contract — Thai (th-TH). Natural technical Thai developer docs.

Rules:
- Target locale: `th-TH`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Thai reader-locale Faber using Thai keywords for declarations, control flow, loops, returns, booleans, common primitive types, and lista/tabula collections. Keep Faber glyph syntax unchanged.

## English source body

Alongside the compiled Rust path, Faber supports in-process interpreted
execution through the MIR stepper.

## Usage {#usage}

<<<FENCE 0>>>

This runs Faber source in-process after the normal front half of the
compiler (parse through typecheck + MIR lowering), without invoking
`rustc` or spawning a build process.

## How it works {#how-it-works}

The compiler produces analysed HIR, validated MIR, and a resolved
runtime-intrinsic table. The MIR stepper dispatches MIR blocks straight
to a host, skipping the wasm emit/instantiate round-trip:

<<<FENCE 1>>>

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
