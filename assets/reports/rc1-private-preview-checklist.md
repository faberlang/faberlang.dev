# RC1 Private Preview Readiness Checklist

Date: 2026-07-14
Scope: `faberlang.dev` local RC1 private-preview packet
Status: private-preview checklist; not public launch approval

## Evidence Boundary

Current local evidence:

- Website packet version: `1.0.0-rc.1`.
- Evidence commit: `1a7001f`.
- Compiler provenance: `82d6230ec`.
- Faber provenance: `edbb54f496e5`.
- Local release-profile build command: `cargo build --release --bin faber`.
- Local CLI version result: `faber 1.0.0-rc.1`.
- Local SHA-256: `77203c7302eb025bbf3ddd01aae798a96f0ca97cc0219066a6a64a991405700b`.

This evidence supports private review of the current local tree only. It does
not create a public artifact, install route, pushed tag, deployment, analytics
setup, announcement, public source export, or live registry proof.

## Private Preview Checklist

| Gate | Private-preview status | Public-release blocker |
| --- | --- | --- |
| Local website packet | Ready for private review after validator and route smoke pass. | Public/private export approval and deployment approval. |
| Local CLI binary evidence | Ready for private review from evidence commit `1a7001f`. | Public artifact build, signing/checksum publication, and install route approval. |
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
