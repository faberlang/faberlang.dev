+++
title = "Radix 0.81.0"
section = "releases"
order = 19
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.81.0 |
| **Tag** | `radix-v0.81.0` |
| **GitHub** | [radix-v0.81.0](https://github.com/faberlang/releases/releases/tag/radix-v0.81.0) |
| **Published** | 2026-08-10 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.81.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.81.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.81.0/radix-v0.81.0-aarch64-apple-darwin.tar.gz) | 5.6 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.81.0/radix-v0.81.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [radix-v0.81.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.81.0/radix-v0.81.0-x86_64-unknown-linux-gnu.tar.gz) | 6.2 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.81.0/radix-v0.81.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.81.0/radix-v0.81.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.81.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

> **Status**: final

Minor release spanning **231 commits** (`v0.80.0..v0.81.0`, 2026-08-07→2026-08-10).
Headline: **Conversion-directed assignment (`↤`) is now codegen-correct on every HIR backend** (Swift, Rust, Go, TypeScript), the **validation ladder was rebuilt** (doctests out, per-crate clippy, module-boundary parity lane, a
302-item pedantic-lint cleanup), and the range lands the **AMDGPU surface**,
the **DDCP device-descriptor emission gates**, and the **forma pretty-v1 policy registry**.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 231 |
| `feat(...)` commits | 30 |
| `fix(...)` commits | 39 |
| `docs(...)` commits | 93 |
| `test(...)` commits | 5 |
| `style(...)` commits | 7 |

Reconstruct the full log:

```bash
git log v0.80.0..HEAD --oneline --no-merges
```

### Major tracks

#### Conversion-directed assignment (`↤`) codegen completeness

The `↤` surface (conversion-directed assignment, added in the v0.79 clean
break) is now emitted correctly on all four HIR backends. Three real codegen
bugs and one import bug were found and fixed by the e2e exempla harness
(`corpus/assignatio/conversio-assign.fab` runs and matches its expected output
on every backend):

- **Swift: destination evaluated once.** An effectful destination index or
  receiver (`xs[idx()] ↤ v`) is bound to a temp so `idx()` runs exactly once
  instead of twice (`9ea3c1242`).
- **Rust: right-associated chains as blocks.** `a ↤ b ↤ "42"` cannot nest
  assignments in Rust (`b = …` evaluates to `()`), so the chain emits as a
  block expression with the inner store as its own statement
  (`f95aa9565`).
- **Go: chains and typed init.** The chain emits sequential statements, and a
  typed initializer (`fixum T x ↤ value`) emits the conversion value rather
  than an invalid `x := x = v` (`d6efb606d`). The import walker now records
  `strconv`/`fmt` for parse-backed `↤` sources with `⇥` recovery
  (`cd629cb1a`).
- **TypeScript: typed init.** `fixum T x ↤ value` emits the conversion result
  directly (`const x: T = Number("7")`), not a self-referential
  `const x: T = x = …` that tsc rejects (TS2448/TS2588). All backends now use
  the precise self-target check so `fixum T x ← (y ↤ v)` with a different
  target falls through to ordinary expression emission (`6a3e5f020`).

#### Validation ladder rebuild

The ladder was restructured so the unit gate stays fast and honest:

- **Doctests disabled across the ladder.** The rustdoc pass is a full
  per-crate compile with near-zero doctest coverage in this repo; it made the
  stage-4 unit gate take 30+ minutes. Stage 4, the module-boundary parity
  lane, the `--ignored` lane, `smoke-ci`, `verify-native-stdlib`, and
  `audit-test-coverage` all run `--lib --bins --tests` (`759d33080`,
  `d9ff7a293`, `493fbd7d7`).
