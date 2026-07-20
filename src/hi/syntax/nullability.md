+++
translation_kind = "translated"

title = "Nullability and optionality"
section = "syntax"
order = 11
sources = [
  "radix/README.md (Nullability and Optionality)",
  "examples/corpus/nihil/",
  "examples/corpus/sponte/",
  "examples/corpus/nonnihil/",
]


prose_hash = "sha256:0bf95ac93cff7571775fd0874fcd4d1b00ce96a7a3f47f75b6da1ed1c2dd2d57"
code_hash = "sha256:08e8387c2c18e42258c69e0ff67816e5f9d187787ef444f20380f76264a4827b"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber किसी मान में अनुपस्थिति और घोषणा स्थल पर वैकल्पिक प्रावधान के बीच भेद करता है।

## नलनीय मान — T ∪ nihil {#nullable-values}

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

## वैकल्पिक घोषणा स्लॉट — sponte {#optional-declaration-slots}

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

## नल-रहित अभिकथन — ! {#non-null-assertion}

किसी नलनीय मान के `nihil` न होने का अभिकथन करने के लिए `!.`, `![`, `!(` का उपयोग करें:

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

`nihil` पर नल-रहित अभिकथन रनटाइम पर प्रोग्राम को रोक देता है।

## नलिश सहसंयोजन — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

## ignotum {#ignotum}

`ignotum` एस्केप हैच और अधूरी जानकारी के लिए शीर्ष-स्तरीय अज्ञात प्रकार है। यह नलनीयता की कोई व्यवस्था नहीं है।
