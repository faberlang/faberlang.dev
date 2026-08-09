+++
title = "Radix 0.32.0"
section = "releases"
order = 65
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.32.0 |
| **Tag** | `radix-v0.32.0` |
| **GitHub** | [radix-v0.32.0](https://github.com/faberlang/releases/releases/tag/radix-v0.32.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.32.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.32.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.32.0/radix-v0.32.0-aarch64-apple-darwin.tar.gz) | 1.1 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.32.0/radix-v0.32.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.32.0/radix-v0.32.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.32.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Release spanning **94 non-merge commits** between `v0.31.0` and `v0.32.0`.
Major themes: workspace consolidation around a single radix crate, the first Go
codegen skeleton and emitter semantics, a new CLI annotation framework, large
codegen module splits for maintainability, and a comprehensive doc-truth
refresh across the entire compiler surface.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 94 |
| Date span | 2026-04-03 → 2026-05-20 |

### Major tracks

#### Workspace consolidation

The repo was restructured from a multi-root layout (`compilers/`, `runtimes/`,
etc.) into a single radix workspace under `radix/`. Archived legacy surfaces
were pruned and the repo surface rewritten around the workspace.

- Collapse active Faber tree into radix workspace (`344680a50`)
- Rewrite repo surface around radix workspace (`0ceb72a63`)
- Remove archived legacy compiler surfaces (`3902fc8dc`)
- refactor: reorganize repo into project domains (`2719abea7`)
- Add pruning delivery plan (`caec7d9d6`)
- Add pruning archive plan (`328d282ea`)
- Plan collapsed radix workspace (`18921e569`)
- chore: scope repo checks around radix-rs (`7dc65715c`)
- chore: remove .claude/ (Claude Code local artifacts) (`fc8d93efa`)

#### Go codegen (radix-go)

A complete Go codegen skeleton was added (~2200 lines across decl, expr,
stmt, and type modules). Subsequent commits tightened lowering for optional
types, custodi blocks, maps, discerne expressions, and algebraic data type
dispatch through bound blocks. Stage A expression semantics, member map
typing, and optional ternary emission were fixed.

- feat(radix): add go codegen skeleton (`72f2bce75`)
- feat(radix-go): tighten optional and custodi lowering (`142a8474b`)
- feat(radix-go): tighten map and discerne lowering (`c10ede2bd`)
- feat(radix-go): lower ad dispatch through bound blocks (`6c635f167`)
- Implement Go ab pipeline subset (`1eec5b2f6`)
- Fix Go Stage A expression semantics (`58c1eea59`)
- Fix Go member map typing (`32b732bf5`)
- Fix Go discerne scrutinee emission (`424c0f6b8`)
- Fix Go optional ternary emission (`3f899d656`)
- Advance Go emitter semantics and update delivery plan (`471e829d6`)
- Gate unsupported Go ad and externa surfaces (`ef3e79bde`)
- docs: add Go emitter delivery plan (`45ea216cf`)
- build: make Go exempla verification package-aware (`16b634d80`)
- build: add radix-rs exempla go script (`f21f5b59d`)

#### CLI framework

A new CLI annotation framework was designed and implemented across multiple
phases: annotation syntax AST parsing, IR validation, Rust subcommand dispatch
codegen, and module mounts. The radix-rs CLI adopted clap for argument parsing
with build and targets subcommands.

- Document CLI framework rework epic (`e4a7baf79`)
- Implement CLI annotation syntax AST (`0eae9d8a4`)
- Harden CLI annotation parser tests (`47ca09ec5`)
- Define CLI IR validation phase (`8d15a0550`)
- Implement phase 02 CLI IR validation (`47920acab`)
- Harden phase 02 CLI validation (`398e81b4c`)
- Mark CLI framework phase 01 complete (`6c755436a`)
- Clarify CLI option syntax plan (`b35e06a91`)
- Clarify single-command CLI codegen plan (`123d3e3c0`)
- Implement phase 03 Rust CLI codegen (`8b5c9fccd`)
- Define subcommand CLI dispatch plan (`08063642a`)
- Implement Rust CLI subcommand dispatch (`15a2964c9`)
- Tighten subcommand dispatch phase constraints (`727d89733`)
- Prefer longest CLI subcommand match (`dae8357eb`)
- Implement CLI module mounts (`6b96bfccf`)
- Harden mounted CLI globals (`fc3eb1e82`)
- Clarify CLI module mount phase (`067173196`)
- Update CLI docs and examples (`750bfa095`)
- Document current radix CLI surface (`113bca22c`)
- Add radix-rs build and targets commands (`5a710a983`)
- Adopt clap for radix-rs CLI parsing (`5fd82b094`)
- Unify radix-rs file and package emission (`954aae071`)
- Clarify CLI packaging naming (`711ad7ecf`)

#### Refactoring: large-module splits

A coordinated large-module refactor split monolithic codegen and typecheck
modules into focused submodules across Go and Rust expression codegen,
typecheck passes, and Faber codegen. The factory plan and ledger document the
extraction strategy.

- docs: add radix large-module refactor factory plan (`397073020`)
- docs: add radix large-module refactor factory ledger (`a0e3838c0`)
- docs: clarify radix refactor extraction strategy (`7619f4f37`)
- refactor: split rust expression codegen (`34c413220`)
- refactor: split go expression codegen (`f6b2d01d2`)
- refactor: split typecheck pass modules (`4ee6a5e89`)
- refactor: split faber codegen modules (`c43689408`)
- refactor: complete expression module split (`876aaeafd`)

#### Faber codegen and parser

Improvements to Faber codegen output for canonical grammar round-trip,
spread-aware array and object codegen, and support for algebraic data types
(`ad`), non-null types, and match expressions. Parser recovery was tightened
and keyword coverage tests added. The glyph conversio syntax was adopted
as canonical.

- feat(faber): prefer glyph conversio syntax (`f9731a1d3`)
- Add Faber codegen support for ad, nonnull, and match updates (`36445c49e`)
- Add spread-aware array and object codegen (`34acc532f`)
- Improve canonical Faber round-trip emission (`31e98634a`)
- Normalize Faber codegen output for canonical grammar (`01025f2b7`)
- Separate type aliases from runtime assignment syntax (`11d98d5bd`)
- Tighten parser recovery and add keyword coverage tests (`0d06e5fdb`)
- Plan radix diagnostics delivery plan (`2c767fb3d`)

#### radix-rs code quality

Code sharing and hygiene improvements: the codegen name resolver was shared
and deduplicated, failable analysis was decomposed, and a hygiene ratchet
was added with corresponding debt reduction.

- Decompose radix-rs Rust failable analysis (`2f6011751`)
- Share radix-rs codegen name resolver (`c647cbc58`)
- Deduplicate radix-rs codegen name collection (`11263370c`)
- Refine radix-rs codegen and package compilation support (`59e6882e5`)
- chore: reduce radix-rs hygiene debt (`7a454a295`)
- test: add radix-rs hygiene ratchet (`e3928ade0`)
- chore: tighten repo housekeeping checks (`cadcee8f5`)
- Clean up radix-rs test fixture mutability (`e2faa976b`)
- chore: run housekeeping (`abdc7cd08`)

#### Documentation refresh

All compiler-facing documentation was refreshed for accuracy: structurae,
grammatica function syntax, targets, member visibility, radix package docs,
CLI docs, mechanics review baseline, and aspirational docs. Stale planning
documents were removed.

- docs: remove stale planning documents (`82b47fa1d`)
- docs: remove stale faber cli product plan (`8248cf866`)
- docs: remove completed radix refactor plan (`2473d4817`)
- docs: update radix module refactor notes (`8632a5abb`)
- Update docs for unified package emission (`5b8efbe74`)
- Clarify radix package docs (`e924bacad`)
- Clarify CLI docs as sketch (`5292bd37c`)
- Clarify aspirational execution docs (`c6513162c`)
- Clarify mechanics review baseline (`af3516d23`)
- Improve radix CLI diagnostic locations (`9226cc464`)
- Clarify member visibility docs truth (`4667bdd5d`, `3e04ea661`)
- Refresh structurae docs truth (`d6f60fc38`)
- Refresh grammatica function syntax docs (`ae10c8d9a`)
- Refresh radix target docs truth (`1e2a6856b`)
- Update radix CLI docs truth (`d8a2725dd`)
- Add futurum lexer coverage (`26832b815`)
- Add Faber language critique (`326079b1a`)
- Add dependency release age policy (`5f23ca4c9`)
- Add Faber CLI product plan (`325942f56`)
- docs: add analysis notes (`b324fcd93`)

#### Other changes

- Remove radix emit-package alias (`1b986b3ed`)
- style(radix-rs): reflow compiler formatting (`9a95c6cab`)

### Verification

| Gate | Result |
| --- | --- |
| `git log v0.31.0..v0.32.0 --oneline --no-merges` | 94 commits |
| Date span | 2026-04-03 → 2026-05-20 |

---

[All releases](/releases/) · [Install the current release](/start/install.html)
