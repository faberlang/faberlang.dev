+++
translation_kind = "translated"

title = "Faber"
section = ""
order = 0
sources = []

prose_hash = "sha256:e63352acf54515593d9aeccf392881d72018d55e6b21d6e1ddd5a3979bef91b8"
code_hash = "sha256:a02ba6ea46d65efd212b09e097d3240402bfe1d46f89b993e389cd53ca1a9c9e"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
**Faber** एक पैकेज-आधारित प्रोग्रामिंग भाषा है, जिसमें लैटिन
व्यवहारिक शब्दावली, एक छोटी नियमित व्याकरण, और प्रकार-प्रथम स्थैतिक
टाइप प्रणाली है। स्रोत को Radix कंपाइलर के माध्यम से समीक्षा योग्य
Rust और नेटिव बाइनरी में संकलित किया जाता है। इसकी विशिष्ट स्थापत्य
विशेषता यह है कि अर्थ किसी विशेष रेंडरिंग में नहीं, बल्कि एक
सार्थक कोर — HIR (हाई-लेवल इंटरमीडिएट रिप्रेज़ेंटेशन) — में निहित रहता है।

यह नाम लैटिन शब्द *maker* या *craftsman* से निकला है। कंपाइलर का नाम
Radix है, जो लैटिन *root* से लिया गया है। भाषा को Ian Zepp विकसित करते
हैं और यह MIT लाइसेंस के अंतर्गत जारी की जाती है।

**यहाँ नए हैं?** [इंस्टॉल और डाउनलोड](/start/install.html) से शुरू करें,
फिर क्रमबद्ध प्रारंभिक ट्रैक चलाएँ: [Hello](/start/hello.html),
[Commands](/start/commands.html), और [Projects](/start/projects.html)।

## Faber 1.1.1 डाउनलोड करें {#download}

वर्तमान रिलीज़: **Faber 1.1.1** (टैग `faber-v1.1.1`)। macOS और Linux के लिए
पहले से बने CLI आर्काइव उपलब्ध हैं; `faber-v1.1.1-<target-triple>/faber`
बाइनरी को निकालकर अपने `PATH` में रखें।

