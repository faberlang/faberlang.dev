# Goal: Site navigation and the cheat sheet — first-click IA rework

## Status

**Implemented — awaiting review.** Captured during a site walkthrough on
2026-08-07, starting from the public homepage and moving inward, then built the
same day. All eight threads have landed on `main`; nothing is pushed.

Build is green: 3407 pages, 0 broken links, leakage gate passing, and all 184
Faber fences in `src/en-US` compiling against radix 0.79.0.

### Scope discipline

The walkthrough deliberately stopped at the **top-left column**. That column is
the most important user experience for someone landing on the site: it is the
one surface that has to be right. Everything below and beyond it is permitted to
stay somewhat disjointed for now.

Consequently, this goal is **not** a site-wide IA rewrite. Work that does not
serve the sidebar's first-contact experience is out of scope, including the
duplicate IA generations and other adjacent defects recorded at the end of this
document — those are logged so they are not lost, not queued for this pass.

### The target column

```
Home
Install
Cheat sheet
Releases
Open source
Examples
Target lanes
```

Seven entries, in that order, mirrored by the homepage buttons for the first
three. Of these: **Home** needs adding, **Cheat sheet** and **Target lanes** do
not exist, **Open source** replaces Repositories, **Install** and **Releases**
need splitting apart, and **Examples** needs rebuilding. Only the labels are
cheap; every entry has real work behind it.

### Thread index

| Thread | Subject | Nature | State |
|---|---|---|---|
| 1 | Homepage call-to-action order | `generate-landing.py` | done |
| 2 | Cheat sheet section | 13 pages, 66 verified fences | done |
| 3 | Install / Releases split | `generate-releases.py`, 88 versions | done |
| 4 | Sidebar order | `html.fab`, `link_prefix.fab` | done |
| 5 | Open source page (replaces Repositories) | migration + redirects | done |
| 6 | Examples rebuild + syntax highlighting | `generate-examples.py` | done |
| 7 | Target lanes section | `capture-lane-panels.sh` + generator | done |
| 8 | GPU support must not read as unsupported | matrix + agent surfaces | done |

Order was forced: destinations before navigation. A sidebar entry or button
pointing at a page that does not exist fails the build's internal-link gate, so
threads 1 and 4 — the cheapest — had to land last.

## Left undone, deliberately

- **`vivilite/src/main.fab` does not compile** with radix 0.79.0: comments sit
  between a closing brace and a following `sin`, which PARSE060 rejects. It was
  the obvious "large real application" example and is omitted rather than
  showcased broken. Fix belongs in the examples repo.
- **Faber release notes are sparse** — 8 versions against more tags. The
  Releases generator lists the union of tags and notes and marks the gaps, so
  backfilled notes appear automatically once written.
- **Site is pinned at 1.4.0.** `faber 1.5.0` notes are already listed, with no
  downloads; it picks those up when the release publishes.
- **The duplicate IA generations in `dist/`** are untouched, per the scope
  discipline above.
- **Locale trees lag.** New English pages are English-only; translated pages
  that moved kept their translations. The leakage gate passes.

Threads 1 and 4 are the cheapest and change the first-contact experience most
directly. Thread 6's two highlighting defects are near-free and independently
worthwhile. Threads 2 and 7 are the substantial builds.

## Summary

The site presents a large amount of correct information with no clear route
through it. This goal reworks the **first click** — what the homepage asks a
visitor to do, and what the left column offers once they are inside — and adds
the one section that is missing entirely: a **cheat sheet** of short, practical
examples, distinct from the exhaustive corpus.

Three threads:

1. **Homepage call-to-action order** — explore before install.
2. **A new Cheat sheet section** — multi-page, example-first, keyword-indexed.
3. **Install / Releases split** — install shows one binary; releases carries
   full version history for both Faber and Radix with per-version notes.

The sidebar and the homepage buttons must teach the same order, so the
navigation shape is learned once.

## Problem

