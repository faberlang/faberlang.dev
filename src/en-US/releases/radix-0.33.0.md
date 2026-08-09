+++
title = "Radix 0.33.0"
section = "releases"
order = 64
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.33.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Tight release establishing the **faber** binary name, a tag-based CI release pipeline,
and the crate version aligned to `v0.33.0`. First compiled release after a long
retrospective-marker ladder.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 7 |
| Date span | 2026-05-20 → 2026-05-20 |

### Major tracks

- **Faber release pipeline.** New GitHub Actions workflow
  (`.github/workflows/release.yml`) triggered by `v*` tags: builds `faber` for
  `x86_64-unknown-linux-gnu` and `aarch64-apple-darwin`, packages tarballs with
  SHA-256 checksums, and uploads to the GitHub Release. Crate version bumped to
  `0.33.0`; `[[bin]] name = "faber"` added to `Cargo.toml`; README goals,
  `package.json`, `scripta/release`, and `scripta/use` updated. (`319582bca`,
  `cc2e2e40c`, `75eea33d2`)
- **CLI identity renamed to "faber".** The `#[command(name)]` attribute in the
  CLI entry point changed from `"radix"` to `"faber"`, so `--help` and related
  surfaces now display the correct binary name. (`897dd7360`)

### Other changes
- Fix rust codegen clippy warnings: `sort_by`/`cmp`/`Reverse` idiom and a
  redundant `format!` wrapper in help-text generation. (`90527bd46`)
- Align markdown table columns in `docs/grammatica/cli.md` (table formatting
  only). (`0f46f75d0`)
- Add `docs/release/retrospective-minor-tags.md` — proposal document for
  annotated marker tags from `v0.8.0` through `v0.32.0`, preserving the
  development epoch story without publishing historical binaries. (`4388e309c`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
