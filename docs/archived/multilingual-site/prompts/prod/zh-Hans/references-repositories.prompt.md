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

Faber is developed across multiple repositories under the `faberlang`
organisation.

## Public repositories {#public-repositories}

| Repository | Description |
|-----------|-------------|
| `faber` | User-facing CLI: check, build, run, test, format, explain |
| `faber-runtime` | Core runtime types (Valor, tensors, frames); crate name `faber` |
| `norma` | Standard library source (`norma:*` modules) |
| `triga` | Optional graphics/geometry library |
| `cista` | Package manager and store (experimental) |
| `examples` | Language corpus, coreutils, AI Workbench, reader-locale packages |
| `faberlang.dev` | This website |

## Private repositories {#private-repositories}

| Repository | Description |
|-----------|-------------|
| `radix` | Compiler: lexing, parsing, semantic analysis, HIR/MIR/AIR, diagnostics, codegen |

## Host platform repositories {#host-platform-repositories}

| Repository | Description |
|-----------|-------------|
| `host-kernel-rs` | Thin router: Frame, Conversation, prefix dispatch, structured errors |
| `host-native-rs` | Native attach: workers, register_providers hook |
| `host-providers-rs` | Provider implementations: solum, processus, consolum, tempus, aleator, http |
