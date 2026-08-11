+++
title = "Radix 0.59.0"
section = "releases"
order = 41
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.59.0 |
| **Tag** | `radix-v0.59.0` |
| **GitHub** | [radix-v0.59.0](https://github.com/faberlang/releases/releases/tag/radix-v0.59.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.59.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.59.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.59.0/radix-v0.59.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.59.0/radix-v0.59.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.59.0/radix-v0.59.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.59.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Indexed tensor types land across eight stages: `tensor<T, Figura>` replaces the
legacy bare tensor spelling with explicit shape expressions, shape holes (`_`),
and constraint-based inference. The generics spine gates close: `prae typus` is
replaced by angle-bracket `<T, magnitudo N>` syntax, and `magnitudo` is a keyword
for size parameters. The macOS-arm64 host carries frame data as `faber::Valor`.
The release pipeline switches to a local Docker build lane and drops GitHub CI.

### Scale
| Signal | Count |
| --- | ---: |
| Commits (no merges) | 36 |
| Date span | 2026-06-28 → 2026-06-28 |

### Major tracks

#### Indexed tensor types: `tensor<T, Figura>` (Stages 1–8)

- **Stage 1:** Index term representation — add `IndexExpr`/`IndexId` arena in
  the semantic layer; extend `Type::Tensor` to carry a `Figura` index alongside
  the element type; legacy `tensor<T>` attaches an `Unspecified` bridge until
  grammar deployment. (`8b30eaec3`)
- **Stage 2:** Index unification engine with NumPy-style size-1 broadcast
  (e.g. `[N] + [N, 1] → [N, N]`); wire strict unify into tensor conversio
  shape checks. (`ef9d3831a`)
- **Stage 3:** Index inference core with `solve` and `finalize` — constraint
  registration, deduplication, and shape hole resolution for tensor shapes.
  (`bd86bc12f`)
- **Stage 4:** `tensor<T, Figura>` grammar and shape holes — add `FiguraExpr`
  to the parser and AST; lower `Figura` into `IndexExpr`; require an explicit
  shape in tensor type spellings; rank-0 vacua uses `[]`; `_` marks infer
  holes. (`dfb4f22e5`)
- **Stage 5:** Deploy tensor shape inference at typecheck — wire index
  constraints from tensor intrinsics (`ex.lista`, `forma`, `crea`, `sectio`),
  literal shape witnesses, and `Type::Tensor` unification; fix per-tensor
  `IndexVar` reset so distinct `_` holes do not alias. (`6bb81cdb1`)
- **Stage 6:** Relax tensor element-type construction gate — allow any `T`
  in `tensor<T, Figura>` at lower/resolve time; move numeric constraint to
  arithmetic intrinsics via `tensor_method_requires_numeric_element`; register
  `tensor addita` with the operation gate. (`bf3e2ef9e`)
- **Stage 7:** Rust emit tensor Faber shape annotations — codegen keeps
  runtime `faber::Tensor<T>` carriers while attaching
  `tensor<elem, Figura>` comments from the semantic type table; add shared
  `format_faber_type` and `literal_index_i64s` helpers. (`96167dd57`)
- **Stage 8:** Migrate exempla to `tensor<T, Figura>` — update conversio and
  intervallum tensor exempla to indexed spellings; `shape.fab` uses explicit
  static Figura; add `tensor/textus.fab` for non-numeric elements; rename HAL
  `mensura` bindings; regenerate exempla index (240 files). (`5f09714b6`)
- Close Gate 2: lock hole-and-unify index inference parallel to `Type::Infer`,
  no default Figura, engine-first staging with sugar deferred. (`cc638effe`)

**Polish (indexed types):**
- Share tensor element-type diagnostic constant (`0a13a33d4`)
- Reuse figura constant in tensor arity error (`3443060fe`)
- Deduplicate tensor shape conversio diagnostic constant (`ee80e5014`)
- Parser union flatten for tensor types (`0e9d1652a`)
- Classify `index_infer` constraint errors (`a241167d6`)
- Unify broadcast dim for literal one (`85a599681`)
- Add `is_infer` helper and test for index exprs (`5f501a745`)
- Resolve Figura diagnostics to use figura constants (`51e3c6e54`)
- Figura lowering with shared index-param errors (`feac8b7ee`)
- Syntax AST docs for `Figura` and `TypeExprKind` (`c2867ec9b`)

#### Angle-bracket generics and `magnitudo` size parameters

Replace `prae typus` with angle-bracket `<T, magnitudo N>` syntax. Functions
declare type and size parameters in `<...>` before value parameters; `prae
typus` is rejected with a migration diagnostic. `magnitudo` becomes a keyword
for explicit size-parameter prefix. Gate 1 of the indexed-types-foundation
spine. (`4e2dabafd`)

#### Host Valor frame data migration

- **macOS-arm64:** Replace `FrameData = serde_json::Map` with `faber::Valor`
  across the kernel; add `frame_data` construction helpers and `valor_wire`
  JSON transport encoding so the `Frame` envelope stays serializable without
  collapsing carrier and codec. (`d455db760`)
- Migrate consolum arg projection, Wasm route stubs, and CLI JSON ingest onto
  Valor tabula helpers backed by `FromValor`. (`24d95637c`)
- Record frame valor carrier correction and deferred wire codecs in docs.
  (`43783e74c`)

#### Release pipeline: local Docker build lane

Replace GitHub Actions CI and release workflows with a local, Docker-based
release build lane. Adds `packaging/docker/build-linux.Dockerfile` (one
parametrized Linux image for x86_64 and aarch64), `scripta/release-build`
(assembles reference pack, builds all targets, tars + SHA256s, publishes via
`gh`), and `.dockerignore`. Removes `.github/workflows/ci.yml` and
`release.yml`. Extends `scripta/update-homebrew-faber` with the aarch64 Linux
formula branch. (`517ee2e8d`)

#### Intervallum polish

- Narrow `longitudo` typecheck guard to reject non-numeric arguments earlier
  (`0675bd6da`)
- Wire `longitudo` as a runtime `numerus` intrinsic (`44a2c187a`)
- Polish intra continet Rust codegen (`b4435dd13`)
- Clean up intrinsics module doc for intervallum (`159e7d6bc`)
- Share intervallum bound diagnostic constant (`608d56c7b`)

#### Fixes

- Restore unary parsing in range-bound factors — the intervallum precedence
  refactor routed expression factors through `parse_postfix_inner` and skipped
  `parse_unary`, breaking `cede` and other prefix operators; route through
  `parse_unary_inner` instead. (`7e9f600cd`)

#### Chore / housekeeping

- Format workspace and clear clippy warnings — rustfmt drift from intervallum
  work; clippy lints in faber instans ordering, radix conversio codegen, and
  equality test cases. (`b972273c3`)
- Regenerate exempla corpus index after exempla migration. (`90b367ab5`)
- Polish conversio outcome and failable test formatting. (`2f799ce4b`)

#### Documentation

- Tighten `AGENTS.md` for agent-facing brevity (75 insertions, 169 deletions).
  (`d6fe3d5f1`)
- Document non-standard local release process in `AGENTS.md`. (`7afc367cd`)
- Add factory recent-commit review campaign (`docs/factory/recent-commit-review-campaign.md`).
  (`987f6db6b`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
