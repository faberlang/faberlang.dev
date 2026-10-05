+++
title = "Annotations & directives"
section = "grammar-annotations"
order = 4
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

An annotation is a `@` line that attaches to the declaration below it. It
does not run. It tells the compiler a fact about that declaration: that it
is exported, that it is a command-line program, that a kernel, compiler
lane, or capability applies.

The generic shape is `@` plus a name, optionally with fields in braces.
`@ public` marks a function an importer can see. `@ cli` names the binary
a package produces. The same family covers `@ kernel`, `@ radix`, and
`@ call` — specialized directives most source meets later. The table
below lists the words those directives use.

```faber locale=en
@ public
fn saluta(string nomen) → string {
    return "Salve, §!"(nomen)
}
```

A command-line entry uses the same `@` shape above `main args`:

```faber locale=en
@ cli { name = "echo" }
@ description "Prints text"
@ operand { rest = true, type = string, binding = words }
main args argv {
    for from argv.words const word {
        print word
    }
}
```

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`kernel`](/en-US/corpus/kernel.html) | `nucleum_sugar` |
| [`kernel`](/en-US/corpus/kernel.html) | `nucleum_braced` |
| [`false`](/en-US/corpus/false.html), [`true`](/en-US/corpus/true.html) | `nucleum_field` |
| [`mut`](/en-US/corpus/mut.html), [`type`](/en-US/corpus/type.html) | `radix_directive` |
| [`call`](/en-US/corpus/call.html) | `ad_annotation` |

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
