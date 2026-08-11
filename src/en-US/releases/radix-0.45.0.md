+++
title = "Radix 0.45.0"
section = "releases"
order = 55
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.45.0 |
| **Tag** | `radix-v0.45.0` |
| **GitHub** | [radix-v0.45.0](https://github.com/faberlang/releases/releases/tag/radix-v0.45.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.45.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.45.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.45.0/radix-v0.45.0-aarch64-apple-darwin.tar.gz) | 1.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.45.0/radix-v0.45.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.45.0/radix-v0.45.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.45.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Operator spelling cleanup: shift arrows migrate to `⇐`/`⇒` (`≪`/`≫` retired),
and the conversion (conversio) glyph moves to `↦` (U+21A6). On the declaration
side, `sit x` gains an optional initializer that desugars to `fixum _ x`, and
the unenforced `fixus` post-name marker is removed.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 14 |
| Date span | 2026-06-24 → 2026-06-25 |

### Major tracks

#### Shift arrows (`⇐`/`⇒`) and conversio (`↦`) glyph migration

Retire `≪`/`≫` as scan errors. Conversio vacates `⇒` so the double-arrow pair
hosts bitwise shifts; the runtime conversion operator moves to `↦` (U+21A6,
"rightwards arrow from bar"). Updates span the lexer, parser, Faber codegen
roundtrip, HIR node types, AST, EBNF, exempla, and MIR tests (`31f312d27`).

#### `sit x` as inferred deferred immutable

The `sit` initializer is now optional: `sit x` desugars to `fixum _ x` — the
inferred deferred immutable — completing symmetry with the init-now `sit x ← v`
shape. EBNF updated to `sitDecl := 'sit' IDENTIFIER ('←' expression)?`,
parser guards removed, and definite-assignment tests added (`c18840350`).

#### `fixus` post-name declaration marker removed

Drop the unenforced `fixus` keyword from lexer through HIR and Faber emit.
The parser rejects lingering spellings with a migration diagnostic. Deletes
the `fixus` exemplum, refreshes `sponte` frontmatter, and aligns EBNF, README,
factory docs, and reference-pack term counts (`4822950d0`).

### Other changes

- Expand fixum/sit deferred-init coverage with parser and definite-assignment
  edge-case tests for typed and inferred deferred immutables, including
  partial-branch rejection and compound-assignment rules (`b9c6ec770`)
- Clear clippy warnings (duplicate test attribute, unused import, needless mut
  bindings) surfaced by `-D warnings` during glyph migration validation
  (`4f40f8323`)
- Update README: add inline JSON valor example contrasting JSON colon syntax
  with genus equals construction (`53a8bca2a`);
  expand glyph inventory to the full lexer surface (`ee6d427b0`);
  align user-facing examples with `↦` conversio and `⇐`/`⇒` shifts
  (`791db253a`)
- Close out factory delivery doc headers for MIR M-001, semantic passes P1–P3a,
  compiler vocabulary consistency, valor unification policy, and library import
  provenance (`c8e5758a2`)
- Close out forma parameterized templates delivery — literal-family Stage 3
  (`e521ddfd8`)
- Close out inline JSON valor delivery — literal-family Stage 6 (`135fb2732`)
- Close out literal, exempla, and hygiene doc tracks — Stage 7 (`87063aab9`)
- Archive superseded stdlib-data-formats factory track to
  `docs/factory/archive/` (`5c58a3b8f`)
- Close out shift-arrows-and-conversio-glyph factory goal — zero deviations
  from plan confirmed (`9d2b3c08d`)

### Verification (pre-release)

| Gate | Result |
| --- | ---: |
| `cargo test --workspace` | 990 tests pass |
| `cargo clippy -- -D warnings` | clean |

---

[All releases](/releases/) · [Install the current release](/start/install.html)
