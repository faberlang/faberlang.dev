+++
title = "Faber 1.15.1"
description = "Release notes and install details for Faber 1.15.1."
section = "releases"
order = 12
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.15.1 |
| **Tag** | `faber-v1.15.1` |
| **GitHub** | [faber-v1.15.1](https://github.com/faberlang/releases/releases/tag/faber-v1.15.1) |
| **Published** | 2026-10-21 |
| **License** | MIT OR Apache-2.0 |

## Install this version {#install}

Pinned download for **Faber 1.15.1**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.15.1-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.15.1/faber-v1.15.1-aarch64-apple-darwin.tar.gz) | 20.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.15.1/faber-v1.15.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.15.1-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.15.1/faber-v1.15.1-x86_64-unknown-linux-gnu.tar.gz) | 22.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.15.1/faber-v1.15.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
# The installer verifies the checksum and installs a versioned
# binary that `faber update` and `faber versions` manage.
curl -fsSL https://raw.githubusercontent.com/faberlang/faber/main/install.sh \
  | sh -s -- --version 1.15.1
export PATH="$HOME/.faber/bin:$PATH"
faber --version
```

## Release notes {#notes}

> **Status**: final — tagged `faber/v1.15.1` on 2026-10-21

1.15.1 is the first published 1.15 release. The `faber/v1.15.0` source tag exists, but its release run stopped before publishing anything (the installer still defaulted to 1.14.0), and release tags are never moved, so 1.15.0 has no artifacts.

Faber 1.15 follows 1.14 with a smaller language surface and a large correctness sweep. The language gains radical glyphs, range slices on tensors, checked list windows and target-bound imports, and the English spellings of two type words change. Kernels now refuse 64-bit integers by name. The `faber` command can update itself. A big part of the release is not a feature: every target was re-run over the whole corpus and a long list of code-generation defects was fixed. Several changes are breaking; read that section before you upgrade.

> **Experimental through version 1.** The language changes constantly, and breaking changes ship in minor releases. Faber 1.15 carries no stability promise, and neither does any other 1.x release. A 2.0 release is planned for when the language is largely stable.

### Language

**Radical glyphs.** `√`, `∛` and `∜` are prefix operators for the square root, the real cube root and the fourth root. They bind like unary minus, so `√ x + 1` is `(√ x) + 1`, and they work where the matching method works (floats and float tensors).

**Ranges as values.** A range stored in a cell can be walked and printed: `for range r let i` walks it, and `print r` shows the construction, `2‥5`.

**Range slices on tensors.** A rank-1 tensor takes a range in brackets, `v[1‥4]`, and gives the strided window as a tensor. A literal range that falls outside a literal shape is `SEM011 index_provably_out_of_bounds`.

```fab
main {
    let f64 x ← 16.0
    print √ x, ∛ -8.0, ∜ x

    let range<int> r ← 2‥5
    print r
    for range r let i {
        print i
    }

    let tf32[6] v ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0] ↦ tf32[6]
    let tf32[3] mid ← v[1‥4]
    print mid
}
```

```text
4.0 -2.0 2.0
2‥5
2
3
4
[2.0, 3.0, 4.0]
```

**Checked list windows.** `xs.take(n)` and `xs.slice(a, b)` now report when the window runs past the end, instead of clamping. Like any failable call they need a handler outside `main`: a `⊥` recovery value, a `do { } catch`, or a failable enclosing function (`SEM011 failable_call_requires_handler`). Inside `main` an unhandled failure ends the program with `take_out_of_range` or `slice_out_of_range`. Generated Rust emits the same checked form.

```fab
fn head(list<int> xs, int n) → list<int> {
    return xs.take(n) ⊥ xs
}

