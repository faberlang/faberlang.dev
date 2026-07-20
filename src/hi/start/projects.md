+++
translation_kind = "translated"

title = "Projects and examples"
section = "projects"
order = 4
sources = []

prose_hash = "sha256:8a914c63394e5bd0bf08ccef737eb95ec4cfb7df1813f3475c78d6ef579fb14d"
code_hash = "sha256:08056868d41c8d2a2925beb910fea8adcf4ac708fa67559e5a160dd900429a06"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
हैलो-वर्ल्ड के बाद वास्तविक पैकेजों की ओर बढ़ें। Faber पैकेज-आधारित है; सीखने का सबसे तेज़ तरीका उन मौजूदा पैकेजों को देखना और पढ़ना है जो उसी कंपाइलर सतह का उपयोग करते हैं जिसे आप इस्तेमाल करने की योजना बना रहे हैं।

## सार्वजनिक रिपॉज़िटरी {#repositories}

| रिपॉज़िटरी | यहाँ से शुरू करें | क्यों |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`, एप्लिकेशन पैकेज, ट्रैक | सार्वजनिक कॉर्पस और एप्लिकेशन उदाहरण |
| [`faberlang/norma`](https://github.com/faberlang/norma) | `norma:*` पैकेज | मानक लाइब्रेरी का स्रोत |
| [`faberlang/faber`](https://github.com/faberlang/faber) | CLI रैपर | उपयोगकर्ता-सामना करने वाला बिल्ड टूल |
| [`faberlang/cista`](https://github.com/faberlang/cista) | पैकेज-स्टोर CLI/लाइब्रेरी | पैकेज प्रबंधन सतह |
| [`faberlang/triga`](https://github.com/faberlang/triga) | `triga:*` स्रोत | ग्राफ़िक्स और ज्यामिति लाइब्रेरी |

## सीखने का वर्कस्पेस क्लोन करें {#clone-workspace}

```bash
mkdir faber-learning
cd faber-learning
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

`norma:*` इम्पोर्ट वाले पैकेज `faber.lock` में दर्ज Cista पैकेज स्टोर से निर्भरताएँ हल करते हैं। `FABER_LIBRARY_HOME` का उपयोग केवल तब करें जब आप जानबूझकर लाइब्रेरी डेवलपमेंट के लिए स्थानीय रिज़ॉल्वर ओवरराइड चाहते हों।

## उदाहरण इस क्रम में पढ़ें {#read-order}

1. [त्वरित परिचय](/start/) में सतही व्याकरण देखें।
2. [Hello, Faber](/start/hello.html) में एकल पैकेज देखें।
3. [कॉर्पस](/corpus/) में प्रत्येक कीवर्ड या कंस्ट्रक्ट के लिए एक पृष्ठ देखें।
4. बड़े एप्लिकेशन के लिए [उदाहरण](/start/examples.html) देखें।
5. CLI विवरण के लिए [Faber बिल्ड टूल](/tooling/faber-build-tool.html) देखें।

## एजेंट वर्कफ़्लो {#agent-workflow}

एजेंटों को केवल गद्य से सिंटैक्स का अनुमान नहीं लगाना चाहिए। मशीन सतहों का उपयोग करें और फिर जनरेट किए गए कोड को मान्य करें:

```bash
curl -fsSL https://faberlang.dev/llms.txt
faber check path/to/package
```

पैकेज कार्य के लिए रिपोर्ट में रिपॉज़िटरी, पैकेज पथ, कमांड और डायग्नोस्टिक कोड का उल्लेख करें। यदि आप इस साइट में फ़ेंस किए गए Faber कोड वाले दस्तावेज़ों को छूते हैं, तो यह दावा करने से पहले फ़ेंस वैलिडेटर चलाएँ कि उदाहरण अब भी कंपाइल होते हैं।

## स्टार्ट ट्रैक के बाद क्या आता है {#after-start}

| लक्ष्य | पढ़ें |
|---|---|
| सिंटैक्स सीखें | [सिंटैक्स](/syntax/) |
| लोकेल समझें | [रीडर लोकेल](/features/reader-locale.html) |
| कंपाइलर का उपयोग करें | [Faber बिल्ड टूल](/tooling/faber-build-tool.html) और [Radix कंपाइलर](/tooling/radix-compiler.html) |
| कंस्ट्रक्ट ब्राउज़ करें | [कॉर्पस](/corpus/) |
| लाइब्रेरी के साथ बिल्ड करें | [इकोसिस्टम](/ecosystem/) |

## अगला {#next}

| पिछला | अगला |
|---|---|
| [आपके द्वारा उपयोग किए जाने वाले कमांड](/start/commands.html) | [उदाहरण](/start/examples.html) |
