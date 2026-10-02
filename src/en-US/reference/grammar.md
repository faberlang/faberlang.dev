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

Faber's grammar is written down as a list of rules, which the compiler calls
productions. Each rule says how one piece of the language is built from
smaller pieces: a loop from a keyword, a binding and a block, a block from
statements. You do not need to read the rules to write Faber. The
[cheat sheet](/cheatsheet/) and the language pages teach every form by
example; this section is for looking up which words belong to which part of
the language.

The 258 rules are grouped into the families below. Each family page lists
the words you write in that part of the language and links each one to its
[term page](/en-US/corpus/).

## Production families {#production-families}

| Family | What it covers |
|---|---|
| [Programs, regions & imports](/en-US/reference/grammar/program.html) | The shape of a source file: optional frontmatter, the optional `module` region, the top-level statement spine, imports, and the program entry points and test suites. |
| [Declarations & bindings](/en-US/reference/grammar/declarations.html) | Bindings, functions, generic parameters, closures, classes, and the fields and methods a class holds. |
| [Annotations & directives](/en-US/reference/grammar/annotations.html) | The `@` annotation family: the generic shape, the kernel (`@ kernel`), compiler-lane (`@ radix`), and capability (`@ call`) directives. |
| [Types & contracts](/en-US/reference/grammar/types.html) | Type syntax and the declarations built on it: interfaces, type aliases, enums, tagged unions, and relational schemas. |
| [Statements & control flow](/en-US/reference/grammar/statements.html) | Statements and control flow: conditionals, loops, `switch` and `match`, guards, extraction, loop and function transfer, and the diagnostic statements. |
| [Expressions & operators](/en-US/reference/grammar/expressions.html) | Expressions and the operator stack, from the assignment root down through the precedence ladder to calls, literals, and the collection and JSON forms. |
| [Patterns & destructuring](/en-US/reference/grammar/patterns.html) | Patterns and destructuring: the atoms a match arm accepts, type and alias patterns, and the object and array destructuring forms. |
| [Error channel](/en-US/reference/grammar/errors.html) | The error channel: throwing, guarded throws, and the local `catch` handler that recovers an error into a value. |
| [Lexical structure & glyphs](/en-US/reference/grammar/lexical.html) | The terminal tokens the lexer produces: identifiers, numbers, strings, width markers, and the frontmatter delimiter. |

## Formal grammar {#formal-grammar}

The rules themselves are the parser's own definition of valid syntax. They are
written for models and tools, in the English reader spellings, and live on one
page: [every production](/agents/grammar/productions.md), with the shorter
[forms the agent pages use](/agents/grammar.md). The
[target matrix](/toolchain/target-matrix.html) is the authority on whether a
given target supports a form. Latin stays the compiler's canonical form, and
`faber explain <term>` prints a mapping from the compiler itself.
