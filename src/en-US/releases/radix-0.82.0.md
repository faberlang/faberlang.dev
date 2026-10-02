+++
title = "Radix 0.82.0"
section = "releases"
order = 26
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.82.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

> **Status**: final

Minor release spanning **760 commits** (`v0.81.0..HEAD`, 2026-08-10→2026-08-15).
Headline: the **tensor-glyph product surface (`·` `×` `⊗` `⊙`) and postfix gradient selection** reach parse/typecheck/emit on the HIR and MIR lanes, the
**visibility model flips to `@ publica` / `@ interna`-only export** (a clean
break), the **census-types schema surface lands** (grammar → HIR → semantics →
locale rows), and the **Haskell and Python source targets** are wired as
emittable HIR backends. The range also rebuilds the ladder's stage-4 split and
commits the compatibility measurement JSON as the faber matrix data contract,
and closes with the **release stabilization set** (`5bdaabaad..80dedd5f6`:
U8 completion, early-merge integration set, all stabilization repairs).

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 760 |
| `feat(...)` commits | 80 |
| `fix(...)` commits | 127 |
| `docs(...)` commits | 300 |
| `test(...)` commits | 26 |
| `style(...)` commits | 12 |
| `chore(...)` commits | 14 |

Reconstruct the full log:

```bash
git log v0.81.0..80dedd5f6 --oneline --no-merges
```

### Major tracks

#### Tensor-glyphs: glyph products + postfix gradient selection

The tensor-glyphs surface reaches working end-to-end paths:

- **Glyph product parse surface** (`·` `×` `⊗` `⊙`) across lexer, parser, and
  HIR (`d1f89f6cf`), with **rank-rule typecheck** (`5fde8ef74`) and
  **fail-closed glyph-product arms** with forma round-trip (`0812e7269`).
- **Host Rust emission for glyph product binops** (`bf0011d02`), glyph
  matvec / vector·matrix emitters with balanced-parens fixes (`511783a58`),
  and glyph **products lowered by operand family** in MIR (`4e8b86c13`).
- **Glyph-spelled device kernels emit on metal/wgsl lanes** (`735165490`),
  full-grid matrix glyph matmul for non-square shapes (`2576f24d9`).
- **Postfix gradient selection parse surface** (Phase 2 unit-2A,
  `766136fa0`) and the TENSOR-GLYPHS-1C host-posture glyph exempla + closeout
  (`a531ad737`).

#### Shape-generics Phase 3: symbolic contracts

- **Symbolic AIR shape scalar and VJP surface** (P3 unit-3A, `26af0c5a3`),
  with `IndexExpr::Infer` pinned fail-closed in `tensor_rank_known`
  (`c91f5148b`).
- **Driver admission of generic backward primals** (unit-3B, `3167728f0`);
  **symbolic proof-suite shape equations** (unit-3C, `7399c6025`).
- **Glyph `·`/`⊙` tensor arms over symbolic contracts** (`5f4f7258d`).

#### Visibility model: `@ publica` / `@ interna` only (clean break)

- `@ interna` annotation parse surface (VM-U1, `9bb0c4ca9`).
- **Export surface flips to `@ publica` / `@ interna` only** (VM-U2,
  `2ba61a284`) — unmarked top-level declarations are now module-private.
- **`privata` dropped on imports**; `publica` re-export kept (VM-U3,
  `3d9c248ff`).
- **Export tiers threaded into import resolution**; `@ interna` fails closed
  (VM-U2, `f84347217`); import-validator seams by tier × package (VM-U4,
  `016c225c4`).

#### Haskell and Python source targets

- **Haskell**: `radix-hir-haskell` pure floor (`23c27046b`), IO / Either /
  scalar workers (`07543a6e0`), `Target::HirHaskell` + `haskell` CLI
  (`e2ab4be46`), faber plans Haskell package artifact paths (`22cd80df6`).
  Dum/Loop worker result kept live in the accumulator (`c3a8c05c1`).
- **Python**: frozen HIR floor emitted from `radix-hir-python`
  (`7c1156839`), `Target::HirPython` + `-t python` (`a54c81436`), faber plans
  Python package artifacts (`6ae49499c`).
- `DISCOVERABLE_TARGET_ROWS` length de-conflicted for the merged
  python+haskell rows (`a79902513`).

#### Census-types schema surface

