+++
title = "Radix 0.47.0"
section = "releases"
order = 50
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.47.0 |
| **Tag** | `radix-v0.47.0` |
| **GitHub** | [radix-v0.47.0](https://github.com/faberlang/releases/releases/tag/radix-v0.47.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.47.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.47.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.47.0/radix-v0.47.0-aarch64-apple-darwin.tar.gz) | 1.8 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.47.0/radix-v0.47.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.47.0/radix-v0.47.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.47.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Dense single-day release completing the MIR staged lowering campaign across
Stages 3–6. Stage 3 pushes coverage from 174→184 exempla; Stage 4 builds the
Wasm/LLVM e2e host infrastructure; Stage 5 lands callable, provider, and async
surface lowering; Stage 6 unifies two-backend emission for all landed MIR
surfaces. Backend floors (Wasm + LLVM) are pinned, evidenced, and ratcheted.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 26 |
| `feat(...)` commits | 7 |
| `fix(...)` commits | 4 |
| `docs(...)` commits | 7 |
| `Polish` commits | 4 |
| `chore(...)` commits | 2 |
| Date span | 2026-06-25 → 2026-06-25 |

### Major tracks

#### Stage 3: MIR lowering coverage (M-002…M-008)

Five commits advancing MIR exempla coverage from 174/210 through 184/210, with
call/aggregate repair, iterator/collection lowering, type zero-init policy, and
struct field materialization.

- M-002 call/aggregate repair — 174/210 exempla lowered (`003945b5e`)
- M-003/M-007/M-008 coverage — 183/210 exempla lowered (`e7dc66a55`)
- M-007 type zero-init policy + verification evidence (`88b47ae13`)
- Stage 3 close-out: unify struct field materialization and MIR evidence
  script (`3b53b8dfb`)
- Fix MIR evidence capture honesty and strengthen sponte struct test
  (`e74df14e9`)

#### Stage 4: Wasm/LLVM backend e2e infrastructure

Ground-up e2e test harness for both Wasm and LLVM backends, including a Wasm
stub host binary, LLVM C runtime, Wasm binary utilities, staged evidence
capture script, and complete toolchain wiring — replacing the old monolithic
`wasm_host` module.

- Wasm/LLVM backend e2e infrastructure (+1923/−618 lines, 32 files)
  (`12a75bacb`)
- `capture-stage4-evidence` verifier script (`736d902b6`)
- Polish: drop dead toolchain param and legacy tier map; fix EOF hygiene
  (`4b818e40c`)
- Documentation: on-demand stub host build in `locate_stub_host_binary`
  (`1c2f08f14`)

#### Stage 5: Callable, provider, and async surface lowering

Lowering support for three new MIR surface areas — `callable` (closures,
function references), `provider` (trait object dispatch), and `async` surface
— plus flattening of the `lower_call` dispatch and hardened `ad` binding
recovery.

- Stage 5 MIR lowering for callable, provider, and async surfaces
  (+622/−180 lines, 27 files) (`17f321b33`)
- Wire Stage 5 callable/ad/cursor lowering correctly (`5e4b7c13e`)
- Align Stage 5 delivery spec with 194/210 harness (`996a1c893`)
- Flatten `lower_call` dispatch, harden ad binding recovery, fix EOF hygiene
  (`8f7ddd364`)

#### Stage 6: Unified two-backend emission

Emission for all landed MIR surfaces unified across Wasm text and LLVM text
backends. Both emitters see substantial additions (~887 lines to Wasm text,
~573 to LLVM text). Backend floors are pinned and verified through evidence
capture.

- Stage 6 unified two-backend emission (+1684/−121 lines, 7 files)
  (`9e223d49a`)
- Close Stage 6 skeptic gaps for emitters and harness (`487013f8f`)
- Print pinned e2e floors in harness stdout (`82a83cef0`)
- Add Wasm aggregate e2e floors and ratchet Stage 6 exempla (`91d75501b`)
- Redefine Stage 6 as unified two-backend emission delivery (`2982f3b0d`)
- Reconcile CAMPAIGN rows with delivered Stage 6 work (`0b81d395c`)

#### Campaign documentation and planning

- Add `DEFERRED.md` rolling inventory, cross-link from CAMPAIGN (`835633bf7`)
- Tighten Stage 7 to the genuine loop-fixpoint gap (`7e2190a66`)
- Close out MIR goal with Wasm/LLVM continuation plans (`f47af1cab`)

### Polish and hygiene

- Dedup nullable-inner traversal and nuntius field name in `mir/semantic`
  (`23ea6d8df`)
- Restore `lower_dum` doc, document `lower_loop_expr` in `mir/lower/control`
  (`94f215d36`)
- Fix EOF hygiene in `intrinsics/mod.rs` and `mir/lower/item.rs` (`7782e7846`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