- **nextest → cargo test.** The ladder (and faber's) replace nextest with
  plain `cargo test` throughout (`0a68b457c`; faber-side `2f18074`).
- **Per-crate clippy with `--no-deps`.** Stage 2 lints one crate at a time
  with progress output (`[i/N]`) and without dependency noise
  (`e02743bfe`, `6fdce240a`).
- **Stale-test adjudication.** 18 tests that froze pre-change expectations
  were updated to the current design: 8 LLVM-text emission-route tests
  (`c7ddd0c62`), 3 TS modular-word rejection tests (`22871a22a`), and 7
  hygiene diagnostics that asserted message text instead of stable
  category/code/issue (`d27b38cae`).
- **EBNF coverage matrix regenerated** (281 terms) after the earlier matrix
  drift (`b95799d85`).
- **Formatting drift normalized** — 27 files of agent-generated code brought
  under `cargo fmt` in one commit (`9fdef6869`).

#### Clippy pedantic cleanup (302+ lints)

The per-crate `--no-deps` inventory cleared 302+ clippy pedantic findings
across 9 crates: `radix-mir` (91 + 38 cascade), `radix-mir-fmir` (31 + 2),
`radix-mir-llvm` (23 + 2), `radix-hir-swift` (14), `radix` (11 + 6
integration), `radix-mir-metal` (5), plus shared lib-target debt in
`hir-swift`/`hir-rust`/`mir` and the `many_single_char_names` /
`ref_option` stragglers (`39525a9b3`, `9268b22b9`, `aebd286bb`, `ebff34bb2`,
`85b76d3b5`, `35a60ed46`, `0c8343c28`, `10993b380`, `418d1e6db`,
`0470258cd`). The structural `#[allow(too_many_arguments)]` exceptions for
codegen entry points remain deliberate.

#### Module-boundary parity (new crate + gates)

A new `radix-module-boundary` crate proves file-interface parity:

- **MB-U1:** seed crate + consumer engine + parity runner + seed parity ledger
  (pattern-establishing unit, `f18d450ed`; fixture header fixed, `b446ed73f`;
  lockfile entry, `805695f87`).
- **MB-U2:** full 309-file corpus baseline with a frozen parity ledger
  (`cd0ccf5f1`).
- **MB-U3:** gates wiring — stage-1 `check-module-boundary`, auto-join, and
  the stage-4 parity lane (`0632dba7b`). Orphan lockfile entry dropped
  (`2d05f7cc7`).

#### AMD GPU surface

The first AMDGPU lowering surface lands (additive, feature-gated):

- **AMDGPU target seed** — `amdgpu/{mod,artifact}` emitter module + additive
  `Amdgpu` backend variant (`bdabb6c66`).
- **AMD-A1:** real AMDGPU LLVM IR for elementwise + tree-reduction kernels on
  `gfx942`/CDNA3 with a leaf fixture (`ccea6664e`).
- **AMD-B1:** pinned ROCm clang compiles AMDGPU IR to a loadable `gfx942`
  HSACO (`3386312d2`).
- **AMD-A2/A3:** `mir-amd` façade feature gate with a fail-closed lane
  diagnostic (`12bf651ff`), and the `amd` backend-id spelling with
  selection/admission/requirements tables and honest-rejection tests
  (`b46222393`; compile-fix `939661c96`).
- **Runpod dc-mi300x lane:** AMD-C2 leaf-probe route + frozen lane registry
  entry (`4321d14a2`, `19548c543`), runpodctl adapter swap (`29c514a47`), and
  the GPU-verify sorted-set SSH host-key stability fix (`4904c47be`).

#### DDCP device-descriptor emission gates

The device-descriptor contract hardens with pre-emission gates:

- **DDCP3-U3:** partition/callsite records with explicit effect boundaries
  (`0270a99fa`).
- **DDCP3-U4:** typed-artifact completeness gate, HotPathGate end-state, and
  `execution_descriptor_hash` domain separation (`c649cd215`).
- **DDCP3-U5:** unsupported host/device call shapes reject before emission
  (gate 6), with the Closure-callee admit proven to lower to the
  prepared-region direct call (`b51b182b8`, `bbe976d6f`).
- **DDCP4 leaf conformance:** Metal and LLVM leaves complete typed artifact
  metadata + FNV rename (`31ddc542e`, `231d99851`), shared conformance fixture
  with reflection-carrier content (`437b9fe6f`).
- **Contracts recorded:** prepared-region invocation cardinality (PIC-U1/U2,
  `ae878f72f`, `3d15b9e29`), execution-descriptor authority (DIC-U1,
  `2489a8875`), and lossless-locale-transcode contract (LTC-U1, `d63c0f34e`).

#### forma FORMAT-PRETTY policies

The format policy registry lands: FORMAT-PRETTY S1 promotes `normalise-v1`
with policy selection (`f3a3639f8`), and S3 completes the `pretty-v1`
registry with engine fixes (`becee4908`).

#### Numeric validators and runtime intrinsics

- `fractus potentia` lowers as the exponentiation identity (`e9e77d62a`);
  rounding (`d0c9708fa`) and absolutum/signum (`2df1af436`) validators accept
  `SizedNumeric(Fractus, _)` receivers.
- `textus.accipe` intrinsic + SizedNumeric zero-init arm (`43c0102ba`);
  zero-init arm for no-initializer nominal struct/union locals
  (`0057ec92e`).
- In-house UUID v4 generator in the stepper; the `uuid` crate dependency is
  dropped (`06dc3a384`, `fbed3cdf4`).

### Breaking / author-visible

| Change | Migration |
| --- | --- |
| `mir-amd` façade feature gate (AMD-A2) | Additive; default `full-targets` builds unchanged. |
| `Amdgpu` backend variant + `amd` backend-id (AMD-A3) | Additive; `amd` selection is fail-closed until the ROCm clang path is provisioned. |
| DDCP3-U3..U5 emission gates | Internal contract hardening; previously accepted unsupported call shapes now reject before emission with the stable call-shape issue. |
| Doctests removed from the ladder | Tooling only; run `cargo test --doc` explicitly when doc-example coverage is wanted. |

No author-visible breaking removals in this range: the `uuid` crate drop and
the nextest retirement are internal tooling changes.

### What is NOT included

- No new language surface beyond completing the `↤` codegen (the operator
  shipped in v0.79; this release makes it correct on every backend).
- No numeric inference accuracy claims; no GPU performance claims.
- The faber product CLI surface (format flags, device arms) is covered in the
  sibling faber release notes.
- The AMDGPU surface is emit/compile-surface capability, not a device-execution
  claim: `amd` selection remains fail-closed without the B1 ROCm path.

### Version alignment

| Item | Value |
| --- | --- |
| Source tag | `v0.81.0` |
| `crates/radix` version | `0.81.0` |
| Public artifact tag | `radix-v0.81.0` on `faberlang/releases` |
| Workspace members bumped | all `0.80.0` → `0.81.0` (hygiene-ratchet stays `0.1.0`) |

### Verification contract

The release commit is gated by `cargo build --locked --release -p radix --bin
radix` and the full ladder. The ladder no longer runs nextest or doctests:
stage 4 is `cargo test --workspace --lib --bins --tests` plus the
module-boundary parity lane, and the tag workflow runs the full Radix ladder
(`./scripta/test --full`) before publishing component artifacts. The e2e
harnesses (rust, canonical, go, ts, wasm, llvm, roundtrip, mir) pass at the
release tip, including the `conversio-assign` exemplar on every backend.

### Publish

1. Bump all workspace crate versions `0.80.0` → `0.81.0` (not hygiene-ratchet);
   use `scripta/bump-version` + `scripta/regen-lock` per the thin runbook.
2. `cargo update` so `Cargo.lock` matches manifests.
3. Verify locked release build + the full ladder (stages 1–6 + `--e2e`).
4. **Single commit** with version bump + lockfile:
   `release(radix): v0.81.0`
5. Annotated tag: `git tag -a v0.81.0 -m "Radix v0.81.0"`
6. Push: `git push origin main && git push origin v0.81.0`
7. Monitor: `gh run list -R faberlang/radix --limit 5`
8. Confirm `faberlang/releases` publishes `radix-v0.81.0` multi-arch archives.

**Never** tag a commit whose `Cargo.lock` is stale relative to the bumped
manifests — CI uses `cargo build --locked`.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
