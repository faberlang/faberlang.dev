+++
title = "Gradus — autograd and ML"
section = "libraries"
order = 3
sources = [
  "sibling gradus/ repository",
  "gradus/README.md",
  "gradus/src/gradus.fab",
  "gradus/faber.toml",
]
+++

Gradus is Faber's library for automatic differentiation, losses, optimizers,
neural-network primitives, and training mechanics. The name is the Latin for
*step, pace, degree* — the root of *gradient*. It is imported as `gradus:*`
and declared as a Cista dependency, the same way as [Triga](/libraries/triga.html).

Gradus does not implement autograd. Reverse-mode differentiation is a compiler
transform inside Radix: a function annotated `@ radix backward` gets a
generated companion function that computes its gradients. Gradus wraps that
mechanism in a library surface so model code calls functions instead of
writing compiler annotations by hand.

The current package version is 0.1.0. Read the [status](#status) section
before planning work on it — the shipped surface is deliberately narrow.

## JAX-shaped, not PyTorch-shaped {#shape}

Models are pure functions of the form `(params, x) → y`. Parameters are
ordinary values you carry and pass; there is no module class hierarchy, no
implicit parameter registry, and no runtime tape. The backward pass is
generated code, not a replayed graph.

The practical consequence is that everything is explicit. A training step
takes the current parameters, the trainable gradients, and a learning rate,
and returns the updated parameters — nothing is mutated behind your back and
nothing is discovered at runtime.

Gradus is also **self-contained**: it imports nothing from Norma or any
sibling library, so a Gradus user imports only from `gradus:*`. The overlap
with Norma's math is deliberate isolation, not duplication waiting to be
cleaned up.

## Modules {#modules}

Each `gradus:<stem>` import resolves to `src/<stem>.fab`. Like Norma and
Triga, the layout is flat leaves with one concern per import path, and there
is no type re-export — import the leaf that owns what you use.

| Import | Owns |
|--------|------|
| `gradus:tensor` | Tensor construction, shape/dtype facts, value storage, element access. Plain values, **not** autograd-aware |
| `gradus:dtype` | The `DType` tag and casting contract |
| `gradus:shape` | Shape representation and rules: broadcast, reshape, expand |
| `gradus:math` | Pure operation families over tensors: elementwise, reduce, matmul, cast, concat/slice |
| `gradus:parameter` | Parameter identity and traversal |
| `gradus:serialize` | Versioned bytes wire format |
| `gradus:gradient` | The `@ radix backward` wrapper: forward call plus its companion gradient call |
| `gradus:loss` | Loss functions |
| `gradus:optimize` | Optimizers and learning-rate schedules |
| `gradus:nn` | Differentiable primitives: linear, activation, norm |
| `gradus:attention` | Scaled dot-product attention |
| `gradus:transformer` | Transformer block |
| `gradus:train` | Training-step mechanics |
| `gradus:data` | Batching, shuffling, tokenization |
| `gradus:gradus` | Package map facade only — holds no genera |

```faber mode=package
importa ex "gradus:tensor" privata tensor
importa ex "gradus:math" privata math
importa ex "gradus:gradient" privata gradient
importa ex "gradus:loss" privata loss
importa ex "gradus:optimize" privata optimize
```

The `gradus:tensor` / `gradus:gradient` split is the one to internalise:
tensor values are plain data, and differentiability is a property of the
*function* you annotate, not of the values flowing through it.

## Shapes are concrete, not generic {#static-shapes}

Faber does not have shape generics yet, so the shipped Gradus functions are
concrete overloads named for the shapes they accept — `linear_2x2`,
`linear_4x4`, `mse_2x8`. This follows the same concrete-overload precedent as
`norma:optimizer`.

This is the single biggest constraint on using Gradus today. A model whose
shapes are not already covered needs the matching overload added to the
library; you cannot instantiate one from the caller. The overloads that exist
were added to serve specific proofs — a 2×2 linear regression, a 4×4 MLP, and
a BERT-tiny fragment at B=2, D=8, H=1 — rather than to cover a shape space.

## Status {#status}

Gradus is pre-1.0 and its API may change. What is proven is narrower than
what the module list suggests: several modules are contract scaffolding with
their production surface still landing.

| Layer | State |
|-------|-------|
| Reverse-mode AD over AIR tensor ops | **Shipped** in Radix — 16 of 18 ops carry VJPs; broadcast and reduce are partial |
| Tensor, dtype, shape, parameter, serialize contracts | **Shipped** as versioned schemas |
| Pure operation families (`gradus:math`) | **Shipped** — elementwise, reduce, matmul, cast, concat/slice |
| Loss, optimizer, NN primitives | **Shipped** as static-shape overloads only |
| BERT-tiny attention and transformer slice | **Shipped** at fixed shapes (B=2, D=8, H=1); a general surface is not built |
| Training loop, metrics, checkpointing | **Planned** — no checkpointing, no safetensors, no model distribution |
| GPU training | Owned by Radix and the hosts, not by Gradus |

The gradient seam — forward loss, generated companion backward across an
`importa` boundary, and a per-element comparison against finite differences —
compiles and executes end to end, and the companion gradient matches finite
differences to roughly 1e-11. That is the load-bearing correctness result
behind everything above.

CPU training is correct and slow. Fast training is a device-execution
question, and that path is owned elsewhere: see
[device execution](/toolchain/cli.html#device-execution) for the `faber run
--backend` surface and the
[device kernel support summary](/toolchain/target-matrix.html#device-kernel-support)
for what the accepted proof actually covers.

## Who it is for {#audience}

Gradus is for people defining differentiable models in Faber who would rather
call library functions than hand-write compiler annotations, and for anyone
validating the Radix autograd pipeline through a clean surface. It is not for
production deployment, not for GPU-scale training, and not a place to port
PyTorch code shape-for-shape.

The stated forcing function is a minimal GPT trained on Shakespeare — chosen
because it runs on CPU for correctness while making the GPU gradient path's
absence expensive enough to close.

## Source {#source}

[github.com/faberlang/gradus](https://github.com/faberlang/gradus) — MIT,
like every public Faber library. See [Open source](/open-source.html).
