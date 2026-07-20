+++
translation_kind = "translated"

title = "Variables and binding"
section = "syntax"
order = 2
sources = [
  "radix/README.md (Runtime binding vs structural definition, Language Orientation)",
  "examples/corpus/fixum/",
  "examples/corpus/sit/",
]


prose_hash = "sha256:2e0180766e816022e87ea9eb6c8c531d30993227db9aa56c9224c9a98d3d984f"
code_hash = "sha256:122027c8f10ed33d224e3b23653279e91d19d9a17f432190340909eea5dd9ab3"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber में तीन variable keywords और assignment के लिए एक विशेष glyph है। मुख्य अंतर `fixum` (केवल एक बार लिखने योग्य) और `varia` (स्वतंत्र रूप से फिर से assign करने योग्य) के बीच है, तथा `←` (runtime flow) और `=` (संरचनात्मक field shape) के बीच है।

## fixum — अपरिवर्तनीय binding {#fixum-immutable-binding}

`fixum` bindings केवल एक बार लिखी जा सकती हैं। इन्हें initializer के साथ या उसके बिना declare किया जा सकता है। यदि initializer के बिना declare किया गया हो, तो पढ़ने से पहले इन्हें ठीक एक बार assign करना आवश्यक है। दूसरी assignment अस्वीकार कर दी जाती है।

```faber
fixum numerus count ← 0
fixum textus name ← "Marcus"
fixum _ inferred ← [1, 2, 3]
```

Deferred initialisation:

```faber
incipit {
    fixum numerus factor
    si verum {
        factor ← 10
    } secus {
        factor ← 100
    }
    nota factor
}
```

## varia — परिवर्तनशील binding {#varia-mutable-binding}

`varia` bindings को स्वतंत्र रूप से फिर से assign किया जा सकता है:

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

## sit — inferred immutable sugar {#sit-inferred-immutable-sugar}

`sit`, `fixum _` का sugar है — inferred type वाली अपरिवर्तनीय binding:

```faber
incipit {
    sit salve ← "Salve"
    sit nomen ← "Marcus"
    sit x ← 42

    # Deferred form
    sit label
    label ← "deferred"
}
```

## Runtime binding बनाम structural definition {#runtime-binding-vs-structural-definition}

Faber उस `=` को दो अलग भूमिकाओं में बाँटता है, जिसे अधिकांश भाषाएँ एक ही रूप में समेट देती हैं:

| Glyph | भूमिका | उपयोग |
|-------|--------|-------|
| `←` | Runtime flow | Initial binding, reassignment, mutation |
| `=` | Structural shape | Literals और metadata के भीतर field names |

```faber
genus Point {
    numerus x
    numerus y
}

incipit {
    # Runtime: ← attaches a value to a name at execution time
    varia numerus count ← 0
    varia textus label ← "ready"
    count ← count + 1

    # Structural: = defines field values inside a type literal
    fixum _ p ← Point {
        x = 10,
        y = 20
    }
}
```

## ex से field extraction {#ex-field-extraction}

`ex` किसी value से fields निकालकर local bindings में रखता है:

```faber
genus Persona {
    textus nomen
    numerus aetas
}

incipit {
    fixum _ p ← Persona { nomen = "Marcus", aetas = 30 }
    ex p fixum nomen, aetas
    # prints "Marcus"
    nota nomen
}
```

## Postfix increment और decrement {#postfix-increment-and-decrement}

`⊕` और `⊖`, परिवर्तनशील `numerus` places के लिए postfix increment/decrement statements हैं। ये केवल statements के रूप में उपयोग किए जा सकते हैं — इनका कोई expression value नहीं होता और इनके prefix रूप नहीं हैं:

```faber
incipit {
    varia numerus i ← 0
    # i becomes 1
    i ⊕
    # i becomes 0
    i ⊖
}
```
