+++
translation_kind = "translated"

title = "Errors and testing"
section = "language"
order = 4
sources = [
  "radix/README.md (Return and Error Channels)",
  "examples/corpus/iace/",
  "examples/corpus/fac/",
  "examples/corpus/cape/",
  "radix/docs/design/failable-conversio.md",
]
+++

## Error handling

Faber तीन संबंधित विचारों को अलग रखता है, जिन्हें कई भाषाएँ एक ही
रूप में मिला देती हैं:

| निर्माण | अर्थ |
|-----------|---------|
| `→ T` | सामान्य सफलता रिटर्न चैनल |
| `T ∪ nihil` | सफलता मान डोमेन में अनुपस्थिति |
| `⇥ E` | त्रुटियों के लिए पुनर्प्राप्त करने योग्य वैकल्पिक-निकास चैनल |

### सामान्य रिटर्न {#normal-return}

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

### विफल हो सकने वाले फ़ंक्शन {#failable-functions}

जब कोई फ़ंक्शन त्रुटि चैनल के माध्यम से बाहर निकल सकता हो, तब `⇥` का
उपयोग करें:

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ergo iace "division by zero"
    redde a / b
}
```

### थ्रो करना — iace {#throwing--iace}

`iace` त्रुटि चैनल पर कोई मान भेजता है:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

### रिकवरी — fac / cape {#recovery--fac--cape}

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

### इनलाइन रूपांतरण रिकवरी {#inline-conversion-recovery}

`⇥`, `↦` रूपांतरणों पर इनलाइन रिकवरी मान भी निर्दिष्ट कर सकता है:

```faber
fixum textus raw ← "42"
fixum _ n ← raw ↦ numerus ⇥ 0
```

### केवल-प्रभाव वाला विफल हो सकने वाला फ़ंक्शन {#effectonly-failable}

ऐसे फ़ंक्शन जो त्रुटि देते हैं, लेकिन सफलता मान वापस नहीं करते, उनमें
`→ T` छोड़ दें:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

### वर्तमान स्थिति {#current-status}

`→`, `redde`, `⇥`, `iace`, और `fac` / `cape` लाइव व्याकरण और चेकर
सतहें हैं। पूर्ण `⇥` / `iace` / `cape` रनटाइम व्यवहार के लिए Rust और Go
लोअरिंग में अभी बैकएंड की कमी है — ये टाइप-चेकिंग पास करते हैं, लेकिन
अभी सभी लक्ष्यों के लिए विफल हो सकने वाला रनटाइम कोड उत्पन्न नहीं करते।

## Inline testing

Faber में भाषा के भीतर ही निर्मित एक प्रथम-श्रेणी परीक्षण फ्रेमवर्क है, जिसमें तीन कीवर्ड हैं: `probandum` एक परीक्षण सूट घोषित करता है, `proba` एकल परीक्षण केस घोषित करता है, और `adfirma` किसी शर्त की पुष्टि करता है। परीक्षण उसी फ़ाइल में रहते हैं जिसमें उनका परीक्षण किया जाने वाला कोड होता है, `faber test` के माध्यम से चलते हैं, और प्रोडक्शन कोड के समान कंपाइलर पाइपलाइन का समर्थन करते हैं — लोकेल-अवेयर, प्रकार-जाँचे हुए और बहु-लक्ष्यीय।

### तीन कीवर्ड {#keywords}

| कीवर्ड | भूमिका | लगभग समतुल्य |
|---------|--------|----------------|
| `probandum` | नामित परीक्षण सूट घोषित करता है | `describe`, `#[cfg(test)] mod` |
| `proba` | एकल परीक्षण केस घोषित करता है | `it`, `#[test]` |
| `adfirma` | रनटाइम पर किसी शर्त की पुष्टि करता है | `assert!`, `assert_eq!` |

#### probandum — परीक्षण सूट {#probandum-test-suite}

`probandum` ब्लॉक संबंधित परीक्षण मामलों को एक साथ समूहित करता है। परीक्षणों को पदानुक्रम के अनुसार व्यवस्थित करने के लिए सूट को नेस्ट किया जा सकता है:

```faber
probandum "arithmetica" {
    proba "unum plus unum" {
        adfirma 1 + 1 ≡ 2
    }

    proba "multiplicatio" {
        adfirma 3 * 4 ≡ 12
    }

    probandum "implicata" {
        proba "comparatio" {
            fixum _ x ← 10
            adfirma x ≥ 10
        }
    }
}
```

#### proba — परीक्षण केस {#proba-test-case}

`proba` ब्लॉक में परीक्षण का तर्क होता है। इसमें कोई भी Faber कोड — वैरिएबल बाइंडिंग, फ़ंक्शन कॉल, नियंत्रण प्रवाह — इस्तेमाल किया जा सकता है और इसका अंत एक या अधिक `adfirma` पुष्टियों के साथ होता है। चयनात्मक निष्पादन के लिए परीक्षणों पर वैकल्पिक `tag` मार्कर लगाया जा सकता है:

