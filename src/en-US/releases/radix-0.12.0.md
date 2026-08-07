+++
title = "Radix 0.12.0"
section = "releases"
order = 87
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.12.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Small but focused release completing **Phase 0** of syntax modernization —
converting every `elige/discerne si` arm across the parser, semantic analyzer,
and codegen to `casu`/`ceterum` syntax — alongside new range-containment
(`intra`) and set-membership (`inter`) operators.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 15 |
| Date span | 2026-01-01 → 2026-01-02 |

### Major tracks

#### Phase 0: Syntax Modernization

The primary theme of this release. All remaining `elige`/`discerne` (`si`-armed)
statements in the `fons-fab/` self-hosted compiler sources are converted to
`casu` syntax (`casu` replaces `elige` / `discerne si`, `ceterum` replaces
`secus` as the default arm). Coverage spans 21 files and ~350 lines across:

- **Parser** — nucleus, errores, sententia/fluxus, sententia/varia
  (`49fd9d05f`)
- **Semantic analysis** — index, nucleus, typi (20+ type-equality checks),
  expressia/* (23 expression analyzers), sententia/* (22 statement analyzers)
  (`49fd9d05f`)
- **Codegen** — TS type annotation generation, expression generators,
  statement generators (`49fd9d05f`)
- **Lexicon/lexor** — keywords `casu`, `ceterum`, `intra`, `inter`, `finge`
  added; lexicon and lexor switched from `si` to `casu` (`3eb13091c`)
- **Original non-self-hosted `fons/` compiler** — all `elige`/`discerne si` in
  parser, AST, tests, and exempla replaced with `casu`/`ceterum`
  (`c217493fa`)
- **Discretio pattern-matching tests** — updated to use `casu` syntax
  (`c9cf75add`)
- **Bootstrap plan** — rewritten with phased approach and syntax-modernization
  priorities (`5ea0b6430`); historical content stripped, actionable info
  retained (`7d6eb7721`)

Verification: `bun run faber compile fons-fab/cli.fab` succeeds, proving the
`fons/` compiler can parse all `fons-fab/` self-hosted source.

#### Annotation refactor

Annotations changed from a `modifiers[]` interface to a single
`name + argument?` form. Each `@` line carries exactly one annotation; the
parser validates that the name is on the same line as `@`. Codegen helpers
check `ann.name` instead of `ann.modifiers`, and the Fab codegen emits one
annotation per line. Design docs for endpoint routing (`ad-annotatio.md`) and
set membership (`si-inter.md`) added alongside. (`4e35f7aff`)

#### `intra` / `inter` operators

New binary operators at comparison precedence:

- **`intra`** — range containment: `x intra 0..100` → `(x >= 0 && x < 100)`
- **`inter`** — set membership: `x inter [1, 2]` → `[1, 2].includes(x)`

Implemented across all six codegen targets (TypeScript, Python, Rust, C++, Zig,
Fab) with semantic validation (`intra` requires a range, `inter` requires an
array). Example files added for both operators. (`4ebac0b16`)

Follow-on work includes YAML test coverage with 5 test cases × all 6 targets
(25 new tests) (`8ec7bfff4`), `GRAMMAR.md` and `grammatica` documentation
updates (`f07a876e8`, `b38a93c88`), and promotion of design specs to `completa/`
(`c4d45058f`).

#### `casu` / `ceterum` design docs promoted to `completa`

The `casu-ceterum.md` design document moved from `consilia/futura/` to
`consilia/completa/`, reflecting full implementation in `c217493`.
(`6e6dfadfe`)

### Other changes

- **AGENTS.md** — Concise-ified and replaced with a symlink to `CLAUDE.md`
  (`d9e925911`)
- **Planning docs** — Updated `GRAMMAR.md`, `grammatica/regimen.md`, and added
  design docs for `discernere-multi` and `casu-ceterum` (`3a9afe8f8`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