- The homepage's first and most prominent action is **Install Faber**. That
  asks for commitment before comprehension. A visitor who does not yet know
  what Faber is has no low-cost path deeper into the site except the small
  `Docs` header link or six cards at the very bottom of a long page.
- The second button, **Run the GPU proof**, is far too specific for a
  first-contact surface. It is a deep link into one example anchor.
- There is **no cheat sheet**. Confirmed: zero hits for "cheat" across `src/`,
  `generator/`, and `static/`. The corpus is comprehensive but is reference,
  not orientation — it answers "what does this keyword mean," never "show me
  the three ways people actually write this."
- **Install and Releases are entangled.** `src/en-US/start/install.md` carries
  `Build from source`, `Homebrew status`, and `Agent path` sections beyond the
  simple install path. `src/en-US/reference/releases.md` opens with a
  "Getting started" table linking Install / Quick tour / Hello / Commands /
  Projects / Examples — duplicating the install page it should be separate from.
- **Release notes exist but are invisible on the site.** They live in sibling
  repositories and are not exposed at all.
- The left column does not start with **Home**. Returning to the landing page
  requires knowing the logo is clickable.

## Thread 1 — Homepage call-to-action order

Single site of change: `generator/scripts/generate-landing.py`, the `.fl-cta`
block (currently two anchors).

Current:

```
[Install Faber] (fl-btn-primary)   [Run the GPU proof] (fl-btn)
```

Target:

```
[Explore Faber] (fl-btn-primary → /en-US/)   [Install] (fl-btn)   [Cheat sheet] (fl-btn)
```

- **Explore** is the primary blue button and the expected first click.
- **Install** stays, demoted to secondary. It is important, just not first.
- **Cheat sheet** replaces the GPU-proof deep link. Both remaining buttons are
  general-purpose destinations, not anchors into one example.

No CSS work is required: `.fl-cta` is a wrapping flex row and `.fl-btn-primary`
is a class swap. Optionally the tertiary button could read lighter than the
secondary; not required.

### Known follow-on

`Explore` lands on `/en-US/`, which today is a **docs index** — sidebar chrome,
an `AGENT-READY` callout at the top, and a download table. The button will be
honest about its destination, but that destination may not deliver what
"Explore" promises. Landing-page content is a separate open question, to be
covered later in this walkthrough.

## Thread 2 — The Cheat sheet section

### What it is

A multi-page section of **short examples showing how to use the language**.

It is deliberately *not* the corpus. The corpus is a comprehensive,
keyword-by-keyword list of everything that exists. The cheat sheet is a curated
set of succinct examples that show those keywords in use. Overlap in subject
matter, opposite in purpose.

### Shape

- **Top-level page** leads with the core feel of the language: a couple of
  representative programs using the core keywords, followed by the **top ~20
  keywords** a reader will actually encounter.
- **Each keyword links through** to its own cheat-sheet page showing several
  ways to use it. Still inside the cheat sheet section — this is a section,
  not a page.
- Examples stay short. No complex programs. The unit of value is a small,
  correct, copyable snippet.

### Two drill-downs from the cheat sheet index

Drilling into Cheat sheet offers **two** things, not one:

1. **Language overview** — the core feel of the language and the keyword
   examples described below.
2. **Commands** — a dedicated area showing how to run the basic Faber
   commands.

### Commands folds in from Everyday commands

`src/en-US/start/commands.md` ("Commands you will use") is useful content in
the wrong place. It becomes the **Commands** area of the cheat sheet rather
than a step in the Start track.

It already has the right shape for a cheat sheet: a daily-loop command table
followed by short sections for `check`, `build`, `run`, `explain`, and
reader-locale commands.

Migration requirements:

- **40 files** across the repo link to `start/commands.html`, including every
  locale tree (`zh-Hans`, `zh-Hant`, `vi`, `ar`, `hi`, `th-TH`), the docs
  landing `src/en-US/index.md`, the Start track pages (`index`, `hello`,
  `projects`), `src/en-US/reference/releases.md`, and `static/llms.txt`.
