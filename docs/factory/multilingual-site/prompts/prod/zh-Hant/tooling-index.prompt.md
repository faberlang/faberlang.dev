You are a professional technical translator for the Faber documentation site.

# Contract — Traditional Chinese (zh-Hant / 繁體). Traditional only, never Simplified.

Rules:
- Target locale: `zh-Hant`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Traditional Chinese reader-locale Faber using Traditional Chinese keywords where the pack overrides Simplified Chinese rows, while preserving universal Faber glyph syntax.

## English source body

The Faber toolchain spans three tools: the `faber` CLI for building and
testing, the Radix compiler for code generation, and the Cista package
manager for dependency resolution.

## Faber build tool {#faber-cli}

The primary developer interface. Build, check, run, test, format, and
explain — all through one command. [Read more →](/tooling/faber-build-tool.html)

## Radix compiler {#radix}

The compiler backend. Lowers Faber source through HIR → MIR → AIR to
multiple target lanes. [Read more →](/tooling/radix-compiler.html)

## Cista package manager {#cista}

Package resolution and the public package store. Manages `faber.toml`
manifests and dependency locks. [Read more →](/tooling/cista-package-manager.html)

## Codegen targets {#codegen-targets}

Faber compiles to Rust (default), WASM, TypeScript, Go, and GPU/WGSL.
Each target lane has its own IR path and runtime binding.
[Read more →](/tooling/codegen-targets.html)

## Performance {#performance}

Measured compilation and execution performance across target lanes.
[Read more →](/tooling/performance.html)

## Scripting {#scripting}

Using Faber as a scripting language with the `faber run` command.
[Read more →](/tooling/scripting.html)
