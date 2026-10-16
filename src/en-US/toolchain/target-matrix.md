+++
title = "Target compatibility"
section = "targets"
order = 2
sources = "radix/grammar/EBNF_MATRIX.md · target-capability-matrix.md · faber targets"
+++

Faber is one language with many compilation contracts. This page is the
**measured lowerability matrix**: for each corpus term, which targets can
lower it, and at what support level.

Policy verbs (support / erase / warn / reject / defer) and pipeline routing
live on [Compiling and targets](/toolchain/compiling.html). This page is the
large scannable row list — HIR application-lane targets and MIR systems-lane
targets side by side in the tables below.

Live CLI summary: `faber targets`.

**About the term column.** The term column below is the English reader
spelling — the same words you write in Faber source on this site. Each
term's identity in the compiler's corpus directory keeps its
Latin key: that key is what the measurement rows are indexed and joined
under, so a row is the same row whichever language you read the site in.

**Rendered**: unknown by `faber/scripta/render-matrices.py` from radix measurement JSON — **do not hand-edit**.
**Measurement**: `emit_hir_target_matrix` + `emit_mir_target_matrix` (in-process, no external toolchains).
**Join**: `corpus/index.toml` terms → exempla.

This is the **official generated** grammar×target support matrix. It reports
**lowerability** — can target X lower grammar production Y — across every term in
the exempla corpus. Runtime semantics (erase/warn/defer policy verbs), per-target
contracts, and pipeline routing live in
[Compiling and targets](/toolchain/compiling.html), which links here for the rows.

## Legend

| Glyph | Meaning |
|---|---|
| ✓ | fully supported — all analyzable exempla for the term lower |
| ◐ | partial — some exempla lower, some have a measured gap |
| ○ | planned — not yet lowering; curated overlay (`scripta/ebnf-matrix-overrides.toml`) |
| ✕ | not supported — no exempla lower; default-truth, measured gap is real |
| — | not measured — no analyzable exempla for this term on this lane |

> A ✓ means the corpus exempla exercising this term lower to the target. It does
> **not** guarantee identical runtime semantics. Some targets *erase* or *warn* on
> certain constructs (e.g. Go erases borrow modes `de`/`in`/`ex`) — those still
> render ✓ here because they lower. See the policy doc for that nuance.

## Corpus-wide summary (all registered terms)

### How to read these percentages

This matrix answers one narrow question:

> For each **general-language corpus term**, does the named **emit target**
> lower the term's exempla?

It is **not** a product completion score for Metal, CUDA, or GPU training.

- **Application HIR** percentages (Rust / Go / TS / Faber) are fair "how much of
  the language emits" scores for host-language projections.
- **General MIR** percentages (llvm-text, wasm, sexp, …) score ordinary systems
  IR emission over the same full corpus.
