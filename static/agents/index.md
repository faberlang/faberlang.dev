# Faber — agent guide

You are reading the Markdown agent entry for **Faber**, a package-oriented
programming language. This page is meant for AI agents and automated tools.

- **Product landing:** https://faberlang.dev/
- **Language portal (locale chooser):** https://faberlang.dev/porta/
- **English documentation home:** https://faberlang.dev/en-US/
- **Machine index:** https://faberlang.dev/llms.txt

Human HTML docs live under `/{site_locale}/…`. The complete authored tree is
`en-US`. Other locales ship reader packs and corpus; Thai (`th-TH`) has a
pilot translated prose slice (`index` + `start/*`). Prefer `/en-US/` links
unless the user asked for another locale.

## Mission

Help a human (or another agent) **install the CLI**, **understand language
shape**, and **open real application packages** quickly — without inventing
non-canonical syntax.

## Ordered path

1. **Index** — https://faberlang.dev/llms.txt  
2. **This guide** — https://faberlang.dev/agents/index.md  
3. **Skills catalog** — https://faberlang.dev/.well-known/agent-skills/index.json  
4. **Install skill** — https://faberlang.dev/.well-known/agent-skills/install/SKILL.md  
5. **Language skill** — https://faberlang.dev/.well-known/agent-skills/language/SKILL.md  
6. **Examples skill** — https://faberlang.dev/.well-known/agent-skills/examples/SKILL.md  
7. **Expanded map** — https://faberlang.dev/llms-full.txt  

## Install the CLI (current: 1.5.0)

Release: https://github.com/faberlang/releases/releases/tag/faber-v1.5.0

| Platform | Archive |
|---|---|
| macOS arm64 | https://github.com/faberlang/releases/releases/download/faber-v1.5.0/faber-v1.5.0-aarch64-apple-darwin.tar.gz |
| Linux x64 | https://github.com/faberlang/releases/releases/download/faber-v1.5.0/faber-v1.5.0-x86_64-unknown-linux-gnu.tar.gz |

Verify the archive by comparing the first hash field from the `.sha256` file to the local archive hash. Extract `faber-v1.5.0-<target-triple>/faber`, put it on `PATH`, run `faber --version`.

HTML install page: https://faberlang.dev/en-US/start/install.html

## Minimum language facts

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

- Type-first: `numerus a` not `a: number`.
- Glyphs: `← → ∴ ≡ ∪`.
- Nullable: `T ∪ nihil`.
- Comments: `#` alone on a line only.
- Package: `faber.toml` + `src/`.

## Real-world packages to open first

Repo: https://github.com/faberlang/examples

| Priority | Path | Why |
|---|---|---|
| 1 | `ai-workbench/packages/faber-ai` | Full multi-command CLI application |
| 2 | `vivilite` | Mailspace / agent coordination CLI |
| 3 | `corpus/` | Construct-by-construct programs + docs source |
| 4 | `coreutils` | Larger application campaign |
| 5 | `gpu-workload` | Systems / GPU track |

Site: https://faberlang.dev/en-US/examples/

## Commands you will use constantly

```bash
faber check <pkg>
faber build <pkg> -t rust
faber test <pkg>
faber explain <CODE>
faber format <pkg>
```

## Documentation map

| Need | URL |
|---|---|
| Portal (pick locale) | https://faberlang.dev/ |
| English overview | https://faberlang.dev/en-US/ |
| Short worked examples | https://faberlang.dev/en-US/cheatsheet/ |
| The language | https://faberlang.dev/en-US/language/ |
| Toolchain and CLI | https://faberlang.dev/en-US/toolchain/ |
| Device execution (GPU) | https://faberlang.dev/en-US/toolchain/cli.html#device-execution |
| Measured target support | https://faberlang.dev/en-US/toolchain/target-matrix.html |
| Source beside its lowering | https://faberlang.dev/en-US/targets/ |
| Real package source | https://faberlang.dev/en-US/examples/ |
| Reader locales, and why these | https://faberlang.dev/en-US/localization.html |
| Every version + release notes | https://faberlang.dev/en-US/releases/ |
| Licensing, repos, issues | https://faberlang.dev/en-US/open-source.html |
| Corpus pages | https://faberlang.dev/en-US/corpus/ |
| Libraries | https://faberlang.dev/en-US/libraries/ |
| EBNF | https://faberlang.dev/en-US/reference/grammar.html |

## Skills

| Name | When |
|---|---|
| install | Downloading / verifying the CLI |
| language | Writing or reviewing Faber source |
| packages | Scaffolding or building packages |
| examples | Choosing real apps to study |
| corpus | Looking up a keyword or construct |

## Anti-patterns

- Do not invent C/JS-style type annotations after names.
- Do not use `//` comments.
- Do not invent package layouts when examples already show one.
- Do not claim Radix source is public.
- Do not scrape only the homepage HTML when `/llms.txt` exists.
- Do not use bare `/start/…` paths, or any of `/syntax/`, `/features/`,
  `/tooling/`, `/ecosystem/`, `/history/`, `/references/`, as canonical docs
  URLs; those are redirect stubs from earlier information architectures.
  Prefer `/en-US/…` (or the locale the user chose).
- Do not claim GPU inference or multi-device execution is shipped. Bounded
  dual-backend training on Metal and CUDA is the current proven device claim.

## Done when

- `faber --version` works on the machine.
- You can name type-first, glyphs, nullable unions, and comment rules.
- You have opened at least one application package under `examples/`.
- You can point a human to install + examples + the skill they need next.