```text
proba "echo formats operands with one space" tag "coreutils" {
    adfirma echo_textus(["hello", "world"]) ≡ "hello world"
}
```

#### adfirma — पुष्टि {#adfirma-assertion}

`adfirma` किसी बूलियन अभिव्यक्ति का मूल्यांकन करता है और उसके असत्य होने पर विफलता की सूचना देता है। विफलता के समय संदर्भ देने के लिए वैकल्पिक संदेश स्ट्रिंग दी जा सकती है:

```faber
incipit {
    fixum _ x ← 10

    # Simple assertion
    adfirma x > 0

    # With custom message
    adfirma x ≡ 10 secus "x decem esse debet"

    # Multiple assertions in sequence
    fixum _ nomen ← "Marcus"
    adfirma nomen ≡ "Marcus"
    adfirma nomen ≠ "" secus "nomen vacuum non sit"
}
```

### कार्यप्रवाह {#workflow}

परीक्षण `faber test` कमांड के माध्यम से चलते हैं:

```text
faber test                        # run all tests in the current package
faber test examples/coreutils/packages/echo  # run tests for a specific package
```

क्योंकि परीक्षण उसी `.fab` फ़ाइल में स्रोत कोड के साथ रहते हैं, इसलिए अलग परीक्षण डायरेक्टरी संरचना, परीक्षण मॉड्यूल घोषणा या परीक्षण और प्रोडक्शन बिल्ड के बीच अलग बिल्ड स्क्रिप्ट की आवश्यकता नहीं होती। कंपाइलर इस्तेमाल किए गए कीवर्ड के आधार पर यह जानता है कि कौन-से ब्लॉक परीक्षण कोड हैं और कौन-से प्रोडक्शन कोड — `probandum` और `proba` को पार्स किया जाता है, लेकिन प्रोडक्शन बिल्ड से बाहर रखा जाता है।

### वास्तविक उदाहरण {#real-world}

coreutils का `echo` पैकेज परीक्षण फ्रेमवर्क को व्यवहार में प्रदर्शित करता है। परीक्षण उसी फ़ाइल में इम्प्लीमेंटेशन के साथ रहते हैं और विकल्प पार्सिंग, एस्केप विस्तार तथा किनारी स्थितियों को कवर करते हैं:

```text
probandum "echo formatting" tag "coreutils" {
    proba "empty operands format as empty text" {
        fixum lista<textus> words ← vacua
        adfirma echo_textus(words) ≡ ""
    }

    proba "single operand is unchanged" {
        adfirma echo_textus(["hello"]) ≡ "hello"
    }

    proba "-E is a leading no-op option" {
        adfirma echo_textus(["-E", "hello", "world"]) ≡ "hello world"
    }

    proba "-n suppresses the trailing newline flag" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }

    proba "-e expands the declared escape subset" {
        adfirma echo_textus(["-e", "a\\nb"]) ≡ "a\nb"
        adfirma echo_textus(["-e", "a\\tb"]) ≡ "a\tb"
    }
}
```

### डिज़ाइन नोट्स {#design}

कई डिज़ाइन विकल्प Faber के परीक्षण फ्रेमवर्क को पारंपरिक तरीकों से अलग बनाते हैं:

- **अलग परीक्षण बाइनरी नहीं।** परीक्षण अलग कंपाइलेशन लक्ष्य नहीं, बल्कि उसी स्रोत फ़ाइल में घोषणाएँ हैं। कंपाइलर परीक्षण ब्लॉकों को प्रोडक्शन आउटपुट से फ़िल्टर कर देता है।
- **डायरेक्टरी नहीं, टैग।** परीक्षण डायरेक्टरी संरचना के बजाय `tag` मार्करों के आधार पर व्यवस्थित किए जाते हैं। किसी परीक्षण को स्थान बदले बिना कई संगठनात्मक अक्षों में शामिल किया जा सकता है।
- **पूर्ण कंपाइलर पाइपलाइन।** परीक्षणों की प्रकार-जाँच और विश्लेषण किया जाता है तथा वे लोकेल-अवेयर होते हैं — परीक्षण आउटपुट पर भी वही `--reader-locale` फ़्लैग लागू होता है।
- **बहु-लक्ष्य।** परीक्षण पैकेज द्वारा लक्षित बैकएंड के माध्यम से चलते हैं — `faber test --interpret` के लिए MIR स्टेपर और `faber test` के लिए कंपाइल्ड Rust।
- **नेस्टेड सूट।** `probandum` ब्लॉक नेस्ट किए जा सकते हैं और उस कोड की संरचना को प्रतिबिंबित करते हैं जिसका वे परीक्षण करते हैं।

### संदर्भ {#references}

1. `examples/corpus/probandum/` — probandum उदाहरण फ़ाइलें
2. `examples/corpus/proba/` — proba उदाहरण फ़ाइलें
3. `examples/corpus/adfirma/` — adfirma उदाहरण फ़ाइलें
4. `examples/coreutils/packages/echo/src/main.fab` — टैग के साथ वास्तविक उपयोग
