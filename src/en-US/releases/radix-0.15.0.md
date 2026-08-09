+++
title = "Radix 0.15.0"
section = "releases"
order = 82
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.15.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Intensive single-day release that introduces the **norma-faber** annotation-driven standard library framework (11 core commits), replaces auto-generated grammar docs with a hand-written EBNF spec and prose-based grammatica tutorials, and integrates the faber-trials LLM learnability research harness into the main repo.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 23 |
| Date span | 2026-01-06 (06:27 → 11:12) |

### Major tracks

#### Norma-faber: stdlib annotation framework

Norma-faber defines standard library methods in Faber source (`.fab` files) with codegen annotations that map to each target language. Four annotation types control the pipeline:

- `@ innatum` — maps a Faber collection type to its native target type (e.g., `@ innatum ts "Array"`, `py "list"`)
- `@ subsidia` — declares an external implementation dependency
- `@ radix` — declares morphological variants
- `@ verte` — maps a method name (simple rename) or supplies a template with `§` / `§0`/`§1` indexed placeholders

Key milestones in this release:

- **Design document** defining the approach for collections (fake morphology) vs IO (real morphology) (`adc0cfc4e`)
- **Faber parser** parses all four annotations into the AST, with tests (`225afbbd5`)
- Parser **rejects multiple `@ verte` targets on a single line** — each must be its own annotation (`cbf856706`)
- Richer grammar documentation of annotations in `EBNF.md` and `fons/grammatica/structurae.md`, plus working exemplum (`e04851ede`)
- **Rivus parser** (Faber's bootstrap compiler) implements parallel annotation parsing with error codes P301–P308 (`14134c1be`)
- **Vertical slice** proves the architecture end-to-end: `lista.adde` and `lista.addita` codegen correctly for TypeScript and Python via the registry (`b5f9ef75b`)
- **All 5 codegen targets** (TS, Py, Rust, C++, Zig) wired to the norma registry; placeholder character fixed from `'S'` to `§` (`45d34369b`)
- **Build-time generated registry** (`scripta/build-norma.ts`) reads `.fab` files and produces `norma-registry.gen.ts` and `norma-registry.gen.fab`; add `bun run build:norma` command (`f297c6dd3`)
- Prefer `bun run` over direct `scripta/` invocation for proper environment setup (`2c055cb7c`)
- **47 of 53 lista methods** migrated to `fons/norma/lista.fab` with indexed `§0`/`§1` placeholders; § regex fixed from matching ASCII `'S'` (`b781954da`)
- Progress, architecture diagrams, and full lista migration plan documented in `consilia/futura/norma-faber.md` (`f1b40501d`, `7f62b6848`)
- Development workflow section (build/test cycle for adding methods) (`a005aef55`)

#### Documentation restructure

- **Hand-written `EBNF.md`** (416-line spec) replaces auto-generated `GRAMMAR.md` (1525 lines), becoming the authoritative language specification for both faber and rivus compilers (`5103db701`)
- **Grammar extraction script** (`scripta/extract-grammar.ts`) removed — docs no longer derived from parser source (`5103db701`)
- **Grammatica docs** rewritten as **prose tutorials** with code examples and etymology-based explanations: `fundamenta.md`, `typi.md`, `functiones.md`, `structurae.md`, `importa.md`, `operatores.md`, `regimen.md`, `errores.md` — ~2686 lines added, ~948 removed (`4ef97717a`)
- Grammatica files moved from `grammatica/` to `fons/grammatica/` (`5103db701`)

#### LLM research harness

- **`probationes/` directory** created by merging `faber-trials/` into the main repo — a full LLM learnability research pipeline (`5103db701`)
- Harness includes: `analyzer.ts`, `grader.ts`, `loader.ts`, `pipeline-runner.ts`, `runner.ts`, `prompt.ts`, `api.ts`, `types.ts` (`5103db701`)
- Tasks: `complete.yml`, `complex.yml`, `predict.yml`, `translate.yml` (`5103db701`)
- Thesis document: `probationes/thesis.md` (526 lines) (`5103db701`)
- **Relative paths** in probationes harness fixed to use `import.meta.dir` for correct resolution from the repo root (`455be4da7`)
- **Trials no longer run post-AI review** — runner updated to skip the review step (`9555f9fe6`)
- **README** reframed as LLM-oriented IR ("Latin hypothesis") with Research & Evidence section citing Framework 1.1 trial results; systems languages (Zig, Rust, C++) as primary value prop (`d2b8d710f`)

### Other changes

- **Test source field standardization**: `faber:` and `input:` fields renamed to `source:` across all 71 YAML test files; harness consolidated to a single `TestCase` type; added `faber: false` skip flag (`ac4d4057d`)
- **CHECKLIST website preparation**: compiler descriptions and CLI usage sections added to both `fons/faber/CHECKLIST.md` and `fons/rivus/CHECKLIST.md` (`e9110fc7b`, `9f6d16bc4`); bracket status markers (`[x]`, `[ ]`, `[~]`) replaced with Unicode circles (`●`, `○`, `◐`) for better HTML rendering (`462b62d2d`); table formatting cleaned up in both CHECKLIST files (`20f3f919f`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
