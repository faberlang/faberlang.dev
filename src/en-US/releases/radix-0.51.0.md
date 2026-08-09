+++
title = "Radix 0.51.0"
section = "releases"
order = 46
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.51.0 |
| **Tag** | `radix-v0.51.0` |
| **GitHub** | [radix-v0.51.0](https://github.com/faberlang/releases/releases/tag/radix-v0.51.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.51.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.51.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.51.0/radix-v0.51.0-aarch64-apple-darwin.tar.gz) | 1.8 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.51.0/radix-v0.51.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.51.0/radix-v0.51.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.51.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Focused release on **deferred correctness**: the compiler gains three semantic
features — return-path exhaustiveness, explicit `discerne omnia` matching, and
a nullable catchall warning — while the Faber runtime namespace lands as a
factory goal, splitting the workspace into `faber` (runtime), `faber-cli` (build
tool), and retargeting codegen to `faber::Valor`.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 27 |
| `feat(...)` commits | 3 |
| `fix(...)` commits | 3 |
| `docs(...)` commits | 5 |
| `chore` commits | 3 |
| Date span | 2026-06-26 → 2026-06-27 |

### Major tracks

#### Return-path exhaustiveness (DEFER-011)

- Enforce that value-returning functions (`→ T` where T is neither vacuum nor
  nihil) cannot fall through without a return. The new `return_path` semantic
  pass runs after typecheck and exhaustiveness, reducing each construct to
  Terminates/FallsThrough — `redde` satisfies the normal channel; `iace`/`mori`
  and diverging loops diverge; `si` needs both branches; `discerne` terminates
  when coverage is total and every reachable arm returns. Generators and
  `→ nihil` effect functions are excluded. Reuses diagnostic `SEM033`
  (MissingReturn). (`17a8bedd0`)

#### `discerne omnia` explicit exhaustive matching (DEFER-028)

- Lower the previously parse-only `omnia` keyword through HIR into the
  exhaustiveness pass. When present, the match must be over a single enum
  scrutinee and every arm must name a variant explicitly — no `casu _`, no bare
  binding, no `ceterum`. Plain `discerne` is unchanged (coverage enforced,
  catchalls allowed). New diagnostics: `SEM043` (OmniaRequiresEnum) and `SEM044`
  (OmniaForbidsCatchall). Composes with return-path exhaustiveness: a returning
  `discerne omnia` is proven covered iff every variant is named and each arm
  returns. (`413c1cb93`)

#### Warning when catchall absorbs null of nullable scrutinee (DEFER-013)

- Emit `WARN011` (WildcardAbsorbsNull) when an unguarded catchall absorbs a
  scrutinee whose constituents include `nihil` — `Option(_)`, any Union
  containing nihil, resolved through aliases, references, and applied generic
  arguments. Suppressed when an explicit `casu nihil` arm is present. This is
  a warning, not an error. (`e737f3a99`)

#### Faber runtime namespace (FRN-000–006)

Split the workspace into `faber` (language runtime) and `faber-cli` (build
tool), retargeting norma HAL and radix Rust codegen to `faber::Valor`.

- **Workspace split:** `crates/faber` becomes the runtime crate (ascii, frame,
  regex, valor types); `crates/faber-cli` carries the CLI/tool logic (explain,
  init, run, test, package, reference). Frame-type extraction moved to FRN-002;
  codegen retarget to FRN-004. Inline Faber* prelude types and
  `norma::datum::Valor` deleted. (`a0e34b32c`)
- **Valor alias:** Emit `use faber::Valor as valor` in standalone Rust output,
  rewriting type-annotation sites without touching variant paths like
  `faber::Valor::Nihil`. (`23da5a09a`)
- **Emit-time policy:** Replace post-pass string rewrite with
  `valor_rust_ident()` threading through type emission, JSON literals, and
  `None::<T>` sites. Variant constructors still emit `faber::Valor::` paths.
  (`eebde7631`)
- **Prelude collision:** Stop emitting bare `use faber::Valor` imports that
  conflict with user `pub type Valor = faber::Valor` aliases (E0255); add faber
  runtime dep header to standalone emit. (`bb4e980c6`)
- **Single FaberValue wrap:** Remove double-wrap for norma runtime method
  results (`FaberValue::from(FaberValue::from(...))`). (`5cf03ef7d`)
- **Verification:** FRN checkpoint scripts (`verify-frn.sh`, `check-frn-markers`)
  with e2e dependency policy (always faber, conditional norma/tokio).
  (`c4548ae99`)
- **Planning docs:** Impact analysis, goal, ledger, plan — two review passes
  with corrections for lib rename, frame extraction ordering, dependency policy,
  and intermediate-state contracts. (`291898c19`, `d9fe2b309`)

### Other changes

- **Breakable-blocks Wasm e2e (DEFER-022):** Register six breakable-blocks
  exempla in the Wasm e2e suite at their real pipeline ceilings; rename
  exempla directory from `breakable-blocks/` to keyword-keyed `rumpe/` and
  `ad/`. (`108272225`)
- **Factory delivery specs:** Add specs for abstract tabular types (exemplar,
  columna, series, census — `cb3418857`), clavis secret key type
  (`e2a8b5a3f`), and tensor/sized numeric types (`4019c0eb5`).
- **Census-types documentation:** Corpus as opaque bag without column encoding
  (`ca3938179`); add corpus population type and subset exemplars
  (`700d7f7bf`).
- **Explain registry:** Teach the `faber` explain/reference registry the
  `conversio` kind and alias so conversion exemplar cross-references resolve.
  (`eba4089bd`)
- **Workspace hygiene ratchet:** Extend the shared `hygiene-ratchet` scanner
  to all workspace crates (faber, norma, scena, cista, macos-arm64 host).
  (`42fb25914`); format the helpers (`ad8ab255b`).
- **Clippy/hygiene gate:** Restore `-D warnings` across 8 production sites;
  box the `Ad` variant outlier in `HirStatementKind` and `StmtKind`; introduce
  `AdWrapperArms` struct and `FieldTypeFn` alias; consolidate path-def guard
  assertions; remove ten `let _ =` smells. (`fef0dfb1f`)
- **Rustfmt:** Apply `cargo fmt --all` across the workspace (48 files).
  (`cf644a7aa`)
- **Factory goals:** Add `faber-format` and `faber-polish` factory goal docs;
  route rustc metadata to scratch/out-dir; ignore `*.rmeta` artifacts.
  (`4c7c0f6ba`)
- **Radix fn naming:** Open naming ledger and plan (RFN-000–008) for
  verb-first consistency audit. (`dd8be5c18`)
- **Chores:** Housekeeping for non-radix faber and host crates (`9910dd3bd`);
  regenerate stale exempla index (210→216 files, `d6074ebf4`); remove
  accidental `salve-munde.rs` build artifact (`71a2eda60`).

---

[All releases](/releases/) · [Install the current release](/start/install.html)
