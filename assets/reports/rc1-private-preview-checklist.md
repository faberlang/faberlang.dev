# RC1 Private Preview Readiness Checklist

Date: 2026-07-14
Scope: `faberlang.dev` local RC1 private-preview packet
Status: private-preview checklist; not public launch approval

## Evidence Boundary

Frozen private-preview evidence snapshot:

- Website packet version: `1.0.0-rc.1`.
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
- Local release-profile build command: `cargo build --release --bin faber`.
- Local CLI version result: `faber 1.0.0-rc.1`.
- Frozen local binary path: `target/release/faber`.
- Local SHA-256: `77203c7302eb025bbf3ddd01aae798a96f0ca97cc0219066a6a64a991405700b`.
- Size observed locally: `16M`.
- Autograd-first proximity evidence: `faber-runtime 4f8d452` and
  `examples 310cef1` have exact rung3 oracle fixtures.
- Output-checked device/autograd floor: 0.
- Boundary statement: no generated-autograd claim.

This frozen evidence supports private review of the named commits only. It
does not create a public artifact, install route, pushed tag, deployment,
analytics setup, announcement, public source export, or live registry proof.
The rung3 oracle fixtures are strategy evidence only. This packet makes no
generated-autograd claim, PyTorch-equivalence claim, rendering claim,
source-export claim, install claim, or registry claim for Faber.

## Private Preview Checklist

| Gate | Private-preview status | Public-release blocker |
| --- | --- | --- |
| Local website packet | Ready for private review after validator and route smoke pass. | Public/private export approval and deployment approval. |
| Local CLI binary evidence | Ready for private review from `faber 1a7001fe4bb26b0f20361e12aa4df8f4dcd604d1`, incorporated into this site at `faberlang.dev 08390f9a9234629fbaaabff38488f196da74d10e`. | Public artifact build, signing/checksum publication, and install route approval. |
| Autograd-first evidence boundary | `faber-runtime 4f8d452` and `examples 310cef1` exact rung3 oracle fixtures may be used as private-preview proximity/strategy evidence only. Output-checked device/autograd floor remains 0. | Faber-generated autograd output must be emitted and output-checked through the approved release path before any generated-autograd, PyTorch-equivalence, rendering, device, source-export, install, or registry claim. |
| Language contracts | Draft contract routes are cataloged in `/contracts/1.0.0-rc.1/documents.json`. | Approved public export, real document digests, and checksum replacement. |
| Discovery/catalog coverage | `documents.json`, `sitemap.xml`, and embedded route validation cover the same local preview route set. | Replace placeholder digests and approve public export before publication. |
| Broken/internal link scrub | Validator checks internal route-like links and discovery JSON URLs against served local assets. | Public link scrub and approved external-link policy before publication. |
| Evaluate/learn copy | Ready as local private-preview copy. | Public source/example authority and launch approval. |
| Quickstart | Workflow preview only. | Released artifact or operator-approved install route. |
| Examples | Indexed as gated/tracked/blocked. | Public source plus run evidence for anything marked runnable. |
| Packages/registry | Local package-store direction only. | Public Cista/package evidence and explicit live registry gate. |
| Launch/growth preparation | Local editorial checklist and reviewer notes may be prepared without external actions. | Operator approval for deployment, public posts, analytics, email capture, roadmap, support/community commitments, and channel changes. |
| Announcement surface | Not enabled. | Operator approval for public posting, DNS, deployment, analytics, and channels. |

## Required Before Public Use

- Approve public/private export boundary.
- Replace placeholder document digests and public artifact checksums.
- Produce a clean public artifact release process and approved install route.
- Select public examples and attach run evidence.
- Approve licensing and repository publication order.
- Approve deployment, DNS, analytics policy, announcements, and community
  channels.

## Validation Commands

```sh
cargo run --bin validate_public_packet
cargo fmt --check
cargo test
git diff --check
PORT=18084 cargo run --bin faber-web
```

For private review, route smoke should return `200` for the homepage,
evaluate page, checklist, leakage report, and agent primer, and `404` for the
removed internal route.
