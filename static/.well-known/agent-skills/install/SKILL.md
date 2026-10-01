---
name: "install"
description: "Download and verify the current Faber CLI release for macOS arm64 or Linux x64."
---

# Install Faber CLI

## Use this skill when

- you need a working `faber` binary on PATH
- you are verifying a release archive or checksum
- a human asks how to install Faber

## Current release

- **Version:** 1.8.0
- **Tag:** `faber-v1.8.0`
- **Published:** 2026-08-24
- **Bundled compiler:** Radix 0.83.0
- **Release page:** https://github.com/faberlang/releases/releases/tag/faber-v1.8.0
- **Human page:** https://faberlang.dev/en-US/start/install.html

## Archives

| Platform | Archive | Checksum |
|---|---|---|
| macOS arm64 | https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-aarch64-apple-darwin.tar.gz | https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-aarch64-apple-darwin.tar.gz.sha256 |
| Linux x64 | https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-x86_64-unknown-linux-gnu.tar.gz | https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-x86_64-unknown-linux-gnu.tar.gz.sha256 |

The archive ships `bin/faber` and `share/faber`. Install both, so the reader packs resolve beside the binary.

## Procedure

1. Detect platform (Darwin arm64 vs Linux x86_64).
2. Download the matching `.tar.gz` and `.sha256`.
3. Verify the checksum by comparing the first hash field from the `.sha256` file to the local archive hash. The published checksum line may name the original build path.
4. Extract. Move `bin/faber` and `share/faber` into place together.
5. Run `faber --version` and `faber explain SEM001`.

### macOS arm64

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv bin/faber /usr/local/bin/faber
sudo mv share/faber /usr/local/share/faber
faber --version
```

### Linux x64

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-x86_64-unknown-linux-gnu.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.8.0/faber-v1.8.0-x86_64-unknown-linux-gnu.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(sha256sum faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv bin/faber /usr/local/bin/faber
sudo mv share/faber /usr/local/share/faber
faber --version
```

## Notes

- Prefer prebuilts. Building from source requires the private Radix tree.
- After install, fetch https://faberlang.dev/agents/index.md and follow only the links that page names.

## Related

- https://faberlang.dev/llms.txt
- https://faberlang.dev/agents/index.md
- skill: `language`
- skill: `packages`
