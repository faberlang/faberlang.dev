+++
title = "Radix 0.26.0"
section = "releases"
order = 71
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.26.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Two-day release spanning **39 commits** — a compact burst focused on nanus (a
new Faber compiler prototype), unifying binding syntax under `fixum`/`varia`,
revamping the CLI annotation toolkit, adding `rivus run`/`rivus fetch`, and
cleaning up the import/collection DSL.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 39 |
| Date span | 2026-01-17 → 2026-01-18 |

### Major tracks

#### nanus: minimal Faber compiler prototype

A new TypeScript compiler (~2.2k lines) targeting the 84 features rivus actually
uses (vs. faber's 139). The prototype was progressively extended across several
commits in this release.

- Add minimal Faber compiler prototype (`fons/nanus/`) with AST, lexer, parser,
  emitter, and CLI (`5e7bde28d`)
- Extend parser for rivus compatibility: import resolution, loop/cura/ergo parse,
  annotation support (`5e95fbc38`)
- Add triple-quote (`"""`) multi-line strings with leading/trailing newline
  stripping and type-first variable declarations (`fixum ignotum name`),
  then rewrite `rivus/cli.fab` from declarative to procedural style using
  `@ externa` + `process.argv` (`89fc1d4c5`)
- Complete rivus compilation support — all 135 files compile (`b389971fa`)
- Fix multiple codegen improvements: `@ publica` extern functions, ambient
  externa declarations, `quidlibet` → `any` mapping, operator precedence fixes
  (`52d86e6b3`)
- Add README documenting nanus purpose, architecture, and key design decisions
  (`071b43c12`)

#### fixum/varia binding unification

Replaced `pro`/`fit`/`fiet` across all binding contexts with `fixum` (immutable)
and `varia` (mutable), making mutability explicit in loop bindings, `cura`
bindings, and variable declarations. The old `fit`/`fiet`/`fiunt`/`fient`
keywords are removed from binding contexts (async returns deferred).

- Mass replace `pro` with `fixum` across 69 rivus source files (`975fc2659`)
- feat(rivus): Unify binding expressions with `fixum`/`varia` in loops, `cura`,
  and AST — add `mutabilis` field, codegen `let`/`const` (`c1ef07dea`)
- feat(faber): Same unification in faber parser, AST, and codegen (`85718c903`)
- Support array destructuring in bindings (`492d5fa88`)

#### CLI annotation toolkit

A coordinated faber+rivus change set introducing `@ optio` with boolean flag
support, `@ operandus ceteri` for variadic positional arguments, and
`optiones <name>` bundles that produce `Map<string, string>`.

- feat(rivus): Parse CLI annotations: `@ optio`, `@ operandus` (`b6fd0ec2e`)
- feat(rivus): Add new `@ optio` syntax and `optiones` modifier (`2e1248aa3`)
- feat(cli): `@ operandus ceteri` (variadic args) and `optiones` bundle for
  subcommands — help generates `[files...]` notation (`abc657d66`)

#### rivus run / fetch commands

- Add `rivus run` for `§ scriptum` build scripts — on-demand compilation to TS
  and execution via Bun (`e8b789696`)
- Add `rivus fetch` for GitHub dependency caching — resolves git refs to SHAs,
  downloads tarballs to `~/.cache/faber/`, content-addressed dedup, `--force`
  and `--json` flags (`27c53b22a`)

#### rivus language fixes

- Normalize visibility annotations to `@ publica` (replaces `@ publicum`/`@ publicus`)
  (`edd652606`)
- Remove `de` keyword from `novum` expressions — `novum Foo { }` not
  `novum Foo de { }` (`061b71105`)
- Replace `secus si` with `sin` (closes #244) (`19c206f88`)
- Fix `secus`/`ceterum` to require braces or `ergo` — prevents ambiguous
  fallback branches; add parser errors P108 and P109 (`b5f9ac2c9`)
- Simplify CLI entry to `incipit {}` (closes #242) (`364aaa799`)
- Add `exitus` modifier for CLI exit codes (closes #243) (`793eee391`)
- Stream-first stdin for `parse` and `check` commands (`47198a2ce`)
- Stream-first stdin and `emit --strict` mode (`e450392b4`)
- Disambiguate `for-of` loop from destructure in parser (`23e584899`)

### Other changes

- `§ dependentia` alias-based import resolution — enables dependency aliases
  declared via annotations, adds `Dependentia` type and `resolveDependentiaPath`
  (`15dd88f29`)
- Add `--manifest` flag for project manifest support (closes #210) (`df89bb9c0`)
- Latinize fetch module identifiers (`9db22f48b`)
- Consolidate collection DSL under `ab`, remove `ex` DSL transforms — `ab`
  gains `ordina`, `collige`, `grupa`, `max/min/medium/numera` with
  `ascendens`/`descendens` direction support (closes #216) (`4a3d8c8dd`)
- Remove bare `ex...importa` syntax — imports now require `§` prefix
  (closes #218) (`2bc05f09a`)
- Drop magic path resolution in faber codegen — when `keepRelativeImports=true`,
  preserve all paths as-is for portable emitted output (closes #234) (`4ab66b378`)
- Add `--verbose` flag to build commands to show subprocess output (`3b44ebaf3`)
- Add typecheck step to `build:faber` before compilation (`b6cc1600c`)
- Refactor build: target-suffixed binaries and output directories (`5fe2244e8`,
  `3e5ba601e`)
- Use `rivus emit` command for artifex compilation (`9c1bd4583`)
- Fix `faber` for-of loop disambiguation after `fixum`/`varia` (`17a9e960c`)
- Fix rivus API usage in minimal entry point (`6bfa28c6a`)
- Refactor rivus: separate CLI from core, add minimal entry point (`231b12aba`)
- Replace array destructuring in loop with explicit bindings (`bd52016ba`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
