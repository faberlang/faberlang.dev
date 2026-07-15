# Agent-first Faber documentation website plan

**Status:** queued — begins after the Faber 1.0 RC release process closes
**Pipeline:** Goal Forge → Goal Check → delivery/factory implementation
**Public origin:** `https://faberlang.dev`
**Primary user:** an agent encountering Faber with no private repository access
**Secondary user:** a human learning, evaluating, or referencing Faber

## Purpose

Build a public, versioned documentation website from which an unfamiliar agent
can discover Faber, learn the supported language and package contract, build a
real program, diagnose errors, and verify the result without conversational
context or access to private Radix implementation material.

Human readability, navigation, and visual design matter, but they are layered
over the same authoritative corpus. The project must not create separate human
and agent documentation truths.

This plan intentionally ignores Abbotik's former platform-as-a-service product
model. It reuses only the agent-discovery and documentation architecture proven
in the Abbotik website work.

## Queue and dependency

Do not begin implementation during the Faber 1.0 RC release campaign.

The release process supplies the documentation version, supported capabilities,
CLI behavior, release notes, target matrix, diagnostics, provider manifests, and
clean installed-layout evidence. Starting the website first would cause it to
publish moving or invented claims. Versioned documentation must also consume
Faber's [major-parity and language-lock policy](../../faber/docs/release/policy.md):
Faber 1 is an odd-major development line, while an even-major LTS line requires
its own lock evidence. A version number alone is never evidence that a language
contract is locked.

After the release campaign closes:

1. Run Goal Forge against this plan and the released evidence.
2. Save one focused, agent-ready website goal with an explicit public/private
   export boundary.
3. Run Goal Check on that goal.
4. If Goal Check passes, lower the goal through delivery and factory for
   implementation.
5. If Goal Check fails, repair the goal rather than improvising implementation.

Production DNS, public deployment, analytics, account creation, outbound
announcement, or publication remains operator-gated even after local
implementation passes.

## Desired end state

An isolated agent can be told:

> Read `https://faberlang.dev/llms.txt`, determine how Faber works, and build a
> Faber package that uses a documented native capability and includes tests.

Using only the public website and a released Faber toolchain, it can then:

1. identify the documentation and compiler version;
2. understand the supported product lane and limitations;
3. find package layout and manifest rules;
4. find exact language syntax without inventing constructs;
5. identify the relevant host provider routes;
6. create, check, build, run, and test a package;
7. interpret stable diagnostics and repair invalid source;
8. distinguish runtime capabilities from external libraries;
9. avoid unsupported target claims;
10. cite stable, versioned documentation URLs.

A human can follow the same corpus through rendered HTML, tutorials, search,
and accessible navigation.

## Documentation invariants

### One authoritative corpus

Markdown, HTML, agent skills, indexes, and contract bundles are generated or
assembled from the same versioned sources. Human rendering must not restate a
second manually maintained contract.

### Released truth only

Every public claim maps to released behavior, an executable test, a generated
contract, or an explicitly labeled limitation. Research, factory plans,
campaigns, private regression artifacts, and unreleased architecture are not
current documentation.

### Private Radix stays private

The site consumes a fail-closed public contract export from Radix. It never
recursively copies private Radix documentation or links users to inaccessible
private implementation paths.

### External projects stay external

Norma, Triga, Cista, and other packages own their own documentation and release
cycles. Faber documentation explains how to resolve and use them, but does not
absorb their full reference material into the language contract.

### Plain text is first-class

Important content is usable without JavaScript, browser automation, or visual
DOM interpretation. Every normative page has a stable Markdown or raw-text
representation in addition to human HTML.

### Versioned and cacheable

Every document identifies the Faber version and release lane it describes.
Stable versioned URLs
are authoritative; `latest` is only a convenience alias.

## Abbotik patterns to carry forward

The Abbotik reference repository separates public discovery into a dedicated
`web` service and demonstrates several useful patterns.

### Root content negotiation

The canonical root serves HTML to browsers and the agent primer when a client
requests Markdown:

```http
GET /
Accept: text/markdown
```

The response varies on `Accept` and emits `Vary: Accept`.

### HTTP discovery links

The root response advertises documentation, machine catalogs, and the Markdown
alternate through HTTP `Link` headers so an agent need not scrape HTML.

### Concise `llms.txt`

`/llms.txt` is an orientation and reading router, not the entire manual. It
identifies the product, version, supported lane, limitations, canonical docs,
and machine-readable entry points.

### Agent Skills Discovery

`/.well-known/agent-skills/index.json` lists focused `SKILL.md` documents with:

- stable names;
- routing descriptions;
- direct URLs;
- SHA-256 digests.

