+++
title = "Faber 1.7.0"
section = "releases"
order = 14
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.7.0 |
| **Tag** | `faber-v1.7.0` |
| **GitHub** | [faber-v1.7.0](https://github.com/faberlang/releases/releases/tag/faber-v1.7.0) |
| **Published** | 2026-08-15 |
| **License** | MIT |

## Install this version {#install}

Pinned download for **Faber 1.7.0**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.7.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.7.0/faber-v1.7.0-aarch64-apple-darwin.tar.gz) | 8.0 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.7.0/faber-v1.7.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.7.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.7.0/faber-v1.7.0-x86_64-unknown-linux-gnu.tar.gz) | 8.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.7.0/faber-v1.7.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.7.0/faber-v1.7.0-aarch64-apple-darwin.tar.gz
tar -xzf faber.tgz
# The archive ships bin/ and share/; keep them together so the
# reader packs resolve beside the binary.
sudo mv bin/faber /usr/local/bin/faber
sudo mv share/faber /usr/local/share/faber
faber --version
```

## Release notes {#notes}

> **Status**: final

Minor product release spanning **383 commits** since the faber 1.6.0 pin
(`6e0438132`, 2026-08-12→2026-08-15). Headline: **Haskell and Python source targets are planned and wired as emittable HIR backends**, the **visibility model flips to `@ publica` / `@ interna`-only export**, the **composite-plan surface lands** (typed shape, assembly, identity verification), the
**convert command and U8 lane-gating feature work complete**, and the release
pins the tested **radix 0.82.0** companion. The range also hardens
package-MIR locale handling and the FMIR script surface, and closes with the
**release stabilization set** (`5bdaabaad..80dedd5f6`: U8 completion,
early-merge integration set, all stabilization repairs) that fixed the
exempla/runner/emitter lanes for the e2e fleet sweep.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 383 |
| `feat(...)` commits | 45 |
| `fix(...)` commits | 58 |
| `docs(...)` commits | 89 |
| `test(...)` commits | 11 |
| `style(...)` commits | 4 |
| `chore(...)` commits | 8 |

Reconstruct the full log:

```bash
git log 6e0438132..80dedd5f6 --oneline --no-merges
```

### Major tracks

#### Haskell and Python source targets

The faber side of the new HIR source backends:

- **Haskell package artifact paths planned** (`22cd80df6`) on top of the
  `radix-hir-haskell` pure floor, IO/Either/scalar workers, and
  `Target::HirHaskell` / `haskell` CLI.
- **Python package artifacts planned from analyzed units** (`6ae49499c`) on
  top of the frozen `radix-hir-python` HIR floor and `Target::HirPython` /
  `-t python`.

Both remain source-emit surfaces; the executable package build/run lanes are
rust-first.

#### Composite-plan surface (EXEC-01)

- **CompositePlan typed shape, assembly, composite-plan v1 serialization**
  (EXEC-01-M1, `557e166fe`).
- **Composite-plan identity verification + first-divergence diagnostics**
  (EXEC-01-M2, `c22e53e1c`).
- Synthetic composite-plan mechanism proof + receipt (EXEC-01-M3,
  `d256be09d`).

#### Visibility model Phase 2

Faber follows the visibility clean break:

- `@ interna` annotation parse surface (VM-U1), export surface flips to
  `@ publica` / `@ interna` only (VM-U2), `privata` dropped on imports with
  `publica` re-export kept (VM-U3), export tiers threaded into import
  resolution with `@ interna` failing closed (VM-U2), and import-validator
  seams by tier × package (VM-U4).
- Type-alias exports join the import surface (`@ publica typus`,
  `33317242a`).

#### Package-MIR and FMIR fixes

- **Sparse package MIR ids allocated** (`0dcf49f3c`) and **collision-free MIR ids** (`d06b6f8d1`); **gradient package links traversed**
  (`9a0820edb`).
- **Captured GGUF range sources execute** (`09168a3b9`); **conversion source types preserved** (`85b5c2709`).
- **Library locale surfaces linked in package-MIR** (`e7f24a60e`), erased in
  HIR under pack authority (`031911ae1`), and lowered to canonical Rust names
  in emit (`1a84c02a6`).
- **FMIR CLI honors script locale and binds rest textus** (`7dd04eb42`).
- Stepper bulk-converts numeric lists to octets (`c1fed64ca`).
- **Import-contract seam recompute retains the resolved target path in the session cache** (`d7bc8124b`), with the compiler set's stage-2 clippy
  findings cleared (`649148e5e`) and `Target::HirPython` covered in
  `lint_generated_code` (`807e83ad5`).

#### Locale and reader packs

- **Library-owned `locale/<id>/pack.toml` fragments load** (`8cda5ca5a`);
  pack-authoritative intrinsic lookup with no Latin fallback (`6a37bae8d`);
  Phase-2A gradient reader-pack rows completed × 8 packs (`f4e6bec7d`).
- Schema (census-types) diagnostics carried through locale: S2-U5
  relational-view reader rows + schema diagnostics × 8 packs (`bf1bf6ef8`)
  and the five-row diagnostic re-home (`0b4180cc2`).

#### Tensor-glyphs and shape-generics (companion surfaces)

- **Glyph product parse surface + rank-rule typecheck + host Rust emission**
  with fail-closed glyph-product arms (`d1f89f6cf`, `5fde8ef74`,
  `0812e7269`, `bf0011d02`); glyph-spelled device kernels emit on metal/wgsl
  (`735165490`); postfix gradient selection parse surface (`766136fa0`).
- **Symbolic AIR shape scalar + VJP surface** and generic backward primal
  admission (shape-generics P3 units 3A/3B/3C, `26af0c5a3`, `3167728f0`,
  `7399c6025`).

#### Ladder and tooling

- **Stage 4 splits into 4a–4d** (`5e3adaab9`); stage 2 lints compiler libs
  only, stops compiling wasmtime, and shares one test compile; one clippy
  over the compiler set with a persisted inventory.
- Compatibility measurement JSON emitted for faber matrix rendering
  (`f916a08d1`, `53d3315c0`).

#### Post-pin delivery (2026-08-14→2026-08-15)

Work that landed after the initial 1.7.0 prepare but inside this release
range:

- **`faber convert` command** — explicit reader-locale conversion with
  `format --locale` retired (`01a2d3c94`), `available_locales` public API
  (`5bdaabaad`).
- **U8 lane gating** — runner/device/emit-leaf features, MIR build with zero
  output formats (`2965a8f00`); **default-off parse→analyze→HIR** with
  `radix-mir` optional behind `mir-core` (`a2f02ed0c`); language vocabulary
  moves down to `radix-types` (`ed5eab7df`).
- **D1 git-dep runtime form** — generated manifests resolve faber-runtime /
  hosts from git sources (`3ddd020de`); dev-kit tooling drops core-support
  references (`869398bae`, `1b5bb6523`).
- **Test/e2e rework** — `scripta/e2e` per-target stage driver + stage-scoped
  exempla harnesses (`7481bf0c3`, `0ff26b92d`); `faber run` is interpreted
  execution always (`7412e5e55`); `mir::stepper` renamed to `mir::runner`
  (`db8fcf9f7`).
- Codgen repairs: tensor reple value-position filled copy (`d444651ce`),
  publica re-export member paths on the root module tree (`6ffe0957d`),
  catch-local error type in handled blocks (`3922dd2d3`).

#### Release stabilization range (5bdaabaad..80dedd5f6)

The final stabilization set that closed the release (U8 completion, early-merge
integration set, all stabilization repairs). Every commit verified against the
repo:

- **E2E lane builds + U8 remainder** — lane-scoped exempla features and
  `scripta/e2e` lane builds (`e094bcf06`), wrapper lane features for e2e
  harness invocations (`e2e0caead`), lane-gated tests behind enabling
  features with the core-only suite green (`34caab3e3`).
- **Runner matrix display** emits nested rows matching compiled-route goldens
  (`b4fb08d71`; closed need `9ca6437d`).
- **Go/TS value-position reple** fills a fresh copy (`b8f824790`; closed need
  `fb06c8c5`), with tensor-glyphs go tables re-landed (`3e4f82a28`, closed
  need `8e00f78b`) and `@faber/runtime` materialization re-landed
  (`6661a3ba0`, closed need `920c6334`).
- **Emit-compat-json passes `--features mir-core`** (`55198ca46`, closed need
  `e8822722`); compatibility measurement JSON refreshed — instans capable +1,
  incdec glyphs ↓/↑ (`487e1a556`, closed need `ec8bf5c6`).
- **Exempla table repairs** — 30 stale swift-emit fixtures as expected
  compile failures (`4ce9a318f`, closed need `23cb01b0`); cuda glyph-proof
  fixtures pinned at the fail-closed wasm tier floor (`4c2edbd92`, closed need
  `70728fa9`), ledgered as runner NoEntryReference failures (`6d359fc9f`).
- **E2e sibling gate** — canonical ancestor-walk fallback (`7c04532f2`,
  closed need `eee9f06d`); **forma author emit** renders the reader pack's
  keyword surface (`767c9027a`); fhir run integration test aligned to the
  interpreted-execution contract (`417109683`).
- **Release tooling** — release-doctor/install-faber test fixtures aligned
  with the D1 form (`1b5bb6523`); U4 followup drops core-support references
  from dev-kit tools (`869398bae`); release-docs zombie pass (`3a350ef91`).
- Tensor-glyphs Phase 2 clean-break re-plan — postfix gradient selection
  (`852d4bcbb`, planner-5 task `b2920cd5`).

### Pin pair

The release-manifest pins the tested companion revisions at the tag:
faber `1.7.0` against **radix 0.82.0** (tag commit), cista `0.1.0`,
faber-api and hosts per `release-manifest.yaml`. The `--locked` release build
from these pins is the proof; `publication.releaseTag` is `faber-v1.7.0`.

### Known-issues (acknowledged open handles)

These ship as acknowledged known-reds in this release (operator
`ship_with_known_red`, memo `f12335e2`):

- `97a33001` — GPU workload rung-0 floor regression: indexed-view ABI gap.
- `f80df1a1` — swift emitter gap coverage: 96 fixtures classified, class
  table pending; post-release backlog.
- `a828a988` — go emitter defects: union-typed error payloads (`requirit`)
  and nil-comparison codegen (`sponte-vel`).
- `8036dd57` — TS lane: codegen internal error on rewritten
  `solum-lege-generic.fab` (definition id 1000000 unresolved).
- `b1f8eeba` — rust e2e lane `instans.fab` cargo build produces no binary.
- `2624fea0` — sermo bare-binary e2e harness host-dispatch gap (3
  solum/tempus fixtures, ad/async golden trio).
- `54a93c8b` — stage-4b new classified failures: forma idempotency x3,
  run-target merge-introduced, coreutils PARSE030, SEM004/SEM006 pinned-norma
  questions, hygiene x3.
- Environmental — `RADIX_WASM_STUB_HOST`: 16 wasm fixtures are
  `environmental_skip` because the run tier requires the retired
  `radix-wasm-stub-host` binary; supply via env when a prebuilt stub-host or
  external runner is available.

### Verification

Every commit hash cited above was verified to resolve in the release base
(`git cat-file -e <hash>` at `80dedd5f6`); every Vivi handle cited
(`9ca6437d`, `fb06c8c5`, `e8822722`, `ec8bf5c6`, `23cb01b0`, `8e00f78b`,
`70728fa9`, `eee9f06d`, `920c6334`, `97a33001`, `f80df1a1`, `a828a988`,
`8036dd57`, `b1f8eeba`, `2624fea0`, `54a93c8b`, `f12335e2`, `b2920cd5`)
resolves via `vivi need show` / `vivi task show` /
`vivi memo show` on the shared board. Scale table regenerated with
`git log 6e0438132..80dedd5f6 --oneline --no-merges | grep -c '<prefix>('`
per row.

### Known limitations

- **Cross-module `textus` handles** remain limited by separate linear
  memories at the package-wasm boundary.
- **Numeric inference accuracy is deferred.** Device execution remains a
  capability statement; no numeric parity band is claimed.
- The Haskell and Python targets are source-emit surfaces — not executable
  package build/run backends.
- The AMD device surface is emit/compile capability — `amd` selection stays
  fail-closed until the ROCm clang path is provisioned.
- Doctests are excluded from the ladders by design; run `cargo test --doc`
  explicitly when doc-example coverage is wanted.

### Deferred

Onboarding Stages 4–8 (doctor, portable no-Rust hello, Norma/Triga
acquisition, locale docs parity), the numeric inference accuracy claim, and
the AMD device-execution path. These are not implied anywhere in this
release.

---

[All releases](/releases/) · [Start](/start/)
