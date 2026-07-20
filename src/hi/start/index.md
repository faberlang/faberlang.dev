+++
translation_kind = "translated"

title = "Quick tour"
section = "start"
order = 0
sources = []

prose_hash = "sha256:fb6f791ae0e9b73d0c92c2127726f558a2b845351779f80217616b8f55629ff0"
code_hash = "sha256:f9eb22ab8a2408fe0076d846dd4266cff4ded675ad8d63a5b2d9ee59c3e0156f"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
Faber के आकार को पाँच मिनट में समझें: CLI इंस्टॉल करें, एक फ़ंक्शन पढ़ें,
फिर एक वास्तविक पैकेज खोलें। क्रमबद्ध रास्ते के लिए यह क्रम अपनाएँ: [इंस्टॉल](/start/install.html) →
[हैलो](/start/hello.html) → [कमांड](/start/commands.html) →
[प्रोजेक्ट](/start/projects.html)।

## 1. CLI इंस्टॉल करें {#install}

अपने प्लेटफ़ॉर्म के लिए वर्तमान रिलीज़ (**1.1.1**) [इंस्टॉल पेज](/start/install.html) से डाउनलोड करें,
आर्काइव का चेकसम सत्यापित करें, और निकाली गई `faber-v1.1.1-<target-triple>/faber` बाइनरी को अपने
`PATH` में रखें। पुष्टि करें:

```bash
faber --version
```

## 2. फ़ंक्शन का आकार {#shape}

टाइप-प्रथम पैरामीटर, ग्लिफ़ रिटर्न टाइप, लैटिन नियंत्रण शब्द, nullable
यूनियन:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

| संकेत | अर्थ |
|---|---|
| `functio` | फ़ंक्शन घोषणा |
| `numerus a` | पहले टाइप, फिर नाम |
| `→` | रिटर्न टाइप |
| `∪ nihil` | Nullable (`T ∪ nihil`) |
| `si … ∴` | संक्षिप्त शाखा |
| `redde` | रिटर्न |

## 3. पैकेज का विन्यास {#package}

एक पैकेज `faber.toml` और `src/` वाली निर्देशिका होती है:

```text
my-app/
  faber.toml
  src/
    main.fab
```

सामान्य कमांड:

```bash
faber check my-app/
faber build my-app/ -t rust
faber run my-app/
faber test my-app/
```

विवरण: [Faber बिल्ड टूल](/tooling/faber-build-tool.html)।

## 4. वास्तविक एप्लिकेशन {#applications}

Hello-world पर न रुकें। सार्वजनिक **examples** रिपॉज़िटरी में बहु-कमांड
CLI, स्थानीय mailspace, GPU workload tracks और एक पूर्ण भाषा corpus शामिल हैं।

| पैकेज | यह क्या दिखाता है |
|---|---|
| AI Workbench | बहु-कमांड CLI, मॉडल निरीक्षण, embeddings |
| ViviLite | फ़ाइल-आधारित mailspace / agent coordination CLI |
| coreutils | बड़ा एप्लिकेशन अभियान (parity harnesses) |
| gpu-workload | सिस्टम / GPU rungs |
| corpus | प्रत्येक भाषा-निर्माण के लिए एक निर्देशिका |

उन्हें [examples पेज](/start/examples.html) पर देखें।

## 5. यदि आप एजेंट हैं {#agents}

1. [`/llms.txt`](/llms.txt) पढ़ें।
2. [`/agents/index.md`](/agents/index.md) खोलें।
3. [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json) से कोई skill चुनें।

## शुरुआत का ट्रैक {#start-track}

| चरण | पेज | परिणाम |
|---|---|---|
| 1 | [इंस्टॉल और डाउनलोड](/start/install.html) | Faber 1.1.1 को `PATH` में रखें और सत्यापित करें |
| 2 | [हैलो, Faber](/start/hello.html) | `salve-munde` बनाएँ और चलाएँ |
| 3 | [वे कमांड जिनका आप उपयोग करेंगे](/start/commands.html) | `check`, `build`, `run`, `test`, `explain` सीखें |
| 4 | [प्रोजेक्ट और उदाहरण](/start/projects.html) | वास्तविक पैकेज और corpus पेजों पर जाएँ |

## आगे {#next}

| विषय | लिंक |
|---|---|
| इंस्टॉल और डाउनलोड | [इंस्टॉल](/start/install.html) |
| हैलो, Faber | [हैलो](/start/hello.html) |
| कमांड | [कमांड](/start/commands.html) |
| प्रोजेक्ट | [प्रोजेक्ट](/start/projects.html) |
| सिंटैक्स संदर्भ | [सिंटैक्स](/syntax/) |
| सुविधाएँ (स्थानीय भाषाएँ, lanes) | [सुविधाएँ](/features/) |
| इकोसिस्टम लाइब्रेरी | [इकोसिस्टम](/ecosystem/) |
| कीवर्ड corpus | [Corpus](/corpus/) |