main {
    let list<int> xs ← [1, 2, 3, 4, 5]
    print head(xs, 2)
    print head(xs, 9)
    print xs.slice(1, 3) ⊥ []
}
```

```text
[1, 2]
[1, 2, 3, 4, 5]
[2, 3]
```

**Bits and floats.** A same-width integer converts to raw bits and back with `↦`, as in `n ↦ b32` for a `u32` or `i32`. A width that does not match is `SEM016 bits_conversion_width_mismatch`, and a literal negative shift count is `SEM010 shift_count_negative`. Converting into `f16` or `bf16` rounds to that format at the store.

```fab
main {
    let u32 n ← 7
    let b32 bits ← n ↦ b32
    let u32 back ← bits ↦ u32
    print bits, back

    let f16 h ← 0.1 ↦ f16
    print h ↦ f64

    let b8 flags ← 0xf0
    print flags ⇒ 4
}
```

```text
0x00000007 7
0.0999755859375
0x0f
```

**Target-bound imports.** `import python "math" m` binds a module of the target language, by its own name and verbatim. A program that does this belongs to that target: `faber build -t python` emits `import math as m`, and every other target, `faber run` and a plain `faber check` refuse it with `SEM017 import_target_bound`.

```fab
import python "math" m

main {
    print m.pi
}
```

**Contracts are checked.** A class that says `implements` and leaves a method out is `SEM010 implet_missing_method`; a method whose signature differs from the contract's is `SEM010 implet_method_signature_mismatch`. Indexing a tensor with one scalar where the rank needs more is `SEM011 tensor_scalar_index_rank`. Converting text to a list of characters with `↦` is refused by name (`SEM016 textus_to_lista_unsupported`).

**Exit codes.** `main exit N` makes `faber run` end with exit code N, as the generated programs do.

### Tooling

**`faber update`.** `faber update --check` reports whether a newer release exists, and `faber update` installs it under a versioned name and moves the `faber` link; `--version` switches to an exact version, rolling back included. `faber versions` lists what is installed.

**Durable writes.** `norma:fs` gains `write_file_durably` and `write_bytes_durably`: the file is replaced atomically, so a failure or interruption leaves the previous complete file and never a partial one.

**Code generation.** This release re-runs the whole corpus on every target, and fixes the defects that turned up in the Rust, Go, TypeScript, Swift, Python, LLVM, Racket and Cranelift outputs. Generated Rust now iterates an enum's members in declaration order with `for from Color let c`.

### GPU

**Kernels use 32-bit integers.** Inside a `@ kernel` function a 64-bit `int` is refused: `SEM008 nucleum_wide_integer` for the declaration and `nucleum_wide_intermediate` for a wide intermediate. Write `i32`. No GPU throughput claim is made here.

### Breaking changes

1. **English type words.** The English spellings `intervallum` and `sparsa` are now `range` and `sparse`. The Latin words in an English file are `PARSE040 wrong_locale_type`; Latin files keep the Latin words. Rewrite `intervallum<int>` as `range<int>`.
2. **List windows report.** `take` and `slice` past the end of a list used to clamp. They are now failable, so a call outside `main` needs a handler, as in `xs.take(n) ⊥ xs`.
3. **Kernel integers.** `int` in a kernel is an error; use `i32` (see GPU).
4. **Contract conformance.** A class that claims `implements` without the methods or signatures now fails to check.

### Known issues

- **Libraries cannot be installed.** The graphics, autograd and UI libraries still have no install command, and `faber doctor` reports them not found.
- **Records without a declared type do not run.** A bare `{ field = value }` literal checks, but the runner stops with `missing type information for MIR lowering`. Declare the record type to run it.
- **Stepped ranges cannot be stored yet.** A cell of type `range<int, 2>` is accepted in a signature, but storing a stepped range literal into one is `SEM010 intervallum_value_step_unsupported`. A step in a `for range` loop works.
- **Checked list windows by target.** Generated Python still clamps a window that runs past the end, and the TypeScript target refuses the `⊥` form (`CODEGEN001 ts_trap_expression_unsupported`). The runner and Rust report as described above.
- **Enum iteration in Go.** `for from Color let c` over an enum does not compile in generated Go.

### Not in this release

- A package manager and library install command.
- Stored stepped ranges (see Known issues).
- CUDA lane-form kernels; `faber run --device cuda` runs whole-tensor kernels only.
- The C and Cranelift targets remain previews that cover a subset of the language and refuse the rest by name.

---

[All releases](/releases/) · [Start](/start/)
