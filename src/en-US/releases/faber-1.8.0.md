+++
title = "Faber 1.8.0"
section = "releases"
order = 8
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.8.0 |
| **Tag** | [`faber/v1.8.0`](https://github.com/faberlang/radix/releases/tag/faber%2Fv1.8.0) |
| **Radix companion** | 0.83.0 (`v0.83.0`) |
| **Published** | 2026-08-18 |
| **License** | MIT |

## Install this version {#install}

Pinned download for **Faber 1.8.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Checksum |
|---|---|---|
| **macOS arm64** | `faber-v1.8.0-aarch64-apple-darwin.tar.gz` | `22d688cce1565af4b8e4382ad425c5d6f66354352c7b3db5b9c1614356a8dbea` |

## Inference {#inference}

First correct end-to-end compiled inference, verified against pinned goldens:

- **SmolLM2-360M-Instruct (Q4_K_M)**: prefill top-1 **and** full top-5 match the
  reference exactly. Every operator family — embedding gather, all sixteen
  linear projections, attention (mask, softmax, RoPE, output projection), both
  residual adds — is golden-verified at the operator level, not just at logits.
- **Qwen2.5-0.5B-Instruct (Q4_K_M)**: closes the same loop, including its
  real QKV bias terms.
- **First autoregressive decode loop**: KV-cached incremental decoding with
  greedy sampling and end-of-generation stop. The first generated token
  matches the golden continuation; generation halts at EOS.
- **Runtime tokenizer**: byte-level BPE encoding over the model's own tables,
  pinned against the identity fixtures.

## Language {#language}

- **Shape generics** — chartered, implemented, and closed in this release:
  symbolic shape-changing contracts, glyph tensor arms, a generic
  `scaled_dot_product` in the standard ML library, and corpus exempla.
- **Keyword-as-identifier** — statement keywords and user identifiers now
  coexist by position: `print(print)` is a call on your function,
  `print print` is the output statement; bindings shadow builtins;
  every name slot accepts keyword spellings.
- **Formatter idempotency** hardening for postfix chains.

## Formats {#formats}

- Storage set grows to nine formats with **F16** and **MXFP4** admission
  (in-kernel dequant classes included).
- **KV cache structure types**: per-layer-set descriptors with dense,
  sliding-window, compressed, and heterogeneous cache classes.

## Quality {#quality}

- Rust emitter fix: recovery expressions on collection conversions were
  silently dropped — found by the new conversion-boundary exemplum.
- End-to-end fleet sweep with expectation ledgers truthed; the Swift lane is
  parked as a consumer-gated optional target with honest ledgers.

## Infrastructure {#infrastructure}

- Packet validation hardening (symlinked-lane refusal).
- Hosts `solum` digest route (streamed SHA-256) for model admission.
- Known-red disclosure: the 1.7.0 known-red suite was carried into this
  release per the known-red release rule.
