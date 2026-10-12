वास्तविक Faber पैकेज — केवल अभ्यास के लिए बनाए गए छोटे स्निपेट नहीं। स्रोत सार्वजनिक
[faberlang/examples](https://github.com/faberlang/examples) रिपॉज़िटरी में है।
जब आपको यह देखना हो कि एप्लिकेशन कैसे संरचित किए जाते हैं, CLI कैसे जोड़ी जाती हैं,
या भाषा कॉर्पस कैसे व्यवस्थित किया गया है, तब इनका उपयोग करें।

## उदाहरण कैसे चलाएँ {#how-to-run}

<<<FENCE 0>>>

प्रवेश कमांड पैकेज के अनुसार अलग-अलग होते हैं — हर पैकेज की `README.md` पढ़ें।

## एप्लिकेशन पैकेज {#applications}

| पैकेज | भूमिका | यहाँ से शुरू करें |
|---|---|---|
| **AI Workbench** | स्थानीय मॉडल इन्वेंटरी, एम्बेडिंग और इन्फरेंस वर्कफ़्लो के लिए बहु-कमांड CLI; Python हार्नेस सत्यापन | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · साइट: [AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | एजेंट समन्वय कमांड के लिए Faber-नेटिव स्थानीय मेलस्पेस CLI (फ़ाइल-आधारित और वैकल्पिक SQLite लेन) | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | समानता हार्नेस के साथ सामान्य यूटिलिटी को फिर से लागू करने वाला बड़ा एप्लिकेशन अभियान | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | GPU / सिस्टम वर्कलोड के स्तर और कॉन्ट्रैक्ट | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | स्क्रिप्टिंग और कर्नेल-उन्मुख डेमो | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | ऑटोमेशन स्केच पैकेज | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | कीवर्ड रीमैपिंग के लिए लोकेल पैक डेमो | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | पैकेज-स्टोर लैब सामग्री | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## भाषा कॉर्पस {#corpus}

**corpus** ट्री कीवर्ड और कंस्ट्रक्ट का संदर्भ है: हर कंस्ट्रक्ट के लिए एक डायरेक्टरी
और उसमें कई छोटे `.fab` प्रोग्राम। यह इस साइट के जनरेट किए गए [Corpus](/corpus/)
पृष्ठों का स्रोत-सत्य है।

| सतह | URL |
|---|---|
| स्रोत ट्री | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| जनरेट किए गए दस्तावेज़ | [/corpus/](/corpus/) |
| इकोसिस्टम नोट | [Language corpus](/ecosystem/corpus.html) |

## स्टैंडर्ड लाइब्रेरी भ्रमण {#stdlib}

Norma की मानक-लाइब्रेरी exempla **norma** रिपॉज़िटरी में हैं, `examples/` के अंतर्गत नहीं:

- [faberlang/norma](https://github.com/faberlang/norma) — उपलब्ध होने पर `norma/exempla/`
- साइट: [Norma](/ecosystem/norma.html)

## सुझाया गया सीखने का क्रम {#order}

1. CLI को [इंस्टॉल](/start/install.html) करें।
2. भाषा की संरचना समझने के लिए [त्वरित भ्रमण](/start/) देखें।
3. जिस भी कीवर्ड को आप नहीं पहचानते, उसके लिए **corpus** पृष्ठ खोलें ([Corpus hub](/corpus/))।
4. एप्लिकेशन की संरचना समझने के लिए **AI Workbench** या **ViviLite** को शुरू से अंत तक पढ़ें।
5. संपादन के दौरान संदर्भ के रूप में [Syntax](/syntax/) और [Tooling](/tooling/) का उपयोग करें।

## एजेंट पथ {#agent-path}

- स्किल: [examples](/.well-known/agent-skills/examples/SKILL.md)
- स्किल: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- इंडेक्स: [`/llms.txt`](/llms.txt)

## पिछला {#previous}

| पिछला | अगला |
|---|---|
| [प्रोजेक्ट और उदाहरण](/start/projects.html) | [फ़ीचर](/features/) |
