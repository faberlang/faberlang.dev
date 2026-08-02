+++
translation_kind = "translated"

title = "Types and values"
section = "language"
order = 2
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
  "radix/README.md (Runtime binding vs structural definition, Language Orientation)",
  "examples/corpus/fixum/",
  "examples/corpus/sit/",
  "radix/README.md (Tensors And Sparsa)",
  "radix/docs/design/tabula-intrinsics.md",
  "examples/corpus/tabula/",
  "examples/corpus/sparsa/",
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "examples/corpus/literalia/",
  "examples/corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
  "radix/README.md (Nullability and Optionality)",
  "examples/corpus/nihil/",
  "examples/corpus/sponte/",
  "examples/corpus/nonnihil/",
  "radix/README.md (Conversion and Construction)",
  "radix/docs/design/conversio-valor.md",
  "radix/docs/design/failable-conversio.md",
]
+++

## Data types

Faber में एक स्थिर, प्रकार-प्रथम प्रकार-प्रणाली है। हर घोषणा में नाम से पहले प्रकार आता है: `textus nomen`, न कि `nomen: textus`। प्रकार-प्रणाली में स्केलर प्रिमिटिव, जेनरिक संग्रह, निर्धारित-आकार वाली संख्याएँ, टेंसर और GPU-संबंधी रजिस्टर प्रकार शामिल हैं।

### प्रिमिटिव प्रकार {#primitive-types}

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

### निर्धारित-आकार वाले संख्यात्मक प्रकार {#sized-numeric-types}

`numerus` और `fractus` की डिफ़ॉल्ट चौड़ाइयाँ (i64 और f64) होती हैं और इनके लिए स्पष्ट चौड़ाई वाले रूप भी उपलब्ध हैं:

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

प्रकार की स्थिति में चौड़ाई-संक्षेप उपलब्ध है: `i8` … `u64`, `f16`, `f32`, `f64`, `numerus<W>` / `fractus<W>` के समतुल्य हैं।

### Nullable प्रकार {#nullable-types}

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

### प्रकार उपनाम {#type-aliases}

```faber
typus UserId = numerus
```

### जेनरिक {#generics}

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

### संग्रह {#collections}

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

### टेंसर प्रकार {#tensor-types}

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

### GPU कोर प्रकार {#gpu-core-types}

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

### प्रकारों पर borrow मार्कर {#borrow-markers}

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

### तुलना नीति {#comparison-policy}

| ऑपरेटर | परिवार | व्यवहार |
|----------|--------|-----------|
| `≡`, `≠` | सटीक समानता | समान प्रकार आवश्यक; `nihil` को अपवाद |
| `≈`, `≉` | संख्यात्मक मान समानता | केवल संख्यात्मक लैटिस |
| `<`, `≤`, `>`, `≥` | क्रम निर्धारण | संख्यात्मक, instant, स्केलर टेक्स्ट |
| `intra` | रेंज समावेशन | रेंज में संख्यात्मक मान |
| `inter` | संग्रह सदस्यता | संग्रह में तत्व |

## Variables and binding

Faber में तीन variable keywords और assignment के लिए एक विशेष glyph है। मुख्य अंतर `fixum` (केवल एक बार लिखने योग्य) और `varia` (स्वतंत्र रूप से फिर से assign करने योग्य) के बीच है, तथा `←` (runtime flow) और `=` (संरचनात्मक field shape) के बीच है।

### fixum — अपरिवर्तनीय binding {#fixum-immutable-binding}

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

### varia — परिवर्तनशील binding {#varia-mutable-binding}

`varia` bindings को स्वतंत्र रूप से फिर से assign किया जा सकता है:

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

### sit — inferred immutable sugar {#sit-inferred-immutable-sugar}

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

### Runtime binding बनाम structural definition {#runtime-binding-vs-structural-definition}

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

### ex से field extraction {#ex-field-extraction}

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

### Postfix increment और decrement {#postfix-increment-and-decrement}

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

## Collections

Faber में कंपाइलर द्वारा स्वामित्व वाले कई कलेक्शन प्रकार हैं। इनके कैनोनिकल तरीके स्टैंडर्ड लाइब्रेरी में नहीं, बल्कि कंपाइलर में परिभाषित होते हैं।

### Lista — क्रमबद्ध डायनेमिक कलेक्शन {#lista}

```faber
fixum lista<numerus> empty ← vacua
fixum _ numbers ← [1, 2, 3, 4, 5]
fixum _ names ← ["Marcus", "Julia", "Gaius"]
fixum _ nested ← [[1, 2], [3, 4]]
```

`sparge` के साथ स्प्रेड करें:

