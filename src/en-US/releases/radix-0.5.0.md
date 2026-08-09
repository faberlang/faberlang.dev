+++
title = "Radix 0.5.0"
section = "releases"
order = 92
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.5.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Patch release spanning **9 commits** (`v0.4.0..v0.5.0`). Adds `fractus`, `decimus`, and `octeti` types for TypeScript codegen, expands the implementation checklist with verb conjugations and collection methods, restructures the README around a condensed thesis, and moves binary distribution to GitHub Releases.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 9 |
| Date span | 2025-12-24 |

### Major tracks

#### Type system: `fractus`, `decimus`, `octeti` for TypeScript

- Adds TypeScript codegen for `fractus` (float → `number`), `decimus` (decimal → `Decimal` with auto-import of `decimal.js`), and `octeti` (bytes → `Uint8Array`) (`764e32ae6`).
- Implements numeric type promotion: `numerus ↔ fractus ↔ decimus` (`764e32ae6`).
- Fixes the `decimal.js` import to use `import type` for type-only usage (`38f2ee996`).

#### TypeScript codegen test coverage (85 %/97 %)

- Adds 38 tests covering previously untested code paths: interface (`pactum`) declarations, computed getters, async/generator return type wrapping, template literals, wildcard imports, catch clauses on control flow, range expressions as values, computed member access, block-body lambdas, empty blocks, else-if chaining, and `emitte`/`ausculta` events (`a409c4e5e`).
- Adds `exempla/structurae/pactum.fab` with comprehensive interface usage examples (`a409c4e5e`).

#### Implementation checklist expansion

- Expands the codegen checklist (`consilia/codegen/checklist.md`) with verb conjugation return types (`fit`/`fiet`/`fiunt`/`fient`), new type system rows (`fractus`/`decimus`/`octeti`/`objectum`), and new sections for `Tabula` (Map, 17 methods) and `Copia` (Set, 12 methods) (`a26a8dfc4`).
- Adds 20 undocumented `Lista` methods, fixes `erade` → `dele` to match implementation, and adds `inLista`/`inObjectum` for `Tabula` and `inLista`/`valores`/`perambula` for `Copia` (`f0f9a8a76`).
- Updates README to mark `fit`/`fiet`/`fiunt`/`fient` as implemented for TypeScript and Python (`bd1346689`).

#### README restructure

- Replaces the tutorial-style README with a condensed thesis explaining why Latin matters as a language design choice (`14c8d29c7`).
- Moves the implementation checklist from `consilia/codegen/` to `README.md` (`14c8d29c7`).
- Deletes the redundant standalone `consilia/codegen/checklist.md` (`14c8d29c7`).
- Consolidates target-platform notes into brief summaries (`14c8d29c7`).

#### Distribution: GitHub Releases

- Deletes the `editiones/` directory (binaries now hosted on GitHub Releases) (`83ffb5303`).
- Rewrites the release script to create GitHub Releases via `gh release create` (`83ffb5303`).
- Simplifies the install script to place `opus`/`faber` binaries into `~/.local/bin` (`83ffb5303`).

### Other changes

- Version bump to `v0.5.0` (`8675cab3c`).

---

[All releases](/releases/) · [Install the current release](/start/install.html)
