+++
title = "Radix 0.73.0"
section = "releases"
order = 27
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.73.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Minor release spanning **147 non-merge commits** (`v0.72.0..v0.73.0`). Canonical
target coverage advances for Go (tensor carriers, narrow CLI, typed imports) and
TypeScript (241/292 Tier-1 e2e). The HIR release readiness review progresses
through RR2b–RR4 evidence, and a broad MIR/LLVM polish pass preserves destination
types across ~45 emit paths.

### Scale
| Signal | Count |
| --- | ---: |
| Commits (no merges) | 147 |
| `feat(...)` commits | 12 |
| `fix(...)` commits | 23 |
| `polish(...)` commits | 67 |
| `docs(...)` commits | 36 |
| Date span | 2026-07-10 → 2026-07-12 |

### Major tracks

#### Go canonical target coverage
- Add tensor elementwise arithmetic carrier (`40676543`)
- Add tensor rank-two matmul carrier (`dfdf9162`)
- Add tensor materialize carrier (`347bfa2e`)
- Revalidate against HIR import producer (`01037b74`)
- Route corpus through typed import contracts (`bdd34c02`)
- Reconcile public corpus coverage accounting (`fd59cf83`)
- G6 GO1: qualify narrow CLI surface for product slice (`e153fb78`)
- G6 GO2: narrow CLI argv emit and driver wiring (`9c5b41d6`)
- G3 GoNeeds: own package imports without body markers (`c9c81496`)
- G6 GO3: map status — mark unused CLI args in emit (`bccc0d71`)
- G6 GO4: elide local package imports; close multi-module status (`e830a632`)
- Revalidate against HIR import producer echo residual (`85c3511a`)
- Fix gap in longitudo field emit + materialize_auto (`6c0adf1b`)

#### TypeScript canonical target coverage
- Advance valor boxing coverage (`36172575`)
- Advance tier-one coverage evidence (`f6ae3ece`)
- Reconcile canonical coverage evidence (`097263e2`)
- Undefer TS, push Tier-1 e2e coverage to 241/292 behavior-checked (`71176e3e`)

#### HIR release readiness review
- Refresh release-readiness review (`83ae5d46`)
- Refill G9 release evidence (`391497a9`)
- Close annotation contract residual (`958a2879`)
- Record RR4 Tier-1 evidence (`6166bbe7`)
- Record RR3 product outcomes (`0b85fc97`)
- Reconcile RR2b capability rows (`936fcd42`)
- Record RR2b delivery split (`578999f1`)
- Record G11 integration checkpoint (`7f5b422d`)
- Record packet-local s0-s1 evidence (`14403a60`)
- Record MIR residual recheck (`252f1914`)
- Record path-safe MIR pivot (`06e9d236`)
- Clear RR4 reader and clippy residuals (`953cf6ab`)

#### MIR/LLVM destination type preservation
Systematic polish pass preserving destination types across nearly every LLVM emit
path so that each operation's result type is carried through to the LLVM value:

- Ordinary call, provider call, try-call, map call destinations (`87cdaa9e`, `8db2def2`, `e7b86906`, `e21439de`)
- GPU builtin destinations (`646f4477`)
- Cast destinations (`9eab8ab0`)
- Array option and array length destinations (`fe8c7b1b`, `8b98e35d`)
- Scalar numeric destinations (`e2325a70`)
- Valor aggregate and genus Valor destinations (`7cdd5c19`, `445cb81a`)
- Tensor conversions, tensor creation, tensor rank, tensor from-flat, tensor slice,
  tensor reductions, tensor pointer results, tensor elementwise spo rad results
  (`69cc230e`, `16edca2c`, `e32d1140`, `dd41c654`, `5ecaebc4`, `5fdb4bd0`, `9294e217`,
  `7f8911df`)
- Sparse conversions, sparse results by destination type (`3843bb82`, `e7a3f459`)
- Text runtime, text length destinations (`168c8852`, `43725fb7`)
- Regex and instans conversions (`0a6e74a5`, `0dfb0390`)
- Tempus and solum destinations (`b2129fbf`, `b1357612`)
- Interval destinations, interval call destinations (`8db2def2`, `418d6c17`)
- Collection conversion and colon lengths (`73bc5ece`, `6c0e8093`)
- Cede semantic types, cede destinations (`dc08a0a4`, `3c239883`)
- Octeti length destinations (`b454c812`, `6c0b8093`)
- Text length destinations (`3fd83d0b`)
- Ordinary call and regex destinations (`384a40aa`, `080edd93`)
- Tensor reductions, pointer, and sparse destinations (`0a2e1d04`, `5fdb4bda`, `1a0a95cc`)
- Tempus wait duration validations (`3de1fa5b`)
- Text runtime and solum read destinations (`9c33d3b7`, `ff8f3535`)
- Lower optional array indices (`2f447ebf`)
- Close G7-GAP-1 hyphen path pub mod residual (`6b74694d`)