Each skill says when to use it, which choice to make, which canonical docs to
read, and which skills are adjacent. Skills route to truth rather than duplicate
it.

### Machine catalog

Abbotik uses a well-known linkset to advertise service documentation and
machine surfaces. Faber should adapt the pattern to a language/toolchain
catalog rather than copying API/PaaS semantics.

### Robots, sitemap, and content intent

Machine entry points appear in the sitemap. Robots policy explicitly covers
search and agent retrieval. Any AI content-signal header or directive must be
verified before reliance, but the intent should be explicit.

### Thin delivery adapters

Abbotik serves one generated asset contract through both Rust/Axum and a
Cloudflare Worker. Faber should likewise make generated assets authoritative
and keep deployment adapters thin.

### Contract tests

Discovery routes, media types, content negotiation, links, digests, sitemap,
robots, and well-known assets receive executable acceptance tests.

## Abbotik limitations not to copy

- The current Abbotik shell advertises `/docs` before the generated docs corpus
  is complete. Faber must not publish discovery links to missing content.
- The newer skill index points several skills back to `/llms.txt`; the richer
  legacy pattern of one skill URL per domain is preferable.
- The legacy `llms.txt` grew into a very large route catalog. Faber should keep
  its primer small and move detail into focused skills and canonical docs.
- OAuth, MCP, API catalog, and service metadata are published only when Faber
  actually has those contracts. More `.well-known` routes are not inherently
  better.
- Legacy or private docs are source material, not automatic public truth.

## Public route contract

### Human and agent root

```text
/
/index.html
/index.css
/llms.txt
/robots.txt
/sitemap.xml
/health
```

`/` serves HTML normally and Markdown when `Accept: text/markdown` is requested.

### Documentation

```text
/docs
/docs/latest/*
/docs/1.0.0-rc.1/*
/raw/1.0.0-rc.1/*.md
```

The exact version in the first implementation will be the released version
available when Goal Forge runs. Versioned URLs are immutable after publication.

### Agent discovery

```text
/.well-known/faber-language
/.well-known/agent-skills/index.json
/.well-known/agent-skills/quickstart/SKILL.md
/.well-known/agent-skills/language-syntax/SKILL.md
/.well-known/agent-skills/packages/SKILL.md
/.well-known/agent-skills/build-run/SKILL.md
/.well-known/agent-skills/testing/SKILL.md
/.well-known/agent-skills/formatting/SKILL.md
/.well-known/agent-skills/diagnostics/SKILL.md
/.well-known/agent-skills/effects/SKILL.md
/.well-known/agent-skills/targets/SKILL.md
/.well-known/agent-skills/libraries/SKILL.md
/.well-known/agent-skills/fmir/SKILL.md
```

### Machine-readable contracts

```text
/contracts/<version>/grammar.ebnf
/contracts/<version>/keywords.json
/contracts/<version>/types.json
/contracts/<version>/operators.json
/contracts/<version>/targets.json
/contracts/<version>/diagnostics.json
/contracts/<version>/providers.json
/contracts/<version>/documents.json
/contracts/<version>/examples.json
/contracts/<version>/checksums.json
```

Do not advertise a bundled contract archive until it is generated with bytes,
served by the website, assigned a content type, and covered by checksum
validation.

## `llms.txt` contract

The primer should remain short enough for immediate ingestion. It contains:

- Faber identity and current documentation version;
- primary Rust package/native binary lane;
- advanced `fmir*` posture;
- explicit limitations for Go, TypeScript, Wasm, LLVM, Metal, WGSL, and
  S-expression surfaces;
- start-here reading order;
- package/build/test links;
- diagnostic and target indexes;
- agent-skill index;
- machine-contract URLs;
- external-project links for Norma, Triga, and Cista;
- a warning not to invent syntax or infer runtime support from emit support.

A generated `llms-full.txt` may concatenate the normative corpus with source URL
markers, but it is not a substitute for focused pages and indexes.

## Agent skill contract

Each published skill contains:

- name and concise description;
- documentation version;
- "Use this skill when" routing triggers;
- canonical choice rules;
- canonical versioned documentation links;
- related skills;
- no private implementation paths;
- a digest published in the skill index.

Example responsibility boundaries:

- `quickstart`: cold-start package creation and verification;
- `language-syntax`: grammar and semantic reference routing;
- `packages`: layout, manifests, imports, external dependencies;
- `build-run`: supported application build and execution lane;
- `effects`: `ad`, runtime builtins, native host, and five provider families;
- `targets`: capability dimensions rather than a generic support label;
- `diagnostics`: stable code lookup and repair workflow;
- `libraries`: external Norma/Triga/Cista resolution boundary;
- `fmir`: advanced executable package/runtime path without presenting MIR as
  the public release name.

