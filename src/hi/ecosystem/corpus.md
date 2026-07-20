+++
translation_kind = "translated"

title = "Language corpus"
section = "ecosystem"
order = 6
sources = [
  "examples/corpus/ (292 .fab files, 174 registry terms, index.toml)",
  "examples/corpus/README.md",
]


prose_hash = "sha256:6dab4295fafeea620e65bd30edcc6c810bc3f0b11cb8681aae63f79ecbe2be63"
code_hash = "sha256:fbdcbf8ce9cd3fdcb367022a7df1cdbd74fd62244d662a6a85229773e4910739"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Faber भाषा कॉर्पस सार्वजनिक भाषा शब्दकोश है: इसमें प्रत्येक कीवर्ड, ऑपरेटर समूह या भाषा-प्रकार के लिए एक शीर्ष-स्तरीय डायरेक्टरी है। यह `faber explain` का विकास-स्रोत और बहु-लक्ष्य संकलन मैट्रिस के लिए प्राथमिक इनपुट है।

## आँकड़े {#stats}

- 292 `.fab` उदाहरण फ़ाइलें
- `index.toml` में 174 रजिस्ट्री टर्म
- लगभग 135 कीवर्ड और अवधारणा डायरेक्टरी

## लेआउट {#layout}

```
corpus/
  functio/           # function keyword exemplars
  genus/             # record type exemplars
  si/                # conditional branch exemplars
  itera/             # iteration exemplars
  lista/ tabula/     # collection type exemplars
  tensor/ sparsa/    # tensor exemplars
  ad/                # capability call exemplars
  operatores/        # glyph / operator groups
  ...
  index.toml         # generated explain manifest
```

## फ़ाइल प्रारूप {#file-format}

प्रत्येक `.fab` फ़ाइल की शुरुआत टर्म का वर्णन करने वाले TOML फ्रंटमैटर से होती है:

```toml
+++
term = "functio"
kind = "keyword"
category = "function"
canonical = true
summary = "Declares a named function or method."
syntax = "functio <name>(<params>) [modifiers] [→ <type>] [⇥ <error-type>] <block>"
aliases = ["function"]
related = ["→", "⇥", "redde", "sponte"]
+++

functio saluta() {
    nota "Salve, Mundus!"
}
```

## उपयोग {#usage}

```bash
faber explain functio       # show keyword reference
faber explain ≡             # show glyph reference
faber explain --search query # search across corpus
faber explain --list         # list all terms
```

## श्रेणियाँ {#categories}

टर्म श्रेणियों के अनुसार व्यवस्थित हैं: `function`, `control-flow`, `type`,
`collection`, `transfer`, `annotation`, `iteration`, `destructuring`,
`testing`, `cli`, `concept`, `operator-group`, `existing-home`.
