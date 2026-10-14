+++
title = "Packages with Cista"
section = "toolchain"
order = 3
sources = [
  "cista/README.md",
]
+++

Cista is the Faber package manager. It handles package resolution,
dependency management, and the public package store.

## Overview {#overview}

Cista manages Faber packages defined by `faber.toml` manifests. Each
package declares its name, entry point, target backend, and dependencies.

## Package manifest {#manifest}

```toml
# faber.toml, as `faber init` writes it
[package]
name = "demo"
version = "0.1.0"
edition = "2026"

[paths]
source = "src"
entry = "main.fab"

[build]
kind = "bin"
```

`[package]` carries the package name, version, and Faber edition. `[paths]`
names the source directory (`src` or `.`) and, for an executable, the entry
module relative to it; `library_home` there overrides where provider
libraries are found. `[build]` declares the package kind (`bin` for
executables). A library package adds a `[library]` table with its `provider`
prefix. Optional: a backend `target` key under `[build]`, and `[locale]`,
`[device]`, and `[dependencies]` tables. Unknown keys are rejected, so a
misspelled key is an error, not a silent no-op.

## Dependencies {#dependencies}

Packages declare dependencies that Cista resolves from the package store.
Dependency resolution produces a lock file that ensures reproducible
builds.

## Status {#status}

Cista is under active development. The public package registry
(`cista.dev`) is a separate campaign from the site implementation. Local
package resolution works for packages within the same workspace.
