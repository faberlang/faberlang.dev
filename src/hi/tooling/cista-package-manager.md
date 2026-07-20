+++
translation_kind = "translated"

title = "Cista package manager"
section = "tooling"
order = 3
sources = [
  "cista/README.md",
]


prose_hash = "sha256:05d23a68f89274ac712edd9df74eceb081ecb757827aedd26e944afc3a23ab42"
code_hash = "sha256:8911c196f515c978b54a345902a35f102715550c60930e2efee379e50e6c7c1e"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Cista Faber का पैकेज प्रबंधक है। यह पैकेज समाधान, निर्भरता प्रबंधन और सार्वजनिक पैकेज स्टोर को संभालता है।

## अवलोकन {#overview}

Cista, `faber.toml` मेनिफेस्ट में परिभाषित Faber पैकेजों का प्रबंधन करता है। प्रत्येक पैकेज अपना नाम, प्रवेश-बिंदु, लक्ष्य बैकएंड और निर्भरताएँ घोषित करता है।

## पैकेज मेनिफेस्ट {#manifest}

```text
faber.toml

[nomen]
speculum-gen

[ingressus]
main.fab

[scopulus]
rust

[genus]
bin
```

`[nomen]` फ़ील्ड पैकेज का नाम है, `[ingressus]` प्रवेश-बिंदु मॉड्यूल है, `[scopulus]` कोड जनरेशन लक्ष्य चुनता है और `[genus]` पैकेज का प्रकार घोषित करता है (`bin` निष्पादन योग्य फ़ाइलों के लिए, `lib` लाइब्रेरी के लिए)।

## निर्भरताएँ {#dependencies}

पैकेज उन निर्भरताओं को घोषित करते हैं जिन्हें Cista पैकेज स्टोर से हल करता है। निर्भरता समाधान एक लॉक फ़ाइल बनाता है, जो पुनरुत्पाद्य बिल्ड सुनिश्चित करती है।

## स्थिति {#status}

Cista का सक्रिय विकास चल रहा है। सार्वजनिक पैकेज रजिस्ट्री (`cista.dev`) साइट के कार्यान्वयन से अलग अभियान है। स्थानीय पैकेज समाधान एक ही वर्कस्पेस के भीतर स्थित पैकेजों के लिए काम करता है।
