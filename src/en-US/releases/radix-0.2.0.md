+++
title = "Radix 0.2.0"
section = "releases"
order = 98
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.2.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Post-hoc release note spanning **67 commits**. `v0.1.0` has no tag — the tag
series starts here — so the base is the repository's first commit
(`664d7a659`, 2025-12-20, "Initial project setup"). Range:
`664d7a659..v0.2.0`, 2025-12-20 → 2025-12-22.

Headline: **first tagged checkpoint of the Faber Romanus era** — a
TypeScript/Bun compiler bootstrapped over three days: lexicon with declension
support, tokenizer, parser, semantic analysis with type resolution, and
TS/Zig/WASM codegen, all behind a Latin-keyword language surface that was still
in rapid flux (extension `src`→`fons`, `.la`→`.fab`, type-first→arrow return
types all changed inside this range).

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 67 |
| `feat(...)` commits | 0¹ |
| `fix(...)` commits | 0¹ |
| `docs(...)` commits | 0¹ |
| `test(...)` commits | 0¹ |

¹ Conventional prefixes were not yet in use; every subject is a bare
imperative verb. Leading-verb signal: 35 `Add`/`Added`, 6 `Fix`,
4 `Implement`, 4 `Complete`, 3 `Update`, 15 other.

Reconstruct the full log:

```bash
git log 664d7a659..v0.2.0 --oneline --no-merges
```

### Major tracks

#### Architecture and syntax bootstrap

- Records the initial architecture decisions (ADR-001 through ADR-005) in
  `docs/decisions.md` (`0577ce88e`), the syntax-sketch decisions (`41c924122`),
  complete control-flow syntax (`e0d00ada4`), and the lexicon design document
  (`33750e07b`).

#### Compiler pipeline (TypeScript/Bun)

- Adds the lexicon module with tests (`25b5fd0d2`) and built-in types with
  complete declension support (`396148872`).
- Implements the tokenizer (`10a64cf30`), parser (`8902b097d`), and code
  generator plus CLI (`261cf8569`).
- Adds a semantic-analysis phase with type resolution — `src/semantic/`
  (`index.ts` 759 lines, `scope.ts`, `types.ts`) with a 257-line test suite
  (`4b6e6bd26`).
- Fixes the `run` command and maps `scribe` to `console.log` (`29ba362d5`).

#### Multi-target codegen: TS, Zig, WASM

- Adds dual codegen (TS + Zig) and renames the source extension to `.la`
  (`0bae43f63`), with a later rename to `.fab` when the Zed extension lands
  (`db84800c3`).
- Adds WASM as a third compilation target — a 759-line `src/codegen/wasm.ts`
  (`0e3bfda36`).
- Adds comprehensive codegen tests and updates the Zig target (`4aa219cd9`);
  fixes Zig codegen (output validation `fa47b8d82`, later issue fixes
  `6510e75c5`) and assert codegen braces for ESLint compliance (`5e1aaffbb`).

#### Language surface

- Migrates to type-first syntax with an expanded type system (`45ab626c0`),
  then changes function return types from type-first to arrow syntax
  (`4a92ff996`).
- Makes types and keywords case-insensitive with lowercase canonical forms
  (`8801b4ebf`, `c58dafc46`).
- Adds array literals (`2c8913a2a`), object literals (`d17b7d77a`), and object
  destructuring (`ec1dfef43`).
- Changes for-loop syntax to source-first `ex/in ... pro` (`384e5703a`) and
  adds range syntax with a per-step form: `0..10 per 2` (`2a1d901e2`).
- Adds control-flow statements: `adfirma` assertion (`652d57733`), `custodi`
  guard (`bcf394c56`), `elige/si` switch (`f73e39d4b`), `cum` with-blocks
  (`d49bd6551`), and `ergo` one-liners for `si`/`aliter` (`7c99020aa`) and
  loops (`c9aa89580`).
- Adds `scribe` as a statement keyword, fixing the switch `ergo` parser bug
  (`032d30e17`) and `scribe` global plus `ergo` switch syntax (`134ae36e2`).