- **Schema/columna grammar substrate** (S2-U1, `c9c59bb8d`), **HIR schema decl node + lowering + serialization** (S2-U3, `cea9771ce`), **semantic schema nodes + metadata + rejections** (S2-U2, `f03abdd73`), **checked schema subset/compat ops** (`schema_subset`, `O ⊆ I`, S2-U4, `bbc9b3193`).
- **Relational-view reader rows + schema diagnostics × 8 packs** (S2-U5,
  `bf1bf6ef8`) and the schema diagnostic-row re-home (S2-U5-rehome,
  `0b4180cc2`).
- Faber package surfaces gained `HirItemKind::Schema` exhaustiveness arms
  (`95c497536`).

#### Locale and intrinsic catalog

- **Intrinsic-name projection schema + validation + reverse cache** (L1,
  `8d864a573`), **en intrinsic catalog + registry completeness test** (L2,
  `b97ceec68`), **locale surface→canonical intrinsic resolution at the call funnel** (L3, `de9b4a7fc`).
- **Library-owned `locale/<id>/pack.toml` fragments** load (`8cda5ca5a`),
  flat self-contained packs materialize (S0-U3, `51199fa47`), pack-authoritative
  intrinsic lookup with no Latin fallback (`6a37bae8d`).

#### Composite plans (EXEC-01)

- **CompositePlan typed shape, assembly, v1 serialization** (EXEC-01-M1,
  `557e166fe`), **identity verification + first-divergence diagnostics**
  (EXEC-01-M2, `c22e53e1c`), synthetic composite-plan mechanism proof +
  receipt (EXEC-01-M3, `d256be09d`).

#### Clean breaks: incdec glyphs and requirit

- **Source-surface `⊕`/`⊖` migrate to `↑`/`↓`** (incdec Unit A, `ec5c2f100`)
  — token names stay `PostInc`/`PostDec`; target emission unchanged.
- **`requirit` proba modifier retired** (U-A1, `e8de2a404`) and the
  **`requirit`/`require` recoverable guard statement** added (U-B1,
  `b40ca88b0`), with the require-statement corpus exemplum recreated (U-C1,
  `a3a9fe47f`).

#### Ladder and tooling

- **Stage 4 splits into 4a–4d** (`5e3adaab9`); stage 2 lints compiler libs
  only, stops compiling wasmtime, and shares one test compile (`69945ff49`,
  `0332a0f25`, `ce32040aa`); one clippy over the compiler set with a
  persisted inventory (`651f1d83f`, `38e689cac`, `5561dbcd0`).
- **Compatibility measurement JSON committed** (`f916a08d1`, `53d3315c0`) as
  the data contract for the public faber matrix rendering.
- `radix-mir-llvm` gated behind `mir-llvm` with the three facade escalation
  sites decoupled (EL-2b, `721acd7f1`).

#### Semantic/typecheck and codegen correctness

- **Narrowed-value unwrap for receiver/field/index seams** (nn-u3,
  `255c4c8cf`, `85c97f8c9`), use-site threading of the null-check refinement
  (nn-u2, `1bcfc5ecc`), flow-refinement record for null checks (nn-u1,
  `10d88d18b`).
- **Union-variant identity scoped by parent union** (uvn-u1/u2,
  `7456a0f50`, `63c0e878a`); qualified variant construction parses and binds
  to imported union identity (uvf-u3, `d8c97e3e9`); imported union variants
  resolve as first-class values (uvf-u4, `b9376c98b`); bare-variant
  resolution with fail-closed ambiguity.
- **Recovered-parse continuation co-reports parse + semantic diagnostics**
  (em-u3, `345b1750c`); pre-lowering gate stops only on coherence-class errors
  (em-u2, `25f2b6b8b`).
- **Scalar `textus`/`ascii` index infers and returns a single-char ascii value** on rust/ts/go/swift (ascii-char-index A2–A4, `3238f6b32`,
  `4f8184af1`, `bdc678b0f`).
- Type-alias exports join the import surface (`@ publica typus`,
  `33317242a`); generic type aliases bind their own type params and generic
  construction instantiates them (tela-d0/d1); tag-discriminant collision-free
  union emit (tela-d2); `Some()` wraps for nullable union variant fields and
  array elements on the rust lane (tela-d3, `059980abc`, `9c095e0ca`,
  `7ed6d3be5`); TS generic struct casts emit applied type args (R-D1).