- **Device-kernel emitters are not scored here.** `metal-text` and `wgsl-text`
  lower a device-safe kernel surface — `@ nucleum` compute kernels and related
  GPU views — and deliberately nothing else: no packages, async, CLI, full
  control flow, or host libraries. Measuring them against all ~280
  general-language terms answers a question that does not apply to them, so
  this matrix does not ask it. Their real support is the
  [device kernel support](#device-kernel-support) summary below, and real
  device execution runs through `faber run --device metal`.
- **There is no `cuda` column.** CUDA is not a text emit target. CUDA device
  programs are produced on the **NVVM → PTX** path (staged with **llvm-text** /
  MIR device emission) and run with `faber run --device cuda`. Product GPU
  backends are **Metal** and **CUDA**; matrix columns track **emit surfaces**,
  not every host session.

For product policy (build/run/package, erase/reject, device backends), use
[Compiling and targets](/toolchain/compiling.html) and `faber targets` — not
these corpus rows as a quality score.

**Application lane (HIR → emitted source languages)**

| target | capable | analyzable | % |
|---|---|---|---|
| rust | 434 | 439 | 99% |
| go | 402 | 439 | 92% |
| ts | 439 | 439 | 100% |
| faber | 439 | 439 | 100% |

**Systems lane (MIR → device/IR artifacts)**

| target | capable | analyzable | % |
|---|---|---|---|
| llvm-text | 396 | 443 | 89% |
| wasm-text | 339 | 443 | 77% |
| wasm | 339 | 443 | 77% |
| sexp-struct | 409 | 443 | 92% |
| sexp | 407 | 443 | 92% |
| runner | 390 | 443 | 88% |

## Device kernel support {#device-kernel-support}

This section is the **GPU product view**, kept apart from the corpus % tables
below, which deliberately do not score device emitters. It states how the device
route is defined and what each device target emits. It carries no measurement;
`faber targets` reports what your binary supports.

### How a device program runs

A kernel is a function marked `@ kernel`. A package carries a device program
when it declares one; a `[device]` manifest table is configuration, not a
requirement. `faber run --device <device>` selects where it runs.

| Device | What it is |
|---|---|
| `reference` | Plain sequential code on the MIR runner; the oracle device results are checked against |
| `cpu` | Processor cores as a device; until the worker device lands, the same route as `reference` |
| `metal` | Apple Metal |
| `cuda` | NVIDIA CUDA, through the NVIDIA driver with PTX that `clang` (NVPTX target) builds at run time. Whole-tensor kernels; lane-form kernels are not lowered for CUDA yet |
| `auto` | Resolve against the machine's probes; fails closed when none, or more than one, is admitted |

An explicit device request never silently falls back. It fails closed before
launch: `E_DEVICE_UNAVAILABLE` when the machine has no runtime for the device,
`E_DEVICE_NONE_ADMITTED` when no device is usable, and `E_NO_DEVICE_PROGRAM`
for a package with no device program. Precedence is the command
line, then the manifest `[device] device`, then `auto`.

### Device targets

| Target | What it is |
|---|---|
| `metal-text` | Metal Shading Language source for the device-safe kernel subset. Device execution is `faber run --device metal`; `-t metal-text` itself is emit-only |
| `llvm-text` | LLVM text. Also the staging chain for CUDA device execution, `faber run --device cuda`; `-t llvm-text` itself is emit-only. There is no separate `cuda` target |
| `wgsl-text` | WGSL compute-shader source for the device-safe subset, validated by an external `naga`. It is not a GPU launch or a package runtime |

Device execution is under active development. The corpus % tables on this page
score whole-language terms against kernel-only emitters, so a low percentage on
a device row is not a statement about the device route.

### Where to read more

| Page | What it covers |
|---|---|
| [Device execution CLI](/toolchain/cli.html#device-execution) | The command contract |
| [Compiling · device execution](/toolchain/compiling.html#device-execution) | Emit versus run |

## Keywords — application lane

### keyword

| term | rust | go | ts | faber |
|---|---|---|---|---|
| <a id="ab"></a>`ab` | ✓ | ✓ | ✓ | ✓ |
| <a id="ad"></a>`ad` | ✓ | ✕ | ✓ | ✓ |
| <a id="adfirma"></a>`adfirma` | ✓ | ✓ | ✓ | ✓ |
| <a id="ante"></a>`ante` | ✓ | ✓ | ✓ | ✓ |
| <a id="argumenta"></a>`argumenta` | ✓ | ✓ | ✓ | ✓ |
| <a id="bivalens"></a>`bivalens` | ✓ | ✓ | ✓ | ✓ |
| <a id="cape"></a>`cape` | ✓ | ✓ | ✓ | ✓ |
| <a id="casu"></a>`casu` | ✓ | ✓ | ✓ | ✓ |
| <a id="cede"></a>`cede` | ✓ | ✓ | ✓ | ✓ |
| <a id="ceteri"></a>`ceteri` | ✓ | ✓ | ✓ | ✓ |
| <a id="ceterum"></a>`ceterum` | ✓ | ✓ | ✓ | ✓ |
| <a id="clausura"></a>`clausura` | ✓ | ✓ | ✓ | ✓ |
| <a id="copia"></a>`copia` | ✓ | ✓ | ✓ | ✓ |
| <a id="cursor"></a>`cursor` | ✓ | ✓ | ✓ | ✓ |
| <a id="custodi"></a>`custodi` | ✓ | ✓ | ✓ | ✓ |
| <a id="de"></a>`de` | ✓ | ✓ | ✓ | ✓ |
| <a id="descriptio"></a>`descriptio` | ✓ | ✓ | ✓ | ✓ |
| <a id="discerne"></a>`discerne` | ✓ | ✓ | ✓ | ✓ |
| <a id="discretio"></a>`discretio` | ✓ | ✓ | ✓ | ✓ |
| <a id="dum"></a>`dum` | ✓ | ✓ | ✓ | ✓ |
| <a id="ego"></a>`ego` | ✓ | ✓ | ✓ | ✓ |
| <a id="elige"></a>`elige` | ✓ | ✓ | ✓ | ✓ |
| <a id="errata"></a>`errata` | ✓ | ✓ | ✓ | ✓ |
| <a id="est"></a>`est` | ✓ | ✓ | ✓ | ✓ |
| <a id="ex"></a>`ex` | ✓ | ✓ | ✓ | ✓ |
| <a id="exitus"></a>`exitus` | ✓ | ✓ | ✓ | ✓ |
| <a id="fac"></a>`fac` | ✓ | ✓ | ✓ | ✓ |
| <a id="falsum"></a>`falsum` | ✓ | ✓ | ✓ | ✓ |
| <a id="fient"></a>`fient` | ✓ | ✓ | ✓ | ✓ |
| <a id="fiet"></a>`fiet` | ✓ | ✓ | ✓ | ✓ |
| <a id="figendum"></a>`figendum` | ✓ | ✓ | ✓ | ✓ |
| <a id="finge"></a>`finge` | ✓ | ✓ | ✓ | ✓ |
| <a id="fiunt"></a>`fiunt` | ✓ | ✓ | ✓ | ✓ |
| <a id="fixum"></a>`fixum` | ✓ | ✓ | ✓ | ✓ |
| <a id="fractus"></a>`fractus` | ✓ | ✓ | ✓ | ✓ |
| <a id="fragilis"></a>`fragilis` | ✓ | ✓ | ✓ | ✓ |
| <a id="functio"></a>`functio` | ✓ | ✓ | ✓ | ✓ |
| <a id="futurum"></a>`futurum` | ✓ | ✓ | ✓ | ✓ |
| <a id="genus"></a>`genus` | ✓ | ✓ | ✓ | ✓ |
| <a id="iace"></a>`iace` | ✓ | ✓ | ✓ | ✓ |
| <a id="ignotum"></a>`ignotum` | ✓ | ✓ | ✓ | ✓ |
| <a id="immutata"></a>`immutata` | ✓ | ✓ | ✓ | ✓ |
| <a id="implendum"></a>`implendum` | ✓ | ✓ | ✓ | ✓ |
| <a id="implet"></a>`implet` | ✓ | ✓ | ✓ | ✓ |
| <a id="importa"></a>`importa` | ✓ | ✓ | ✓ | ✓ |
| <a id="in"></a>`in` | ✓ | ✓ | ✓ | ✓ |
| <a id="incipiet"></a>`incipiet` | ✓ | ✓ | ✓ | ✓ |
| <a id="incipit"></a>`incipit` | ✓ | ✓ | ✓ | ✓ |
| <a id="insere"></a>`insere` | ✓ | ✓ | ✓ | ✓ |
| <a id="instans"></a>`instans` | ✓ | ✓ | ✓ | ✓ |
| <a id="itera"></a>`itera` | ✓ | ◐ | ✓ | ✓ |
| <a id="iuncta"></a>`iuncta` | ✓ | ✓ | ✓ | ✓ |
| <a id="lege"></a>`lege` | ✓ | ✓ | ✓ | ✓ |
| <a id="lineam"></a>`lineam` | ✓ | ✓ | ✓ | ✓ |
| <a id="lista"></a>`lista` | ✓ | ✓ | ✓ | ✓ |
| <a id="mone"></a>`mone` | ✓ | ✓ | ✓ | ✓ |
| <a id="mori"></a>`mori` | ✓ | ✓ | ✓ | ✓ |
| <a id="nihil"></a>`nihil` | ✓ | ✓ | ✓ | ✓ |
| <a id="non"></a>`non` | ✓ | ✓ | ✓ | ✓ |
| <a id="numerus"></a>`numerus` | ✓ | ◐ | ✓ | ✓ |
| <a id="numquam"></a>`numquam` | ✓ | ✓ | ✓ | ✓ |
| <a id="objectum"></a>`objectum` | ✓ | ✓ | ✓ | ✓ |
| <a id="octeti"></a>`octeti` | ✓ | ✓ | ✓ | ✓ |
| <a id="omitte"></a>`omitte` | ✓ | ✓ | ✓ | ✓ |
| <a id="omnia"></a>`omnia` | ✓ | ✓ | ✓ | ✓ |
| <a id="operandus"></a>`operandus` | ✓ | ✓ | ✓ | ✓ |
| <a id="optio"></a>`optio` | ✓ | ✓ | ✓ | ✓ |
| <a id="optiones"></a>`optiones` | ✓ | ✓ | ✓ | ✓ |
| <a id="ordo"></a>`ordo` | ✓ | ✓ | ✓ | ✓ |
| <a id="per"></a>`per` | ✓ | ✓ | ✓ | ✓ |
| <a id="perge"></a>`perge` | ✓ | ✓ | ✓ | ✓ |
| <a id="postpara"></a>`postpara` | ✓ | ✓ | ✓ | ✓ |
| <a id="postparabit"></a>`postparabit` | ✓ | ✓ | ✓ | ✓ |
| <a id="praefixum"></a>`praefixum` | ✓ | ✓ | ✓ | ✓ |
| <a id="praepara"></a>`praepara` | ✓ | ✓ | ✓ | ✓ |
| <a id="praeparabit"></a>`praeparabit` | ✓ | ✓ | ✓ | ✓ |
| <a id="privata"></a>`privata` | ✓ | ✓ | ✓ | ✓ |
| <a id="proba"></a>`proba` | ✓ | ✓ | ✓ | ✓ |
| <a id="probandum"></a>`probandum` | ✓ | ✓ | ✓ | ✓ |
| <a id="promissum"></a>`promissum` | ✓ | ✓ | ✓ | ✓ |
| <a id="protecta"></a>`protecta` | — | — | — | — |
| <a id="publica"></a>`publica` | ✓ | ✓ | ✓ | ✓ |
| <a id="ratio"></a>`ratio` | ✓ | ✓ | ✓ | ✓ |
| <a id="redde"></a>`redde` | ✓ | ✓ | ✓ | ✓ |
| <a id="reddet"></a>`reddet` | ✓ | ✓ | ✓ | ✓ |
| <a id="reice"></a>`reice` | ✓ | ✓ | ✓ | ✓ |
| <a id="repete"></a>`repete` | ✓ | ✓ | ✓ | ✓ |
| <a id="requirit"></a>`requirit` | ✓ | ✓ | ✓ | ✓ |
| <a id="rumpe"></a>`rumpe` | ✓ | ✓ | ✓ | ✓ |
| <a id="scribe"></a>`scribe` | ✓ | ✓ | ✓ | ✓ |
| <a id="scriptum"></a>`scriptum` | ✓ | ✓ | ✓ | ✓ |
| <a id="secus"></a>`secus` | ✓ | ✓ | ✓ | ✓ |
| <a id="selective-import"></a>`selective_import` | ✓ | ✓ | ✓ | ✓ |
| <a id="si"></a>`si` | ✓ | ✓ | ✓ | ✓ |
| <a id="sin"></a>`sin` | ✓ | ✓ | ✓ | ✓ |
| <a id="sit"></a>`sit` | ✓ | ✓ | ✓ | ✓ |
| <a id="solum"></a>`solum` | ✓ | ✓ | ✓ | ✓ |
| <a id="solum-in"></a>`solum_in` | ✓ | ✓ | ✓ | ✓ |
| <a id="sparge"></a>`sparge` | ✓ | ✓ | ✓ | ✓ |
| <a id="sponte"></a>`sponte` | ✓ | ✓ | ✓ | ✓ |
| <a id="tabula"></a>`tabula` | ✓ | ✓ | ✓ | ✓ |
| <a id="tacebit"></a>`tacebit` | ✓ | ✓ | ✓ | ✓ |
| <a id="tacet"></a>`tacet` | ✓ | ✓ | ✓ | ✓ |
| <a id="tag"></a>`tag` | ✓ | ✓ | ✓ | ✓ |
| <a id="temporis"></a>`temporis` | ✓ | ✓ | ✓ | ✓ |
| <a id="textus"></a>`textus` | ✓ | ✓ | ✓ | ✓ |
| <a id="typus"></a>`typus` | ✓ | ✓ | ✓ | ✓ |
| <a id="ubique"></a>`ubique` | ✓ | ✓ | ✓ | ✓ |
| <a id="usque"></a>`usque` | ✓ | ✓ | ✓ | ✓ |
| <a id="ut"></a>`ut` | ✓ | ✓ | ✓ | ✓ |
| <a id="vacuum"></a>`vacuum` | ✓ | ✓ | ✓ | ✓ |
| <a id="varia"></a>`varia` | ✓ | ✓ | ✓ | ✓ |
| <a id="variandum"></a>`variandum` | ✓ | ✓ | ✓ | ✓ |
| <a id="verum"></a>`verum` | ✓ | ✓ | ✓ | ✓ |
| <a id="vide"></a>`vide` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∪` | ✓ | ✓ | ✓ | ✓ |

## Operators — application lane

### operator-group

| term | rust | go | ts | faber |
|---|---|---|---|---|
| <a id=""></a>`!(` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`!.` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`![` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`=` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?(` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?.` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?[` | ✓ | ✓ | ✓ | ✓ |
| <a id="aut"></a>`aut` | ✓ | ✓ | ✓ | ✓ |
| <a id="ergo"></a>`ergo` | ✓ | ✓ | ✓ | ✓ |
| <a id="et"></a>`et` | ✓ | ✓ | ✓ | ✓ |
| <a id="modulus-u16"></a>`modulus<u16>` | ✓ | ✕ | ✓ | ✓ |
| <a id="modulus-u32"></a>`modulus<u32>` | ✓ | ✕ | ✓ | ✓ |
| <a id="modulus-u64"></a>`modulus<u64>` | ✓ | ✕ | ✓ | ✓ |
| <a id="modulus-u8"></a>`modulus<u8>` | ✓ | ✕ | ✓ | ✓ |
| <a id="non-est"></a>`non est` | ✓ | ✓ | ✓ | ✓ |
| <a id="vel"></a>`vel` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`§` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`¬` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`·` | ◐ | ◐ | ✓ | ✓ |
| <a id=""></a>`×` | ✓ | ○ | ✓ | ✓ |
| <a id=""></a>`‥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`…` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`←` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`→` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↤` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↦` | ◐ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇐` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇒` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∈` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∧` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∨` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∴` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∷` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≡` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≢` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≤` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊗` | ✓ | ○ | ✓ | ✓ |
| <a id=""></a>`⊘` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊙` | ✓ | ◐ | ✓ | ✓ |
| <a id=""></a>`⊚` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊛` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊜` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊻` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`✓` | ✓ | ✓ | ✓ | ✓ |

## Keywords — systems lane

### keyword

| term | llvm-text | wasm-text | wasm | sexp-struct | sexp | runner |
| --- | --- | --- | --- | --- | --- | --- |
| <a id="ab"></a>`ab` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ad"></a>`ad` | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| <a id="adfirma"></a>`adfirma` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ante"></a>`ante` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="argumenta"></a>`argumenta` | ✓ | ◐ | ◐ | ◐ | ◐ | ✓ |
| <a id="bivalens"></a>`bivalens` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="cape"></a>`cape` | ✓ | ✓ | ✓ | ✓ | ✓ | ◐ |
| <a id="casu"></a>`casu` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="cede"></a>`cede` | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ceteri"></a>`ceteri` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ceterum"></a>`ceterum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="clausura"></a>`clausura` | ◐ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="copia"></a>`copia` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="cursor"></a>`cursor` | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="custodi"></a>`custodi` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="de"></a>`de` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="descriptio"></a>`descriptio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="discerne"></a>`discerne` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="discretio"></a>`discretio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="dum"></a>`dum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ego"></a>`ego` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="elige"></a>`elige` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="errata"></a>`errata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="est"></a>`est` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id="ex"></a>`ex` | ✓ | ◐ | ◐ | ◐ | ◐ | ✓ |
| <a id="exitus"></a>`exitus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fac"></a>`fac` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="falsum"></a>`falsum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fient"></a>`fient` | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fiet"></a>`fiet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="figendum"></a>`figendum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="finge"></a>`finge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fiunt"></a>`fiunt` | ✕ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fixum"></a>`fixum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fractus"></a>`fractus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fragilis"></a>`fragilis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="functio"></a>`functio` | ✓ | ◐ | ◐ | ✓ | ✓ | ◐ |
| <a id="futurum"></a>`futurum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="genus"></a>`genus` | ◐ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="iace"></a>`iace` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ignotum"></a>`ignotum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="immutata"></a>`immutata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="implendum"></a>`implendum` | ◐ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="implet"></a>`implet` | ◐ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="importa"></a>`importa` | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ |
| <a id="in"></a>`in` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="incipiet"></a>`incipiet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="incipit"></a>`incipit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="insere"></a>`insere` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="instans"></a>`instans` | ✓ | ✕ | ✕ | ◐ | ◐ | ◐ |
| <a id="itera"></a>`itera` | ◐ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="iuncta"></a>`iuncta` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id="lege"></a>`lege` | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| <a id="lineam"></a>`lineam` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="lista"></a>`lista` | ◐ | ◐ | ◐ | ◐ | ◐ | ✓ |
| <a id="mone"></a>`mone` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="mori"></a>`mori` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="nihil"></a>`nihil` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="non"></a>`non` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="numerus"></a>`numerus` | ✓ | ◐ | ◐ | ✓ | ✓ | ◐ |
| <a id="numquam"></a>`numquam` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="objectum"></a>`objectum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="octeti"></a>`octeti` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="omitte"></a>`omitte` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="omnia"></a>`omnia` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="operandus"></a>`operandus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="optio"></a>`optio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="optiones"></a>`optiones` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="ordo"></a>`ordo` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="per"></a>`per` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="perge"></a>`perge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="postpara"></a>`postpara` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="postparabit"></a>`postparabit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="praefixum"></a>`praefixum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="praepara"></a>`praepara` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="praeparabit"></a>`praeparabit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="privata"></a>`privata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="proba"></a>`proba` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="probandum"></a>`probandum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="promissum"></a>`promissum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="protecta"></a>`protecta` | — | — | — | — | — | — |
| <a id="publica"></a>`publica` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ratio"></a>`ratio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="redde"></a>`redde` | ✓ | ✓ | ✓ | ✓ | ✓ | ◐ |
| <a id="reddet"></a>`reddet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="reice"></a>`reice` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="repete"></a>`repete` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="requirit"></a>`requirit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="rumpe"></a>`rumpe` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="scribe"></a>`scribe` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="scriptum"></a>`scriptum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="secus"></a>`secus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="selective-import"></a>`selective_import` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="si"></a>`si` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sin"></a>`sin` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sit"></a>`sit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="solum"></a>`solum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="solum-in"></a>`solum_in` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="sparge"></a>`sparge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sponte"></a>`sponte` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="tabula"></a>`tabula` | ◐ | ◐ | ◐ | ✓ | ✓ | ◐ |
| <a id="tacebit"></a>`tacebit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="tacet"></a>`tacet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="tag"></a>`tag` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="temporis"></a>`temporis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="textus"></a>`textus` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="typus"></a>`typus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ubique"></a>`ubique` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="usque"></a>`usque` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ut"></a>`ut` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="vacuum"></a>`vacuum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="varia"></a>`varia` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="variandum"></a>`variandum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="verum"></a>`verum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="vide"></a>`vide` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∪` | ◐ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Operators — systems lane

### operator-group

| term | llvm-text | wasm-text | wasm | sexp-struct | sexp | runner |
| --- | --- | --- | --- | --- | --- | --- |
| <a id=""></a>`!(` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`!.` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`![` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`=` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?(` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?.` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?[` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="aut"></a>`aut` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ergo"></a>`ergo` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="et"></a>`et` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="modulus-u16"></a>`modulus<u16>` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="modulus-u32"></a>`modulus<u32>` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="modulus-u64"></a>`modulus<u64>` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="modulus-u8"></a>`modulus<u8>` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="non-est"></a>`non est` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="vel"></a>`vel` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`§` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`¬` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`·` | ◐ | ◐ | ◐ | ✓ | ✓ | ◐ |
| <a id=""></a>`×` | ✓ | ○ | ○ | ✓ | ✓ | ✓ |
| <a id=""></a>`‥` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`…` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`←` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`→` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↤` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↦` | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ |
| <a id=""></a>`⇐` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇒` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇥` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∈` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∧` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∨` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∴` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∷` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≡` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≢` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≤` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≥` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊗` | ○ | ○ | ○ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊘` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊙` | ◐ | ◐ | ◐ | ✓ | ✓ | ◐ |
| <a id=""></a>`⊚` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊛` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊜` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊥` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊻` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`✓` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Other terms (`existing-home` / unspecified)

### existing-home

| term | rust | go | ts | faber |
|---|---|---|---|---|
| <a id="block-string"></a>`block-string` | ✓ | ✓ | ✓ | ✓ |
| <a id="guillemet"></a>`guillemet` | ✓ | ✓ | ✓ | ✓ |
| <a id="metior"></a>`metior` | ✓ | ✓ | ✓ | ✓ |
| <a id="named-holes"></a>`named-holes` | ✓ | ✓ | ✓ | ✓ |
| <a id="prima"></a>`prima` | ✓ | ✓ | ✓ | ✓ |
| <a id="string"></a>`string` | ✓ | ✓ | ✓ | ✓ |
| <a id="ultima"></a>`ultima` | ✓ | ✓ | ✓ | ✓ |
