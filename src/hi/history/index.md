+++
translation_kind = "translated"

title = "History"
section = "history"
order = 0
sources = []


prose_hash = "sha256:99390038c112db9d79c728a21f5bc2c804af48f6de648df7e6ff6f2f0bc32a99"
code_hash = "sha256:8cfe9c845ef9a1247454bc890937eafa78a38164428679c7a6981c3c8cf3b9c4"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
## उत्पत्ति {#origins}

Radix कंपाइलर का पहला कमिट **20 दिसंबर 2024** को Bun + TypeScript प्रोजेक्ट के रूप में किया गया था, जिसमें केवल एक `docs/decisions.md` फ़ाइल थी। दूसरे कमिट में पाँच Architecture Decision Records को औपचारिक रूप दिया गया, जो आज भी भाषा की दिशा तय करते हैं।

**ADR-003**, जिसका शीर्षक था "Case endings carry semantic meaning", ने शुरुआत में ही स्थापित कर दिया था कि लैटिन रूप-विज्ञान केवल कीवर्ड की बाहरी परत नहीं होगा — कंपाइलर विभक्ति और क्रिया-रूपों को समझकर प्रोग्राम के आशय का अनुमान लगाएगा। मूल case mappings इस प्रकार थे:

```text
Nominative  (subject)       →  return value, caller
Accusative  (direct object)  →  primary argument
Dative      (indirect obj.)  →  recipient, callback, destination
Genitive    (possession)     →  property access, "of" relationships
Ablative    (instrument)     →  dependencies, context, "using X"
```

उसी दस्तावेज़ में यह भी लिखा था: *"Verb conjugation is a natural follow-on question (future tense → async?)."* यही बीज आगे चलकर आधुनिक **morphologia** नामकरण परंपरा में विकसित हुआ, जिसमें standard library sync बनाम async और mutate बनाम copy-out का संकेत देने के लिए लैटिन क्रियाओं के conjugated रूपों का उपयोग करती है — और इसके लिए कंपाइलर को स्वयं लैटिन व्याकरण समझने की आवश्यकता नहीं होती।

प्रोजेक्ट की शुरुआत TypeScript में हुई, बाद में इसे Rust में फिर से लिखा गया, और edition 2026 के साथ 1.x श्रृंखला के लिए व्याकरण को स्थिर कर दिया गया। मूल पाँच ADRs (फ़ाइल एक्सटेंशन `.fab`, error hints, case endings, recursive descent parser, custom AST) आज भी git इतिहास में दिखाई देते हैं।

## रिलीज़ {#releases}

पहले वर्तमान Faber रिलीज़ के CLI archive, फिर [faberlang/releases](https://github.com/faberlang/releases) में प्रकाशित हर tag और binary:

- **[रिलीज़](/history/releases.html)** — डाउनलोड लिंक और ऐतिहासिक सूची
- **[इंस्टॉल और डाउनलोड](/start/install.html)** — PATH सेटअप और पहला `faber check`