```faber
fixum _ a ← [1, 2, 3]
fixum _ b ← [4, 5, 6]
fixum _ combined ← [sparge a, sparge b]
fixum _ headed ← [0, sparge a, 99]
```

मुख्य तरीके: `longitudo`, `accipe`, `appende`, `summa`, `primus`, `novissimus`।

### Tabula — कुंजी-मान मैप {#tabula}

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

### Tensor — घना निश्चित-आकार बफ़र {#tensor}

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

Tensor शुगर (संख्यात्मक कोड के लिए):

```faber
fixum tf32[] seed ← vacua
fixum tf32[4] lanes ← seed.strue([1.0, 2.0, 3.0, 4.0], [4])
```

मुख्य तरीके: `forma`, `accipe`, `ponde`, `crea`, `structa`, `strue`, साथ ही
तत्व-स्तरीय अंकगणित, मैट्रिक्स गुणन (`multiplicatio`) और
रिडक्शन (`summa`, `productum`)।

### Sparsa — विरल निश्चित-आकार बफ़र {#sparsa}

```faber
fixum sparsa<fractus<f32>, [2, 3]> sparse ← vacua
sparse.ponde([0, 1], 4.0)
sparse.ponde([1, 2], 9.0)

# accipe returns the stored value, here 4.0
nota sparse.accipe([0, 1])
# count of stored entries
nota sparse.nonnihil()
```

घने और विरल रूपों के बीच रूपांतरण:

```faber
fixum tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
fixum sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
fixum tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
```

### Cursors — लेज़ी स्ट्रीम {#cursors}

`cursor<T>` एक लेज़ी स्ट्रीम प्रकार है। इसे कलेक्शन इटरेटर, `tuus` व्यू या जनरेटर फ़ंक्शन से बनाया जाता है। इसका उपभोग `itera ex` के माध्यम से किया जाता है:

```faber
fixum _ items ← [1, 2, 3]
itera ex items fixum item {
    nota item
}
```

### Intervallum — रेंज {#intervallum}

```faber
# exclusive range: 0, 1, 2, 3, 4
itera ab 0‥5 fixum i {
    nota i
}
# inclusive range: 0, 1, 2, 3, 4, 5
itera ab 0…5 fixum i {
    nota i
}
```

`‥` एक्सक्लूसिव रेंज एंडपॉइंट है; `…` इनक्लूसिव है।

## String and template literals

Faber में सीमाचिह्नों के अर्थ निश्चित होते हैं — हर उद्धरण-रूप स्रोत की अलग संरचना दर्शाता है। ये एक-दूसरे के पर्याय नहीं हैं।

### शाब्दिक रूप {#literal-forms}

| रूप | प्रकार | भूमिका |
|------|------|------|
| `'…'` | `ascii` | स्थिर मशीन टोकन; इसमें `§` नहीं होता और `(…)` का उपयोग नहीं होता |
| `"…"` | `textus` | छोटी Unicode पंक्ति-स्ट्रिंग; `(…)` का रेंडर होता है |
| `«…»` | `textus` | ब्लॉक/बहुपंक्ति Unicode; `(…)` का रेंडर होता है |
| `` `…` `` | `forma` | कैप्चर किए गए टेम्पलेट; `(…)` कैप्चर करता है |
| `{ … }` | `json` | संकलन-समय JSON दस्तावेज़ |
| `|…|` | `octeti` | संकलन-समय हेक्स बाइट्स |
| `[ … ]` | `lista<T>` | Faber सूची लिटरल |

### स्ट्रिंग-टेम्पलेट अनुप्रयोग {#string-template-application}

Faber स्ट्रिंग-टेम्पलेट अनुप्रयोग से पाठ को फ़ॉर्मैट करता है: पहले `"…"` या `«…»` लिटरल में `§` रिक्त-स्थान होते हैं, फिर कोष्ठक में तर्क दिए जाते हैं:

```faber
functio greet(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}

fixum numerus pagina ← 3
fixum numerus totum ← 10
fixum textus code ← "200"
fixum textus label ← "OK"

fixum _ msg ← "Page § of §"(pagina, totum)
fixum _ block ← «status: § (§)»(code, label)
```

मुख्य नियम:

- `§` (U+00A7) टेम्पलेट रिक्त-स्थान है
- स्थितीय रिक्त-स्थान: स्पष्ट क्रम के लिए `§0`, `§1`, … का उपयोग करें
- अंतिम `!` प्रदर्शन फ़ॉर्मैटिंग चुनता है: `"Salve, §!"(nomen)`
- `(args)` प्रत्यय टेम्पलेट अनुप्रयोग है, फ़ंक्शन कॉल नहीं

