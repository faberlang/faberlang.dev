## English source body (fences as <<<FENCE n>>>)

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

<<<FENCE 0>>>

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

<<<FENCE 1>>>

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

| Previous | Next |
|---|---|
| [Commands you will use](/start/commands.html) | [Examples](/start/examples.html) |
