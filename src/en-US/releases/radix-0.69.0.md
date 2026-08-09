+++
title = "Radix 0.69.0"
section = "releases"
order = 28
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.69.0 |
| **Tag** | `radix-v0.69.0` |
| **GitHub** | [radix-v0.69.0](https://github.com/faberlang/releases/releases/tag/radix-v0.69.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.69.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.69.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.69.0/radix-v0.69.0-aarch64-apple-darwin.tar.gz) | 2.8 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.69.0/radix-v0.69.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.69.0/radix-v0.69.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.69.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

FMIR package binary / package MIR target docs and final target descriptions.
This release builds the complete FMIR (Faber MIR) packaging pipeline across
three image formats — text, binary, and self-contained executable — and
closes the scena package target. On the planning side, the tensor systems
campaign timeline and shaped-value definition land alongside a clean-break
retirement of several obsolete source surfaces.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 58 |
| Date span | 2026-07-07 → 2026-07-08 |

### Major tracks

#### FMIR package binary pipeline

The MIR package binary campaign is established, executed, and documented
across three image formats:

- **FMIR text image floor**: add the base text-format image target,
  including lexer tokens (`fmir_text`, `fmir_bin`), MIR ABI extensions,
  and semantic type wiring (`bd1d4baa6`).
- **Text image hardening**: robust loading with deserialization error
  handling and round-trip validation (`1fc6b1268`).
- **Type metadata serialization**: Radix serializes full type metadata
  into the FMIR text format, covering precision, numeric width, and type
  index data (`751d49f14`).
- **CLI argument binding**: runtime CLI arguments are bound to FMIR text
  image parameters through the runner's invocation path (`ebc2d715c`).
- **Normalized package runner**: the FMIR stepper loader boundary is
  refactored into a consistent runner abstraction shared across formats
  (`6f3770e70`).
- **FMIR binary image target**: add a compact binary image format with
  its own target and package surface (`537162870`).
- **FMIR executable bundle target**: produce a self-contained native
  executable that bundles the MIR image with a stepper harness
  (`4709762dc`).
- **Executable runner embedding**: the bundled executable runner is
  wired end-to-end through the radix codegen pipeline, package build
  commands, and integration tests (`9bcb6c89a`).
- **Polish and final descriptions**: preserve raw FMIR source paths,
  align `fmir-exe` target naming, and describe final package targets in
  README and help docs (`b2ab1d213`, `3b46a8c56`, `6ec050ebd`).

Campaign docs manage the lifecycle: open, close, reopen for the expanded
FMIR scope, record the native packaging decision, and lower each stage
(`487142805`, `c22a621a1`, `769b7fa64`, `c506e91f1`, `6962cd7d5`,
`6075741eb`, `49ec77d11`).

#### Scena package target

- **Target commands wired**: `scena` package target commands are
  integrated into the faber-cli CLI, radix codegen coverage, driver, and
  semantic passes (`1f04710c2`).
- **Target capability advertised**: the scena target is listed in the
  capability matrix, help docs, and `radix targets` output
  (`9c9a40521`).
- **Runtime requirements declared**: scena artifacts declare host runtime
  requirements via a manifest (`e7bb55770`).
- **CLI exit gap burned down**: scena CLI exit behavior is hardened with
  expected-failure tests and gap analysis (`4cf67de54`).
- **Artifact harness floor**: test harness coverage for scena exemplars
  and coreutils artifact validation (`f65fa1d18`).
- **Closeout**: final packaging, delivery doc, and v0.39.0 release note
  update (`7e12b5d74`).

#### Tensor systems campaign (planning)

- **Tensor systems timeline**: full campaign timeline with seven goal
  documents: tensor semantics contract, storage locus, layout views,
  failable runtime, packed numeric blocks, MIR tensor operation parity
  (`289d8db3e`).
- **Semantics refined**: narrow the tensor semantics contract, clarify
  neighbor types, and mark the tensor lane as MIR-first
  (`7cb2ef013`, `97db4d7bb`, `f82bc889f`).
- **Shaped values defined**: MIR-first shaped value family documented
  with scalar elements, storage locus descriptor facts and first-slice
  conventions (`7c6cacd45`, `ecbcb6f92`, `51f638846`, `79339bbc1`,
  `68f9159df`).
- **Campaign structure**: campaign made implementation-shaped with
  extended end-to-end roadmap, locked MIR stepper target, locked model
  fixture, and tensor sectio view-producing semantics
  (`b084394bb`, `5b58312d9`, `7e2f581a3`, `733e5ebb3`, `2da5f2503`).

#### Retired surfaces clean break

- **Clean-break goal**: retire externa, subsidia, and HAL as source
  surfaces; retain `@ verte` as a time-boxed exception until the unified
  package manifest resolves codegen template placement
  (`237c9f7f1`, `025110475`).
- **Externa and subsidia removed**: all externa/subsidia source fixtures,
  codegen paths, parser/syntax promotion, annotation lowering, and
  exempla fixtures are deleted. Target policy simplified
  (`255976d07`).
- **HAL surface references purged**: runtime HAL fixture files, library
  import paths, and documentation references to the retired HAL surface
  are removed (`17168bb92`).
- **Stale wording removed** from EBNF, README, and target capability
  matrix (`6d829af3d`).
- **Verte alias residue and Zig target mentions** cleaned up
  (`8722442f6`, `62b11b670`).
- **Legacy error fixtures** replaced with fac cape equivalents
  (`e626ac9b7`).

### Other changes

- **External library home**: factory goal and implementation for
  resolving libraries from an external home directory; replaces the
  2800+ line norma stdlib directory with a slim external lookup path
  (`9a7b22258`, `d214d84d8`). Clippy lint satisfied (`067bca00e`).
- **Unified package manifest**: planning doc for a single canonical
  manifest format replacing the split faber.toml / cargo.toml world;
  Phase 3 text-scan claim corrected (`fbdb1f412`, `664bfa288`).
- **Norma retirement CI**: test adjustments to keep fast CI green while
  the norma stdlib directory trees are removed (`fa58e2013`).
- **Worktree home standardized**: worktree convention doc and audit
  script aligned (`2526c75a5`).
- **Stale external declaration comments** removed from syntax modules
  (`682562cb5`).
- **Modulus namespace wording** retired across stdlib docs and scripts
  (`5d1c56851`).

---

[All releases](/releases/) · [Install the current release](/start/install.html)