- Adds `nulla`/`nonnulla` empty/non-empty operators (`3253a67cb`).
- Adds an intrinsics layer and the `norma` stdlib written in Faber
  (`1c2902314`), then underscores all intrinsics for consistency
  (`c9c1050c3`).

#### Lexicon and Latin keyword surface

- Refines the verb lexicon around a Unix command philosophy (`9b3e0e940`),
  adding the 2nd conjugation for stateful operations (`19d885e5c`) and the 4th
  conjugation for IO/side-effect operations (`b3456ff86`).
- Adds OOP/module keywords for cross-target portability (`0a3bf2f3c`), returns
  a structured `LexiconError` instead of `null` (`8e40da11e`), removes `Res`
  and `Functio` from `types-builtin` (`daa44eb40`), and completes the
  high-priority lexicon TODOs (`a4e185be8`).

#### Editors and tooling

- Adds Zed syntax highlighting with an in-repo tree-sitter grammar and renames
  the extension to `.fab` (`db84800c3`).
- Adds ESLint with Stroustrup brace style (`80ac73af6`) and replaces
  `@stylistic` with Prettier for code formatting (`8054c30c8`), with a
  linter-applied pass (`75c7017d0`).
- Adds the systems-language developer code standards (`0472f3acb`) and
  comprehensive module documentation (`f36339c5d`).

#### Build, release, and repo organization

- Renames directories to Latin: `src`→`fons`, `examples`→`exempla`
  (`9113c1560`); adds `scripta/` for package scripts (`79f029a6a`) and a
  standalone executable build (`bun run build` → `opus/faber`, `3c6b7d9bf`).
- Adds the `release` script (`da966fdfc`) and ESLint (`d6247b081`) and Zig
  `build-exe` (`1455fd481`) verification to `build:exempla`.
- Updates examples to the `fixum` keyword (`6ed3cc00d`) and `scribe` statement
  syntax (`c28c27f12`); deletes `examples/app` (`5729c1823`).
- Adds the comprehensive README (`e4f135fc2`), the WASM-target architecture
  README update (`fe78436b8`), user-defined types documentation (`ac3a7e92f`),
  the current-features README update (`046560505`), and a documentation
  cleanup pass (`e7a15475c`).
- Releases v0.2.0: bumps `package.json` and commits the standalone binary as
  `editiones/faber-0.2.0` (`8b2169d19`).

### Honest limitations

- **Post-hoc note.** This document was written after the fact from the git
  range; no release process or verification record survives from the era.
  `v0.1.0` was never tagged, so the range base is the repository's first
  commit (`664d7a659`), not a v0.1.0 boundary.
- **No gated test suite.** No CI or test gates existed in this range; the
  closest checks were ESLint, Prettier, and manual `build:exempla`
  verification. Test files exist (parser, semantic, codegen, lexicon) but no
  pass/fail record is in the range.
- **Binary committed to the repo.** `editiones/faber-0.2.0` is a ~60 MB
  bun-standalone executable committed directly to the tree — an era practice,
  not a multi-arch release artifact.
- **Rapidly moving language.** Keyword surface, syntax, file layout, and even
  the source extension changed within this range. Nothing here is a stability
  promise.
- **WASM target depth.** `wasm.ts` landed near the end of the range; its
  coverage at v0.2.0 is unverified from this range alone.
- **Classification caveat.** Without conventional prefixes, the Scale table's
  `feat`/`fix`/`docs`/`test` rows are all zero; the leading-verb counts are
  the era's only signal.

### Version alignment

| Item | Value |
| --- | --- |
| Source tag | `v0.2.0` (commit `8b2169d19`, 2025-12-22) |
| `package.json` version (`faber-romanus`) | `0.2.0` |
| Release artifact | `editiones/faber-0.2.0` (committed binary) |
| Prior tag | none — `v0.1.0` was never tagged |

---

[All releases](/releases/) · [Install the current release](/start/install.html)
