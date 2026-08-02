+++
translation_kind = "translated"

title = "Glyphs and Latin"
section = "language"
order = 5
sources = [
  "radix/README.md (Glyphs and Words)",
  "examples/corpus/operatores/",
  "examples/corpus/assignatio/",
  "radix/EBNF.md",
]
+++

## Glyphs and operators

Faber ऐसे ग्लिफ़ का उपयोग करता है जिनमें प्रतीक संरचनात्मक भूमिका निभाता है। नीचे लेक्सर द्वारा पहचाने जाने वाले स्रोत ग्लिफ़ का पूरा संग्रह दिया गया है।

### मान प्रवाह {#value-flow}

| ग्लिफ़ | अर्थ |
|-------|---------|
| `←` | रनटाइम बाइंडिंग, पुनर्निर्धारण और म्यूटेशन |
| `→` | फ़ंक्शन का रिटर्न प्रकार |
| `⇥` | वैकल्पिक निकास — त्रुटि-चैनल प्रकार या इनलाइन रूपांतरण पुनर्प्राप्ति |
| `∴` | समापन संधि — क्लोज़र बॉडी को उसके सिग्नेचर से जोड़ती है (`(a, b) → T ∴ a + b`) |

### प्रकार का आकार {#type-shape}

| ग्लिफ़ | अर्थ |
|-------|---------|
| `∷` | स्थिर प्रकार अभिलेखन (कम्पाइल-टाइम कास्ट) |
| `↦` | रनटाइम रूपांतरण (विफल हो सकने वाला पार्स/कोअर्स) |
| `∪` | इनलाइन यूनियन प्रकार (`T ∪ nihil`) |

### तुलना {#comparison}

| ग्लिफ़ | अर्थ |
|-------|---------|
| `≡` `≠` | सटीक समानता और असमानता |
| `<` `>` `≤` `≥` | क्रम तुलना |
| `≈` `≉` | संख्यात्मक मान की समानता |

### तार्किक और बिटवाइज़ {#logical-and-bitwise}

| ग्लिफ़ | अर्थ |
|-------|---------|
| `∧` `∨` `⊻` `¬` | और, या, एक्सओआर, नहीं |
| `⇐` `⇒` | बाएँ और दाएँ बिट शिफ़्ट |

### असाइनमेंट अपडेट {#assignment-updates}

| ग्लिफ़ | अर्थ |
|-------|---------|
| `←` | अभिव्यक्तियों में एकमात्र असाइनमेंट ऑपरेटर |
| `⊕` `⊖` | पोस्टफ़िक्स वृद्धि/कमी स्टेटमेंट (केवल म्यूटेबल `numerus`) |

### वैकल्पिक चेनिंग और नॉन-नल अभिकथन {#optional-chaining-and-non-null-assertion}

| ग्लिफ़ | अर्थ |
|-------|---------|
| `?` `?.` `?[` `?(` | वैकल्पिक चेनिंग |
| `!` `!.` `![` `!(` | नॉन-नल अभिकथन |

### रेंज {#ranges}

| ग्लिफ़ | अर्थ |
|-------|---------|
| `‥` | एक्सक्लूसिव रेंज एंडपॉइंट |
| `…` | इन्क्लूसिव रेंज एंडपॉइंट |

### लिटरल सीमांकक {#literal-delimiters}

| ग्लिफ़ | प्रकार | भूमिका |
|-------|------|------|
| `'` | `ascii` | स्थिर मशीन टोकन |
| `"` | `textus` | पंक्ति स्ट्रिंग |
| `«` `»` | `textus` | ब्लॉक स्ट्रिंग (गिलमेट) |
| `` ` `` | `forma` | कैप्चर किया गया टेम्पलेट |
| `|` | `octeti` | हेक्स लिटरल |
| `§` | टेम्पलेट होल | `"…"`, `«…»`, `` `…` `` के भीतर प्लेसहोल्डर |

### विराम-चिह्न {#punctuation}

| ग्लिफ़ | भूमिका |
|-------|------|
| `(` `)` | समूह और कॉल |
| `{` `}` | ब्लॉक, जीनस लिटरल या JSON दस्तावेज़ |
| `[` `]` | सूची लिटरल और इंडेक्सिंग |
| `.` | सदस्य अभिगम |
| `,` | विभाजक |
| `;` | स्टेटमेंट विभाजक |
| `:` | JSON फ़ील्ड विभाजक |
| `=` | संरचनात्मक फ़ील्ड आकार (रनटाइम असाइनमेंट नहीं) |
| `@` | एनोटेशन मार्कर |
| `#` | पंक्ति टिप्पणी |

