+++
title = "Faber 1.10.0"
section = "releases"
order = 11
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.10.0 |
| **License** | MIT |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

> **Status**: draft

Faber 1.10 continues the 1.x development line. Since 1.9.0, the language
adds type algebra and heritage, Cartesian range products, lockstep collection
walks, decimal widths, conversion enrollment, kernel closures, and per-file
reader locales. Tooling adds execution statistics, stronger generated-Rust
validation, and more honest target checks. This draft covers the 26 August
through 2 September 2026 candidate window; version files remain labeled 1.9.0
until the release commit.

### Language

**Type algebra and heritage.** `∩` and `∪` are checked type operators. In the
English reader, `abstract`, `extends`, and `implements` are checked language
forms; the Latin spellings are `abstractus`, `sub`, and `implet`. They are
semantic relations, not comments. The English `trap` capture boundary
(`capta` in Latin) reifies a failable result alongside declared `⇥` channels
and local handlers. `expect_failure` (`erratur` in Latin) now has strict
behavior: a case that unexpectedly succeeds is rejected.

**N-ary iteration.** `for range a‥b, c‥d` (`itera ab` in Latin) walks the
Cartesian product of its ranges. `for from xs, ys` (`itera ex` in Latin)
walks several collections in lockstep, with one binder per source.

**Decimals.** `d32` and `d64` are scaled-decimal width markers. Arithmetic uses
scaled integer carriers with round-half-even arithmetic. `d32` widens to
`d64`; the reverse narrowing is rejected. Integer literals are rejected in a
decimal context; write a decimal literal or use an explicit conversion.

**Conversions (breaking).** In-union `@ conversion` (`@ conversio` in Latin)
arms are gone. Conversions are standalone annotated functions enrolled in one
table: at most one conversion is allowed per ordered type pair per scope,
builtins cannot be shadowed, and failure channels compose.

**Guards.** `reject` (`reice` in Latin) is the boolean opposite of `require`
(`requirit`).

**Match and narrowing.** `match` (`discerne` in Latin) cases use type patterns
with `case` (`casu` in Latin) and bind narrowed values. Narrowing persists
across control flow instead of ending at the `if` arm.

**Annotations.** Bare declaration annotations must end their line before the
declaration they annotate. Braced annotations remain available for same-line
use.

**Lista.** `all` / `any` (`omnia` / `quilibet` in Latin) are predicate twins
on `lista`.

**Kernel closures.** `kernel` (`nucleum` in Latin) marks a capture-free,
device-safe closure inside a host function. It is not a first-class host value
or a public launch entry. Declaration annotations `@ kernel` / `@ nucleum` keep
their existing role; only public annotated functions are launchable device
entries.

**Locale.** Each source file selects its own reader locale. `faber format`
fails closed when the required reader pack is unavailable. Packs for `ar`,
`en`, `hi`, `la`, `th-TH`, `vi`, `zh-Hans`, and `zh-Hant` ship embedded in the
binary.

**Complexity.** `faber check` warns when a function exceeds the default
cyclomatic budget of 12. Override it with `--complexity-budget` or the
`[check] complexity-budget` manifest key; the CLI value wins over the manifest
value, which wins over the default.

### Tooling

- `faber run --stats` and `--stats-file` write execution-statistics JSON for
  package runs. Device routes refuse statistics requests rather than emitting
  a partial artifact.
- Generated Rust is held to compile-clean output for supported members, while
  broader emitter-shape cleanup continues. The Rust e2e harness now places its
  host module after crate attributes, so real lint and build stages run. The
  Swift e2e lint path invokes `swiftc -typecheck` with the accepted flag.
- Target e2e lanes now register expected failures by family instead of hiding
  them behind an early harness failure.
- Generic size parameters (`magnitudo`) forward caller witnesses to callees,
  allowing declared `[T, D]` shapes to materialize through specialization.
- The compiler workspace is now Rust edition 2024.
- Locked release builds remap private workspace and Cargo-registry paths, and
  the release gate scans the binary for leakage before continuing.
- The release manifest's hosts input and lockfile are refreshed together.
- Canonical Rust validation keeps its hard floor while recording only the
  intentional generated-artifact lint families `never_loop`, `eq_op`, and
  `approx_constant` as receipted debt. Other clippy failures remain errors.

### GPU

Staged composed matmuls, destination provenance, and plan-admission validation
landed on the Metal inference path. Reverse-mode VJPs for RMSNorm and RoPE are
available. Gather reverse-mode remains a known-red path (see Known issues).
Metal-versus-llama.cpp parity measurement provides a baseline; closing the
remaining speed gap is outside this release.

### Breaking changes

1. In-union `@ conversion` (`@ conversio` in Latin) arms are rejected. Rewrite
   them as standalone annotated conversion functions.
2. Same-line bare declaration annotations are rejected. Put the declaration on
   the following line, or use a braced annotation.
3. Integer literals in decimal contexts are rejected.
4. `d64` to `d32` decimal narrowing is rejected.
5. Only public `@ kernel` / `@ nucleum` functions are launchable device
   entries. A private declaration annotation is not a public entry.

### Known issues

- The browser-product build check remains red because generated TypeScript
  still misses `__faberValorTag` on `Identity`.
- The Gather reverse-mode VJP check remains red on the repeated-index path; a
  required indexed scatter-add AIR primitive is still reported there.
- The Gradus cache package check reports a live `LOCALE002` near-keyword
  warning where its expectation records `SEM002`. This is diagnostic-code
  drift, not a cache failure.
- Thirteen environment-gated checks remain skipped: nine device-artifact/export
  gates and four prefill-oracle gates requiring `GEA_SOURCE` or
  `GEA2_F32_GGUF`.
- Two package checks remain unavailable when the optional Triga provider is
  absent; they report `PKG001` for the missing `triga:math` provider.

### Not in this release

- The larger collection-ergonomics rewrite remains outside this release and
  is still in design and admission.
- Type-algebra corpus conversion, remaining generated-Rust shape cleanup, and
  later kernel-closure units continue after 1.10.
- Tensor-glyph law text, set-algebra glyphs, and container-bounds folding
  remain open or deferred.
- Cista remains on the 0.1.0 line.
- Haskell and Python remain source-emit surfaces. Cross-module `textus`
  handles and numeric-inference accuracy are unchanged claims.
- The AMDGPU lane remains a limited discovery-first surface and requires ROCm
  clang for compilation.
- Decimal widening from non-Rust call sources remains fail-closed.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
