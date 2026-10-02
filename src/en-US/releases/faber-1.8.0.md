+++
title = "Faber 1.8.0"
section = "releases"
order = 13
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.8.0 |
| **Tag** | `faber-v1.8.0` |
| **GitHub** | [faber-v1.8.0](https://github.com/faberlang/releases/releases/tag/faber-v1.8.0) |
| **Published** | 2026-08-24 |
| **License** | MIT |

## Install this version {#install}

Pinned download for **Faber 1.8.0**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.8.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-aarch64-apple-darwin.tar.gz) | 8.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.8.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-x86_64-unknown-linux-gnu.tar.gz) | 9.8 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-aarch64-apple-darwin.tar.gz
tar -xzf faber.tgz
# The archive ships bin/ and share/; keep them together so the
# reader packs resolve beside the binary.
sudo mv bin/faber /usr/local/bin/faber
sudo mv share/faber /usr/local/share/faber
faber --version
```

## Release notes {#notes}

> **Status**: final

Minor product release on the odd-major 1.x development line (`policy.md`).
Range: `faber/v1.7.0` (`5d7d42bf8`) → pin `1eaf4ec68` (2026-08-15→2026-08-18).
Headline: the **compiler package surface moves into `radix-package`** (RP1–RP5),
**packed quantized kernel plans** land on Metal/NVVM (Q8_0 / Q4_K / Q5_K /
Q5_0 / Q6_K / BF16 / F16 + QuantizedGather), **shape-generics Phase 3+4 closes** (unroll pass, guard-as-mask, SG-4B corpus, SG-4C archive), and the
release pins the tested **radix 0.83.0** companion.

**Notes provenance:** the release-lane charter says notes arrive pre-written.
No `v1.8.0` / `v0.83.0` document was attached to handle `5dbc3c01`. These
notes are a factual reconstruction from `git log faber/v1.7.0..1eaf4ec68`
plus the carried 1.7.0 known-issues list. Disclose, do not invent.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 315 |
| `feat(...)` commits | 39 |
| `fix(...)` commits | 134 |
| `docs(...)` commits | 61 |
| `test(...)` commits | 50 |
| `style(...)` commits | 17 |
| `chore(...)` commits | 6 |

Reconstruct the full log:

```bash
git log faber/v1.7.0..1eaf4ec68 --oneline --no-merges
```

### Major tracks

#### radix-package (compiler package surface)

Package compilation moves out of the faber product crate into
`radix-package`: identities + API envelope (RP1), compiler manifest/lock
view (RP2a), discovery + source loading (RP2b), import graph + library
resolution + file interface (RP2c), multi-unit analysis (RP3), artifact
planning + HIR emission (RP4), package MIR/FHIR/FMIR subset (RP5).

#### Packed quantized kernels (EXEC-02 / R-PACK)

Frozen packed kernel plan/op ABI, FMIR wire-mirror, then Metal + NVVM
emit for QuantizedMatMul (Q8_0, Q4_K, Q5_K, Q5_0, Q6_K, BF16, F16) and
QuantizedGather. F16 admission + WGSL F16 elementwise IO.

#### Shape-generics closeout

Named unroll pass for concrete-N `itera` (3E), guard-as-mask
differentiable subset (3F), SG-4B conversion-boundary + generic SDPA
corpus, hir-rust `⇥` recovery, SG-4C goal closeout + archive at
`docs/archived/shape-generics/`.

#### Product / tooling

`faber check` fails when the emit def table misses a resolved def.
Locale register for triga geometry layout helper. Library façade replaces
the excluded stub. Canary smoke-test now proves codegen + `faber run`
(not just packs) and the first-time-user journey.

#### Pin-window residuals (hand-65)

Landed on the pin: rustfmt of five stage-1 compiler files, HIR compat
measurement JSON regen, module-boundary SG-4B MIR recovery classified as
a capability-gap, shape-generics archive.

### Pin pair

`release-manifest.yaml` pins this candidate against **radix 0.83.0**
(source `1eaf4ec68`), hosts `0783406e2a93`, cista `0.1.0` (no cista
protocol call in this dispatch). `publication.releaseTag` is
`faber-v1.8.0`. The `--locked` release build from these pins is the
proof.

### Radix companion (binary question)

**2026-08-25 update:** the Radix binary release workflow has been removed.
Faber is the only active binary release surface; historical Radix CLI archives
can be backfilled manually if needed.

**Live tree: radix is source+tag / library. There is no product radix binary.** `crates/radix` has no `[[bin]]` (README: library façade;
developer `radix` bin stays in `radix-module` until RTR4).
`cargo build -p radix --bin radix` fails: "no bin target named `radix`
in `radix` package".

`radix/AGENTS.md` still says verify with `-p radix --bin radix` — that
step is stale. Live `release.yml` would also fail on the same
`-p radix --bin radix` invocation. The remaining `radix` CLI is
`radix-module`'s developer binary, not a published component artifact.

This release therefore **minor-bumps radix without a radix archive**.
Local tags `v0.83.0` (AGENTS.md) and `radix/v0.83.0` (workflow name)
are created and **not pushed**. Pushing `radix/v0.83.0` would fire a
workflow that cannot build the named bin until that workflow is
repointed. The shipped CLI is `faber 1.8.0`.

### Known-issues (carried from 1.7.0; not re-derived)

Operator `ship_with_known_red` (memo `f12335e2`) still applies. Carried
verbatim:

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

`--full` is recorded as a known-red-or-unrun receipt in the release
closeout mail if the local tag-path suite is not completed before tag.

### Verification

Pin `1eaf4ec68` ran `./scripta/test --stage 1-2` (ok; clippy 0 errors)
and `cargo test -p radix-module-boundary` (38 passed, 0 failed) before
assembly. Post-build canary: assemble-dev-kit → package-archive →
`install-faber` from the archive → installed `faber --version` + locale
packs + `faber check` / `faber run` on the hello-world canary.

### Known limitations

Same as 1.7.0: cross-module `textus` handles, no numeric-inference
accuracy claim, Haskell/Python are source-emit surfaces, AMD stays
fail-closed until ROCm clang is provisioned.

### Deferred

Onboarding Stages 4–8, numeric inference accuracy, AMD device-execution.
Cista stays `0.1.0` (no protocol call).

---

[All releases](/releases/) · [Start](/start/)