## Latin vocabulary and structural glyphs

*तीन संकेत-चयन, जिनसे Faber स्रोत को एक नज़र में पहचाना जा सकता है।*

Faber तीन ऐसे जानबूझकर चुने गए संकेतों का उपयोग करता है, जो मिलकर एक स्थिर व्याकरणिक आकार वाला स्रोत तैयार करते हैं। पाठक यह समझ सकता है कि हर रचना की अर्थगत भूमिका क्या है, भले ही उसे अभी यह न पता हो कि कोड किस लक्ष्य बैकएंड के लिए संकलित होगा।

### तीन संकेत {#three}

| संकेत | उदाहरण | भूमिका |
|--------|----------|------|
| प्रकार-प्रथम घोषणाएँ | `textus nomen`, `numerus aetas` | आकार बाइंडिंग की ओर पढ़ता है — पहले प्रकार, फिर नाम। |
| लैटिन व्यवहारिक शब्द | `functio`, `genus`, `si`, `redde`, `fixum` | घोषणाएँ, कथन, जीवनचक्र और व्यवहारिक आशय। |
| संरचनात्मक ग्लिफ़ | `← → ∴ ≡ ∪ ⇥` | मान-प्रवाह, प्रकार-प्रवाह और संरचनात्मक जोड़ — सार्वभौमिक, कभी स्थानीयकृत नहीं। |

इन तीनों को एक-दूसरे को मजबूत करने के लिए बनाया गया है। जो पाठक किसी एक locale में Faber जानता है, वह इसे किसी भी locale में पढ़ सकता है, क्योंकि ग्लिफ़ और संरचना कभी नहीं बदलते। जो पाठक Rust बैकएंड जानता है, वह भी Faber स्रोत को पहचान सकता है, क्योंकि लैटिन कीवर्ड और प्रकार-प्रथम क्रम एक विशिष्ट दृश्य रूप बनाते हैं।

### प्रकार-प्रथम घोषणाएँ {#type-first}

Faber हर घोषणा में नाम से पहले प्रकार रखता है। यह मुख्यधारा के C-परिवार के सिंटैक्स के विपरीत है, और यह जानबूझकर किया गया है:

| रचना | C-परिवार की परंपरा | Faber |
|-----------|----------------|-------|
| चर | `int count = 0` | `numerus count ← 0` |
| फ़ंक्शन | `fn greet(name: String) → String` | `functio salve(textus nomen) → textus` |
| पैरामीटर | `(String name)` | `(textus nomen)` |

प्रकार-प्रथम घोषणाओं में डेटा का आकार सबसे पहले दिखाई देता है। यह उन भाषाओं के साथ स्वाभाविक रूप से मेल खाता है, जो अर्थगत विस्तार के लिए बाएँ से दाएँ पढ़ी जाती हैं — चीनी, हिंदी और अरबी घोषणाएँ भी यही क्रम अपनाती हैं।