- `generator/scripts/generate-releases-page.py:142` emits a hard-coded link to
  `/start/commands.html`. Generated, so it must be fixed in the script.
- The Start track is a sequenced path (`Install → Hello → Commands →
  Projects`). Removing Commands from the middle breaks the sequence — decide
  whether Start links across into the cheat sheet at that step or the track
  is re-sequenced around it.
- Redirect the old URL.

### Sections to cover

| Topic | What it must show |
|---|---|
| **Entry points** | `main`; async vs non-async entry; annotation arguments on the entry point |
| **Bindings** | Constant vs modifiable variable |
| **Type holes** | Type hole; union type hole; worked example of each |
| **Generics** | Generic list creation; generic tensor creation |
| **Loops** | The different loop forms; looping over keys; over an object; over a range |
| **Control flow** | `if`/`else`; cases; discriminated unions |
| **Catching** | Its own section — see below |
| **Alternate return channel** | The dedicated error channel, its glyph syntax, and what is actually happening |
| **Conversions** | The conversion glyph; conversion vs casting |
| **Types and widths** | Signed / unsigned / float widths as fundamentally numbers, plus sugar forms; lists and their generics; tensors, vectors, matrices and their sugar forms |
| **Imports** | Shortest sugar form; declared module names; aliasing; importing a specific item from a module; local file vs standard library |
| **Locales** | Side-by-side comparison, English against pre-generated other locales, showing same meaning under different rendering |
| **Testing** | Test syntax; grouping syntax; assertions; test files; how to run tests |

### Catching deserves its own section

A `catch` block can attach to many different control and function block forms,
not only a `try`. This is a genuinely unusual language feature and gets lost if
folded into general control flow.

It pairs with the **alternate return channel**: Faber does not throw errors the
way most languages do. A thrown value returns through a dedicated error channel
that must be handled somewhere up the pipeline, and there is a distinct glyph
syntax for it. This needs a worked example plus a short explanation of the
mechanism, not just syntax.

### To verify before writing

- **Item-level imports** — whether importing a specific item from within a
  module is implemented today or is still an open factory goal. Check against
  the grammar (`EBNF.md`) and live compiler behaviour before documenting.

## Thread 3 — Install / Releases split

### Install page

Narrows to the simple path only:

- The most recent binary
- How to install it
- How to run it at a basic level

Nothing else. No prior-version list, no build-from-source, no ancillary tracks.
Anything about other versions belongs on Releases.

### Releases page

A long list of **every versioned release for both Faber and Radix**. Not a
dense table — a browsable index. Clicking a version gives:

1. How to install that specific pinned version
2. The full release notes for that version

### Source material (verified 2026-08-07)

Release notes already exist in the sibling repositories and are simply not
exposed on the website:

| Source | Files | Range |
|---|---|---|
| `radix/docs/release/v*.md` | 79 | `v0.3.0` … `v0.79.0` |
| `faber/docs/release/v*.md` | 7 | `v1.0.0`, `v1.0.0-rc.2`, `v1.1.1`, `v1.3.0`, `v1.4.0`, `v1.5.0-dev-notes`, `v1.5.0` |

Faber's history is sparse relative to its tag list. **Historical Faber release
notes will be generated** so that every actual tag has notes, rather than the
current handful. Plan for a complete set on both sides.

### Version currency

`faber/docs/release/v1.5.0.md` exists (238 commits past v1.4.0; headline is the
Metal/CUDA device execution the site already markets). The v1.5.0 release is
**in progress** — binaries expected shortly. The site stays pinned at **1.4.0**
until v1.5.0 is officially published, then download tables and version claims
move together.

## Thread 5 — Open source page

A new page in the left column, positioned **after Releases**.

### Overview paragraph (top of page)

