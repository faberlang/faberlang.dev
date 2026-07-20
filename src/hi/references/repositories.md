+++
translation_kind = "translated"

title = "Repositories"
section = "references"
order = 3
sources = [
  "github.com/faberlang",
]


prose_hash = "sha256:1f00ec1ce77844348776b258be2b9246bf876b614a2849a0e8dcbb54a8dc82f0"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
Faber को `faberlang` संगठन के अंतर्गत कई रिपॉज़िटरी में विकसित किया जाता है।

## सार्वजनिक रिपॉज़िटरी {#public-repositories}

| रिपॉज़िटरी | विवरण |
|-----------|-------------|
| `faber` | उपयोगकर्ता-केंद्रित CLI: check, build, run, test, format, explain |
| `faber-runtime` | मुख्य रनटाइम प्रकार (Valor, tensors, frames); क्रेट का नाम `faber` |
| `norma` | मानक लाइब्रेरी का स्रोत (`norma:*` मॉड्यूल) |
| `triga` | वैकल्पिक ग्राफ़िक्स/ज्यामिति लाइब्रेरी |
| `cista` | पैकेज प्रबंधक और स्टोर (प्रायोगिक) |
| `examples` | भाषा कॉर्पस, coreutils, AI Workbench, reader-locale पैकेज |
| `faberlang.dev` | यह वेबसाइट |

## निजी रिपॉज़िटरी {#private-repositories}

| रिपॉज़िटरी | विवरण |
|-----------|-------------|
| `radix` | कंपाइलर: लेक्सिंग, पार्सिंग, सिमेंटिक विश्लेषण, HIR/MIR/AIR, डायग्नॉस्टिक्स, कोड जनरेशन |

## होस्ट प्लेटफ़ॉर्म रिपॉज़िटरी {#host-platform-repositories}

| रिपॉज़िटरी | विवरण |
|-----------|-------------|
| `host-kernel-rs` | पतला राउटर: Frame, Conversation, प्रीफ़िक्स डिस्पैच, संरचित त्रुटियाँ |
| `host-native-rs` | नेटिव अटैच: वर्कर्स, `register_providers` हुक |
| `host-providers-rs` | प्रोवाइडर कार्यान्वयन: solum, processus, consolum, tempus, aleator, http |
