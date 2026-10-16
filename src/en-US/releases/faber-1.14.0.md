+++
title = "Faber 1.14.0"
section = "releases"
order = 10
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.14.0 |
| **Tag** | `faber-v1.14.0` |
| **GitHub** | [faber-v1.14.0](https://github.com/faberlang/releases/releases/tag/faber-v1.14.0) |
| **Published** | 2026-10-16 |
| **License** | MIT OR Apache-2.0 |

## Install this version {#install}

Pinned download for **Faber 1.14.0**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.14.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-aarch64-apple-darwin.tar.gz) | 19.5 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.14.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-x86_64-unknown-linux-gnu.tar.gz) | 22.2 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.14.0/faber-v1.14.0-aarch64-apple-darwin.tar.gz
tar -xzf faber.tgz
# The archive ships bin/ and share/; keep them together so the
# reader packs resolve beside the binary.
sudo mv bin/faber /usr/local/bin/faber
sudo mv share/faber /usr/local/share/faber
faber --version
```

## Release notes {#notes}

> **Status**: final — tagged `faber/v1.14.0` on 2026-10-16

Faber 1.14 is the first release after the source went public. Programs can now touch the outside world: the file system, console, process, clock and entropy modules run under `faber run` and in generated Rust, and their failures are values with a kind and a path. The language gets typed holes and open records, an insertion-ordered `ledger` map, tighter escapes and templates, bytes as `list<b8>`, and checked axis markers on tensor row operations. Several of these are breaking changes; read that section before you upgrade.

> **Experimental through version 1.** The language changes constantly, and breaking changes ship in minor releases. Faber 1.14 carries no stability promise, and neither does any other 1.x release. A 2.0 release is planned for when the language is largely stable.

### Language

**Failures are values.** The standard library reports failure as `⇥ IoFault`, a union with one variant per kind of failure (`NotFound`, `Permission`, `ConnectionRefused`, `TimedOut`, and so on). A variant carries the path or address the program passed and no message text; platform text appears only in debug output. A caught fault prints as `IoFault.NotFound { path = "/nonexistent/x" }` on the runner and in generated Rust alike. Absence is not a failure: the end of input and an unset variable are `∪ none`.

**Holes and open records.** A typed cell can solve its own holes: `list<_>[1, 2]` solves the element type, `tuple<_, string>[1, "x"]` solves one slot, and a bare `[..]` or `_ [..]` into a set cell builds the set. `record<*>` declares a record whose whole field list is left to inference, and a bare `{ field = value }` literal with no cell to name it is such a record. (`record<g: f32, *>`, a partial list with a hole, is `PARSE001 ratio_field_list_hole_not_sole`.) An untyped empty literal, `{}` or `[]` with nothing to name its type, is a named error. The stated keyed constructor `Type { "k": v }` builds JSON and `map<K, V>` values.

```fab
main {
    let list<int> xs ← list<_>[1, 2]
    let tuple<int, string> pair ← tuple<_, string>[1, "x"]
    let set<int> seen ← [1, 2, 2]
    print xs.length(), seen.length()
    print "§0 and §0 and §1"("a", "b")
    print «say "hi"»
    print pair
}
```

```text
2 2
a and a and b
say "hi"
tuple [1, "x"]
```

**Ledger.** `ledger<K, V>` is an insertion-ordered map. The runner constructs it from a keyed literal, indexes, stores, deletes, counts, tests membership, loops in insertion order, compares (order matters for `≡`), and prints it. Conversions, sort and the other wrapper operations are refused by name (`SEM010 ledger_operation_not_implemented`). Every other target refuses the type (`CODEGEN001 ledger_type_unsupported_on_target`).

```fab
main {
    mut ledger<string, int> tally ← { "b": 2, "a": 1 }
    tally["c"] ← 3
    tally["a"] ← 10
    for from tally at [name] let count {
        print name, count
    }
    print tally.length()
}
```

```text
b 2
a 10
c 3
3
```

**Bytes are `list<b8>`.** `list<b8>` and the bounded `list<b8, N>` are the byte types in the standard library, the corpus, the re-emitter and the grammar; `faber format` rewrites the older byte-string spellings to them. The scalar words `byte` and `octetus` are retired (`SEM008 retired_byte_word`): write `b8` for raw bits or `u8` for a number. Converting a list to a bounded list checks the length and reports a recoverable failure. Converting a sized number to a bounded byte list is `n ↦ list<b8, 4> via Le` (or `via Be`), bit-exact on the runner and in generated Rust; the other targets refuse the row by name. `x ↦ f32` rounds to binary32, and so does storing a float into a bare `f32` local on the runner.

**Text and escapes.** A string literal may escape only its own delimiter, the backslash, `n`, `t`, `r` and `u{…}`; any other escape is `LEX003 unknown_escape`. A string that contains quotes can use guillemets, `«say "hi"»`, with no escapes, and the lint `WARN034` suggests that rewrite. Regex literals (`regex /pattern/`, or `_ /pattern/` where the type is known) keep their body raw and round-trip through `faber format`. The pattern is not checked by `faber check`: an invalid one fails when the program runs.

**Templates.** A numbered hole `§N` selects argument N, counting from 0, and may repeat; a repeated hole evaluates its argument once on every target that supports templates. Every position from `§0` up to the highest hole must be read: a gap in the numbering is `SEM008 template_hole_index_gap`, and an argument that no hole reads is `SEM008 template_application_arity_mismatch`.

**Enums.** `≺ ≻ ≤ ≥` order enum values by declaration order, and `for from Color let c` walks the members of an enum in that order.

```fab
enum Color { Red, Green, Blue }