States the licensing position plainly: the language as a whole is fully open
source **except the Radix compiler**, which is closed for now until market
demand is established, at which point it will be opened. This is the same
position already stated in the landing page's `.fl-open-source` note and the
docs landing prose — this page is where it lives in full rather than as an
aside.

Named as open and public:

- The Faber build tool
- The package manager (Cista)
- Triga (graphics / geometry)
- Norma (standard library)
- All other libraries, code examples, and documents

Followed by the full list of public repositories with links, so a reader can go
look for themselves.

### Maintainer contact (bottom of page)

- **Ian Zepp** — `ian.zepp@protonmail.com`
- Faber's X / Twitter profile: **`@faberlang`**

Nothing on the site references a social account today — this is net-new. The
only contact surface that currently exists is "file a GitHub issue."

Note that `reference/repositories.md` currently states outright: "There is no
mailing list or support email — GitHub Issues is the way to get in touch."
Publishing an address contradicts that line, so it must be rewritten rather
than carried over during the fold-in, or the page will argue with itself.

Publish as a plain `mailto:` — no obfuscation. The address already appears in
public commit metadata across the org, so hiding it on one page protects
nothing, and every JS-assembly trick fails the site's no-JavaScript-for-content
property.

### Replaces the Repositories page

**Decided:** Open source **replaces** `src/en-US/reference/repositories.md`.
Repositories does not survive as a separate page.

That page already carries most of this material — the "everything is public
except the compiler" framing, a public-repository table, a private-repository
entry for `radix`, a host-platform repository table, and a "Reporting issues"
routing table — but it is buried under `reference/`, where nobody looking for
"is this open source?" would find it. All of it folds into the new page.

Migration requirements:

- Fold in the **Reporting issues** routing table; it is the site's only stated
  contact path today and must not be lost.
- Keep the **host-platform repositories** table (`host-kernel-rs`,
  `host-native-rs`, `host-providers-rs`) — it is not in the landing page's repo
  list and exists nowhere else.
- Redirect the old `reference/repositories.html` URL.
- `static/llms.txt` has a `## Contact / provenance` block that deep-links
  `reference/repositories.html#reporting-issues`. Update it to the new anchor.
- Inbound links to `repositories.html` exist across locale trees and in
  `src/en-US/index.md`'s repository table. Sweep them.

## Thread 6 — Examples page rebuild

Last item in the sidebar column, below Open source. The link already exists;
the page is wrong.

### Problem with the page as it stands

`src/en-US/start/examples.md` is 188 lines that mostly do not show examples.

- The **first section is "How to run an example"** — `git clone`, `faber check`,
  `faber build`. That is useless to someone who has installed nothing and is
  just looking at the website. It asks for setup before it delivers value.
- The rest is largely prose descriptions of packages plus links out to
  **GitHub**. Sending a curious visitor to dig through unfamiliar repository
  directories is exactly the experience to avoid. Someone evaluating a language
  wants to click and read code, not navigate a foreign repo tree.
- Of the four code fences on the page, three are `bash` and one is Faber. The
  page nominally about examples contains a single example.

### Target shape

Same pattern as the Releases page in Thread 3 — an index of links into nested
pages that hold the actual content.

- **Examples index** lists each project with its **name** and a **short
  description** — enough to make a reader want to click.
- **Each nested page** holds the real source: complex, production code, read
  directly on the site, syntax highlighted.
- No "here is how to run it" preamble at the top of the index. Setup
  instructions belong after the code has earned interest, or on the Install
  page.
- Do not offload to GitHub. GitHub links are fine as provenance; they are not
  the delivery mechanism.

### Syntax highlighting

The requirement is that code reads like it would in an IDE, not as flat plain
text.

**Partly built already.** `generator/scripts/highlight-code.py` runs in
`build-site.sh` and wraps tokens in `.tok-*` spans coloured by
`speculum.css:810-817` (`tok-kw`, `tok-ty`, `tok-st`, `tok-nu`, `tok-co`,
`tok-an`, `tok-op`, `tok-fn`). Keyword vocabulary is read per-locale from the
generated search index (116 keyword entries in `search-index.en-US.json`), so
it cannot drift from the language. No client-side highlighter ships.