```faber
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

### लैटिन व्यवहारिक शब्दावली {#latin}

Faber हर उस रचना के लिए लैटिन शब्दों का उपयोग करता है, जिसमें व्यवहारिक या व्याकरणिक आकार होता है। यह शब्दावली छोटी और नियमित है। यह अधिकांश प्रोग्रामिंग भाषाओं की मिश्रित व्युत्पत्तियों के बजाय एक ही शास्त्रीय स्रोत से ली गई है।

#### घोषणाएँ {#declarations}

| कीवर्ड | भूमिका | लगभग समतुल्य |
|---------|------|------------------------|
| `functio` | नामित फ़ंक्शन या मेथड घोषित करता है | `fn`, `def`, `function` |
| `genus` | फ़ील्ड वाले ठोस प्रकार को घोषित करता है | `class`, `struct` |
| `implendum` | व्यवहारिक अनुबंध घोषित करता है | `interface`, `trait` |
| `typus` | प्रकार उपनाम घोषित करता है | `typedef`, `type` |
| `discretio` | टैग किए गए यूनियन को घोषित करता है | `enum`, `sum type` |

#### बाइंडिंग और स्थानांतरण {#bindings-and-transfer}

| कीवर्ड | भूमिका | लगभग समतुल्य |
|---------|------|------------------------|
| `fixum` | अपरिवर्तनीय बाइंडिंग (एक बार लिखें) | `let`, `const` |
| `varia` | परिवर्तनीय बाइंडिंग | `let mut`, `var` |
| `sit` | संक्षिप्त, अनुमानित अपरिवर्तनीय बाइंडिंग | `let` (अनुमानित) |
| `redde` | फ़ंक्शन से कोई मान लौटाता है | `return` |
| `iace` | त्रुटि चैनल पर अपवाद फेंकता है | `throw`, `raise` |
| `mori` | स्थगित — व्यवहार अभी अभिव्यक्त करने योग्य नहीं है | `unimplemented!`, `todo` |

#### नियंत्रण प्रवाह {#control-flow}

| कीवर्ड | भूमिका | लगभग समतुल्य |
|---------|------|------------------------|
| `si` | सशर्त शाखा | `if` |
| `sin` | अन्यथा-यदि शाखा | `else if` |
| `secus` | अन्यथा शाखा | `else` |
| `dum` | जब तक लूप | `while` |
| `itera` | पुनरावृत्ति (मान, कुंजी या रेंज) | `for` |
| `elige` | पैटर्न-मिलान (पहली सफल शाखा चुनी जाती है) | `match`, `switch` |
| `fac` | त्रुटि-पुनर्प्राप्ति वाला प्रयास ब्लॉक | `try`, `do` |
| `cape` | `fac` के लिए त्रुटि हैंडलर | `catch` |

> लैटिन शब्दावली **बाइंड करने योग्य** है — यह कैनोनिकल पैक के साथ आती है, लेकिन reader locale के माध्यम से इसे फिर से मैप किया जा सकता है। थाई प्रोग्रामर को `si` के स्थान पर `ถ้า` दिखाई देता है; चीनी प्रोग्रामर को `functio` के स्थान पर `函数` दिखाई देता है। शब्दावली को विशेषाधिकार प्राप्त नहीं है; केवल व्याकरण स्थिर रहता है।

### संरचनात्मक ग्लिफ़ {#glyphs}

जहाँ व्यवहारिक शब्दावली लैटिन शब्दों का उपयोग करती है, वहीं संरचनात्मक अर्थ सार्वभौमिक ग्लिफ़ का उपयोग करता है। ये कभी स्थानीयकृत नहीं होते और अलग-अलग रेंडरिंग में इनका अर्थ कभी नहीं बदलता। यही दृश्य आधार है, जो Faber स्रोत को पहचानने योग्य बनाता है, चाहे कीवर्ड किसी भी मानव भाषा में रेंडर किए गए हों।

#### मान-प्रवाह {#value-flow}

| ग्लिफ़ | अर्थ |
|-------|---------|
| `←` | रनटाइम बाइंडिंग, पुनर्बाइंडिंग और म्यूटेशन — एकमात्र असाइनमेंट ऑपरेटर |
| `→` | फ़ंक्शन के रिटर्न प्रकार की घोषणा |
| `⇥` | वैकल्पिक निकास: त्रुटि-चैनल प्रकार या इनलाइन रूपांतरण पुनर्प्राप्ति |
| `∴` | समापन संधि — क्लोज़र बॉडी को उसके सिग्नेचर से जोड़ती है |

#### प्रकार का आकार {#type-shape}

| ग्लिफ़ | अर्थ |
|-------|---------|
| `∷` | स्थिर प्रकार-निर्देशन — किसी मान के प्रकार के बारे में संकलन-समय का दावा |
| `↦` | रनटाइम रूपांतरण — ऐसा पार्सिंग या कोअर्शन, जो विफल हो सकता है |
| `∪` | इनलाइन यूनियन प्रकार — दो प्रकारों को जोड़ता है (जैसे `T ∪ nihil`) |

#### तुलना और तर्क {#comparison-and-logic}

| ग्लिफ़ | अर्थ |
|-------|---------|
| `≡` `≠` | सटीक समानता और असमानता — सख्त प्रकार-मिलान आवश्यक |
| `<` `>` `≤` `≥` | क्रम-संबंधी तुलनाएँ |
| `∧` `∨` `⊻` `¬` | तार्किक और बिटवाइज़: और, या, XOR, नहीं |

#### बाइंडिंग परंपरा महत्वपूर्ण है {#the-binding-convention-matters}

एक ग्लिफ़-चयन पर विशेष ध्यान देना चाहिए, क्योंकि नए पाठकों के लिए भ्रम का यह सबसे सामान्य बिंदु है:

| ग्लिफ़ | भूमिका | उपयोग |
|-------|------|---------|
| `←` | **रनटाइम प्रवाह** | प्रारंभिक बाइंडिंग, पुनर्बाइंडिंग और निष्पादन-समय का म्यूटेशन |
| `=` | **संरचनात्मक आकार** | लिटरल के भीतर फ़ील्ड नाम और घोषणा मेटाडेटा — रनटाइम स्टोर के लिए नहीं |

अधिकांश भाषाएँ `=` को "इस प्रकार में यह फ़ील्ड परिभाषित करें" और "इस चर में रनटाइम मान रखें" — दोनों के लिए ओवरलोड करती हैं। Faber इन दोनों कार्यों को अलग करता है। हर `←` सक्रिय डेटा-प्रवाह है; हर `Type { … }` के भीतर का `=` जीनस फ़ील्ड लेआउट है।

```text
# Runtime binding: ← attaches a value to a name
fixum numerus count ← 0
varia textus label ← "ready"
count ← count + 1

