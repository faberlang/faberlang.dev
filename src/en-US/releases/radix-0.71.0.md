+++
title = "Radix 0.71.0"
section = "releases"
order = 26
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.71.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Host provider gateway architecture and LLVM-host parity campaign: pairwise output
ledger, package-expanded MIR consumption, diagnostic ABI namespace enforcement,
and JSON as a formal document genus.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 48 |
| `feat(...)` commits | 7 |
| `fix(...)` commits | 9 |
| Date span | 2026-07-09 → 2026-07-10 |

### Major tracks

#### Host provider gateway design

Record the pluggable dispatch architecture (documented in
`docs/design/host-provider-gateway.md`): host-kernel, native, and provider
runtimes with `-rs`/`-ts` suffix resolution, wildcard prefix providers, and a
compile manifest. Wire the Host Gateway Coverage campaign (`docs/factory/
host-gateway-coverage/`) to implement against this shape while keeping the
interim macOS monolith tactical for Goal A. Formally pause Metal GPU factory
work, routing Mac-local GPU proof through WebGPU and product inference through
CUDA. (`a5efb09d1`, `4dd347040`, `7ca49545a`, `bfd4417de`)

#### LLVM-host parity: campaign and baseline oracle

Propose and compile the LLVM-host parity campaign — a rustc-shaped host-native
LLVM path measured by per-exemplum stdout parity against Rust lane binaries.
Extract a reusable Rust oracle baseline model (`oracle.rs`) and refresh typed
runtime conversion dumps. Close the baseline oracle stage with a comprehensive
gap ledger (2200+ lines). (`d84a996f6`, `5b288f011`, `131f980e7`,
`52649646d`, `f67b82c94`, `6fc4d34ef`)

#### LLVM-host parity: versioned ABI and pairwise parity ledger

Close the versioned host ABI stage. Enforce a pairwise parity ledger tracking
pass/fail/gap per exemplum across LLVM and Rust lanes (1926-line TOML ledger
with harness and test infrastructure). Scope enum assertions to program body
boundaries. (`253ea3d6c`, `60212f8e8`, `8e089b763`)

#### LLVM-host parity: coherent tools and runtime bridge

Add a coherent `llvm_host` tool module (`llvm_host.rs`) with versioned host
LLVM IR entry emission (`host.rs` layout, declarations, emit path). Harden
imported Rust contracts used as the oracle baseline. Route LLVM exempla
through the Rust host runtime, replacing the standalone C e2e runtime shim.
(`fef675ea6`, `7bbd1340a`, `32b4f09af`, `0da50bb9c`)

#### LLVM-host parity: package-expanded MIR and Stage 3 reachability

Consume package-expanded MIR in the LLVM host lane. Close Stage 3 MIR
reachability: instantiate generic enum payloads, preserve sparse representation
semantics and nonzero counts, close verifier gaps (emission + layout fixes),
and close emission gaps. Route CLI MIR outcomes through the host lane and honor
explicit MIR targets in the driver. (`80536a1fc`, `3ad1c1f9c`, `ecd08283a`,
`442d1eb56`, `4893fdb48`, `d9bb192ab`, `087488d2e`, `beaccbd3f`, `f3f0ee7f5`)

#### LLVM-host parity: diagnostic family and ABI namespace

Close the diagnostic runtime family (assert, panic, scalar format, scalar
conversion imports) through the LLVM text backend. Enforce diagnostic ABI
namespace by correcting symbol prefixing, keeping host diagnostics in the
reserved `faber_diag_*` namespace and out of the user-visible name scope.
(`a64b8d13d`, `b5a53be9e`, `e165271c7`, `a6659faba`, `7674d81d3`, `70361aa19`)

#### JSON as a formal document genus

Make JSON a formal Faber document type across the EBNF, MIR device/layout/lower
tiers, and all codegen backends (Rust, Go, TypeScript). Support nested genus
document conversion and reject missing required genus fields. Box instans values
as text in the JSON genus and render JSON map keys as wire textus. Require the
JSON family for MIR wire keys. Track test coverage across Rust codegen,
MIR stepper conversio, and validation. (`e75cac7a6`, `fa0a1dea6`, `8fee34b85`,
`55f43afd7`, `ab7055599`, `c3251350f`)

#### Async sermo lowering

Record the async sermo runtime core and partial sermo lowering delivery. Fix
codegen to properly lower async sermo materialization across Rust decl, call,
conversion, expression, and statement tiers. (`5bf314f8d`, `7f174caf9`,
`55aeed472`)

### Other changes

- **Host kernel fixes:** route bounded solum byte reads in the macOS host kernel
  frame data path, and accept root text-list process arguments. (`c48b097ef`,
  `1e1fbf9f3`)
- **Codegen:** render exact Rust binding probes for external declarations; drop
  the obsolete private host attach shim. (`0392894d7`, `5daeefb36`)
- **Parser:** scope bodyless function declarations to library analysis only
  (not top-level executable context). (`70b60cbeb`)
- **Housekeeping:** satisfy `radix` clippy warnings; point corpus audit scripts
  at the examples repo. (`336701cd5`, `e491accb7`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