| प्लेटफ़ॉर्म | आर्काइव | चेकसम |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [faber-v1.1.1-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

त्वरित इंस्टॉल (macOS arm64 उदाहरण):

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv faber-v1.1.1-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

सभी रिलीज़ नोट्स और एसेट: [github.com/faberlang/releases · faber-v1.1.1](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1)।
चरण-दर-चरण: [इंस्टॉल गाइड](/start/install.html)। पूरा ऐतिहासिक
इन्वेंटरी: [रिलीज़](/history/releases.html)।

| | |
|---|---|
| **प्रतिमान** | पैकेज-आधारित; अर्थगत स्टेजिंग |
| **टाइपिंग** | स्थैतिक, प्रकार-प्रथम; `T ∪ nihil` के माध्यम से nullable |
| **ग्लिफ़** | `← → ∴ ≡ ∪ ⇥` |
| **डिज़ाइनर** | Ian Zepp |
| **पहली प्रस्तुति** | 2024 |
| **कंपाइलर** | Radix (Rust) |
| **लेन** | एप्लिकेशन (HIR) · सिस्टम्स (MIR) |
| **प्राथमिक लक्ष्य** | Rust → नेटिव बाइनरी |
| **रीडर लोकेल** | 7 उपलब्ध (la, ar, hi, vi, th-TH, zh-Hans, zh-Hant) |
| **मानक लाइब्रेरी** | Norma (`norma:*`) |
| **लाइसेंस** | MIT |

## यहाँ से शुरू करें {#start-here}

| पथ | किसके लिए | क्या |
|---|---|---|
| [इंस्टॉल](/start/install.html) | मानव | डाउनलोड, PATH, पहला `faber check` |
| [Hello](/start/hello.html) | मानव | `salve-munde` बनाएँ और चलाएँ |
| [Commands](/start/commands.html) | मानव + एजेंट | दैनिक CLI चक्र: check, build, run, test, explain |
| [Projects](/start/projects.html) | मानव + एजेंट | hello-world से वास्तविक पैकेजों तक जाएँ |
| [त्वरित परिचय](/start/) | मानव | पाँच मिनट में भाषा का रूप |
| [उदाहरण](/start/examples.html) | मानव + एजेंट | वास्तविक पैकेज: CLI ऐप्स, mailspace, GPU, corpus |
| [`/llms.txt`](/llms.txt) | एजेंट | मशीन इंडेक्स — यदि आप मॉडल हैं तो यहाँ से शुरू करें |
| [एजेंट गाइड](/agents/index.md) | एजेंट | Faber सीखने और पैकेज जारी करने का तरीका |
| [एजेंट स्किल्स](/.well-known/agent-skills/index.json) | एजेंट | केंद्रित स्किल गाइड (इंस्टॉल, भाषा, उदाहरण, …) |

## पोर्टल स्थिति {#portal-status}

यह `/` पृष्ठ अंग्रेज़ी साइट के लिए Speculum Porta है: एक ऐसा locale-less
प्रवेश बिंदु जो लोगों को इंस्टॉल/प्रारंभ पृष्ठों तक भेजता है, एजेंटों को
मशीन सतहों तक पहुँचाता है, और ब्राउज़र-समय नेगोशिएशन के बिना लोकेल पैक
की स्थिति बताता है। Stage 7 एक आंशिक बहु-लोकेल प्रमाण है, पूर्ण स्थानीयकृत
साइट नहीं: केवल `th-TH`, `zh-Hans`, `zh-Hant`, `vi`, `ar`, और `hi` में
जनरेट किए गए पोर्टल/प्रारंभ लेखक-स्लाइस और जनरेट किए गए corpus पृष्ठ हैं,
जबकि लेखकित गद्य अभी भी अंग्रेज़ी पर फ़ॉलबैक करता है।

| लोकेल | स्थिति | टिप्पणियाँ |
|---|---|---|
| `la` | आधिकारिक लाइव साइट | पूर्ण जनरेट की गई अंग्रेज़ी/लैटिन साइट |
| `th-TH` | Stage 7 आंशिक प्रमाण | पोर्टल/प्रारंभ लेखक-स्लाइस और जनरेट किया गया corpus; अंग्रेज़ी गद्य पर फ़ॉलबैक; पूर्ण लेखकित दस्तावेज़ लंबित |
| `zh-Hans` | Stage 7 आंशिक प्रमाण | पोर्टल/प्रारंभ लेखक-स्लाइस और जनरेट किया गया corpus; अंग्रेज़ी गद्य पर फ़ॉलबैक; पूर्ण लेखकित दस्तावेज़ लंबित |
| `vi` | Stage 7 आंशिक प्रमाण | पोर्टल/प्रारंभ लेखक-स्लाइस और जनरेट किया गया corpus; अंग्रेज़ी गद्य पर फ़ॉलबैक; पूर्ण लेखकित दस्तावेज़ लंबित |
| `zh-Hant` | Stage 7 आंशिक प्रमाण | पोर्टल/प्रारंभ लेखक-स्लाइस और जनरेट किया गया corpus; अंग्रेज़ी गद्य पर फ़ॉलबैक; पूर्ण लेखकित दस्तावेज़ लंबित |
| `ar` | Stage 7 आंशिक प्रमाण | पोर्टल/प्रारंभ लेखक-स्लाइस और जनरेट किया गया corpus; अंग्रेज़ी गद्य पर फ़ॉलबैक; पूर्ण लेखकित दस्तावेज़ लंबित |
| `hi` | Stage 7 आंशिक प्रमाण | पोर्टल/प्रारंभ लेखक-स्लाइस और जनरेट किया गया corpus; अंग्रेज़ी गद्य पर फ़ॉलबैक; पूर्ण लेखकित दस्तावेज़ लंबित |

आधिकारिक लैटिन में जीवंत उदाहरण:

```faber
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
```

उसी अर्थगत प्रोग्राम को थाई, सरलीकृत चीनी, पारंपरिक चीनी, अरबी, हिंदी और
वियतनामी पैक्स के माध्यम से रेंडर किया हुआ देखने के लिए
[रीडर लोकेल](/features/reader-locale.html) देखें।

## अवलोकन {#overview}

Faber एक मूल अंतर्दृष्टि के आधार पर डिज़ाइन की गई है: इंटरमीडिएट
रिप्रेज़ेंटेशन ही सत्य है, और किसी लक्ष्य या मानव-भाषा सतह को विशेष
अधिकार प्राप्त नहीं है। लैटिन कीवर्ड में लिखा गया Faber प्रोग्राम उसी
तंत्र के माध्यम से थाई, अरबी या चीनी कीवर्ड में रेंडर किया जा सकता है
जिससे वह Rust, Go या WebAssembly में रेंडर होता है — क्योंकि HIR ही
प्राधिकृत स्रोत है और हर आउटपुट उसका एक *रेंडरिंग* है।

भाषा तीन सोच-समझकर चुने गए संकेतों का उपयोग करती है, जो साथ मिलकर काम करते हैं:

- **प्रकार-प्रथम घोषणाएँ** — आकार को बाइंडिंग की ओर पढ़ने योग्य बनाती हैं:
  `textus nomen`, न कि `nomen: textus`।
- **लैटिन व्यवहारिक शब्द** — घोषणाएँ, कथन और जीवनचक्र:
  `functio`, `genus`, `fixum`, `redde`, `si`।
- **संरचनात्मक ग्लिफ़** — मान प्रवाह और प्रकार-संधियाँ: `←` (बाइंड),
  `→` (रिटर्न प्रकार), `∴` (संक्षिप्त शाखा), `≡` (समानता), `∪` (यूनियन)।

परिणाम ऐसा स्रोत है जिसका व्याकरणिक रूप स्थिर रहता है और जिसे पाठक के
आशय की अनुभूति खोए बिना समीक्षा, रूपांतरण और लोअर किया जा सकता है।

## दस्तावेज़ीकरण {#documentation}

| अनुभाग | विवरण |
|---|---|
| [इतिहास](/history/) | विकास-समयरेखा, प्रभाव और रिलीज़ इतिहास |
| [रिलीज़](/history/releases.html) | नवीनतम Faber डाउनलोड तथा प्रकाशित प्रत्येक टैग और बाइनरी |
| [विशेषताएँ](/features/) | रीडर लोकेल, संकलन लेन, लैटिन शब्दावली, ग्लिफ़ प्रणाली, डिज़ाइन सिद्धांत |
| [सिंटैक्स](/syntax/) | पूर्ण संदर्भ: प्रकार, फ़ंक्शन, नियंत्रण प्रवाह, त्रुटियाँ, जेनरिक, संग्रह |
| [टूलिंग](/tooling/) | Radix कंपाइलर पाइपलाइन, Faber CLI, कोडजेन लक्ष्य, स्क्रिप्टिंग |
| [इकोसिस्टम](/ecosystem/) | Norma, Cista, Triga, coreutils, AI Workbench, corpus |
| [Corpus](/corpus/) | सार्वजनिक corpus से जनरेट किए गए कीवर्ड और कंस्ट्रक्ट पृष्ठ |
| [संदर्भ](/references/) | EBNF व्याकरण, डिज़ाइन दस्तावेज़, रिपॉज़िटरी |

## त्वरित उदाहरण {#quick-example}

एक सरल फ़ंक्शन, जो Faber के प्रमुख पैटर्न दिखाता है — प्रकार-प्रथम
पैरामीटर, ग्लिफ़ रिटर्न प्रकार, nullable यूनियन, लैटिन नियंत्रण शब्द:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## लाइव रेंडरिंग {#live-rendering}

ऊपर दिया गया divide फ़ंक्शन डिफ़ॉल्ट रूप से लैटिन पैक में रेंडर होता है।
कंपाइलर उसी प्रोग्राम को सात रीडर लोकेल — थाई, सरलीकृत चीनी, पारंपरिक
चीनी, अरबी, हिंदी, वियतनामी — में रेंडर कर सकता है। हर लोकेल कीवर्ड और
प्रकारों को उस भाषा में पुनः मैप करता है, जबकि ग्लिफ़ और पहचानकर्ता
अपरिवर्तित रहते हैं। यह पृष्ठ पर लागू की गई अनुवाद परत नहीं है; यह वही
तंत्र है जिसका उपयोग कंपाइलर स्थानीयकृत स्रोत बनाने के लिए करता है।

पूरी चर्चा के लिए [रीडर लोकेल](/features/reader-locale.html) दस्तावेज़ देखें।

## रिपॉज़िटरी {#repositories}

| रिपॉज़िटरी | भूमिका |
|---|---|
| [faberlang/faber](https://github.com/faberlang/faber) | सार्वजनिक उपयोगकर्ता CLI |
| [faberlang/releases](https://github.com/faberlang/releases) | टैग किए गए CLI रिलीज़ एसेट |
| [faberlang/faber-runtime](https://github.com/faberlang/faber-runtime) | जनरेट किए गए Rust के लिए रनटाइम प्रकार |
| [faberlang/norma](https://github.com/faberlang/norma) | मानक लाइब्रेरी स्रोत |
| [faberlang/cista](https://github.com/faberlang/cista) | पैकेज-स्टोर CLI/लाइब्रेरी |
| [faberlang/triga](https://github.com/faberlang/triga) | ग्राफ़िक्स / ज्यामिति लाइब्रेरी |
| [faberlang/examples](https://github.com/faberlang/examples) | Corpus, ट्रैक, एप्लिकेशन पैकेज |
| [faberlang/faberlang.dev](https://github.com/faberlang/faberlang.dev) | यह दस्तावेज़ीकरण साइट |
