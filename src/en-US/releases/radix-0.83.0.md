+++
title = "Radix 0.83.0"
section = "releases"
order = 25
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.83.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

> **Status**: final

Minor component release. Range: `v0.82.0` (`6ed8cec6e`) → pin
`1eaf4ec68` (2026-08-15→2026-08-18). Headline: **`radix-package` takes the compiler package surface**, **packed quantized kernel plans** emit on
Metal/NVVM, **shape-generics Phase 3+4 closes**.

**Notes provenance:** no pre-written `v0.83.0` document was attached to
release handle `5dbc3c01`. Factual reconstruction from
`git log v0.82.0..1eaf4ec68`.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 324 |
| `feat(...)` commits | 39 |
| `fix(...)` commits | 137 |
| `docs(...)` commits | 61 |
| `test(...)` commits | 50 |

Reconstruct the full log:

```bash
git log v0.82.0..1eaf4ec68 --oneline --no-merges
```

### Major tracks

#### radix-package (RP1–RP5)

New crate owns package identities, manifest/lock view, discovery, import
graph, multi-unit analysis, artifact planning, and the package
MIR/FHIR/FMIR compiler subset previously in faber.

#### Packed quantized kernels

EXEC-02 packed kernel plan/op ABI frozen; FMIR wire-mirror; Metal + NVVM
QuantizedMatMul for Q8_0, Q4_K, Q5_K, Q5_0, Q6_K, BF16, F16;
QuantizedGather; F16 admission; WGSL F16 elementwise IO.

#### Shape-generics Phase 3+4

Unroll pass (3E), guard-as-mask (3F), SG-4B corpus + hir-rust `⇥`
recovery, SG-4C archive to `docs/archived/shape-generics/`. Pin-window
hand-65: rustfmt five stage-1 files, compat JSON regen, module-boundary
SG-4B MIR recovery classified as a capability-gap.

### Binary question (operator)

**2026-08-25 update:** the Radix binary release workflow has been removed.
Faber is the only active binary release surface; historical Radix CLI archives
can be backfilled manually if needed.

**Radix is source+tag / library. No product radix binary exists.**

Evidence (live tree at pin `1eaf4ec68`):

1. `crates/radix/Cargo.toml` has no `[[bin]]`. `crates/radix/README.md`:
   "This package has no `[[bin]]`, no clap, and no process exit. The
   developer binary `radix` and `tool` stay in `radix-module` until
   RTR4."
2. `cargo build --locked --release -p radix --bin radix` fails:
   `error: no bin target named radix in radix package` (help points at
   `radix-module`).
3. `radix/AGENTS.md` still names `-p radix --bin radix` as the release
   verify step — stale vs the crate.
4. Live `.github/workflows/release.yml` still builds
   `-p radix --bin radix` on tag `radix/vX.Y.Z`. That workflow would
   fail on this tree. Historical tags `v0.81.0` / `v0.82.0` do not
   match the `radix/v*` trigger.
5. Live `ci.yml` is main-only `cargo build --locked -p faber`. The
   AGENTS.md claim that a `v*.*.*` tag runs `./scripta/test --full` is
   stale.

Operator said a minor bump without a binary is entirely possible. This
release **does that**: bump 0.82.0 → 0.83.0, lock, source tags, no
radix archive. Local tags `v0.83.0` and `radix/v0.83.0` are created and
**not pushed**. Do not push `radix/v0.83.0` until `release.yml` is
repointed at `radix-module` (or the façade grows a bin again). The
shipped CLI is Faber `1.8.0`.

### Version alignment

| Item | Value |
| --- | --- |
| Source tags (local, unpushed) | `v0.83.0`, `radix/v0.83.0` |
| `crates/radix` version | `0.83.0` |
| Public artifact tag | `radix-v0.83.0` only after operator push |
| Workspace members bumped | all `0.82.0` → `0.83.0` (34 crates) |
| Not bumped | `crates/faber` (1.8.0 product), `faber-hir-rust` 1.4.0, `radix-program` / `exempla` / `proba` / `handroll` / `faber-prefill-oracle` / `hygiene-ratchet` 0.1.0 |

`./scripta/bump-version` is not used: it would smash the product and
0.1.0 tracks onto one version. Bump is scoped to crates that were at
`0.82.0`.

### Known-issues

Carried from v0.82.0 / memo `f12335e2` (not re-derived). Same list as
`docs/release/faber/v1.8.0.md`. Tag-path `--full` is recorded as
known-red or unrun in the closeout receipt.

### Verification contract

Pin `1eaf4ec68`: stages 1–2 green, `cargo test -p radix-module-boundary`
green. Locked release build of `radix` + `faber` bins is the local
integrity gate. Faber product canary (install from archive + check/run)
is the operator-defined payload proof.

### Publish (operator only — this lane does not push)

1. Fast-forward main to the release commit (or merge `factory/release`).
2. `git push origin main`
3. `git push origin v0.83.0`
4. `git push origin radix/v0.83.0`  # fires release.yml binary publish
5. `git push origin faber/v1.8.0`   # fires release-faber.yml

**Never** tag a commit whose `Cargo.lock` is stale relative to the
bumped manifests.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