#### MIR matrix / GPU shapes (WGSL Stage1)
- Fail-closed metal/llvm matrix shapes after WGSL Stage1 (`2f3e3ccb`)
- WGSL register matrix construct + cell emit (Stage1 subset) (`f99b8fad`)
- Unit B stable shape for matrix kernel param reject (`87b2b2b8`)
- Fix llvm-text nucleum matrix params fail-closed Unit B shape (`b0597a51`)
- Post-Stage1 matrix kernel ABI residual (`520610a8`)
- MIR residual recheck for matrix path (`252f1914`)
- Path-safe MIR pivot for matrix kernel lowering (`06e9d236`)

#### MIR/LLVM host ABI and kernel conventions
- Route text concat through v1 host ABI (`1f2b871b`)
- Emit failable captured closure calls (`09829299`)
- Preserve host kernel calling convention (`6ef8edfa`)
- Define host GPU builtins (`7b686da7`)
- Lower solum providers to host filesystem (`749234bf`)
- Lower tempus waits to host poll (`af0b275f`)
- Lower host cede as identity (`77418c62`)
- Reject invalid solum text carriers (`2e291071`)
- Reject solum write destinations (`8e3b3e46`)
- Require solum read destinations (`14403a60`)
- Validate scalar format returns (`5b00716a`)
- Validate solum read destinations (`b73fdfed`)
- Validate cede destinations (`3c239883`)
- Validate tempus wait destinations (`5064b2fc`)
- Validate text length destinations (`578999f1`)
- Validate scalar format destinations (`41438b88`)
- Lower optional array indices, project optional physical fields (`baa24d64`, `05f59886`)
- Omit vacuum runtime operands (`10f9e1bf`)

#### Factory campaign tracking
- Canonical-lane charter — three-tier model (work/pretty/equal) (`746d4a52`)
- TS-canonical, RS-canonical, Go-canonical campaign control plane refreshes
  (`b9be939e`, `f329949b`, `bee58c77`)
- G6 H3 true/false/echo Go product path complete (`a00df8a8`)
- G8 DB1 sqlite linkage, DB2 error-boundary, DB3 evidence (`886928d4`, `ebd961eb`, `332b02c2`)
- G8 DB4 transactio, G8 DB5 re-oracle field assign (`f4f4f755`)
- G9 API0–API5 transporter/router/concurrency/evidence/reciprocity/delivery
  (`ce1cde1a`, `9b45f79e`, `7ccf6197`, `49b5c26d`, `bd08382a`, `047206dd`, `1d869080`)
- G8 H3 DB1–DB5 complete; theme ready-to-merge (`3e0a5c64`)
- G6 H3 complete; next open unit G8 (`f5ecf78c`)
- G7 Rust CLI carrying evidence batch (`fccd0787`)
- G7-GAP-1 hyphen path pub mod residual (`366b4a6e`)
- Arena-handle contract for Triga Stage 2 identity (`366b4a6e`)
- Close G4 packet status on HIR delivery map (`46f89396`)
- Chart post-Stage1 matrix kernel ABI residual (`520610a8`)

#### Semantic / file-interface hardening
- Formal json/valor in file-interface; unhollow norma:json tool path (`a34e259e`)
- WARN014 when file-interface exports are skipped (`9ede078c`)
- File-interface skip-unsupported for norma:solum imports (`3a6ea700`)
- Install nominal shells across namespaces in file-interface (`fb5387ef`)
- Distinguish cursor yields from awaits (`d8d863ef`)

#### Rust codegen fixes
- Preserve assignment place context (`01c499b3`)
- Route host frame errors through fac (`dffff211`)
- Track async call posture (`43b270a7`)
- Stabilize failable numquam signatures (`653af87d`)
- Optional return wrap, sponte field copy, owned loop clone (`9d685ab8`)

### Other changes
- Prefer Verte target for library call-arg record emit (`cbb87cc3`)
- Restore hygiene ratchet budgets (`efe79c18`); clear RR4 ratchet residuals (`4ac9547c`)
- Align stepper octeti valor boxing (`4428bad6`)
- Retire shim placeholders from probe tests (`03ba6a71`)
- Sync LLVM host gap ledger assertion (`dc22a846`)
- Preserve scalar `vel` representation (`e60516f5`)
- Tighten script classify ledger and valor boxing (`10f9e1bf`)
- Cargo fmt on go/needs/codegen/mir/semantic/tool paths + hosts/macos-arm64
  (`3d89bb38`, `50d74e61`, `b9dde23d`)
- Green-gate main for HIR packet base-update (`2036859c`)
- Main→packet base-update policy with green main gate (`4e5059b6`)
- Drop unused field_access_root_def after clone-policy change (`77fc8720`)
- Keep target policy assertions structural (`e7e9e790`)
- Make Rust oracle debt accounting exact (`16490c66`)
- Ratchet Rust oracle after main refresh (`df46b51e`)
- Defer target policy help to renderer (`62782c9f`)
- Share catalog argument lookup (`01620257`)
- Centralize TypeScript argument emission (`ae6652fd`)
- Centralize Rust harness progress plumbing (`29b2ef85`)
- Name conversion renderer argument (`09b3eb5b`)
- Clarify tensor shape type failure path (`14fdbb22`)
- Close stale Go echo residual (`8ae43c2f`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
