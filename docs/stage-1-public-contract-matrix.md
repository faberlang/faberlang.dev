# Faber Stage 1 Public Contract Matrix

Date: 2026-07-13
Owner: Mind selection packet
Status: local-only readiness packet; not public copy
Scope: `faberlang.dev` public contract, content gates, and leakage checks

This packet converts the Stage 0 positioning work into Mind-selectable Stage 1
contract buckets. It is discovery/docs only: it does not authorize deployment,
publication, DNS, analytics, public repository changes, or install claims.

## Source Inputs

| Input | Current evidence | Contract use |
| --- | --- | --- |
| `docs/CAMPAIGN.md` | Stage 1 requires an explicit allowlist, forbidden paths, link scrub, dry-run export manifest, and fail-closed public build. It also states that installation/public posting/DNS/deployment are operator-gated. | Stage 1 gate authority and stop conditions. |
| `docs/stage-0-positioning-brief.md` | Recommends the primary audience, problem/promise/proof hierarchy, prohibited claims, launch sequence, and the hard blocker on installability/public repos. | Claim buckets and proof requirements. |
| `docs/head-cpo-product-story.md` | Selects J1 evaluate and J3 learn/reference as authorable now, while J2 install/run and J4 packages are hard-gated. It defines the "left-column-only" public-explainable rule. | Page-family readiness and leakage rule. |
| `docs/AGENT-FIRST-DOCUMENTATION-WEBSITE-PLAN.md` | Requires one authoritative corpus, released truth only, private Radix isolation, plain text first-class docs, versioned URLs, machine contracts, and contract tests. | First local-only website/doc producer packet. |
| `assets/llms.txt`, `assets/index.html`, `assets/docs/1.0.0-rc.1/*`, `assets/contracts/1.0.0-rc.1/*` | Local draft public assets already exist, with version placeholders and build-time digest placeholders. `targets.json` marks Rust native binary as product lane and Go/TypeScript/S-expression as emit-only. | Evidence of desired asset shape; not publication evidence. |

## Mind-Selectable Claim Buckets

| Bucket | Allowed claim | Public prerequisites | Prohibited until gate clears | Gate type |
| --- | --- | --- | --- | --- |
| Identity | Faber is an intent-first application language for readable source that carries across execution lanes. | Mind accepts Stage 0 positioning; public examples/snippets are selected from public-eligible sources. | Category claims that imply production maturity, ecosystem adoption, or open source availability. | Soft gate: message acceptance. |
| Audience/problem | Primary audience is builders who want readable application code across more than one runtime/deployment surface. | 2-3 lightweight message tests or Mind accepts the Stage 0 default. | Targeting all audience hypotheses equally in homepage copy. | Soft gate: Mind selection. |
| Readability/language | Faber source is readable and has a distinctive keyword vocabulary; the public language contract includes grammar, keywords, operators, types, diagnostics, and docs. | Public contract export is generated from approved language truth and link-scrubbed. | Claims based on private Radix docs, unreleased grammar files, or private regression fixtures. | Hard gate: Stage 1 export. |
| `faber explain` / reference | The toolchain can provide in-place language reference for documented keywords or constructs. | Released CLI evidence and shared corpus between `/reference` and `faber explain`. | Any CLI command claim before a released binary or operator-approved install path exists. | Hard gate for public CLI claim; soft gate for local content design. |
| Execution lanes | Public wording may distinguish supported product lane, emit-only targets, host-backend lanes, and tracked limitations. | Capability matrix generated from released contracts; examples checked against released compiler. | "Write once, run on GPU/browser", "Go is supported", or backend counts as runnable lanes. | Hard gate: capability evidence. |
| Examples | Real `.fab` snippets, `coreutils`, `vivilite`, and `automation` can support evaluate/learn content once public-eligible and checked. | Public example source selected, runnable status recorded, and no private path leaks. | "Full coreutils", "multi-backend coreutils", or examples requiring private checkout. | Hard gate for runnable public examples; soft gate for local authoring plan. |
| Install | Installation is binary-first as a planned path. | Released binary or operator-approved install route; quickstart verified against that artifact. | "Install with one command", Homebrew/curl/download claims, or public source-build path. | Hard gate. |
| Packages/Cista | Faber packages can be described locally as a future/public-contract journey. | Working public package docs, public package manager release, and live or explicitly staged registry path. | "cista.dev is live", "publish your package", registry login/fetch/publish, or ecosystem availability. | Hard gate. |
| Norma/Triga/external projects | Norma, Triga, and Cista may be named as external projects with their own docs/release cycles. | Public repos/docs or sanitized package docs are available. | Absorbing full external references into Faber docs; GPU/render pipeline claims for Triga. | Hard gate for feature claims; soft gate for cross-link plan. |
| Updates/growth | `faberlang.dev/updates` can be the durable archive concept; X can mirror later. | Launch gate clears and operator approves public posting/channel use. | Posting cadence, public roadmap promises, analytics, email collection, or outbound announcements. | Hard operator gate. |

