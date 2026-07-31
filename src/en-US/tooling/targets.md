+++
title = "Target compatibility"
section = "targets"
order = 2
sources = "radix/EBNF_MATRIX.md · target-capability-matrix.md · faber targets"
+++

Faber is one language with many compilation contracts. This page is the
**measured lowerability matrix**: for each corpus term, which targets can
lower it, and at what support level.

Policy verbs (support / erase / warn / reject / defer) and pipeline routing
live on [Codegen targets](/tooling/codegen-targets.html). This page is the
large scannable row list — HIR application-lane targets and MIR systems-lane
targets side by side in the tables below.

Live CLI summary: `faber targets`.

**Generated**: unknown by `scripta/generate-ebnf-matrix.py` — **do not edit**.
**Measurement**: `emit_hir_target_matrix` + `emit_mir_target_matrix` (in-process, no external toolchains).
**Join**: `corpus/index.toml` terms → exempla.

This is the **official generated** grammar×target support matrix. It reports
**lowerability** — can target X lower grammar production Y — across every term in
the exempla corpus. Runtime semantics (erase/warn/defer policy verbs), per-target
contracts, and pipeline routing live in
[Codegen targets](/tooling/codegen-targets.html), which links here for the rows.

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

**Application lane (HIR → emitted source languages)**

| target | capable | analyzable | % |
|---|---|---|---|
| rust | 277 | 279 | 99% |
| go | 258 | 279 | 92% |
| ts | 273 | 279 | 98% |
| faber | 279 | 279 | 100% |

**Systems lane (MIR → device/IR artifacts)**

| target | capable | analyzable | % |
|---|---|---|---|
| llvm-text | 255 | 265 | 96% |
| wasm-text | 210 | 265 | 79% |
| wasm | 210 | 265 | 79% |
| metal-text | 6 | 265 | 2% |
| wgsl-text | 6 | 265 | 2% |
| sexp-struct | 211 | 265 | 80% |
| sexp | 211 | 265 | 80% |
| scena | 224 | 265 | 85% |

## Keywords — application lane

### keyword

