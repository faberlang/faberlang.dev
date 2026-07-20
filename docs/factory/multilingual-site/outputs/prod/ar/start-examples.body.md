حزم Faber حقيقية — ليست مقاطع تجريبية. المصدر موجود في مستودع [faberlang/examples](https://github.com/faberlang/examples) العام. استخدمها حين تحتاج رؤية كيفية تنظيم التطبيقات، أو كيفية توصيل واجهات الأوامر، أو كيفية تنظيم مرجع اللغة.

## كيفية تشغيل مثال {#how-to-run}

<<<FENCE 0>>>

تختلف أوامر الدخل الدقيقة حسب الحزمة — اقرأ `README.md` لكل حزمة.

## حزم التطبيقات {#applications}

| الحزمة | الدور | ابدأ من هنا |
|---|---|---|
| **AI Workbench** | واجهة أوامر متعددة لجرد النماذج المحلية والتضمينات وسير عمل الاستدلال؛ مع تحقق من هيكل Python | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · الموقع: [AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | واجهة أوامر محلية لمساحة البريد مبنية بـ Faber (مدعومة بالملفات + مسار SQLite اختياري) لأوامر تنسيق الوكلاء | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | حملة تطبيقية أكبر لإعادة تنفيذ الأدوات الشائعة مع هياكل تحقق متكافئة | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | درجات وعقود أحمال عمل GPU والأنظمة | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | عروض توضيحية للبرمجة النصية ومواجهة النواة | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | حزم أولية للأتمتة | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | عروض توضيحية لحزم اللغات لإعادة تعيين الكلمات المفتاحية | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | مواد مختبرية لمخزن الحزم | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## مرجع اللغة {#corpus}

شجرة **المرجع** هي مرجع الكلمات المفتاحية والتراكيب: دليل واحد لكل تركيب، وبرامج `.fab` صغيرة متعددة. وهي مصدر الحقيقة لصفحات [المرجع](/corpus/) المولّدة على هذا الموقع.

| السطح | الرابط |
|---|---|
| شجرة المصدر | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| الوثائق المولّدة | [/corpus/](/corpus/) |
| ملاحظة النظام البيئي | [مرجع اللغة](/ecosystem/corpus.html) |

## جولات المكتبة المعيارية {#stdlib}

أمثلة مكتبة Norma المعيارية موجودة في مستودع **norma**، وليس تحت `examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` حين تكون موجودة
- الموقع: [Norma](/ecosystem/norma.html)

## ترتيب التعلم المقترح {#order}

1. [ثبّت](/start/install.html) واجهة الأوامر.
2. تصفّح [الجولة السريعة](/start/) لاستيعاب شكل اللغة.
3. افتح صفحات **المرجع** لأي كلمة مفتاحية لا تعرفها ([مركز المرجع](/corpus/)).
4. اقرأ **AI Workbench** أو **ViviLite** من البداية إلى النهاية لاستيعاب شكل التطبيق.
5. استخدم [الصياغة](/syntax/) و[الأدوات](/tooling/) كمراجع أثناء التحرير.

## مسار الوكيل {#agent-path}

- مهارة: [examples](/.well-known/agent-skills/examples/SKILL.md)
- مهارة: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- فهرس: [`/llms.txt`](/llms.txt)

## السابق {#previous}

| السابق | التالي |
|---|---|
| [المشاريع والأمثلة](/start/projects.html) | [الميزات](/features/) |
