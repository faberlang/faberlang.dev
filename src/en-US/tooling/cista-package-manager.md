+++
title = "Cista package manager"
section = "tooling"
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

```text
faber.toml

[nomen]
speculum-gen

[ingressus]
main.fab

[scopulus]
rust

[genus]
bin
```

The `[nomen]` field is the package name, `[ingressus]` is the entry
point module, `[scopulus]` selects the codegen target, and `[genus]`
declares the package kind (`bin` for executables, `lib` for libraries).

## Dependencies {#dependencies}

Packages declare dependencies that Cista resolves from the package store.
Dependency resolution produces a lock file that ensures reproducible
builds.

## Status {#status}

Cista is under active development. The public package registry
(`cista.dev`) is a separate campaign from the site implementation. Local
package resolution works for packages within the same workspace.