| term | rust | go | ts | faber |
|---|---|---|---|---|
| `abstractus` | ✓ | ✓ | ✓ | ✓ |
| `ab` | ✓ | ✓ | ✓ | ✓ |
| `ad` | ✓ | ✓ | ✓ | ✓ |
| `adfirma` | ✓ | ✓ | ✓ | ✓ |
| `ante` | ✓ | ✓ | ✓ | ✓ |
| `atomic` | ✕ | ✓ | ✓ | ✓ |
| `argumenta` | ✓ | ✓ | ✓ | ✓ |
| `bivalens` | ✓ | ✓ | ✓ | ✓ |
| `cape` | ✓ | ✓ | ✓ | ✓ |
| `casu` | ✓ | ✓ | ✓ | ✓ |
| `cede` | ✓ | ✓ | ✓ | ✓ |
| `ceteri` | ✓ | ✓ | ✓ | ✓ |
| `ceterum` | ✓ | ✓ | ✓ | ✓ |
| `clausura` | ✓ | ✓ | ✓ | ✓ |
| `cli` | ✓ | ✓ | ✓ | ✓ |
| `copia` | ✓ | ✓ | ✓ | ✓ |
| `cura` | ✓ | ✓ | ✓ | ✓ |
| `curata` | ✓ | ✓ | ✓ | ✓ |
| `cursor` | ✓ | ✓ | ✓ | ✓ |
| `custodi` | ✓ | ✓ | ✓ | ✓ |
| `de` | ✓ | ✓ | ✓ | ✓ |
| `descriptio` | ✓ | ✓ | ✓ | ✓ |
| `discerne` | ✓ | ✓ | ✓ | ✓ |
| `discretio` | ✓ | ✓ | ✓ | ✓ |
| `dum` | ✓ | ✓ | ✓ | ✓ |
| `ego` | ✓ | ✓ | ✓ | ✓ |
| `elige` | ✓ | ✓ | ✓ | ✓ |
| `errata` | ✓ | ✓ | ✓ | ✓ |
| `est` | ✓ | ✓ | ✓ | ✓ |
| `ex` | ✓ | ✓ | ✓ | ✓ |
| `exitus` | ✓ | ✓ | ✓ | ✓ |
| `fac` | ✓ | ✓ | ✓ | ✓ |
| `falsum` | ✓ | ✓ | ✓ | ✓ |
| `fient` | ✓ | ✓ | ✓ | ✓ |
| `fiet` | ✓ | ✓ | ✓ | ✓ |
| `figendum` | ✓ | ✓ | ✓ | ✓ |
| `finge` | ✓ | ✓ | ✓ | ✓ |
| `fiunt` | ✓ | ✓ | ✓ | ✓ |
| `fixum` | ✓ | ✓ | ✓ | ✓ |
| `fragilis` | ✓ | ✓ | ✓ | ✓ |
| `fractus` | ✓ | ✓ | ✓ | ✓ |
| `functio` | ✓ | ✓ | ✓ | ✓ |
| `futura` | ✓ | ✓ | ✓ | ✓ |
| `futurum` | ✓ | ✓ | ✓ | ✓ |
| `generis` | ✓ | ✓ | ✓ | ✓ |
| `genus` | ✓ | ✓ | ✓ | ✓ |
| `iace` | ✓ | ✓ | ✓ | ✓ |
| `iacit` | ✓ | ✓ | ✓ | ✓ |
| `ignotum` | ✓ | ✓ | ✓ | ✓ |
| `immutata` | ✓ | ✓ | ✓ | ✓ |
| `implet` | ✓ | ✓ | ✓ | ✓ |
| `importa` | ✓ | ✓ | ✓ | ✓ |
| `in` | ✓ | ✓ | ✓ | ✓ |
| `incipiet` | ✓ | ✓ | ✓ | ✓ |
| `incipit` | ✓ | ✓ | ✓ | ✓ |
| `inter` | ✓ | ✓ | ✓ | ✓ |
| `intra` | ✓ | ✓ | ✓ | ✓ |
| `instans` | ✓ | ✓ | ✓ | ✓ |
| `itera` | ✓ | ✓ | ✓ | ✓ |
| `lege` | ✓ | ✓ | ✓ | ✓ |
| `lineam` | ✓ | ✓ | ✓ | ✓ |
| `lista` | ✓ | ✓ | ✓ | ✓ |
| `matrix` | ✓ | ✕ | ✓ | ✓ |
| `mone` | ✓ | ✓ | ✓ | ✓ |
| `mori` | ✓ | ✓ | ✓ | ✓ |
| `nexum` | ✓ | ✓ | ✓ | ✓ |
| `nihil` | ✓ | ✓ | ✓ | ✓ |
| `numquam` | ✓ | ✓ | ✓ | ✓ |
| `numerus` | ✓ | ✓ | ✓ | ✓ |
| `non` | ✓ | ✓ | ✓ | ✓ |
| `omitte` | ✓ | ✓ | ✓ | ✓ |
| `omnia` | ✓ | ✓ | ✓ | ✓ |
| `operandus` | ✓ | ✓ | ✓ | ✓ |
| `optio` | ✓ | ✓ | ✓ | ✓ |
| `optiones` | ✓ | ✓ | ✓ | ✓ |
| `ordo` | ✓ | ✓ | ✓ | ✓ |
| `octeti` | ✓ | ✓ | ✓ | ✓ |
| `implendum` | ✓ | ✓ | ✓ | ✓ |
| `per` | ✓ | ✓ | ✓ | ✓ |
| `perge` | ✓ | ✓ | ✓ | ✓ |
| `postpara` | ✓ | ✓ | ✓ | ✓ |
| `postparabit` | ✓ | ✓ | ✓ | ✓ |
| `prae` | ✓ | ✓ | ✓ | ✓ |
| `praefixum` | — | — | — | — |
| `praepara` | ✓ | ✓ | ✓ | ✓ |
| `praeparabit` | ✓ | ✓ | ✓ | ✓ |
| `promissum` | ✓ | ✓ | ✓ | ✓ |
| `privata` | ✓ | ✓ | ✓ | ✓ |
| `proba` | ✓ | ✓ | ✓ | ✓ |
| `probandum` | ✓ | ✓ | ✓ | ✓ |
| `protecta` | — | — | — | — |
| `publica` | ✓ | ✓ | ✓ | ✓ |
| `redde` | ✓ | ✓ | ✓ | ✓ |
| `reddet` | ✓ | ✓ | ✓ | ✓ |
| `repete` | ✓ | ✓ | ✓ | ✓ |
| `rumpe` | ✓ | ✓ | ✓ | ✓ |
| `scribe` | ✓ | ✓ | ✓ | ✓ |
| `scriptum` | ✓ | ✓ | ✓ | ✓ |
| `secus` | ✓ | ✓ | ✓ | ✓ |
| `si` | ✓ | ✓ | ✓ | ✓ |
| `sic` | ✓ | ✓ | ✓ | ✓ |
| `sin` | ✓ | ✓ | ✓ | ✓ |
| `sit` | ✓ | ✓ | ✓ | ✓ |
| `solum_in` | ✓ | ✓ | ✓ | ✓ |
| `solum` | ✓ | ✓ | ✓ | ✓ |
| `sparge` | ✓ | ✓ | ✓ | ✓ |
| `sponte` | ✓ | ✓ | ✓ | ✓ |
| `sub` | ✓ | ✓ | ✓ | ✓ |
| `tacet` | ✓ | ✓ | ✓ | ✓ |
| `tacebit` | ✓ | ✓ | ✓ | ✓ |
| `tabula` | ✓ | ✓ | ✓ | ✓ |
| `tag` | ✓ | ✓ | ✓ | ✓ |
| `temporis` | ✓ | ✓ | ✓ | ✓ |
| `tensor` | ✓ | ✕ | ✓ | ✓ |
| `textus` | ✓ | ✓ | ✓ | ✓ |
| `typus` | ✓ | ✓ | ✓ | ✓ |
| `ubique` | ✓ | ✓ | ✓ | ✓ |
| `usque` | ✓ | ✓ | ✓ | ✓ |
| `ut` | ✓ | ✓ | ✓ | ✓ |
| `varia` | ✓ | ✓ | ✓ | ✓ |
| `variandum` | ✓ | ✓ | ✓ | ✓ |
| `vector` | ✓ | ✓ | ✓ | ✓ |
| `vacuum` | ✓ | ✓ | ✓ | ✓ |
| `verum` | ✓ | ✓ | ✓ | ✓ |
| `vide` | ✓ | ✓ | ✓ | ✓ |

