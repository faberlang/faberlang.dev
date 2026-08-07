+++
title = "Radix 0.25.0"
section = "releases"
order = 74
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.25.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Release spanning 43 non-merge commits between v0.24.0 and v0.25.0. This is a
significant language-evolution release focused on syntax modernization, keyword
refactoring, project cleanup, and compiler-subsystem modularization.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 43 |
| Date span | 2026-01-16 → 2026-01-17 |

### Major tracks

#### Lambda keyword refactor: `pro` → `clausura`

- The lambda keyword is renamed from `pro` to `clausura`. `pro` is now reserved
  for for-loop iteration bindings (`ex...pro`, `de...pro`, `casu...pro`). The
  initial WIP pass updated the TypeScript parser, AST, semantic, codegen, Zed
  grammar, tests, and documentation (`5c945abe9`). The follow-up completed the
  refactor in the rivus lexer/lexicon and all exempla files (`66b4ddaad`).
- Tests updated from old `pro` lambda references (`ec974eb8a`).

#### Sectional prefix syntax (`§ ex`)

- Both faber and rivus parsers accept the `§ ex "module" importa Name` syntax
  for imports. Bare imports remain valid as a non-breaking superset
  (`5f91affdb`). The entire codebase was mass-migrated to the prefixed form
  (`eefa1a11a`).

#### Language removals and deprecations

- **Disabled `fit`/`fiet`/`fiunt`/`fient` return-type syntax**: the return
  arrow (`→`) is now the canonical form. Also added `@ cursor` annotation for
  generator functions, `@ imperia` annotation parsing, keywords as method names
  in pactum declarations, and structural type-alias resolution (fixes #117,
  #226, #227, #228) (`c53e1d526`).
- **Removed `in` mutation block syntax**: the `in target { field = value }`
  form is gone; the explicit `target.field = value` is canonical (closes #222)
  (`d9199bd9f`).

#### Multi-line string literals (`"""`)

- Triple-quote syntax for multi-line strings in both faber and rivus lexers.
  Embedded newlines are preserved; no escape sequences needed for internal
  quotes (`44e017e90`).

#### Auto-wrap string literals in `scribe`/`vide`/`mone`

- The faber parser automatically wraps string literals in `scribe`, `vide`, and
  `mone` statements as `scriptum("…")` expressions. The `§` placeholder count
  determines how many trailing arguments are consumed (`3b13c0d60`). The rivus
  parser mirrors this behavior (`358ca3bd9`). Existing callsites across the
  codebase were simplified to the new sugar form (`5fca4bf62`).

#### `tacet` keyword for explicit empty blocks

- Added `tacet` keyword support to the faber parser and rivus compiler,
  providing an explicit no-op statement for empty blocks (`38b85d961`,
  `755a145e3`).

#### `nihil`/`nonnihil` null-check operators

- Added `nihil` and `nonnihil` as unary operators for null checks, plus a
  `--no-typecheck` build flag (`21ca4f718`). Updated rivus semantic errors for
  these operators (`ed6c82b7d`). Added compiler warning S018 for `== nihil`
  / `!= nihil` patterns, guiding users toward the preferred unary forms
  (`b8d6e9845`).

#### `§` annotations on Programma AST

- Section annotations (`§`) are now accumulated during parsing and stored on
  the Programma AST node instead of being discarded. Enables dependency
  resolution and build-config downstream features (closes #215) (`dbe0cdad4`).

#### Shared codegen extraction (#119)

- Extracted target-agnostic codegen for `si`/`dum` handlers into
  `shared/si.fab` and `shared/dum.fab`, with `ScopusSyntaxis`, `Generans`,
  `Revocata` pactum infrastructure (`9ce52c4a6`).
- Extracted `shared/elige.fab` for if/else chain generation from `elige`
  expressions, unifying Go output with TypeScript (`7206a38f8`).
- Extracted `shared/iteratio.fab` for range-loop codegen (`genAmbitusIteratio`),
  with new `syntaxis` fields for `forVarDecl`, `forVarAssign`, `habetAsync`
  (`436a9cedf`).

#### Standalone test runner

- Self-contained test harness with annotation-based configuration (`@ tag`,
  `@ temporis`, `@ omitte`, `@ solum`, `@ repete`, `@ fragilis`, `@ requirit`,
  `@ solumIn`). Adds `rivus test` command with `--tag`, `--exclude`, `--only`
  filter options and `--strip-tests` for production builds. Works without
  Jest/Vitest dependencies (`bf1c5e0de`).

#### Rivus compiler refinements

- **Flatten deeply nested conditionals**: reduced nesting from 5–6 levels to
  2–3 in semantic and codegen paths using guard clauses (fixes #122)
  (`88179ad37`).
- **Consolidated body parsing into `parseCorpus` helpers**: removed
  `parseCorpusBrevis`, added `parseCorpusAutSententia`, removed undocumented
  `fac...fine` legacy block syntax (closes #220) (`de450b525`).
- **LPAREN lookahead for keyword disambiguation**: `scribe("hello")` is now
  correctly parsed as a function call rather than a keyword statement (fixes
  #195) (`e2587e446`).
- **`figendum` for async declarations**: replaced explicit async handling in
  CLI commands with `figendum` (`459acd751`).
- **Rivus as primary compiler**: documentation updated to present rivus as the
  primary compiler for new development, with faber reserved as a bootstrap
  compiler (`86cf46600`).

#### Bug fixes

- Parameter alias (`ut`) now correctly registers both names in scope (fixes
  #225) (`f385e0b29`).
- `ego` returns instance type instead of metatype inside `genus` methods,
  fixing fluent/builder patterns (fixes #224) (`f12682d63`).
- Destructuring patterns (`ex obj fixum name, age`, `fixum [a, b, c] = arr`)
  now register all bound identifiers in scope, including aliases, rest
  patterns, and placeholders (fixes #221) (`79e3fc34f`).
- Regex flag parsing uses inline syntax `sed "(?i)pattern"` instead of
  consuming the next token as a flag (fixes #223) (`216b6f665`).
- Namespace kind preserved for HAL pactum imports in faber semantic/codegen
  (`6a7eeb573`).

#### CLI and build system

- `--strip-tests` flag for faber CLI to strip `probandum`/`proba` blocks from
  production builds (`d3b9c7f00`).
- `--faber`/`--rivus`/`--artifex` flags for selective stage builds in the
  build script (`4b7740af2`). The `build:exempla` script renamed to `exempla`
  (`cca978258`).
- Removed `bun run` wrappers; compilers run directly from `opus/bin/*`
  binaries. The build chain is now `faber source → opus/bin/faber → rivus
  source → opus/bin/rivus` (`9df83b609`).

#### Project cleanup

- Removed `consilia/` (design docs) from the repository entirely
  (`9c5ee9e21`).
- Removed `coreutils/` (standalone binaries) from the repository entirely
  (`b51543ea6`).
- Removed `editors/zed` (Zed grammar and extension) from the repository
  entirely (`65d3aaa55`).
- Removed `archivum/` (historical design artifacts) from the repository
  entirely (`304b51076`).

#### Documentation

- Updated `AGENTS.md` with rivus as primary compiler, correct project layout,
  agent command syntax, and build-chain prerequisites (`c11526342`,
  `02d365bdb`, `579085950`, `86cf46600`, `9df83b609`).
- Fixed documentation errors: `discerne` uses `casu` not `si`, stale
  references to `consilia/` and old codegen filenames (`6ac9031f1`).

---

[All releases](/releases/) · [Install the current release](/start/install.html)
