+++
translation_kind = "translated"

title = "String and template literals"
section = "syntax"
order = 8
sources = [
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "examples/corpus/literalia/",
  "examples/corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
]


prose_hash = "sha256:61bc93552e4a6ccc2a3a51453c146c31eee8331c6e82a3b17de5bc70f4ce24b0"
code_hash = "sha256:e7cba6e75a702466f92ecdbaa2c9d777b027a09a7f1b0414387cc746376d3075"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber में सीमाचिह्नों के अर्थ निश्चित होते हैं — हर उद्धरण-रूप स्रोत की अलग संरचना दर्शाता है। ये एक-दूसरे के पर्याय नहीं हैं।

## शाब्दिक रूप {#literal-forms}

| रूप | प्रकार | भूमिका |
|------|------|------|
| `'…'` | `ascii` | स्थिर मशीन टोकन; इसमें `§` नहीं होता और `(…)` का उपयोग नहीं होता |
| `"…"` | `textus` | छोटी Unicode पंक्ति-स्ट्रिंग; `(…)` का रेंडर होता है |
| `«…»` | `textus` | ब्लॉक/बहुपंक्ति Unicode; `(…)` का रेंडर होता है |
| `` `…` `` | `forma` | कैप्चर किए गए टेम्पलेट; `(…)` कैप्चर करता है |
| `{ … }` | `json` | संकलन-समय JSON दस्तावेज़ |
| `|…|` | `octeti` | संकलन-समय हेक्स बाइट्स |
| `[ … ]` | `lista<T>` | Faber सूची लिटरल |

## स्ट्रिंग-टेम्पलेट अनुप्रयोग {#string-template-application}

Faber स्ट्रिंग-टेम्पलेट अनुप्रयोग से पाठ को फ़ॉर्मैट करता है: पहले `"…"` या `«…»` लिटरल में `§` रिक्त-स्थान होते हैं, फिर कोष्ठक में तर्क दिए जाते हैं:

```faber
functio greet(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}

fixum numerus pagina ← 3
fixum numerus totum ← 10
fixum textus code ← "200"
fixum textus label ← "OK"

fixum _ msg ← "Page § of §"(pagina, totum)
fixum _ block ← «status: § (§)»(code, label)
```

मुख्य नियम:

- `§` (U+00A7) टेम्पलेट रिक्त-स्थान है
- स्थितीय रिक्त-स्थान: स्पष्ट क्रम के लिए `§0`, `§1`, … का उपयोग करें
- अंतिम `!` प्रदर्शन फ़ॉर्मैटिंग चुनता है: `"Salve, §!"(nomen)`
- `(args)` प्रत्यय टेम्पलेट अनुप्रयोग है, फ़ंक्शन कॉल नहीं

## ब्लॉक स्ट्रिंग {#block-strings}

बहुपंक्ति ब्लॉक गिलेमे `«…»` का उपयोग करते हैं:

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

## कैप्चर किए गए टेम्पलेट (`forma`) {#captured-templates}

बैकटिक टेम्पलेट पाठ और पैरामीटर को रेंडर किए बिना कैप्चर करते हैं।
बाउंड SQL/URL पेलोड के लिए ये सुरक्षित हैं:

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

## इनलाइन JSON {#inline-json}

सादा `{ … }` इनलाइन JSON है: यह संकलन-समय का `json` दस्तावेज़ है, अनाम Faber ऑब्जेक्ट नहीं। कुंजियाँ उद्धृत स्ट्रिंग होती हैं और `:` से अलग की जाती हैं:

```faber
fixum _ empty ← {}
fixum _ user ← { "name": "Marcus", "age": 30, "active": true }
fixum _ nested ← { "meta": { "version": 1 }, "tags": ["alpha", "beta"] }
```

टाइप किए गए `genus` निर्माण के लिए, प्रकार का नाम और `=` फ़ील्ड संरचना का उपयोग करें:

```faber
genus Point {
    numerus x
    numerus y
}
fixum _ p ← Point { x = 10, y = 20 }
```
