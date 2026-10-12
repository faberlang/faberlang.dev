You are a professional technical translator for the Faber documentation site.

# Contract — Traditional Chinese (zh-Hant / 繁體). Traditional only, never Simplified.

Rules:
- Target locale: `zh-Hant`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Traditional Chinese reader-locale Faber using Traditional Chinese keywords where the pack overrides Simplified Chinese rows, while preserving universal Faber glyph syntax.

## English source body

Install the **Faber** CLI from the current prebuilt release. The compiler
front end ships inside the `faber` binary; you do not need a separate
Radix install for ordinary package work.

This page is written against the repository release artifacts for Faber 1.1.1.
Package-manager formulae may lag behind the repo release; if Homebrew or another
manager reports an older Radix/Faber version, prefer the archives below for this
track.

## Current release {#current-release}

| Field | Value |
|---|---|
| **Version** | 1.1.1 |
| **Tag** | `faber-v1.1.1` |
| **Release page** | [faber-v1.1.1 on GitHub](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1) |
| **All releases** | [Site releases inventory](/history/releases.html) |
| **License** | MIT |

## Prebuilt archives {#archives}

| Platform | Download | SHA-256 |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

The archives extract to `faber-v1.1.1-<target-triple>/faber`. The checksum files may name the original build path, so verify by comparing the first hash field against the local archive instead of relying on `sha256sum -c` path matching.

### macOS arm64 {#macos}

<<<FENCE 0>>>

### Linux x64 {#linux}

<<<FENCE 1>>>

## Verify {#verify}

<<<FENCE 2>>>

You should see a version line for the CLI and a diagnostic explanation.
If `faber` is not found, check that the directory containing the binary
is on `PATH`.

## First package check {#first-package}

With the CLI on `PATH`, clone the public examples (or any Faber package)
and type-check. Product packages resolve dependencies from the Cista store
through `faber.lock`; local source checkouts are only for explicit
library-development overrides.

<<<FENCE 3>>>

More packages: [Examples](/start/examples.html). CLI surface:
[Faber build tool](/tooling/faber-build-tool.html).

## Homebrew status {#homebrew}

Homebrew publication is not the authority for this start track yet. If a formula
serves an older compiler such as Radix 0.38.0 while this site documents Faber
1.1.1, treat the formula as lagging and use the prebuilt release archive. The
container verification gate for this page remains residual until formula
publication catches up.

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

## Next {#next}

| Previous | Next |
|---|---|
| [Quick tour](/start/) | [Hello, Faber](/start/hello.html) |
