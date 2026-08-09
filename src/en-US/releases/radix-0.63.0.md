+++
title = "Radix 0.63.0"
section = "releases"
order = 34
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.63.0 |
| **Tag** | `radix-v0.63.0` |
| **GitHub** | [radix-v0.63.0](https://github.com/faberlang/releases/releases/tag/radix-v0.63.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.63.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.63.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.63.0/radix-v0.63.0-aarch64-apple-darwin.tar.gz) | 2.0 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.63.0/radix-v0.63.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.63.0/radix-v0.63.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.63.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Synthetic release spanning **71 commits** (`v0.62.0..v0.63.0`, ~22 hours). Sermo
conversio materialization ships through Phase 6, the macos-arm64 host kernel gets
stdlib HAL coverage, processus.lege enforces strict env-read semantics, and the
legacy `ad` expression form reaches full compiler integration. Explicit call
type-args and tensor type-directed construction land on the language side.

### Scale
| Signal | Count |
| --- | ---: |
| Commits (no merges) | 71 |
| Date span | 2026-06-30 → 2026-07-01 |

### Major tracks

#### Sermo materialization (Phases 2–6)

- **Phase 2 — conversio materialization**: runtime helpers in `crates/faber/src/frame.rs` support `sermo ↦` vacuum, textus, octeti, valor, lista\<T\>, and scalar\<T\> conversions with typecheck validation and Rust codegen dispatch (`513e1a634`)
- **Phase 3 — inbound `tuus` stream view**: `s.tuus()` typechecks and lowers through the Rust codegen pipeline with lexical keyword registration (`ebe828584`)
- **Phase 4 — recovery coverage**: hardened runtime error handling for all materializer paths (`8f29391bc`)
- **Phase 5 — solum lege migration**: generically materialize solum's `lege` routes instead of bespoke block-local arms (`2c0bbc903`)
- **Phase 6 — deprecate block-local stream arms**: block-local `tuus<` collect boilerplate parser path deprecated in EBNF (`5b79ab96b`)
- **`sermo.meus()` skeleton**: fail-closed runtime stub typechecks like the directional view API without shipping outbound sink behavior (`a14915eda`)
- **Stdlib migration**: all norma `ad` wrappers (aleator, consolum, processus, solum, tempus) migrate from block-local collect to canonical `redde ad ... ↦ T` (`6bb83c079`); closed with a regression gate script (`60e42dbb0`)
- Factory ledger closed (`4159d056f`); sermo-norma expansion opened as follow-up

#### Host syscalls (macos-arm64 kernel)

- **Stdlib HAL coverage**: full syscall implementations for aleator (entropy, sample), consolum (console I/O), processus (args, env, exit), solum (file I/O, JSON persistence), and tempus (clock, civil time) in the macos-arm64 host kernel (`7ae7df07f`)
- **Payload contract**: factory goal locks the kernel↔frame data contract for ongoing host ABI work (`7961820f4`)

#### Processus.lege strict env read

- **Unset fails**: `processus.lege(...)` now fails on unset environment variables (aligning with solum.lege semantics); set-but-empty returns `""` (`fe88832b5`)
- **Soft read posture**: soft env reads framed as deferred design, not a missing feature (`542c136a3`)
- **Morphology design policy**: canonical `docs/design/morphologia.md` codifies naming and identifier conventions for the whole stdlib surface (`2876ed72e`)

#### Legacy `ad` expression removal baseline

- **Parse and codegen**: `ad` parsed as an expression form, `Ad` emitted in forma (author/canonical), `est non` spelling rejected with a diagnostic pointing to `non est` (`64a227240`)
- **Full compiler integration**: ad expression flows through AST, HIR, MIR, typecheck, air-purity, and Rust/Go/TS codegen backends (`14bdb697e`)

#### Explicit call type arguments

- **Syntax and lowering**: callers can spell `callee<type, ...>(args)` for direct functions, modulus-qualified calls, and receiver methods; parser uses `<...>(` lookahead to avoid ambiguity with comparisons (`7ed91d32a`)
- **Hardening**: explicit type args rejected on string/forma template applications, infer/ignotum callee paths, intrinsic methods, and partial-binding paths (`826bec73c`, `2cf47b8b0`)
- **Codegen fix**: turbofish lowered callee types now substitute generic parameter types during argument coercion (`0aef2669f`)
- **Closeout**: factory goal closed with ledger (`93fe1cc27`)

#### Tensor type-directed construction

- **`numerus.creata` / type-directed tensor init**: parser, HIR, typecheck, and Rust codegen support for constructing tensors via explicit type parameters; stepper lowers bridge intrinsics through the MIR (`ecded6bc8`)
- **Closeout**: factory goal closed with ledger (`d1f61d8fe`)

#### Rust canonical (RC) polish

- **RC-000/RC-001**: context-aware `textus` coercion policy replaces blind `.to_string()` emission, reducing redundant literal patterns 750→2 in the emit-ok corpus; `audit-rust-canonical.py` tool ships (`43d4fa96b`)
- **RC-002**: blanket `#[allow(...)]` narrowed to body-driven prelude policy — implemented then reverted (`00618660b`, `39bfee62d`)
- Go/TS emit lanes deferred; Rust `err_ty` goals closed (`2555e9116`)

#### MIR stepper width fidelity

- Integer overflow in the MIR stepper now honors declared `numerus<W>` bounds instead of evaluating everything as `i64`; closes FAO-008 parity gap between stepper and codegen (`427cf2083`)

#### Stdlib and compiler housekeeping

- **Stdlib merge follow-ups**: frame shim registration, textus literal parsing, stepper carriage for bridge intrinsics, kernel namespace cleanup (`6611fe771`)
- **Chorda guard flow**: documented stdlib guard/retine flow with expanded corpus exemplars (`8c7c1765f`)
- **Continuation clause layout**: line-start Faber continuation style adopted across all exempla and stdlib sources (`fe8a6bc2c`)
- **Module call codegen**: stabilized import-param remapping and Rust codegen module structure (`b73b6d1c6`)
- **Varia binding lint**: WARN diagnostic for unnecessary `varia` bindings (`13da8a5e6`)
- Miscellaneous: fmt warning silenced, lint gate satisfied, semantic ownership goal added, EBNF status refreshed

### Other changes

- EBNF grammar status refreshed (`80ded42fa`)
- Semantic ownership goal added with FAO-008 width-fidelity correction (`628b6ab64`, `6ed547eac`, `29e668211`)
- Generic parameter defaults goal documented (`bf6d12943`)
- HIR codegen emission needs goal added (`0ebb680e9`)
- Safetensors/GGUF breakpoint spike parked (`1db1b0295`)
- Stale factory goals and campaign statuses closed (`8f19575dc`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
