+++
title = "Libraries"
section = "libraries"
order = 0
sources = []
+++

Two libraries matter today. **Norma** ships with the compiler and you can use
it immediately. **Triga** is an optional dependency you declare when you need
graphics or geometry.

## Norma — bundled {#norma}

The standard library. Imported as `norma:*`, no installation step, no entry in
`faber.toml`:

```faber
importa norma:solum
importa norma:textus
```

It covers I/O, collections, strings, math, and system interaction. It is
deliberately small — the surface that exists is stable, rather than broad and
provisional. [Norma →](/libraries/norma.html)

## Triga — opt in {#triga}

A native graphics and geometry engine written in Faber: math, scene graph,
materials, geometry, and resource types as `triga:*` modules. Declare it as a
Cista dependency in `faber.toml` and the compiler resolves it from the package
store.

Its shapes model the three.js abstractions so that models and people already
familiar with that vocabulary can move quickly — but Triga is **not** a binding
to three.js. These are native Faber types compiled to GPU shaders. The frames
on the [home page](/) were produced by it. [Triga →](/libraries/triga.html)

## The corpus — not a library {#corpus}

The **corpus** is the language's worked-example tree: one directory per
construct, each holding small programs that exercise it. It is the source of
truth for what the compiler supports, it generates the
[target matrix](/toolchain/target-matrix.html), and it is browsable at
[/corpus/](/corpus/).

You do not import it. You read it when you want to know how a construct
actually behaves rather than how it is described.
[About the corpus →](/libraries/corpus.html)

## Writing your own {#your-own}

A library is a package with `kind = "lib"` in its `faber.toml` and a
`[library] provider` name. `faber install` puts it in the Cista store; other
packages resolve it through `faber.lock`. See
[Packages with Cista](/toolchain/packages.html).
