+++
title = "Radix 0.55.0"
section = "releases"
order = 42
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.55.0 |
| **Tag** | `radix-v0.55.0` |
| **GitHub** | [radix-v0.55.0](https://github.com/faberlang/releases/releases/tag/radix-v0.55.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.55.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.55.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.55.0/radix-v0.55.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.55.0/radix-v0.55.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.55.0/radix-v0.55.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.55.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Synthetic tag documenting the **octeti unification** theme: `octeti` becomes semantic sugar over `lista<numerus<u8>>` with bidirectional assignability, the `octet` builtin scalar alias for `numerus<u8>` arrives, and the `↦` conversion operator gains bidirectional text/ascii/octet arms. Includes the `pactum` → `implendum` contract keyword rename, modulus call diagnostic hardening, and factory planning for transitive stdlib imports and tensor-types closeout.

### Scale
| Signal | Count |
| --- | ---: |
| Commits (no merges) | 12 |
| Date span | 2026-06-27 19:18 → 2026-06-27 21:34 (all same day) |

### Major tracks

- **Octeti / `lista<numerus<u8>>` unification.** `octeti` and `lista<numerus<u8>>` become bidirectionally assignable; octeti receivers route through the existing lista intrinsic surface. The `octet` builtin scalar arrives as a natural spelling for `numerus<u8>`, restoring the byte/buffer pairing. The `↦` conversion operator gains working codegen for all four text/ascii/octet directions with dedicated Rust arms and a new `Ascii::try_from_bytes` runtime helper. (`067eb1d36`, `649993a39`, `121697136`)

- **`pactum` → `implendum` keyword rename.** Retire the `pactum` contract keyword in favour of `implendum` (gerundive of *implere*, paired with `implet`). Migrate all lexer, parser, HIR, codegen, exempla, stdlib HAL signature blocks, and factory docs. (`22c53fe5a`)

- **Modulus call diagnostic enforcement.** Propagate `@ nondum` availability from modulus method lowering into typecheck and apply SEM017 / unknown-method diagnostics to modulus calls, matching the existing enforcement on implendum interface calls. (`7de3024de`)

### Other changes
- `docs(norma)`: add stdlib architecture README as north-star vision — documents the thin-floor thesis, layering (intrinsics → chorda → formats/mathesis → HAL), and honest current state (`483d8fcf7`)
- `docs(factory)`: add transitive-library-imports goal — 317-line plan covering splice, provenance, and cycle detection for multi-hop stdlib imports (`b416593f6`)
- `docs(factory)`: refine transitive-library-imports goal with loader-path verification of package.rs and the norma runtime crate, collapsing stages from 7 to 6 (`2102bb0eb`)
- `docs(factory)`: close tensor-types goal as complete — sync status, mark success criteria satisfied, record evidence (`959ad734d`, `6e7f95e88`)
- `docs(factory)`: reframe DEFER-029 resolution as octeti unification with `lista<numerus<u8>>`, superseding both prior resolution paths (`518a5ea16`)
- `style(radix)`: `cargo fmt` MIR stratum files as post-merge cleanup after native-stdlib merge (`b697d9ed9`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
