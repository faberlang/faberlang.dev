+++
title = "EBNF grammar"
section = "references"
order = 1
sources = [
  "radix/EBNF.md",
]
+++

The canonical Faber grammar is defined in the Radix repository at
`radix/EBNF.md`. It is the formal authority for all language syntax.

The grammar covers:

- Lexical structure (glyphs, keywords, literals, comments)
- Declarations (functio, genus, implendum, typus, discretio, ordo)
- Statements (binding, control flow, returns, iteration)
- Expressions (calls, operators, conversions, literals)
- Annotations (@ syntax)
- CLI annotations (@ cli, @ optio, @ operandus, @ imperium)
- Type expressions (primitives, generics, sugar forms)
- Module system (importa)

```ebnf
(* excerpt: function declaration *)
funcDecl = 'functio' ident genericParams? '(' paramList ')' ('→' type)? ('⇥' type)? block;
block    = '{' stmt* '}';
```
