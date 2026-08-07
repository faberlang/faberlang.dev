+++
title = "Radix 0.79.0"
section = "releases"
order = 20
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.79.0 |
| **Tag** | `radix-v0.79.0` |
| **GitHub** | [radix-v0.79.0](https://github.com/faberlang/releases/releases/tag/radix-v0.79.0) |
| **Published** | 2026-07-31 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.79.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.79.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.79.0/radix-v0.79.0-aarch64-apple-darwin.tar.gz) | 4.3 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.79.0/radix-v0.79.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [radix-v0.79.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.79.0/radix-v0.79.0-x86_64-unknown-linux-gnu.tar.gz) | 4.6 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.79.0/radix-v0.79.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.79.0/radix-v0.79.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.79.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Minor release spanning **81 commits** (`v0.78.0..v0.79.0`, 2026-07-30→2026-07-31).
Headline: **contextual keywords — tokenless parser surface** (Batches A–G of the
contextual-keywords campaign), plus the corpus split into `radix/corpus` with
proba runners, the six-stage `scripta/test` ladder, cross-backend codegen
fixes, and clippy pedantic debt clearing.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 81 |
| `feat(...)` commits | 17 |
| `fix(...)` commits | 21 |
| `docs(...)` commits | 19 |
| `test(...)` commits | 1 |

Reconstruct the full log:

```bash
git log v0.78.0..v0.79.0 --oneline --no-merges
```

### Major tracks

#### Contextual keywords — tokenless parser surface (Batches A–G)

The contextual-keywords campaign is complete: every batch-table word now has
`token_kind None`. There is no global reserved keyword table — the lexer emits
identifiers for all words and the parser recognizes keywords by spelling in
grammar position, resolving the active reader-locale surface spelling. A word
is only a keyword in the grammar slot where it is expected; everywhere else it
is a free identifier.

| Batch | Surface migrated to tokenless |
| --- | --- |
| A | `modulus` / `iuncta`, with loud Latin fallback |
| B | Builtin I/O, registry-driven prefix lookahead |
| C | Literals `verum` / `falsum` / `nihil`, spelling-aware prefix detection |
| D | Logical operators `aut` / `et` / `non` / `est` / `vel`, annotation slot fix |
| E | Declaration introducers, spelling-aware statement dispatch |
| F | Control flow, spelling-aware keyword groups |
| G | Tokenless long tail; all batch-table words `token_kind None` |

Supporting work: contextual slot owners for Batch A keywords with tokenless
rows enforced non-Global; tests prove migrated keywords work as contextual
identifiers across use positions. Post-campaign fixes landed: exact declared
spellings skip READER002 suggestions, and localized `est <type>` routes via
`reader_type_latin_keys`.

#### Clean break: retired statement/token surfaces removed

Per `docs/factory/retired-statement-token-removal/goal.md`, `tempta`, `demum`,
`emitte`, the sed identifier-spelling check, the dead `pro` token, and the
retired block-string spellings (`❝...❞`, `"""`) no longer have keyword, token,
grammar, locale, corpus, or diagnostic roles. Each spelling is an ordinary
identifier now and fails generically; `❝` and `"""` fail as ordinary lex
errors. Guillemets `«...»` remain the only block-string spelling. EBNF.md,
localized EBNF, reader packs, corpus, and EBNF_MATRIX.md were cleaned in the
same pass.

#### Corpus split & proba

Single-file language exempla are now hosted in-tree under `radix/corpus` (the
corpus-split goal moves package-shaped corpora to sibling `examples/`). A
target-neutral proba inventory with a MIR stepper case runner lands tier-one
proba on logic, binding, and control demos; `radix test` runs single-file MIR
stepper proba. EBNF vocabulary and matrix are radix-only language law, and
`EBNF_MATRIX.md` was regenerated for the radix/corpus join.

#### Six-stage `scripta/test` ladder

`./scripta/test` is now a progressive six-stage ladder — gate → lint → proba →
unit (nextest) → matrix → parity — ordered cheap-first so fast lanes gate
before slow ones. New aliases: `--check` (stages 1–3), `--release` (stages 1–4
plus all e2e targets), `--stage`, and `--e2e` target selection (e2e is no
longer a stage). CI is thinned to the scripta ladder: main push →
`--stage 1-4`, tag push → `--full`.

#### Cross-backend codegen & semantic fixes

- **TypeScript**: cross-file `DefId` resolution from sibling module imports;
  valor display and async entry for `for-await`.
- **Go**: blank-assign pure value expression statements.
- **Rust**: parenthesize numeric methods; Faber-`nihil` options.
- **Semantic**: lint warnings surface as non-fatal findings; diagnostics bag
  renamed from `errors`.
- Test temp data stays under the cargo-managed target tree.

#### Lint & polish

Clippy pedantic debt cleared across the codegen crates (including
`radix-mir-llvm` emit test fixtures); probe tests migrated from the radix
façade into `radix-mir-llvm/emit/`; inline tests extracted across
`radix-mir-stepper`, `radix-lower-ts`, `radix-codegen-rust`, `radix-mir`, and
the radix façade. New tooling: `scripta/release-stats.sh` (per-tag tests vs
LOC series).

### Breaking / author-visible

| Change | Migration |
| --- | --- |
| `tempta`, `demum`, `emitte`, `pro` are ordinary identifiers | Remove retired statement/token spellings; only `cape`-style active surfaces remain |
| Block strings are guillemets `«...»` only | `❝...❞` and `"""` fail as ordinary lex errors |
| Keywords are contextual, not globally reserved | A word is only a keyword in its grammar slot; elsewhere it is a free identifier |
| `./scripta/test` e2e is not a stage | Use `--e2e <targets>` or `--release` (stages 1–4 + all e2e) |

### What is NOT included

- No new language features beyond the contextual-keywords and clean-break
  surfaces above.
- No change to the MIR/GPU target posture; Metal factory campaigns remain
  paused.
- No changes to the `faber` product CLI surface (sibling repo release).

### Version alignment

| Item | Value |
| --- | --- |
| Source tag | `v0.79.0` |
| `crates/radix` version | `0.79.0` |
| Public artifact tag | `radix-v0.79.0` on `faberlang/releases` |
| Workspace members bumped | all `0.78.0` → `0.79.0` (hygiene-ratchet stays `0.1.0`) |

### Verification (pre-release)

Recorded on the release candidate tree (2026-07-31):

| Gate | Result |
| --- | --- |
| `cargo build --locked --release -p radix --bin radix` | pass |
| `radix --version` (release binary) | `radix 0.79.0` |
| `cargo nextest run` | pass — 5251 passed, 154 skipped |

### Publish

1. Bump all workspace crate versions `0.78.0` → `0.79.0` (not hygiene-ratchet).
2. `cargo update` so `Cargo.lock` matches manifests.
3. Verify locked release build + nextest.
4. **Single commit** with version bump + lockfile (+ this notes file if still dirty):
   `release(radix): v0.79.0`
5. Annotated tag: `git tag -a v0.79.0 -m "Radix v0.79.0"`
6. Push: `git push origin main && git push origin v0.79.0`
7. Monitor: `gh run list -R faberlang/radix --limit 5`
8. Confirm `faberlang/releases` publishes `radix-v0.79.0` multi-arch archives.

**Never** tag a commit whose `Cargo.lock` is stale relative to the bumped
manifests — CI uses `cargo build --locked`.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
