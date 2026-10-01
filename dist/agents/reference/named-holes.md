# named-holes

Named template holes, positional rendering, and forma capture.

**Term** `named-holes` · **Section** TYPES

## Syntax

```
"§{label} …"(label: value)
```

## What this teaches

- named-only template application: "§{greet} world"(greet: "Salve")
- mixed named and anonymous STRING holes with positional actuals
- forma capture with a labeled actual; the captured template is erased to §
- named holes erase before rendering, so the output is ordinary text Reject teaching rows (comments only; these must not become stage-3 inputs):
- ordinary-call label: f(greet: "x")
- `=` form: "§ world"(greet = "x")
- unknown label: "§{greet} world"(other: "x")

## Example

```fab
main {
    # A labeled actual fills the named hole.
    const _ named ← "§{greet} world"(greet: "Salve")
    print named

    # A named and an anonymous hole share one positional sequence.
    const _ mixed ← "§{greet} §"("Salve", "Mundus")
    print mixed

    # Named-hole erasure renders the same as the positional § form.
    const _ erased ← "§{greet} world"("Salve")
    print erased

    # Forma capture accepts labels but stores only erased template text.
    const _ captured ← `where id = §{id}`(id: "42")
    print captured.template
}
```

See also: [`forma`](reshape.md), [`format`](format.md), [`string`](string.md), [`string`](textus.md), [`§`](§.md).

Fetch list: https://faberlang.dev/agents/index.md
