+++
translation_kind = "translated"

title = "Examples"
section = "examples"
order = 5
sources = [
  "examples/README.md",
  "examples/ai-workbench/",
  "examples/vivilite/",
  "examples/ai-workbench/ (README.md, package, harness)",
  "examples/coreutils/ (38 packages, README.md, campaign docs)",
  "examples/coreutils/packages/echo/src/main.fab",
]
+++

## Examples

वास्तविक Faber पैकेज — केवल अभ्यास के लिए बनाए गए छोटे स्निपेट नहीं। स्रोत सार्वजनिक
[faberlang/examples](https://github.com/faberlang/examples) रिपॉज़िटरी में है।
जब आपको यह देखना हो कि एप्लिकेशन कैसे संरचित किए जाते हैं, CLI कैसे जोड़ी जाती हैं,
या भाषा कॉर्पस कैसे व्यवस्थित किया गया है, तब इनका उपयोग करें।

### उदाहरण कैसे चलाएँ {#how-to-run}

```bash
# CLI on PATH (see Install)
faber --version

# Clone examples
git clone https://github.com/faberlang/examples.git

# Type-check a package; dependencies resolve through faber.lock
# and the Cista package store.
faber check examples/ai-workbench/packages/faber-ai

# Build / run / test when the package supports it
faber build examples/ai-workbench/packages/faber-ai -t rust
faber test examples/ai-workbench/packages/faber-ai
```

प्रवेश कमांड पैकेज के अनुसार अलग-अलग होते हैं — हर पैकेज की `README.md` पढ़ें।

### एप्लिकेशन पैकेज {#applications}

| पैकेज | भूमिका | यहाँ से शुरू करें |
|---|---|---|
| **AI Workbench** | स्थानीय मॉडल इन्वेंटरी, एम्बेडिंग और इन्फरेंस वर्कफ़्लो के लिए बहु-कमांड CLI; Python हार्नेस सत्यापन | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · साइट: [AI Workbench](/start/examples.html) |
| **ViviLite** | एजेंट समन्वय कमांड के लिए Faber-नेटिव स्थानीय मेलस्पेस CLI (फ़ाइल-आधारित और वैकल्पिक SQLite लेन) | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | समानता हार्नेस के साथ सामान्य यूटिलिटी को फिर से लागू करने वाला बड़ा एप्लिकेशन अभियान | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | GPU / सिस्टम वर्कलोड के स्तर और कॉन्ट्रैक्ट | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | स्क्रिप्टिंग और कर्नेल-उन्मुख डेमो | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | ऑटोमेशन स्केच पैकेज | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | कीवर्ड रीमैपिंग के लिए लोकेल पैक डेमो | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | पैकेज-स्टोर लैब सामग्री | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

### भाषा कॉर्पस {#corpus}

**corpus** ट्री कीवर्ड और कंस्ट्रक्ट का संदर्भ है: हर कंस्ट्रक्ट के लिए एक डायरेक्टरी
और उसमें कई छोटे `.fab` प्रोग्राम। यह इस साइट के जनरेट किए गए [Corpus](/corpus/)
पृष्ठों का स्रोत-सत्य है।

| सतह | URL |
|---|---|
| स्रोत ट्री | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| जनरेट किए गए दस्तावेज़ | [/corpus/](/corpus/) |
| इकोसिस्टम नोट | [Language corpus](/libraries/corpus.html) |

### स्टैंडर्ड लाइब्रेरी भ्रमण {#stdlib}

Norma की मानक-लाइब्रेरी exempla **norma** रिपॉज़िटरी में हैं, `examples/` के अंतर्गत नहीं:

- [faberlang/norma](https://github.com/faberlang/norma) — उपलब्ध होने पर `norma/exempla/`
- साइट: [Norma](/libraries/norma.html)

### सुझाया गया सीखने का क्रम {#order}

1. CLI को [इंस्टॉल](/start/install.html) करें।
2. भाषा की संरचना समझने के लिए [त्वरित भ्रमण](/start/) देखें।
3. जिस भी कीवर्ड को आप नहीं पहचानते, उसके लिए **corpus** पृष्ठ खोलें ([Corpus hub](/corpus/))।
4. एप्लिकेशन की संरचना समझने के लिए **AI Workbench** या **ViviLite** को शुरू से अंत तक पढ़ें।
5. संपादन के दौरान संदर्भ के रूप में [Syntax](/language/) और [Tooling](/toolchain/) का उपयोग करें।

### एजेंट पथ {#agent-path}

- स्किल: [examples](/.well-known/agent-skills/examples/SKILL.md)
- स्किल: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- इंडेक्स: [`/llms.txt`](/llms.txt)

### पिछला {#previous}

| पिछला | अगला |
|---|---|
| [प्रोजेक्ट और उदाहरण](/start/projects.html) | [फ़ीचर](/language/) |

## AI Workbench

AI वर्कबेंच एक Faber CLI एप्लिकेशन है, जो स्थानीय मॉडल इन्वेंटरी, मेटाडेटा निरीक्षण, एम्बेडिंग, इंडेक्सिंग और इन्फ़रेंस वर्कफ़्लो के लिए है। यह दिखाता है कि Faber वास्तविक I/O, JSON आउटपुट और Python हार्नेस वैलिडेशन के साथ एक व्यापक, बहु-कमांड CLI एप्लिकेशन बना सकता है।

### पैकेज {#package}

`examples/ai-workbench/packages/faber-ai/` में CLI सबकमांड:

- `model inspect` — स्थानीय मॉडल उपनाम, रूट और स्थिति पूछें
- `embed` — टेक्स्ट इनपुट से एम्बेडिंग बनाएँ

### कमांड {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

### वैलिडेशन {#validation}

AI वर्कबेंच में 20 से अधिक Python हार्नेस स्क्रिप्ट शामिल हैं, जो मॉडल इन्वेंटरी, इन्फ़रेंस, GPU साक्ष्य, सेशन लाइफ़साइकल और पैकेज पुनःउपयोग के लिए Faber आउटपुट की तुलना फ़िक्स्चर मैप से करती हैं। यह संकलित Faber बाइनरी के क्रॉस-लैंग्वेज वैलिडेशन को प्रदर्शित करता है।

## Coreutils

Faber GNU coreutils को एप्लिकेशन-लेन प्रूफ के रूप में फिर से लागू करता है। ये वास्तविक CLI प्रोग्राम हैं, जो argv, stdio, exit codes और host I/O के साथ काम करने वाले बाइनरी बनाने की Faber की क्षमता प्रदर्शित करते हैं। इन्हें parity harness के माध्यम से host की GNU utilities के विरुद्ध सत्यापित किया गया है।

### लागू की गई utilities {#implemented-utilities}

**चरण 1 — scaffold + true/false**  
`true`, `false`

**चरण 2 — साझा common helpers + inline tests**  
`echo`, `basename`, `dirname`, `printf`, `seq`

**चरण 3 — nullable-stdin slices**  
`cat`, `head`, `tail`, `wc`, `tac`, `uniq`, `fold`, `nl`, `expand`,  
`unexpand`, `sort`, `cut`, `grep`, `tr`, `tee`, `paste`

**Scaffolded — चरण 5+**  
`rm`, `cp`, `mv`, `mkdir`, `touch`, `pwd`, `readlink`, `realpath`,  
`join`, `comm`, `od`, `cksum`, `split`, `yes`, `printenv`

### उदाहरण — echo {#example--echo}

`echo` पैकेज coreutils में पूरे प्रोजेक्ट में उपयोग किए जाने वाले Faber पैटर्न प्रदर्शित करता है: CLI annotations, option parsing, `probandum`/`proba`/`adfirma` के साथ inline tests और साझा common modules:

```faber locale=la
importa ex "norma:consolum" privata consolum

functio echo_textus(lista<textus> words) → textus {
    redde ""
}

functio echo_novam_lineam(lista<textus> words) → bivalens {
    redde falsum
}

probandum "echo formatting" tag "coreutils" {
    proba "empty operands" {
        adfirma echo_textus([]) ≡ ""
    }
    proba "-n suppresses newline" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }
}

@ cli "echo"
@ descriptio "GNU coreutils echo parity exemplum"
@ operandus ceteri textus words
incipit argumenta args {
    # ... CLI logic here
}
```

### चलाना {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
