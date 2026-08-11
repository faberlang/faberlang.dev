+++
title = "Faber 1.6.0"
section = "releases"
order = 10
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.6.0 |
| **Tag** | `faber-v1.6.0` |
| **GitHub** | [faber-v1.6.0](https://github.com/faberlang/releases/releases/tag/faber-v1.6.0) |
| **Published** | 2026-08-10 |
| **License** | MIT |

## Install this version {#install}

Pinned download for **Faber 1.6.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.6.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.6.0/faber-v1.6.0-aarch64-apple-darwin.tar.gz) | 10.5 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.6.0/faber-v1.6.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.6.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.6.0/faber-v1.6.0-x86_64-unknown-linux-gnu.tar.gz) | 11.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.6.0/faber-v1.6.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.6.0/faber-v1.6.0-aarch64-apple-darwin.tar.gz
tar -xzf faber.tgz
sudo mv faber-v1.6.0-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

## Release notes {#notes}

> **Status**: final

Minor product release spanning **103 commits** since `v1.5.1`
(2026-08-08→2026-08-10). Headline: **the first stable release on the rewritten packaging/CI pipeline** — the 1.5.1 dev-kit tooling (consumer
smoke-test gate, CI packaging rewrite) is rolled into main, and the release
pins the tested **radix 0.81.0** companion. Also lands the module-boundary
exempla parity profile, the `format` CLI steady-state flag surface
(FORMAT-PRETTY S4), and the AMD device consume arms.

The v1.6.0-rc.1 candidate is superseded by this release: the rc was a
no-tag, no-push archive-gate lock (package/run proven at RC level on burgus
Metal and pharos CUDA). This release takes the stable publication path on the
same pinned tree plus the new release gate.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 103 |
| `feat(...)` commits | 11 |
| `fix(...)` commits | 11 |
| `docs(...)` commits | 26 |
| `test(...)` commits | 10 |

```bash
git log v1.5.1..HEAD --oneline --no-merges
```

### Major tracks

#### 1.5.1 dev-kit roll-in (release pipeline rewrite)

The 1.5.1 patch-train tooling landed on main before this release; 1.6.0 is the
first release built on it:

- **CI packaging rewrite** with the dev-kit assembly layout (`2cac54b`).
- **Consumer smoke-test gate** — a scripted consumer path that installs the
  release archive and runs a real compile (`13116d9`), wired into CI with
  process docs and readback (`9148331`), including the hyphenated pin-output
  key normalization so the gate's expressions stay safe (`5fe2405`).

#### Validation ladder

- **nextest → cargo test** across the faber config, scripts, and docs
  (`2f18074`), matching the radix ladder change; the exempla e2e harnesses are
  the stage-4+ surface.
- Exempla scena-debt ledger refreshed: the resolved `est/est.fab` row is
  dropped from the MIR target matrix (`5e5543a`).

#### Module-boundary exempla parity (MB-U4)

The exempla suite gains the import-boundary emit-lane parity profile — the
rust lane first — so file-interface contracts are proven against the corpus
(`eb555a3`), riding the radix `radix-module-boundary` crate from the same
range.

#### FORMAT-PRETTY S4 — format CLI flag surface

The `format` CLI gains its steady-state flag surface (`1b8f1f6`): the
rule-slug policy selection and the explicit `--stdout` / `--write` /
`--stdin` / `--check` spellings that scripts and editors rely on, matching
the radix forma pretty-v1/normalise-v1 registry.

#### AMD device consume arms

The faber side of the radix AMD surface:

- `Target::MirAmd` arms where faber matches targets exhaustively (`8d37f6a`,
  `245ddc8`), the `route_selection` `Amd` fail-closed arm (`5eb6c51`), and
  `FmirDeviceBackend::Amd` fixture arms for the device lane (`917c5ff`).
- The device route receipt print consumes the re-domained program-graph hash
  (DIC-U2, `7e014c3`).

#### package/mir correctness

- **Shadowed-alias rewrite** recovers synthetic HIR receiver names
  (`06a5313`); the rewriter is hoisted to module scope with a borrow-order
  fix (`acb5dda`) and regression tests for the forma-shadowing guard
  (`33320ed`).
- PML4 executed-lane acceptance re-enabled now that LIB-MIR landed
  (`04ba15f`); guard-condition tests moved to the lane test file (`3784a44`).

### Pin pair

The release-manifest pins the tested companion revisions at the tag:
faber `1.6.0` against **radix 0.81.0** (tag commit), cista `0.1.0`,
faber-runtime and hosts per `release-manifest.yaml`. The `--locked` release
build from these pins is the proof; `publication.releaseTag` is
`faber-v1.6.0`.

### Known limitations

- **Cross-module `textus` handles** remain limited by separate linear
  memories at the package-wasm boundary.
- **Numeric inference accuracy is deferred.** Device execution remains a
  capability statement (`faber run --backend metal|cuda`, package/run proven
  at RC level on burgus and pharos); no numeric parity band is claimed.
- The AMD device surface is emit/compile capability — `amd` selection stays
  fail-closed until the ROCm clang path is provisioned.
- Doctests are excluded from the ladders by design (radix and faber); run
  `cargo test --doc` explicitly when doc-example coverage is wanted.

### Deferred

Onboarding Stages 4–8 (doctor, portable no-Rust hello, Norma/Triga
acquisition, locale docs parity), the numeric inference accuracy claim, and
the AMD device-execution path. These are not implied anywhere in this
release.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
