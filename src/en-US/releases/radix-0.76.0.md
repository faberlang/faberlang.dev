+++
title = "Radix 0.76.0"
section = "releases"
order = 23
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.76.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Minor release spanning **~204 commits** (`v0.75.0..v0.76.0`). This is the first
**crate-versioned** minor after the synthetic history ladder that ended at
`v0.75.0` (marker tags with crate manifests still at `0.38.0`). Manifests move
from `0.38.0` → `0.76.0` so source tags, `crates/radix` version, and public
`radix-vX.Y.Z` artifacts stay aligned.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | ~204 |
| `feat(...)` commits | ~42 |
| `fix(...)` commits | ~29 |
| Workspace crate DAG extract stages | 0b–8 |
| Reader packs with full 653 diagnostic rows | 7 (`la`, `hi`, `ar`, `zh-Hans`, `th-TH`, `vi`, `zh-Hant`) |

Reconstruct the full log:

```bash
git log v0.75.0..v0.76.0 --oneline --no-merges
```

### Major tracks

#### Language: `ergo` vs `∴` clean break

- **`ergo`** is the only statement-body joint (`si … ergo …`, `casu … ergo …`).
- **`∴`** is the only compact **clausura** joint.
- Distinct diagnostics: PARSE026 (∴ in statement body), PARSE027 (`ergo` in clausura).
- Lexer tokens: `TokenKind::Ergo` vs `TokenKind::Therefore`.
- Exempla and deferred docs updated; clausura examples keep `∴`.

#### Reader locale packs (Stage 2 diagnostics)

- Full **keyword + type** packs for the non-Latin locales (EBNF-first).
- Full **653 diagnostic** templates for:
  - Hindi, Arabic, Simplified Chinese (earlier in range)
  - **Thai (`th-TH`), Vietnamese (`vi`), Traditional Chinese (`zh-Hant`)** (this release)
- Locale EBNFs promoted (`EBNF.hi.md`, `EBNF.th-TH.md`, …).
- `[llm]` snippets preserved on every installed pack.
- Reader-locale emit surface: pack reverse lookup, HIR→Faber threading,
  `cmd_emit_with_reader_pack`, visible Latin-fallback notice.

#### Workspace crate DAG (compiler modularization)

Extract stages that leave the monocrates split while keeping one workspace:

| Stage | Extracted crates (theme) |
| --- | --- |
| 0b | `radix-codegen-shared` |
| 1B | `radix-diagnostics`, `radix-lexer`, `radix-syntax` |
| 1C | `radix-types`, `radix-hir` |
| 2–4 | `radix-codegen-{ts,go,rust,faber}` |
| 5 | `radix-mir` |
| 6 | MIR sexp / metal / wgsl emit leaves |
| 7 | host-abi + MIR llvm/wasm emit leaves |
| 8 | runtime-contract, stepper, coverage |

Pedantic clippy deny waves applied across leaves after extract.

#### Modular words and unsigned literals

- Width-parametric modular word family (`u8` / `u16` / `u32` / `u64`).
- Unsigned `u64` magnitude through lexer, syntax, and HIR.
- MIR stepper carriers for UInt constants, map keys, equality, bitwise, sort.
- Target parity and mutation hardening for modular words.

#### Conversio, indexing, ABI

- Conversio coverage matrix (Phase 1: rust + wasm-text) with fixture-backed cells.
- `textus[i]` / `ascii[i]` return `numerus` (Unicode scalar), zero-allocation path.
- Radix-owned **host ABI** contract and `radix abi` tool surface.
- Literal regex patterns capped at 1024 bytes (DEFER-019).

#### MIR / GPU / AIR proofs

- WGSL fragment entry + varying contract proof.
- AIR eligibility ledger, same-shape derivative oracle, companion metadata,
  same-shape transform and air→MIR backward validation proofs.
- MIR backward result contract proof; inference blocker matrix; rank2 readiness map.

#### Parser / semantics / codegen fixes (selected)

- Optional `si` guard on `mori` / `iace`.
- Rust codegen: interface values as `Box<dyn Trait>` (DEFER-117); `in` parameter
  mutability and owned returns; format! quote escaping; tabula `HashMap` fields
  (DEFER-115); `incipit argumenta` binding.
- WARN015 for unrecognized `curata` allocator names.
- Valor wire: preserve Instans/Octeti tags through frame JSON codec.
- TS codegen: restore lista valor boxing after pedantic merge.

#### Release tooling

- Explicit Linux build contexts; RC-safe local release phases (docs + CI plumbing).
- Shared public artifact surface remains `faberlang/releases` with `radix-vX.Y.Z`.

### Breaking / author-visible

| Change | Migration |
| --- | --- |
| Statement-body `∴` rejected | Use `ergo` (`si cond ergo redde x`) |
| Clausura `ergo` rejected | Use `∴` (`numerus x ∴ x * 2`) |
| Vector type-call constructors (if still in older notes) | Prefer `[lanes…] ↦ vf32[N]` / `vector<T,N>` forms per EBNF |

### Version alignment note

Synthetic annotated tags `v0.36.0`–`v0.75.0` document history themes; their
checkouts kept crate manifests at `0.38.0`. This release **realigns** the
semver ladder: `v0.76.0` tag ≡ `crates/radix` `version = "0.76.0"` ≡ public
component release `radix-v0.76.0`.

Draft `docs/release/v0.39.0.md` (script-kernel campaign notes) remains historical
campaign prose; it is **not** this crate version.

### Verification (pre-release)

Recorded on the release candidate tree (2026-07-20):

| Gate | Result |
| --- | --- |
| `./scripta/lint` (`-D warnings`) | pass |
| `./scripta/test --full` with `RUST_TEST_THREADS=1` | pass (static gates, `cargo test --all`, MIR/HIR matrices, hir_mir_stage parity) |
| `cargo build --locked --release -p radix --bin radix` | pass |
| `./target/release/radix --version` | `radix 0.76.0` |
| `cargo test -p radix --lib installed_` | pass (all 7 packs load) |

Re-run on the release commit:

```bash
./scripta/lint
RUST_TEST_THREADS=1 ./scripta/test --full
cargo build --locked --release -p radix --bin radix
./target/release/radix --version   # expect 0.76.0
```

Notes:

- LLVM host link-and-run fixtures are not parallel-safe on this host; use
  `RUST_TEST_THREADS=1` for the full exempla lane (or run `llvm_host_*` alone).
- Conversio matrix freshness requires a stable `ROWS` marker under libtest
  `--nocapture` (fixed in this release).

### Publish

1. Push `main` (includes this notes file and version bump).
2. Annotated tag: `git tag -a v0.76.0 -m "Radix v0.76.0"`
3. Push tag: `git push origin v0.76.0` (triggers `.github/workflows/release.yml`)
   or `workflow_dispatch` with tag `v0.76.0`.
4. Confirm `faberlang/releases` publishes `radix-v0.76.0` multi-arch archives.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