- **`PreferStringTemplate` lint** warns on naive string concat chains
  (PST-U1, `07867a99f`), with la WARN018 row + deny tests (PST-U3).
- **Import-contract seam recompute keeps the resolved target path in the session cache** (`d7bc8124b`); stage-2 clippy findings cleared on the
  compiler set (`649148e5e`), `Target::HirPython` covered in
  `lint_generated_code` (`807e83ad5`), compiler crates rustfmt-clean
  (`0eb52c824`).

#### Post-pin delivery (2026-08-14→2026-08-15)

- **U8 lane gating** — runner/device/emit-leaf features, MIR build with zero
  output formats (`2965a8f00`); **default-off parse→analyze→HIR** with
  `radix-mir` optional behind `mir-core` (`a2f02ed0c`); language vocabulary
  moves down to `radix-types` (`ed5eab7df`).
- **Test/e2e rework** — `scripta/e2e` per-target stage driver + stage-scoped
  exempla harnesses (`7481bf0c3`, `0ff26b92d`); `faber run` is interpreted
  execution always (`7412e5e55`); `mir::stepper` renamed to `mir::runner`
  (`db8fcf9f7`).
- **D1 git-dep runtime form** — generated manifests resolve faber-runtime /
  hosts from git sources (`3ddd020de`); dev-kit tooling drops core-support
  references (`869398bae`, `1b5bb6523`).
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
`8036dd57`, `b1f8eeba`, `2624fea0`, `54a93c8b`, `f12335e2`) resolves via
`vivi need show` / `vivi memo show` on the shared board. Scale table
regenerated with `git log a85d802d7..80dedd5f6 --oneline --no-merges |
grep -c '<prefix>('` per row.

### Breaking / author-visible

| Change | Migration |
| --- | --- |
| Export surface is now `@ publica` / `@ interna` only (VM-U2) | Unmarked top-level declarations become module-private; mark exports `@ publica` explicitly. |
| `privata` dropped on imports (VM-U3) | Use `publica` re-export; module-private is the default. |
| Source-surface `⊕`/`⊖` → `↑`/`↓` (incdec Unit A) | Rewrite post-inc/dec source glyphs to the arrow spellings. |
| `requirit` proba modifier retired (U-A1) | Use the `requirit`/`require` recoverable guard statement (U-B1). |
| `radix-mir-llvm` behind `mir-llvm` feature (EL-2b) | Enable `mir-llvm` in Cargo features when the LLVM lane is required. |

### What is NOT included

- No tensor inference accuracy claims; no GPU performance claims.
- The tensor-glyphs gradient surface is Phase-2 parse/selection; Phase-3
  lowering remains in flight beyond the glyph-product MIR/metal/wgsl paths.
- The Haskell and Python targets are source-emit surfaces, not executable
  package build/run backends.
- The faber product CLI surface is covered in the sibling faber release notes.

### Version alignment

| Item | Value |
| --- | --- |
| Source tag | `v0.82.0` |
| `crates/radix` version | `0.82.0` |
| Public artifact tag | `radix-v0.82.0` on `faberlang/releases` |
| Workspace members bumped | all `0.81.0` → `0.82.0` (hygiene-ratchet stays `0.1.0`) |

### Verification contract

The release commit is gated by `cargo build --locked --release -p radix --bin
radix` and `cargo build --locked --release -p faber --bin faber`. The ladder
runs the stage-1–6 gates and the module-boundary parity lane; the tag workflow
runs the full Radix ladder (`./scripta/test --full`) before publishing
component artifacts.

### Publish

1. Bump all workspace crate versions `0.81.0` → `0.82.0` (not
   hygiene-ratchet).
2. `cargo update` so `Cargo.lock` matches manifests.
3. Verify locked release build + the full ladder (stages 1–6 + `--e2e`).
4. **Single commit** with version bump + lockfile (+ measurement JSON when it
   moved): `release(radix): v0.82.0`.
5. Annotated tag: `git tag -a v0.82.0 -m "Radix v0.82.0"`.
6. Push: `git push origin main && git push origin v0.82.0`.
7. Monitor: `gh run list -R faberlang/radix --limit 5`.
8. Confirm `faberlang/releases` publishes `radix-v0.82.0` multi-arch archives.

**Never** tag a commit whose `Cargo.lock` is stale relative to the bumped
manifests — CI uses `cargo build --locked`.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
