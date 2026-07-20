+++
translation_kind = "translated"

title = "Tooling and compiler"
section = "tooling"
order = 0
sources = []


prose_hash = "sha256:23ae82d266e39d96b2059d2b97d4b03c5e6efcba389ab0bfb621d32a2e7caad2"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Faber टूलचेन में तीन टूल शामिल हैं: बिल्ड और परीक्षण के लिए `faber` CLI, कोड जनरेशन के लिए Radix कंपाइलर, और निर्भरता समाधान के लिए Cista पैकेज मैनेजर।

## Faber बिल्ड टूल {#faber-cli}

प्राथमिक डेवलपर इंटरफ़ेस। बिल्ड, जाँच, रन, परीक्षण, फ़ॉर्मैट और व्याख्या — सब कुछ एक ही कमांड से। [और पढ़ें →](/tooling/faber-build-tool.html)

## Radix कंपाइलर {#radix}

कंपाइलर बैकएंड। Faber सोर्स को HIR → MIR → AIR के माध्यम से कई टार्गेट लेन में निम्नीकृत करता है। [और पढ़ें →](/tooling/radix-compiler.html)

## Cista पैकेज मैनेजर {#cista}

पैकेज समाधान और सार्वजनिक पैकेज स्टोर। `faber.toml` मैनिफ़ेस्ट और निर्भरता लॉक को प्रबंधित करता है। [और पढ़ें →](/tooling/cista-package-manager.html)

## कोड जनरेशन टार्गेट {#codegen-targets}

Faber, डिफ़ॉल्ट रूप से Rust, तथा WASM, TypeScript, Go और GPU/WGSL में कंपाइल होता है। प्रत्येक टार्गेट लेन का अपना IR पथ और रनटाइम बाइंडिंग होती है। [और पढ़ें →](/tooling/codegen-targets.html)

## प्रदर्शन {#performance}

विभिन्न टार्गेट लेनों पर मापा गया कंपाइलेशन और निष्पादन प्रदर्शन। [और पढ़ें →](/tooling/performance.html)

## स्क्रिप्टिंग {#scripting}

`faber run` कमांड के साथ Faber को स्क्रिप्टिंग भाषा के रूप में उपयोग करना। [और पढ़ें →](/tooling/scripting.html)
