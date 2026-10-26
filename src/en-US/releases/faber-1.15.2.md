+++
title = "Faber 1.15.2"
description = "Release notes and install details for Faber 1.15.2."
section = "releases"
order = 11
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.15.2 |
| **Tag** | `faber-v1.15.2` |
| **GitHub** | [faber-v1.15.2](https://github.com/faberlang/releases/releases/tag/faber-v1.15.2) |
| **Published** | 2026-10-21 |
| **License** | MIT OR Apache-2.0 |

## Install this version {#install}

Pinned download for **Faber 1.15.2**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.15.2-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.15.2/faber-v1.15.2-aarch64-apple-darwin.tar.gz) | 20.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.15.2/faber-v1.15.2-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.15.2-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.15.2/faber-v1.15.2-x86_64-unknown-linux-gnu.tar.gz) | 22.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.15.2/faber-v1.15.2-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
# The installer verifies the checksum and installs a versioned
# binary that `faber update` and `faber versions` manage.
curl -fsSL https://raw.githubusercontent.com/faberlang/faber/main/install.sh \
  | sh -s -- --version 1.15.2
export PATH="$HOME/.faber/bin:$PATH"
faber --version
```

## Release notes {#notes}

> **Status**: final — tagged `faber/v1.15.2` on 2026-10-21

Faber 1.15.2 is a patch release. It fixes the `llvm-host` target in the released binary and makes its errors say what went wrong. The language is unchanged from 1.15.1; read the 1.15.1 notes for what 1.15 brought.

> **Experimental through version 1.** The language changes constantly, and breaking changes ship in minor releases. Faber 1.15 carries no stability promise, and neither does any other 1.x release. A 2.0 release is planned for when the language is largely stable.

### Fixes

**`llvm-host` works from the released binary.** `faber build -t llvm-host` and `faber run --target llvm-host` build a small runtime library with Cargo on first use. In every published binary up to 1.15.1 that step failed, so the target refused every program with `PKG001 llvm_host_runtime_archive_unavailable`. It now builds, and a native executable comes out:

```bash
faber init hello
faber build -t llvm-host hello
```

The target needs Cargo and an LLVM toolchain whose `llvm-as` and `clang` are the same version (on macOS, Homebrew's `llvm`; set `LLVM_HOME` to its prefix or put its `bin` on `PATH`).

**`llvm-host` errors name the cause.** A refused `llvm-host` build used to print only the code, `error[PKG001:llvm_host_toolchain_unavailable]:`, with no reason. Each refusal now says what is missing or what failed and what to do next: the tool that was not found, the runtime manifest path, or the last lines of Cargo's output when the runtime build fails. The messages follow `--diagnostics-locale` in all eight reader locales.

### Install

The installer is the recommended route; it verifies the checksum and installs a versioned binary that `faber update` and `faber versions` manage:

```bash
curl -fsSL https://raw.githubusercontent.com/faberlang/faber/main/install.sh | sh
```

An existing managed install upgrades with `faber update`. A `faber` binary copied onto `PATH` by hand runs, but `faber update` and `faber versions` cannot manage it; reinstall with the installer to adopt the managed layout.

### Known issues

The 1.15.1 known issues still apply. Other `PKG001` package refusals outside `llvm-host` can still print the code without its cause.

---

[All releases](/releases/) · [Start](/start/)
