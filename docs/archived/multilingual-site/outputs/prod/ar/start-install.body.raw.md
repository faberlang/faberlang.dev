ثبّت واجهة أوامر **Faber** من الإصدار المُجمّع مسبقًا الحالي. تأتي
واجهة المُصرّف الأمامية داخل ثنائيّة `faber`؛ لا تحتاج تثبيت Radix منفصلًا
لأعمال الحزم العادية.

كُتبت هذه الصفحة مقابل قطع الإصدار المُجمّعة لمستودع Faber 1.1.1. قد تتأخّر
صيغ مديري الحزم عن إصدار المستودع؛ لو أبلغ Homebrew أو مدير آخر عن إصدار
Radix/Faber أقدم، ففضِّل الأرشيفات أدناه لهذا المسار.

## الإصدار الحالي {#current-release}

| الحقل | القيمة |
|---|---|
| **الإصدار** | 1.1.1 |
| **الوسم** | `faber-v1.1.1` |
| **صفحة الإصدار** | [faber-v1.1.1 على GitHub](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1) |
| **كل الإصدارات** | [جرد إصدارات الموقع](/history/releases.html) |
| **الترخيص** | MIT |

## الأرشيفات المُجمّعة مسبقًا {#archives}

| المنصّة | التحميل | SHA-256 |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [المجموع الاختباري](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [المجموع الاختباري](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

تُستخرج الأرشيفات إلى `faber-v1.1.1-<target-triple>/faber`. قد تُسمّي ملفات
المجاميع الاختباريّة مسار البناء الأصلي، لذا تحقّق بمقارنة حقل التلبيدة الأول
مقابل الأرشيف المحلّي بدل الاعتماد على مطابقة مسار `sha256sum -c`.

### macOS arm64 {#macos}

<<<FENCE 0>>>

### Linux x64 {#linux}

<<<FENCE 1>>>

## التحقّق {#verify}

<<<FENCE 2>>>

ينبغي أن ترى سطر إصدار لواجهة الأوامر وشرحًا تشخيصيًا. لو لم يُعثَر على
`faber`، فتأكّد من أن الدليل الذي يحوي الثنائيّة موجود ضمن `PATH`.

## أوّل فحص حزمة {#first-package}

بواجهة الأوامر على `PATH`، استنسخ الأمثلة العامة (أو أي حزمة Faber)
وافحص الأنواع. تحلّ حزم المنتج التبعيات من مخزن Cista عبر `faber.lock`؛
نُسخ المصدر المحلّية المفحوصة مخصّصة فقط لتجاوزات تطوير المكتبات
الصريحة.

<<<FENCE 3>>>

مزيد من الحزم: [أمثلة](/start/examples.html). سطح واجهة الأوامر:
[أداة بناء Faber](/tooling/faber-build-tool.html).

## حالة Homebrew {#homebrew}

نشر Homebrew ليس المرجعية لهذا المسار الابتدائي بعد. لو قدّمت صيغة
مُصرّفًا أقدم مثل Radix 0.38.0 بينما يوثّق هذا الموقع Faber 1.1.1،
فعامل الصيغة كمُتأخّرة واستعمل أرشيف الإصدار المُجمّع مسبقًا. تبقى
بوابة التحقّق بالحاوية لهذه الصفحة متبقّية حتى تلحق الصيغة بالنشر.

## البناء من المصدر {#from-source}

البنى المُجمّعة مسبقًا هي المسار المُوصى به للوكلاء ولمعظم المطوّرين.
البناء من المصدر يتطلّب شجرة مُصرّف Radix الخاصة وهو خارج نطاق هذه
الصفحة. فضّل الأرشيفات أعلاه إلا إن كنت تعمل على المُصرّف نفسه.

## مسار الوكيل {#agent-path}

ينبغي للوكلاء تحميل مهارة **install** وفهرس الوكيل بدل كشط HTML هذا:

- [`/llms.txt`](/llms.txt)
- [مهارة install](/.well-known/agent-skills/install/SKILL.md)
- [دليل الوكيل](/agents/index.md)

## التالي {#next}

| السابق | التالي |
|---|---|
| [الجولة السريعة](/start/) | [مرحبًا، Faber](/start/hello.html) |
