+++
title = "Radix 1.0.0-rc.1"
section = "releases"
order = 18
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 1.0.0-rc.1 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

**Status:** source-tag candidate only in Faber's first odd-major development
line. This note does not authorize a GitHub release, binary publication,
Homebrew update, package publication, or final `v1.0.0` release. It is not a
language-lock or LTS record; the product policy is
[`faber/docs/release/policy.md`](../../../faber/docs/release/policy.md).

### Candidate scope

This release-candidate preparation lands the self-contained core-support lane:

- Faber embeds deterministic source-only support for `faber-runtime`,
  `host-kernel-rs`, `host-native-rs`, and the explicit `aleator`, `consolum`,
  `processus`, `solum`, and `tempus` providers.
- Installed Faber materializes and verifies that payload in a content-addressed
  local cache before generated Cargo uses it.
- Generated Cargo routes core dependencies only through that verified cache,
  selecting providers only when analysis requires them.
- Clean-install proofs cover a minimal package and a native `solum` provider
  package.
- Release preparation is split into non-publishing `prepare`, `validate`, and
  `build-local` phases; Linux recipe inputs are explicit post-split contexts.

### Evidence commits

| Surface | Commit | Evidence |
| --- | --- | --- |
| Faber payload assembly | `2eba7cd` | Deterministic embedded core-support archive. |
| Faber materialization | `18a24f1` | Verified content-addressed extraction. |
| Faber dependency routing | `aa8eb94` | Generated Cargo uses materialized core paths. |
| Faber clean-install proofs | `82105bf` | Minimal and native-provider isolated executable tests. |
| Radix RC-safe phases | `c83d5fb43` | Local-only prepare, validate, and build-local commands. |
| Radix Linux contexts | `e1471f24a` | Explicit named Radix/Faber/runtime/host/provider contexts. |

### Limitations and gates

- The Linux Docker artifact extraction proof remains pending a Docker-enabled
  runner; the recipe and dry-run context contract are committed.
- Existing external native-library packaging can carry its own runtime path
  dependency and requires separate packaging work; no checkout fallback was
  added to Faber's core route.
- `examples/corpus/index.toml` is release-validation input only. It is not
  regenerated, staged, or modified by release tooling.
- The candidate source tag requires explicit Mind/operator approval after clean
  candidate validation. Creating or pushing the tag is intentionally outside
  this preparation commit.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
