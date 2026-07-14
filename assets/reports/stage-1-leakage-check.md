# Stage 1 Local Leakage Check

Date: 2026-07-13
Scope: `faberlang.dev` local RC1 evaluate/learn packet
Status: local-only report

## RC1 Evidence

Frozen private-preview evidence for `1.0.0-rc.1` exists as a website asset
version, local contract directory under `assets/docs/1.0.0-rc.1/` and
`assets/contracts/1.0.0-rc.1/`, and a local release-profile Faber CLI build.
The machine-readable evidence source is
`/reports/rc1-provenance-manifest.json`; the report prose must match that
manifest rather than revalidating independent hard-coded provenance strings.
I did not find a released public artifact, public source export, deployed site,
live registry proof, or operator-approved install route in this repo.
Therefore the packet uses RC1 as a local preview label and keeps public
release/install claims gated.

## Local Binary Evidence

Frozen snapshot source:

- Evidence contract: `frozen_private_preview_snapshot`.
- Snapshot date: `2026-07-14`.
- Manifest route: `/reports/rc1-provenance-manifest.json`.

- Evidence commit: `faber 1a7001fe4bb26b0f20361e12aa4df8f4dcd604d1`
  (`Refresh RC1 evidence after provider fix`).
- Website sync commit:
  `faberlang.dev 08390f9a9234629fbaaabff38488f196da74d10e`
  (`Sync private preview evidence to latest RC1 hash`).
- Compiler provenance: `82d6230ec`.
- Faber provenance: `edbb54f496e5`.
- Build command: `cargo build --release --bin faber`.
- Version command result: `faber 1.0.0-rc.1`.
- Frozen local binary path: `target/release/faber`.
- Local SHA-256: `77203c7302eb025bbf3ddd01aae798a96f0ca97cc0219066a6a64a991405700b`.
- Size observed locally: `16M`.

This is frozen private-review evidence for the named commits only. It is not a
public download, install route, pushed tag, or deployment. During verification,
the evidence record was refreshed at
`faber 1a7001fe4bb26b0f20361e12aa4df8f4dcd604d1` from the provenance above,
then incorporated into
`faberlang.dev 08390f9a9234629fbaaabff38488f196da74d10e`; do not treat the
checksum above as a public release artifact checksum.

## Autograd-First Boundary

Current proximity evidence:

- `faber-runtime 4f8d452`.
- `examples 310cef1`.
- exact rung3 oracle fixtures exist for private strategy review.

Boundary:

- This packet makes no generated-autograd claim.
- Output-checked device/autograd floor: 0.
- Do not claim PyTorch-equivalence, rendering, source export, public deploy,
  install route, or live registry from this evidence.

## Export Manifest

Primary local preview files:

- `/index.html`
- `/index.css`
- `/llms.txt`
- `/llms-full.txt`
- `/.well-known/faber-language.json`
- `/.well-known/agent-skills/index.json`
- `/.well-known/agent-skills/quickstart/SKILL.md`
- `/.well-known/agent-skills/language-syntax/SKILL.md`
- `/.well-known/agent-skills/packages/SKILL.md`
- `/.well-known/agent-skills/build-run/SKILL.md`
- `/.well-known/agent-skills/testing/SKILL.md`
- `/.well-known/agent-skills/diagnostics/SKILL.md`
- `/.well-known/agent-skills/effects/SKILL.md`
- `/.well-known/agent-skills/targets/SKILL.md`
- `/.well-known/agent-skills/libraries/SKILL.md`
- `/docs/__DOCS_VERSION__/evaluate/index.md`
- `/docs/__DOCS_VERSION__/learn/index.md`
- `/docs/__DOCS_VERSION__/reference/index.md`
- `/docs/__DOCS_VERSION__/targets/index.md`
- `/docs/__DOCS_VERSION__/examples/index.md`
- `/docs/__DOCS_VERSION__/quickstart.md`
- `/docs/__DOCS_VERSION__/language/index.md`
- `/docs/__DOCS_VERSION__/packages/index.md`
- `/docs/__DOCS_VERSION__/effects/index.md`
- `/docs/__DOCS_VERSION__/diagnostics/index.md`
- `/contracts/__DOCS_VERSION__/grammar.ebnf`
- `/contracts/__DOCS_VERSION__/keywords.json`
- `/contracts/__DOCS_VERSION__/types.json`
- `/contracts/__DOCS_VERSION__/operators.json`
- `/contracts/__DOCS_VERSION__/targets.json`
- `/contracts/__DOCS_VERSION__/diagnostics.json`
- `/contracts/__DOCS_VERSION__/providers.json`
- `/contracts/__DOCS_VERSION__/documents.json`
- `/contracts/__DOCS_VERSION__/checksums.json`
- `/reports/rc1-private-preview-checklist.md`
- `/reports/stage-1-leakage-check.md`

## Leakage Result

The packet is intended to avoid:

- private implementation internals as proof;
- internal planning ledgers and task IDs;
- install, source-build, public-repo, live-registry, analytics, roadmap, or
  deployment claims;
- public runnability claims without public examples and run evidence;
- GPU/browser/product-target claims beyond tracked status.

Known remaining gates:

- replace placeholder public artifact checksums and document digests;
- generate or approve the public language export;
- select public examples and attach run evidence;
- approve install route, licensing, repository publication, deployment,
  analytics, and announcements before any public launch.

## Local Validation

Commands run for this packet:

```sh
cargo fmt --check
cargo test
cargo run --bin validate_public_packet
cargo build --release --bin faber
target/release/faber --version
sha256sum target/release/faber
PORT=18084 cargo run --bin faber-web
HTTP smoke check against `http://127.0.0.1:18084/docs/1.0.0-rc.1/evaluate/index.md`
```

Results:

- `cargo fmt --check`: pass.
- `cargo test`: pass.
- local Faber release-profile build: pass.
- local Faber version check: `faber 1.0.0-rc.1`.
- local Faber SHA-256 recorded above.
- route smoke: homepage, evaluate, learn, reference, targets, examples,
  `llms.txt`, agent-skill index, and leakage report returned `200`; removed
  internal skill route returned `404`.
- public packet validator: checks required routes, forbidden private/source
  terms, prohibited public claims, local-only labels, removed internal route
  references, cataloged document assets, sitemap/document coverage, embedded
  routes, internal route-like links, discovery JSON URLs, and JSON syntax.
