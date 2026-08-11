+++
title = "Radix 0.66.0"
section = "releases"
order = 34
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.66.0 |
| **Tag** | `radix-v0.66.0` |
| **GitHub** | [radix-v0.66.0](https://github.com/faberlang/releases/releases/tag/radix-v0.66.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.66.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.66.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.66.0/radix-v0.66.0-aarch64-apple-darwin.tar.gz) | 2.6 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.66.0/radix-v0.66.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.66.0/radix-v0.66.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.66.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Major release spanning **818 non-merge commits** across ten interleaved themes.
This is the largest single Radix release by commit volume, covering GPU/LLVM
kernel emission, metadata exposure, diagnostic event system overhaul, TLA+
verification infrastructure, Rust canonical cleanup, stepper alignment,
annotation syntax design, deferred correctness fixes, and faber-cli package MIR
delivery. The tag theme ("Package MIR stepper and Faber CLI package MIR campaign
closure") captures the final layer; the bulk of the work is GPU/LLVM compiler
infrastructure.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 818 |
| Date span | 2026-07-01 → 2026-07-05 |
| `feat` commits | ~389 |
| `polish` commits | ~96 |
| `docs` commits | ~92 |
| `test` commits | ~41 |
| `fix` commits | ~24 |
| Unique authors | 1 |

Daily distribution: Jul 1 (5), Jul 2 (218), Jul 3 (302), Jul 4 (245), Jul 5 (48).

### Major tracks

#### Theme 1: MIR GPU/LLVM kernel emission + reflection (~180 commits)

The dominant theme. MIR gains full GPU kernel emission for WebGPU/WGSL and Metal
targets, plus LLVM text-target kernel emission and a GPU reflection infrastructure
that exposes builtin axes, dispatch sizes, workgroup counts, resource bindings,
and register types.

Key commits:

- `a22b78657` feat(mir): emit llvm external call imports
- `681030c65` feat(mir): emit llvm regex raw data globals
- `2b0428f5a` feat(mir): emit llvm octeti raw data globals
- `761f3d8f0` feat(mir): emit llvm function reference symbols
- `674065fc9` feat(mir): reflect gpu resource bind groups
- `ec0db574c` feat(mir): reflect gpu dispatch sizes
- `7fd15a10c` feat(mir): reflect gpu resource element counts
- `304da285c` feat(mir): normalize gpu loop control entry gotos
- `a9651ee8b` feat(mir): normalize gpu loop entry gotos
- `66272148e` feat(mir): lower GPU builtin call sources
- `330ad22ad` feat(mir): version GPU reflection JSON
- `c2033d871` feat(mir): expose GPU reflection source names
- `e11613bbc` feat(mir): emit u32 modulo gpu kernels
- `cc82edbb0` feat(mir): emit u32 bitwise gpu kernels
- `1b3e4b25d` feat(mir): emit u32 bitwise not kernels
- `e49bdfe1c` feat(mir): add gpu workgroup builtin facts
- `b0d7f6232` feat(mir): reflect gpu builtin axes
- `a96bf7f8a` feat(mir): reflect gpu workgroup counts
- `0062a534d` feat(radix): implement vector source model for GPU register types
- `bcfbd42f2` feat(llvm): emit register vector lanes
- `6c121aeb0` feat(mir): lower numeric to boolean llvm casts
- `f5db186aa` feat(mir): lower boolean to numeric llvm casts
- `533dad3fd` feat(mir): lower float to integer llvm casts
- `7aba2f03d` feat(mir): lower integer to float llvm casts
- `9b77306cb` Plan captured closure environment layout
- `5bf3c45ae` Plan GPU closure callable legality reconciliation

#### Theme 2: LLVM/GPU metadata exposure (~192 commits)

A massive paired `feat(llvm): expose byte X` / `feat(gpu): expose webgpu Y`
block that systematically exposes every metadata field of the LLVM byte-descriptor
and GPU WebGPU binding families. Each field gets an `index count` + `index`
commit pair, making the full descriptor/property surface observable through
reflection.

Selected from ~66 `expose byte` / `expose webgpu` commits:

- `eed6d7b73` feat(llvm): expose byte terminator policy index count
- `0a5fef0bc` feat(llvm): expose byte terminator policy index
- `bf7224819` feat(llvm): expose byte schema version index count
- `5229bcf0c` feat(llvm): expose byte schema version index
- `fda414fae` feat(llvm): expose byte representation index count
- `e49f1eb5a` feat(llvm): expose byte representation index
- `aba7469bf` feat(llvm): expose byte linkage index count
- `95a3434f5` feat(llvm): expose byte linkage index
- `e5de985dc` feat(llvm): expose byte pointer policy index count
- `6125e341e` feat(llvm): expose byte mutability index count
- `79cf40600` feat(gpu): expose webgpu bind group entry element type
- `413b4891e` feat(gpu): expose webgpu bind group entry element byte width
- `41b914939` feat(gpu): expose webgpu bind group entry element count
- `dcaf61dba` feat(gpu): expose webgpu bind group entry element layout
- `931ea4eb2` feat(gpu): expose webgpu bind group entry shader visibility
- `30afd2c52` feat(gpu): expose webgpu bind group entry shader access
- `00731201a` feat(gpu): expose webgpu bind group entry access
- `5cfafb12a` feat(llvm): expose byte payload index
- `6e65692f2` feat(llvm): expose byte layout index count
- `b68f6b533` feat(llvm): expose descriptor family count
- `a9b57d4f7` feat(llvm): expose descriptor pointer policy count

#### Theme 3: Test contract locking + campaign cleanup (~93 commits)

Systematic `test(gpu): lock webgpu X` and `test(llvm): lock Y` commits
lock down every metadata contract. Paired with phase-completion markers
and LLVM fix commits that close the loop on each sub-campaign.

- `555a3feb3` test(gpu): lock webgpu adapter schema contract
- `6c7aed364` test(gpu): lock webgpu output entry contract bundle
- `4d815aef7` test(gpu): lock webgpu output entry access
- `6cd611711` test(gpu): lock webgpu output entry role
- `49b2c1b69` test(gpu): lock webgpu output entry kind
- `87a815317` test(gpu): lock webgpu layout entry layout index
- `1ea9c8bcb` test(llvm): lock descriptor family metadata contract
- `00c0778fa` test(llvm): lock byte-data family metadata contract
- `ddf42005c` test(llvm): lock failable function constant arguments
- `fe9dcc3d6` fix(llvm): render function constant arguments as pointers
- `658094972` fix(llvm): materialize closure function values as pointers

#### Theme 4: Design/planning interlude + reader locale (~65 commits)

A reader-locale substrate is designed for the Faber human-facing surface, with
north-star design docs, reference locale set definition, NFKC normalization
switch, and English keyword sugar specification. Planning commits cover
prefix predicate retirement, annotation sugar, and split of the private
compiler from public language concerns.

- `f5895006a` docs: add reader-locale north-star design for human-facing surface
- `ef330eb69` Rewrite reader-locale design around reference locale set
- `437d6e981` Complete reader locale keyword lookup phase
- `102d8dc5b` feat(radix): switch lex normalization from NFC to NFKC
- `05dd80780` Add goal: switch Faber lex normalization from NFC to NFKC
- `5522921c3` Add goal: aspect-oriented TLA+ verification over the HIR
- `808300e3c` docs: lock glyph operators as fixed in English keyword sugar spec
- `8f96b8fad` docs(plans): split private compiler from public language
- `1e806af6d` docs(factory): plan prefix predicate retirement
- `150f58c68` docs(factory): add annotation-sugar goal from design spec
- `3696ec53f` docs: add reader locale substrate goal

#### Theme 5: Diagnostic event system overhaul (~88 commits)

A systematic restructuring of the diagnostic event system. Every subsystem's
diagnostic messages are converted from ad-hoc prose to structured templates
with event spines. The `Structure ... diagnostics` commit pattern covers
every class: type mismatch, operand, call, pattern, interval, aggregate,
access, expression, generic constraint, failable call, alternate exit.

- `2505b1c37` Isolate diagnostic source lines for bidi rendering
- `46e41fcaf` Structure remaining ops type mismatch diagnostics
- `60ed295b7` Structure ops operand type mismatch diagnostics
- `c03bcea94` Structure call lookup type mismatch diagnostics
- `33f9494f2` Structure convert type mismatch diagnostics
- `3bcaf03c7` Structure aggregate type mismatch diagnostics
- `926b2f036` Structure item expression diagnostics
- `d55c1d3e0` Structure pattern index diagnostics
- `b00385e4a` Structure intervallum type mismatch diagnostics
- `31ae040c4` Structure call argument diagnostics
- `39c1e9676` Structure failable call diagnostics
- `ffff51db8` Structure alternate exit diagnostics
- `7782fa4ad` Structure statement type mismatch diagnostics
- `530d3c1bd` Structure comparison operand diagnostics
- `bf3342893` Structure intrinsic operand diagnostics
- `94670f04c` Structure generic constraint diagnostics
- `f0df6073f` Remove parser semantic diagnostic prose fields
- `cbc407834` fix(radix): close deferred diagnostics stage

#### Theme 6: TLA+ verification + WebGPU proof + polish (~140 commits)

Two concurrent sub-campaigns:

**TLA+ verification infrastructure**: Complete pipeline from HIR aspect report
substrate through template emission, model checker runner, coverage reporting,
and catalog expansion.

- `5522921c3` Add goal: aspect-oriented TLA+ verification over the HIR
- `84ae01787` Complete TLA HIR aspect report substrate
- `745400de2` Complete TLA aspect template emission
- `aa65559af` Complete TLA model checker runner
- `12cf814b3` Complete TLA coverage reporting
- `633f562d3` Complete TLA catalog expansion decision
- `2020c8ffd` polish(aspect): factor TLA template constants and variant emission

**WebGPU browser host proof**: Full proof-of-concept WebGPU browser host
scaffold, reflection consumer implementation, and proof check.

- `0824deff1` Implement WebGPU browser proof
- `840997610` Add WebGPU browser proof check
- `ceb9aaf5e` Implement WebGPU reflection consumer
- `37b87589b` Plan WebGPU browser host scaffold
- `90bcf9e8d` docs(factory): close WebGPU browser host proof

**GPU vector proofs**: Formal MIR proofs for GPU vector operations.

- `1b039b686` feat(mir): prove GPU vector swizzle
- `b441fbd21` feat(mir): prove GPU vector cross product
- `f2d00170a` feat(mir): prove GPU vector elementwise arithmetic
- `1a4196e11` feat(mir): prove GPU vector constructor dot

**`polish(mir):` pass** (~44 commits): Systematic naming, documenting, and
exposing of MIR emission boundaries — LLVM symbols, stepper dispatch, wasm
imports, kernel ABI errors, WGSL/Metal unsupported diagnostics, capability
gap slice accessors, and dump ID namespace prefixes.

- `d5ed79ff7` polish(mir): name llvm pre-emission empty-rejection fallbacks
- `feeb8dce9` polish(mir): name stable device-safe rejection shape strings
- `ff6a970fd` polish(mir): name kernel ABI error messages
- `2572f9416` polish(mir): document llvm symbols and runtime prefix
- `7ee8fb08f` polish(mir): document llvm declare gathering
- `cb5d363a8` polish(mir): document structured CFG recognition boundary
- `2864f947f` polish(mir): document llvm emit and name probe header
- `bc8996f25` polish(mir): name llvm literal global families and descriptors
- `1bb0432c8` polish(mir): dedupe wasm import prefixes and arg suffixes
- `81e5f10dc` polish(mir): name stepper unsupported diagnostic prefix

#### Theme 7: Rust canonical cleanup + closure ABI (~60 commits)

The RC-002 through RC-009 campaign closes the Rust canonical cleanup cycle.
Highlights include prelude allow narrowing, control-flow lowering, static
generis emission, valor helper ratchet, typed error reconciliation, and
package materialization formatting. MIR generic monomorphization is
implemented and the closure value call ABI is selected and implemented.

- `5afa42fb0` Complete RC-002 prelude allow narrowing
- `acdd459a8` Complete RC-004 control-flow lowering
- `4b08d3266` Complete RC-005 static generis emission
- `9c1476092` Complete RC-006 valor helper ratchet
- `6003af9a0` Complete RC-007 typed error reconciliation
- `d788914c1` Complete RC-008 Rust field spelling policy
- `e6a01d149` Complete RC-009 package materialization formatting
- `860dc6190` Complete Rust canonical cleanup
- `07d87fe18` Add optimized Rust canonical harness
- `be9834042` Implement closure value call ABI
- `fcad40f27` Select closure value call ABI packet
- `231f9ee03` Implement MIR generic monomorphization
- `e279bf0fa` fix(radix): instantiate generic MIR call signatures
- `81cb2814e` feat(llvm): canonicalize literal data pointers

#### Theme 8: Stepper alignment + MIR sexp + annotation sugar (~45 commits)

Three convergent sub-themes:

**Stepper alignment**: Three stages (0–2) refresh the stepper baseline, build
a structural capability classifier + matrix tier, and add a runtime-boundary
ledger stepper column with guard.

- `70ebc5ae8` Add stepper-alignment factory goal and campaign
- `6525f5cd7` stepper-alignment(stage0): refresh baseline, bucket corpus growth, ratchet floors
- `c0db54d96` stepper-alignment(stage1): structural capability classifier + matrix tier
- `c48e84129` stepper-alignment(stage2): runtime-boundary ledger stepper column + guard

**MIR sexp text target**: The sexp probe is promoted to a proper text target
with default carriers, runtime helpers, aggregate carriers, CFG terminators,
and nullable runtime helpers.

- `8f079f6a2` feat(mir): promote sexp probe to text target
- `b357e2537` feat(mir): add sexp default carriers
- `320718c56` feat(mir): emit sexp runtime tier one
- `eb9d4bb6f` feat(mir): emit sexp cfg terminators
- `96b0727ee` feat(mir): emit sexp aggregate carriers
- `6349e6106` feat(mir): emit sexp nullable runtime helpers

**Annotation sugar + type-call retirement**: Four-stage annotation sugar
implementation (attachment fix → braced parse → canonical braced emit →
token-backed family promotion) plus retirement of the old type-call constructors
and prefix predicate syntax.

- `91fd91e1b` feat(radix): annotation sugar stage 1 — attachment fix and HirAnnotation
- `640086063` feat(radix): annotation sugar stage 2 — braced parse surface
- `6628938d9` feat(radix): annotation sugar stage 3 — canonical braced emit
- `dc159447d` feat(radix): annotation sugar stage 4 — promote token-backed families
- `ecb05f5f3` feat(radix): retire type-call constructors and prefix predicates

#### Theme 9: Deferred fix campaign (~25 commits)

Closing correctness findings from the MIR audit. Each `fix(radix): close deferred X`
commit resolves a stage: parser clean-break, annotation metadata, canonical
annotation, rust handled expression, MIR generic, air eligibility, MIR target
honesty, field collision, and diagnostics. Specific DEFER-* tickets are addressed:

- `6edf3a27c` fix(radix): validate generic call sites with uninstantiated param slots (DEFER-074)
- `1a711b9c7` fix(radix): emit multi-guard custodi in source order (DEFER-068)
- `ad8f57d20` fix(radix): make Go/TS target gate a lazy spelling smoke test (DEFER-071)
- `990b9aeca` feat(mir): defer enum llvm layout explicitly
- `5f0fe6682` feat(mir): classify callable llvm deferral
- `fcb013c9b` feat(mir): classify failable llvm cfg deferral
- `cbc407834` fix(radix): close deferred diagnostics stage
- `da725e0e3` fix(radix): close deferred proof honesty stage
- `1058ea9aa` fix: address deferred fix review findings

#### Theme 10: faber-cli package MIR campaign (~24 commits)

The user-facing tail of the release. The faber-cli gains full package MIR
capability: CLI option parsing (root flags, scalar operands, global options,
mounted text operands, defaulted options), command alias dispatch, zip archive
interpretation, MIR linking, MIR interpretation through the stepper, and
probe-target parity with `radix emit`.

- `3355c50c8` feat(faber-cli): interpret zip package archives
- `80bb6b44e` feat(faber-cli): spike package MIR linking
- `41b1adad9` feat(faber-cli): run packages through MIR interpretation
- `7111381e7` feat(faber-cli): MIR probe target parity with radix emit
- `b8b06bb1c` feat(faber-cli): extract package analysis API
- `5f58668ef` feat(faber-cli): close package MIR CLI campaign
- `4d2c7305e` feat(faber-cli): dispatch package MIR command aliases
- `840e91a65` feat(faber-cli): parse mounted CLI text operands in package MIR
- `7e0fad74c` feat(faber-cli): dispatch mounted CLI package MIR commands
- `5a1db8a69` feat(faber-cli): interpret root CLI packages in MIR

### Interleaving note (Jul 4)

July 4 produced 245 commits with heavy interleaving across themes 5, 6, and 7.
The diagnostic event system (`Structure … diagnostics`), TLA+ verification
completion markers, and Rust canonical close-out commits (RC-009, RC-008, RC-007,
RC-006, RC-005, RC-004, RC-002) all landed within overlapping hours. This is
visible in the commit log as back-to-back `Structure ... diagnostics`, `Complete RC-...`,
and `Complete TLA ...` commits from a single session.

### Breaking / author-visible

| Change | Migration |
| --- | --- |
| Type-call constructors and prefix predicates retired | Use annotation sugar syntax (`@`-prefixed braced forms) |
| Faber lex normalization switched from NFC to NFKC | Affects character-level source matching; NFKC normalizes more compatibility characters |
| Reader-locale substrate in design phase | No runtime impact yet; design is internal planning |

### Verifying the release tag

```bash
git log v0.65.0..v0.66.0 --oneline --no-merges | wc -l
# expect 818
```

The commit range is RFC3339-bounded: `git log v0.65.0..v0.66.0 --format="%ai" --no-merges`
should show dates from 2026-07-01 through 2026-07-05 inclusive.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