## Information architecture

### Agent start

- Quickstart.
- Task router.
- Constraints and unsupported assumptions.
- Verification workflow.

### Language

- Lexical structure and grammar.
- Declarations and bindings.
- Functions, closures, and control flow.
- Types, generics, optionality, and nullable domains.
- Failures and recovery.
- Collections, tensors, modules, imports, and annotations.
- Effects and `ad` routing.

Every language page includes valid and invalid examples, semantic rules,
related grammar productions, diagnostic codes, and tested example links.

### Packages and tools

- Package layout and `faber.toml`.
- Modules, imports, dependencies, and lockfiles.
- `check`, `build`, `run`, `test`, `format`, `explain`, `targets`, and `script`.
- Generated artifacts and core runtime/host behavior.
- External library installation and resolution.

### Host effects

- Runtime builtin routes.
- Native host selection.
- Provider pages for `aleator`, `consolum`, `processus`, `solum`, and `tempus`.

Provider reference should be generated from released capability manifests and
include route, opener type, result type, sync/async behavior, platform
assumptions, examples, and security implications.

### Targets

Document parse/check, emit, validate, build, run, package, and status dimensions
separately. Never convert those dimensions into one ambiguous "supported"
label.

### Diagnostics

Every released diagnostic has a stable page with code, meaning, likely cause,
invalid example, corrected example, related rule, and structured arguments where
useful.

### Examples

Publish complete packages rather than context-free snippets. Each example has
versioned metadata, exact commands, expected output, required external packages,
supported target, concepts demonstrated, and executable verification evidence.

## Source ownership and export

The website repository assembles public material from explicit inputs:

- Faber owns CLI, package, and tool behavior.
- Radix exports the public language contract, grammar, diagnostics, and target
  facts through a fail-closed allowlist.
- Host providers own provider manifests.
- Norma, Triga, and Cista own their project documentation and expose versioned
  links or public exports.
- Examples owns runnable public packages and metadata.

The website build uses an explicit source manifest. It does not traverse sibling
repositories looking for content.

Public export rejects:

- `docs/factory` and campaign material;
- private repository URLs;
- compiler `.rs` implementation paths;
- deferred/internal issue IDs;
- regression expectations and private fixtures;
- unpublished target or roadmap claims;
- absolute developer filesystem paths;
- broken or inaccessible links.

## Build and validation

The generated website must prove:

- deterministic output from pinned source commits;
- idempotent public export;
- correct content types;
- root Markdown negotiation and `Vary: Accept`;
- discovery `Link` headers;
- every skill URL exists and matches its digest;
- every docs/catalog link resolves;
- sitemap includes human and machine entry points;
- robots policy is explicit;
- no private-content leakage;
- target docs match released capability data;
- diagnostics match released codes;
- all published examples pass with the documented released toolchain;
- HTML is accessible, responsive, keyboard-operable, and usable with reduced
  motion;
- core documentation remains usable without JavaScript.

## Agent acceptance trial

Run a clean agent with no private repository context and only the public origin.
Ask it to:

1. discover Faber through `/` or `/llms.txt`;
2. create a minimal package;
3. use one documented native provider capability;
4. add and run tests;
5. intentionally trigger and repair a diagnostic;
6. explain why an emit-only target is not a package runtime;
7. identify Norma, Triga, and Cista as external projects.

The trial passes only when the resulting package checks, builds, runs, and tests
through documented commands without hidden local knowledge.

## Implementation sequence after Goal Check

1. Public-contract inventory and source authority.
2. Fail-closed Radix/public export and leakage gate.
3. Versioned machine contract schemas and generators.
4. `llms.txt`, root negotiation, discovery headers, and language catalog.
5. Agent skill index and focused `SKILL.md` files.
6. Core language, package, tool, target, provider, and diagnostic documentation.
7. Executable examples and metadata pipeline.
8. Human HTML renderer, navigation, search, and visual system.
9. Contract tests and isolated agent trial.
10. Local deployment preview.
11. Operator review before DNS or production publication.

This sequence is provisional intake for Goal Forge. It must not be mistaken for
an implementation-ready delivery DAG before Goal Check passes.

## Stop conditions

Pause rather than improvise if:

- released behavior and proposed public claims disagree;
- public export requires private implementation material;
- a page family has no authoritative owner;
- agent discovery points to missing or stale docs;
- example validation requires unreleased compiler behavior;
- an external project would need to be copied rather than linked/versioned;
- the build leaks private paths or historical factory content;
- production DNS, deployment, analytics, accounts, or announcements are needed.
