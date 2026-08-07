+++
title = "Radix 0.3.0"
section = "releases"
order = 96
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.3.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Minor release spanning **22 commits** (`v0.2.0..v0.3.0`). This release focuses on
editor tooling — a Prettier plugin for `.fab` source formatting, a standalone
tree-sitter grammar repository, and a polished Zed extension with syntax
highlighting — alongside CLI refinements and build/release tooling improvements.

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 22 |
| Date span | 2025-12-22 (09:28 → 10:57, same day) |

### Major tracks

#### Prettier plugin and `.fab` formatting

- Adds a Prettier plugin for Faber Romanus source files with 4-space indentation, Stroustrup brace style, 3+-item list breaking, and blank-line/comment preservation (`fons/prettier/` — parser, printer, comments, plugin entry) (`a02918ab0`)
- Adds `faber format <file.fab>` CLI command with `--check` flag for CI validation (`9186f7087`)
- Fixes `nulla`/`nonnulla` spacing in the Prettier printer — was collapsing `si nonnulla items` into `si nonnullaitems` (`bde289ca0`)
- Updates `exempla/qr_static.fab` — migrates `esto` → `fixum` to match current keyword conventions (`2330de7d9`)

#### Tree-sitter grammar extraction and Zed extension

- Moves grammar sources to a dedicated **`tree-sitter-faber-romanus`** GitHub repository; updates the Zed extension to reference the external repo (`7b8d02410`)
- Cleans up the in-repo grammar skeleton by removing unused bindings (Rust, Go, Python, Swift, Node, C) and stale artifacts (`69aec430d`)

#### Syntax highlighting

- Fixes `highlights.scm` node type references to match the actual parser output (`2256b9627`)
- Simplifies `highlights.scm` to remove impossible query patterns (`24d3d740a`)

#### Zed extension configuration

- Adds the full tree-sitter grammar source tree (`grammar.js`, `parser.c`, `scanner.c`, `grammar.json`, `node-types.json`, tree-sitter headers) at `editors/zed/grammars/faber_romanus/` (`9ed558437`)
- Creates the compiled WebAssembly grammar binary `faber_romanus.wasm` (`17cad3339`)
- Adds `repository` and `rev` fields to the Zed grammar config (`6dfe41280`)
- Fixes grammar path and naming in the Zed extension manifest (`579c98a41`)
- Aligns the Zed grammar with the actual parser syntax (`3c704cb05`)
- Updates the grammar revision pointer multiple times as the external repo evolved (`08410d9cd`, `fbe9444d9`, `223348a5c`)

#### CLI Latin aliases

- Adds Latin aliases for all CLI commands: `finge` (compile), `curre` (run), `proba` (check), `forma` (format) (`a864c8f21`)

#### Build and release tooling

- Adds `scripta/use` — a version-switching script that symlinks `faber` to a dev build (`opus/faber`) or a named release (`editiones/faber-<version>`) (`84d876757`)
- Cleans up `.bun-build` artifacts after build (`13c7eaef7`)
- Fixes the cleanup glob pattern to match hidden `.bun-build` files (`.*.bun-build`) (`9022da77d`)
- Fixes `scripta/release` to set the upstream branch on first push (`d922d98bf`)
- Bumps `package.json` version to `0.3.0` and publishes the release binary (`9c7b46016`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
