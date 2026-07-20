+++
translation_kind = "translated"

title = "Language corpus"
section = "ecosystem"
order = 6
sources = [
  "examples/corpus/ (292 .fab files, 174 registry terms, index.toml)",
  "examples/corpus/README.md",
]


prose_hash = "sha256:6dab4295fafeea620e65bd30edcc6c810bc3f0b11cb8681aae63f79ecbe2be63"
code_hash = "sha256:fbdcbf8ce9cd3fdcb367022a7df1cdbd74fd62244d662a6a85229773e4910739"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
مدونة لغة Faber هي قاموس اللغة العام: دليل واحد من المستوى الأعلى لكل كلمة مفتاحية، أو مجموعة عوامل، أو سطح نوع لغوي. وهي المصدر التطويري لأمر `faber explain` والمدخل الأساسي لمصفوفات الترجمة متعددة الأهداف.

## إحصائيات {#stats}

- 292 ملفًا نموذجيًا بامتداد `.fab`
- 174 مصطلحًا مسجلًا في `index.toml`
- قرابة 135 دليلًا للكلمات المفتاحية والمفاهيم

## التخطيط {#layout}

```
corpus/
  functio/           # function keyword exemplars
  genus/             # record type exemplars
  si/                # conditional branch exemplars
  itera/             # iteration exemplars
  lista/ tabula/     # collection type exemplars
  tensor/ sparsa/    # tensor exemplars
  ad/                # capability call exemplars
  operatores/        # glyph / operator groups
  ...
  index.toml         # generated explain manifest
```

## تنسيق الملف {#file-format}

يبدأ كل ملف `.fab` بمقدمة TOML تصف المصطلح:

```toml
+++
term = "functio"
kind = "keyword"
category = "function"
canonical = true
summary = "Declares a named function or method."
syntax = "functio <name>(<params>) [modifiers] [→ <type>] [⇥ <error-type>] <block>"
aliases = ["function"]
related = ["→", "⇥", "redde", "sponte"]
+++

functio saluta() {
    nota "Salve, Mundus!"
}
```

## الاستخدام {#usage}

```bash
faber explain functio       # show keyword reference
faber explain ≡             # show glyph reference
faber explain --search query # search across corpus
faber explain --list         # list all terms
```

## الفئات {#categories}

تُنظَّم المصطلحات حسب الفئة: `function`، `control-flow`، `type`، `collection`، `transfer`، `annotation`، `iteration`، `destructuring`، `testing`، `cli`، `concept`، `operator-group`، `existing-home`.
