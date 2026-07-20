+++
translation_kind = "translated"

title = "Design documents"
section = "references"
order = 2
sources = [
  "radix/docs/design/README.md",
]


prose_hash = "sha256:c668ff445d22132defdedd2c1535366f6ce81513e0ae589bd1ab450683a06c3f"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
Radix रिपॉज़िटरी में Faber भाषा और कंपाइलर के रूप में कैसे काम करता है, इसके आधिकारिक डिज़ाइन दस्तावेज़ मौजूद हैं। ये `radix/docs/design/` के अंतर्गत हैं।

## इंडेक्स {#index}

| क्षेत्र | फ़ाइलें |
|------|-------|
| टार्गेट और लोअरिंग | `target-capability-matrix.md`, `lowering-routes.md`, `semantic-ownership.md` |
| प्रकार और शुगर | `numeric-type-sugar.md`, `comparison-operators.md`, `annotation-sugar.md` |
| कलेक्शन इंट्रिंसिक्स | `lista-intrinsics.md`, `tabula-intrinsics.md`, `tensor-intrinsics.md`, `numerus-intrinsics.md`, `fractus-intrinsics.md`, `textus-intrinsics.md`, `intervallum-intrinsics.md`, `instans-intrinsics.md`, `copia-intrinsics.md` |
| कन्वर्ज़न | `conversio-valor.md`, `failable-conversio.md` |
| फ़्रेम और इफ़ेक्ट | `frame-stream-types.md`, `host-provider-gateway.md` |
| रीडर और फ़ॉर्मैट | `reader-locale.md`, `faber-canonical-surface.md` |
| सिस्टम / AIR | `air-dialect.md`, `aiml-foundation.md`, `systems-shaped-values.md` |
| टूलिंग सतह | `faber-scripting.md` |
| नामकरण संबंधी ऋण | `mixed-case-naming-debt.md` |

## स्टैंडर्ड लाइब्रेरी डिज़ाइन दस्तावेज़ {#stdlib-design-docs}

`radix/docs/stdlib/` डायरेक्टरी में ये दस्तावेज़ हैं:

| दस्तावेज़ | भूमिका |
|-----|------|
| `morphologia.md` | सभी स्टैंडर्ड लाइब्रेरी मेथड नामों के लिए रूप-परिवर्तन नीति |
| `tensor-methods.md` | Tensor रिसीवर मेथड संदर्भ |
| `chorda-methods.md` | Chorda (टेक्स्ट) मेथड संदर्भ |
| `mathesis-methods.md` | गणितीय मेथड संदर्भ |
| `tempus-methods.md` | समय संबंधी मेथड संदर्भ |
| `stdlib-mechanical-verbs.md` | `pange`/`solve`/`tempta` त्रयी की नीति |
