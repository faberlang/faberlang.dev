+++
translation_kind = "translated"

title = "Hello, Faber"
section = "hello"
order = 2
sources = []

prose_hash = "sha256:3a78129bf3787f7c726e39104c95fe9bde78855c4a9f63650410c5cef9610067"
code_hash = "sha256:1ee50be729b09d1bfba27a1f994ef4d1a47c73a645764f9d5986c9bab1aecfb8"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
सबसे छोटा उपयोगी Faber प्रोग्राम लिखें: एक पैकेज का प्रवेश बिंदु, जो किसी स्ट्रिंग को फ़ॉर्मैट करके उसे प्रिंट करता है।

## पूर्वापेक्षाएँ {#prerequisites}

पहले [इंस्टॉल और डाउनलोड](/start/install.html) पूरा करें। आपके `PATH` में `faber` बाइनरी होनी चाहिए और आप ऐसी कार्यशील डायरेक्टरी में शेल चला रहे हों जहाँ फ़ाइलें बना सकें।

## पैकेज बनाएँ {#create-package}

```bash
mkdir salve-munde
cd salve-munde
mkdir src
cat > faber.toml <<'EOF'
[package]
name = "salve-munde"
version = "0.1.0"
EOF
cat > src/main.fab <<'EOF'
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
EOF
```

## जाँचें {#check}

```bash
faber check .
```

`faber check` फ़्रंट एंड चलाता है: लेक्सिंग, पार्सिंग, प्रकार-जाँच और इतना लोअरिंग कि सामान्य पैकेज संबंधी गलतियाँ बिना नेटिव बाइनरी बनाए पकड़ी जा सकें। यदि कमांड विफल हो, तो पहले डायग्नॉस्टिक कोड पढ़ें; Faber डायग्नॉस्टिक्स को स्थिर खोज-संकेत के रूप में उपयोग करने के लिए बनाया गया है।

## चलाएँ {#run}

```bash
faber run .
```

अपेक्षित आउटपुट:

```text
Salve, munde!
```

## आपने अभी क्या उपयोग किया {#what-you-used}

| स्रोत | अर्थ |
|---|---|
| `functio salve(textus nomen) → textus` | `salve` नाम का फ़ंक्शन, प्रकार-प्रथम पैरामीटर और टेक्स्ट रिटर्न |
| `fixum textus msg ← ...` | अपरिवर्तनीय बाइंडिंग |
| `"Salve, §!"(nomen)` | डिस्प्ले इंटरपोलेशन वाली फ़ॉर्मैट स्ट्रिंग |
| `redde msg` | रिटर्न |
| `incipit` | पैकेज का प्रवेश बिंदु |
| `nota m` | नोट/आउटपुट मान प्रिंट करना |

## लोकेल प्रमाण {#locale-proof}

ऊपर दिया गया प्रोग्राम कैनोनिकल लैटिन रीडर रेंडरिंग है। रीडर लोकेल समान अर्थ वाले प्रोग्राम को अलग-अलग कीवर्ड पैक के साथ रेंडर कर सकते हैं, जबकि ग्लिफ़ और आइडेंटिफ़ायर सुरक्षित रहते हैं। गैर-लैटिन पैकेज लिखने से पहले [रीडर लोकेल](/features/reader-locale.html) में पूरा प्रमाण देखें।

## अगला कदम {#next}

| पिछला | अगला |
|---|---|
| [इंस्टॉल और डाउनलोड](/start/install.html) | [वे कमांड जिनका आप उपयोग करेंगे](/start/commands.html) |
