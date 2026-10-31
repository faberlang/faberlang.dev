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

- [all](all.md) — Marks a test hook as applying to every case.
- [args](args.md) — Binds command-line arguments for an entry point.
- [as](as.md) — Introduces an alias name.
- [assert](assert.md) — Asserts that a condition is true at runtime.
- [async](async.md) — Callable posture for asynchronous finite functions.
- [async_generator](async_generator.md) — Callable posture for asynchronous stream functions.
- [async_main](async_main.md) — Declares the asynchronous program entry point.
- [async_setup](async_setup.md) — Registers an async before-each test hook.
- [async_teardown](async_teardown.md) — Registers an async after-each test hook.
- [await](await.md) — Awaits a promissum and discards the success value.
- [await_const](await_const.md) — Awaits a promissum and binds an immutable name.
- [await_var](await_var.md) — Awaits a promissum and binds a mutable name.
- [before](before.md) — Creates an exclusive range with a Latin keyword.
- [bool](bool.md) — Primitive types bivalens, vacuum, and ignotum.
- [break](break.md) — Breaks out of the innermost loop.
- [call](call.md) — ad opens a sermo endpoint and materializes the stream with an explicit conversio target.
- [case](case.md) — Introduces a branch inside an elige or discerne statement.
- [catch](catch.md) — Starts a catch block.
- [class](class.md) — Declares a concrete type with fields and methods.
- [comptime](comptime.md) — Computes a module constant's value at build time.
- [const](const.md) — Declares an immutable binding.
- [continue](continue.md) — Continues with the next loop iteration.
- [cursor](cursor.md) — Compatibility annotation for stream/generator posture.
- [debug](debug.md) — Writes a debug value to standard error.
- [default](default.md) — Starts the default branch of an elige or discerne statement.
- [describe](describe.md) — Groups related test cases into a named suite.
- [description](description.md) — Attaches a description string to CLI metadata.
- [do](do.md) — Starts a scoped do-while style loop.
- [elif](elif.md) — Adds an else-if branch after a previous si branch.
- [else](else.md) — Runs the fallback branch when preceding conditional branches do not match.
- [embed](embed.md) — Embeds a package file into a module constant at build time.
- [enum](enum.md) — Declares an enumeration.
- [errors](errors.md) — Marks a function parameter or binding as carrying an error value.
- [exit](exit.md) — Sets the exit code or exit expression for an entry point.
- [expect_failure](expect_failure.md) — Defines a single test case and its modifiers.
- [false](false.md) — Represents the false boolean value and can prefix a falsity check.
- [flaky](flaky.md) — Rejected by faber test because flaky retries are not executed.
- [float](float.md) — Primitive floating-point number type.
- [fn](fn.md) — Declares a named function or method.
- [for](for.md) — Starts a for-each iteration statement.
- [format](format.md) — Creates a formatted string with `§` placeholders.
- [from](from.md) — Extracts fields from a value into local bindings.
- [generator](generator.md) — Callable posture for synchronous stream (generator) functions.
- [global](global.md) — Marks an option or operand as global.
- [guard](guard.md) — Groups early-exit guard checks before the main body of a function.
- [if](if.md) — Starts a conditional branch that runs when its condition is true.
- [implements](implements.md) — Declares that a type implements one or more implendum contracts.
- [import](import.md) — Imports names from another module or package source.
- [instant](instant.md) — Absolute point-in-time primitive with precision contract.
- [int](int.md) — Primitive integer number type.
- [interface](interface.md) — Declares a behavioral contract with method signatures.
- [is](is.md) — Tests whether a value's runtime type is a given type.
- [lambda](lambda.md) — Declares or explains an inline closure expression; compact ∴ syntax is preferred for new code.
- [let](let.md) — Declares an inferred immutable local.
- [line](line.md) — Reads one line of input.
- [list](list.md) — Generic ordered collection type.
- [list<b8>](list<b8>.md) — A byte buffer is a list<b8>; hex literals like |de ad be ef| write one.
- [main](main.md) — Declares the synchronous program entry point.
- [map](map.md) — Generic key/value map type.
- [match](match.md) — Starts an exhaustive pattern match over a value or values.
- [mut](mut.md) — Declares a mutable binding.
- [mut (function)](mut (function).md) — Marks a mutable borrowed parameter.
- [never](never.md) — Primitive never type for code paths that do not return normally.
- [none](none.md) — The absent-member type: none (la nihil) is the type, null (la nulla) is its value.
- [not](not.md) — Negates a boolean expression.
- [object](object.md) — Declares a type alias.
- [only](only.md) — Marks a test as the only test to run.
- [only_in](only_in.md) — Restricts a test to a named environment or target.
- [operand](operand.md) — Declares a CLI operand annotation.
- [option](option.md) — Declares a CLI option annotation.
- [optional](optional.md) — Marks a named declaration slot (parameter or genus field) as voluntary — the caller or provider may omit the value.
- [options](options.md) — Binds CLI options metadata to a function declaration.
- [panic](panic.md) — Raises a fatal error or panic.
- [pass](pass.md) — Marks an explicit no-op statement.
- [private](private.md) — Marks a declaration as module-private (the default tier).
- [promise](promise.md) — Promise-like result type associated with async finite functions.
- [protected](protected.md) — Reserved visibility annotation rejected by semantic analysis.
- [public](public.md) — Marks an import as re-exported from the current module.
- [range](range.md) — Selects numeric range iteration in an itera loop.
- [read](read.md) — Reads input from the active input stream.
- [readonly](readonly.md) — Marks a function as non-mutating.
- [record](record.md) — Labeled ad-hoc record type: construction, .name access, objectPattern, and holes.
- [ref](ref.md) — Introduces borrowed iteration or borrowed parameters.
- [reject](reject.md) — Reject a condition or throw a recoverable error.
- [repeat](repeat.md) — Runs a test N times and passes only if every run passes.
- [require](require.md) — Require a condition or throw a recoverable error.
- [rest](rest.md) — Collects remaining parameters, operands, or extracted fields.
- [return](return.md) — Returns a value from a function.
- [return_await](return_await.md) — Awaits a promissum and returns its success value from a fiet body.
- [selective_import](selective_import.md) — Selective imports bind exported members by name: one exported value or type per fixum local, with the imported file interface supplying the complete type.
- [self](self.md) — Refers to the current instance inside a method.
- [set](set.md) — Generic set collection type.
- [setup](setup.md) — Registers a before-each test hook.
- [skip](skip.md) — Marks a test case as skipped with a reason.
- [spread](spread.md) — Spreads an array or collection literal into its surrounding expression.
- [step](step.md) — Sets the step for a range.
- [string (type)](string (type).md) — Primitive string/text type.
- [switch](switch.md) — Starts a value-based branch statement.
- [tag](tag.md) — Attaches a test tag string.
- [teardown](teardown.md) — Registers an after-each test hook.
- [test](test.md) — Defines a single test case and its modifiers.
- [throw](throw.md) — Throws a recoverable error.
- [timeout](timeout.md) — Sets a wall-clock timeout in seconds for a test modifier.
- [todo](todo.md) — Marks a test case as pending future work with a reason.
- [true](true.md) — Represents the true boolean value and can prefix a truthiness check.
- [tuple](tuple.md) — Labeled iuncta elements: type args, construction, member access, objectPattern, and holes.
- [type](type.md) — Declares a type alias.
- [union](union.md) — Declares a tagged union with variant payloads.
- [unknown](unknown.md) — Primitive types bivalens, vacuum, and ignotum.
- [until](until.md) — Creates an inclusive range with a Latin keyword.
- [variant](variant.md) — Constructs a tagged union variant.
- [void](void.md) — Primitive no-value return type.
- [warn](warn.md) — Writes a warning message.
- [while](while.md) — Repeats a block while a condition remains true.
- [write](write.md) — Writes a value to standard output.
- [yield](yield.md) — Yields one value from a generator.
- [∪](∪.md) — Declares a type alias.

