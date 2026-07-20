+++
translation_kind = "translated"

title = "Commands you will use"
section = "commands"
order = 3
sources = []

prose_hash = "sha256:0e56e02cfc5bc616178712a8ff6e3d914b95257913dbd22db2e8e8aac3c0e72e"
code_hash = "sha256:adf615632f084c7edf7f1f0dfc205ee4912e8b497b19c9c96167bf9b97e443cc"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
هذه الصفحة هي الخريطة العملية لواجهة الأوامر لأسبوع العمل الأول مع Faber. استخدمها
كفهرس أوامر، ثم افتح صفحة [أداة بناء Faber](/tooling/faber-build-tool.html)
التفصيلية عندما تحتاج إلى الأعلام وتفاصيل مسار المترجم.

## الحلقة اليومية {#daily-loop}

| الأمر | استخدمه من أجل |
|---|---|
| `faber check <package>` | تحقق سريع للواجهة الأمامية: التحليل المعجمي، التحليل النحوي، فحص الأنواع، التخفيض |
| `faber build <package> -t rust` | إصدار مشروع Rust للمراجعة أو الترجمة الأصلية |
| `faber run <package>` | بناء وتنفيذ حزمة تطبيقية |
| `faber test <package>` | تشغيل اختبارات الحزمة عندما تعرّف الحزمة أسطح اختبار |
| `faber explain <code>` | قراءة شرح تشخيصي مستقر |

ابدأ بـ `check`. هو أرخص أمر والأمر الذي يجب على الوكلاء تشغيله
قبل اقتراح كود مولّد على أنه Faber صالح.

## التحقق {#check}

```bash
faber check .
faber check examples/ai-workbench/packages/faber-ai
```

التحقق الناجح يعني أن الحزمة مقبولة نحوياً ودلالياً
من قبل الواجهة الأمامية للمترجم. لا يعني أن سلسلة الأدوات الأصلية النهائية قد تم
استدعاؤها.

## البناء {#build}

```bash
faber build . -t rust
```

هدف Rust قابل للمراجعة عن قصد. Rust المُولّد هو ناتج
مترجم، وليس مصدر الحقيقة؛ حرر حزمة Faber وأعد البناء بدلاً من
ترقيع Rust المُصدر يدوياً.

## التنفيذ {#run}

```bash
faber run .
```

استخدم `run` للحزم التطبيقية التي تحتوي على نقطة دخول `incipit`. الحزم
المكتبية فقط يجب التحقق منها واختبارها بدلاً من ذلك.

## شرح التشخيصات {#explain}

```bash
faber explain SEM001
faber explain LEX006
```

عائلات التشخيص هي مقابض مستقرة: `LEX` للأخطاء المعجمية، `PAR` لأخطاء
المحلل النحوي، `SEM` للأخطاء الدلالية/النوعية. في الوثائق وتقارير الوكلاء، استشهد
برمز التشخيص بدلاً من إعادة صياغة فشل المترجم بشكل فضفاض.

## أوامر لغة القارئ {#reader-locale}

```bash
faber format --reader-locale=la path/to/file.fab
faber format --reader-locale=th-TH path/to/file.fab
faber emit -t faber --reader-locale=zh-Hans path/to/file.fab
```

مخرجات لغة القارئ هي عرض للنموذج الدلالي للمترجم، وليست
طبقة ترجمة في وقت المتصفح. عمل اللغة يأتي بعد أن تتحقق الحزمة
بالصيغة القانونية.

## التالي {#next}

| السابق | التالي |
|---|---|
| [مرحباً، Faber](/start/hello.html) | [المشاريع والأمثلة](/start/projects.html) |
