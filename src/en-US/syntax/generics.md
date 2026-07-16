+++
title = "Generics"
section = "syntax"
order = 6
sources = [
  "radix/README.md (Type and Size Generics)",
  "examples/corpus/generic/",
  "examples/corpus/functio/generic-call-type-args.fab",
]
+++

Functions, type aliases, `genus`, and `implendum` accept type parameters
with `<T>` syntax.

## Generic functions

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

## Explicit call-site type arguments

```faber
fixum _ value ← identitas<numerus>(7)
fixum _ maybe ← primum<numerus>([value])
```

## Generic genus

```faber
genus Par<T> {
    T primus
    T secundus
}
```

## Size parameters

`magnitudo` declares a size/index parameter in generic parameter lists:

```faber
functio crea<T, magnitudo N>() → tensor<T, [N]> {
    // ...
}
```
