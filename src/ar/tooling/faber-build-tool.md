+++
translation_kind = "translated"

title = "Faber build tool"
section = "tooling"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
]


prose_hash = "sha256:5d8304941413ba003c019f0b1c43cd19e99ad0f25fa9b7a4ffadbc1327e8dfb6"
code_hash = "sha256:7657ec817fefbfb88c20a7b862970c668ebe2835de88c17eda584340fd2d6654"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
أداة `faber` CLI هي المدخل الأساسي لبناء شيفرة Faber وفحصها وتشغيلها
وتنسيقها واختبارها. تغلّف مترجم Radix في أداة تطوير سهلة الاستخدام.

## الأوامر الأساسية {#core-commands}

| الأمر | الغرض |
|---|---|
| `faber build <path>` | ترجمة حزمة إلى واجهة خلفية مستهدفة (الافتراضي: Rust) |
| `faber check <path>` | التحقق من الأنواع دون إصدار شيفرة |
| `faber run <path>` | بناء وتنفيذ |
| `faber test <path>` | تشغيل مجموعات اختبار proba |
| `faber format <path>` | تطبيق التنسيق المعياري |
| `faber explain <code>` | شرح رمز تشخيصي |
| `faber emit <path>` | إصدار المصدر بصيغة سطح مستهدف |

## بناء حزمة {#building}

```text
faber build my-package/ -t rust
```

العلامة `-t` تختار هدف توليد الشيفرة. الأهداف المدعومة تشمل `rust`
(الافتراضي) و `wasm` و `typescript` و `go`.

## التحقق بدون إصدار {#checking}

```text
faber check my-package/
```

تشغيل الواجهة الأمامية كاملة (تحليل معجمي ← تحليل نحوي ← التحقق من الأنواع ← خفض إلى MIR)
دون إنتاج مخرجات. يُستخدم هذا في CI وفي إضافات المحررات.

## تشغيل الاختبارات {#testing-command}

```text
faber test my-package/
```

ترجمة جميع مجموعات `probandum` في الحزمة إلى دوال `#[test]` في Rust
وتشغيلها عبر Cargo. تعيش الاختبارات المضمنة إلى جانب الشيفرة المصدرية —
لا حاجة لثنائي اختبار منفصل.

## التنسيق {#formatting}

```text
faber format my-package/
```

تطبيق منسّق Faber المعياري. يفرض المنسّق تخطيطًا متسقًا:
إعلان واحد لكل سطر، وتباعد معياري، وسطوح كلمات مفتاحية موحّدة.

## شرح التشخيصات {#explaining}

```text
faber explain SEM001
```

طباعة شرح مقروء لأي رمز تشخيصي يمكن للمترجم إصداره.
مفيد لتعلّم معنى الخطأ وكيفية إصلاحه.
