+++
title = "Projects and examples"
section = "projects"
order = 4
sources = []
translation_kind = "fallback"
source_locale = "en-US"
source_hash = "sha256:0b7a36b44a44e748ef7fd159a0f42e49d90dcb063f7809cb9ff291a7127abcee"
+++
**Translation status:** Hindi reader-locale proof. Prose falls back to the English source for this Stage 7 slice; Faber code fences pass through the `hi` render step during the site build.


After hello-world, move into real packages. Faber is package-oriented; the
fastest way to learn is to check and read existing packages that exercise the
same compiler surface you plan to use.

## Public repositories {#repositories}

| Repository | Start here | Why |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`, application packages, tracks | Public corpus and application examples |
| [`faberlang/norma`](https://github.com/faberlang/norma) | `norma:*` packages | Standard library source |
| [`faberlang/faber`](https://github.com/faberlang/faber) | CLI wrapper | User-facing build tool |
| [`faberlang/cista`](https://github.com/faberlang/cista) | package-store CLI/lib | Package management surface |
| [`faberlang/triga`](https://github.com/faberlang/triga) | `triga:*` source | Graphics and geometry library |

## Clone a learning workspace {#clone-workspace}

```bash
mkdir faber-learning
cd faber-learning
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

Packages with `norma:*` imports resolve dependencies from the Cista package
store recorded in `faber.lock`. Use `FABER_LIBRARY_HOME` only when you
intentionally want a local resolver override for library development.

## Read examples in this order {#read-order}

1. [Quick tour](/start/) for the surface grammar.
2. [Hello, Faber](/start/hello.html) for a single package.
3. [Corpus](/corpus/) for one page per keyword or construct.
4. [Examples](/start/examples.html) for larger applications.
5. [Faber build tool](/tooling/faber-build-tool.html) for CLI details.

## Agent workflow {#agent-workflow}

Agents should not infer syntax from prose alone. Use the machine surfaces and
then validate generated code:

```bash
curl -fsSL https://faberlang.dev/llms.txt
faber check path/to/package
```

For package work, cite the repo, package path, command, and diagnostic code in
reports. If you touch docs with fenced Faber code in this site, run the fence
validator before claiming the examples still compile.

## What comes after the start track {#after-start}

| Goal | Read |
|---|---|
| Learn syntax | [Syntax](/syntax/) |
| Understand locales | [Reader locale](/features/reader-locale.html) |
| Use the compiler | [Faber build tool](/tooling/faber-build-tool.html) and [Radix compiler](/tooling/radix-compiler.html) |
| Browse constructs | [Corpus](/corpus/) |
| Build with libraries | [Ecosystem](/ecosystem/) |

## Next {#next}

| Previous | Continue |
|---|---|
| [Commands you will use](/start/commands.html) | [Examples](/start/examples.html) |
