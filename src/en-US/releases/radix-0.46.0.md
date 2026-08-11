+++
title = "Radix 0.46.0"
section = "releases"
order = 54
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.46.0 |
| **Tag** | `radix-v0.46.0` |
| **GitHub** | [radix-v0.46.0](https://github.com/faberlang/releases/releases/tag/radix-v0.46.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.46.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.46.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.46.0/radix-v0.46.0-aarch64-apple-darwin.tar.gz) | 1.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.46.0/radix-v0.46.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.46.0/radix-v0.46.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.46.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Regex conversio and fallback policy: `textus ↦ regex`, reject incoherent fallback.  
Compound assignment removed; postfix `⊕`/`⊖` increment/decrement added.  
README reorganized as a front-loaded landing doc; MIT license filed.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 7 |
| Date span | 2026-06-25 → 2026-06-25 |

### Major tracks

#### `textus ↦ regex` conversio and fallback rejection (Part A)

- Ship real `textus`/`ascii`-to-`regex` conversio with constant folding to `HirLiteral::Regex`, backend codegen via `FaberRegex::new`, and removal of the `sed` keyword with a migration diagnostic. Exempla, EBNF, and factory docs updated. Slash `/…/` literals deferred to Part B. (`0a5cac22e`)
- Add template-built path conversio to the exempla: `"/home/§/.*"(tenant) ↦ regex` cross-referencing `scriptum` template application. (`774abc464`)
- Reject `vel` fallback on `↦ regex` as structurally incoherent — the fallback slot requires a target-typed occupant but regex has no literal form, making recursion the only possible fallback. Typecheck diagnostic added; lowering guarded against silent drop. (`2d86d9b4a`)

#### Remove compound assignment; add postfix `⊕`/`⊖` statements

- Reverse the v0.31 Unicode compound-assignment operators and repurpose `⊕`/`⊖` as Go-style postfix increment/decrement statements for `numerus` places. Lexer `PostInc`/`PostDec` tokens, parser `incDecStmt`, HIR/MIR lowering with evaluate-once semantics, semantic and codegen support across all four backends (Faber, Rust, Go, TypeScript). Delivers exempla (`incrementa.fab`), EBNF update, and reference-pack index migration. (`cb697b222`)
- Update README assignment policy: expression-level `←` only, statement-only postfix `⊕`/`⊖`, with link to the breaking-change release note. (`0fd328da2`)

#### Docs reorganization and licensing

- Reorganize README as a front-loaded landing doc: lead tagline + status + badges, Why Faber thesis, Commandments, Language Snapshot, trimmed Quick Start — with the full language reference intact below the fold for LLM ingestion. Moves common failure modes to `AGENTS.md`. (`81cffe791`)
- Add MIT `LICENSE` and wire up real license badge. (`5a9bcae05`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
