# Faber Stage 0 — Positioning, Audience, and Narrative Brief

Date: 2026-07-11
Owner: head-cmo (with head-cpo input)
Status: discovery deliverable — pending Mind accept
Source campaigns: `docs/CAMPAIGN.md` (Stage 0), `docs/LAUNCH-AND-GROWTH-CAMPAIGN.md` (Stage 0)
Evidence rule: every public claim below maps to a shipped or public-eligible artifact. Radix internals are private and are never cited as proof.

## 0. Evidence baseline (what is actually true today)

This section is the honesty floor. No claim in this brief may exceed it.

Publicly visible right now:
- `faberlang/faberlang.dev` on GitHub — README-only, not deployed.
- `faberlang/tree-sitter-faber` on GitHub — Zed syntax highlighting via a **dev extension**; **not** in the extension registry; **highlighting only**, no LSP, no diagnostics, no structural parsing.

Public-eligible but **not yet published** (no git remote, no release):
- `faber` CLI — command surface `check / build / run / test / script / format / explain / targets`. `faber script` interprets (MIR) without Cargo. **No released binary.** Building from source requires a private Radix checkout.
- `faber-runtime` — public Rust runtime types (`use faber::…`): Valor, tensors, frames.
- `norma` — default standard library (`norma:json`, `norma:solum`, `norma:chorda`, …).
- `triga` — graphics/geometry library. Vector3/Matrix4 transform family typechecks and emits Rust. **GPU/provider execution and render pipeline are tracked blockers, not shipped.**
- `cista` — package manager. Local loop works (install/inspect/remove/exec/meta/filesystem dev registry). Remote `cista.dev` login/logout/fetch/publish contract exists but is **environment-gated, not live**.
- `examples` — corpus (keyword reference, source of `faber explain`), plus application packages: `coreutils` (GNU coreutils reimplementation), `vivilite` (Faber-native mailspace CLI), `gpu-workload` (matmul/softmax/MLP), `ai-workbench` (AI CLI), `air`, `script-kernel`.

Language identity facts (safe to claim):
- Latin-derived keyword vocabulary: `incipit`, `itera`, `ab/per/de/ex`, `fixum`, `functio`, `nota`, `valor`, `solum`, `mori`. Distinctive and memorable; a learnability variable to manage.
- `faber explain <keyword>` returns an in-toolchain language reference sourced from the corpus — a genuine, evidenced product hook.
- The public grammar (`EBNF.md`) currently lives inside private Radix and is **not yet exported** as public language truth (depends on CAMPAIGN.md Stage 1).

## 1. Positioning statement

**For** developers who write application logic that has to survive more than one execution surface **(native applications, systems, and accelerated workloads)**, **Faber is** the intent-first application language whose readable source is the same source that carries across those execution lanes **—** unlike rewriting intent per target (the status quo) or learning each target's compiler internals (the systems-language cost), Faber lets the readable version and the deployed version stay the same program.

Category framing (category-of-one, not "another programming language"):
- Not competing with Rust/Go (systems languages) or Python (dynamic scripting).
- Competing with the **rewrite tax**: the cost of re-expressing the same intent every time it crosses a runtime boundary.
- One-line category: *"the application language whose intent is portable across execution lanes."*

## 2. Primary audience recommendation

**Recommended primary (pending message-test validation):** Audience Hypothesis 1 — *builders who want application code to remain readable while targeting more than one runtime or deployment environment.*

Why this audience, on today's evidence:
- It has the most shipped proof: `coreutils` (native app), `vivilite` (CLI app), `gpu-workload` (accelerated), `ai-workbench` (AI) are all Faber packages. The multi-lane claim is demonstrable, not aspirational.
- It is the most differentiated framing — "write intent once, carry it across lanes" is unusual and maps directly to the runtime/lane architecture without exposing compiler internals.
- It tolerates pre-launch state best: the *idea* and the *examples* can be shown before the binary install path is live.

**Secondary (Stage 2+):** Hypothesis 2 (Rust-adjacent developers wanting explicit contracts at a higher level). Strong narrative fit, but over-indexing here risks implying an interop/FFI maturity that is not yet evidenced. Pursue after the native-application story is proven.

