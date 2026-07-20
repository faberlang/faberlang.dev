+++
translation_kind = "translated"

title = "Control flow"
section = "syntax"
order = 4
sources = [
  "radix/README.md (Control Flow Shape, Canonical Surface)",
  "examples/corpus/si/",
  "examples/corpus/itera/",
  "examples/corpus/dum/",
  "examples/corpus/custodi/",
  "examples/corpus/discerne/",
  "examples/corpus/elige/",
]


prose_hash = "sha256:a3b4f77dd7b65f73e835e9e2f65070f22930ad14df15c71a262b81113827a814"
code_hash = "sha256:e257a14fcd068ec06da9199895e899ffb03f352663185ce892b355beadb5cd0b"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
## सशर्त शाखाकरण {#conditional-branching}

### si / sin / secus {#si-sin-secus}

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

### ergo के साथ संक्षिप्त शाखा {#compact-branch-with-ergo}

एकल-कथन वाली शाखा का बॉडी `ergo` का उपयोग करता है:

```faber
functio classify(numerus b, bivalens ready, numerus value) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    si ready ergo redde value
    redde nihil
}
```

## पुनरावृत्ति {#iteration}

### मान — itera ex {#values-itera-ex}

```faber
functio inveni(lista<numerus> items, numerus target) → numerus ∪ nihil {
    itera ex items fixum item {
        si item ≡ target ergo redde item
    }
    redde nihil
}
```

### कुंजियाँ — itera de {#keys-itera-de}

```faber
incipit {
    fixum _ tabula ← { "unus": 1, "duo": 2 }
    itera de tabula fixum key {
        nota key
    }
}
```

### परास — itera ab {#range-itera-ab}

```faber
itera ab 0‥10 fixum i {
    nota i
}
```

## While लूप {#while-loops}

```faber
incipit {
    fixum _ condition ← verum
    dum condition {
        # body
        tacet
    }
}
```

## Guard अनुभाग — custodi {#guard-sections-custodi}

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

## पैटर्न मिलान — elige {#pattern-matching-elige}

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

## टैग किए गए यूनियन का मिलान — discerne {#tagged-union-matching-discerne}

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

## Try ब्लॉक — fac / cape {#try-blocks-fac-cape}

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