## Operators — application lane

### operator-group

| term | rust | go | ts | faber |
|---|---|---|---|---|
| `⊜` | ✓ | ✓ | ✓ | ✓ |
| `∧` | ✓ | ✓ | ✓ | ✓ |
| `→` | ✓ | ✓ | ✓ | ✓ |
| `⇥` | ✓ | ✓ | ✓ | ✓ |
| `←` | ✓ | ✓ | ✓ | ✓ |
| `aut` | ✓ | ✓ | ✓ | ✓ |
| `![` | ✓ | ✓ | ✓ | ✓ |
| `!.` | ✓ | ✓ | ✓ | ✓ |
| `≠` | ✓ | ✓ | ✓ | ✓ |
| `!(` | ✓ | ✓ | ✓ | ✓ |
| `⊻` | ✓ | ✓ | ✓ | ✓ |
| `↦` | ✓ | ◐ | ✓ | ✓ |
| `⇒` | ✓ | ✓ | ✓ | ✓ |
| `‥` | ✓ | ✓ | ✓ | ✓ |
| `…` | ✓ | ✓ | ✓ | ✓ |
| `≡` | ✓ | ✓ | ✓ | ✓ |
| `=` | ✓ | ✓ | ✓ | ✓ |
| `et` | ✓ | ✓ | ✓ | ✓ |
| `≥` | ✓ | ✓ | ✓ | ✓ |
| `≤` | ✓ | ✓ | ✓ | ✓ |
| `⊖` | ✓ | ✓ | ✓ | ✓ |
| `modulus<u16>` | ✓ | ✕ | ✕ | ✓ |
| `modulus<u32>` | ✓ | ✕ | ✕ | ✓ |
| `modulus<u64>` | ✓ | ✕ | ✕ | ✓ |
| `modulus<u8>` | ✓ | ✕ | ✕ | ✓ |
| `non est` | ✓ | ✓ | ✓ | ✓ |
| `⊚` | ✓ | ✓ | ✓ | ✓ |
| `∨` | ✓ | ✓ | ✓ | ✓ |
| `∪` | ✓ | ✓ | ✓ | ✓ |
| `⊕` | ✓ | ✓ | ✓ | ✓ |
| `?[` | ✓ | ✓ | ✓ | ✓ |
| `?.` | ✓ | ✓ | ✓ | ✓ |
| `?(` | ✓ | ✓ | ✓ | ✓ |
| `§` | ✓ | ✓ | ✓ | ✓ |
| `⇐` | ✓ | ✓ | ✓ | ✓ |
| `⊘` | ✓ | ✓ | ✓ | ✓ |
| `⊛` | ✓ | ✓ | ✓ | ✓ |
| `¬` | ✓ | ✓ | ✓ | ✓ |
| `vel` | ✓ | ✓ | ✓ | ✓ |
| `∷` | ✓ | ✓ | ✓ | ✓ |
| `∴` | ✓ | ✓ | ✓ | ✓ |
| `ergo` | ✓ | ✓ | ✓ | ✓ |

## Keywords — systems lane

### keyword

