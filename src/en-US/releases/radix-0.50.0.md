+++
title = "Radix 0.50.0"
section = "releases"
order = 49
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.50.0 |
| **Tag** | `radix-v0.50.0` |
| **GitHub** | [radix-v0.50.0](https://github.com/faberlang/releases/releases/tag/radix-v0.50.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.50.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.50.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.50.0/radix-v0.50.0-aarch64-apple-darwin.tar.gz) | 1.8 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.50.0/radix-v0.50.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.50.0/radix-v0.50.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.50.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Scena scripting campaign: new MIR stepper interpret path, `faber run` single-file mode, interactive REPL, `-c` one-liner, and `faber_script` embed crate (renamed `scena`). On the compiler side: frame-gateway stream lowering ships stages 1–3 with `ad`/`emitte` via HIR→MIR sermon intrinsics, a shared hygiene naming ledger unifies temporaries across Rust/Go/TS codegen, a MIR sexp probe target with Racket e2e harness goes live, and breakable-block diagnostics are tightened.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 30 |
| `feat(...)` / `fix(...)` | 15 |
| `docs(...)` | 9 |
| `refactor(...)` | 2 |
| Date span | 2026-06-26 → 2026-06-26 |

### Major tracks

#### Scena scripting — MIR stepper interpret path, REPL, embed API

- **Phase 0** spike: introduce `mir/stepper.rs` with `Value` model, `Host` trait, `BufferHost`, and entry-function dispatch for constants, assign, CFG terminators, nota diagnostics, and `FormatString`. `salve-munde` runs in-process with no Cargo or wasm round-trip (`1181124f9`).
- **Phase A**: expand the stepper into a module with aggregates, function calls, switch, collection/convert/option intrinsics, and place projections. Wire `faber run` so single `.fab` files interpret in-process while package directories keep the compile-to-Rust path. Eight stepper fixtures cover core patterns (`961626773`).
- **Phase B**: implement `TryCall`/`ReturnError` for `fac`/`cape` and failable ⇥ functions, add remaining `MirCollectionOp` set algebra/delete/text slice, wire `processus` HAL providers (`argumenta`, `identitas`, `exi`), forward script args via `StdioHost`, and add exempla e2e harness with 152-run floor (`e6bd8861f`).
- **Phase C**: add `faber repl` (accumulating cells with MIR re-lower per line), `faber -c`/`--command` for inline stepper execution, wire `processus.lege`/`scribe`/`sedes`/`muta` with module-qualified dispatch, share `interpret_source` across run/repl/`-c` paths (`975945a6c`).
- **Phase D**: publish `faber_script` crate as the public embed API — `run_source`/`run_named`/`run_with_session` returning `ExitCode` via a trap host that captures `exi`/`abort` without terminating the embedder process. Re-export `Host`, `BufferHost`, `StdioHost`, and low-level stepper hooks (`83d0cb404`).
- **Rename** `faber_script` → `scena` (five-letter Latin name, `3aa16c247`).
- **Phase E parity**: fix `MirUnOp::Not` identity bug on bivalens (broke `fac-dum` do-while loops), teach collection `Append` to mutate copia sets, implement numerus bitwise binops/bitnot, map index assignment for tabula, and canonical `verum`/`falsum` nota output. Script e2e pass count ratchets from 152 → 154 → 158 (`d5cf034f1`, `973b70e95`).

#### Frame-gateway — stream lowering stages 1–3

- **Stage 1**: register `emitte` as lexer keyword (`TokenKind::Emitte`), keyword registry tests, stage gate recorded (`ca50d39c9`).
- **Stage 2 spec**: author delivery spec for in-process `sermo` shim (`2098e366d`).
- **Stage 2 shim**: introduce in-process `FaberSermo` helpers with concrete `Done` frames, fix `tuus-drain` newline glue after breakable scopes, add Go HIR-direct shim test (`9f9e3ec1f`). Close stage-2 gate with full validation evidence (`0f0f0111e`).
- **Stage 2 review items**: add `registry↔is_keyword` invariant test, replace non-deterministic Go frame-ID generation with atomic counter, fix missing trailing newline in `frame_shim.rs`. Record substantial items as `DEFER-024…026` (`0ee922bfd`).
- **Stage 3 lowering**: wire stream-shaped `ad` (ascii route + optional opener) and `emitte` through parser, lazy frame builtins, HIR/MIR sermo intrinsics, and `frame_shim` codegen. Legacy typed `ad` emits deprecation warning, Go driver allows stream `ad` only. 52 files, ~1261 lines added (`c200610d2`).
- **Stage 3 skeptic gaps**: align codegen with scrinium frame types — per-target breakable loops, user-to-shim scrinium conversion, partial literal defaults, valor local widening. Rust/Go smoke compile tests (`2944f7bc5`).
- **Smoke compile fix**: emit status before scrinium, place Rust frame shim helpers after builtin type declarations, default omitted union/valor fields to `FaberValue::Nihil` (`9cfa09af3`).
- **Go status deferral** (`DEFER-027`): record that Faber `status::byte`/`status::error` names collide with Go's predeclared identifiers. Root cause is Go's flat enum namespace — Latin names avoid the class. Resolution deferred to stage 4 (gateway-stream-api) alongside `DEFER-024` (`fa8890753`).

#### MIR probe naming hygiene + sexp target

- **Shared `MirNames` ledger**: `mir/names.rs` as canonical source for source function names (`incipit`, `factorial`), single-letter slot ids (`l`/`t`/`v`/`b`), and `p0` dispatch. Retire `__faber_*` and `bb` prefixes across LLVM, wasm, and sexp probe output (`2138ae202`).
- **Migrate Rust probe** to shared `MirNames`: replace `__faber_fn_*`/`__faber_local_*`/`__faber_tmp_*` with `f`/`l`/`t`/`b` names and `Block::b{N}` dispatch (`c56216a4b`).
- **Shared HIR hygiene** (`codegen/hygiene.rs`): single ledger for compiler-inserted temporaries (`s0`, `t3`, `ok`/`err`, `y0`, `g0`, etc.) — route Rust and Go emitters through it. 20 files, ~366 lines added (`9ca4f04ed`).
- **Route TypeScript** codegen through shared hygiene naming: use `CLOSURE_ITEM` (`x`) for copia set predicates and `range_cursor` (`n0`) for stepped `textus` slice filters (`ef736a868`).
- **MIR sexp probe**: wire `Target::Sexp` through `radix` and `faber` emit (`-t sexp`/`racket`/`lisp`, `.rkt` output). Lowers validated MIR to runnable `#lang racket` with block-dispatch loop and `displayln` diagnostics. Fix emitter parenthesis bugs. Exempla e2e: 57 emitted, 55 pass with Racket 9.2 (`dbf798212`).

#### Breakable blocks

- Tighten breakable-block cleanup across all codegen backends, parser, semantic passes, and exempla e2e test expectations — 62 files changed (`de520337f`).
- Record review follow-ups: `DEFER-021` (rename `BreakOutsideLoop` → `BreakOutsideBreakable`), `DEFER-022` (register breakable-blocks exempla in wasm e2e), `DEFER-023` (`fac`/`cape` err handler has no MIR lowering, overlaps `DEFER-007`) (`1268f3b05`).

### Other changes

- Author `docs/design/faber-scripting.md` (317-line design doc for interpreted execution, host contract, CLI UX, v1 subset, phases) (`be42d53f7`).
- Ground scripting design against real MIR backends — wasm already executes MIR end-to-end; stepper mirrors known-working executor. Close 5 of 6 open questions. Add maturity table across all four backends (`f6f079538`).
- Add `docs/design/target-capability-matrix.md`: support/erase/warn/reject policy per target, HIR vs MIR routing, exempla baselines (`24248a54c`).
- Add phased roadmaps for rust-canonical and go-canonical: linter/vet ratchets, easy emitter wins, architectural work — 1072 lines across 6 files (`809e349bc`).
- Clarify `rust_probe` is least developed MIR backend: add DO NOT banner pointing at wasm as the complete executing backend (`26f443811`).
- Align Phase A run wording with file-vs-dir policy (`761ef38cd`).

---

[All releases](/releases/) · [Install the current release](/start/install.html)
