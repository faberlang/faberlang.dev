+++
title = "Radix 0.49.0"
section = "releases"
order = 50
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.49.0 |
| **Tag** | `radix-v0.49.0` |
| **GitHub** | [radix-v0.49.0](https://github.com/faberlang/releases/releases/tag/radix-v0.49.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.49.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.49.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.49.0/radix-v0.49.0-aarch64-apple-darwin.tar.gz) | 1.8 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.49.0/radix-v0.49.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.49.0/radix-v0.49.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.49.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Breakable blocks ship end-to-end: `rumpe` generalises from `fac` to loops,
closures, and `meus`/`tuus` ad arms. The frame gateway architecture design is
laid in parallel, establishing the protocol model and stage-1 stream-types
spec that `emitte` will build on. Backend smoke-check CI hardens alongside.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 37 |
| Date span | 2026-06-25 → 2026-06-26 |

### Major tracks

#### Breakable blocks: `rumpe` with `fac`, `meus`, `tuus`

The breakable-block work that began in earlier cycles reaches a
cross-target implementation milestone. `rumpe` — the breakable-block
construct — generalises beyond `fac` (loop) to cover closure fac and
arbitrary statement blocks. The `meus` (receive) and `tuus` (send) ad
arms are parsed, lowered through HIR/MIR, and codegenned for Rust, Go,
and TypeScript targets.

- Generalise `rumpe` to breakable blocks: `fac`, loops, closure fac
  (`db7ecf75f`)
- Parser-first `meus`/`tuus` breakable ad arms for `rumpe`
  (`496f77901`)
- Correct breakable fac closure codegen for `rumpe` (`0df91398a`)
- Emit `meus` auto-done epilogue in breakable ad codegen (`92f28333e`)
- Repair breakable-block MIR CFG for `rumpe` (fac, meus, tuus)
  (`62b5dfbef`)
- Close breakable-blocks codegen skeptic gaps, phase 1 (`a43dd2ad4`)
- Close breakable-blocks codegen skeptic gaps, phase 3 (`34d7a279f`)
- Add breakable-blocks goal design doc; link from gateway architecture
  (`2736c44ff`)
- Clarify `tuus rumpe` drains gateway terminal before ad completes
  (`3428f9b19`)

#### Frame gateway architecture design (`emitte` groundwork)

A dense design track lays the foundation for stream-based frame
gateways. The architecture document (`frame-gateway-architecture.md`)
goes through multiple review rounds: opaque routing, bidirectional
protocol with `meus`/`tuus` arms, Latin type naming (`nuntius`,
`status`, `sermo`; envelope → `scrinium`; `discerne`), sequential ad
arms with one `emitte` per frame, and an ASCII route requirement at the
Faber layer. A campaign and stage-1 `frame-stream-types` spec are
published. The architecture is then aligned with the breakable-blocks
shipment that shipped alongside it.

- Capture frame gateway architecture design (`13e8cb040`)
- Add frame gateway reviewer notes (`a92ae304d`)
- Rewrite frame-gateway architecture around opaque routing
  (`b37e3e5de`)
- Address frame-gateway review: frame types, ABI, strict shape
  (`1a4087549`)
- Fix frame-gateway review leftovers: slice gating, host ABI, refs
  (`9c58d7d55`)
- Revert ad input ABI to opaque payload (`fcf383170`)
- Make frame protocol bidirectional with `meus`/`tuus` arms
  (`acfa02c36`)
- Tighten frame protocol terminology and termination (`c96c2b0fc`)
- Adopt Latin type names `nuntius`/`status`/`sermo` (`1cdbaaf9f`)
- Rename envelope to `scrinium`; use `discerne` for status
  (`c94391ada`)
- Capture ad consumer and payload decisions in gateway architecture
  (`84f5ec46a`)
- Settle sequential ad arms and one `emitte` per frame (`27e30d931`)
- Require ASCII route at the Faber layer (`466907f70`)
- Close remaining review questions in gateway and breakable-blocks
  (`97d83dc29`)
- Add frame-gateway campaign and stage-1 `frame-stream-types` spec
  (`8353420d1`)
- Align frame-gateway architecture with breakable-blocks shipment
  (`8fc1fb39c`)

#### Backend smoke-check CI infrastructure

The smoke-check infrastructure generalises from a Rust-specific check
into a multi-backend smoke framework with shared helpers, trace logging,
a canonical `smoke.rs` module, and a `smoke-ci` script lane.

- Generalise Rust smoke-check into `backend-smoke-check` goal
  (`d9f22307e`)
- Add shared backend smoke helpers and `smoke-ci` lane (`d4af8445e`)
- Harden smoke helpers: skip unsupported targets, add self-tests
  (`c416e6163`)
- Canonicalise `smoke.rs` and fix regression-guard emit paths
  (`ebf4463fc`)
- Add smoke trace logging and backend smoke evidence recorder
  (`68eaab5d1`)
- Clarify B-002 phase references canonical `smoke.rs` module
  (`cf7dc077b`)
- Polish `exempla_e2e/common.rs`: refresh module doc for smoke hoist
  (`ca425ee66`)
- Fix `scripta/smoke-ci` TypeScript toolchain: ensure deno, not
  `tsc`-via-node (`9a5fdb698`)
- Polish `exempla_e2e/smoke.rs`: document the `assert!`/`loop{}`
  budget idiom (`3899e071b`)
- Mark `backend-smoke-check` policy table rows done (`f5399b1cd`)

### Other changes

- Record black-hat language-surface findings DEFER-011..020
  (`33ce4b395`)
- Close `ad-core-capabilities` as won't fix (`5b707707d`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
