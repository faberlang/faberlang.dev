+++
title = "Radix 0.41.0"
section = "releases"
order = 59
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.41.0 |
| **Tag** | `radix-v0.41.0` |
| **GitHub** | [radix-v0.41.0](https://github.com/faberlang/releases/releases/tag/radix-v0.41.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.41.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.41.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.41.0/radix-v0.41.0-aarch64-apple-darwin.tar.gz) | 1.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.41.0/radix-v0.41.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.41.0/radix-v0.41.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.41.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Minor release spanning **32 commits** (`v0.40.0..v0.41.0`). Three intersecting
campaigns deliver the `+++` TOML frontmatter pipeline (replacing legacy `§`
line-start directives), merge the `explain/` corpus into exempla with
educational tours and parity frontmatter, and extract the exempla reference
pack to a disk-backed format with Homebrew distribution.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 32 |
| `feat(...)` commits | 5 |
| Date span | 2026-06-22 → 2026-06-23 |

### Major tracks

#### `+++` frontmatter pipeline (Stages 1–5)

Replace `§` line-start directives with a shared `+++` TOML-delimited file
header parsed before lexing. The pipeline spans the compiler splitter, typed
`FileFrontmatter` deserialization, `SourceFile` raw/body split, removal of
the old `§` lexer/parser/syntax paths, and package-build consumption with
manifest merging and test selection.

- Shared `+++` frontmatter splitter with strict line-1 opening, BOM rejection,
  and empty-body support (`8ee7fba10`)
- Wire into `SourceFile` and driver: typed v1 deserialization, peel-before-lex,
  frontmatter in `radix inspect` JSON output (`b2a9aaa45`)
- Remove line-start `§` directives: lexer tokens, parser `§`-based module
  declaration, syntax AST nodes (`6c3514370`)
- Consume `+++` frontmatter in package builds: per-file peel before parse,
  modulus module path handling, manifest override rejection, entry
  sectio/probanda test selection (`76412ae07`)
- Complete Stage 5 grammar and explain alignment (`4e04a0354`)
- Polish: centralize PARSE052 frontmatter diagnostics in `source.rs`
  (`3a9c8e38b`); extract manifest conflict helper and tighten entry merge
  (`07b952403`); fix catalog comment after `§` removal (`4c1bb4bfc`)

#### exempla/explain corpus merge (Phases 1–7)

Fold the standalone `explain/` Markdown corpus into the exempla tree, using
the new `+++` frontmatter to carry explain-parity metadata. Add keyword-dir
smoke exempla, operator-family tours (`operatores/`), literal and primitive
tours (`literalia/`, `intrinseca/primitiva.fab`), deeper CLI exempla, and a
`meta/` family. Freeze the explain corpus, generate a canonical
`index.toml`, and mark exempla as the source of truth.

- Generic TOML frontmatter container for exempla explain-metadata
  (`bd15ad082`)
- Inject explain-parity `+++` frontmatter across 90+ exempla files
  (`38b7892f0`)
- Keyword-dir smoke exempla to fill explain coverage gaps (`bc148223e`)
- `operatores/` tours: bitwise, comparison, logic, optional/nonnull chains,
  function types, metadata, control, range glyphs (`81e4bd0f0`)
- `literalia/` (boolean, nihil, string, block-string, regex, textus) and
  `intrinseca/primitiva.fab` tours (`5dc7febb6`)
- CLI deep dive (`versio`, `optio`, `imperium`, alias) and `meta/` family
  (`9519b7074`)
- Freeze explain corpus, canonical `index.toml` (2306 entries), website
  export plan (`2044a1cb4`)

#### Disk reference pack (Stages 1–6)

Extract the exempla reference pack from a compile-time binary embed to a
versioned disk layout with `PACK.toml` metadata, a TOML index and legacy
redirects, a fab-parser for exempla frontmatter, and a disk-backed `explain`
CLI. Publish `faber-reference` tarballs from CI with Homebrew integration.

- Stage 1: Pack assembler (`assemble-reference-pack.py`) and CI ratchet
  (`2ff916000`)
- Stage 2: Disk resolver, index/redirect parsing, term indexes, path
  validation for Pack and Repo layouts (`2aeb1b4b0`)
- Stages 3–4: Fab parser for exempla frontmatter, disk-backed `explain`
  CLI (`4bf29ac7d`)
- Stage 5: Remove compile-time `build.rs` embed and Markdown-specific parsing
  (`5bb3e9bee`)
- Polish: loader imports/docs (`4a7d8fe15`); shared test support (`4e140c3a7`);
  index scan loop cleanup (`c97c1bc02`)
- Stage 6: Release workflow publishes `faber-reference` tarballs, version-skew
  check at explain load, Homebrew formula refresh script (`4d3742497`)

#### Exempla corpus expansion and hygiene

Broaden exempla coverage with new files, `.expected` sidecars, and harness
metadata ratchets. Normalize file headers to a canonical template, add
educational comments across the full corpus, and redesign stdout contracts
for cross-target (Rust/Go) parity.

- Hygiene pass: coverage gaps, stdout contracts, file renames, removed stale
  exempla (`3e83d9658`)
- Harness metadata ratchet for Rust, Go, and Wasm (124-file suite green)
  (`2fc853bf7`)
- Phase 5: secondary coverage for cura, externa, functio, integratio, octeti,
  probandum, promissum, tacet (`52d6275af`)
- Redesign deferred stdout contracts: scalar checks replace native list/map
  debug printing for cross-target `.expected` sharing (`ef43bb872`)
- Normalize all exempla file headers to canonical template (`5be813381`)
- Add educational comments across the full corpus (`db0c2e2e4`)

### Other changes

- `ut` aliases on `discerne` variant payload bindings: parse `fixum field ut
  alias` in pattern arms, resolve/lower through HIR/MIR, emit Rust/Go field
  renames (`b638e9620`)
- Align README and EBNF with current compiler contract: correct legacy
  error-handling guidance, add missing keyword entries, drop stale harness
  scoreboard (`b9662ae4c`)
- Canonicalize array types on `lista<T>`, align EBNF with parser
  (`b93dd672b`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