# Structural shape: = defines field values inside a literal
fixum _ p ← Point {
    x = 10,
    y = 20
}
```

### मुख्यधारा की भाषाओं की तुलना में {#compare}

नीचे दी गई तालिका दिखाती है कि प्रोग्रामिंग भाषाओं के सामान्य पैटर्न Faber की तीन-संकेत प्रणाली में कैसे मैप होते हैं। Faber कॉलम हर अलग अर्थगत कार्य के लिए अलग ग्लिफ़ या कीवर्ड का उपयोग करता है — कोई ओवरलोडिंग नहीं।

| अर्थगत कार्य | अन्य भाषाओं में सामान्य | Faber |
|--------------|---------------------------|-------|
| पैरामीटर प्रकार की घोषणा | `name: String` | `textus nomen` |
| रिटर्न प्रकार | `→ String`, `: String` | `→` `textus` |
| रनटाइम असाइनमेंट | `x = value` | `←` |
| समानता परीक्षण | `==` | `≡` |
| नल-योग्यता | `T?`, `Option<T>` | `T ∪ nihil` |
| शाखा + एक कथन | `if (cond) return x` | `si cond ergo redde x` |
| प्रकार कास्ट | `(T)value`, `value as T` | `value ∷ T` |
| रूपांतरण (विफल हो सकता है) | `try_into()` | `value ↦ T` |

### संदर्भ {#references}

1. EBNF व्याकरण — ग्लिफ़ और कीवर्ड की पूरी सूची
2. examples/corpus/ — सभी कीवर्ड वाली 292 उदाहरण फ़ाइलों का भाषा कॉर्पस
3. examples/corpus/operatores/ — ऑपरेटर और ग्लिफ़ के उदाहरण
4. Commandments — इन संकेतों को सुरक्षित रखने वाले डिज़ाइन के नौ नियम

## Canonical vs sugar surfaces

*एक ही अर्थ-रूप वाली अनेक पार्स की जा सकने वाली सतहें।*

Faber के डिज़ाइन में एक पैटर्न बार-बार दिखाई देता है: भाषा हर construct के
लिए **एक canonical spelling** निर्धारित करती है, लेकिन कई **sugar spellings**
स्वीकार करती है जो अर्थ की दृष्टि से समान होती हैं। Compiler इनमें से किसी एक
को प्राथमिकता नहीं देता — दोनों एक ही AST node में parse होते हैं। Formatter
संदर्भ और mode के आधार पर यह तय करता है कि कौन-सी spelling emit करनी है।

> **नियम:** Sugar spellings, long form के अर्थ की दृष्टि से समान होती हैं।
> कई सतहें एक ही `HirAnnotation` या type node में parse होती हैं।
> `faber format --canonical` canonical spellings को प्राथमिकता देता है;
> author mode लेखक द्वारा लिखी गई sugar को सुरक्षित रखता है।

### संख्यात्मक प्रकार शुगर {#numeric-type-sugar}

Numeric types के canonical spellings long form में होते हैं और इनके compact
sugar forms भी होते हैं। यह चुनाव repository-स्तर पर नहीं, module-स्तर पर होता
है — कोई CLI package हर जगह long form का उपयोग कर सकता है, जबकि कोई tensor
kernel module sugar का उपयोग कर सकता है:

| Sugar | Canonical form | Domain |
|-------|----------------|--------|
| `f32`, `f64`, `i32`, `u64` | `fractus<f32>`, `numerus<i32>` | Width markers — scalar numeric types |
| `tf32`, `tf32[4]`, `ti64[2, 3]` | `tensor<f32, _>`, `tensor<f32, [4]>` | Dense tensor — `t` + width + optional shape |
| `sf32`, `sf32[2, 3]`, `si64[N]` | `sparsa<f32, _>`, `sparsa<f32, [2, 3]>` | Sparse tensor — `s` + width + optional shape |
| `mf32[4, 4]`, `mu32[3, 3]` | `matrix<f32, [4, 4]>` | Register-class matrix — `m` + width + shape |
| `lf32`, `lu32`, `li64` | `lista<f32>`, `lista<u32>` | List — `l` + width |
| `f16` | `fractus<f16>` | Half-float width marker (semantic/layout only) |

**सामान्य Faber (long form को प्राथमिकता दें):**

```faber
fixum lista<f32> values ← vacua
fixum tensor<f32, [2, 3]> grid ← vacua
fixum numerus<i32> narrow ← 7
```

**Numeric modules (sugar को प्राथमिकता दें):**

```faber
fixum lf32 values ← vacua
fixum tf32[2, 3] grid ← vacua
fixum i32 narrow ← 7
```

Sugar केवल **type-position** में मान्य है। `f32`, `tf32`, या `mf32` नाम वाले
value identifiers अपरिवर्तित रहते हैं — compiler इन्हें केवल type positions
में आने पर sugar के रूप में समझता है। जो file लगातार sugar का उपयोग करती है,
उसे शीर्ष पर एक बार यह बात बतानी चाहिए:

```faber
# STYLE: numeric sugar (tf32, mf32, sf32, lf32, lu32)
```

### एनोटेशन शुगर {#annotation-sugar}

Faber annotations भी numeric types की तरह dual-surface model का पालन करते हैं।
Annotations, declarations से जुड़ा compiler-owned metadata हैं — जैसे CLI option
definitions के लिए `@ optio` या async functions के लिए `@ futura`।

**Canonical form:** स्पष्ट field names वाला braced record:

```text
@ optio {
    binding = verbose,
    brevis = "v",
    longum = "verbose",
    typus = bivalens,
    ubique = verum,
    descriptio = "Enable verbose output"
}
```

**Sugar form:** positional arguments और named aliases:

```text
@ optio verbose brevis "v" longum "verbose" typus bivalens ubique descriptio "Enable verbose output"
```

दोनों forms एक ही `HirAnnotation` record बनाते हैं। Canonical form स्पष्ट और
self-documenting है; sugar form उन annotations के लिए संक्षिप्त है जिनका अक्सर
उपयोग होता है और जिनके field order को अच्छी तरह जाना जाता है।
`faber format --canonical` braced records को प्राथमिकता देता है; author mode
लेखक द्वारा चुना गया form सुरक्षित रखता है।

### लेखक बनाम कैनोनिकल फ़ॉर्मैटिंग {#author-vs-canonical-formatting}

`faber format` command दो modes में काम करता है, जो canonical-vs-sugar
principle को प्रतिबिंबित करते हैं:

| Mode | Command | Input | Output |
|------|---------|-------|--------|
| Author | `faber format` | Parsed AST + leading trivia | Faber source, जिसमें `#` comments, blank lines और sugar spellings सुरक्षित रहती हैं |
| Canonical | `faber format --canonical` | Analysed HIR + `TypeTable` | Normalised Faber — कोई comments नहीं, canonical spellings, कोई sugar नहीं |

