# Stage 1 Local Leakage Check

Date: 2026-07-13
Scope: `faberlang.dev` local RC1 evaluate/learn packet
Status: local-only report

## RC1 Evidence

Local evidence for `1.0.0-rc.1` exists as a website asset version, local
contract directory under `assets/docs/1.0.0-rc.1/` and
`assets/contracts/1.0.0-rc.1/`, and a local release-profile Faber CLI build.
I did not find a released public artifact, public source export, deployed site,
live registry proof, or operator-approved install route in this repo.
Therefore the packet uses RC1 as a local preview label and keeps public
release/install claims gated.

## Local Binary Evidence

Evidence source:

- Faber checkout: clean HEAD `5d508d7` (`Wire library namespace info into package Rust generation`).
- Build command: `cargo build --release --bin faber`.
- Version command result: `faber 1.0.0-rc.1`.
- Local binary path: `target/release/faber`.
- Local SHA-256: `d0b23f8b9e03422a467d5ab2ccf7c4e78e0e3f497662ab29b4826af6953ab92e`.
- Size observed locally: `16M`.

This is private-review evidence for the local tree only. It is not a public
download, install route, pushed tag, or deployment. During verification, the
Faber checkout was clean at HEAD `5d508d7`; do not treat the checksum above as
a public release artifact checksum.

## Export Manifest

Primary local preview files:

- `/index.html`
- `/index.css`
- `/llms.txt`
- `/llms-full.txt`
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
- `/contracts/__DOCS_VERSION__/*`
- `/reports/rc1-private-preview-checklist.md`

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
  references, sitemap/document coverage, embedded routes, and JSON syntax.
