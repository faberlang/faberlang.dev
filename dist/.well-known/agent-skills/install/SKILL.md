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

- **Version:** 1.15.1
- **Tag:** `faber-v1.15.1`
- **Published:** 2026-10-21
- **Bundled compiler:** Radix 0.84.0
- **Release page:** https://github.com/faberlang/releases/releases/tag/faber-v1.15.1
- **License:** MIT OR Apache-2.0

## Archives

| Platform | Archive | Checksum |
|---|---|---|
| macOS arm64 | https://github.com/faberlang/releases/releases/download/faber-v1.15.1/faber-v1.15.1-aarch64-apple-darwin.tar.gz | https://github.com/faberlang/releases/releases/download/faber-v1.15.1/faber-v1.15.1-aarch64-apple-darwin.tar.gz.sha256 |
| Linux x64 | https://github.com/faberlang/releases/releases/download/faber-v1.15.1/faber-v1.15.1-x86_64-unknown-linux-gnu.tar.gz | https://github.com/faberlang/releases/releases/download/faber-v1.15.1/faber-v1.15.1-x86_64-unknown-linux-gnu.tar.gz.sha256 |

The archive ships one file, `bin/faber`; the reader packs and Norma are built into the binary. These are the only two archives published. On any other platform, stop and tell the human.

## Procedure

1. Detect platform (Darwin arm64 vs Linux x86_64).
2. Download the matching `.tar.gz` and `.sha256`.
3. Verify the checksum by comparing the first hash field from the `.sha256` file to the local archive hash. The published checksum line may name the original build path.
4. Extract. Move `bin/faber` onto your `PATH`.
5. Run `faber --version` and `faber explain SEM001`. The first prints the CLI version and the second prints a diagnostic explanation. If `faber` is not found, the directory holding the binary is not on `PATH`.
6. Prove it with a first program check (below).

### macOS arm64

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.15.1/faber-v1.15.1-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.15.1/faber-v1.15.1-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv bin/faber /usr/local/bin/faber
faber --version
```

### Linux x64

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.15.1/faber-v1.15.1-x86_64-unknown-linux-gnu.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.15.1/faber-v1.15.1-x86_64-unknown-linux-gnu.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(sha256sum faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv bin/faber /usr/local/bin/faber
faber --version
```

## First program check

With the CLI on `PATH`, write a small program to a temporary file, type-check
it, and run it. `norma:*` resolves from the Norma library embedded in the
binary, so this needs no other download.

```bash
tmp=$(mktemp -d)
printf 'main {\n    print "Hello, world!"\n}\n' > "$tmp/hello.fab"
faber check "$tmp/hello.fab"
faber run "$tmp/hello.fab"
```

`faber run` prints `Hello, world!`. The install is done when `faber --version`
prints and both commands pass. For a real package (manifest, dependencies,
`--library-home`), use the `packages` skill.

## Notes

- Prefer prebuilts. Building from https://github.com/faberlang/faber (`cargo build --release -p faber`) gives the open-source compiler front end and MIR runner. The release binaries also include the target code generators, which are not in that repository.
- Write the verify commands as shown. Do not run the archive's contents before the checksum passes.
- After install, fetch https://faberlang.dev/agents/index.md and follow only the links that page names.

## Related

- https://faberlang.dev/install.md
- https://faberlang.dev/agents/index.md
- skill: `language`
- skill: `packages`
