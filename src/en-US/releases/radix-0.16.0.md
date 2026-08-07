+++
title = "Radix 0.16.0"
section = "releases"
order = 83
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.16.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Compact release spanning **13 commits** on a single day. The dominant theme is
the **conversio** type-conversion operator system — from design document through
keywords, AST, parser, semantic analysis, codegen for all 6 targets, and a
57-test suite. A secondary track adds indexed placeholder syntax (`§0`, `§1`)
to `scriptum` expressions and fixes template positional issues in the `norma`
template registry.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 13 |
| Date span | 2026-01-06 → 2026-01-06 |

### Major tracks

#### Conversio: type conversion operators

Full pipeline from design to test suite for four postfix conversion operators:

| Operator | Semantics | Example |
| --- | --- | --- |
| `numeratum` | string → integer (with optional `<type, radix>`) | `"42" numeratum` |
| `fractatum` | string → float | `"3.14" fractatum` |
| `textatum` | any → string (infallible) | `x textatum` |
| `bivalentum` | any → boolean (nonnulla semantics) | `x bivalentum` |

The chain of commits covers:
- **Design doc** with syntax, fallback via `vel`, type parameters, and radix constants (`Hex`, `Oct`, `Bin`, `Dec`) (`ef962008f`)
- **Design decisions** — radix changed from literal integers to predefined types; expanded AST with `targetType` and `radix` fields (`cf20b6d1b`)
- **Implementation checklist** — 7-phase plan with concrete file paths (`ebbf2d9c1`)
- **Phase 1** — keywords (`numeratum`, `fractatum`, `textatum`, `bivalentum`, `Dec`, `Hex`, `Oct`, `Bin`), AST node (`ConversionExpression`), parser extension (`f5f980362`)
- **Grammar docs** — EBNF rule `conversionOp` and operator reference in `operatores.md` (`3508ce627`)
- **Phase 4: semantic analysis** — result type resolution, `targetType` override, fallback validation, nullable result with `vel nihil` (`9fcd55ad6`)
- **Codegen plan** — per-target details (Rust `.parse()`, Python `int()`/`float()`, C++ `std::stoll()`, Zig `std.fmt.parseInt()`, Faber identity re-emit) (`c35d6efdc`)
- **Codegen implementation** — all 6 targets (ts, py, rs, cpp, zig, fab) with basic conversion, type params, radix, and fallback support (`b45541524`)
- **Test cases** — YAML structure following `qua.yaml`/`innatum.yaml` patterns (`402020ab8`)
- **Test suite** — 57 tests covering all operators, chains, and edge cases (`421a3dd16`)

#### Scriptum indexed placeholders and norma template fixes

- **Indexed placeholder support** (`§0`, `§1`) in `scriptum()` expressions across all 5 codegen targets (TS: template literal reordering; Python/Rust/C++: `{0}`, `{1}`; Zig: argument tuple reorder) (`3a1da493e`)
- **Norma template positional fix** — `applyNormaTemplate` consumes `alloc` from args; `lista.fab` templates updated to use `§0`/`§1` for repeated `ego` references; all 144 lista tests pass (`76d4dc5cc`)

### Other changes

- **Norma-faber migration status** — `norma-faber.md` marks lista migration complete (47 methods in norma, 5 reserved in fallback); documents indexed placeholder syntax; lists remaining work (tabula.fab, copia.fab, morphology validation) (`1ce8fee98`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