**But it is barely firing.** Two concrete defects, both verified in `dist/`:

1. **Fence attributes break the matcher.** `BLOCK_RE` in `highlight-code.py`
   requires `class="lang-([a-zA-Z0-9_-]+)"` with the quote immediately after
   the language name. A fence written ` ```faber locale=la ` renders as
   `class="lang-faber locale=la"`, which the pattern cannot match. The single
   Faber example on the examples page — the `echo` coreutils source at
   `dist/en-US/start/examples.html` — has **zero token spans** as a result.
   The page's only real code sample is the one thing left unhighlighted.
2. **The homepage is not highlighted at all.** `generate-landing.py` emits
   `<pre class="fl-src">`, `<pre class="fl-run">`, and bare `<pre>`, none of
   which are `pre.faber-code`, so `highlight-code.py` never touches them.
   `dist/index.html` contains **no `.tok-*` spans whatsoever**. Every code
   panel on the site's most-viewed page — the locale tab strip, the target tab
   strip, the GPU kernel strip — is flat monochrome text.

Also note `text` fences are deliberately excluded as program output, but
`src/en-US/` uses ` ```text ` **41 times**. Some of those are almost certainly
Faber source that will never colour. Worth auditing.

### Tree-sitter integration

`faberlang/tree-sitter-faber` exists locally at `~/work/faberlang/tree-sitter-faber`
and already carries highlighting assets:

- `queries/highlights.scm` — 69 lines, generated by
  `scripta/generate_grammar.py`, with full capture coverage (keywords, builtin
  types, strings in all five literal forms, numbers, annotations, operators,
  punctuation, comments).
- `grammars/faber.wasm` — a compiled grammar, i.e. a browser-capable path via
  `web-tree-sitter`.
- `grammars/fab.tmLanguage.json` — a TextMate grammar, i.e. a build-time path
  via any TextMate-compatible highlighter.

Three viable approaches, in increasing cost:

| Approach | Cost | Trade-off |
|---|---|---|
| Fix the two defects in `highlight-code.py` | Lowest | Keeps zero-JS, keeps corpus-derived vocabulary; still regex-based, no structural awareness |
| Build-time TextMate via `fab.tmLanguage.json` | Medium | Real grammar, still zero-JS at read time; new build dependency |
| Runtime `web-tree-sitter` + `faber.wasm` | Highest | True parse-quality highlighting; ships a wasm payload and breaks the zero-JS-for-content property |

Recommendation: fix the two defects first regardless of which path is chosen —
they are cheap, and defect 2 is the difference between the homepage having
highlighting and not. Treat tree-sitter as the quality upgrade after the
plumbing works.

## Thread 7 — Target lanes section

A further sidebar section. Naming is unsettled — candidates: **Targets**,
**Codegen**, **Target lanes**. Pick one before building; the concept is stable
even if the label is not.

### What it is

The landing page's **Compiler lanes** table, expanded from a single flat table
into a browsable section. Structurally parallel to the cheat sheet, but where
the cheat sheet shows *the Faber language*, this shows *what Faber becomes*.

Three levels:

1. **Section index** — the lanes: Locale, HIR, AIR, MIR, GPU, Packaging.
2. **Per-lane page** — a table of the targets within that lane, each with a
   description of what it does and what is supported. HIR gets its section
   (Rust, Faber, TypeScript, Go, Swift); MIR gets its own (LLVM, WASM, WGSL,
   S-expression, FMIR); GPU gets its own (Metal, CUDA).
3. **Per-target page** — **side-by-side**: the Faber source against the
   generated output in that target, across a handful of scenarios.

### Why side-by-side matters

