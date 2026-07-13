# Campaign: Faber Public Surface

Date: 2026-07-11
Status: draft — ready for discovery delivery

## Summary

Build `faberlang.dev` as Faber's public product, language, documentation, and
community surface while the Radix compiler, lowering architecture, private
tests, and internal factory plans remain private. The site should feel like a
credible developer-product launch, not an implementation wiki.

The dedicated agent-first documentation intake is
[`AGENT-FIRST-DOCUMENTATION-WEBSITE-PLAN.md`](AGENT-FIRST-DOCUMENTATION-WEBSITE-PLAN.md).
It is queued after the Faber 1.0 RC process and must pass Goal Forge and Goal
Check before lowering into implementation.

## Desired End State

- A visitor understands in one minute what Faber is, who it is for, and why it
  matters.
- The public language contract includes tutorials, reference material, Norma
  APIs, runnable `.fab` examples, release notes, and honest target capability.
- Installation is binary-first; public pages never require compiler source.
- No public build can traverse or expose private Radix implementation paths.
- Product storytelling, documentation, releases, and `cista.dev` form one
  coherent ecosystem.

## Public / Private Invariant

Faber-authored language material is public by default. Rust compiler/runtime
implementation, lowering and code generation, private regression fixtures,
factory ledgers, and unreleased implementation strategy are private by default.
The detailed authority is Radix's private
`docs/plans/private-compiler-public-language.md`.

## Product Story Hypothesis

Faber is a language for writing clear application intent once and carrying it
across multiple execution lanes—from reviewable native applications to
systems, data, and accelerated workloads—without making users learn the
compiler's internal machinery. The public story must lead with user outcomes:
readability, trustworthy tooling, deployable artifacts, and a growing package
ecosystem. Lane internals are evidence, not the homepage pitch.

*Vision framing. The evidenced V1 lanes are narrower: native applications,
self-contained package binaries, and a narrow Go CLI. See the Stage 0
positioning brief and the V1 release contract.*

## Current State

| Track | State | Next action |
| --- | --- | --- |
| Site repo | Clean, README-only dedicated repo exists. | Discovery-first design/content delivery spec. |
| Public language truth | Boundary plan exists; public repo/export flow not yet established. | Freeze source authority and leakage gate. |
| Positioning | No accepted audience/problem narrative. | CPO positioning brief and message tests. |
| Information architecture | Not selected. | Map startup narrative + docs/reference journeys. |
| Visual system | Not selected. | Produce design directions after positioning. |
| Publishing | No selected stack or deployment flow. | Select only after content/build constraints are known. |
| Community | No public update/support cadence. | Route to launch-and-growth campaign. |

## Campaign Path

### Stage 0 — Positioning And Audience Discovery

- Status: active discovery
- Owner: head-cpo advisory; Mind selects the result
- Gate: one primary audience, one problem statement, one differentiated promise,
  proof points that can be shown without revealing private internals
- Batching: discovery-first
- Lowers to: delivery

### Stage 1 — Public Truth And Leakage Boundary

- Source: private/public boundary plan in Radix
- Gate: explicit allowlist, forbidden paths, link scrub, dry-run export manifest,
  and fail-closed public build
- Batching: split-on-boundary (language contract vs release artifacts)
- Lowers to: delivery, then factory

### Stage 2 — Information Architecture And Content Model

- Status: queued after Faber 1.0 RC closeout
- Intake: [`AGENT-FIRST-DOCUMENTATION-WEBSITE-PLAN.md`](AGENT-FIRST-DOCUMENTATION-WEBSITE-PLAN.md)
- Required process: Goal Forge → Goal Check → delivery/factory implementation
- Required journeys: agent cold start, evaluate Faber, install it, learn it,
  look up a construct, build/test a package, diagnose errors, browse examples,
  understand targets, find external packages, follow releases
- Gate: page map, agent-discovery contract, content ownership, freshness rules,
  public/private source for every page family, and passing Goal Check
- Batching: batch-by-default after one generated content family proves the model
- Lowers to: Goal Forge first; implementation only after Goal Check

### Stage 3 — Visual Direction And Interactive Prototype

- Produce two or three distinct startup-quality directions, then select one.
- Gate: responsive homepage plus representative guide, reference, release, and
  package-integration pages; accessibility and performance budgets
- Batching: discovery-first, then one selected system
- Lowers to: delivery, then factory

### Stage 4 — Documentation And Example Pipeline

- Export or curate public grammar, guides, Norma source/API, examples, CLI
  reference, and released capability matrix.
- Gate: forbidden-path scan, example runnability, stale-claim scan, idempotent
  export, public-source manifest
- Batching: batch-by-default after one proven content family
- Lowers to: delivery, then factory

### Stage 5 — Launch-Ready Site

- Build, test, deploy-preview, analytics/privacy choice, SEO/social cards,
  support/security routes, and release/update feed.
- Gate: browser/device/accessibility checks and explicit operator approval for
  DNS, production deployment, analytics, or public announcement
- Batching: split-on-boundary (local build vs external effects)
- Lowers to: factory

## Routing Rules

- Website content must consume a public language source or sanitized export,
  never private Radix source directly.
- Do not explain lowering/codegen mechanics beyond released user-visible
  behavior and capability claims.
- `cista.dev` protocol, registry backend, identity, moderation, and package
  pages route through the registry campaign; the Faber site links into them.
- Public posting, account changes, DNS, deployment, analytics, and outbound
  messages require operator authorization at action time.

## First Useful Milestones

1. Accepted positioning brief and public/private content matrix.
2. Clickable homepage/docs prototype with real Faber examples.
3. Public-language export/check pipeline.
4. Preview deployment suitable for private review.

## Validation

- No public output contains `docs/factory`, private repo links, `.rs` compiler
  paths, internal deferred IDs, or generated regression expectations.
- Every runnable example is checked against a released compiler.
- Homepage promise is supported by an installable artifact and demonstrable
  public example.
- Responsive, keyboard, contrast, reduced-motion, and performance checks pass.

## Stop Conditions

Pause for the operator before choosing licensing, creating public repositories,
changing DNS, enabling analytics, publishing a roadmap, deploying production,
or announcing externally.
