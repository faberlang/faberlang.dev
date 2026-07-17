+++
title = "Triga graphics library"
section = "ecosystem"
order = 2
sources = [
  "sibling triga/ repository",
  "radix/README.md (mentions triga)",
]
+++

Triga is an optional public source library for geometry, scene, and
GPU-facing type contracts. In normal projects, declare Triga as a Cista
package dependency in `faber.toml`; Cista records the resolved source in
`faber.lock` and the compiler resolves it from the package store.

`FABER_LIBRARY_HOME` is for local development against sibling source
checkouts, or for explicit `--legacy-library-home` runs. It is not the
primary product path for consuming Triga.

Triga provides types and operations for:

- Geometry primitives (points, vectors, matrices, transforms)
- Scene graph structures
- GPU-facing type contracts that align with Faber's systems lane

Triga is not part of Norma. It is an optional dependency that packages
opt into when they need graphics or geometry work.
