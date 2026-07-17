+++
title = "Install and download"
section = "install"
order = 1
sources = []
+++

Install the **Faber** CLI from the current prebuilt release. The compiler
front end ships inside the `faber` binary; you do not need a separate
Radix install for ordinary package work.

## Current release {#current-release}

| Field | Value |
|---|---|
| **Version** | 1.1.1 |
| **Tag** | `faber-v1.1.1` |
| **Release page** | [faber-v1.1.1 on GitHub](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1) |
| **License** | MIT |

## Prebuilt archives {#archives}

| Platform | Download | SHA-256 |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

The archives extract to `faber-v1.1.1-<target-triple>/faber`. The checksum files may name the original build path, so verify by comparing the first hash field against the local archive instead of relying on `sha256sum -c` path matching.

### macOS arm64 {#macos}

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
# place on PATH, e.g.:
sudo mv faber-v1.1.1-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

### Linux x64 {#linux}

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(sha256sum faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv faber-v1.1.1-x86_64-unknown-linux-gnu/faber /usr/local/bin/
faber --version
```

## Verify {#verify}

```bash
faber --version
faber explain SEM001
```

You should see a version line for the CLI and a diagnostic explanation.
If `faber` is not found, check that the directory containing the binary
is on `PATH`.

## First package check {#first-package}

With the CLI on `PATH`, clone the public examples (or any Faber package)
and type-check:

```bash
git clone https://github.com/faberlang/examples.git
# Norma stdlib is typically a sibling checkout for library packages:
# git clone https://github.com/faberlang/norma.git
faber check examples/ai-workbench/packages/faber-ai
```

More packages: [Examples](/start/examples.html). CLI surface:
[Faber build tool](/tooling/faber-build-tool.html).

## Build from source {#from-source}

Prebuilts are the recommended path for agents and most developers. Building
from source requires the private Radix compiler tree and is out of scope
for this page. Prefer the archives above unless you are working on the
compiler itself.

## Agent path {#agent-path}

Agents should load the **install** skill and the agent index rather than
scraping this HTML:

- [`/llms.txt`](/llms.txt)
- [install skill](/.well-known/agent-skills/install/SKILL.md)
- [Agent guide](/agents/index.md)