| term | llvm-text | wasm-text | wasm | metal-text | wgsl-text | sexp-struct | sexp | scena |
|---|---|---|---|---|---|---|---|---|
| `abstractus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ab` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ad` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `adfirma` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ante` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `atomic` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `argumenta` | — | — | — | — | — | — | — | — |
| `bivalens` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `cape` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `casu` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `cede` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `ceteri` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ceterum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `clausura` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `cli` | — | — | — | — | — | — | — | — |
| `copia` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `cura` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `curata` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `cursor` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `custodi` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `de` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `descriptio` | — | — | — | — | — | — | — | — |
| `discerne` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `discretio` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `dum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ego` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `elige` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `errata` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `est` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `ex` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `exitus` | — | — | — | — | — | — | — | — |
| `fac` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `falsum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `fient` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `fiet` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `figendum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `finge` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `fiunt` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `fixum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `fragilis` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `fractus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `functio` | ✓ | ◐ | ◐ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `futura` | ◐ | ◐ | ◐ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `futurum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `generis` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `genus` | ✓ | ✓ | ✓ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `iace` | ✓ | ◐ | ◐ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `iacit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ignotum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `immutata` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `implet` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `importa` | ✓ | ✓ | ✓ | ✕ | ✕ | ◐ | ◐ | ◐ |
| `in` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `incipiet` | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `incipit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `inter` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `intra` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `instans` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `itera` | ✓ | ✓ | ✓ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `lege` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `lineam` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `lista` | ✓ | ✓ | ✓ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `matrix` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `mone` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `mori` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `nexum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `nihil` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `numquam` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `numerus` | ✓ | ◐ | ◐ | ✕ | ✕ | ◐ | ◐ | ◐ |
| `non` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `omitte` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `omnia` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `operandus` | — | — | — | — | — | — | — | — |
| `optio` | — | — | — | — | — | — | — | — |
| `optiones` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `ordo` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `octeti` | ✓ | ◐ | ◐ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `implendum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `per` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `perge` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `postpara` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `postparabit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `prae` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `praefixum` | — | — | — | — | — | — | — | — |
| `praepara` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `praeparabit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `promissum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `privata` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `proba` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `probandum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `protecta` | — | — | — | — | — | — | — | — |
| `publica` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `redde` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ◐ |
| `reddet` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `repete` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `rumpe` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `scribe` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `scriptum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `secus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `si` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `sic` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `sin` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `sit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `solum_in` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `solum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `sparge` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `sponte` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `sub` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `tacet` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `tacebit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `tabula` | ✓ | ◐ | ◐ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `tag` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `temporis` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `tensor` | ✓ | ✕ | ✕ | ✕ | ✕ | ◐ | ◐ | ◐ |
| `textus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `typus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ubique` | — | — | — | — | — | — | — | — |
| `usque` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ut` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `varia` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `variandum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `vector` | ✓ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ✕ |
| `vacuum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `verum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `vide` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |

## Operators — systems lane

### operator-group

| term | llvm-text | wasm-text | wasm | metal-text | wgsl-text | sexp-struct | sexp | scena |
|---|---|---|---|---|---|---|---|---|
| `⊜` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `∧` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `→` | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⇥` | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `←` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `aut` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `![` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `!.` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `≠` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `!(` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⊻` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `↦` | ✓ | ◐ | ◐ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `⇒` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `‥` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `…` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `≡` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `=` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `et` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `≥` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `≤` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⊖` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `modulus<u16>` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `modulus<u32>` | ◐ | ✕ | ✕ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `modulus<u64>` | ✕ | ✕ | ✕ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `modulus<u8>` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `non est` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⊚` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `∨` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `∪` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⊕` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `?[` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `?.` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `?(` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `§` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⇐` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⊘` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⊛` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `¬` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `vel` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `∷` | ✓ | ✕ | ✕ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `∴` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ergo` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |

## Other terms (`existing-home` / unspecified)

### existing-home

| term | rust | go | ts | faber |
|---|---|---|---|---|
| `alias` | ✓ | ✓ | ✓ | ✓ |
| `arena` | ✓ | ✓ | ✓ | ✓ |
| `@` | ✓ | ✓ | ✓ | ✓ |
| `f16` | ✕ | ✓ | ✓ | ✓ |
| `imperia` | ✓ | ✓ | ✓ | ✓ |
| `imperium` | ✓ | ✓ | ✓ | ✓ |
| `manifest` | ✓ | ✓ | ✓ | ✓ |
| `metior` | ✓ | ✓ | ✓ | ✓ |
| `nondum` | ✓ | ✓ | ✓ | ✓ |
| `objectum` | ✓ | ✓ | ✓ | ✓ |
| `prima` | ✓ | ✓ | ✓ | ✓ |
| `requirit` | ✓ | ✓ | ✓ | ✓ |
| `string` | ✓ | ✓ | ✓ | ✓ |
| `block-string` | ✓ | ✓ | ✓ | ✓ |
| `summa` | ✓ | ✓ | ✓ | ✓ |
| `targets` | ✓ | ✓ | ✓ | ✓ |
| `ultima` | ✓ | ✓ | ✓ | ✓ |
| `versio` | ✓ | ✓ | ✓ | ✓ |
