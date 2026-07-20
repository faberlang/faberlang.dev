+++
translation_kind = "translated"

title = "AI Workbench"
section = "ecosystem"
order = 4
sources = [
  "examples/ai-workbench/ (README.md, package, harness)",
]


prose_hash = "sha256:3a8940d1ee168b9bdf75f40f70ce5e5eb6b6446f47510df9c3511b2d4d1bef33"
code_hash = "sha256:dc8f04249d6a95c65b63ba0ccd58c402d6f8ed47a96bc15da4b6ad844922d007"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
محطة عمل الذكاء الاصطناعي هي تطبيق Faber للطرفية لإدارة مخزون النماذج المحلية،
وفحص البيانات الوصفية، والتضمين، والفهرسة، وسير عمل الاستدلال. وهي توضح
بناء Faber لتطبيق طرفية متعدد الأوامر وجوهري، مع إدخال وإخراج حقيقيين،
ومخرجات JSON، وتحقق بوساطة برامج Python المساعدة.

## الحزمة {#package}

`examples/ai-workbench/packages/faber-ai/` مع أوامر طرفية فرعية:

- `model inspect` — استعلام عن أسماء النماذج المحلية المستعارة ومساراتها وحالتها
- `embed` — توليد تضمينات من مُدخل نصي

## الأوامر {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

## التحقق {#validation}

تشمل محطة عمل الذكاء الاصطناعي أكثر من 20 برنامجًا مساعدًا بلغة Python تقارن
مخرجات Faber بخرائط مرجعية لمخزون النماذج، والاستدلال، وأدلة GPU، ودورة حياة
الجلسة، وإعادة استخدام الحزمة — مما يوضح التحقق عبر اللغات من ثنائيات Faber المُصرَّفة.
