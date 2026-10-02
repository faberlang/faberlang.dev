# Reference

One page per `faber explain` entry, generated from the compiler registry so
it cannot drift from it. Fetch a page, or run the same lookup locally:

```bash
faber explain fn
faber explain fn --json
```

Each page names its registry term, its section, and any alternate spelling.
Latin spellings are accepted lookups; the documented spelling is English.

## Keywords

- [all](all.md) (`omnia`) — Marks a test hook as applying to every case.
- [args](args.md) (`argumenta`) — Binds command-line arguments for an entry point.
- [as](as.md) (`ut`) — Introduces an alias name.
- [assert](assert.md) (`adfirma`) — Asserts that a condition is true at runtime.
- [async](async.md) (`fiet`) — Callable posture for asynchronous finite functions.
- [async_generator](async_generator.md) (`fient`) — Callable posture for asynchronous stream functions.
- [async_main](async_main.md) (`incipiet`) — Declares the asynchronous program entry point.
- [async_setup](async_setup.md) (`praeparabit`) — Registers an async before-each test hook.
- [async_teardown](async_teardown.md) (`postparabit`) — Registers an async after-each test hook.
- [await](await.md) (`tacebit`) — Awaits a promissum and discards the success value.
- [await_const](await_const.md) (`figendum`) — Awaits a promissum and binds an immutable name.
- [await_var](await_var.md) (`variandum`) — Awaits a promissum and binds a mutable name.
- [before](before.md) (`ante`) — Creates an exclusive range with a Latin keyword.
- [bool](bool.md) (`bivalens`) — Primitive types bivalens, vacuum, and ignotum.
- [break](break.md) (`rumpe`) — Breaks out of the innermost loop.
- [bytes](bytes.md) (`octeti`) — Primitive byte-buffer type.
- [call](call.md) (`ad`) — ad opens a sermo endpoint and materializes the stream with an explicit conversio target.
- [case](case.md) (`casu`) — Introduces a branch inside an elige or discerne statement.
- [catch](catch.md) (`cape`) — Starts a catch block.
- [class](class.md) (`genus`) — Declares a concrete type with fields and methods.
- [comptime](comptime.md) (`praefixum`) — Computes a module constant's value at build time.
- [const](const.md) (`fixum`) — Declares an immutable binding.
- [continue](continue.md) (`perge`) — Continues with the next loop iteration.
- [cursor](cursor.md) — Compatibility annotation for stream/generator posture.
- [debug](debug.md) (`vide`) — Writes a debug value to standard output.
- [default](default.md) (`ceterum`) — Starts the default branch of an elige or discerne statement.
- [describe](describe.md) (`probandum`) — Groups related test cases into a named suite.
- [description](description.md) (`descriptio`) — Attaches a description string to CLI metadata.
- [do](do.md) (`fac`) — Starts a scoped do-while style loop.
- [elif](elif.md) (`sin`) — Adds an else-if branch after a previous si branch.
- [else](else.md) (`secus`) — Runs the fallback branch when preceding conditional branches do not match.
- [embed](embed.md) (`insere`) — Embeds a package file into a module constant at build time.
- [enum](enum.md) (`ordo`) — Declares an enumeration.
- [errors](errors.md) (`errata`) — Marks a function parameter or binding as carrying an error value.
- [exit](exit.md) (`exitus`) — Sets the exit code or exit expression for an entry point.
- [false](false.md) (`falsum`) — Represents the false boolean value and can prefix a falsity check.
- [flaky](flaky.md) (`fragilis`) — Marks a test as fragile.
- [float](float.md) (`fractus`) — Primitive floating-point number type.
- [fn](fn.md) (`functio`) — Declares a named function or method.
- [for](for.md) (`itera`) — Starts a for-each iteration statement.
- [format](format.md) (`scriptum`) — Creates a formatted string with `§` placeholders.
- [from](from.md) (`ex`) — Extracts fields from a value into local bindings.
- [generator](generator.md) (`fiunt`) — Callable posture for synchronous stream (generator) functions.
- [global](global.md) (`ubique`) — Marks an option or operand as global.
- [guard](guard.md) (`custodi`) — Groups early-exit guard checks before the main body of a function.
- [if](if.md) (`si`) — Starts a conditional branch that runs when its condition is true.
- [implements](implements.md) (`implet`) — Declares that a type implements one or more implendum contracts.
- [import](import.md) (`importa`) — Imports names from another module or package source.
- [instant](instant.md) (`instans`) — Absolute point-in-time primitive with precision contract.
- [int](int.md) (`numerus`) — Primitive integer number type.
- [interface](interface.md) (`implendum`) — Declares a behavioral contract with method signatures.
- [is](is.md) (`est`) — Tests whether a value's runtime type is a given type.
- [lambda](lambda.md) (`clausura`) — Declares or explains an inline closure expression; compact ∴ syntax is preferred for new code.
- [let](let.md) (`sit`) — Declares an inferred immutable local.
- [line](line.md) (`lineam`) — Reads one line of input.
- [list](list.md) (`lista`) — Generic ordered collection type.
- [main](main.md) (`incipit`) — Declares the synchronous program entry point.
- [map](map.md) (`tabula`) — Generic key/value map type.
- [match](match.md) (`discerne`) — Starts an exhaustive pattern match over a value or values.
- [mut](mut.md) (`in`) — Marks a mutable borrowed parameter.
- [never](never.md) (`numquam`) — Primitive never type for code paths that do not return normally.
- [nihil](nihil.md) — Represents the null value and can prefix a null check.
- [not](not.md) (`non`) — Negates a boolean expression.
- [object](object.md) (`objectum`) — Declares a type alias.
- [only](only.md) (`solum`) — Marks a test as the only test to run.
- [only_in](only_in.md) (`solum_in`) — Restricts a test to a named environment or target.
- [operand](operand.md) (`operandus`) — Declares a CLI operand annotation.
- [option](option.md) (`optio`) — Declares a CLI option annotation.
- [optional](optional.md) (`sponte`) — Marks a named declaration slot (parameter or genus field) as voluntary — the caller or provider may omit the value.
- [options](options.md) (`optiones`) — Binds CLI options metadata to a function declaration.
- [panic](panic.md) (`mori`) — Raises a fatal error or panic.
- [pass](pass.md) (`tacet`) — Marks an explicit no-op statement.
- [private](private.md) (`privata`) — Marks a declaration as module-private (the default tier).
- [promise](promise.md) (`promissum`) — Promise-like result type associated with async finite functions.
- [protected](protected.md) (`protecta`) — Reserved visibility annotation rejected by semantic analysis.
- [public](public.md) (`publica`) — Marks an import as re-exported from the current module.
- [range](range.md) (`ab`) — Selects numeric range iteration in an itera loop.
- [read](read.md) (`lege`) — Reads input from the active input stream.
- [readonly](readonly.md) (`immutata`) — Marks a function as non-mutating.
- [record](record.md) (`ratio`) — Labeled ad-hoc record type: construction, .name access, objectPattern, and holes.
- [ref](ref.md) (`de`) — Introduces borrowed iteration or borrowed parameters.
- [reject](reject.md) (`reice`) — Reject a condition or throw a recoverable error.
- [repeat](repeat.md) (`repete`) — Repeats a test a fixed number of times.
- [require](require.md) (`requirit`) — Require a condition or throw a recoverable error.
- [rest](rest.md) (`ceteri`) — Collects remaining parameters, operands, or extracted fields.
- [return](return.md) (`redde`) — Returns a value from a function.
- [return_await](return_await.md) (`reddet`) — Awaits a promissum and returns its success value from a fiet body.
- [selective_import](selective_import.md) — Selective imports bind exported members by name: one exported value or type per fixum local, with the imported file interface supplying the complete type.
- [self](self.md) (`ego`) — Refers to the current instance inside a method.
- [set](set.md) (`copia`) — Generic set collection type.
- [setup](setup.md) (`praepara`) — Registers a before-each test hook.
- [skip](skip.md) (`omitte`) — Marks a test case as skipped with a reason.
- [spread](spread.md) (`sparge`) — Spreads an array or collection literal into its surrounding expression.
- [static](static.md) (`generis`) — Marks a class member as belonging to the type itself.
- [step](step.md) (`per`) — Sets the step for a range.
- [switch](switch.md) (`elige`) — Starts a value-based branch statement.
- [tag](tag.md) — Attaches a test tag string.
- [teardown](teardown.md) (`postpara`) — Registers an after-each test hook.
- [test](test.md) (`proba`) — Defines a single test case.
- [textus](textus.md) — Primitive string/text type.
- [throw](throw.md) (`iace`) — Throws a recoverable error.
- [timeout](timeout.md) (`temporis`) — Sets a wall-clock timeout in seconds for a test modifier.
- [todo](todo.md) (`futurum`) — Marks a test case as pending future work with a reason.
- [true](true.md) (`verum`) — Represents the true boolean value and can prefix a truthiness check.
- [tuple](tuple.md) (`iuncta`) — Labeled iuncta elements: type args, construction, member access, objectPattern, and holes.
- [type](type.md) (`typus`) — Declares a type alias.
- [union](union.md) (`discretio`) — Declares a tagged union with variant payloads.
- [unknown](unknown.md) (`ignotum`) — Primitive types bivalens, vacuum, and ignotum.
- [until](until.md) (`usque`) — Creates an inclusive range with a Latin keyword.
- [var](var.md) (`varia`) — Declares a mutable binding.
- [variant](variant.md) (`finge`) — Constructs a tagged union variant.
- [void](void.md) (`vacuum`) — Primitive no-value return type.
- [warn](warn.md) (`mone`) — Writes a warning message.
- [while](while.md) (`dum`) — Repeats a block while a condition remains true.
- [write](write.md) (`scribe`) — Writes a value to standard output.
- [yield](yield.md) (`cede`) — Yields one value from a generator.
- [∪](∪.md) — Declares a type alias.

