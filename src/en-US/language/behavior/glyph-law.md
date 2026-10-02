+++
title = "The glyph law"
section = "language"
order = 10
sources = [
  "radix/corpus/assignatio/",
  "radix/corpus/operatores/",
  "radix/docs/design/faber-canonical-surface.md",
]
+++

Most languages spell two different jobs with one symbol. `=` declares a field
of a type and also stores a value into a variable. Those jobs happen at
different times, and a reader should not have to guess which one a line is
doing. Faber splits them.

- `←` is a **runtime event**. It binds a value to a name, reassigns it, or
  mutates it. Every `←` in a program happens when the program runs.
- `=` is a **compile-time fact**. It fixes the shape of a value inside a
  literal, or a declaration's metadata. Nothing happens at run time.
- `→` declares a function's return type; `⇥` declares its error channel. Both
  describe flow, and both are written where the flow is declared.
- `≡` tests equality, `↦` converts at run time and may fail, `∷` asserts a type
  at compile time.

The rule behind the split is *one sign, one job*. A glyph may have exact
aliases, but it should not carry unrelated meanings. That is why a reader can
scan a Faber function and see every data-flow operation at once: every `←` is
live, and every `=` is settled before the program starts.

## What it looks like {#shape}

```faber
genus Punctum {
    fixum numerus x
    fixum numerus y
}

incipit {
    fixum _ p ← Punctum { x = 10, y = 20 }
    varia numerus count ← 0
    count ← count + 1
    nota p.x, count
}
```

```text
$ faber run
10 1
```

`p ← Punctum { … }` runs: it attaches a value to the name `p`. The `x = 10`
inside the braces does not run — it is the shape of the value being built,
known while compiling. `count ← 0` then `count ← count + 1` are two runtime
events in sequence. Nothing here is a matter of style; the glyph decides.

## One canonical spelling, many sugars {#canonical}

The same separation runs one level up, between *what a construct means* and
*how it is spelled*. Faber defines one canonical spelling for each construct
and accepts sugar spellings that parse to exactly the same node. The parser
does not prefer one over the other; `faber format --locale la` re-emits the
canonical form, while author mode preserves what was written.

Numeric containers follow it (`tf32[4]` and `tensor<f32, [4]>` are the same
type), annotations follow it (`@ option verbose …` and the braced record are
the same `HirAnnotation`), and reader locales follow it — Latin is the
canonical surface, every pack is a rendering of it.

## Why it matters {#why}

Two properties fall out of the split:

- **Local reasoning.** Nothing about a line depends on distant context. A
  reader sees the declared shape and the runtime step separately, without
  knowing a library's internals.
- **Lossless round-trips.** Because the canonical form is defined and the
  sugar is a rendition of it, a program can be reformatted, converted, or
  re-emitted without changing its meaning. The glyphs and the type-first order
  survive every rendering; only the words change.

The full glyph inventory, including the comparison and logic operators, is in
[Glyphs and Latin](/language/glyphs.html). The design laws that keep these
choices stable are in [Design notes](/reference/design.html).
