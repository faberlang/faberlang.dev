+++
translation_kind = "translated"

title = "Faber build tool"
section = "tooling"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
]


prose_hash = "sha256:5d8304941413ba003c019f0b1c43cd19e99ad0f25fa9b7a4ffadbc1327e8dfb6"
code_hash = "sha256:7657ec817fefbfb88c20a7b862970c668ebe2835de88c17eda584340fd2d6654"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
`faber` CLI Faber स्रोत बनाने, जाँचने, चलाने, फ़ॉर्मैट करने और परीक्षण करने का मुख्य प्रवेश-बिंदु है। यह Radix कंपाइलर को डेवलपर के लिए सुविधाजनक टूल में समाहित करता है।

## मुख्य कमांड {#core-commands}

| कमांड | उद्देश्य |
|---|---|
| `faber build <path>` | पैकेज को लक्ष्य बैकएंड में कंपाइल करना (डिफ़ॉल्ट: Rust) |
| `faber check <path>` | कोड बनाए बिना प्रकार-जाँच करना |
| `faber run <path>` | बिल्ड करके चलाना |
| `faber test <path>` | `proba` परीक्षण सुइट चलाना |
| `faber format <path>` | मानक फ़ॉर्मैटिंग लागू करना |
| `faber explain <code>` | डायग्नॉस्टिक कोड की व्याख्या करना |
| `faber emit <path>` | स्रोत को किसी लक्ष्य सरफेस में उत्सर्जित करना |

## पैकेज बनाना {#building}

```text
faber build my-package/ -t rust
```

`-t` फ़्लैग कोडजन लक्ष्य चुनता है। समर्थित लक्ष्यों में `rust`
(डिफ़ॉल्ट), `wasm`, `typescript` और `go` शामिल हैं।

## कोड बनाए बिना जाँच करना {#checking}

```text
faber check my-package/
```

पूरा फ़्रंट एंड (lex → parse → typecheck → MIR lowering) चलाता है, लेकिन
आउटपुट आर्टिफ़ैक्ट नहीं बनाता। CI और एडिटर इंटीग्रेशन में इसका उपयोग करें।

## परीक्षण चलाना {#testing-command}

```text
faber test my-package/
```

पैकेज में मौजूद सभी `probandum` सुइट को Rust की `#[test]` फ़ंक्शन में
कंपाइल करता है और उन्हें Cargo के माध्यम से चलाता है। इनलाइन परीक्षण स्रोत
कोड के साथ ही रहते हैं — अलग परीक्षण बाइनरी की आवश्यकता नहीं होती।

## फ़ॉर्मैटिंग {#formatting}

```text
faber format my-package/
```

मानक Faber फ़ॉर्मैटर लागू करता है। फ़ॉर्मैटर एकरूप लेआउट लागू करता है:
प्रति पंक्ति एक घोषणा, मानक स्पेसिंग और एकरूप कीवर्ड सरफेस।

## डायग्नॉस्टिक की व्याख्या {#explaining}

```text
faber explain SEM001
```

कंपाइलर द्वारा जारी किए जा सकने वाले किसी भी डायग्नॉस्टिक कोड की मानव-पठनीय
व्याख्या प्रिंट करता है। यह समझने में उपयोगी है कि किसी त्रुटि का अर्थ क्या है
और उसे कैसे ठीक किया जाए।
