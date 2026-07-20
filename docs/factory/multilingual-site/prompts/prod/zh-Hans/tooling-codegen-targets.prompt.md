You are a professional technical translator for the Faber documentation site.

# Contract — Simplified Chinese (zh-Hans / 简体). Simplified characters only.

Rules:
- Target locale: `zh-Hans`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Simplified Chinese reader-locale Faber using Chinese keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged.

## English source body

Faber has one language and many compilation contracts. Not every feature
must lower to every target. This page documents which features each target
supports, erases, warns on, or rejects.

## Policy verbs {#policy-verbs}

| Verb | Meaning |
|------|---------|
| **Support** | Lowers with intended semantics |
| **Erase** | Typechecks; codegen drops target-specific semantics |
| **Warn** | Legal Faber; no effect or degraded behaviour on target |
| **Reject** | Check or emit fails with explicit diagnostic |
| **Defer** | Parses/binds; lowering not implemented for any target |
| **Limited** | Stable contract with explicit subset gates |

## Target table {#target-table}

| Target | Lane | Build | Run | Package | Policy |
|--------|------|-------|-----|---------|--------|
| `rust` | HIR | yes | yes | yes | **Support** |
| `fmir-text` | MIR | yes | yes | yes | **Support** |
| `fmir` | MIR | yes | yes | yes | **Support** |
| `fmir-bin` | MIR | yes | yes | yes | **Support** |
| `faber` | HIR | yes | no | no | **Support** |
| `ts` | HIR | yes | no | no | **Probe** |
| `go` | HIR | yes | no | no | **Erase** |
| `wasm` | MIR | yes | no | no | **Limited** |
| `wasm-text` | MIR | yes | no | no | **Limited** |
| `llvm-text` | MIR | yes | no | no | **Limited** |
| `metal-text` | MIR | yes | no | no | **Limited** |
| `wgsl-text` | MIR | yes | no | no | **Limited** |
| `sexp` | MIR | yes | no | no | **Limited** |

## Pipeline routing {#pipeline-routing}

<<<FENCE 0>>>

## Application lane (HIR) {#application-lane-hir}

| Target | Measured floor |
|--------|---------------|
| Rust | Production path. Borrow modes, CLI generation, failable Result lowering. |
| Faber | Canonical source view / round-trip. Not an execution backend. |
| TypeScript | 288/318 analysed · 268/318 typecheck-valid · 262/318 runnable |
| Go | 146/216 pass. Borrow modes erased; `ad` rejected. |

## Systems lane (MIR) {#systems-lane-mir}

| Target | Measured floor |
|--------|---------------|
| fmir* | Package MIR images; runner proves source independence. |
| wasm | 200/289 emitted · 195/289 validate · 171/289 stub-host runnable |
| llvm-text | 249/289 emitted · 232/289 verifier-valid · 65/289 runnable |
| metal-text | Device-safe kernel subset; 88 focused tests. Campaign paused. |
| wgsl-text | Validates with naga 30.x. 87 focused tests. Reflection sidecar. |
| sexp | 193 emitted · 190 Racket-compiled · 190 Racket-run. Validation target. |

For live capability flags, run `faber targets`.
