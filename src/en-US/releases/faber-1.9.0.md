+++
title = "Faber 1.9.0"
section = "releases"
order = 12
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.9.0 |
| **License** | MIT |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

> **Status**: final

Minor product release on the odd-major 1.x development line (`policy.md`),
cut from the `release/1.9.0` branch under the release-branch model (operator
amendment 2026-08-25: freeze commit → soak → ladder on branch tips → tag).
Range: `faber/v1.8.0` (`1277976c7`, 2026-08-18) → branch tip `e3af59886`
(+ release commit; 2026-08-18→2026-08-26). Headline: **MIR completeness lands** (the release hold condition), the **stage-4b recipe repair** ends the
canary blind spot, and the window carries the **kernel/reduction wave**,
**tensor glyphs**, **container-bounds law**, and the **equality ladder**.
The release pins the tested **radix 0.84.0** companion (no radix archive,
per the 2026-08-25 recomposition).

### Provenance

Routine disclosure. Anchor: `faber/v1.8.0` (last final tag of the faber
family). Window: `git log faber/v1.8.0..e3af59886` (2016 no-merge commits,
2026-08-18→2026-08-26). Sources consulted: the window git log, factory goal
docs (`docs/factory/`, `docs/archived/`), the release-prep plan
(`v1.9.0-plan.md`, need `332513a9`), the stage-4b classification record
(`1.9.0-stage4b-classification.md`), the operator SHIP decision (memo
`b70088fa`, 2026-08-26 21:2xZ), and the release-lane execution receipts in
this document. The `release-notes` skill template governs section shape.
Not consulted: full Vivi dumps (handles cited inline where they were part of
the release record); per-goal delivery audits beyond the status lines.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 2016 |
| Merge commits | 314 |
| `feat(...)` commits | 296 |
| `fix(...)` commits | 272 |
| `docs(...)` commits | 784 |
| `test(...)` commits | 206 |
| `style(...)` commits | 56 |
| `chore(...)` commits | 61 |
| `refactor(...)` commits | 37 |
| `perf(...)` commits | 2 |

Reconstruct the full log:

```bash
git log faber/v1.8.0..e3af59886 --oneline --no-merges
```

### Release-branch record

- **Freeze commit:** `9c8bd6a99` (operator-declared 2026-08-25).
- **Branch:** `release/1.9.0`; stabilization commits on the branch:
  `a1ec273f1` (e2e coverage-ledger regen), `2d1fa5319` (metal
  FunctionScope param-struct clippy fix), `ee376deee` (rustfmt drift),
  `e3af59886` (stage-4b recipe cherry-pick of main `6c5b42528`).
- **Soak:** 24h target from freeze declaration; canary-refire waves closed
  the known-red picture to 7 genuine reds + 9 env-gated skips at main
  (handle `65351193`, classification doc "Post-wave delta").
- **Operator decision:** SHIP with the 7-row known-red table acked
  (memo `b70088fa`, verdict verbatim "SHIP IT", 2026-08-26 21:2xZ).

### Major tracks

#### MIR completeness (the release hold)

The 1.9.0 plan existed because of this goal; it landed at `9518b21c5`
(closeout audit `3788f300` — residual, no blocker), satisfying the "hold
until MIR implementation is in place" condition from release instruction
need `332513a9`. The systems lane (MIR → FMIR runtime/emit/staging/
validation, tensors/kernels/low-level targets) reached its completeness
gate inside this window.

#### Stage-4b recipe repair (test-harness integrity)

Stage 4b previously ran one workspace-wide fail-fast `cargo test`, which
aborted at the first failing crate and hid later crates from the
canary/gate verdict — a blind spot that hid 67 failures across prior
"green" runs. The fix — a per-crate `--no-fail-fast` loop with an
env-gated skip taxonomy — landed on main as `6c5b42528` and was
cherry-picked to this branch as `e3af59886` (the branch tip). The full
classification record (67 hidden failures → 7 genuine reds + 9 env-gated
skips after the canary-closure waves) is
[`1.9.0-stage4b-classification.md`](1.9.0-stage4b-classification.md).

#### Kernel / reduction wave

Kernel-lane K1/K2 and reduction verbs M1–M4a+R2 (window content per need
`332513a9`); the `faber-kernel-*` goal family (host, json, namespace,
processus, glob-import, aleator) moved through the window with 242
MIR-touching commits, 35 kernel-named and 20 reduction-named.

