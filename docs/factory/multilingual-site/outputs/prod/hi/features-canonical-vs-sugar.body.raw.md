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

## Numeric type sugar {#numeric-type-sugar}

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

<<<FENCE 0>>>

**Numeric modules (sugar को प्राथमिकता दें):**

<<<FENCE 1>>>

Sugar केवल **type-position** में मान्य है। `f32`, `tf32`, या `mf32` नाम वाले
value identifiers अपरिवर्तित रहते हैं — compiler इन्हें केवल type positions
में आने पर sugar के रूप में समझता है। जो file लगातार sugar का उपयोग करती है,
उसे शीर्ष पर एक बार यह बात बतानी चाहिए:

<<<FENCE 2>>>

## Annotation sugar {#annotation-sugar}

Faber annotations भी numeric types की तरह dual-surface model का पालन करते हैं।
Annotations, declarations से जुड़ा compiler-owned metadata हैं — जैसे CLI option
definitions के लिए `@ optio` या async functions के लिए `@ futura`।

**Canonical form:** स्पष्ट field names वाला braced record:

<<<FENCE 3>>>

**Sugar form:** positional arguments और named aliases:

<<<FENCE 4>>>

दोनों forms एक ही `HirAnnotation` record बनाते हैं। Canonical form स्पष्ट और
self-documenting है; sugar form उन annotations के लिए संक्षिप्त है जिनका अक्सर
उपयोग होता है और जिनके field order को अच्छी तरह जाना जाता है।
`faber format --canonical` braced records को प्राथमिकता देता है; author mode
लेखक द्वारा चुना गया form सुरक्षित रखता है।

## Author vs canonical formatting {#author-vs-canonical-formatting}

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

## Design principle {#design-principle}

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

## References {#references}

1. `radix/docs/design/numeric-type-sugar.md` — पूर्ण sugar families, spelling preferences
2. `radix/docs/design/annotation-sugar.md` — dual-surface annotation model
3. `radix/docs/design/faber-canonical-surface.md` — author बनाम canonical format policy
4. `radix/EBNF.md` — sugar forms के grammar tables