दोनों modes compiler के पूरे front half से गुजरते हैं (canonical के लिए lex,
parse और analyse)। Invalid source compiler diagnostics उत्पन्न करता है —
formatter broken input को चुपचाप format नहीं करता।

दोनों modes के लिए मुख्य नियम:

- चार-space indentation
- Stroustrup braces: opening `{`, controlling header वाली उसी line पर होता है
- Author mode blank lines की *उपस्थिति* सुरक्षित रखता है, लेकिन एक से अधिक लगातार blank lines को समेट देता है
- Author mode ऐसी blank lines नहीं जोड़ता जो source में मौजूद नहीं थीं
- Canonical mode type spellings को long form में, tensor sugar को canonical रूप में और annotations को braced records में normalise करता है
- Canonical mode nullable unions के लिए `T ∪ nihil` और optional parameters के लिए `sponte` emit करता है

### डिज़ाइन सिद्धांत {#design-principle}

Canonical-vs-sugar pattern कई स्थानों पर दिखाई देता है क्योंकि यह एक
जानबूझकर अपनाया गया design principle है, न कि अलग-अलग सुविधाओं का संग्रह:

| Domain | Canonical | Sugar |
|--------|-----------|-------|
| Numeric types | `numerus<i32>` | `i32` |
| Tensor types | `tensor<f32, [4]>` | `tf32[4]` |
| Annotations | `@ optio { binding = verbose }` | `@ optio verbose ...` |
| Formatting | `faber format --canonical` | `faber format` (author mode) |
| Reader locale | Latin (`la`) | कोई भी locale pack |

यह pattern दो उद्देश्यों की पूर्ति करता है। पहला, यह प्रवेश की बाधा कम करता है —
नए users `tensor<fractus<f32>, [4]>` लिखे बिना `tf32[4]` लिख सकते हैं। दूसरा,
यह canonical language को अस्पष्ट नहीं होने देता — जब precision महत्वपूर्ण हो,
तो long form ठीक-ठीक बताता है कि उसका अर्थ क्या है। Formatter दोनों के बीच
पुल का काम करता है: authors sugar लिखते हैं, reviewers canonical की मांग कर
सकते हैं, और CI किसी भी रूप को लागू कर सकता है।

### संदर्भ {#references}

1. `radix/docs/design/numeric-type-sugar.md` — पूर्ण sugar families, spelling preferences
2. `radix/docs/design/annotation-sugar.md` — dual-surface annotation model
3. `radix/docs/design/faber-canonical-surface.md` — author बनाम canonical format policy
4. `radix/EBNF.md` — sugar forms के grammar tables
