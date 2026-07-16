+++
title = "Tooling and compiler"
section = "tooling"
order = 0
sources = []
+++

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
