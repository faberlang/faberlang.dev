+++
translation_kind = "translated"

title = "Error handling"
section = "syntax"
order = 5
sources = [
  "radix/README.md (Return and Error Channels)",
  "examples/corpus/iace/",
  "examples/corpus/fac/",
  "examples/corpus/cape/",
  "radix/docs/design/failable-conversio.md",
]


prose_hash = "sha256:7b9b055ee1b8fc13b23faefb29514dd947982a0f768d911767255fdc0ee9f738"
code_hash = "sha256:81aa5174263eeb0a80a64870335680dec64748cbdb7896e4de78021d8c4f197f"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber तीन संबंधित विचारों को अलग रखता है, जिन्हें कई भाषाएँ एक ही
रूप में मिला देती हैं:

| निर्माण | अर्थ |
|-----------|---------|
| `→ T` | सामान्य सफलता रिटर्न चैनल |
| `T ∪ nihil` | सफलता मान डोमेन में अनुपस्थिति |
| `⇥ E` | त्रुटियों के लिए पुनर्प्राप्त करने योग्य वैकल्पिक-निकास चैनल |

## सामान्य रिटर्न {#normal-return}

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

## विफल हो सकने वाले फ़ंक्शन {#failable-functions}

जब कोई फ़ंक्शन त्रुटि चैनल के माध्यम से बाहर निकल सकता हो, तब `⇥` का
उपयोग करें:

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ergo iace "division by zero"
    redde a / b
}
```

## थ्रो करना — iace {#throwing--iace}

`iace` त्रुटि चैनल पर कोई मान भेजता है:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

## रिकवरी — fac / cape {#recovery--fac--cape}

कॉलर `fac` ब्लॉक और `cape` हैंडलर के साथ स्थानीय रूप से रिकवरी करते हैं:

```faber
functio divide(numerus a, numerus b) → numerus {
    si b ≡ 0 {
        redde 0
    }
    redde a / b
}

functio tutum(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    }
    cape err {
        mone err
        redde 0
    }
}
```

किसी विफल हो सकने वाले `→ T ⇥ E` फ़ंक्शन को सीधे कॉल करना सामान्य
एक्सप्रेशन नहीं है। ऐसे कॉल को सक्रिय `fac` / `cape` सीमा के भीतर रखें।

## इनलाइन रूपांतरण रिकवरी {#inline-conversion-recovery}

`⇥`, `↦` रूपांतरणों पर इनलाइन रिकवरी मान भी निर्दिष्ट कर सकता है:

```faber
fixum textus raw ← "42"
fixum _ n ← raw ↦ numerus ⇥ 0
```

## केवल-प्रभाव वाला विफल हो सकने वाला फ़ंक्शन {#effectonly-failable}

ऐसे फ़ंक्शन जो त्रुटि देते हैं, लेकिन सफलता मान वापस नहीं करते, उनमें
`→ T` छोड़ दें:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

## वर्तमान स्थिति {#current-status}

`→`, `redde`, `⇥`, `iace`, और `fac` / `cape` लाइव व्याकरण और चेकर
सतहें हैं। पूर्ण `⇥` / `iace` / `cape` रनटाइम व्यवहार के लिए Rust और Go
लोअरिंग में अभी बैकएंड की कमी है — ये टाइप-चेकिंग पास करते हैं, लेकिन
अभी सभी लक्ष्यों के लिए विफल हो सकने वाला रनटाइम कोड उत्पन्न नहीं करते।