### ब्लॉक स्ट्रिंग {#block-strings}

बहुपंक्ति ब्लॉक गिलेमे `«…»` का उपयोग करते हैं:

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

### कैप्चर किए गए टेम्पलेट (`forma`) {#captured-templates}

बैकटिक टेम्पलेट पाठ और पैरामीटर को रेंडर किए बिना कैप्चर करते हैं।
बाउंड SQL/URL पेलोड के लिए ये सुरक्षित हैं:

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

### इनलाइन JSON {#inline-json}

सादा `{ … }` इनलाइन JSON है: यह संकलन-समय का `json` दस्तावेज़ है, अनाम Faber ऑब्जेक्ट नहीं। कुंजियाँ उद्धृत स्ट्रिंग होती हैं और `:` से अलग की जाती हैं:

```faber
fixum _ empty ← {}
fixum _ user ← { "name": "Marcus", "age": 30, "active": true }
fixum _ nested ← { "meta": { "version": 1 }, "tags": ["alpha", "beta"] }
```

टाइप किए गए `genus` निर्माण के लिए, प्रकार का नाम और `=` फ़ील्ड संरचना का उपयोग करें:

```faber
genus Point {
    numerus x
    numerus y
}
fixum _ p ← Point { x = 10, y = 20 }
```

## Nullability and optionality

Faber किसी मान में अनुपस्थिति और घोषणा स्थल पर वैकल्पिक प्रावधान के बीच भेद करता है।

### नलनीय मान — T ∪ nihil {#nullable-values}

जब मान अनुपस्थित हो सकता है, तब `T ∪ nihil` का उपयोग करें:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

### वैकल्पिक घोषणा स्लॉट — sponte {#optional-declaration-slots}

जब कोई पैरामीटर या फ़ील्ड कॉलर या कंस्ट्रक्टर द्वारा छोड़ा जा सकता हो, तब नाम के बाद `sponte` का उपयोग करें:

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    textus email sponte
}
```

उधार-चिह्न वैकल्पिक पैरामीटरों के साथ संयोजित किए जा सकते हैं:

```faber
functio process(de numerus depth sponte) → vacuum { }
```

### नल-रहित अभिकथन — ! {#non-null-assertion}

किसी नलनीय मान के `nihil` न होने का अभिकथन करने के लिए `!.`, `![`, `!(` का उपयोग करें:

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

`nihil` पर नल-रहित अभिकथन रनटाइम पर प्रोग्राम को रोक देता है।

### नलिश सहसंयोजन — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

### ignotum {#ignotum}

`ignotum` एस्केप हैच और अधूरी जानकारी के लिए शीर्ष-स्तरीय अज्ञात प्रकार है। यह नलनीयता की कोई व्यवस्था नहीं है।

## Conversion and construction

रनटाइम और कंपाइल-टाइम के लिए दो महत्वपूर्ण रूपांतरण ऑपरेटर:

```faber
# runtime conversion
fixum _ parsed ← "42" ↦ numerus
# static ascription
fixum numerus value ← 7
fixum _ text ← value ∷ textus
```

### रनटाइम रूपांतरण — ↦ {#runtime-conversion}

रनटाइम रूपांतरण के लिए `↦` का उपयोग करें, विशेष रूप से ऐसी पार्सिंग या कोअर्शन के लिए जो विफल हो सकती है। `⇥` के साथ इनलाइन रिकवरी दें:

```faber
fixum textus input ← "9"
fixum _ n ← "42" ↦ numerus
fixum _ safe ← input ↦ numerus ⇥ 0
```

टाइप-निर्देशित मटेरियलाइज़ेशन:

```faber
fixum textus path ← "/etc/hosts"
fixum _ lanes ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
fixum _ body ← ad 'solum:lege' (path) ↦ textus
```

### स्थिर प्रकार-निर्देशन — ∷ {#static-ascription}

स्पष्ट स्थिर प्रकार-निर्देशन के लिए `∷` का उपयोग करें। यह पोस्टफ़िक्स होता है और लक्ष्य-प्रकार द्वारा निर्देशित होता है:

```faber
fixum numerus value ← 7
fixum _ x ← 7 ∷ numerus<i32>
fixum _ text ← value ∷ textus
```

### नलिश कोअलेसिंग — vel {#nullish-coalescing}

जब कोई मान `nihil` हो, तब नलिश कोअलेसिंग के लिए `vel` का उपयोग करें:

```faber
fixum textus ∪ nihil provided_name ← nihil
fixum _ name ← provided_name vel "default"
```
