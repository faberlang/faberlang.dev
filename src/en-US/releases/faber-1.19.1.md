+++
title = "Faber 1.19.1"
description = "Release notes and install details for Faber 1.19.1."
section = "releases"
order = 10
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.19.1 |
| **Tag** | `faber-v1.19.1` |
| **GitHub** | [faber-v1.19.1](https://github.com/faberlang/releases/releases/tag/faber-v1.19.1) |
| **Published** | 2026-11-09 |
| **License** | MIT OR Apache-2.0 |

## Install this version {#install}

Pinned download for **Faber 1.19.1**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.19.1-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.19.1/faber-v1.19.1-aarch64-apple-darwin.tar.gz) | 49.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.19.1/faber-v1.19.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.19.1-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.19.1/faber-v1.19.1-x86_64-unknown-linux-gnu.tar.gz) | 56.0 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.19.1/faber-v1.19.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
# The installer verifies the checksum and installs a versioned
# binary that `faber update` and `faber versions` manage.
curl -fsSL https://raw.githubusercontent.com/faberlang/faber/main/install.sh \
  | sh -s -- --version 1.19.1
export PATH="$HOME/.faber/bin:$PATH"
faber --version
```

## Release notes {#notes}

> **Status**: final — tagged `faber/v1.19.1` on 2026-11-09

Faber 1.19.1 is a patch release. It prints `u64` values above 2⁶³ correctly on `--device cpu`, which was a known issue in 1.19.0, and it fixes a MIR validation failure on methods with an immutable `ref` parameter.

> **Experimental through version 1.** The language changes constantly, and breaking changes ship in minor releases. Faber 1.19 carries no stability promise, and neither does any other 1.x release. A 2.0 release is planned for when the language is largely stable.

### Fixes

**`u64` above 2⁶³ on `--device cpu`.** The Cranelift JIT host half of a device program printed such a value as signed when it was read back from a tensor, and refused a `u64` literal that large. Both now print what `--device reference` prints. Integer comparison, approximate equality on integers and the typing of hex `u64` literals are unchanged.

**Immutable `ref` parameters pass MIR validation.** A call that passed an argument to an immutable `ref` parameter of a method in the same unit was rejected by MIR validation, because only mutable access accepted the referenced payload as a place. Immutable access now accepts it too.

**Norma conformance packages.** The `fs` and `leaves` round-trip test packages put their header first and handle their failable calls, so `faber test` runs their cases again.

### Install

The installer is the recommended route; it verifies the checksum and installs a versioned binary that `faber update` and `faber versions` manage:

```bash
curl -fsSL https://raw.githubusercontent.com/faberlang/faber/main/install.sh | sh
```

An existing managed install upgrades with `faber update`.

---

[All releases](/releases/) · [Start](/start/)
