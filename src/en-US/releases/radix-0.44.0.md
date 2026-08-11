+++
title = "Radix 0.44.0"
section = "releases"
order = 56
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.44.0 |
| **Tag** | `radix-v0.44.0` |
| **GitHub** | [radix-v0.44.0](https://github.com/faberlang/releases/releases/tag/radix-v0.44.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.44.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.44.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.44.0/radix-v0.44.0-aarch64-apple-darwin.tar.gz) | 1.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.44.0/radix-v0.44.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.44.0/radix-v0.44.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.44.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Dense single-day release (58 commits, all 2026-06-24) spanning four
interleaved campaigns: **directional assignment unification** (split unify →
sound type-assign rejection), **compiler vocabulary consistency** (Stages 2–5
renames), **definite assignment** (InitState lattice + `fixum` write-once
binding), and **literal-family polish** across the pipeline.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 58 |
| Date span | 2026-06-24 → 2026-06-24 |

### Major tracks

#### Directional assignment unification (valor unification policy)

Type unification had a single symmetric path (`unify`) used for both inference
joins and assignment checks, allowing invalid assignments (e.g. `tabula` to a
`numerus` field) to pass silently in some JSON literal paths.

- Split `unify` into `unify_join` (symmetric, for inference) and
  `unify_assign` (directional, requires `assignable(left, right)`), then
  route all 67 call sites and enforce the split (`9f6b9046c`,
  `0da5c476e`)
- Fold `tabula` ascribe validation into JSON literal typing (valor Stage 4);
  delete the now-redundant `validate_json_valor_for_map` and
  `check_literal_with_expected` paths (`f9e3faa5c`)
- Acceptance gate (Stage 5) with explicit F8–F11 bare tabula rejection tests
  (`ff0788e1b`, `e6a02b279`)

#### Vocabulary consistency (Stages 2–5)

A multi-stage mechanical rename campaign aligning naming across AST, HIR, MIR,
and all codegen backends. Staged to keep diffs reviewable per layer.

- **Stage 2:** align MIR nil-test spelling with HIR (`IsNotNil`), AST
  `Literal::Int` → `HirLiteral::Int`, Latin `MirDiagnosticKind` mirror
  (`597c924a3`)
- **Stage 3:** expand `MirStmt`/`MirStmtKind` to `MirStatement`/`MirStatementKind`
  across MIR nodes, lowering, validation, dump, and probes (`ce595bad6`)
- **Stage 4:** expand `HirStmt`/`HirStmtKind` to `HirStatement`/`HirStatementKind`
  across HIR, lowering, visitors, semantic passes, MIR lowering, and codegen
  (`874b86586`)
- **Stage 5:** expand `HirExpr`/`HirExprKind` to `HirExpression`/`HirExpressionKind`
  across the same full pipeline span (`6099e8b5a`)
- Rename block statement fields to `statements` to align with `HirBlock`,
  `BlockStmt`, `Program`, and `MirBlock` (`05bc51477`)

#### Definite assignment and `fixum` deferred init

Introduce a new semantic Phase 3a definite-assignment pass and unify
"initialized now" / "initialized later" into the `fixum` write-once concept.

- Add definite-assignment pass with shared `InitState` lattice export,
  `UseBeforeInit` (SEM058) diagnostics (`d96cb13bc`)
- Fix branch-soundness: join branch exit states at control-flow joins using
  `InitState::join_paths` so conditional initialization degrades to
  `MaybeAssigned` and is rejected (`0bc8e6b4e`)
- Parse `fixus` local bindings (`fixus <type> <name>`) through HIR with
  `Mutability::Fixus` and `HirLocal.fixus` (`128b43038`)
- Drop the `fixus` prefix-binding form (not a sibling to `fixum`);
  `fixum` is the canonical write-once binding (`1c3896af6`)
- Unify `fixum` deferred init: a `fixum numerus x` with no initializer
  declares a write-once slot tracked as `Unassigned`; a second assignment
  emits `ImmutableAssignment` (SEM020). All assignment discipline lives in
  the definite-assignment pass (`bce528c94`)

#### Campaign 0a–0b (semantic passes pre-work)

- Single-pass inferred-callee argument typechecking: remove the duplicate
  `check_call_args` traversal on inferred-callee paths (`919f96a32`)
- Union member dedup via structural equality (`TypeTable::is_distinct_union_member`)
  instead of `TypeId` identity, fixing compound union collapse in annotations
  (`e80a8c045`)

#### MIR e2e harness and gap ledger

- `exempla_mir_e2e` harness that stops at validated MIR lowering (independent
  of Wasm/LLVM emission) (`9b7f993eb`)
- Baseline gap ledger with per-exemplum tiers, four-way gap classification,
  and intentional-subset count (42) for backend floor ratchets

#### Literal-family polish

A coordinated polish pass across the full pipeline to share parsing, lowering,
and codegen helpers for the literal family (`ascii`, `octeti`, JSON `tabula`,
numeric).

- Lexer: shared `delimited-literal` and `escape` helpers, register `ascii` and
  retired-block scan cases (`db26aa983`, `6301d169f`)
- Parser: share JSON object member parsing, accept `octeti` literals in arm
  heads (`a0064f393`, `f3f362bd4`)
- HIR lowering: share `literal_to_hir`, allow `octeti` patterns
  (`03fcc93bc`)
- MIR lowering: extract `unsupported_literal` for deferred literals
  (`970249d09`)
- Typecheck: fix literal docs, share interned payload helper (`c6db9ba18`)
- Codegen restore blank-line separation in Rust/Go literal generators
  (`7266eafab`, `161e1e228`)
- Driver tests: add `compile-failure` helper and literal-family coverage
  (`49b94485e`)

### Other changes

- `fix(faber)`: compile `faber` CLI against the current program AST after
  Rust codegen refactors (`244c7c33b`)
- Add explicit `F8`–`F11` bare `tabula` assignment rejection tests
  (`e6a02b279`)
- Clarify `Option` unwrap assignability rule, inferred-return join policy,
  and JSON valor map validation in typecheck / driver comments
  (`9ee31abfc`, `18cb153b0`, `eba4b00a0`)
- Reconcile pipeline tracks and add compiler campaign overview (`8489952cb`)
- Reclassify semantic pass phases and resolve open blockers (`62181f014`)
- Refresh Wasm/LLVM continuation plans for binary emit and Rust-parity e2e
  (`c35238c23`, `7af4f50c4`)
- Lock MIR lowering scope decisions in factory goal (`809ad3594`, `e275d4ef4`)
- Compiler vocabulary consistency delivery spec, goal, and ledger
  (`910b82eb9`, `e41bf66ac`, `61b7ad85e`, `2c0e56126`)
- Valor unification policy goal and delivery spec (`78218c500`,
  `d61d06539`, `b5158d0e2`)
- Semantic passes delivery spec (`b5158d0e2`)
- FaberValue canonicalization goal (deferred shortcoming) (`d9779baaf`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
