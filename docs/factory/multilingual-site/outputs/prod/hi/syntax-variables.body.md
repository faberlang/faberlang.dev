Faber में तीन variable keywords और assignment के लिए एक विशेष glyph है। मुख्य अंतर `fixum` (केवल एक बार लिखने योग्य) और `varia` (स्वतंत्र रूप से फिर से assign करने योग्य) के बीच है, तथा `←` (runtime flow) और `=` (संरचनात्मक field shape) के बीच है।

## fixum — अपरिवर्तनीय binding {#fixum-immutable-binding}

`fixum` bindings केवल एक बार लिखी जा सकती हैं। इन्हें initializer के साथ या उसके बिना declare किया जा सकता है। यदि initializer के बिना declare किया गया हो, तो पढ़ने से पहले इन्हें ठीक एक बार assign करना आवश्यक है। दूसरी assignment अस्वीकार कर दी जाती है।

<<<FENCE 0>>>

Deferred initialisation:

<<<FENCE 1>>>

## varia — परिवर्तनशील binding {#varia-mutable-binding}

`varia` bindings को स्वतंत्र रूप से फिर से assign किया जा सकता है:

<<<FENCE 2>>>

## sit — inferred immutable sugar {#sit-inferred-immutable-sugar}

`sit`, `fixum _` का sugar है — inferred type वाली अपरिवर्तनीय binding:

<<<FENCE 3>>>

## Runtime binding बनाम structural definition {#runtime-binding-vs-structural-definition}

Faber उस `=` को दो अलग भूमिकाओं में बाँटता है, जिसे अधिकांश भाषाएँ एक ही रूप में समेट देती हैं:

| Glyph | भूमिका | उपयोग |
|-------|--------|-------|
| `←` | Runtime flow | Initial binding, reassignment, mutation |
| `=` | Structural shape | Literals और metadata के भीतर field names |

<<<FENCE 4>>>

## ex से field extraction {#ex-field-extraction}

`ex` किसी value से fields निकालकर local bindings में रखता है:

<<<FENCE 5>>>

## Postfix increment और decrement {#postfix-increment-and-decrement}

`⊕` और `⊖`, परिवर्तनशील `numerus` places के लिए postfix increment/decrement statements हैं। ये केवल statements के रूप में उपयोग किए जा सकते हैं — इनका कोई expression value नहीं होता और इनके prefix रूप नहीं हैं:

<<<FENCE 6>>>
