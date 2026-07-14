# Stage 1 Local Leakage Check

Date: 2026-07-13
Scope: `faberlang.dev` local RC1 evaluate/learn packet
Status: local-only report

## RC1 Evidence

Local evidence for `1.0.0-rc.1` exists as a website asset version and local
contract directory under `assets/docs/1.0.0-rc.1/` and
`assets/contracts/1.0.0-rc.1/`. I did not find a released public binary,
public source export, deployed site, live registry proof, or operator-approved
install route in this repo. Therefore the packet uses RC1 as a local preview
label and keeps public release/install claims gated.

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

## Leakage Result

The packet is intended to avoid:

- private compiler internals as proof;
- factory ledgers and deferred task IDs;
- install, source-build, public-repo, live-registry, analytics, roadmap, or
  deployment claims;
- public runnability claims without public examples and run evidence;
- GPU/browser/product-target claims beyond tracked status.

Known remaining gates:

- replace placeholder checksums and document digests;
- generate or approve the public language export;
- select public examples and attach run evidence;
- approve install route, licensing, repository publication, deployment,
  analytics, and announcements before any public launch.

## Local Validation

Commands run for this packet:

```sh
cargo fmt --check
cargo test
find assets -type f \( -name '*.html' -o -name '*.css' -o -name '*.md' -o -name '*.txt' -o -name '*.json' -o -name '*.xml' -o -name '*.ebnf' \) -print0 | xargs -0 rg -n "docs/factory|deferred|Homebrew|curl|download|production ready|cista\.dev is live|publish your package|open source|public repo|public repository|GPU execution|WebGPU|browser execution|Full coreutils|multi-backend coreutils|HIR|MIR|FMIR|lowering|codegen|Radix|private compiler|systems language|multi-target systems language|registry and resolution service"
PORT=18084 cargo run
curl -s -o /tmp/faber-smoke -w '%{http_code}\n' http://127.0.0.1:18084/docs/1.0.0-rc.1/evaluate/index.md
```

Results:

- `cargo fmt --check`: pass.
- `cargo test`: pass.
- route smoke: homepage, evaluate, learn, reference, targets, examples,
  `llms.txt`, agent-skill index, and leakage report returned `200`; removed
  internal skill route returned `404`.
- forbidden-token scan: remaining hits are negative/gated mentions in this
  report, `llms.txt`, and evaluate/targets docs; no positive public claim was
  found for the scanned terms.
