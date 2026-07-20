+++
translation_kind = "translated"

title = "AI Workbench"
section = "ecosystem"
order = 4
sources = [
  "examples/ai-workbench/ (README.md, package, harness)",
]


prose_hash = "sha256:3a8940d1ee168b9bdf75f40f70ce5e5eb6b6446f47510df9c3511b2d4d1bef33"
code_hash = "sha256:dc8f04249d6a95c65b63ba0ccd58c402d6f8ed47a96bc15da4b6ad844922d007"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
AI वर्कबेंच एक Faber CLI एप्लिकेशन है, जो स्थानीय मॉडल इन्वेंटरी, मेटाडेटा निरीक्षण, एम्बेडिंग, इंडेक्सिंग और इन्फ़रेंस वर्कफ़्लो के लिए है। यह दिखाता है कि Faber वास्तविक I/O, JSON आउटपुट और Python हार्नेस वैलिडेशन के साथ एक व्यापक, बहु-कमांड CLI एप्लिकेशन बना सकता है।

## पैकेज {#package}

`examples/ai-workbench/packages/faber-ai/` में CLI सबकमांड:

- `model inspect` — स्थानीय मॉडल उपनाम, रूट और स्थिति पूछें
- `embed` — टेक्स्ट इनपुट से एम्बेडिंग बनाएँ

## कमांड {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

## वैलिडेशन {#validation}

AI वर्कबेंच में 20 से अधिक Python हार्नेस स्क्रिप्ट शामिल हैं, जो मॉडल इन्वेंटरी, इन्फ़रेंस, GPU साक्ष्य, सेशन लाइफ़साइकल और पैकेज पुनःउपयोग के लिए Faber आउटपुट की तुलना फ़िक्स्चर मैप से करती हैं। यह संकलित Faber बाइनरी के क्रॉस-लैंग्वेज वैलिडेशन को प्रदर्शित करता है।
