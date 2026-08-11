+++
title = "Radix 0.62.0"
section = "releases"
order = 38
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.62.0 |
| **Tag** | `radix-v0.62.0` |
| **GitHub** | [radix-v0.62.0](https://github.com/faberlang/releases/releases/tag/radix-v0.62.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.62.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.62.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.62.0/radix-v0.62.0-aarch64-apple-darwin.tar.gz) | 2.0 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.62.0/radix-v0.62.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.62.0/radix-v0.62.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.62.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Synthetic retrospective minor tag covering the **HIR/MIR semantic sync** and
**stdlib merge** milestone. This is the first release where fail-closed lowering
invariants gate both compiler lanes, and the first where `norma` contracts unify
across the stdlib effect interface.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 89 |
| Date span | 2026-06-30 → 2026-06-30 |

Reconstruct the full log:

```bash
git log v0.61.0..v0.62.0 --oneline --no-merges
```

### Major tracks

#### HIR/MIR semantic sync — lista/tensor conversio

The dominant theme of this release. The compiler enforces **fail-closed lowering invariants** — any HIR construct that lacks a MIR lowering partner now produces a
hard error rather than silently dropping predicates.

- Shaped, rectangular lista literal → tensor conversio through MIR and Rust emit
  (`b65fb81e8`, `c74507750`)
- Fail-closed lista tensor MIR convert and lowering invariants
  (`a6ab2a7c0`, `039338f7e`)
- Close HIR/MIR cleanse validation across both lanes (`ce0fb6024`)
- Split `conversio` into focused submodules (`9cb660e1d`)
- Route intrinsic emit through a shared registry (`9b8d8b73e`)
- Redundant conversio emit guard removed (`96dda1295`)
- Centralize scalar display helpers and failable conversio channel checks
  (`f5a05945c`, `4a95ca091`)

#### Width type sugar for listas

Introduced per-width type aliases for lista literals (`lu32`, `li64`, `lf32`,
`lf64`, …) parallel to the existing tensor width sugar, closing a long-standing
parity gap.

- Add lista width type sugar (`57b905e5c`)
- Route width sugar keyword checks through a shared helper (`d998c6e1e`)
- Extract and unify lista/tensor width sugar type parsers and marker helpers
  (`3798520e0`, `9168c4e3e`)
- Fix tensor sugar conversio targets (`ce166c411`)

#### Tensor bracket access policy

Unified the bracket-indexing path through a shared `tensor_bracket` policy module,
replacing ad-hoc typecheck/MIR/Rust emit branches.

- Add shared tensor bracket access policy module (`8d19953bd`)
- Route tensor bracket typecheck through `tensor_bracket` policy (`be07eb5cd`)
- Use `tensor_bracket` list-index probe in Rust bracket emit (`47f6d7f35`)
- Unify MIR tensor bracket lowering on `tensor_bracket` policy (`9fa8ecb4c`)

#### Stdlib merge (factory/stdlib)

Eight-phase migration that wraps effect bodies in `ad` (automatic dispatch)
contracts and unifies `norma` kernel interfaces with `faber` runtime types.

| Phase | Content |
| --- | --- |
| **Phase 0** | Norma contract unification (`7efa08447`) |
| **Phase 1a** | Solum ad-wrapped effect bodies (`db2ee8eeb`) |
| **Phase 1b** | Processus sync ad bodies (`f57712898`) |
| **Phase 1c** | Aleator sync ad bodies (`5dd0c867e`) |
| **Phase 1d** | Consolum sync ad bodies + R2a TTY (`2c52cf7d4`) |
| **Phase 1e** | Tempus clock ad bodies (`e80f16684`) |
| **Phase 2** | Faber/norma kernel parity + Faber-vs-ad note (`18089ddbe`) |
| **Phase 3** | Native chorda.diducta (`aa830792c`) |

Phase 4 (native valor navigation in norma:toml, `914cad0b2`) and Phase 5
closeout (toml.exige_claves and explora contract exempla, `b893bef4f`) round
out the pipeline.

#### HIR/MIR stage parity fixtures

Systematic test coverage closing the parity gap between HIR and MIR stages.

- Close HIR MIR stage1 parity fixtures (`79d002aa3`)
- Close scalar conversio parity fixtures (`25f837211`)
- Align regex conversio parity (`d8448dc2d`)
- Align valor scalar, boxing, recursive aggregate, and aggregate-defaults parity
  (`ffc1e4a7c`, `087adfdbc`, `c8168ec21`, `80b5df2f0`)
- Align collection method policy (`9dac01b61`)
- Decompose scalar valor conversio sync rows (`3204b4707`)

#### Lista-to-tensor polish (dedup & extraction)

Systematic deduplication and extraction across the lista-to-tensor conversion
pipeline — MIR lowering, Rust emit, typecheck, and stepper.

- Unify lista-to-tensor MIR lowering through `TensorFromFlat` helper
  (`a9d599b49`)
- Extract rank-2 literal helpers (`a125e5e26`)
- Share `Tensor` structa emission for lista tensor conversio (`fbf035aa7`)
- Align lista tensor conversio structa emit with outcome ladder (`dfe343c64`)
- Tighten lista-to-tensor conversio typecheck arms (`6f0f00d2f`)
- Dedupe lista-to-tensor MIR lowering and Rust emit regression assertions
  (`64db01385`, `8f5a97904`)
- Polish stepper `Convert` fallback path and shape helper (`8fcd6cd5b`,
  `ee0cf2c90`)
- Polish lista-to-tensor structa emit helper return type (`f40ad1b6d`)
- Polish tensor bracket index typecheck signature (`8669860b4`)

#### Ordering, overflow, and lexer consolidation

- Centralize ordering comparison emission helper and dedupe Rust emit assertions
  (`9d71e8dfb`, `17e4019ae`)
- Cross-reference scalar longitudo ordering emit coverage (`f58947eda`)
- Align numerus overflow policy and polish overflow message constants
  (`014637b67`, `b79e21fc6`)
- Centralize line-start comment lexer policy and dedupe regression helpers
  (`4ed3273a8`, `5f13b9652`, `a7ebc4f8d`)

#### Generic param call-site unification

- Extend generic param call-site ratchet tests (`460019de4`)
- Extract generic call-site instantiation helpers (`e6b945f20`)
- Document `Type::Param` unification policy in infer (`784931f66`)

#### Factory planning & product framing docs

Extensive factory documentation shaping the next campaign waves.

- HIR/MIR semantic sync discovery ledgers (families 1–7, 8–12) and campaign
  staging (`70694bad9`, `8de340f14`, `a148341be`)
- Rectangular lista tensor conversio goal, Phase 1 closeout, and Phase 2
  library-method expansion (`0b091d0f5`, `0c438ac77`, `6e6521de3`,
  `63bba16d6`)
- App-stdlib naming contract, method naming table, and renaming tracks
  (`f65094786`, `dde83227c`, `a047619d4`)
- Architectural cleanse campaign: scope, mechanical posture, follow-up
  (`d068e01d3`, `137e9a4a1`, `9c563d1cd`)
- Two-lane product framing in `AGENTS.md` and `README.md`
  (`bdcd75220`, `a54fd6881`)
- Numeric type sugar spelling preference notes (`31699d3d9`, `9bb78fabf`)
- DEFER-066 (textus escape decoding) and DEFER-067 (si-block parse bug)
  documentation (`88056723a`, `838ecb303`)

### Other changes

- Share tensor policy helpers across `faber` (`e01653d08`)
- Polish exempla_e2e parity harness (`249ce2f71`)
- Link intentional split capability matrix (`3ea45438d`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
