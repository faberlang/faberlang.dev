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

- **Version:** 1.1.1
- **Tag:** `faber-v1.1.1`
- **Release page:** https://github.com/faberlang/releases/releases/tag/faber-v1.1.1
- **Human page:** https://faberlang.dev/start/install.html

## Archives

| Platform | Archive | Checksum |
|---|---|---|
| macOS arm64 | https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz | https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256 |
| Linux x64 | https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz | https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256 |

## Procedure

1. Detect platform (Darwin arm64 vs Linux x86_64).
2. Download the matching `.tar.gz` and `.sha256`.
3. Verify the checksum (`shasum -a 256 -c` or `sha256sum -c`).
4. Extract; move `faber` onto PATH.
5. Run `faber --version` and `faber explain SEM001`.

### macOS arm64 example

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz
tar -xzf faber.tgz
sudo mv faber /usr/local/bin/
faber --version
```

## Notes

- Prefer prebuilts. Building from source requires the private Radix tree.
- Windows prebuilts are not listed in 1.1.1; check the release page for new targets.
- After install, continue with the **language** or **examples** skill.

## Related

- `/llms.txt`
- `/agents/index.md`
- skill: `language`
- skill: `packages`
