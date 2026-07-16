+++
title = "Functions"
section = "syntax"
order = 3
sources = [
  "radix/README.md (Language Orientation, Borrowing and Mutability, How Faber Feels)",
  "examples/corpus/functio/",
  "examples/corpus/de/",
  "examples/corpus/in/",
  "examples/corpus/ex/",
  "radix/docs/design/semantic-ownership.md",
]
+++

Functions in Faber are declared with `functio`, using type-first parameter
syntax and a glyph return type.

## Basic syntax

```faber
functio name(parameter_list) → return_type {
    body
}
```

With an error channel:

```faber
functio name(parameters) → return_type ⇥ error_type {
    body
}
```

## Examples

```faber
// No parameters, no return
functio saluta() {
    nota "Salve, Mundus!"
}

// Parameter, no explicit return
functio dic(textus verbum) {
    nota verbum
}

// Parameter and return type
functio duplica(numerus n) → numerus {
    redde n * 2
}

// Multiple parameters
functio adde(numerus a, numerus b) → numerus {
    redde a + b
}
```

## Return values

Use `redde` for normal returns:

```faber
functio porta(numerus x) → numerus {
    si x < 0 ∴ redde 0
    redde x * 2
}
```

Bare `redde` for `vacuum` return type:

```faber
functio tace() → vacuum {
    redde
}
```

## Borrowing and mutability (de, in, ex)

Faber marks how a value is passed with short prepositions on parameters:

| Marker | Intent | Typical Rust lowering |
|--------|--------|----------------------|
| *(none)* | Owned value | `T` by value |
| `de` | Shared borrow (read-only) | `&T` |
| `in` | Mutable borrow | `&mut T` |
| `ex` | Consume (move into callee) | `T` by move |

```faber
// Shared borrow
functio imprime(de textus label) → vacuum {
    nota label
}

// Mutable borrow
functio duplica(in numerus value) → vacuum {
    value ← value * 2
}

// Consume
functio consume(ex textus buffer) → textus {
    redde buffer
}

// Owned
functio salve(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}
```

The same words (`de`, `ex`) are reused in other constructs — do not read
every `ex` as "consume":

| Surface | Role |
|---------|------|
| `de textus name` on parameter | Shared borrow |
| `in numerus count` on parameter | Mutable borrow |
| `ex textus buffer` on parameter | Move into callee |
| `itera ex items fixum item` | Iterate values |
| `itera de tabula fixum key` | Iterate keys |
| `ex source fixum x, ceteri rest` | Destructure fields |
| `importa ex "path"` | Import from module |

## Entry point

The program entry point is `incipit`:

```faber
incipit {
    nota "ingressus"
}
```

## CLI entry point

For CLI programs, `incipit argumenta` receives parsed command arguments:

```faber
@ cli "echo"
@ descriptio "Prints text"
@ operandus ceteri textus words
incipit argumenta args {
    itera ex args.words fixum word {
        nota word
    }
}
```

## Passing mode — `sponte`

`sponte` marks a parameter that may be omitted by the caller:

```faber
functio connect(textus host, numerus port sponte) → vacuum
```