The comparison is the argument. It is interesting on length and complexity
grounds in a way prose cannot be, and it is strongest on the GPU lane: Faber's
kernel intrinsics (`matmul` is the clearest case; there are others) let a
kernel be written very succinctly, and the generated Metal or CUDA is markedly
more verbose. Reading both next to each other is the most direct case for
writing kernels in Faber rather than the native shading language.

Measured from the panels already captured in `generator/landing/targets/`:

| Source | Lines | Target | Lines | Ratio |
|---|---:|---|---:|---:|
| `kernel.fab` | 4 | Metal | 36 | 9× |
| `kernel.fab` | 4 | WGSL | 34 | 8.5× |
| `source.fab` | 10 | LLVM IR | 397 | 40× |
| `source.fab` | 10 | TypeScript | 294 | 29× |
| `source.fab` | 10 | Go | 221 | 22× |
| `source.fab` | 10 | WASM text | 104 | 10× |
| `source.fab` | 10 | Rust | 14 | 1.4× |

Note the honest exception: **Rust is 1.4×**, because the Rust emitter is a
close structural projection. Do not build a page template that assumes the
generated side is always dramatically longer — it would make the Rust page
look like a failure when it is actually the expected result. Let each target
tell its own story.

### Infrastructure that already exists

This is a generalization of working machinery, not new plumbing:

- `generator/scripts/capture-landing-panels.sh` already captures compiler
  output for 7 targets from a shared `source.fab` plus a `kernel.fab`, pins the
  toolchain to the repo build rather than `PATH`, and prints the versions used.
  Its header documents *why*: panels were once captured against a compiler
  three days stale and the page made claims the toolchain could not back.
- `generator/landing/targets/` holds the captured `out.*.txt` artifacts.
- `generator/scripts/generate-target-matrix.py` already generates
  `src/en-US/toolchain/target-matrix.md` from `radix/EBNF_MATRIX.md`, with
  prose held separately in per-locale `targets.toml` so regeneration does not
  wipe translations.

What is needed: extend capture from **one program × N targets** to **several
scenarios × N targets**, and generate per-lane and per-target pages from the
result. The rule from `capture-landing-panels.sh` carries over unchanged — every
panel is literal compiler output, never hand-authored.

### Relationship to the existing target matrix

`src/en-US/toolchain/target-matrix.md` already exists and is the measured
support authority (corpus-wide percentages, per-lane breakdowns, device kernel
support, CUDA hardware verification). It is a **measurement** surface, dense and
statistical.

The new section is a **demonstration** surface. They are complementary, but the
overlap needs an explicit boundary or this repeats the Install/Releases and
Open source/Repositories problem a third time. Suggested split: the matrix
stays the numeric source of truth and the new section links into it for
support claims; the new section owns the worked side-by-side examples.

## Thread 8 — GPU support must not read as unsupported

### The concern

The target matrix scores every target against the **full general-language
corpus** (~280 terms). Metal and WGSL are device-kernel subset emitters — they
are only ever meant to lower `@ nucleum` compute kernels and GPU views, not
packages, async, CLI, host libraries, or general control flow. Scoring them
against all 280 terms therefore produces a tiny percentage **by design**.

The risk is a reader concluding "Metal and CUDA are barely supported" when in
fact GPU kernel support is fully functional, dual-backend training is proven on
real hardware locally and on RunPod, and multi-GPU training and inference are
close.

### Finding: the matrix page already handles this — carefully

This is worth stating plainly before any rewrite, because the temptation is to
"fix" prose that is already correct.
`src/en-US/toolchain/target-matrix.md` already:

- Titles the section "**device kernel text (subset emitters; low % is
  expected)**".
- Annotates the `metal-text` 2% row inline: "**Kernel-subset lowerability over
  the full corpus** — not Metal product health."
- Carries a "How to read these percentages" block stating the matrix "is **not**
  a product completion score for Metal, CUDA, or GPU training," and spelling out
  that 2% "does **not** mean Metal or WGSL 'are 2% done.'"
