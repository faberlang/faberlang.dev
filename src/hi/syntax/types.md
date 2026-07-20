+++
translation_kind = "translated"

title = "Data types"
section = "syntax"
order = 1
sources = [
  "radix/README.md (Core Type Surfaces, Numeric Widths, Tensors And Sparsa, GPU Core Types)",
  "radix/docs/design/numeric-type-sugar.md",
  "radix/docs/design/tensor-intrinsics.md",
  "radix/docs/design/lista-intrinsics.md",
  "radix/docs/design/comparison-operators.md",
  "radix/EBNF.md",
  "examples/corpus/typi/",
  "examples/corpus/tensor/",
  "examples/corpus/lista/",
]


prose_hash = "sha256:b3f22d05ed3eb8bbc5d3322fd71f7677a77ba9909b6c80f1cfa00455320e7de5"
code_hash = "sha256:c2351c4cdd58a84dd89c4adc956cce28ce5d7a3db572eae85b44d4a6dbb5d48a"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber में एक स्थिर, प्रकार-प्रथम प्रकार-प्रणाली है। हर घोषणा में नाम से पहले प्रकार आता है: `textus nomen`, न कि `nomen: textus`। प्रकार-प्रणाली में स्केलर प्रिमिटिव, जेनरिक संग्रह, निर्धारित-आकार वाली संख्याएँ, टेंसर और GPU-संबंधी रजिस्टर प्रकार शामिल हैं।

## प्रिमिटिव प्रकार {#primitive-types}

| प्रकार | भूमिका | उदाहरण लिटरल |
|------|------|-----------------|
| `textus` | Unicode स्ट्रिंग | `"Salve, munde"` |
| `ascii` | निश्चित मशीन टोकन | `'solum:lege'` |
| `numerus` | चिह्नित पूर्णांक (डिफ़ॉल्ट i64) | `42` |
| `fractus` | फ्लोटिंग-पॉइंट (डिफ़ॉल्ट f64) | `3.14` |
| `bivalens` | बूलियन | `verum`, `falsum` |
| `vacuum` | यूनिट / कोई मान नहीं | — |
| `nihil` | null / अनुपस्थित | `nihil` |
| `instans` | अवधि / समय-क्षण | — |
| `json` | संकलन-समय JSON मान | `{ "key": "value" }` |
| `octeti` | हेक्स बाइट अनुक्रम | \|00ff\| |

## निर्धारित-आकार वाले संख्यात्मक प्रकार {#sized-numeric-types}

`numerus` और `fractus` की डिफ़ॉल्ट चौड़ाइयाँ (i64 और f64) होती हैं और इनके लिए स्पष्ट चौड़ाई वाले रूप भी उपलब्ध हैं:

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

प्रकार की स्थिति में चौड़ाई-संक्षेप उपलब्ध है: `i8` … `u64`, `f16`, `f32`, `f64`, `numerus<W>` / `fractus<W>` के समतुल्य हैं।

## Nullable प्रकार {#nullable-types}

Nullable मान यूनियन सिंटैक्स `T ∪ nihil` का उपयोग करते हैं:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio maybe() → textus ∪ nihil {
    redde nihil
}
```

Faber में `T?` या `Option<T>` सिंटैक्स नहीं है। यूनियन स्पष्ट रूप से लिखना आवश्यक है।

## प्रकार उपनाम {#type-aliases}

```faber
typus UserId = numerus
```

## जेनरिक {#generics}

फ़ंक्शन, प्रकार उपनाम, `genus` और `implendum`, `<T>` सिंटैक्स के साथ प्रकार पैरामीटर स्वीकार करते हैं:

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

कॉल-साइट पर स्पष्ट प्रकार आर्ग्युमेंट भी समर्थित हैं:

```faber
functio identitas<T>(T valor) → T { redde valor }

fixum numerus value ← identitas<numerus>(7)
```

## संग्रह {#collections}

| प्रकार | भूमिका | संक्षिप्त रूप |
|------|------|-------|
| `lista<T>` | क्रमबद्ध डायनेमिक संग्रह | `lf32`, `lu32` |
| `tabula<K, V>` | कुंजी-मान मैप | — |
| `tensor<T, Figura>` | घना, निश्चित-आकार वाला बफ़र | `tf32[4]`, `ti64[2,3]` |
| `sparsa<T, Figura>` | विरल, निश्चित-आकार वाला बफ़र | `sf32[4]`, `si64[2,3]` |
| `intervallum` | रेंज प्रकार | — |
| `copia<T>` | अनियंत्रित सेट | — |
| `cursor<T>` | लेज़ी स्ट्रीम | — |

```faber
fixum lista<numerus> nums ← [1, 2, 3]
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

## टेंसर प्रकार {#tensor-types}

`tensor<T, Figura>` घना, निश्चित-आकार वाला कंटेनर है:

| रूप | अर्थ |
|---------|---------|
| `tensor<T, Figura>` | मानक लेखन |
| `tensor<T, []>` | रैंक-0 (स्केलर कंटेनर) |
| `tensor<T, _>` | आकार-अनुमान रिक्ति |
| `tensor<T, [N]>` | रैंक-1 वेक्टर |
| `tensor<T, [N, M]>` | रैंक-2 मैट्रिक्स |

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

## GPU कोर प्रकार {#gpu-core-types}

GPU और रजिस्टर कार्य के लिए सिस्टम लेन इन प्रकारों को पहचानती है।
जिन पैकेज लक्ष्यों में हार्डवेयर समर्थन नहीं होता, वे इन्हें अस्वीकार कर देते हैं:

```faber
functio half(f16 x) → f16 { redde x }

functio add(matrix<f32, [2, 2]> a, matrix<f32, [2, 2]> b) → matrix<f32, [2, 2]> {
    redde a.addita(b)
}

functio swap(atomic<i32> cell, i32 value) → i32 {
    redde cell.exchange(value)
}
```

## प्रकारों पर borrow मार्कर {#borrow-markers}

Borrow मार्कर (`de`, `in`, `ex`) पैरामीटर स्थितियों में प्रकारों पर दिखाई दे सकते हैं। वे बताते हैं कि कोई मान किस प्रकार पास किया जाता है:

```faber locale=la
# shared borrow — caller retains ownership
functio imprime(de textus label) → vacuum { }

# mutable borrow — caller lends mutable access
functio duplica(in numerus value) → vacuum { }

# move — caller gives up ownership
functio consume(ex textus buffer) → textus {
    redde buffer
}
```

## तुलना नीति {#comparison-policy}

| ऑपरेटर | परिवार | व्यवहार |
|----------|--------|-----------|
| `≡`, `≠` | सटीक समानता | समान प्रकार आवश्यक; `nihil` को अपवाद |
| `≈`, `≉` | संख्यात्मक मान समानता | केवल संख्यात्मक लैटिस |
| `<`, `≤`, `>`, `≥` | क्रम निर्धारण | संख्यात्मक, instant, स्केलर टेक्स्ट |
| `intra` | रेंज समावेशन | रेंज में संख्यात्मक मान |
| `inter` | संग्रह सदस्यता | संग्रह में तत्व |
