+++
title = "Grammar"
section = "reference"
order = 1
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

The formal grammar for every Faber production, generated from the compiler's
own specification and shown in the English reader spellings. The words in
quotes are the words you write: a loop is `for`, a class is `class`, a function
is `fn`. Rule names (`itera_stmt`, `genus_decl`) are stable grammar identifiers.
Latin stays the compiler's canonical form; `faber explain <term>` prints a
mapping from the compiler itself.

This page is the authority on whether something is valid syntax. The
[target matrix](/toolchain/target-matrix.html) is the authority on whether a
given target supports it.

The productions are grouped into families below. Each family page carries its
productions and links the productions whose keywords have a
[corpus term page](/en-US/corpus/). Uppercase names are lexical terminals;
grammar examples are fragments, not standalone programs.

## Production families {#production-families}

| Family | Productions | What it covers |
|---|---|---|
| [Programs, regions & imports](/en-US/reference/grammar/program.html) | 30 | The shape of a source file: optional frontmatter, the optional `module` region, the top-level statement spine, imports, and the program entry points and test suites. |
| [Declarations & bindings](/en-US/reference/grammar/declarations.html) | 42 | Bindings, functions, generic parameters, closures, classes, and the fields and methods a class holds. |
| [Annotations & directives](/en-US/reference/grammar/annotations.html) | 15 | The `@` annotation family: the generic shape, the kernel (`@ kernel`), compiler-lane (`@ radix`), and capability (`@ call`) directives. |
| [Types & contracts](/en-US/reference/grammar/types.html) | 32 | Type syntax and the declarations built on it: interfaces, type aliases, enums, tagged unions, and relational schemas. |
| [Statements & control flow](/en-US/reference/grammar/statements.html) | 35 | Statements and control flow: conditionals, loops, `switch` and `match`, guards, extraction, loop and function transfer, and the diagnostic statements. |
| [Expressions & operators](/en-US/reference/grammar/expressions.html) | 69 | Expressions and the operator stack, from the assignment root down through the precedence ladder to calls, literals, and the collection and JSON forms. |
| [Patterns & destructuring](/en-US/reference/grammar/patterns.html) | 11 | Patterns and destructuring: the atoms a match arm accepts, type and alias patterns, and the object and array destructuring forms. |
| [Error channel](/en-US/reference/grammar/errors.html) | 4 | The error channel: throwing, guarded throws, and the local `catch` handler that recovers an error into a value. |
| [Lexical structure & glyphs](/en-US/reference/grammar/lexical.html) | 20 | The terminal tokens the lexer produces: identifiers, numbers, strings, width markers, and the frontmatter delimiter. Uppercase rule names here are lexical terminals. |

All 258 productions. Every family page links back here, and rule names stay
stable across the tree so a search for `itera_stmt` finds its one page.
