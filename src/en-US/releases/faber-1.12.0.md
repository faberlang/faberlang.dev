+++
title = "Faber 1.12.0"
section = "releases"
order = 9
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.12.0 |
| **Tag** | `faber-v1.12.0` |
| **GitHub** | [faber-v1.12.0](https://github.com/faberlang/releases/releases/tag/faber-v1.12.0) |
| **Published** | 2026-10-02 |
| **License** | MIT |

## Install this version {#install}

Pinned download for **Faber 1.12.0**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.12.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-aarch64-apple-darwin.tar.gz) | 12.8 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.12.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-x86_64-unknown-linux-gnu.tar.gz) | 14.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-aarch64-apple-darwin.tar.gz
tar -xzf faber.tgz
# The archive ships bin/ and share/; keep them together so the
# reader packs resolve beside the binary.
sudo mv bin/faber /usr/local/bin/faber
sudo mv share/faber /usr/local/share/faber
faber --version
```

## Release notes {#notes}

> **Status**: final

Private source identity: `faber/v1.12.0`. Public input identities are recorded
in the release manifest.

---

[All releases](/releases/) · [Start](/start/)
