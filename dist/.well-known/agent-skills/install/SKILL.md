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

- **Version:** 1.14.0
- **Tag:** `faber-v1.14.0`
- **Published:** 2026-10-16
- **Bundled compiler:** Radix 0.84.0
- **Release page:** https://github.com/faberlang/releases/releases/tag/faber-v1.14.0
- **License:** MIT OR Apache-2.0

## Archives

| Platform | Archive | Checksum |
|---|---|---|
| macOS arm64 | https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-aarch64-apple-darwin.tar.gz | https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-aarch64-apple-darwin.tar.gz.sha256 |
| Linux x64 | https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-x86_64-unknown-linux-gnu.tar.gz | https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-x86_64-unknown-linux-gnu.tar.gz.sha256 |

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
  https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-aarch64-apple-darwin.tar.gz.sha256
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
  https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-x86_64-unknown-linux-gnu.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-x86_64-unknown-linux-gnu.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(sha256sum faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv bin/faber /usr/local/bin/faber
sudo mv share/faber /usr/local/share/faber
faber --version
```

## First package check

With the CLI on `PATH`, type-check a real package. `norma:*` resolves from
the Norma library embedded in the binary. The source libraries `triga:*`,
`gradus:*` and `tela:*` are checkouts: pass `--library-home <DIR>` (or set
`[paths] library_home` in `faber.toml`) to a directory that holds them, and run
`faber doctor` to see which libraries `faber` can find.

```bash
git clone https://github.com/faberlang/examples.git
faber check examples/coreutils/packages/wc
```

Then write and check a hello program with the `packages` skill. The install is
done when `faber --version` prints and that program passes `faber check`.

## Notes

- Prefer prebuilts: the official binary carries every code generator. A build from the public source (https://github.com/faberlang/faber, `cargo build --release -p faber`) gives `check`, `run`, `test`, `format`, `convert` and the C emitter only.
- Write the verify commands as shown. Do not run the archive's contents before the checksum passes.
- After install, fetch https://faberlang.dev/agents/index.md and follow only the links that page names.

## Related

- https://faberlang.dev/install.md
- https://faberlang.dev/agents/index.md
- skill: `language`
- skill: `packages`
