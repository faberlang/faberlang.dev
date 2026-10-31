+++
title = "Faber 1.18.1"
description = "Release notes and install details for Faber 1.18.1."
section = "releases"
order = 9
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.18.1 |
| **Tag** | `faber-v1.18.1` |
| **GitHub** | [faber-v1.18.1](https://github.com/faberlang/releases/releases/tag/faber-v1.18.1) |
| **Published** | 2026-10-31 |
| **License** | MIT OR Apache-2.0 |

## Install this version {#install}

Pinned download for **Faber 1.18.1**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.18.1-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.18.1/faber-v1.18.1-aarch64-apple-darwin.tar.gz) | 33.6 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.18.1/faber-v1.18.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.18.1-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.18.1/faber-v1.18.1-x86_64-unknown-linux-gnu.tar.gz) | 37.7 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.18.1/faber-v1.18.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
# The installer verifies the checksum and installs a versioned
# binary that `faber update` and `faber versions` manage.
curl -fsSL https://raw.githubusercontent.com/faberlang/faber/main/install.sh \
  | sh -s -- --version 1.18.1
export PATH="$HOME/.faber/bin:$PATH"
faber --version
```

## Release notes {#notes}

> **Status**: final — published 2026-10-31

Faber 1.18.1 is a patch release. It fixes Norma imports on an installed `faber`, a load failure on `.fhirpkg` artifacts and a Cranelift failure on Linux, and it brings the public source up to date. The language is unchanged from 1.18.0.

> **Experimental through version 1.** The language changes constantly, and breaking changes ship in minor releases. Faber 1.18 carries no stability promise, and neither does any other 1.x release.

### Fixes

**`faber format`, `emit`, `test` and `verify` resolve `norma:*` on an installed binary.** These commands failed with `PKG001:unknown_library_module` on any file importing Norma, even though `faber check` and `faber run` accepted it. They now use the Norma library embedded in the binary, as `check` and `run` do. A `--library-home` flag or a manifest's `[paths] library_home` still wins.

**`.fhirpkg` artifacts with interfaces load again.** A module declaring an interface failed to load from its artifact with `dangling DefId index`. `faber check`, `run` and `build` were not affected.

**Cranelift handles large return values on x86-64.** On Linux, a function returning a large value failed with Cranelift's "too many return values" error, because x86-64 has fewer return registers than arm64. Such values now go through an implicit return area on both routes. A multi-value return that crosses into the runtime is refused by name.

**A target missing from the build says so.** `error[PKG001:target_not_in_this_build]:` printed no text. It now names the target, and it points at `faber targets`.

### Public source

This release brings the open-source repository up to date, including the fix for `cargo build -p faber`. The exported tree now passes `cargo test --workspace`, and the public README covers 1.18: the default engine for `faber run`, the current target table, kernels and the simulations.

`corpus-simulations/` is public from this release, and so is `docs/internals/`.

### How this release was gated

`./scripta/release-gate --locked-release-build` passed on the candidate, and `scripta/corpus-release` reported no failures on any target leg. The counts match 1.18.0: `runner` 901, `canonical` 878, `roundtrip` 872, `mir` 870, `rust` 864, `ts` 812, `go` 741, `llvm` 701, `sexp` 680, `clif` 666, `python` 642, `wasm` 611, `swift` 469. The `gpu` leg ran no cases, so it proves nothing here.

The exported public tree builds and passes `cargo test --workspace` on macOS arm64 and Linux x86-64. Its public corpus passes on the runner and in round trip on macOS.

### Known issues

The 1.18.0 known issues still apply. `faber build --target clif` does not yet work from an installed binary; that fix is planned for 1.19.