main {
    let Color a ← Color.Red
    let Color b ← Color.Blue
    print a ≺ b, a ≻ b, b ≥ a
    for from Color let c {
        print c
    }
}
```

```text
true false true
Color.Red
Color.Green
Color.Blue
```

**Instants.** `≅` and `≇` compare instants of different precisions.

**Range containment.** `x ∈ 1‥5` and `x ∉ 1‥5` now run on the runner and emit on every target except Haskell, which still refuses ranges.

**Tensor row operations.** `sum`, `mean` and `softmax` take the axis marker at the call: `t.sum(axis 1)`, `t.sum(axis 1, axis 2)`, or a named constant, `t.sum(axis K)`. `softmax` takes an optional axis and only the last axis is legal (`SEM010 softmax_axis_not_last`). `norm_rms` and `norm_layer` require the marker too, as in `input.norm_rms(axis 1, 1e-5, weight)`. `rope_half` and `softmax_causal` are source methods.

**Diagnostics.** The six translated reader packs (ar, hi, th-TH, vi, zh-Hans, zh-Hant) now translate the rows that used to repeat the English text, and the parser's "expected X" errors carry named issues instead of prose. New codes include `LEX003 unknown_escape`, `WARN034`, `SEM008 template_hole_index_gap` and `PKG001 target_not_in_this_build`.

### Tooling

**Compiled programs can do I/O.** The standard library's file-system, console, process, clock and entropy modules run through native leaves, both under `faber run` and in a Rust package built with `faber build --target rust`; TCP, an HTTP client and a WebSocket client run under `faber run`. The 1.13 gate that stopped such builds (`PKG001 package_host_selection_required`) no longer fires for these modules. `time.now()` works under `faber run`. Text, encoding, TOML, digests and HMAC are ordinary Faber. No standard-library function is marked deferred any more, and the stub modules `cache`, `compression`, `database`, `model`, `optimizer` and `yaml` are deleted. The limits of this route are under Known issues.

**`faber check --lower`.** Checking a program normally stops at semantic analysis. With `--lower` the program is also compiled to Faber's reference form without being run, which reports the errors semantic analysis cannot see: a program that checks but cannot run. It needs a file or package path, not standard input.

**Library location.** `--library-home <dir>` on the command line and `[paths] library_home` in `faber.toml` select where optional libraries are found; the standard library is embedded and needs neither. The `FABER_LIBRARY_HOME` environment variable is ignored, and so are the other `FABER_*` and `RADIX_*` variables that used to change behaviour (cache home, support-path override, shuffle seed, Metal and device debug switches); each has a flag or a manifest key. There is still no package manager or library install command.

**New and changed flags.** `faber run --shuffle-seed N`, `faber run --debug`, `faber run --threads N`, `faber test --solum-in NAME` and `faber corpus --filter TEXT`. `--threads` is accepted only with `--device cpu`, and until the worker device lands it has no effect (`faber` prints a note saying so). The corpus runner reports a `rejects` outcome for programs that are meant to be refused, and `timeout_secs` now bounds only the run phase; setup phases have their own bound.

**Generated code spells names differently.** Parameters and locals are emitted with `p_` and `l_` prefixes in Rust, Go, TypeScript, Swift, Python and Haskell so that a Faber name can never collide with a target keyword; device kernels are `k<id>` and their buffers `b<N>`. Regenerate generated code; older output and this release's runtimes do not mix.

**Targets.** Go gets lazy generators (a range-over-function iterator), imported generators, and package builds that emit declarations from sibling modules; Go and TypeScript use the exporter's canonical spelling for imported names. Swift emits `@escaping` where needed, copies owned collection and genus parameters on entry, and imports Darwin or Glibc by platform. Python gets maps, sets and set operations, anonymous records, interval values, the `ascii` and `bytes` conversions, and the reference Unicode script and property tables in its regex carrier. TypeScript bounded lists are native arrays with a length check, and every `mut` parameter is boxed so that a projected `mut` argument is written back through its place. LLVM reads shared fields of `@ commune` tagged unions. WebAssembly lowers scalar `sqrt` inline and handles recovered float-to-integer conversions. The Go runtime library gains stdio, process, clock and entropy leaves, which `faber build --target go` does not use yet. Metal and WGSL max and min reductions seed from element 0.

**Performance.** The reference runner compiles each regex literal once and borrows block terminators instead of cloning them. The C emitter writes an integer `discerne` as a `switch`, deduplicates interned literals and emits a one-piece template without a join, and the C runtime keeps a position index beside maps and sets, stores the byte and code-point counts of text in a header, and appends lists in bulk. The Cranelift runtime looks maps up by index and builds text in one allocation, MIR lowering mints one check helper per signature, and FHIR and FMIR artifacts are parsed and encoded without the extra round trips. These are code-level improvements checked against the corpus; no throughput figure is claimed.

**`PKG001 target_not_in_this_build`.** Asking a build for a target it was compiled without now answers `PKG001 target_not_in_this_build` instead of failing later. The released binary carries Rust, Faber, TypeScript, Go, Swift, Python, Haskell, FHIR, FMIR, WebAssembly, LLVM, Metal, WGSL and S-expression emitters. It also carries two preview targets. `-t c` writes readable C from a checked program, rejects constructs it cannot express by name, and builds with GCC or Clang; it now covers maps, sets, closures with the higher-order list methods, `f32`, optional chaining, standard-input reads, and `ref` and `mut` scalar parameters. `-t clif` writes a native object through Cranelift for a fail-closed subset, and `faber build --target clif` links it. The experimental Pascal, COBOL, Fortran, Odin and BASIC targets are not part of the binary.

### GPU

`faber run --device cpu`, `--device metal` and `--device cuda` run `@ kernel` functions; the Metal route works on Apple silicon (a two-element kernel gave the same result on both). The CUDA route is new: it launches kernels in process through the NVIDIA driver, with PTX that `clang` (NVPTX target) builds from the compiler's NVVM output at run time, and it needs no CUDA toolkit. On an RTX 5070 it ran the whole-tensor kernel programs (elementwise, matmul, scalar arguments and scalar returns) with output equal to `--device reference`. Lane-form kernels (control flow inside a lane, genus parameters, tensor extents, math calls inside a lane) are not lowered for CUDA yet; a call to one fails closed and names the kernel. Without the NVIDIA driver, `--device cuda` fails closed with `E_DEVICE_UNAVAILABLE`. In this release the device gate admits genus locals (constructed, read and written) inside lane-form kernels, Metal lowers elementwise add, subtract, multiply and negate in a kernel, a rank-1 right operand is admitted for matmul, and the max and min reductions on Metal and WGSL seed correctly. `--device reference` runs a kernel as plain sequential code on the runner, the oracle that device results are compared with. CPU, FMIR and runner timings are not GPU performance; no GPU throughput claim is made here.

### Breaking changes

1. **Binding words.** Four words now say how a name is bound.

   | Word | Meaning | Latin |
   | --- | --- | --- |
   | `let T x ← e` | a fixed name | `sit` |
   | `mut T x ← e` | re-pointable and writable | `varia` |
   | `ref T x ← e` | re-pointable and read-only | `de` |
   | `const T X = e` | a compile-time fact, set with `=` | `fixum` |

   Every binding word writes its type slot. There is no short form: `let x ← 3` is `PARSE010 binding_type_slot_required`. Write the type, `let int x ← 3`, or `_` to have it inferred, `let _ x ← 3`. Rewrite old code by this table: a run-time `const T x ← e` becomes `let T x ← e`, and `var T x ← e` becomes `mut T x ← e`. A compile-time `const T X = e` stays as it is. The old spellings are errors: `var` is `PARSE010 var_retired`, and a run-time `const T x ← e` (Latin `fixum`) is `PARSE010 runtime_const_retired`. The product does not ship a migration tool, and `faber format` refuses a file that still holds the old words, so run `faber check`, which names every site, and rewrite by hand. A bare parameter is `ref`: the function may read it and may not write it. To write a parameter, mark it `mut` in the signature and at the call, `grow(mut xs)`. A `ref` or `mut` name may hold `T ∪ none` when the other member is a reference type (a class, a collection or text). Over a number or other scalar it is `SEM008 scalar_access_marker`, bare or optional. The binders of a loop, `ex`, `match`, sort, reduce and destructuring take `let` or `mut`. A `const` binder is `PARSE010 binder_fixum_retired`, and a `ref` binder is `PARSE010 ref_binder_refused`.

   ```fab
   class Node {
       const int LIMIT = 3
       let string tag = "n"
       mut int value
       mut Node next optional
   }

   fn grow(mut list<int> xs) → void {
       xs.append(9)
   }

   fn last(Node head) → int {
       ref Node ∪ none cursor ← head
       while cursor not is none {
           if cursor.next is none {
               return cursor.value
           }
           cursor ← cursor.next
       }
       return head.value
   }

   main {
       let Node b ← Node { value = 2 }
       let Node a ← Node { value = 1, next = b }
       mut list<int> xs ← [1]
       grow(mut xs)
       print last(a), Node.LIMIT, xs.length()
   }
   ```

   ```text
   2 3 2
   ```

2. **Class fields.** An instance field is `let T x = e` (fixed after construction) or `mut T x = e` (writable). A field marked `ref` is `PARSE010 ref_field_refused`. The old read-only field `const T x` with no initializer is `PARSE010 const_member_requires_initializer`, and `var T x` is `PARSE010 field_modifier_missing`; write `let` and `mut`. A field written `const T X = e` is now a type-level constant, not an instance field (see the next entry).
3. **Class-level `static` members.** `static` (Latin `generis`) members of a class are retired: `static T X = e` there is `PARSE010 static_member_retired`. A type-level constant is `const T X = e` in the class body, and you read it through the type, `Tab.X`. Storing into it is `SEM020 assignment_to_const_member`. State that changes belongs in a `mut` field.
4. **Environment variables.** `FABER_LIBRARY_HOME` and the other `FABER_*` and `RADIX_*` switches listed under Tooling no longer do anything; use `--library-home`, `[paths] library_home` and the new flags.
5. **Unknown escapes.** An unknown backslash escape in a string literal is `LEX003 unknown_escape`; the old pass-through is gone. Use a guillemet string for text with quotes.
6. **Empty literals.** `{}` and `[]` need a typed cell (a declared type or an inference site); `let _ a ← {}` is `SEM016 inferred_constructor_no_expected_type` and `let list<_> a ← []` is `SEM014 cannot_infer_empty_list_element_type`.
7. **Templates.** Numbered holes count from 0; a template that skips a number or leaves an argument unread is now an error.
8. **Row operations need the axis marker.** `norm_rms(1, …)` and `norm_layer(1, …)` with a bare integer are `SEM057 axis_marker_required`; write `axis 1`. `sum(1)` and `mean(1)` with a bare integer are unknown methods.
9. **Renamed methods.** `rms_norm` is `norm_rms`, `rope_norm` is `norm_rope`, `layer_norm` is `norm_layer`; the Vector, Matrix and Tensor elementwise methods are `subtracted`, `multiplied` and `divided` (the old `subtract`, `multiply` and `divide` on those types are unknown methods); the set method `symmetric_difference` is `difference_symmetric`, and the sparse `nonzero_count` is `count_nonzero`.
10. **Standard library signatures.** File-system, process, console, net, HTTP and WebSocket calls report `⇥ IoFault`; end of input (`console.read_line`, `console.read_bytes`) and an unset variable (`process.read_env`) are `∪ none`. `process.spawn` and `process.detach` no longer take `directory` and `environment`. `time.interval` returns a `Ticker` that you read with `time.tick`. Callers that matched on the old error types must be updated.
11. **Removed library modules.** `norma:cache`, `norma:compression`, `norma:database`, `norma:model`, `norma:optimizer` and `norma:yaml` are gone; importing one is `PKG001 unknown_library_module`.
12. **Generated identifiers.** Emitted names carry `p_` and `l_` prefixes (see Tooling); anything that scraped generated source must follow.

### Known issues

Carried from 1.13 and re-checked against this build. Two 1.13 items are fixed (range containment on the MIR targets, and `faber convert` on files that import library types), and compiled programs can now do I/O, with the edges listed first below.

- **Libraries cannot be installed.** The graphics, autograd and UI libraries still have no install command and `faber doctor` reports them not found; `--library-home` only points at a directory.
- **The I/O route has edges.**
  - Under `faber run`, the `*_async` file, clock and TCP wrappers are refused during lowering, an HTTP server and client in one program (a loopback) is refused, and a WebSocket client and server in one program can hang instead of finishing.
  - In generated Rust, a package that uses TCP, HTTP or WebSocket does not compile (`faber build --target rust` hands rustc a program it rejects), and a few catch forms over an imported `IoFault` do not compile either.
  - Go and TypeScript packages build for pure code, but a package that uses the I/O modules is refused (`PKG001 leaf_unsupported_on_target` for Go; the TypeScript build fails in code generation). `faber targets` still lists Go and TypeScript package compilation as unsupported even though pure-code packages build.
- **Records without a declared type do not run.** A bare `{ field = value }` literal checks and emits in Rust, but the runner stops with `missing type information for MIR lowering`; write `record<g: f32, w: int> { g = 1.0, w = 2 }` to run one. `faber check --lower` reports the program as one that checks but does not lower.
- **Printing a `list<b8, N>` on the runner** writes the raw bytes instead of `[0x01, 0x02, …]`; an unbounded `list<b8>` prints correctly.
- **Some shipped example files are stale.** Most of the loose example files under the standard library's `exempla` directory (the `chorda` and `stdlib-nativum` groups) fail `faber check` because they import module names that no longer exist, such as `norma:solum`; three more fail on tensor calls or a missing export. The example packages there check clean.
- **Device limits.** The full-size flood simulation completes on Metal, but its accuracy comparison against the donor program was withdrawn because no correct run can meet it; the reduced grid is still checked to 0.01 m. A throwing kernel can throw only a constant text per failure site. The CPU worker count has no effect yet.
- **Regex engine gaps by target** (carried, and narrower for Python): Go has no Unicode `\b`; TypeScript clears a quantified group's captures at each iteration; Swift differs on line terminators under `(?m)`, on `\b` next to combining marks and on some case folds; Python rebinds the capture of a nullable repeated group to the empty text after an extra empty iteration, where the reference keeps the earlier value. TypeScript, Swift and Python are backtracking engines and can take exponential time on hostile patterns. Racket (`sexp`) and Haskell refuse regex constructs by name.
- **Haskell** also refuses string templates and ranges.
- **WebAssembly** types a 32-bit float local as `f64`.
- **Ledger runs only on the runner,** and `ledger<K, V> {}` with an empty brace body is refused as an unfinished operation; use a keyed literal.

### Not in this release

- A package manager and library install command. Cista has no published release.
- Ratio, plus-minus and superscript-power types and the set-algebra glyphs are designed but not built (`x²`, `±` and `∖` are lexical errors).
- `trap { }` still returns a bare union of its result and error types. The built-in `trapped<R, T>` result type is registered in the compiler, but its name cannot be written in source yet.
- The C and Cranelift targets are previews: they cover a subset of the language and refuse the rest by name. Neither runs under `faber run`.
- CUDA lane-form kernels. The flood simulation and the lane-form acceptance packages run on Metal and `--device reference`, not on CUDA.
- Radix stays at 0.84.0 (no separate Radix release).
- Public publication of the Go runtime module and `@faber/runtime` is still pending; neither is on its package registry.

### Open source

Faber's source is public at <https://github.com/faberlang/faber> under `MIT OR Apache-2.0`. The repository holds the compiler front end, the reference runner, the standard library (Norma), the grammar and locale packs, the corpus and a public test suite, the FHIR and FMIR artifact formats, the C generator and the Cranelift native backend, the two coding-agent skills (`skills/faber` for writing Faber and `skills/faberlang` for changing the repository), and the scripts that regenerate the grammar files and the compatibility matrices, with measurement for the columns whose backends are public (`faber` and `runner`), and it builds a working `faber` that checks, formats and runs programs. The released binary also carries the code generators that are not part of the public source (Rust, Go, TypeScript, Swift, Python, Haskell, LLVM, WebAssembly and the GPU emitters), which is why installing this release, not building the public tree, is the way to get every target. The repository takes no outside pull requests. Faber 1.14 is part of the experimental 1.x series, so treat the public source the same way: expect it to keep changing, and pin an exact version.

The previous public repository is now `faberlang/faber-1.x` and is archived. Its `v1.x` tags were carried into the new repository, so projects pinned to a 1.x tag keep resolving. History in the new repository starts on 2026-08-02. Releases continue to be published at <https://github.com/faberlang/releases>.

---

[All releases](/releases/) · [Start](/start/)
