+++
title = "Types & contracts"
section = "grammar-types"
order = 5
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

A type is what a value is. Faber writes the type before the name, so you
read the kind of thing first. This page is the syntax of types and the
declarations that introduce new ones: `interface` is a contract of
methods, `type` is another name for an existing type, `enum` is a closed
set of named constants, `union` is a tagged choice with variants, and
`schema` describes relational columns.

Absence is a union, not a question mark. A missing integer is
`i32 ∪ none`; the missing value is `null`. There is no `i32?`. Widths are
bare markers — `i32`, `f32` — written in type position.

Everyday types, type first:

```faber locale=en
main {
    const string name ← "Marcus"
    const i32 age ← 30
    const bool flag ← true
    const list<i32> nums ← [1, 2, 3]
    const i32 ∪ none missing ← null
    print name
    print age
    print flag
    print nums
    print missing
}
```

A `type` alias is a transparent name. It does not create a new kind of
value:

```faber locale=en
type Signum = i32
type Nomina = list<string>

main {
    const Signum signum ← 42
    const Nomina sodales ← ["Gaius", "Lucius"]
    print signum
    print sodales
}
```

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`interface`](/en-US/corpus/interface.html) | `implendum_decl` |
| [`fn`](/en-US/corpus/fn.html) | `implendum_method_decl` |
| [`type`](/en-US/corpus/type.html) | `typus_decl` |
| [`enum`](/en-US/corpus/enum.html) | `ordo_decl` |
| [`union`](/en-US/corpus/union.html) | `discretio_decl` |
| [`schema`](/en-US/corpus/schema.html) | `schema_decl` |
| [`column`](/en-US/corpus/column.html) | `schema_column` |
| [`ref`](/en-US/corpus/ref.html), [`mut`](/en-US/corpus/mut.html) | `union_hole_type` |
| [`ref`](/en-US/corpus/ref.html), [`mut`](/en-US/corpus/mut.html) | `owned_type` |
| [`record`](/en-US/corpus/record.html) | `ratio_type` |

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
