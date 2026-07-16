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
GPU-facing type contracts. It is resolved through `FABER_LIBRARY_HOME`
and installable as a Cista source package.

Triga provides types and operations for:

- Geometry primitives (points, vectors, matrices, transforms)
- Scene graph structures
- GPU-facing type contracts that align with Faber's systems lane

Triga is not part of Norma. It is an optional dependency that packages
opt into when they need graphics or geometry work.