## Operators

- [!(](!(.md) — Asserted member, index, and call access on known-present values.
- [!.](!..md) — Asserted member, index, and call access on known-present values.
- [![](![.md) — Asserted member, index, and call access on known-present values.
- [=](=.md) — Assigns a value to a binding, field, or assignable expression.
- [?(](?(.md) — Null-safe member, index, and call access.
- [?.](?..md) — Null-safe member, index, and call access.
- [?[](?[.md) — Null-safe member, index, and call access.
- [and](and.md) (`et`) — Combines boolean expressions with logical and.
- [coalesce](coalesce.md) (`vel`) — Provides a default when the left side is null.
- [modulus<u16>](modulus<u16>.md) — Unsigned 16-bit modular-word arithmetic and bit-pattern edges.
- [modulus<u32>](modulus<u32>.md) — Unsigned 32-bit modular-word arithmetic and bit-pattern edges.
- [modulus<u64>](modulus<u64>.md) — Unsigned 64-bit modular-word arithmetic and bit-pattern edges.
- [modulus<u8>](modulus<u8>.md) — Unsigned 8-bit modular-word arithmetic and bit-pattern edges.
- [non est](non est.md) — Bitwise or and est-negation operators.
- [or](or.md) (`aut`) — Combines boolean expressions with logical or.
- [then](then.md) (`ergo`) — Introduces a compact statement consequent.
- [§](§.md) — String-template substitution holes inside quoted literals.
- [¬](¬.md) — Bitwise and, or, xor, not, and shifts on numerus operands.
- [·](·.md) — Glyph inner product: vector · vector reduces to a scalar dot product.
- [×](×.md) — Glyph cross product: width-3 vectors × multiply into the perpendicular vector.
- [‥](‥.md) — Half-open and inclusive range endpoints in itera ab and ∈.
- […](….md) — Half-open and inclusive range endpoints in itera ab and ∈.
- [←](←.md) — Assigns a value to a binding, field, or assignable expression.
- [↑](↑.md) — Postfix increment statement for a mutable numerus place.
- [→](→.md) — Success return type and recoverable alternate-exit type in function signatures.
- [↓](↓.md) — Postfix increment statement for a mutable numerus place.
- [↤](↤.md) — Conversion-directed assignment: evaluate the right side, convert it to the statically known type of the left place through the ↦ route, then assign.
- [↦](↦.md) — Converts a value with explicit runtime parsing or coercion semantics.
- [⇇](⇇.md) — Exact-output transfer: sink ⇇ payload invokes a callable sink value once per payload — no formatting, no separators, no channel selection, no conversions.
- [⇐](⇐.md) — Bitwise and, or, xor, not, and shifts on numerus operands.
- [⇒](⇒.md) — Bitwise and, or, xor, not, and shifts on numerus operands.
- [⇥](⇥.md) — Success return type and recoverable alternate-exit type in function signatures.
- [∈](∈.md) — Checks whether a value appears in a collection.
- [∧](∧.md) — Bitwise and, or, xor, not, and shifts on numerus operands.
- [∨](∨.md) — Bitwise or and est-negation operators.
- [∴](∴.md) — Compact consequent after si/dum heads via ergo, with ∴ reserved for closure bodies.
- [∷](∷.md) — Converts a value with explicit runtime parsing or coercion semantics.
- [≠](≠.md) — Equality and ordering comparisons returning bivalens.
- [≡](≡.md) — Equality and ordering comparisons returning bivalens.
- [≤](≤.md) — Equality and ordering comparisons returning bivalens.
- [≥](≥.md) — Equality and ordering comparisons returning bivalens.
- [⊗](⊗.md) — Glyph outer product: vector ⊗ vector yields the rank-summed matrix of pairwise products.
- [⊘](⊘.md) — Assigns a value to a binding, field, or assignable expression.
- [⊙](⊙.md) — Glyph Hadamard: identical-shape elementwise product on vectors, matrices, and tensors.
- [⊚](⊚.md) — Assigns a value to a binding, field, or assignable expression.
- [⊛](⊛.md) — Assigns a value to a binding, field, or assignable expression.
- [⊜](⊜.md) — Assigns a value to a binding, field, or assignable expression.
- [⊥](⊥.md) — Converts a value with explicit runtime parsing or coercion semantics.
- [⊻](⊻.md) — Bitwise and, or, xor, not, and shifts on numerus operands.
- [✓](✓.md) — The value conditional: c ✓ a ✗ b, one level only.

## Annotations

- [@](@.md) — Introduces an annotation for the following declaration or statement.
- [alias](alias.md) — CLI root with options, operands, subcommands, and module mounts.
- [cli](cli.md) — CLI root with options, operands, subcommands, and module mounts.
- [command](command.md) (`imperium`) — CLI root with options, operands, subcommands, and module mounts.
- [future](future.md) (`futura`) — Compatibility annotation for asynchronous posture.
- [imperia](imperia.md) — CLI root with options, operands, subcommands, and module mounts.
- [unstable](unstable.md) (`nondum`) — Marks an interface method as planned but unavailable for a target.
- [versio](versio.md) — Attaches a version string to a CLI root.

## Literals

- [reshape](reshape.md) (`forma`) — Captured backtick templates for bound payloads.

## Modifiers

- [throws](throws.md) (`iacit`) — Marks a function as able to throw along a recoverable channel.

## Types

- [atomic](atomic.md) — atomic<i32> operations are storage-sensitive compiler-owned methods.
- [bench](bench.md) (`metior`) — Marks a test for metered or measured execution.
- [block-string](block-string.md) — Block textus literals with embedded quotes and newlines.
- [f16](f16.md) — the bare `f16` type-position width marker.
- [matrix](matrix.md) — matrix<T, [R, C]> is a register-class type distinct from tensor.
- [named-holes](named-holes.md) — Named template holes, positional rendering, and forma capture.
- [string](string.md) — Short quoted textus string literals and template application.
- [take](take.md) (`prima`) — Marks a test for metered or measured execution.
- [take_last](take_last.md) (`ultima`) — Marks a test for metered or measured execution.
- [tensor](tensor.md) — tensor<T, Figura> declaration shell with rank-0 vacua.
- [vector](vector.md) — vector type declarations: long form and vf32 sugar.

## Concepts

- [manifest](manifest.md) — faber.toml package metadata for build, run, and test.
- [prae](prae.md) — Angle-bracket generic parameters on functions and declarations.
- [primus_quem](primus_quem.md) — Dedicated total first-match expression: first live element of a source satisfying the owned ubi predicate, nihil for no-match and empty sources.
- [sum](sum.md) (`summa`) — Sequential sum-reduce expression: summa ex <tensor> apud [i] fixum s { redde <term> }.
- [targets](targets.md) — Compilation backends listed by faber targets or radix targets.
- [thread](thread.md) (`filum`) — Distributed sum-reduce kernel admit: summa ex … apud [i] filum f fixum s { redde <term> } inside @ nucleum.

## Conversions

- [Bits](Bits.md) — The Bits conversio hint is an exact-width IEEE bitcast — u16↔f16, u16↔bf16, u32↔f32, u64↔f64 only — never a value conversion.
- [finite](finite.md) — finite()-style NaN detection on float payloads via the Bits field-read gate (exponent 0xFF, fraction ≠ 0), never via x ≠ x.

Fetch list: https://faberlang.dev/agents/index.md