**Tertiary / deferred:** Hypothesis 3 (tool/library authors wanting inspectable packages). Real, but `cista.dev` is not live, so the package-ecosystem pitch cannot be proven today. Becomes a content pillar once the registry ships.

Caveat: Stage 0 is discovery. This recommendation is the **default to act on**, not a closed decision. It should be validated by 2–3 lightweight message tests before the homepage locks (CAMPAIGN.md Stage 3).

## 3. Problem / Promise / Proof hierarchy

**Problem.** Application intent dies at execution boundaries. Every time logic crosses from a reviewable native app into a system, a data pipeline, or an accelerated workload, it gets rewritten in the target's terms. The readable version stops matching the deployed version, and the original intent is buried under target-specific machinery.

**Promise.** Write Faber once; carry that same readable intent across execution lanes — reviewable native applications, systems, and accelerated workloads — without learning each target's compiler internals.

**Proof hierarchy (each item must map to released public evidence; if the evidence is not yet public, the claim waits).**

| Tier | Claim | Required evidence | Status |
| --- | --- | --- | --- |
| 1 | Readable, intentional source | Real `.fab` snippets from `corpus`, `coreutils`, `vivilite` | Ready when repos are public |
| 2 | Toolable today | `faber check/build/run/test/script/format/explain/targets` + tree-sitter highlighting | CLI claim waits on binary; highlighting claim ready |
| 3 | One intent, many lanes | `coreutils` + `vivilite` + `gpu-workload` + `ai-workbench` as Faber packages | Ready when `examples` is public |
| 4 | Portable artifacts | Generated code against `faber-runtime`; `cista` packaged interfaces + compiled artifacts | Ready when `faber-runtime`/`cista` public |
| 5 | Library ecosystem in progress | Norma stdlib tours; Triga geometry mirroring three.js | Partial (Triga CPU-only today) |

## 4. Prohibited claims

These cannot appear in any public surface until the cited evidence ships.

- "Open source" / "public repo" for `faber`, `norma`, `cista`, `triga`, `examples`, `faber-runtime` (no remotes yet).
- "Install with one command" / Homebrew / curl / binary download (no released binary).
- "Build from source" as a *public* path (currently requires private Radix).
- GPU rendering / render pipeline / WebGPU execution for Triga (tracked blocker; CPU typecheck/emit only).
- LSP, diagnostics, or IDE integration beyond syntax highlighting.
- "Package registry live at cista.dev" / "publish your package" (environment-gated).
- Performance or benchmark claims vs Rust/C/Python (none published).
- Adoption, star, or traction numbers (none exist).
- Compiler internals as proof: MIR, lowering, codegen, hygiene, arena. The only user-visible internal vocabulary is `faber script "interprets"` — nothing deeper.
- Roadmap dates or shipping commitments.
- "Production ready" / "stable" / version stability claims (pre-launch).

## 5. Content pillars

Each pillar is evidence-grounded and has at least one owner artifact.

1. **Language design in public** — keyword vocabulary, explicit contracts, readability. Artifacts: `corpus`, `faber explain`, real `.fab` snippets.
2. **What you can build today** — deep dives on `coreutils`, `vivilite`, `gpu-workload`, `ai-workbench`.
3. **The execution-lane idea** — how one intent targets native / systems / accelerated surfaces. User-visible only; no compiler internals.
4. **Library ecosystem in progress** — Norma stdlib tours; Triga geometry and the three.js mirror rationale.
5. **Release and capability updates** — honest capability matrix (what works today vs tracked), release notes.
6. **Engineering lessons, sanitized** — design rationale and trade-offs without private implementation detail.

## 6. Channel and cadence

- **X** is the timely distribution channel; **`faberlang.dev/updates`** is the durable canonical archive. Every X post has a durable long-form home.
- **Weekly short update** — only when there is real progress. **Monthly** deeper technical or product story. **Release-triggered** notes. **Occasional** ecosystem spotlight.
- **Hard rule: no invented cadence filler.** Posting to maintain a schedule is prohibited; a quiet week ships nothing.
- **One** developer community channel is evaluated *after* the first content cycle, not sprayed across every network.
- **Pre-launch:** the secured X account posts nothing until the launch gate (site + install + flagship example live and honest) clears (LAUNCH-AND-GROWTH Stage 2 gate).

