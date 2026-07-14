# RC1 Private Preview Readiness Checklist

Date: 2026-07-14
Scope: `faberlang.dev` local RC1 private-preview packet
Status: private-preview checklist; not public launch approval

## Evidence Boundary

Current local evidence:

- Website packet version: `1.0.0-rc.1`.
- Faber checkout: clean HEAD `5d508d7`.
- Local release-profile build command: `cargo build --release --bin faber`.
- Local CLI version result: `faber 1.0.0-rc.1`.
- Local SHA-256: `d0b23f8b9e03422a467d5ab2ccf7c4e78e0e3f497662ab29b4826af6953ab92e`.

This evidence supports private review of the current local tree only. It does
not create a public artifact, install route, pushed tag, deployment, analytics
setup, announcement, public source export, or live registry proof.

## Private Preview Checklist

| Gate | Private-preview status | Public-release blocker |
| --- | --- | --- |
| Local website packet | Ready for private review after validator and route smoke pass. | Public/private export approval and deployment approval. |
| Local CLI binary evidence | Ready for private review from clean HEAD `5d508d7`. | Public artifact build, signing/checksum publication, and install route approval. |
| Language contracts | Draft routes exist under `/contracts/1.0.0-rc.1/`. | Approved public export, real document digests, and checksum replacement. |
| Discovery/catalog coverage | `documents.json`, `sitemap.xml`, and embedded route validation cover the same local preview route set. | Replace placeholder digests and approve public export before publication. |
| Evaluate/learn copy | Ready as local private-preview copy. | Public source/example authority and launch approval. |
| Quickstart | Workflow preview only. | Released artifact or operator-approved install route. |
| Examples | Indexed as gated/tracked/blocked. | Public source plus run evidence for anything marked runnable. |
| Packages/registry | Local package-store direction only. | Public Cista/package evidence and explicit live registry gate. |
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
