+++
title = "Libraries"
section = "libraries"
order = 0
sources = []
+++

**Norma** ships with the compiler and you can use it immediately. **Triga**,
**Gradus**, and **Tela** are optional source libraries you point `faber` at
when you need graphics work, automatic differentiation, or typed views. **Inferentia** is an
application built on them, still in development.

## Norma — bundled {#norma}

The standard library. Imported as `norma:*`, no installation step, no entry in
`faber.toml`:

```faber
importa ex "norma:fs" fs
importa ex "norma:text" text

incipit {
    nota "ready"
}
```

It covers I/O, collections, strings, math, and system interaction. It is
deliberately small — the surface that exists is stable, rather than broad and
provisional. [Norma →](/libraries/norma.html)

## Triga — opt in {#triga}

A native graphics and geometry engine written in Faber: math, scene graph,
materials, geometry, and resource types as `triga:*` modules. Check out the
`triga` repository and give `faber` its location with `--library-home` (or
`[paths] library_home` in `faber.toml`); `faber doctor` confirms it is found.

Its shapes model the three.js abstractions so that models and people already
familiar with that vocabulary can move quickly — but Triga is **not** a binding
to three.js. These are native Faber types compiled to GPU shaders. The frames
on the [home page](/) were produced by it. [Triga →](/libraries/triga.html)

## Gradus — opt in {#gradus}

Automatic differentiation, losses, optimizers, and neural-network primitives
as `gradus:*` modules. Reverse-mode gradients are a Radix compiler transform —
a function annotated `@ radix backward` gets a generated companion that
computes its gradients — and Gradus is the library surface over that
mechanism, so model code calls functions instead of hand-writing annotations.

It is JAX-shaped: models are pure `(params, x) → y` functions with explicit
parameters, and there is no module class hierarchy or runtime tape. It is also
pre-1.0 and narrower than its module list suggests — most of it is a
structural contract surface, and training is CPU-correct rather than fast.
[Gradus →](/libraries/gradus.html)

## Tela — opt in {#tela}

A view library: typed HTML and SVG values, a fail-closed serializer that turns
a valid tree into markup, and the DOM and Canvas2D contracts for a browser
host. Imported as `tela:*`. It is early; read its status page before
relying on it. [Tela →](/libraries/tela.html)

## Inferentia — an application {#inferentia}

A local-first inference server written in Faber: a command line and a small
HTTP API over a GGUF model, built on Gradus and Norma. It is not a library and
not a released product. The page states what exists and what does not.
[Inferentia →](/libraries/inferentia.html)

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

A library is a package with `kind = "lib"` in its `[build]` table in
`faber.toml` and a `[library] provider` name. Other packages import it as
`provider:module` once its parent directory is the library home. See
[Packages](/toolchain/packages.html).
