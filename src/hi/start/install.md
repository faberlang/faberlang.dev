+++
translation_kind = "translated"

title = "Install and download"
section = "install"
order = 1
sources = []

prose_hash = "sha256:662becbb3dd5349058bcdfec9219fd07f6fe4217c2e5115c0aade45e0f17f0d4"
code_hash = "sha256:cc9de43077b1262ee3d9edfbd3bd56c4ae51bcca18d0316fa0bb95312f3033b7"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
वर्तमान प्रीबिल्ट रिलीज़ से **Faber** CLI इंस्टॉल करें। कंपाइलर का फ्रंट एंड `faber` बाइनरी के अंदर शामिल है; सामान्य पैकेज कार्य के लिए आपको अलग से Radix इंस्टॉल करने की आवश्यकता नहीं है।

यह पृष्ठ Faber 1.1.1 के रिपॉज़िटरी रिलीज़ आर्टिफैक्ट पर आधारित है। पैकेज मैनेजर के फ़ॉर्मूले रिपॉज़िटरी रिलीज़ से पीछे रह सकते हैं; यदि Homebrew या कोई अन्य मैनेजर Radix/Faber का पुराना संस्करण दिखाता है, तो इस ट्रैक के लिए नीचे दिए गए आर्काइव को प्राथमिकता दें।

## वर्तमान रिलीज़ {#current-release}

| फ़ील्ड | मान |
|---|---|
| **संस्करण** | 1.1.1 |
| **टैग** | `faber-v1.1.1` |
| **रिलीज़ पृष्ठ** | GitHub पर [faber-v1.1.1](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1) |
| **सभी रिलीज़** | [साइट रिलीज़ इन्वेंटरी](/history/releases.html) |
| **लाइसेंस** | MIT |

## प्रीबिल्ट आर्काइव {#archives}

| प्लेटफ़ॉर्म | डाउनलोड | SHA-256 |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [चेकसम](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [चेकसम](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

आर्काइव `faber-v1.1.1-<target-triple>/faber` में एक्सट्रैक्ट होते हैं। चेकसम फ़ाइलों में मूल बिल्ड पथ दिया हो सकता है, इसलिए `sha256sum -c` के पथ मिलान पर निर्भर रहने के बजाय पहले हैश फ़ील्ड की स्थानीय आर्काइव से तुलना करके सत्यापित करें।

### macOS arm64 {#macos}

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
# place on PATH, e.g.:
sudo mv faber-v1.1.1-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

### Linux x64 {#linux}

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(sha256sum faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv faber-v1.1.1-x86_64-unknown-linux-gnu/faber /usr/local/bin/
faber --version
```

## सत्यापन {#verify}

```bash
faber --version
faber explain SEM001
```

आपको CLI के लिए एक संस्करण पंक्ति और डायग्नोस्टिक व्याख्या दिखाई देनी चाहिए। यदि `faber` नहीं मिलता है, तो जाँचें कि बाइनरी वाली निर्देशिका `PATH` में शामिल है।

## पहला पैकेज चेक {#first-package}

CLI को `PATH` में उपलब्ध कराने के बाद, सार्वजनिक उदाहरणों (या किसी भी Faber पैकेज) को क्लोन करें और उसका टाइप-चेक करें। प्रोडक्ट पैकेज `faber.lock` के माध्यम से Cista स्टोर से निर्भरताएँ हल करते हैं; स्थानीय सोर्स चेकआउट केवल स्पष्ट लाइब्रेरी-विकास ओवरराइड के लिए होते हैं।

```bash
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

अधिक पैकेज: [उदाहरण](/start/examples.html)। CLI सतह:
[Faber बिल्ड टूल](/tooling/faber-build-tool.html)।

## Homebrew स्थिति {#homebrew}

इस स्टार्ट ट्रैक के लिए Homebrew प्रकाशन अभी प्राधिकृत स्रोत नहीं है। यदि कोई फ़ॉर्मूला Radix 0.38.0 जैसे पुराने कंपाइलर की सेवा देता है, जबकि यह साइट Faber 1.1.1 का दस्तावेज़ देती है, तो फ़ॉर्मूले को पीछे चल रहा मानें और प्रीबिल्ट रिलीज़ आर्काइव का उपयोग करें। इस पृष्ठ के लिए कंटेनर सत्यापन गेट तब तक अवशिष्ट रहेगा, जब तक फ़ॉर्मूला प्रकाशन अद्यतन नहीं हो जाता।

## सोर्स से बिल्ड करें {#from-source}

एजेंटों और अधिकांश डेवलपरों के लिए प्रीबिल्ट अनुशंसित मार्ग हैं। सोर्स से बिल्ड करने के लिए निजी Radix कंपाइलर ट्री आवश्यक है और यह इस पृष्ठ के दायरे से बाहर है। जब तक आप स्वयं कंपाइलर पर काम न कर रहे हों, ऊपर दिए गए आर्काइव का उपयोग करें।

## एजेंट मार्ग {#agent-path}

एजेंटों को इस HTML को स्क्रैप करने के बजाय **इंस्टॉल** स्किल और एजेंट इंडेक्स लोड करना चाहिए:

- [`/llms.txt`](/llms.txt)
- [इंस्टॉल स्किल](/.well-known/agent-skills/install/SKILL.md)
- [एजेंट गाइड](/agents/index.md)

## अगला चरण {#next}

| पिछला | अगला |
|---|---|
| [त्वरित परिचय](/start/) | [नमस्कार, Faber](/start/hello.html) |
