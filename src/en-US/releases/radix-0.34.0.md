+++
title = "Radix 0.34.0"
section = "releases"
order = 65
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.34.0 |
| **Tag** | `radix-v0.34.0` |
| **GitHub** | [radix-v0.34.0](https://github.com/faberlang/releases/releases/tag/radix-v0.34.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.34.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.34.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.34.0/radix-v0.34.0-aarch64-apple-darwin.tar.gz) | 981.0 KB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.34.0/radix-v0.34.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.34.0/radix-v0.34.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.34.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

This release covers the initial **faber/radix tool split**, the **build pipeline** (phases 0–7) and **test runner** (phases 1–6) for the new `faber` CLI, the **glyph token clean break** that migrates ASCII compound operators to Unicode glyphs, and the **`faber explain`** command with an indexed corpus, search, and renderer.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 54 |
| Date span | 2026-05-21 → 2026-05-21 |

### Major tracks

#### Faber/Radix tool split

- Split the `faber` project tool from the `radix` compiler binary, establishing separate CLIs with distinct responsibilities (`docs/` plan at `5ee761684`, refactor at `7b95b150a`)
- Added a `[faber]` TOML package manifest schema for packages (`7c8c919a2`)

#### Faber build tool evolution (phases 0–7)

Multi-phase implementation of a full `faber build` pipeline backed by generated Rust crates and Cargo, planned at `2af9df498`:

- **Phase 0:** Preflight and baseline capture (`e7f101a4f`)
- **Phase 1:** Build layout model — `BuildLayout`, `discover_build_layout`, non-negotiable sibling directory contract (`0f171704e`)
- **Phase 2:** Generated Rust crate emission — writes `target/faber/Cargo.toml` + `src/main.rs` per the phase-1 layout (`992ed319b`)
- **Phase 3:** Cargo backend invocation — `invoke_cargo_build` spawns `cargo build` with exact `--manifest-path` / `--target-dir` (`c51e67300`)
- **Phases 4–7:** `--release` mode, `faber run` (always builds incrementally, forwards args + exit code), docs alignment, full validation gate (`846ce6b94`)
- **Phase 6 (final pass):** Help text, README, targets doc, and manifest documentation updated (`88ca44595`)

#### Faber test runner evolution (phases 1–6)

Multi-phase implementation of `faber test` backed by Cargo, planned at `84a813614`:

- **Phase 1:** Minimal `faber test` replacing the stub with `compile_package` → `emit_generated_crate` → `invoke_cargo_test` — passes smoke fixtures for passing, failing, ignored, and suite packages (`08d11d800`)
- **Phase 2:** Test ergonomics — positional FILTER, `--exact`, `--nocapture`, `--test-threads` forwarded to the Rust harness (`e8d52f9e3`); phases 2–3 spec at `670e196d7`
- **Phase 3:** Ignored test execution — `--ignored` and `--include-ignored` flags with Clap conflict rejection (`17c27bb99`); implementation ledger and gates recorded at `68b7f8404`
- **Phase 4:** Test metadata model — `solum`/`tag` annotation support (`a9bff8652`, `1cb23b69c`)
- **Phase 5:** Test selection — filter by metadata annotations (`5c22a8800`, `9d4c57288`)
- **Phase 6:** Scope tightener, behavior documentation, and docs polish (`1cef058e4`, `80bc6e87e`, `740e1e370`); plan tightened at `ff2568c11`
- Fixture contracts specified and canonical equality used in test fixtures (`98def597c`, `7408fff72`)
- Plan closed for v0.34 (`53b7d1492`)

#### Glyph token clean break (phases 0–5)

Migration from ASCII compound operators to canonical Unicode glyphs across the entire compiler and documentation surface:

- **Phase 0:** Inventory ledger of all old ASCII operator tokens (`b47b3edb0`)
- **Phase 1:** Lexer front-end break — removed `==`, `!=`, `<=`, `>=`, `->`, `+=`, `-=`, `*=`, `/=`, `==`, `===`, `!==` branches from `scan_operator`; glyphs (`≡`, `≠`, `≤`, `≥`, `→`, `⊕` etc.) remain as sole producers of compound tokens (`7de699711`)
- **Phase 2:** Compiler test migration — all old operator sources updated, 268/268 tests pass (`9b8c8f485`)
- **Phase 3:** Examples migration (`726de5850`)
- **Phase 4:** Grammar and docs migration (`58f553e64`)
- **Phase 5:** Negative guardrails, lexer rejection tests, residue clean (`271ad4085`)
- Completion pass: canonical `→` in 15+ `explain/*.md` files, operatores doc fix, factory bookkeeping (`2c303732c`)
- Plan at `cf661c76b`

#### `faber explain` command

A new `faber explain` CLI command with a corpus of reference documents, search, and formatted output:

- Command implementation at `047e2bd3c`, planned at `2e5543b8f`
- Coverage completion plan (`e7742bfcf`), expanded corpus including slug filename conventions (`5c5b94505`, `ccac83e30`)
- Renderer and search planned at `f64ba916a`, implemented with grouped list output, section-aligned display, and summaries in list view (`6b4034bb8`, `22f0d67b3`, `5c5daef19`, `eceb8be7a`)
- Polished reference output, hidden repo example paths, improved missing-query help (`79b3600de`, `557310fdb`, `df3933ca0`)
- Legacy filename adjacency for explain entries (`7e027c2a0`)
- Glyph clean break aligned with explain coverage (`25a8c4eac`)
- `faber help` updated with examples (`b8e68bd7b`)

### Other changes

- Added automation example skeleton (`f04eb96bf`) and documented gaps (`59b1965a0`)
- Added package-aware `faber check` command (`88d356dac`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