#### Tensor glyphs (tensor-glyphs-3)

U1 (operator form `⊙` + exemplar pins), U2 (homoglyph diagnostics:
`∘→⊙`, `‖/∥→.rms_norm(...)` did-you-mean), U3 (`ᵀ` transpose sugar,
rank-1 permanent decline + rank-3+ deferred), U4 (`⊘` identical-shape
law), U6 (u32→position-independent idiom migration). EBNF, tree-sitter,
and skills rode each unit.

#### Container-bounds law

B1 literal-bounds check (`0598206dd`) and B2 hard-error at lowering +
runtime (`e46e598c0`); B3 folding follow-up deferred, B4 skill-leg open
(goal status: active — the deferred/open units are not release gates).

#### Equality ladder

Goal archived this window (`docs/archived/equality-ladder/`): A+B+C+E
landed with closeout; the ≅/≈ promotion-exact vs fuzzy tiers and the
pairs ≡≢ ≅≇ ≈≉ re-spelling (need record in the 1.8.0→1.9.0 window).

#### Other window content (per release instruction `332513a9`)

Error-conversion E1–E5, infinity literals IL-1..5, the collection
program, silu admission, the int-power fix, and pack parity. The
`collection-ergonomics` goal itself remained pre-implementation at freeze
(status: planned) — the collection window content rode other goals.

### Pin pair

`release-manifest.yaml` (regenerated by `scripta/assemble-dev-kit`,
prepared 2026-08-26) pins this candidate against **radix 0.84.0**
(source `e3af59886a8ce9ecf5ded89cab24f7efbdca3a75` — faber and radix
share the pin per the sweep-14 E2 rule), **hosts `c1f9fd1e17ca`**
(`c1f9fd1e17ca6da0389538bc9a0dee101f68c150`), launcher digest
`sha256:6d1d89ff07bcbe5c717556a551d318db97657a46cc3da7879ea38dda64cd772f`,
reference-pack digest
`sha256:0037686316a5ee23b20c36c98b804dd9219a09d1c19b925b8e6d29090716709e`.
`releaseIntent.version` is `1.9.0`, channel candidate, line `1.x`.
The `--locked` release build from these pins is the proof.

### Radix companion

Radix minor-bumps to **0.84.0** with this release (39 workspace crates;
`faber-hir-rust` stays 1.4.0, support crates stay 0.1.0). No radix binary
archive: the Radix binary release workflow is retired (2026-08-25
recomposition); Faber is the only active binary release surface. The
companion tag `v0.84.0` is created locally and **not pushed** (1.8.0
precedent). Companion notes: [`../v0.84.0.md`](../v0.84.0.md).

### Known-issues (operator-acked, verbatim)

Operator decision 2026-08-26 21:2xZ (memo `b70088fa`): verdict verbatim
**"SHIP IT"**; known-red releases are legal with operator ack
(`radix/AGENTS.md`). The acked list — the 7-row table in the 21:21Z
package — recorded verbatim from the decision memo:

> Acked list = the 7-row table in the 21:21Z package: classification-table
> 7, CTR-08 transitional (self-deleting), PML4 FMIR (gradus-owned,
> self-deleting), PTX IR (diagnosis queued), corpus-count 365->368 re-pin
> (owner filed), runner/async-tempus rows, bijection transpone gap.

Row 1 ("classification-table 7") is the seven genuine unit-test reds,
recorded verbatim from
[`1.9.0-stage4b-classification.md`](1.9.0-stage4b-classification.md)
("Remaining genuine reds (7)", post-wave delta at pin `18519ccd3`):

| # | Crate | Test | Class |
| --- | --- | --- | --- |
| 1 | faber | `faber_build_writes_static_assets_and_manifest_for_browser_product` | web2_build (tela-validate.ts TS2345) |
| 2 | mir-emit-harness | `conversio_tests::valor_lista_to_lista_numerus_preserves_dynamic_strictness_per_element` | bounded-literal conversio/copiae class |
| 3 | mir-emit-harness | `runner_tests::runner_runs_lista_methodi_copiae_fixture` | same class as #2 |
| 4 | radix-module | `empty_array_and_spread_literals_no_longer_report_annotation_or_type_errors` | array_spread mechanical (cluster 3) |
| 5 | radix-module | `lowers_nested_collection_higher_order_synthetic_closures` | collection-transform mechanical (cluster 3) |
| 6 | radix-module | `discerne_alias_and_multi_subject_roundtrip_through_faber_codegen` | discerne SEM004 |
| 7 | radix-module | `bijection_ratchet_equals_probe_derived_gap_set` | bijection ratchet gap (cluster 8) |

