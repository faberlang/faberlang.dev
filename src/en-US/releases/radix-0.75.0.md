+++
title = "Radix 0.75.0"
section = "releases"
order = 22
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.75.0 |
| **Tag** | `radix-v0.75.0` |
| **GitHub** | [radix-v0.75.0](https://github.com/faberlang/releases/releases/tag/radix-v0.75.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.75.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.75.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.75.0/radix-v0.75.0-aarch64-apple-darwin.tar.gz) | 3.1 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.75.0/radix-v0.75.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.75.0/radix-v0.75.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.75.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Faber 1.0 release-preparation documentation boundary: RR4 evidence close, CPO
contract archive, operator review drafting, and synthetic-history reset. All 7
commits land within a single day and touch only documentation and one lockfile
line.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 7 |
| Date span | 2026-07-13 |
| Lockfile changes | 1 (`Cargo.lock`) |
| New factory docs | 3 files (~682 lines) |

### Major tracks

- **Route Faber 1.0 preparation campaign** — Scaffold `docs/factory/faber-v1-release/CAMPAIGN.md` (319 lines) and a factory README index. Defines the campaign structure for the Faber 1.0 release. (`82283f2aa`)

- **Close RR4 release evidence** — Tighten the RR4 readiness matrix in `docs/factory/faber-hir-v1/release-readiness.md` (41 insertions, 47 deletions). Removes stale rows and marks remaining evidence as complete. (`53f3e8c0a`)

- **Archive CPO v1 release contract** — Record the head-CPO release contract (231 lines) in `docs/factory/faber-hir-v1/head-cpo-v1-release-contract.md` as historical reference. (`bc1a51238`)

- **Draft and iterate Faber 1.0 operator review** — Three-commit chain building `stage-3-operator-review.md`:
  - Present initial review content (131 new lines) plus CAMPAIGN.md edits (`224bd5387`)
  - Rework for scannability (+159 −27) (`402b1c239`)
  - Reset synthetic history boundary (+28 −48) to mark the pre-release docs seam (`2d0243bcf`)

### Other changes

- Record `consolum` libc dependency in `Cargo.lock` (`9aec9f261`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