## Operators

- [!(](!(.md) — Asserted member, index, and call access on known-present values.
- [!.](!..md) — Asserted member, index, and call access on known-present values.
- [![](![.md) — Asserted member, index, and call access on known-present values.
- [=](=.md) — Assigns a value to a binding, field, or assignable expression.
- [?(](?(.md) — A `?(` call runs only when the function value is present, and gives `none` when it is absent.
- [?.](?..md) — Null-safe member, index, and call access.
- [?[](?[.md) — Null-safe member, index, and call access.
- [and](and.md) — Combines boolean expressions with logical and.
- [coalesce](coalesce.md) — Provides a default when the left side holds `null`.
- [list<T, size lo‥hi>](list<T, size lo‥hi>.md) — A length range on a list: growing past the maximum or shrinking below the minimum reports on the error channel, and a range of at least one element is never empty.
- [modulus<u16>](modulus<u16>.md) — Unsigned 16-bit modular-word arithmetic and bit-pattern edges.
- [modulus<u32>](modulus<u32>.md) — Unsigned 32-bit modular-word arithmetic and bit-pattern edges.
- [modulus<u64>](modulus<u64>.md) — Unsigned 64-bit modular-word arithmetic and bit-pattern edges.
- [modulus<u8>](modulus<u8>.md) — Unsigned 8-bit modular-word arithmetic and bit-pattern edges.
- [non est](non est.md) — Bitwise or and est-negation operators.
- [or](or.md) — Combines boolean expressions with logical or.
- [saturating<W, lo‥hi>](saturating<W, lo‥hi>.md) — A range as the second argument of saturating: a store clamps into the range, not only into the width.
- [then](then.md) — Introduces a compact statement consequent.
- [trapping<W, lo‥hi>](trapping<W, lo‥hi>.md) — A range as the second argument of trapping: a store inside the range keeps its value, a store outside it traps.
- [whole-width range](whole-width range.md) — The existing store-policy spellings are the whole-width range: saturating<u8> is saturating<u8, 0…255>, u8 is trapping<u8, 0…255>.
- [wrapping<W, lo‥hi>](wrapping<W, lo‥hi>.md) — A range as the second argument of wrapping: a store wraps around the range, offset by its low end.
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
- [⇇](⇇.md) — Copy-into: target ⇇ value writes every value of a tensor into the existing storage of another tensor; storage identity is preserved and ← only ever rebinds a name.
- [⇐](⇐.md) — Bitwise and, or, xor, not, and shifts on numerus operands.
- [⇒](⇒.md) — Bitwise and, or, xor, not, and shifts on numerus operands.
- [⇜](⇜.md) — Sink-into writes one exactly typed item with ⇜, the operator form of sink.sink(item).
- [⇥](⇥.md) — Success return type and recoverable alternate-exit type in function signatures.
- [∈](∈.md) — Checks whether a value appears in a collection.
- [∧](∧.md) — Bitwise and, or, xor, not, and shifts on numerus operands.
- [∨](∨.md) — Bitwise or and est-negation operators.
- [∴](∴.md) — Compact consequent after si/dum heads via ergo, with ∴ reserved for closure bodies.
- [∷](∷.md) — Converts a value with explicit runtime parsing or coercion semantics.
- [≡](≡.md) — Equality and ordering comparisons returning bivalens.
- [≢](≢.md) — Equality and ordering comparisons returning bivalens.
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
- [command](command.md) — CLI root with options, operands, subcommands, and module mounts.
- [commands](commands.md) — CLI root with options, operands, subcommands, and module mounts.
- [future](future.md) — Compatibility annotation for asynchronous posture.
- [unstable](unstable.md) — Marks an interface method as planned but unavailable for a target.
- [version](version.md) — Attaches a version string to a CLI root.

## Literals

- [reshape](reshape.md) — Captured backtick templates for bound payloads.

## Modifiers

- [throws](throws.md) — Marks a function as able to throw along a recoverable channel.

## Types

- [atomic](atomic.md) — atomic<i32> operations are storage-sensitive compiler-owned methods.
- [bench](bench.md) — Marks a test for metered or measured execution.
- [block-string](block-string.md) — Block textus literals with embedded quotes and newlines.
- [f16](f16.md) — the bare `f16` type-position width marker.
- [first](first.md) — Marks a test for metered or measured execution.
- [guillemet](guillemet.md) — Guillemet textus literals: quotes and apostrophes need no escape.
- [matrix](matrix.md) — matrix<T, [R, C]> is a register-class type distinct from tensor.
- [named-holes](named-holes.md) — Named template holes, positional rendering, and forma capture.
- [string](string.md) — Short quoted textus string literals and template application.
- [take_last](take_last.md) — Marks a test for metered or measured execution.
- [tensor](tensor.md) — tensor<T, Figura> declaration shell with rank-0 vacua.
- [trapped](trapped.md) — The result of a capture boundary: trap { ... } reifies the error channel into a value read by match.
- [vector](vector.md) — vector type declarations: long form and vf32 sugar.

## Concepts

- [manifest](manifest.md) — faber.toml package metadata for build, run, and test.
- [prae](prae.md) — Angle-bracket generic parameters on functions and declarations.
- [reducta-first](reducta-first.md) — First-match reduction: reducta via prima ex <tensor> sit x { redde <predicate> } yields the first live element (row-major) whose predicate holds, `none` for no match and empty sources.
- [sum](sum.md) — Sequential sum-reduce expression: reducta via summa ex <tensor> apud [i] sit s.
- [targets](targets.md) — Compilation backends listed by faber targets or radix targets.
- [thread](thread.md) — Distributed reducta via summa ex … filum kernel inside @ nucleum.

## Conversions

- [Bits](Bits.md) — The Bits conversio hint is retired: a bit pattern is a b16, b32 or b64 value, and ↦ bN reads or writes it — u16↔f16, u16↔bf16, u32↔f32, u64↔f64 only.
- [finite](finite.md) — finite()-style NaN detection on float payloads via the bN field-read gate (exponent 0xFF, fraction ≠ 0), never via x ≢ x.

Fetch list: https://faberlang.dev/agents/index.md
