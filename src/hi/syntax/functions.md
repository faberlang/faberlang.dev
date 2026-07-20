+++
translation_kind = "translated"

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


prose_hash = "sha256:ccb89a2cbb2274f10a9cf14807cb355ac88f2a65ac03fb0a5d6cea62f999df28"
code_hash = "sha256:c87e3ad8847578d6410ecd0d2147894a502f9700487a2d53bf6e86334209d5ad"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber में फ़ंक्शन `functio` का उपयोग करके घोषित किए जाते हैं। पैरामीटर के लिए type-first सिंटैक्स और return type के लिए glyph का उपयोग किया जाता है।

## मूल सिंटैक्स {#basic-syntax}

```faber
functio twice(numerus n) → numerus {
    redde n
}
```

त्रुटि चैनल के साथ:

```faber
functio parse(textus input) → numerus ⇥ textus {
    redde 0
}
```

## उदाहरण {#examples}

```faber
# No parameters, no return
functio saluta() {
    nota "Salve, Mundus!"
}

# Parameter, no explicit return
functio dic(textus verbum) {
    nota verbum
}

# Parameter and return type
functio duplica(numerus n) → numerus {
    redde n * 2
}

# Multiple parameters
functio adde(numerus a, numerus b) → numerus {
    redde a + b
}
```

## Return मान {#return-values}

सामान्य return के लिए `redde` का उपयोग करें:

```faber
functio porta(numerus x) → numerus {
    si x < 0 ∴ redde 0
    redde x * 2
}
```

`vacuum` return type के लिए खाली `redde`:

```faber
functio tace() → vacuum {
    redde
}
```

## Borrowing और mutability (`de`, `in`, `ex`) {#borrowing-and-mutability}

Faber पैरामीटर पर छोटे पूर्वसर्गों के माध्यम से बताता है कि कोई मान किस प्रकार पास किया जाता है:

| Marker | उद्देश्य | सामान्य Rust lowering |
|--------|---------|----------------------|
| *(none)* | स्वामित्व वाला मान | `T` by value |
| `de` | साझा borrow (केवल पढ़ने योग्य) | `&T` |
| `in` | mutable borrow | `&mut T` |
| `ex` | consume करना (callee में move करना) | `T` by move |

```faber
# Shared borrow
functio imprime(de textus label) → vacuum {
    nota label
}

# Mutable borrow
functio duplica(in numerus value) → vacuum {
    value ← value * 2
}

# Consume
functio consume(ex textus buffer) → textus {
    redde buffer
}

# Owned
functio salve(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}
```

यही शब्द (`de`, `ex`) अन्य constructs में भी दोबारा उपयोग किए जाते हैं — हर `ex` को “consume” न समझें:

| Surface | भूमिका |
|---------|--------|
| पैरामीटर पर `de textus name` | साझा borrow |
| पैरामीटर पर `in numerus count` | mutable borrow |
| पैरामीटर पर `ex textus buffer` | callee में move करना |
| `itera ex items fixum item` | मानों पर iterate करना |
| `itera de tabula fixum key` | keys पर iterate करना |
| `ex source fixum x, ceteri rest` | fields को destructure करना |
| `importa ex "path"` | module से import करना |

## Entry point {#entry-point}

प्रोग्राम का entry point `incipit` होता है:

```faber
incipit {
    nota "ingressus"
}
```

## CLI entry point {#cli-entry-point}

CLI प्रोग्रामों के लिए `incipit argumenta` parsed command arguments प्राप्त करता है:

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

## Passing mode — `sponte` {#passing-mode-sponte}

`sponte` ऐसे पैरामीटर को चिह्नित करता है जिसे caller छोड़ सकता है:

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```
