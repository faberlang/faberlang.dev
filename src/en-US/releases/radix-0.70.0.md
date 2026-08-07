+++
title = "Radix 0.70.0"
section = "releases"
order = 29
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.70.0 |
| **Tag** | `radix-v0.70.0` |
| **GitHub** | [radix-v0.70.0](https://github.com/faberlang/releases/releases/tag/radix-v0.70.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.70.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.70.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.70.0/radix-v0.70.0-aarch64-apple-darwin.tar.gz) | 2.8 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.70.0/radix-v0.70.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.70.0/radix-v0.70.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.70.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Package host bridge milestone: JSON genus contracts enforce cross-target serialization
contracts, the package host attach hook and `norma:solum` bridge complete package-MIR
stdout I/O, annotation contracts (`@ annotatio`) land as a compiler-owned schema
mechanism, and the MIR target promotion campaign graduates all planned emit targets.
The tensor systems campaign closes with view-backed storage, packed numeric blocks,
and indexed access parity.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 103 |
| Date span | 2026-07-08 → 2026-07-09 |

### Major tracks

#### Package host bridge (norma:solum)

- **Bridge `norma:consolum` for package-MIR stdout:** adds `KernelModule::Consolum`
  (dic/scribe/mone), host `write_stdout_raw`, and stepper dispatch so interpreted
  packages emit raw stdout without a forced newline. Unblocks coreutils `echo -n`
  and `printf` parity. (`4a7987793`)
- **Emit package host attach hook:** `frame_shim.rs` generates the attach/detach
  wrapper so compiled packages wire into the host runtime. (`44540dd20`)
- **Complete package host solum bridge:** `hosts/macos-arm64/src/norma/solum.rs`
  implements the solum kernel module with full test coverage. (`5c7c06373`)

#### Annotation contracts and JSON genus contracts

- **Annotation contracts (`@ annotatio`):** adds compiler-owned contract machinery —
  `@ annotatio` marks a genus as a compile-time schema; braced applications validate
  constant fields and attachment targets; HIR carries `contract_id` for consumers;
  file interfaces export/import schemas without framework-specific compiler families.
  877-line semantic pass with 311-line test module. (`82537ee52`)
- **Polish passes on annotation contracts:** structure tightening, pipeline extraction,
  simplified HIR lowering, shared named-type value helpers, and doc coverage across
  contract HIR and file-interface surfaces. (4 `polish` commits: `527c8ef5f`,
  `4c835c276`, `a387e9544`, `8b52ee0ba`, `598a766b1`, `e08b79b15`)
- **JSON genus contracts:** enforces cross-target serialization contracts through a
  dedicated semantic pass (`json_genus.rs`), updates EBNF, forma, typechecker, HIR
  lowering, and adds a 130-line `json_genus_test.rs`. 24 files changed, +560/−10.
  (`159a7a167`)

#### MIR target promotion campaign

All five planned MIR emit targets promoted from probe to supported-with-limitations:

| Target | Delivery doc | Key commit |
| --- | --- | --- |
| sexp (Stage 1, substrate routing) | `stage-1-substrate-decision.md`, `stage-2-sexp-promotion-delivery.md` | `23a7f25b5` |
| llvm-text / metal-text / wasm | `stage-2-{llvm,metal,wasm}-promotion-delivery.md` | `75d43918a` |
| wgsl-text (via naga gate) | `stage-2-wgsl-promotion-delivery.md`, `stage-3-closeout-delivery.md` | `01148512e` |

- **Naga WGSL gate:** wire a skip-if-missing naga validate test for promoted wgsl-text
  emit; expose `naga_available` in exempla e2e helpers. (`021611f54`)
- **MIR validation confidence gate:** complete MIR lane validation, retires the sexp
  probe shim, hides legacy scena target discovery, and harvests scalar layout substrate.
  (`b97564528`, `70593ca534`, `cd6e3969e`, `3434e0628`)
- **Target capability matrix** updated in `docs/design/target-capability-matrix.md`
  across all promotion commits. Campaign closeout documented in
  `docs/factory/mir-target-promotion/CAMPAIGN.md`.

#### Tensor systems campaign

The tensor systems campaign closes with a full proof floor across 15+ `feat:` commits:

- **View-backed storage:** tensor `sectio` reworked as a view over the backing buffer
  (+233/−65 in `faber/src/tensor.rs`). (`90c5dbb34`)
- **Packed numeric blocks:** toy `u4` packed block type for dense tensor storage.
  (`95c082fbb`)
- **Materialize intrinsic** exposed for tensor instantiation. (`89df943de`)
- **Indexed access parity** for tensor element read/write. (`ee1aafd27`)
- **Runtime ABI** recorded with placement policy, storage locus facts, and failable
  matmul. (`b71c7fda4`, `7d20f704a`, `550dfdd96`, `da0b9dd91`)
- **Target support** recorded for tensor systems with operation floor, workload proof
  floor, and FMIR package proof. (`385ebe3d3`, `2f4ca0b26`, `fabd05dba`, `00e85a52c`,
  `4a14474c9`)
- **Campaign closeout** with e2e closeout fixtures and stage-13 delivery doc.
  (`401ea1398`)

#### Vel defaulting and expression lowering

- **Local `vel` defaulting and intervallum bound conversio:** reclassify expression
  `vel` as tight nullable elimination (above multiplicative), with RHS interval
  constructor completion so `maybeRange vel 0‥0` stays intact. Emit intervallum width
  conversio bound-wise instead of invalid `as` carrier. EBNF, forma/faber precedence
  updated. (`6ca0a24d9`)
- **Lower expression AD to sermo MIR:** expression lowering path from abstract
  declarations to sermo MIR, with stepper runtime support. (`1f41facfb`)
- **Captured argv process calls:** stepper kernel and host processus support for
  captured `argv` in subprocess calls. (`d9d63a69d`)
- **Fix numeric conversions and dense octeti valor:** numeric cast corrections in
  Rust codegen and dense octeti tag preservation through stepper valor wire.
  (`effc4aba8`, `0ff60098a`)

#### Workspace reorganization

Two large refactoring waves consolidate the private compiler workspace:

- **Absorb forma into `radix::forma`; extract `faber-runtime`:** fold the forma
  formatter crate into the compiler (private surface), move `faber-runtime` to the
  public sibling `faberlang/faber-runtime`. 55 files changed, +60/−4551.
  (`323c25b7c`)
- **Retire `norma` crate; extract `faber-cli` and `examples`:** remove dead
  `crates/norma`, rename `crates/faber` → `faber-runtime`, move `faber-cli` to
  sibling `faberlang/faber` and `examples` to `faberlang/examples`. 336 files
  changed, +286/−39208. (`8e633750c`)
- **Extract `cista` to public sibling repo.** (`1e0d1ce5e`)
- **Absorb `scena` into `faber-cli`** and drop the separate crate. (`daabd1bd7`)
- **Repoint corpus fixtures** to sibling `examples/corpus`. (`407a5c573`)
- **Fix library home resolution** from nested worktrees. (`70594b113`)
- **Keep radix hygiene budget green.** (`74bd81b2f`)

### Other changes

- **Coreutils:** land `echo -n` stepper slice — parse leading `-n`, write via
  `norma:consolum.dic`, strict no-newline parity fixtures. (`c129b60da`)
- **FMIR diagnostics:** assert FMIR diagnostic identity in companion modules, fix
  manifest FMIR build target discovery, resolve post-merge FMIR and tensor defers.
  (`532d04716`, `9ec2f8bd2`, `f8bfe0e9e`, `18be1db36`)
- **Centralized packed `u4` decoding:** move packed u4 logic into faber central
  helper. (`59a28a63f`)
- **Morphologia docs:** link morphologia for conjugation and stdlib posture; revise
  conjugation policy for stems and dual axes. (`3b57b5b3e`, `eb7c935bc`)
- **Async AD phase zero boundary locked** for the next lowering slice. (`b045c9db6`)
- **Chore:** ignore project-local Vivi mailspace. (`5c55ae329`)
- **Exempla harness** discovers public sibling corpora. (`cb9862846`)
- **AI workbench:** record stage5 systems discovery. (`62e5ed8e7`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
