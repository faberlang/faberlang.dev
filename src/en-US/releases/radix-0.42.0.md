+++
title = "Radix 0.42.0"
section = "releases"
order = 57
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.42.0 |
| **Tag** | `radix-v0.42.0` |
| **GitHub** | [radix-v0.42.0](https://github.com/faberlang/releases/releases/tag/radix-v0.42.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.42.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.42.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.42.0/radix-v0.42.0-aarch64-apple-darwin.tar.gz) | 1.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.42.0/radix-v0.42.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.42.0/radix-v0.42.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.42.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Synthetic release spanning **19 commits** (`v0.41.0..v0.42.0`). The tag theme is **Rust
keyword runnability factory and `sit`/binding ergonomics** — the first focused campaign
to drive Faber exempla through Rust emit, rustc, and run, paired with the introduction
of `sit` as shorthand sugar for inferred immutable bindings.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 19 |
| Date span | 2026-06-23 |

### Major tracks

#### Rust keyword runnability factory

Established and executed a factory campaign measuring Rust codegen keyword coverage
against emit/rustc/run success. The campaign ran each exemplum through three gates
(emit parity, rustc compilation, binary execution) with a live ledger and audit script.

- Factory goal, plan, baseline ledger, and `scripta/audit-rust-keyword-runnability.py`
  audit script added (`bdf4de463`)
- Rust exempla runnability audit aligned across 52 files — cleaned up exempla whitelist
  drift, fixture frontmatter, intrinsic registration, and parser/keyword tables
  (`7085c7f7e`)
- Handled errors and `lege` lowered to Rust codegen — touched the HIR, MIR, semantic
  typecheck, all backends, and the driver (`ca4de3094`)
- Async executor switched to std-only (`da0665178`)
- Inline union (tagged union) locals lowered — statement emitter, dynamic tests, exempla
  e2e (`c5f6ab96e`)
- Nullable non-null access lowered — option chain and operator emission, optional tests
  (`748d2e2d0`)
- Generic and `in` parameter exempla lowered — match expression, statement emitter,
  collection and decl tests (`9950772c9`)
- Regex literals lowered standalone — literal/format emitter, Rust prelude (`regex` crate
  integration), type mapping (`856780f18`)
- `importa` exemplum run through package path — package resolution, decl/module codegen,
  exempla e2e (`2487ebe20`)
- Naked stub bodies emitted for `externa` declarations (`f8714e9a9`)
- `lista summa` promoted from intrinsic registry to Rust codegen, with typecheck and
  collection test coverage (`035ad4fa3`)
- `operandus` exemplum executed with argv fixture — CLI operand plumbing and audit script
  wiring (`d127057f3`)
- Factory closed with adjusted denominator accounting for target parity exclusions
  (`17c4431eb`)

#### sit keyword for inferred immutable bindings

`sit name ← expr` introduced as parser sugar for `fixum _ name ← expr` (`11b6222fc`).
The implementation rejects typed, destructuring, and initializer-less forms at parse
time. Includes parser tests, EBNF coverage, canonical `examples/exempla/sit/` exempla,
and selective migrations that reduce repetition while keeping `fixum _` in teaching
contexts. Closes the sit-inferred-binding design doc.

### Other changes

- Factory plan added for core ad capabilities (`677161f0a`)
- Frame-native concurrency vision document marked as strongly theoretical / speculative
  (`e7b531431`)
- Exempla reference pack and explain-merge factory deliveries closed out with closure
  notes, final corpus counts, deferred follow-ups (`bfbca8502`)
- Retired `explain/` Markdown corpus removed entirely — exempla is now the sole
  reference source. All migration scripts, legacy redirects, and excluded-term ratchets
  consolidated in `examples/exempla/` (`9c031b595`)
- Version manifest bumped to `0.37.0` (`1428edb38`)

### Notes

- This is a synthetic history tag. The crate manifest version (`0.77.0`) is not aligned
  with the tag number.
- The Rust keyword runnability factory introduced a new cross-cutting audit pattern
  (`scripta/audit-rust-keyword-runnability.py`) for driving e2e codegen completion
  campaigns against a live ledger.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
