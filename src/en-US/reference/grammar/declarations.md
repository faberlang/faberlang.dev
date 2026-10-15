+++
title = "Declarations & bindings"
section = "grammar-declarations"
order = 3
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "radix/grammar/EBNF.md",
  "radix/grammar/sources/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

A declaration introduces a name the rest of the file can use. Bindings hold
values: `const` is written once, `var` can be assigned again, and `let` is
the short inferred form of an immutable binding. Functions, closures, and
classes are declarations too — they name a callable or a type, and the
fields and methods it holds.

The type always comes before the name: `i32 count`, never `count: i32`.
`←` stores a value at run time. `=` is for a field's shape inside a
literal, not for binding a local. Generic parameters (`<T>`), `implements`
bounds, and the modifiers on a function (`async`, `throws`, `args`) belong
here because they are part of how the name is declared.

A function and two bindings:

```faber locale=en
fn divide(i32 a, i32 b) → i32 ∪ none {
    if b ≡ 0 then return null
    return a / b
}

main {
    let i32 seven ← 7
    mut i32 n ← 3
    n ← n + 1
    print divide(seven, n)
}
```

A class names its fields the same way. Methods are functions on the class;
`self` is the instance:

```faber locale=en
class Span {
    let f64 low
    let f64 high

    fn contains(f64 x) → bool {
        return self.low ≤ x and x ≤ self.high
    }
}

main {
    let Span bytes ← Span { low = 0.0, high = 255.0 }
    print bytes.contains(128.0)
}
```

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`embed`](/en-US/corpus/embed.html) | `insere_expr` |
| [`const`](/en-US/corpus/const.html), [`mut`](/en-US/corpus/mut.html) | `fixum_decl` |
| [`await_const`](/en-US/corpus/await_const.html), [`await_var`](/en-US/corpus/await_var.html) | `figendum_decl` |
| [`let`](/en-US/corpus/let.html) | `sit_decl` |
| [`ref`](/en-US/corpus/ref.html) | `ref_decl` |
| [`let`](/en-US/corpus/let.html), [`mut`](/en-US/corpus/mut.html) | `array_destruct` |
| [`let`](/en-US/corpus/let.html), [`mut`](/en-US/corpus/mut.html) | `object_destruct` |
| [`fn`](/en-US/corpus/fn.html) | `functio_decl` |
| [`implements`](/en-US/corpus/implements.html) | `generic_bound` |
| [`rest`](/en-US/corpus/rest.html), [`optional`](/en-US/corpus/optional.html), [`as`](/en-US/corpus/as.html), [`coalesce`](/en-US/corpus/coalesce.html) | `parameter` |
| [`args`](/en-US/corpus/args.html), [`errors`](/en-US/corpus/errors.html), [`exit`](/en-US/corpus/exit.html), [`throws`](/en-US/corpus/throws.html), [`readonly`](/en-US/corpus/readonly.html), [`options`](/en-US/corpus/options.html) | `func_modifier` |
| [`async_generator`](/en-US/corpus/async_generator.html), [`async`](/en-US/corpus/async.html), [`generator`](/en-US/corpus/generator.html) | `callable_posture` |
| [`then`](/en-US/corpus/then.html) | `ergo_joint` |
| [`do`](/en-US/corpus/do.html) | `fac_block` |
| [`lambda`](/en-US/corpus/lambda.html) | `clausura_legacy_expr` |
| [`class`](/en-US/corpus/class.html), [`implements`](/en-US/corpus/implements.html) | `genus_decl` |
| [`fn`](/en-US/corpus/fn.html) | `nondum_method_decl` |
| [`let`](/en-US/corpus/let.html), [`optional`](/en-US/corpus/optional.html), [`mut`](/en-US/corpus/mut.html) | `genus_field_decl` |
| [`const`](/en-US/corpus/const.html) | `genus_const_decl` |
| [`let`](/en-US/corpus/let.html), [`optional`](/en-US/corpus/optional.html), [`mut`](/en-US/corpus/mut.html) | `field_decl` |
| [`fn`](/en-US/corpus/fn.html) | `functio_method_decl` |
## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