Env-gated skips (9, not red): the 5 `gea*_pipeline_exports_*` /
`gea3_pipeline_plan_admission` artifact-dir gates (mir-emit-harness) plus
the 4 faber-prefill-oracle GEA_SOURCE / GEA2_F32_GGUF gates.

Branch-base note (disclosed, not re-derived): the canary-closure regens
(pin `18519ccd3` era) landed on main after the freeze and are not on the
`release/1.9.0` branch; the branch therefore measures the pre-closure
known-red picture (13 genuine reds per the classification record) unless
a wave landed on-branch. The operator ack covers the 7-row table above;
the branch-measured delta is recorded in the Verification section as
receipt lines, not investigated here (release-lane charter: dispatch is
the decision).

### Verification

Release-lane receipts (candidate = `release/1.9.0` tip `e3af59886` +
version-bump/manifest/notes release commit, packet
`worktrees/release-190`):

- **Version bump:** `crates/faber` 1.8.0→1.9.0; 39 radix-line crates
  0.83.0→0.84.0; `cargo update` lockfile refresh (61/61 lines).
- **Cheap gates:** `cargo build --locked --release -p faber --bin faber` —
  green, `target/release/faber --version` → `faber 1.9.0`.
  `scripta/validate-release-manifest release-manifest.yaml` — ok.
  `scripta/faber-regen-lock --pinned-siblings --check` — ok
  (hosts=`c1f9fd1e17ca`, Cargo.lock fresh).
