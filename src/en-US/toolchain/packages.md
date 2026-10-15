+++
title = "Packages"
section = "toolchain"
order = 3
sources = []
+++

A Faber package is a directory with a `faber.toml` manifest. `faber init`
writes one, and `faber check`, `build`, `run`, `test` and `format` all take the
package directory.

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
prefix. The other tables the manifest accepts are `[locale]` (the source
locale of the package), `[device]` (device selection for `faber run`),
`[target.<name>]` (per-target settings), `[dependencies]`, `[dispatch]` and
`[check]`. Unknown keys are rejected, so a misspelled key is an error, not a
silent no-op.

## What `faber build` writes {#build}

With no `-t`, `faber build` on a package writes the portable FHIR package
envelope under `target/faber-fhir/`. Pass `-t rust` to get a Cargo project,
or any other target listed by `faber targets`. A package that only needs to
run does not need a build: `faber run` interprets it on the MIR runner.

## Libraries {#libraries}

Norma, the standard library, is embedded in the `faber` binary: `import`
from `norma:*` needs no installation and no manifest entry. Other
libraries (`triga:*`, `gradus:*`, `tela:*`) are source checkouts. Point
`faber` at a directory that holds them with `--library-home <DIR>` or
`[paths] library_home` in `faber.toml`; `faber doctor` prints the resolved
library home and which libraries it can see.

## Dependencies {#dependencies}

`[dependencies]` lists direct dependencies as exact pins (`name =
"version"`); the resolved paths live in `faber.lock`. Both are plain files
you can read and commit.

## Cista {#cista}

Cista is a separate, experimental package-store project. It is not part of
the `faber` binary: `faber` has no `install` command, and the public package
registry (`cista.dev`) does not exist yet. Local package resolution works for
packages that sit side by side in one workspace.
