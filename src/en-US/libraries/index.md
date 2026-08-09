+++
title = "Libraries"
section = "libraries"
order = 0
sources = []
+++

**Norma** ships with the compiler and you can use it immediately. **Triga**
and **Gradus** are optional dependencies you declare when you need graphics
work or automatic differentiation.

## Norma — bundled {#norma}

The standard library. Imported as `norma:*`, no installation step, no entry in
`faber.toml`:

```faber
importa ex "norma:solum" privata solum
importa ex "norma:textus" privata textus

incipit {
    nota "ready"
}
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

## Gradus — opt in {#gradus}

Automatic differentiation, losses, optimizers, and neural-network primitives
as `gradus:*` modules. Reverse-mode gradients are a Radix compiler transform —
a function annotated `@ radix backward` gets a generated companion that
computes its gradients — and Gradus is the library surface over that
mechanism, so model code calls functions instead of hand-writing annotations.

It is JAX-shaped: models are pure `(params, x) → y` functions with explicit
parameters, and there is no module class hierarchy or runtime tape. It is also
pre-1.0 and narrower than its module list suggests — shapes are concrete
overloads rather than generics, and training is CPU-correct rather than fast.
[Gradus →](/libraries/gradus.html)

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
