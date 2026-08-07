+++
title = "Radix 0.61.0"
section = "releases"
order = 38
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.61.0 |
| **Tag** | `radix-v0.61.0` |
| **GitHub** | [radix-v0.61.0](https://github.com/faberlang/releases/releases/tag/radix-v0.61.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.61.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.61.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.61.0/radix-v0.61.0-aarch64-apple-darwin.tar.gz) | 2.0 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.61.0/radix-v0.61.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.61.0/radix-v0.61.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.61.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Faber script kernel and frame/script e2e hardening route. This release completes
the binary-owned **Faber script kernel** (phases 1–3) and drives the MIR stepper
through a large e2e hardening campaign that adds tensor intrinsic execution,
collection operations, conversions, and frame-gateway host streaming. A new **AIR**
(Abstract Intermediate Representation) layer is introduced and routed through MIR
targets.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 126 |
| `feat(...)` commits | 44 |
| `fix(...)` commits | 15 |
| Date span | 2026-06-29 → 2026-06-30 |

### Major tracks

#### Faber script kernel (phases 1–3)

- Add `faber:*` namespace and `MirProviderKind::Kernel` (`7f32f701c`)
- Stage 2: host dispatch, valor bridge, and manifest CLI (`33c185250`)
- Stage 3: binary-owned kernel sub-modules (aleator, args, json, processus, solum) (`5cb70ff44`)
- Add Faber glob import (`6158a33e5`)
- Lock v1 surfaces; record open architecture questions (`fc1329894`)
- Close faber-script-kernel campaign; route successor to e2e hardening (`492146638`)

#### MIR stepper — script e2e hardening

**Tensor intrinsics:**
- Run tensor intrinsics through the stepper (`46415fffe`)
- Run valor tensor carrier (`be629e8d5`)
- Lower `tensor_longitudo` in MIR (`7fee35dbd`)

**Collection operations:**
- Lower `lista` copy views (`ff7c51132`)
- Lower `lista` mutation methods (`ac57ce61d`)
- Lower `lista reducta` (`351ffab2b`)
- Lower `lista summa` (`ad15842a1`)
- Lower `tabula pone` (`ded9eb42a`)
- Lower `fractus approximata` (`f0e7341b6`)

**Conversions:**
- Support instans runtime conversion (`698e9a37d`)
- Support collection conversions (`a5a3705f1`)
- Propagate failable conversions through the stepper (`7789cc14e`)
- Support `octeti` index and append (`8f2ceed72`)
- Recover `octeti` conversions and radix hints (`bdf323953`)

**Operator methods and control flow:**
- Lower numeric operator methods (`c5e0cdc21`)
- Concatenate `textus` addition (`1d1622948`)
- Lower logical short-circuit (`93ebaa44b`)
- Run `valor` genus conversion (`2568a3e49`)
- Run regex constants (`3bd05b6ae`)

**Stepper fixes:**
- Run named variant payloads (`873b727ed`)
- Run optional index chains (`b3deffd18`)
- Require explicit script entry (`fac908eab`)

#### MIR lowering

- Lower nested JSON `valor` (`20ad670dc`)
- Lower handled conversions through try calls (`93bfdbd29`)
- Lower top-level const paths in functions (`4b7dcc8e3`)
- Lower `tacet` as noop (`170d8b10f`)
- Preserve variant `elige` fallthrough (`8a01ef98b`)

#### AIR (Abstract Intermediate Representation)

- Add AIR node model, names, and visitor (`d88bf76cd`)
- Lower HIR air lane to AIR (`3f8c3ea3a`)
- Validate and dump AIR (`aa7863f9a`)
- Relower AIR to MIR (`3729fb1fd`)
- Route AIR lane through MIR targets (`27b1e4401`)
- Enforce AIR purity policy (`a8bf2c091`)
- Add typed `tuus` payload views (`c6b02d78b`)
- Implement lane routing metadata (`f421379c1`)

#### Frame gateway (host runtime)

- Stage 4: host stream API (`2dd4c1a1e`)
- Implement runtime echo slice (`8f0465873`)
- Prove host-bound echo (`52bf44cea`)
- Scope Stage 5: runtime echo slice (`5d05e4155`)
- Add typed `tuus` payload goal (`e468219bb`)

#### Tensor

- Ship rank-2 matmul (`1acde416d`)
- Support tensor bracket access (`60010e2ba`)
- Tensor index intrinsics accept integer-width index lists (DEFER-064) (`4ece27f67`)
- Infer `f32` literal context (`86a980629`)
- Reject `u64` tensor index vectors (`c5efd0325`)
- Reject invalid shape and index input as recoverable errors (`0047509b9`)
- Polish intrinsic outcome emission and slice bound validation (`0c6e35a8e`, `cefb39812`)

#### Line-start-only `#` comment rule

- Reject mid-line `#` comments at lex time — Stage 1 (`6c8148677`)
- Reject C-style comments with a clear lexer diagnostic LEX006 (`8bbfd200b`)
- Address line-start comment review feedback (`18b76e14d`)
- Stage 0 docs: document the line-start-only `#` comment rule (`4496ac59c`)
- State mechanical/predictable thesis (`cf7105b38`)
- Close comment-preservation goal; add line-start-comments goal (`28cd87d95`)
- Close line-start-comments goal — Stage 4 (`d3be804b4`)

#### Metal / GPU spike

- Add Faber metal launch spike (`8ea6bf2c9`)
- Add metal text probe (`d794585eb`)
- Docs: frame payload model and lowering routes (`562d56205`, `db2a9d05d`)

### Other changes

#### Forma (formatter) polish

- Polish author `proba` modifier emission (`647bfc983`)
- Polish author layout trivia policy (`6eb2b62f0`)
- Polish canonical emission: postfix chains (`b4e3ffbea`), statement expression lists (`df8c80b35`),
  declaration helpers (`6ca1a2259`), type helpers (`452dc0887`), pattern emission (`5fddb8c70`),
  name policy helpers (`db3701baa`), emitter entrypoint (`32c02ed7f`), and object-field emission (`b6383c2ab`)

#### Module splits and CLI polish

- Split `faber-cli` 3000-line `package.rs` into focused submodules (`7b81690ed`)
- Split `package/mod.rs` into manifest, discovery, and compile (`83b16c200`)
- Split `cista` commands into per-command modules (`fe7bf1185`)
- Polish `cista` command install and cargo helpers (`9a2cc4e7e`),
  manifest display helpers (`b599edb4d`), and crate status string (`4fac8b4b8`)
- Light polish of `faber-cli` commands and reference tests (`d0408f2fc`)

#### Fixes

- Replace `Type::Param` assignment widening with call-site instantiation (`241f8c408`)
- Align `textus.longitudo()` with Unicode scalar indexing (`b07390271`)
- Parenthesize `MethodCall` lhs in ordering comparisons (`fba784518`)
- Preserve scalar numeric widths in arithmetic (`fe3b4866f`)
- Restore `tempus-civil` stdlib build (`ab677ccda`)
- Clear MIR gate for AIR routing (`25aebd15b`)
- Correct Homebrew reference pack install and formula tests (`6855d8d94`)
- Polish scalar interval closure context wiring (`99dbeb67b`)

#### Exempla test classification

- Classify instans `norma` script failure (`17208264e`)
- Classify `norma` script failures (`7fee35dbd`)
- Expect Latin boolean output (`59b9b937c`)
- Prune passing script failures (`278e01976`)
- Reconcile instans script fixture precision (`05a7c052b`)
- Classify script e2e expected failures (`efd6da9bf`)

#### Documentation and factory goals

- Record frame payload model (`27b1e4401`), document lowering routes (`562d56205`)
- Add AIR representation delivery spec (`9c4759c21`), purity policy gate (`7cfe03c17`),
  radix AIR composite campaign (`f421379c1`)
- Define script e2e hardening goal (`9021ae4e4`), constrain scope (`a88db1fcf`),
  include MIR codegen scope (`4b28e9f28`)
- Close `metal-kernel-spike` campaign (`1b509cfa2`)
- Add tensor index width goal history (`8d0956dd8`)
- Add `immutabilis` binding goal (`596145aea`)
- Defer tensor bracket codegen gap and KIR source gaps (`3f64c2a2b`, `d993b73d9`)
- Add local release runbook and expand v0.38.0 notes (`5b9770a5f`, `254efec75`)
- Move release validation into release dry run (`5cb70ff44`)
- Point releases section at `docs/release/process.md` (`9978161be`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
