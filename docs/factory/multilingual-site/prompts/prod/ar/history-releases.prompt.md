You are a professional technical translator for the Faber documentation site.

# Contract — Arabic (ar). Natural technical Arabic; preserve RTL prose quality.

Rules:
- Target locale: `ar`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Arabic reader-locale Faber using Arabic keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged and keep source in logical order.

## English source body

Download prebuilt Faber CLI archives and browse every published tag in the [faberlang/releases](https://github.com/faberlang/releases) asset repository. This page is for **installing** the compiler CLI, not for building the compiler from source.

## Getting started {#getting-started}

| Path | What it covers |
|---|---|
| [Install and download](/start/install.html) | Current release, PATH setup, verify, first `faber check` |
| [Quick tour](/start/) | Language shape in a few minutes |
| [Hello, Faber](/start/hello.html) | First package |
| [Commands](/start/commands.html) | Daily CLI loop |
| [Projects](/start/projects.html) | Real package layout |
| [Examples](/start/examples.html) | Public sample packages |

Build-from-source instructions are intentionally **not** linked here. Use the prebuilt archives unless you work on the private compiler tree.

## Latest release — Faber 1.1.1 {#latest}

| Field | Value |
|---|---|
| **Product** | Faber CLI |
| **Version** | 1.1.1 |
| **Tag** | `faber-v1.1.1` |
| **Published** | 2026-07-17 |
| **GitHub** | [faber-v1.1.1](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1) |
| **License** | MIT |

### Binaries {#latest-binaries}

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| **macOS arm64** | [faber-v1.1.1-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | 5.1 MB | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | 5.7 MB | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

Extract the archive and put the `faber` binary on your `PATH`. Step-by-step: [Install and download](/start/install.html).

## Historical releases {#historical}

Every tag currently published under [github.com/faberlang/releases](https://github.com/faberlang/releases/releases), newest first. **Faber** tags are the user CLI. **Radix** tags are historical compiler CLI archives (most are macOS arm64 only).

_Inventory snapshot from the GitHub Releases API. 41 tags, regenerated for this page._

### `faber-v1.1.1` {#faber-v1-1-1}

**Faber CLI** · published 2026-07-17 · [GitHub release](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [faber-v1.1.1-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | 5.1 MB | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| Linux x64 | [faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | 5.7 MB | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

### `radix-v0.75.0` {#radix-v0-75-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.75.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.75.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.75.0/radix-v0.75.0-aarch64-apple-darwin.tar.gz) | 3.1 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.75.0/radix-v0.75.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.74.0` {#radix-v0-74-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.74.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.74.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.74.0/radix-v0.74.0-aarch64-apple-darwin.tar.gz) | 3.1 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.74.0/radix-v0.74.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.70.0` {#radix-v0-70-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.70.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.70.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.70.0/radix-v0.70.0-aarch64-apple-darwin.tar.gz) | 2.8 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.70.0/radix-v0.70.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.69.0` {#radix-v0-69-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.69.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.69.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.69.0/radix-v0.69.0-aarch64-apple-darwin.tar.gz) | 2.8 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.69.0/radix-v0.69.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.68.0` {#radix-v0-68-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.68.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.68.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.68.0/radix-v0.68.0-aarch64-apple-darwin.tar.gz) | 2.8 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.68.0/radix-v0.68.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.67.0` {#radix-v0-67-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.67.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.67.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.67.0/radix-v0.67.0-aarch64-apple-darwin.tar.gz) | 2.6 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.67.0/radix-v0.67.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.66.0` {#radix-v0-66-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.66.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.66.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.66.0/radix-v0.66.0-aarch64-apple-darwin.tar.gz) | 2.6 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.66.0/radix-v0.66.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.65.0` {#radix-v0-65-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.65.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.65.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.65.0/radix-v0.65.0-aarch64-apple-darwin.tar.gz) | 2.1 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.65.0/radix-v0.65.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.64.0` {#radix-v0-64-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.64.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.64.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.64.0/radix-v0.64.0-aarch64-apple-darwin.tar.gz) | 2.0 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.64.0/radix-v0.64.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.63.0` {#radix-v0-63-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.63.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.63.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.63.0/radix-v0.63.0-aarch64-apple-darwin.tar.gz) | 2.0 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.63.0/radix-v0.63.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.62.0` {#radix-v0-62-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.62.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.62.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.62.0/radix-v0.62.0-aarch64-apple-darwin.tar.gz) | 2.0 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.62.0/radix-v0.62.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.61.0` {#radix-v0-61-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.61.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.61.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.61.0/radix-v0.61.0-aarch64-apple-darwin.tar.gz) | 2.0 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.61.0/radix-v0.61.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.60.0` {#radix-v0-60-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.60.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.60.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.60.0/radix-v0.60.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.60.0/radix-v0.60.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.59.0` {#radix-v0-59-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.59.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.59.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.59.0/radix-v0.59.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.59.0/radix-v0.59.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.58.0` {#radix-v0-58-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.58.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.58.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.58.0/radix-v0.58.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.58.0/radix-v0.58.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.57.0` {#radix-v0-57-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.57.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.57.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.57.0/radix-v0.57.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.57.0/radix-v0.57.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.56.0` {#radix-v0-56-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.56.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.56.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.56.0/radix-v0.56.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.56.0/radix-v0.56.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.55.0` {#radix-v0-55-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.55.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.55.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.55.0/radix-v0.55.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.55.0/radix-v0.55.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.54.0` {#radix-v0-54-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.54.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.54.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.54.0/radix-v0.54.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.54.0/radix-v0.54.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.53.0` {#radix-v0-53-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.53.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.53.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.53.0/radix-v0.53.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.53.0/radix-v0.53.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.52.0` {#radix-v0-52-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.52.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.52.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.52.0/radix-v0.52.0-aarch64-apple-darwin.tar.gz) | 1.8 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.52.0/radix-v0.52.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.51.0` {#radix-v0-51-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.51.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.51.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.51.0/radix-v0.51.0-aarch64-apple-darwin.tar.gz) | 1.8 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.51.0/radix-v0.51.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.50.0` {#radix-v0-50-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.50.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.50.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.50.0/radix-v0.50.0-aarch64-apple-darwin.tar.gz) | 1.8 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.50.0/radix-v0.50.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.49.0` {#radix-v0-49-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.49.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.49.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.49.0/radix-v0.49.0-aarch64-apple-darwin.tar.gz) | 1.8 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.49.0/radix-v0.49.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.48.0` {#radix-v0-48-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.48.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.48.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.48.0/radix-v0.48.0-aarch64-apple-darwin.tar.gz) | 1.8 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.48.0/radix-v0.48.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.47.0` {#radix-v0-47-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.47.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.47.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.47.0/radix-v0.47.0-aarch64-apple-darwin.tar.gz) | 1.8 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.47.0/radix-v0.47.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.46.0` {#radix-v0-46-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.46.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.46.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.46.0/radix-v0.46.0-aarch64-apple-darwin.tar.gz) | 1.4 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.46.0/radix-v0.46.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.45.0` {#radix-v0-45-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.45.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.45.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.45.0/radix-v0.45.0-aarch64-apple-darwin.tar.gz) | 1.4 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.45.0/radix-v0.45.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.44.0` {#radix-v0-44-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.44.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.44.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.44.0/radix-v0.44.0-aarch64-apple-darwin.tar.gz) | 1.4 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.44.0/radix-v0.44.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.43.0` {#radix-v0-43-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.43.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.43.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.43.0/radix-v0.43.0-aarch64-apple-darwin.tar.gz) | 1.4 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.43.0/radix-v0.43.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.42.0` {#radix-v0-42-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.42.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.42.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.42.0/radix-v0.42.0-aarch64-apple-darwin.tar.gz) | 1.4 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.42.0/radix-v0.42.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.41.0` {#radix-v0-41-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.41.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.41.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.41.0/radix-v0.41.0-aarch64-apple-darwin.tar.gz) | 1.4 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.41.0/radix-v0.41.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.40.0` {#radix-v0-40-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.40.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.40.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.40.0/radix-v0.40.0-aarch64-apple-darwin.tar.gz) | 1.3 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.40.0/radix-v0.40.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.39.0` {#radix-v0-39-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.39.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.39.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.39.0/radix-v0.39.0-aarch64-apple-darwin.tar.gz) | 1.3 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.39.0/radix-v0.39.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.38.0` {#radix-v0-38-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.38.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.38.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.38.0/radix-v0.38.0-aarch64-apple-darwin.tar.gz) | 1.2 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.38.0/radix-v0.38.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.37.0` {#radix-v0-37-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.37.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.37.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.37.0/radix-v0.37.0-aarch64-apple-darwin.tar.gz) | 1.1 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.37.0/radix-v0.37.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.36.0` {#radix-v0-36-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.36.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.36.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.36.0/radix-v0.36.0-aarch64-apple-darwin.tar.gz) | 1.1 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.36.0/radix-v0.36.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.35.0` {#radix-v0-35-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.35.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.35.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.35.0/radix-v0.35.0-aarch64-apple-darwin.tar.gz) | 993 KB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.35.0/radix-v0.35.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.34.0` {#radix-v0-34-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.34.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.34.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.34.0/radix-v0.34.0-aarch64-apple-darwin.tar.gz) | 981 KB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.34.0/radix-v0.34.0-aarch64-apple-darwin.tar.gz.sha256) |

### `radix-v0.32.0` {#radix-v0-32-0}

**Radix compiler** · published 2026-07-16 · [GitHub release](https://github.com/faberlang/releases/releases/tag/radix-v0.32.0)

| Platform | Archive | Size | SHA-256 |
|---|---|---|---|
| macOS arm64 | [radix-v0.32.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.32.0/radix-v0.32.0-aarch64-apple-darwin.tar.gz) | 1.1 MB | [checksum](https://github.com/faberlang/releases/releases/download/radix-v0.32.0/radix-v0.32.0-aarch64-apple-darwin.tar.gz.sha256) |

## Source of truth {#source-of-truth}

Assets live in the public [faberlang/releases](https://github.com/faberlang/releases) repository. When a new tag is published, regenerate this page with `generator/scripts/generate-releases-page.py` and rebuild the site.

## See also {#see-also}

| Link | Role |
|---|---|
| [Install and download](/start/install.html) | Recommended install path |
| [History](/history/) | Project timeline and origins |
| [faberlang/releases on GitHub](https://github.com/faberlang/releases/releases) | Raw tag list and assets |
