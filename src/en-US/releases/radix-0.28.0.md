+++
title = "Radix 0.28.0"
section = "releases"
order = 69
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.28.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

This release spans **39 non-merge commits** (`v0.27.0..v0.28.0`, 2026-01-21 → 2026-01-22). It covers a broad nullable-type migration from `Type?` suffix to `si Type` prefix, a new `tacet` no-op keyword, a suite of "syntaxis aliena" diagnostic errors (P400–P409) that catch foreign syntax and suggest the correct Latin form, a unified keyword-dispatch annotation grammar across all compilers, the first Zed tree-sitter grammar for syntax highlighting, substantial nanus-rs codegen maturation, and a reworked build pipeline that removes the legacy `faber` compiler and splits exempla verification into separate stages.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 39 |
| Date span | 2026-01-21 → 2026-01-22 |

### Major tracks

#### Nullable type syntax: `si Type` prefix

- Replace `Type?` nullable suffix with `si Type` prefix across the rivus parser and all 44 source files; emit diagnostic P403 (`SyntaxisAlienaNullabilis`) when the old suffix appears (`aad4f4bf7`)
- Convert remaining generic nullable patterns (`lista<T>?` → `si lista<T>`) in AST definitions (`67ee1d19d`)
- Fix canonical order to `si` before ownership — `si de textus` not `de si textus` — matching nanus-ts parse order (`a9d82ff50`)
- Update all nanus compilers (ts, py, rs, go) to parse and emit `si Type` instead of `Type?` (`394a8d6f2`)
- Update the norma generator to emit `si textus` / `-> si VerteTranslation` (`353262373`)

#### Syntaxis aliena diagnostics (P400–P409)

- P400: colon type annotations (`fixum x: textus` → `fixum textus x`) (`eac9b9d5e`)
- P401: `pro...de` loops (`pro item de list` → `ex list fixum item`) (`eac9b9d5e`)
- P402: arrow functions (`(x) => x + 1` → `clausura x: x + 1`) (`eac9b9d5e`)
- P403: `Type?` nullable suffix → `si Type` prefix (`aad4f4bf7`)
- P404: `aliter` / `aliter si` → `secus` / `sin` (`c1894fe08`)
- P405: `??` nullish coalescing → `vel` (`e5458cb69`)
- P406: `? :` ternary → `sic` / `secus` (`b9dd540d0`)
- P407: `exspecta` (await) → `cede` (`7b12ad505`)
- P408: `@ asynca` → `@ futura` (`48b0dc5e6`)
- P409: `secus si` (else-if) → `sin` (`f0d51f788`)
- Hints for ~40 common JS/Python assumed globals (JSON, console, Math, etc.) with Faber equivalents; English method names on `lista`, `tabula`, `copia`, `textus` suggest Latin alternatives from `norma/innatum` (`bac6772c8`)

#### `tacet` keyword (explicit no-op)

- Add `tacet` to rivus parser and semantic analysis; replace 92 `casu _ { }` and 22 `ceterum { }` instances with `casu _ tacet` / `ceterum tacet`; emit semantic error for empty blocks (`eac9b9d5e`)
- Add `tacet` keyword to all nanus lexers (ts, py, go, rs); `parseElige`/`parseDiscerne` delegate to `parseBody()` which already supports it (`ad72a561b`)
- Add `tacet` to the EBNF grammar (`45f39400e`)
- Add `tacet` keyword to the Zed tree-sitter grammar (`c5c00c210`)

#### Unified annotation grammar (keyword dispatch)

- `subsidia-rs`: keyword-dispatch parser for `§` (importa, sectio) and `@` annotations (publica, futura, externa, innatum, subsidia, radix, verte, CLI metadata); unknown keywords produce parse errors instead of silent skip; emitter normalizes to new import syntax (`29ccaa1fc`)
- All remaining compilers (nanus-ts, nanus-go, nanus-py, faber-ts): keyword-dispatch `parseSectio()` / `parseAnnotatio()` for `§` and `@` annotations; unknown `@` keywords error at parse time; emitters always emit new syntax (`90be9c560`)
- New import syntax: `§ importa ex "path" bindings`; legacy `§ ex "path" importa` still supported (`9d86d4df9`, `90be9c560`)

#### nanus-rs: bundle command and Rust codegen

- Add `bundle` subcommand that collects cross-file AST types into a single Rust file for compilation (`dbe90ad79`)
- Implement heuristics for cross-file AST type resolution; sanitize Rust codegen (`55a2b2906`)
- Make the generated rivus crate typecheck: large emitter rewrite + bundler fixes spanning 500+ lines (`5ca7a2c8b`)
- Add `tacet` to lexer; fix emitter for new annotation syntax (`11355ff83`, `29ccaa1fc`)

#### Build pipeline rework

- Split `build:exempla` into codegen (stage 4) and verify (stage 5) using stdin-based CLI; output to `opus/<compiler>/exempla/<target>/`; add `--no-verify` / `--verify-only` flags (`f88cd3f7b`)
- Stage 4 runs exempla using all rivus variants that passed stages 2+3; `build-exempla.ts` accepts `-c <compiler>` for explicit selection (`4d9c614ea`)
- Remove `faber` compiler; make nanus-ts canonical bootstrap; remove `--no-faber` / `--no-rivus` flags; stages: 1 = nanus + norma, 2 = rivus via nanus-ts (must succeed), 3 = rivus via other nanus compilers (optional) (`a5f27e55b`)
- Pass `--stdin-filename` to compilers so error messages show real file paths instead of `<stdin>` (`1284fba78`)
- Unwrap shell errors in `build-rivus.ts` (`0045cddcd`)

#### Zed tree-sitter grammar

- Initial token-based grammar for keyword/literal/annotation highlighting with language config and highlights queries (`c2dd062df`)
- Expand to full keyword coverage matching EBNF: `custodi`, `cura`, `clausura`, `prae`, `ceteri`, `futura`, Hex/Oct/Bin/Dec radix types, and many more (`36dbd5907`)
- Simplify annotation/directive parsing to single-line tokens (`d45c0a787`)
- Register grammar in `extension.toml` (`57917d23f`)
- Move tree-sitter grammar to separate `tree-sitter-faber` repository; delete bulk-generated parser files from this repo (`63b7f5401`)
- Simplify language name from "Faber Romanus" to "Faber" (`45a1fc767`)

### Other changes

- Rename `lista.adde` to `lista.appende` to disambiguate list-append from set-add (`copia.adde`); fixes TypeScript type error where nanus emitted `.push()` for `copia<T>` fields (`8cd00e96d`)
- Generator-first parameter convention: flip generator parameter to first position in all 93 `gen*()` function signatures across rivus codegen; refactor `genFunctio` and `genGenus` to pass whole AST nodes; raise rivus compile count from 112/125 to 125/125 (`d09f27708`)
- Remove unreachable symbolic shift tokens (`<<`, `>>`, `>>>`) from AST; enforce keyword-only shift operators; add parse-error tests (`8970e30ec`)
- Remove unused English dialect support (`Dialectus.Anglicus`, `verbumAnglicusId`) from rivus (`a1bbd18d0`)
- Require typed callable parameters; warn on `ignotum` in rivus semantic analysis (`1726e5b31`)
- Fix bootstrap build chain bugs across nanus-py, nanus-rs, nanus-ts, rivus Go codegen, and `subsidia-rs` (`11355ff83`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
