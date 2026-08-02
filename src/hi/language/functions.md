+++
translation_kind = "translated"

title = "Functions and control flow"
section = "language"
order = 3
sources = [
  "radix/README.md (Language Orientation, Borrowing and Mutability, How Faber Feels)",
  "examples/corpus/functio/",
  "examples/corpus/de/",
  "examples/corpus/in/",
  "examples/corpus/ex/",
  "radix/docs/design/semantic-ownership.md",
  "radix/README.md (Control Flow Shape, Canonical Surface)",
  "examples/corpus/si/",
  "examples/corpus/itera/",
  "examples/corpus/dum/",
  "examples/corpus/custodi/",
  "examples/corpus/discerne/",
  "examples/corpus/elige/",
  "radix/README.md (Type and Size Generics)",
  "examples/corpus/generic/",
  "examples/corpus/functio/generic-call-type-args.fab",
]
+++

## Functions

Faber में फ़ंक्शन `functio` का उपयोग करके घोषित किए जाते हैं। पैरामीटर के लिए type-first सिंटैक्स और return type के लिए glyph का उपयोग किया जाता है।

### मूल सिंटैक्स {#basic-syntax}

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

### उदाहरण {#examples}

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

### Return मान {#return-values}

सामान्य return के लिए `redde` का उपयोग करें:

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

`vacuum` return type के लिए खाली `redde`:

```faber
functio tace() → vacuum {
    redde
}
```

### Borrowing और mutability (`de`, `in`, `ex`) {#borrowing-and-mutability}

Faber पैरामीटर पर छोटे पूर्वसर्गों के माध्यम से बताता है कि कोई मान किस प्रकार पास किया जाता है:

| Marker | उद्देश्य | सामान्य Rust lowering |
|--------|---------|----------------------|
| *(none)* | स्वामित्व वाला मान | `T` by value |
| `de` | साझा borrow (केवल पढ़ने योग्य) | `&T` |
| `in` | mutable borrow | `&mut T` |
| `ex` | consume करना (callee में move करना) | `T` by move |

```faber locale=la
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

### प्रवेश बिंदु {#entry-point}

प्रोग्राम का entry point `incipit` होता है:

```faber
incipit {
    nota "ingressus"
}
```

### CLI प्रवेश बिंदु {#cli-entry-point}

CLI प्रोग्रामों के लिए `incipit argumenta` parsed command arguments प्राप्त करता है:

```faber locale=la
@ cli "echo"
@ descriptio "Prints text"
@ operandus ceteri textus words
incipit argumenta args {
    itera ex args.words fixum word {
        nota word
    }
}
```

### पासिंग मोड — `sponte` {#passing-mode-sponte}

`sponte` ऐसे पैरामीटर को चिह्नित करता है जिसे caller छोड़ सकता है:

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```

## Control flow

### सशर्त शाखाकरण {#conditional-branching}

#### si / sin / secus {#si-sin-secus}

```faber
incipit {
    fixum _ condition ← verum
    si condition {
        # truthy branch
        nota "matched"
    }
}
```

`else-if` और `else` के साथ:

```faber
incipit {
    fixum _ score ← 85
    si score ≥ 90 {
        nota "A"
    } sin score ≥ 80 {
        nota "B"
    } secus {
        nota "C"
    }
}
```

#### ergo के साथ संक्षिप्त शाखा {#compact-branch-with-ergo}

एकल-कथन वाली शाखा का बॉडी `ergo` का उपयोग करता है:

```faber
functio classify(numerus b, bivalens ready, numerus value) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    si ready ergo redde value
    redde nihil
}
```

### पुनरावृत्ति {#iteration}

#### मान — itera ex {#values-itera-ex}

```faber
functio inveni(lista<numerus> items, numerus target) → numerus ∪ nihil {
    itera ex items fixum item {
        si item ≡ target ergo redde item
    }
    redde nihil
}
```

#### कुंजियाँ — itera de {#keys-itera-de}

```faber
incipit {
    fixum _ tabula ← { "unus": 1, "duo": 2 }
    itera de tabula fixum key {
        nota key
    }
}
```

#### परास — itera ab {#range-itera-ab}

```faber
itera ab 0‥10 fixum i {
    nota i
}
```

### While लूप {#while-loops}

```faber
incipit {
    fixum _ condition ← verum
    dum condition {
        # body
        tacet
    }
}
```

### Guard अनुभाग — custodi {#guard-sections-custodi}

`custodi` किसी फ़ंक्शन के मुख्य बॉडी से पहले शीघ्र-बाहर निकलने वाली जाँचों को समूहित करता है।  
प्रत्येक `si` क्लॉज़ एक क्रमिक guard है:

```faber
functio divide(numerus a, numerus b) → numerus {
    custodi {
        si b ≡ 0 {
            redde 0
        }
    }
    redde a / b
}
```

v1 में `custodi` से बाहर निकलना संभव नहीं है — यह लूप नहीं, बल्कि एक guard rail है।

### पैटर्न मिलान — elige {#pattern-matching-elige}

`elige` पहली मेल खाने वाली शाखा चुनता है:

```faber
functio describe(numerus value) → textus {
    elige value {
        casu 1 { redde "one" }
        casu 2 { redde "two" }
        ceterum { redde "many" }
    }
}
```

### टैग किए गए यूनियन का मिलान — discerne {#tagged-union-matching-discerne}

`discerne` `discretio` के सभी वैरिएंट का पूर्ण मिलान करता है:

```faber
discretio Exitus {
    Bonum { textus nuntius },
    Malum { textus causa }
}

functio refer(Exitus eventus) → textus {
    discerne eventus {
        casu Bonum fixum nuntius { redde nuntius }
        casu Malum fixum causa { redde "Error: §"(causa) }
    }
}
```

### Try ब्लॉक — fac / cape {#try-blocks-fac-cape}

`fac` ऐसा ब्लॉक खोलता है जिसमें त्रुटि उत्पन्न हो सकती है, और `cape` उसे संभालता है:

```faber
functio divide(numerus a, numerus b) → numerus {
    redde a / b
}

functio tutus(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    } cape err {
        mone err
        redde 0
    }
}
```

## Generics

फ़ंक्शन, टाइप उपनाम, `genus`, और `implendum` `<T>` सिंटैक्स का उपयोग करके टाइप पैरामीटर स्वीकार करते हैं।

### जेनेरिक फ़ंक्शन {#generic-functions}

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

### कॉल-साइट पर स्पष्ट टाइप आर्ग्युमेंट {#explicit-callsite-type-arguments}

```faber
functio identitas<T>(T valor) → T { redde valor }

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde nihil
}

fixum _ value ← identitas<numerus>(7)
fixum _ maybe ← primum<numerus>([value])
```

### जेनेरिक `genus` {#generic-genus}

```faber
genus Par<T> {
    T primus
    T secundus
}
```

### आकार पैरामीटर {#size-parameters}

`magnitudo` जेनेरिक पैरामीटर सूचियों में आकार/इंडेक्स पैरामीटर घोषित करता है:

```faber
functio crea<T, magnitudo N>() → tensor<T, [N]> {
    redde vacua
}
```