- Explains that **there is no `cuda` column** because CUDA runs the NVVM → PTX
  path, and that matrix columns track emit surfaces, not host sessions.
- Provides a separate `#device-kernel-support` product view with per-backend
  accepted proofs, a Proven / Emit-staging / Building vocabulary, and a RunPod
  CUDA hardware verification matrix.

`src/en-US/toolchain/compiling.md:87` independently warns: "Do not read
Metal/WGSL '2% capable' rows on the [matrix] …". The prose is consistently
careful across `target-matrix.md`, `compiling.md`, and `radix.md`.

**So the defect is not honesty. It is structure and reach.**

### Residual problems to actually fix

1. **DECIDED: drop the subset-emitter rows from the matrix entirely.** Not a
   softened percentage, not an *n/a* label — remove them. The question the
   matrix asks does not apply to a device-kernel subset emitter. As the owner
   put it: it is like asking a submarine how fast it swims. A wrong answer to a
   category-error question is worse than no answer, because the number travels
   without its caveat — skimmers read tables and models extract tables, while
   the qualifier sits in an adjacent cell that does not survive quoting,
   screenshotting, or scraping.

   CUDA already has no row and stays that way, for the same reason.

   **Scope — this is bigger than the two summary rows.** `metal-text` and
   `wgsl-text` also appear as **columns** in the per-term tables at
   `target-matrix.md:377` (Keywords — systems lane) and `:509` (Operators —
   systems lane), where they render ✕ against nearly every one of ~280 terms.
   That is the same category-error question asked hundreds of times. Removing
   the summary rows while leaving those columns would be inconsistent and would
   leave the misleading signal in place at greater volume. Remove both.

   **Where the removal must happen.** The page is generated:
   `generate-target-matrix.py` reads `radix/EBNF_MATRIX.md` and rewrites its
   tables. Hand-editing `src/en-US/toolchain/target-matrix.md` would be undone
   by the next regeneration. The exclusion belongs in the generator — a target
   exclusion list applied in `build_summary()` and `section_table()`, which
   both pass tables through `extract_table_blocks()` — or upstream in the radix
   matrix itself. Prefer the generator so the raw radix measurement stays intact
   for internal use.

   **Keep the explanation, lose the number.** The "How to read these
   percentages" block should still state why device emitters are not scored
   here, and point to `#device-kernel-support` and
   `faber run --backend metal|cuda`. The reader learns the distinction without
   being handed a 2% to misread. The `Product GPU backend` mapping table at
   `:108-112` stays — it explains the emit surfaces without scoring them.
2. **Ordering buries the good news.** The low-percentage subset table appears at
   roughly line 101; the product view `#device-kernel-support` starts at line
   114. A reader hits "2%" before reaching "dual-backend MLP training, Proven on
   both backends." The product view should come first, or the subset table
   should be reachable only from it.
3. **`compiling.md:45` shows `metal-text … **Limited**`** in a support column,
   without the adjacent caveat that carries elsewhere on that page.
4. **The agent surfaces omit GPU entirely.** This is the largest gap found.
   - `dist/llms.txt` — 174 lines — mentions GPU **once**, as the directory name
     `gpu-workload/`. No Metal, no CUDA, no device execution, no `--backend`.
   - `dist/llms-full.txt` — 2378 lines — contains **zero** occurrences of
     "metal" or "cuda", case-insensitive.

   So the most-defended claim on the human site is invisible on the machine
   surface. A model reading `llms.txt` to learn what Faber does would not
   discover that it runs on GPUs at all. Given how much of the site's
   positioning is GPU-first, this is a straightforward miss and probably the
   highest-value fix in this thread.

### Boundary to hold

Whatever is rewritten must not overclaim in the other direction. The current
accepted position stays: bounded dual-backend training is **proven**;
end-to-end device inference is **not shipped**; multi-device execution is
**frontier**. RunPod lanes are verification infrastructure, not a product
backend. The goal is to stop *understating* kernel and training support, not to
start overstating inference or multi-GPU.