## 7. First eight post concepts

Ordered for the launch sequence; each assumes the relevant evidence is public. Every concept names its required evidence.

1. **Why Faber exists** — application intent shouldn't die when it crosses an execution lane. (Founder narrative + positioning. Evidence: the problem/promise hierarchy.)
2. **Read Faber out loud** — tour the Latin keyword vocabulary with a real `.fab` snippet. (Evidence: `corpus`, `vivilite` or `coreutils` source.)
3. **`faber explain`** — a language reference that lives inside your toolchain. (Evidence: corpus as `faber explain` source; CLI command surface.)
4. **One intent, many lanes** — coreutils, a mailspace CLI, and a GPU workload, all Faber. (Evidence: `coreutils`, `vivilite`, `gpu-workload`.)
5. **Rebuilding a coreutils tool in Faber** — runnable deep dive. (Evidence: `coreutils`; requires public repo.)
6. **Triga** — Faber's geometry types and why they mirror three.js. (Evidence: `triga` types; honest about CPU-only status.)
7. **Norma in practice** — JSON, async, iteration. (Evidence: `norma:json`, async exempla.)
8. **How we talk about capability honestly** — the capability matrix as a trust artifact. (Evidence: Triga-style capability report pattern.)

## 8. Launch sequence

Evidence-ordered; each step gates the next.

1. Pre-launch explainer (this positioning) as a durable site page.
2. Homepage live with real `.fab` examples.
3. **Installation path live** — hard gate; requires binary-first release or another operator-approved install.
4. **Flagship example runnable** (`coreutils` or `vivilite`) — requires public repo.
5. **Initial package story** (Norma) — requires public repo + working local `cista` loop.
6. Release notes / honest capability matrix.
7. Founder narrative post (durable).
8. **First promotional X post** — only after site + install + example are live and honest.

## 9. Metrics that reward useful adoption (not vanity)

Measured signals:
- **Install success rate**, not download count.
- **Example completion** — did a visitor run a flagship example end-to-end?
- **Docs/construct lookup success** — `faber explain` usage proxies and on-site search success.
- **Package discovery and install success** (`cista install`).
- **Returning readers** to `faberlang.dev/updates`.
- **Issue quality** (reproducible, on-contract) over raw issue count.

Explicitly **not** primary signals: follower count, star count, raw impressions. These are visible but never the goal.

Note: external analytics or a mailing list requires operator approval (stop condition). Default is no external analytics until Stage 4, then revisit with a privacy-preserving option.

## 10. Critical blocker (cross-campaign dependency)

The narrative can be authored now, but **no claim of installability or public repos can be made** until CAMPAIGN.md Stage 1 (public truth and leakage boundary) ships and a binary-first release path exists. Today, of seven public-eligible repos, only two are public, and there is no released binary. The CMO brief is ready; its external activation is gated on:

- Public/private boundary export and leakage gate (CAMPAIGN.md Stage 1).
- Licensing decision (operator stop condition).
- Binary-first release pipeline (cli-release).
- Order of repo publication.

## 11. Open operator questions (decisions, with defaults)

1. **Licensing** (stop condition before public repos). Default if no answer: prepare the language surface repos as MIT/Apache-2.0; keep the Radix compiler private.
2. **Repo publication order.** Default: `tree-sitter-faber` (done) → `faberlang.dev` (done) → `norma` + `examples` + `triga` (read-only value, low leakage) → `faber` + `cista` + `faber-runtime` once binary-first install exists.
3. **Install path.** Default: Homebrew tap + static binary as the first public install, built from a private-Radix org build.
4. **Analytics.** Default: none initially; revisit at Stage 4.
5. **X handle confirmation.** Default: hold all posting until the launch gate clears; operator confirms the secured handle.
6. **Latin vocabulary as brand element.** Default: lean in (strong differentiator) and ship a keyword cheatsheet; flag learnability for a head-cpo read.
