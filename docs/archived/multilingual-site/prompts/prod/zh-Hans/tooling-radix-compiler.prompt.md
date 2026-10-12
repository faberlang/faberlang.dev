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

Radix is the Faber compiler. It is a private crate (`radix/`) that
implements the full compilation pipeline from source text to target
backends.

## Pipeline {#pipeline}

Radix lowers Faber source through three intermediate representations:

1. **HIR** (High-level IR) — the semantic core. Reader locale integration,
   type checking, and HIR-direct backends operate here.
2. **MIR** (Mid-level IR) — the execution-shaped IR. This is the semantic
   ownership boundary where borrowing and effect analysis run.
3. **AIR** (Autodiff IR) — a pure-functional transform for automatic
   differentiation and fusion, used by GPU target lanes.

## Target lanes {#target-lanes}

| Lane | IR | Output | Status |
|---|---|---|---|
| CPU runtime | MIR | FMIR (Rust runtime) | Shipping |
| LLVM | MIR | LLVM text | Experimental |
| WASM | MIR | WebAssembly text | Experimental |
| TypeScript | HIR | TypeScript source | Experimental |
| Go | HIR | Go source | Experimental |
| GPU/WGSL | AIR | WGSL via WGPU | Experimental |

## Architecture {#architecture}

Radix takes a text-emission approach rather than embedding LLVM. Target
backends produce text in their respective languages, which are then
compiled by the target's own toolchain. This keeps the compiler
self-contained and makes target output human-readable.

## Diagnostics {#diagnostics}

Radix emits structured diagnostic codes with stable identifiers:

- `LEX0xx` — lexer errors
- `PARSE0xx` — parser errors
- `SEM0xx` — semantic analysis errors
- `DEFER0xx` — deferred features (valid syntax, not yet implemented)

Every diagnostic can be explained via `faber explain <code>`.