- **Release boundary ladder** (`./scripta/test --release`, packet
  `worktrees/release-190`, run log receipts retained by the release seat):
  - stage 1 gate + fmt: **green**; stage 2 clippy `-D warnings`:
    **0 errors** (inventory `target/stage-2-clippy.jsonl`).
  - stage 3 proba canary: **1 package ok** (ratchet list clean).
  - stage 4a measurement freshness: initially **red — committed compat JSON stale**; regenerated per the protocol step
    (`./scripta/emit-compat-json.py`, 13 files) — gate **green** after
    regen. The regen is part of the release commit (1.8.0 hand-65
    precedent).
  - stage 4b per-crate `--no-fail-fast` (the branch-tip recipe
    `e3af59886`): **genuine FAILs 63 across 6 crates; env-gated skips 7**
    — faber 1 (the acked row #1), mir-emit-harness 24, radix-mir-metal 1,
    radix-module 34, radix-program 1, radix-semantic 2. This is the
    **pre-closure** picture (classification record pin `06eefed00`: 63
    genuine + 9 env-gated); the canary-closure regens that reduce it to
    the acked 7 landed on main after the freeze and are not on the
    branch. The ladder aborts at 4b on genuine reds by design; the
    remaining boundary legs ran as separate receipts (below). Per the
    release charter the operator ack governs; reds are notes lines, not
    holds.
  - stage 4c boundary (module-boundary parity), 4d metal spike, 4e
    generated-crate check: **green** (`./scripta/test --stage 4c-4e`,
    exit 0).
  - e2e fleet (`./scripta/e2e all` then per-target lanes): receipts in
    the e2e section below.
- **Matrix refresh (faber repo):** `scripta/render-matrices.py` over the
  regenerated measurement JSON (packet faber sibling, path-limited
  commit on its packet branch) — `docs/EBNF_MATRIX.md` +
  `docs/CONVERSIO_MATRIX.md` rewritten, `--check` → **matrices fresh**.
- **Packet pinning (mechanical environment facts, disclosed):** the
  release packet carries writable `radix` + `faber` only; the ladder's
  sibling lookups were pinned read-only — container symlinks for
  `hosts`/`gradus`/`examples`/`norma`/`triga`/`tela`/`cista`, plus
  packet-local env pins for the frozen surfaces
  (`FABER_RADIX_STDLIB=$PWD/stdlib`, `FABER_EXEMPLA_CORPUS=$PWD/corpus`,
  `FABER_PACKAGE_CORPUS=$PWD/product-corpus`,
  `FABER_LIBRARY_HOME=/tmp/freeze-home-190` — a read-only freeze-era
  library home: gradus `a39eefe`, norma `46732cc`, faber `1b7100d`,
  extracted by `git archive`). Without the stdlib pin the exempla
  harness resolves the **main** checkout's stdlib through
  `faberlang_home()` and reports `HIR analysis_ok floor regression:
  0 < 279`; with the pin the parse floor passes (354/413).
- **e2e fleet** (packet-local corpus pins as above; per-target lanes run
  individually because `all` aborts at the first red lane): **green** —
  `canonical`, `mir`, `gpu` (exit 0). **red** — `rust` (emit: 20
  unexpected exempla failures, LOCALE002/SEM010/CODEGEN001 classes —
  the classification record's locale-drift "corpus-emit helpers" family
  and codegen string-shape drift cluster), `go` (emit: 24), `ts`
  (lint: 89), `wasm` (environmental: `RADIX_WASM_STUB_HOST` absent —
  the carried 1.8.0 environmental class), `llvm`, `roundtrip` (69),
  `sexp` (481), `runner` (includes `ad/async-tempus-dormiet.fab` — the
  acked runner/async-tempus row), `swift` (optional target; emit reds).
  These are the frozen-branch e2e known-reds; per the charter they are
  notes lines under the operator ack, not investigation targets.
- **`./scripta/release-gate --locked-release-build`** (run once on the
  exact candidate): locked release build **ok**, hygiene **ok**
  (851 passed), `cargo test -p faber` green except **one** red —
  `faber_build_writes_static_assets_and_manifest_for_browser_product`
  (web2_build) — exactly acked row #1. Exit 101 on that single acked
  red.
- **Artifact + install-from-artifact proof** (runbook local proof,
  `aarch64-apple-darwin` leg): `assemble-dev-kit` → staging +
  regenerated `release-manifest.yaml`; `package-archive` →
  `dist/faber-v1.9.0-aarch64-apple-darwin.tar.gz` (10,699,506 bytes) +
  basename-only `.sha256`, `--check` **ok**;
  `smoke-test-release-archive` → **RELEASABLE** (bare-binary locale
  explains en/la/zh-Hans/zh-Hant/th-TH/vi, reference pack, rust emit,
  MIR-runner hello-world, 18-subcommand tree, package intake, 9 emit
  lanes, convert, `faber --version` contains 1.9.0, archive layout);
  `install-faber --version 1.9.0 --triple aarch64-apple-darwin
  --base-url dist --prefix dist/install-prefix` (SHA-256-verified
  local-mirror channel) → installed `bin/faber --version` →
  **faber 1.9.0**; installed-binary `faber explain SEM001` (en) and
  `--diagnostics-locale la` → embedded reader-locale packs load;
  `faber check` + `faber run` on `corpus/incipit/salve-munde.fab` →
  `ok` / `Salve, Munde!`.
- **`verify-dev-kit` (stale script, disclosed):** crashes with
  `FileNotFoundError … share/faber/locale` — the verifier still expects
  the pre-`e8b840c09` locale-tree layout, but the dev kit dropped
  locale packs from the payload on 2026-08-21 (reader locales are
  embedded in the binary; manifest and payload agree;
  `validate-release-manifest` green). Identical on main — a repo
  defect in the verifier, not an artifact defect. Embedded-locale
  usability is instead proven by the smoke + installed-binary receipts
  above.
- **Leakage scan (disclosed finding):** no credentials, private checkout
  URLs, or hidden build logs in the archive; the only absolute paths in
  `bin/faber` are build-machine paths compiled in via
  `env!("CARGO_MANIFEST_DIR")` defaults
  (`/Users/ianzepp/work/faberlang/worktrees/release-190/radix/crates/faber`)
  plus public `~/.cargo/registry` panic locations. The installed
  public-channel 1.7.0 binary carries the same class
  (`worktrees/release/radix/crates/faber`, 193 path strings) —
  pre-existing product shape, recorded for the operator's
  publish-time verification.

### Known limitations

Carried from 1.8.0 unless the window provably changed them: cross-module
`textus` handles, no numeric-inference accuracy claim, Haskell/Python are
source-emit surfaces, AMD stays fail-closed until ROCm clang is
provisioned.

### Deferred

Per the 1.9.0 plan D1: GEA2-U5e physical receipt and U6b/U6c closeout
continue post-1.9.0 (not release-gating). Container-bounds B3/B4.
Tensor-glyphs U5 (law text) gated. `collection-ergonomics` minted but
pre-implementation. Cista stays `0.1.0`-line (no protocol call this
release).

---

[All releases](/releases/) · [Start](/start/)