## Leakage Checks

Stage 1 should fail closed if any local or exported public asset contains:

- private Radix implementation paths or repo links;
- `docs/factory`, factory ledgers, deferred IDs, private plans, or regression
  expectation artifacts;
- compiler-internal proof vocabulary such as HIR, MIR, FMIR, lowering, codegen,
  hygiene, arenas, LLVM/WGSL/Metal internals, except for an explicitly approved
  user-facing `faber script` wording;
- install, source-build, public-repo, registry-live, analytics, roadmap, or
  adoption claims that lack their hard-gate evidence;
- links to missing documents, undeployed routes, inaccessible repositories, or
  private boundary docs.

Recommended local checks before any Stage 1 acceptance:

1. Export manifest lists every public file and source authority.
2. Link scrub verifies all in-repo links and all external links are approved.
3. Forbidden-token scan covers Markdown, HTML, JSON, text, sitemap, robots, and
   contract archive inputs.
4. Contract checksum and document digest placeholders are replaced in the build
   artifact before preview or publication.
5. Example runnability status is recorded per example against a released
   compiler, or the example is labeled non-runnable/tracked.

## Example And Content Prerequisites

The first content packet should use only authorable-now material and keep
install/package claims closed:

| Page family | Allowed first packet | Required evidence before public use |
| --- | --- | --- |
| Homepage evaluate section | One-line promise, primary audience, one public-safe `.fab` snippet, and an honest capability teaser. | Mind accepts identity/audience bucket; snippet source is public-eligible and scrubbed. |
| `/learn` | Language design narrative, keyword vocabulary, and read-it-out-loud examples. | Public language export and selected snippets. |
| `/reference` | Construct pages sourced from the same corpus intended for `faber explain`. | Shared corpus exists; drift check between site and tool reference. |
| `/targets` or capability matrix | Works/tracked/emit-only table with product-lane dimensions. | Released contract equivalent to `assets/contracts/1.0.0-rc.1/targets.json`, checked against actual release. |
| `/examples` | Curated examples with status labels: runnable, read-only, tracked, or blocked. | Public example sources and run evidence for anything marked runnable. |
| `/install` | Placeholder or omitted route only. | Binary-first release or operator-approved install route. |
| `/packages` | Placeholder or cross-campaign note only. | Public Cista/package evidence and registry gate clearance. |

## Hard Vs Soft Gates

Hard gates block public claims and public routes:

- public/private boundary export and fail-closed leakage gate;
- released binary or operator-approved install path;
- public example source plus run evidence for runnable examples;
- live or explicitly staged registry evidence before package publishing claims;
- operator approval for licensing, public repositories, production deployment,
  DNS, analytics, email collection, public posts, public roadmap, and community
  commitments.

Soft gates can be resolved by Mind selection before local authoring continues:

- accept or revise primary audience;
- accept the "intent-first / execution lanes" phrasing;
- choose "execution lanes" vs another user-facing lane term;
- decide whether the first local packet is read-only value before install;
- select the first flagship snippet/example family for local copy.

## First Local-Only Website/Doc Producer Packet

Recommended packet: **P0 evaluate/learn contract producer**.

Goal: produce a local, non-deployed content family for evaluation and learning
that proves the public contract shape without claiming installation, packages,
publication, or source availability.

Inputs:

- accepted buckets from this matrix;
- Stage 0 positioning brief;
- approved public language export or a clearly labeled local mock export;
- selected public-eligible `.fab` snippets;
- current local asset contract under `assets/`, treated as draft evidence only.

Outputs:

- homepage copy with install/package CTAs omitted or disabled;
- `/learn`, `/reference`, `/targets`, and `/examples` drafts;
- local `llms.txt` update that routes agents to current, versioned docs and
  names hard limitations;
- export manifest and leakage-check report.

Done-when:

- every claim maps to an allowed bucket and cited source input;
- every prohibited bucket is absent or explicitly labeled blocked/tracked;
- no route promises install, public source, live registry, deployment, analytics,
  or publication;
- the leakage checks pass locally;
- Mind can choose whether to advance to implementation after Stage 1 boundary
  evidence exists.

## Stop Conditions

Stop and return to Mind/operator if the work requires any of the following:

- choosing or applying a license;
- creating, publishing, or modifying public repositories;
- deploying, previewing publicly, changing DNS, or enabling analytics;
- posting externally, collecting email, or opening community channels;
- claiming installability, source-build support, package publication, public
  registry availability, production readiness, stability, or roadmap dates;
- using private Radix internals as public proof;
- making local docs depend on unreleased facts without a tracked/blocked label.
