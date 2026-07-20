+++
translation_kind = "translated"

title = "EBNF grammar"
section = "references"
order = 1
sources = [
  "radix/EBNF.md",
]


prose_hash = "sha256:901fe46feace9eaea92780fc259f6ae17c168dba45fe1ff9c0ee95e8c4858ea2"
code_hash = "sha256:4f0d91b053057a4ac78a57bb7ecb6914b647b3bd8c5855e3696e48f2c32fc265"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
Faber का आधिकारिक व्याकरण Radix रिपॉज़िटरी में
`radix/EBNF.md` में परिभाषित है। यह भाषा के पूरे सिंटैक्स के लिए औपचारिक प्राधिकरण है।

व्याकरण में ये विषय शामिल हैं:

- लेक्सिकल संरचना (ग्लिफ़, कीवर्ड, लिटरल, टिप्पणियाँ)
- घोषणाएँ (`functio`, `genus`, `implendum`, `typus`, `discretio`, `ordo`)
- कथन (बाइंडिंग, नियंत्रण प्रवाह, रिटर्न, पुनरावृत्ति)
- अभिव्यक्तियाँ (कॉल, ऑपरेटर, रूपांतरण, लिटरल)
- एनोटेशन (`@` सिंटैक्स)
- CLI एनोटेशन (`@ cli`, `@ optio`, `@ operandus`, `@ imperium`)
- प्रकार अभिव्यक्तियाँ (प्रिमिटिव, जेनेरिक, शुगर रूप)
- मॉड्यूल सिस्टम (`importa`)

```ebnf
(* excerpt: function declaration *)
funcDecl = 'functio' ident genericParams? '(' paramList ')' ('→' type)? ('⇥' type)? block;
block    = '{' stmt* '}';
```
