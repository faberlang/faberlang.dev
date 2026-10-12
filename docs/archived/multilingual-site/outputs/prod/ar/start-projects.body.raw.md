بعد hello-world، انتقل إلى الحزم الحقيقية. Faber موجّه نحو الحزم؛ أسرع طريقة للتعلّم هي فحص وقراءة الحزم الموجودة التي تمارس نفس سطح المترجم الذي تخطط لاستخدامه.

## المستودعات العامة {#repositories}

| المستودع | ابدأ من هنا | السبب |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`، حزم تطبيقية، مسارات | مجموعة الأمثلة العامة والتطبيقات |
| [`faberlang/norma`](https://github.com/faberlang/norma) | حزم `norma:*` | مصدر المكتبة القياسية |
| [`faberlang/faber`](https://github.com/faberlang/faber) | غلاف CLI | أداة البناء للمستخدم |
| [`faberlang/cista`](https://github.com/faberlang/cista) | CLI/lib لمخزن الحزم | سطح إدارة الحزم |
| [`faberlang/triga`](https://github.com/faberlang/triga) | مصدر `triga:*` | مكتبة الرسوميات والهندسة |

## استنساخ مساحة عمل للتعلّم {#clone-workspace}

<<<FENCE 0>>>

الحزم التي تستورد `norma:*` تحل التبعيات من مخزن حزم Cista المسجّل في `faber.lock`. استخدم `FABER_LIBRARY_HOME` فقط عندما تريد عمدًا تجاوز محلّل محلي لتطوير المكتبات.

## اقرأ الأمثلة بهذا الترتيب {#read-order}

1. [جولة سريعة](/start/) لقواعد السطح النحوية.
2. [مرحبًا، Faber](/start/hello.html) لحزمة واحدة.
3. [المجموعة](/corpus/) لصفحة واحدة لكل كلمة مفتاحية أو بناء.
4. [أمثلة](/start/examples.html) لتطبيقات أكبر.
5. [أداة بناء Faber](/tooling/faber-build-tool.html) لتفاصيل CLI.

## سير عمل الوكيل {#agent-workflow}

لا ينبغي للوكلاء استنتاج الصيغة من النثر وحده. استخدم الأسطح الآلية ثم تحقق من صحة الكود المُنشأ:

<<<FENCE 1>>>

للعمل على الحزم، اذكر المستودع ومسار الحزمة والأمر ورمز التشخيص في التقارير. إذا لمست مستندات تحتوي كود Faber داخل أسوار في هذا الموقع، شغّل مدقق الأسوار قبل الادعاء بأن الأمثلة لا تزال تُترجم.

## ماذا بعد مسار البداية {#after-start}

| الهدف | اقرأ |
|---|---|
| تعلّم الصيغة | [الصيغة](/syntax/) |
| فهم الإعدادات المحلية | [إعدادات القارئ المحلية](/features/reader-locale.html) |
| استخدام المترجم | [أداة بناء Faber](/tooling/faber-build-tool.html) و[مترجم Radix](/tooling/radix-compiler.html) |
| تصفّح البنى | [المجموعة](/corpus/) |
| البناء بالمكتبات | [النظام البيئي](/ecosystem/) |

## التالي {#next}

| السابق | التالي |
|---|---|
| [الأوامر التي ستستخدمها](/start/commands.html) | [أمثلة](/start/examples.html) |
