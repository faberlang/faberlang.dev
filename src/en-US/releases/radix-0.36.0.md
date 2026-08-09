+++
title = "Radix 0.36.0"
section = "releases"
order = 61
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.36.0 |
| **Tag** | `radix-v0.36.0` |
| **GitHub** | [radix-v0.36.0](https://github.com/faberlang/releases/releases/tag/radix-v0.36.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.36.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.36.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.36.0/radix-v0.36.0-aarch64-apple-darwin.tar.gz) | 1.1 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.36.0/radix-v0.36.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.36.0/radix-v0.36.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.36.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Release spanning **92 non-merge commits** (`v0.35.0..v0.36.0`). This tag
closes out the MIR foundation campaign: the full compiler middle-end — data
model, structural visitor, phased lowering (primitive expressions through
runtime intrinsics), validation, and Rust probe — has been delivered. Alongside
the MIR work, the language syntax gains structural-equals fields, compact
closure ergonomics, and several string/text refinements.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 92 |
| Date span | 2026-05-22 → 2026-05-23 |

### Major tracks

#### MIR foundation closeout (Phases 0–9.5)

The planned MIR layer factory was delivered in ten phases:

- **Phase 0 — Data model:** initial MIR node types, test fixtures, and delivery
  specification (`12a9326c9`).
- **Phase 1 — Layer design:** factory plan, design questions resolved
  (`7c42c8b9f`, `5cb6928d7`).
- **Phase 2 — Inspection:** `radix mir` subcommand with contract completion
  (`9750265db`, `0bf5fb8e9`).
- **Phase 3 — Primitive lowering:** expression lowering for scalar/primitive
  forms (`8a3104efe`).
- **Phase 4 — Control-flow lowering:** `si`/`casu`/loop MIR lowering
  (`dbdf0fb58`).
- **Phase 5A — Alternate exits:** function surface (`redde`, `iace`, `mori`)
  and MIR lowering (`29a9899fd`, `025cdde51`).
- **Phase 5B — Structured cape:** full cape (`exit`, `throw`, `raise`) MIR
  handling (`3b56cdcc6`, `e4c97d216`).
- **Phase 6A — Aggregate contract:** MIR contract for aggregate/option forms
  (`c9692aead`).
- **Phase 6B — Lowering:** aggregate and option MIR lowering
  (`675116d99`).
- **Phase 7 — Runtime intrinsics:** intrinsic function MIR lowering
  (`06f5ac726`).
- **Phase 8 — Validation:** structural MIR validation pass
  (`2409bc7b4`, `dfea2ec70`).
- **Phase 9 — Rust probe:** Rust ABi compatibility probe (`ae8610d99`).
- **Phase 9.5 — Hardening closeout:** documentation finalization and coverage
  hardening (`9e1df660e`, `c4dfbc50e`, `1268eb8cb`).

#### MIR visitor infrastructure

A structural MIR visitor was built to unify dump, probe, and validation
consumption, replacing ad-hoc traversal across the codebase:

- Read-only HIR visitor (`6605ecdbd`).
- Structural MIR visitor (`c1323f511`).
- Fallible visitor with lowering context collector (`4870a7f15`).
- MIR dumps rendered through the visitor (`9e4e3f967`).
- Visitor applied to probe and validation (`a16732d63`).

#### MIR lowering module decomposition

The monolithic `mir/lower.rs` was split into focused submodules, each routed
through the HIR visitor:

- Expression visitor as the recursive lowering path (`b20cd345c`,
  `a66893127`).
- Statement, item, and context submodules (`e16e76313`, `0a7b0b5dc`,
  `6466c3595`, `1bebbfc3d`).
- Control-flow and runtime helper extraction (`9ab314a52`, `ed652f6dc`,
  `ac5fcd9fe`).

#### Language: structural-equals syntax

A new structural-equals (`==`) feature was designed and delivered across
parser, semantics, and codegen:

- Parse structural-equals fields (`f9d682aa0`).
- Object destructuring aliases (`f3b368eaa`).
- Typed vacua expression (`aaa25fa17`).
- Retire colon (`:`) structural fields (`cc18a4dc2`).
- Canonicalize structural-equals syntax in explain docs (`8e6027809`).

#### Language: compact closure ergonomics

The `ergo` vs `∴` (therefore) syntax was settled and implemented:

- Document closure ergo syntax plan (`523bde65e`).
- Choose therefore glyph for compact clausura (`6054492b3`).
- Adopt `fac` block closure syntax (`6ee32e675`).
- Refine inferred closure parameter syntax (`a50fbe535`).
- Implement compact closure `ergo` syntax (`a3ad2a641`).
- Fix typecheck `redde` in closure blocks (`6567453e4`).

#### Language: string and text refinements

- Remove backtick template string syntax (`a98df1846`).
- Use glyph block strings (`877690327`).
- Support Unicode `textus` indexing and slicing across Rust and TypeScript
  codegen (`1256b6b67`).
- Add string literal format application (`329d3337d`).
- Normalize `scriptum` placeholder indexing (`89e588e97`).
- Document template application as canonical (`8b32de0bc`).

#### Language: minor syntax cleanup

- Remove C-style comment syntax (`/* … */`) (`a33cb7304`).
- Narrow `cura` to allocator-only syntax (`50a6f7da3`).
- Add explicit inferred type marker (`ubi` glyph) (`9be2759c4`).

#### CLI and tooling

- Add `--format` and `--linter` flags to `radix emit` and `radix build`
  (`4cd55c139`).
- Add macOS arm64 Faber host placeholder crate (`5610e75b1`).

#### Documentation and planning

- Add faber commandments and conjugation commandment (`7ad42cdfb`,
  `5a28a88ee`).
- Plan requirit package manager design and registry policy
  (`9689671d0`, `6705e6917`).
- Plan lint and format tooling (`617a358e9`, `9fe6ade4d`).
- Plan structural-equals syntax (`865223397`).
- Fold `grammatica/` into `explain/` and `EBNF.md` (`95adebe63`).
- Add deduplication and testability decomposition analysis report
  (`497eb6d32`).
- Add release notes for v0.7–v0.34 from tag commit history (`2961c55d5`).
- Repair README release and quick-start drift (`f402dcf87`).

#### Chores

- Make hygiene ratchet robust (cwd-independent via `CARGO_MANIFEST_DIR`)
  (`db03c3332`).
- Validate structural-equals rollout (`373c70fd8`).

#### Examples

- Make automation package manifest-backed (`5fe651ce1`).
- Add automation package proba tests (`5e7a84765`).

### Verification

```bash
./scripta/lint
RUST_TEST_THREADS=1 ./scripta/test --full
cargo build --locked --release -p radix --bin radix
```

---

[All releases](/releases/) · [Install the current release](/start/install.html)
