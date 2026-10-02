---
name: "install"
description: "Download and verify the current Faber CLI release for macOS arm64 or Linux x64."
---

# Install Faber CLI

## Use this skill when

- you need a working `faber` binary on PATH
- you are verifying a release archive or checksum
- a human gave you https://faberlang.dev/install.md or asked you to install Faber

## Current release

- **Version:** 1.12.0
- **Tag:** `faber-v1.12.0`
- **Published:** 2026-10-02
- **Bundled compiler:** Radix 0.84.0
- **Release page:** https://github.com/faberlang/releases/releases/tag/faber-v1.12.0
- **License:** MIT

## Archives

| Platform | Archive | Checksum |
|---|---|---|
| macOS arm64 | https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-aarch64-apple-darwin.tar.gz | https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-aarch64-apple-darwin.tar.gz.sha256 |
| Linux x64 | https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-x86_64-unknown-linux-gnu.tar.gz | https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-x86_64-unknown-linux-gnu.tar.gz.sha256 |

The archive ships `bin/faber` and `share/faber`. Install both, so the reader packs resolve beside the binary. These are the only two archives published. On any other platform, stop and tell the human.

## Procedure

1. Detect platform (Darwin arm64 vs Linux x86_64).
2. Download the matching `.tar.gz` and `.sha256`.
3. Verify the checksum by comparing the first hash field from the `.sha256` file to the local archive hash. The published checksum line may name the original build path.
4. Extract. Move `bin/faber` and `share/faber` into place together.
5. Run `faber --version` and `faber explain SEM001`. The first prints the CLI version and the second prints a diagnostic explanation. If `faber` is not found, the directory holding the binary is not on `PATH`.
6. Prove it with a first package check (below).

### macOS arm64

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-aarch64-apple-darwin.tar.gz.sha256
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
  https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-x86_64-unknown-linux-gnu.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-x86_64-unknown-linux-gnu.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(sha256sum faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv bin/faber /usr/local/bin/faber
sudo mv share/faber /usr/local/share/faber
faber --version
```

## First package check

With the CLI on `PATH`, type-check a real package. Product packages resolve
their dependencies from the Cista package store through `faber.lock`. Set
`FABER_LIBRARY_HOME` only for an intentional local library-development
override.

```bash
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

Then write and check a hello program with the `packages` skill. The install is
done when `faber --version` prints and that program passes `faber check`.

## Notes

- Prefer prebuilts. Building from source requires the private Radix tree.
- Write the verify commands as shown. Do not run the archive's contents before the checksum passes.
- After install, fetch https://faberlang.dev/agents/index.md and follow only the links that page names.

## Related

- https://faberlang.dev/install.md
- https://faberlang.dev/agents/index.md
- skill: `language`
- skill: `packages`
