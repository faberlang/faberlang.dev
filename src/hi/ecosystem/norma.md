+++
translation_kind = "translated"

title = "Norma standard library"
section = "ecosystem"
order = 1
sources = [
  "radix/README.md (Standard Library section)",
  "sibling norma/ repository",
  "norma/exempla/",
  "radix/docs/stdlib/morphologia.md",
]


prose_hash = "sha256:f333d0ee78b78e5ad3ebfb1bfdda0a4069a9b7daf3579d8c55d6b83c668be833"
code_hash = "sha256:0ef63774f36a5e950889dcae691b2a9c5add05fe03c89c061ba60d829195f2ff"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Norma, Faber की मानक लाइब्रेरी है। यह `norma:*` पथों से एक्सेस किए जाने वाले सरल Latin-नाम वाले मॉड्यूल प्रदान करती है। मानक लाइब्रेरी की घोषणाएँ सहायक `norma` रिपॉज़िटरी में Faber स्रोत के रूप में उपलब्ध हैं।

## मॉड्यूल {#modules}

| मॉड्यूल | क्षेत्र |
|--------|--------|
| `norma:solum` | फ़ाइल सिस्टम संचालन |
| `norma:solum/path` | शुद्ध पथनाम संचालन |
| `norma:http` | HTTP क्लाइंट |
| `norma:processus` | प्रक्रिया निष्पादन |
| `norma:consolum` | कंसोल I/O (stdin, stdout, stderr) |
| `norma:json` | JSON पार्सिंग और सीरियलाइज़ेशन |
| `norma:toml` | TOML पार्सिंग |
| `norma:yaml` | YAML पार्सिंग |
| `norma:valor` | कोडेक नेविगेशन |
| `norma:tensor` | टेन्सर ब्रिज सहायक |
| `norma:tempus` | समय और अवधि |
| `norma:aleator` | यादृच्छिकता |

## Morphologia नामकरण परंपरा {#morphologia-naming-convention}

Norma सभी मेथड नामों के लिए morphologia नीति का पालन करती है। Latin क्रिया-रूप निष्पादन मोड दर्शाते हैं:

| मूल | समकालिक | असमकालिक | अर्थ |
|------|------|-------|---------|
| `leg-` | `lege` | `leget` | पढ़ना |
| `scrib-` | `scribe` | `scribet` | लिखना |
| `quaer-` | — | `quaeret` | क्वेरी (सीमित) |
| `quaer-` | — | `quaerent` | क्वेरी (स्ट्रीम) |

स्वामित्व युग्म (म्यूटेट बनाम कॉपी-आउट):

| म्यूटेट | कॉपी-आउट | अर्थ |
|--------|------|---------|
| `adde` | `addita` | जोड़ना |
| `inverte` | `inversa` | उलटना |
| `filtra` | `filtrata` | फ़िल्टर करना |

## उपयोग {#usage}

```faber locale=la
importa ex "norma:solum" privata solum

functio legeConfig() → textus {
    redde solum.lege("config.toml")
}
```
