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
and resolved from a library checkout (`--library-home <DIR>` or `[paths] library_home`
in `faber.toml`), the same way as [Triga](/libraries/triga.html).

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
| `gradus:nn` | Differentiable primitives: linear, activation, norm, embedding, dropout |
| `gradus:attention` | Facade; the leaves are `gradus:attention/rope` and `gradus:attention/gqa` |
| `gradus:mlp` | Two-layer MLP forward and training-path companion |
| `gradus:transformer` | Transformer blocks, positional encoding, heads |
| `gradus:train` | Training loops, checkpointing |
| `gradus:metrics` | Defined metrics over tensor values |
| `gradus:data` | Batching, shuffling, tokenization helpers |
| `gradus:storage` | Opaque encoded numeric storage |
| `gradus:tokenizer` | Facade; the leaves are `tokenizer/identity`, `tokenizer/unicode`, `tokenizer/bpe` |
| `gradus:sampling` | Token sampling policies |
| `gradus:decode`, `gradus:generation`, `gradus:cache` | Decode loop, generation, and KV-cache contracts (`generation` and `cache` are facades over leaves) |
| `gradus:model/*` | Model admission and architecture leaves: GGUF, Safetensors, capsules, dense and MoE graphs |
| `gradus:gradus` | Package map facade only — holds no genera |

```faber mode=package
importa ex "gradus:tensor" tensor
importa ex "gradus:math" math
importa ex "gradus:gradient" gradient
importa ex "gradus:loss" loss
importa ex "gradus:optimize" optimize
```

The `gradus:tensor` / `gradus:gradient` split is the one to internalise:
tensor values are plain data, and differentiability is a property of the
*function* you annotate, not of the values flowing through it.

## Shapes {#static-shapes}

Tensor functions are generic over their sizes. `loss.mse` takes
`tensor<f32, [M, N]>` operands with `size M, size N` parameters, and
`nn.linear` is generic over `M`, `K` and `N` the same way, so a model whose
shapes are not already covered does not need a matching overload added to the
library.

Alongside the typed-tensor forms, several operations have a `_carrier`
variant over `tensor.NumericBlock`, the decoded F32 host-list carrier that the
CPU and reference tiers execute on. Those variants report failure through a
typed error (`LossError`, `NnError`) instead of a shape type.

## Status {#status}

Gradus is pre-1.0 and its API may change. `faber check-library gradus` with
the Faber 1.14.0 release compiler does not pass yet: the sources still use the
retired binding words (`var`, run-time `const`, `fixum` binders), which the
compiler now rejects. What is proven is narrower than
what the module list suggests: most of it is structural, with source contracts
that check and are pinned by proba tests, and a narrow set of executed proofs.

| Layer | State |
|-------|-------|
| Reverse-mode AD over AIR tensor ops | **Shipped** in Radix; the admitted VJP family and its gaps live in the Radix autograd crate, not in Gradus |
| Tensor, dtype, shape, parameter, serialize contracts | **Shipped** as versioned schemas |
| Pure operation families (`gradus:math`) | **Shipped** — elementwise, reduce, matmul, cast, concat/slice |
| Loss, optimizer, NN primitives | **Shipped** (structural), generic over tensor sizes |
| Attention and transformer blocks | **Shipped** (structural) |
| Training loop, metrics, checkpointing | **Shipped** (structural): SGD state and step, `Checkpoint`, `accuracy` / `Metric` |
| Model admission | **Shipped**: GGUF and Safetensors admission into typed capsules |
| GPU training | **Not claimed**; device execution and emission are Radix scope |

The gradient seam — a forward loss, its generated companion backward, and a
per-element comparison against central finite differences — runs end to end in
the repository's self-contained `exempla/gradient-seam-nolib` package: the
companion gradient comes out equal to the analytic values, and the
single-precision finite differences agree with it to about 1e-2. That is the
load-bearing correctness result behind everything above. The same seam written
across a `gradus:*` import boundary lives in `exempla/gradient-seam`.

CPU training is correct and slow. Fast training is a device-execution
question, and that path is owned elsewhere: see
[device execution](/toolchain/cli.html#device-execution) for the `faber run
--device` surface and the
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

[github.com/faberlang/gradus](https://github.com/faberlang/gradus) — MIT.
See [Open source](/open-source.html).
