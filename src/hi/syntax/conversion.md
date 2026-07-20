+++
translation_kind = "translated"

title = "Conversion and construction"
section = "syntax"
order = 9
sources = [
  "radix/README.md (Conversion and Construction)",
  "radix/docs/design/conversio-valor.md",
  "radix/docs/design/failable-conversio.md",
]


prose_hash = "sha256:5804f612f8d3df38cbb8bf659a1e16484df7bab2c0fb0ca31f24f2281821aeb6"
code_hash = "sha256:a9b4077c5847b3cd815b5494ca2fdaed9f8eb83835307924dacd7a7fb6b72270"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
रनटाइम और कंपाइल-टाइम के लिए दो महत्वपूर्ण रूपांतरण ऑपरेटर:

```faber
# runtime conversion
fixum _ parsed ← "42" ↦ numerus
# static ascription
fixum numerus value ← 7
fixum _ text ← value ∷ textus
```

## रनटाइम रूपांतरण — ↦ {#runtime-conversion}

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

## स्थिर प्रकार-निर्देशन — ∷ {#static-ascription}

स्पष्ट स्थिर प्रकार-निर्देशन के लिए `∷` का उपयोग करें। यह पोस्टफ़िक्स होता है और लक्ष्य-प्रकार द्वारा निर्देशित होता है:

```faber
fixum numerus value ← 7
fixum _ x ← 7 ∷ numerus<i32>
fixum _ text ← value ∷ textus
```

## नलिश कोअलेसिंग — vel {#nullish-coalescing}

जब कोई मान `nihil` हो, तब नलिश कोअलेसिंग के लिए `vel` का उपयोग करें:

```faber
fixum textus ∪ nihil provided_name ← nihil
fixum _ name ← provided_name vel "default"
```