## Thread 4 — Sidebar order

The left column opens with the same shape as the homepage buttons, so the
navigation order is taught once and reinforced:

```
Home          → back to the landing page (explicit link, not the logo)
Install
Cheat sheet
Releases
Open source
Examples
Target lanes   (name unsettled: Targets / Codegen / Target lanes)
… existing sections follow
```

`Home` must be a real link. Requiring a visitor to discover that the brand mark
is clickable is a needless puzzle.

## Trap discovered during implementation

`build-site.sh:199` runs `generate-target-matrix.py --all-locales` on **every
build**. `src/en-US/toolchain/target-matrix.md` is therefore a generated file.

The zombie-docs pass (`7ce82b7b`) hand-edited 153 lines of GPU honesty prose
into it — the percentage framing and the entire device-kernel product summary.
The next build silently deleted all of it and reverted the page's cross-links to
the retired `/tooling/…` IA. This was latent from the moment it was written; the
first rebuild merely triggered it.

Fixed in `ef260571` by moving that prose into
`generator/locales/en-US/targets.toml`, which is where the generator's own
design puts it ("Prose/chrome lives in generator/locales/<locale>/targets.toml
so matrix regeneration does not wipe translations").

**Rule for anyone working here:** before editing a page under `src/`, check
whether a script writes it. Currently generated: `toolchain/target-matrix.md`,
`reference/releases.md` (`generate-releases-page.py`), the whole `corpus/` tree,
`dist/index.html`, and `dist/porta/index.html`.

## Adjacent defects found while walking

Not part of this goal's scope, but discovered during the walkthrough and worth
tracking so they are not lost:

1. **`dist/` is stale relative to `src/`.** `src/en-US/index.md` was rewritten
   in `7ce82b7b` (zombie-docs pass — "no privileged executable path", capability
   ladder), but `dist/en-US/index.html` was last rendered one commit earlier and
   still says "Rust is the primary executable path." `build-site.sh` has not run
   since that content change.
2. **The deploy is stalled.** Per `todo.md`, GitHub Pages deploys have been
   timing out at `deployment_queued` since 2026-08-06, so the public site is
   behind the repository as well. Two independent layers of staleness.
3. **Two IA generations coexist in `dist/`.** Both the current
   `en-US/{start,language,toolchain,libraries,reference}/` and the retired
   `en-US/{features,syntax,tooling,references,history,ecosystem}/` render real
   pages — e.g. `dist/en-US/syntax/functions.html` and
   `dist/en-US/language/functions.html` both exist. Root-level `/start/`,
   `/language/`, `/syntax/` form a third set. This is a strong candidate cause
   for the site feeling unnavigable.
4. **`AGENTS.md` misdescribes the entry point.** It states that `/` is the
   locale-less language portal with a chooser ring, generated by
   `generate-portal.py`. In fact `/` is the marketing landing page from
   `generate-landing.py`; the portal now lives at `/porta/`.

## Files in play

| File | Role |
|---|---|
| `generator/scripts/generate-landing.py` | Homepage; the `.fl-cta` button block |
| `generator/scripts/inject-chrome.py` | Sidebar injection |
| `generator/locales/en-US/chrome.toml` | Sidebar group and item labels |
| `generator/www/speculum.css` | `.fl-cta`, `.fl-btn`, `.fl-btn-primary` |
| `src/en-US/start/install.md` | To be narrowed |
| `src/en-US/reference/releases.md` | To be rebuilt as a version index |
| `src/en-US/reference/repositories.md` | Overlaps the new Open source page — fold in or keep as exhaustive list |
| `static/llms.txt` | `## Contact / provenance` block links the repositories anchor |
| `src/en-US/cheatsheet/` | New — does not exist yet |
| `src/en-US/open-source.md` | New — does not exist yet |
