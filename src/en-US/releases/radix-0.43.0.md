+++
title = "Radix 0.43.0"
section = "releases"
order = 56
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.43.0 |
| **Tag** | `radix-v0.43.0` |
| **GitHub** | [radix-v0.43.0](https://github.com/faberlang/releases/releases/tag/radix-v0.43.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.43.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.43.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.43.0/radix-v0.43.0-aarch64-apple-darwin.tar.gz) | 1.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.43.0/radix-v0.43.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.43.0/radix-v0.43.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.43.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Literal-family campaign: five new literal forms shipped across the compiler
pipeline — guillemet block text, ascii, backtick forma templates, pipe-delimited
octeti, and inline JSON valor. The old `{ key = expr }` anonymous-object syntax
is retired (clean break) in favor of JSON `{ "key": value }` valor literals.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 32 |
| Date span | 2026-06-23 → 2026-06-24 |

### Major tracks

#### Guillemet block textus (Stage 1)

- Ship `«...»` block string scanning with multiline and embedded-quote support;
  reject legacy `❝...❞` with a replacement diagnostic. (`b0bf20b6c`)
- Migrate the block-string exemplar and EBNF; prove `«...»(...)` template
  rendering via scriptum. (`b0bf20b6c`)

#### Ascii primitive (Stage 2)

- Ship `'...'` as compiler-owned ascii with compile-time ASCII validation,
  reject template application, provide safe widening to textus and fallible
  textus ⇒ ascii conversio via FaberAscii. (`cc765658e`)
- Fix: `FaberAscii` now `Deref<Target=str>` so `textus ⊕ ascii` append emits
  valid Rust. (`b9c5c42ec`)
- Codegen stubs across all backends (Rust, Go, TS, Faber). (`cc765658e`)

#### Forma template capture (Stage 3)

- Ship compiler-owned `forma` genus with backtick `` `...` `` literals and
  `` `...`(args) `` application; captures lower to genus construction via Verte,
  never through scriptum rendering. (`f2d7e5be9`)
- Builtin registration, conditional HIR injection, valor widening, Rust codegen,
  and internal postgres/sqlite renderer proofs. (`f2d7e5be9`)
- Fix: inline `FaberValue` for valor instead of pulling `norma::datum::Valor`
  (emitted Rust failed to compile); borrow fix for multi-param captures. (`6304a3866`)
- Partition user/builtin def-id ranges — user def ids start at `0x1000`, builtins
  allocate from a separate range — removing the hardcoded `FORMA_DEF_ID` sentinel. (`6304a3866`)
- `forma_render` is now `#[cfg(test)]` only; `forma` is reserved like
  `numerus`/`textus` and rejected in user source as duplicate definition. (`6304a3866`)

#### Octeti hex literals (Stage 5)

- Ship `|hex|` compile-time byte constants with whitespace-tolerant decoding;
  `||` is empty octeti; odd or invalid hex is diagnosed. (`2f6cfd6db`)
- Rename Unicode bitwise token kinds to `Bitwise*` to free the `|` delimiter. (`2f6cfd6db`)
- Rust codegen emits `vec![0x..]`; exempla and EBNF updated. (`2f6cfd6db`)
- Fix: propagate decode errors in literal codegen as `CodegenError` instead of
  silently falling back to `vec![]` / raw text. (`14b99ec73`)

#### Inline JSON valor (Stage 6)

- **Parser:** bare `{ ... }` in expression position now parses as JSON grammar,
  not a Faber anonymous record. True/false/null lex as ident; `-7` assembled in
  parser with `checked_neg`; trailing commas allowed; bare-ident keys and Faber
  keywords rejected. (`f78f0a9e7`)
- **Typecheck:** `JsonValor` typed to `Primitive::Valor`; duplicate keys rejected
  (explicit compile-time error, not silent last-wins). Threads through full
  HIR/MIR/codegen pipeline. (`c043667b9`)
- **`tabula<K,V>` ascribe:** JSON valor literal ascribed to `tabula<K,V>` lowers
  to a real `HashMap<K,V>` constant (contract §9), not a `FaberValue::Tabula`
  wrapper. (`82cab0329`)
- **Retire `lower_objectum`:** dead-code deletion of the old anonymous-object
  lowering path; bare `ExprKind::Object` now errors with a clear diagnostic. (`82cab0329`)
- **Exempla migration (Stage 6a):** all canonical exempla/fixtures migrated from
  `{ key = expr }` to JSON valor, genus types, or tabula as built. Test clean-up:
  9 deleted tests of retired features, 3 restored with corrected types. (`dbf736771`)
- **EBNF update (Stage 6b):** `objectLiteral` production replaced by
  `jsonLiteral`; `objectField`/`objectKey` renamed to `fieldInit`/`fieldKey`. (`23f8f2262`)
- **Validation (Stage 7):** 775 radix tests pass, `cargo build -p faber` clean. (`a25df45ce`)

#### Factory planning / decisions

- Resolve six cross-delivery decision gates: forma manual construction allowed,
  duplicate JSON keys are an error, `tabula<K,V>` ascribe in v1 scope,
  non-Rust backend parity is routine `CodegenError` work, valor Stage 6 split
  into 6a/6b, JSON literals get a dedicated parser. (`ca67497b8`)
- Add factory specs: inline JSON valor (`f2eaf09d2`, `50d6f219e`), octeti pipe hex
  (`6fc8f382f`), regex literal with `/`/`⇒` (`f4351d4a6`), string delimiter family
  (`d9da96329`), clean-break policy (`430655a43`), empty regex (`3f9a0c3bd`).
- Sync goal docs with shipped valor/FaberValue codegen. (`3869e5aff`)
- Complete inline-json-valor Goal Stages 0 and 1 baseline contracts. (`a72c479ba`, `32b38c154`)
- Record `lower_objectum` retirement plan in inline-json-valor ledger. (`38488ca06`)
- Clarify octeti pipe delimiter factory plan. (`9845d71bb`)
- Align literal family factory plans. (`4329a07fa`)
- Pause regex-literal delivery pending `/`-vs-division lexing contract. (`ca67497b8`)
- Add lightly-defined rust codegen smoke-check goal. (`546afa171`)

### Other changes

- Remove unused intrinsic parameter kinds. (`1691027e6`)
- Use Tokio `block_on` for runtime-backed packages. (`6057068ba`)
- Polish rust runnability factory docs. (`d34571630`)
- Style: fmt ascii-widening helpers in rust stmt codegen. (`4f20f3964`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
