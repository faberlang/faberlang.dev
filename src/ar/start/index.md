+++
translation_kind = "translated"

title = "Quick tour"
section = "start"
order = 0
sources = []

prose_hash = "sha256:fb6f791ae0e9b73d0c92c2127726f558a2b845351779f80217616b8f55629ff0"
code_hash = "sha256:f9eb22ab8a2408fe0076d846dd4266cff4ded675ad8d63a5b2d9ee59c3e0156f"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
خمس دقائق لشكل Faber: ثبّت CLI، اقرأ دالة واحدة، ثم افتح حزمة حقيقية. لمسار متسلسل، اتبع: [تثبيت](/start/install.html) →
[مرحباً](/start/hello.html) → [الأوامر](/start/commands.html) →
[المشاريع](/start/projects.html).

## ١. ثبّت CLI {#install}

نزّل الإصدار الحالي (**1.1.1**) لمنصتك من
[صفحة التثبيت](/start/install.html)، تحقق من بصمة الأرشيف، وضع
الملف الثنائي `faber-v1.1.1-<target-triple>/faber` المستخرج على `PATH` لديك. تأكد:

```bash
faber --version
```

## ٢. شكل الدالة {#shape}

وسائط النوع أولاً، نوع الإرجاع بالرمز، كلمات تحكم لاتينية، اتحاد
قابل للعدم:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

| إشارة | معنى |
|---|---|
| `functio` | تعريف دالة |
| `numerus a` | النوع أولاً، ثم الاسم |
| `→` | نوع الإرجاع |
| `∪ nihil` | قابل للعدم (`T ∪ nihil`) |
| `si … ∴` | تفرع مضغوط |
| `redde` | إرجاع |

## ٣. تخطيط الحزمة {#package}

الحزمة هي مجلد فيه `faber.toml` و `src/`:

```text
my-app/
  faber.toml
  src/
    main.fab
```

الأوامر النموذجية:

```bash
faber check my-app/
faber build my-app/ -t rust
faber run my-app/
faber test my-app/
```

تفاصيل: [أداة بناء Faber](/tooling/faber-build-tool.html).

## ٤. تطبيقات حقيقية {#applications}

لا تتوقف عند hello-world. مستودع **الأمثلة** العام يحتوي على CLI متعدد الأوامر،
مساحة بريد محلية، سجلات أعباء GPU، ومجموعة لغة كاملة.

| حزمة | ما تعرضه |
|---|---|
| منصة عمل AI | CLI متعدد الأوامر، فحص النماذج، تضمينات |
| ViviLite | مساحة بريد مدعومة بملفات / CLI تنسيق الوكلاء |
| coreutils | حملة تطبيق أكبر (أدوات مضاهاة) |
| gpu-workload | أنظمة / درجات GPU |
| corpus | مجلد واحد لكل بناء لغوي |

استعرضها في [صفحة الأمثلة](/start/examples.html).

## ٥. إذا كنت وكيلاً {#agents}

1. اقرأ [`/llms.txt`](/llms.txt).
2. افتح [`/agents/index.md`](/agents/index.md).
3. اختر مهارة من [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json).

## مسار البداية {#start-track}

| خطوة | صفحة | النتيجة |
|---|---|---|
| ١ | [تثبيت وتنزيل](/start/install.html) | ضع Faber 1.1.1 على `PATH` وتحقق منه |
| ٢ | [مرحباً، Faber](/start/hello.html) | أنشئ وشغّل `salve-munde` |
| ٣ | [أوامر ستستخدمها](/start/commands.html) | تعلم `check`، `build`، `run`، `test`، `explain` |
| ٤ | [مشاريع وأمثلة](/start/projects.html) | انتقل إلى حزم حقيقية وصفحات المجموعة |

## التالي {#next}

| موضوع | رابط |
|---|---|
| تثبيت وتنزيل | [تثبيت](/start/install.html) |
| مرحباً، Faber | [مرحباً](/start/hello.html) |
| الأوامر | [أوامر](/start/commands.html) |
| المشاريع | [مشاريع](/start/projects.html) |
| مرجع الصياغة | [الصياغة](/syntax/) |
| ميزات (مواضع، مسارات) | [ميزات](/features/) |
| مكتبات النظام البيئي | [نظام بيئي](/ecosystem/) |
| مجموعة الكلمات المفتاحية | [مجموعة](/corpus/) |
