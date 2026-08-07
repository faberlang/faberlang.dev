+++
translation_kind = "translated"

title = "Projects and examples"
section = "projects"
order = 4
sources = []

prose_hash = "sha256:8a914c63394e5bd0bf08ccef737eb95ec4cfb7df1813f3475c78d6ef579fb14d"
code_hash = "sha256:08056868d41c8d2a2925beb910fea8adcf4ac708fa67559e5a160dd900429a06"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
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

```bash
mkdir faber-learning
cd faber-learning
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

الحزم التي تستورد `norma:*` تحل التبعيات من مخزن حزم Cista المسجّل في `faber.lock`. استخدم `FABER_LIBRARY_HOME` فقط عندما تريد عمدًا تجاوز محلّل محلي لتطوير المكتبات.

## اقرأ الأمثلة بهذا الترتيب {#read-order}

1. [جولة سريعة](/start/) لقواعد السطح النحوية.
2. [مرحبًا، Faber](/start/hello.html) لحزمة واحدة.
3. [المجموعة](/corpus/) لصفحة واحدة لكل كلمة مفتاحية أو بناء.
4. [أمثلة](/examples/) لتطبيقات أكبر.
5. [أداة بناء Faber](/toolchain/cli.html) لتفاصيل CLI.

## سير عمل الوكيل {#agent-workflow}

لا ينبغي للوكلاء استنتاج الصيغة من النثر وحده. استخدم الأسطح الآلية ثم تحقق من صحة الكود المُنشأ:

```bash
curl -fsSL https://faberlang.dev/llms.txt
faber check path/to/package
```

للعمل على الحزم، اذكر المستودع ومسار الحزمة والأمر ورمز التشخيص في التقارير. إذا لمست مستندات تحتوي كود Faber داخل أسوار في هذا الموقع، شغّل مدقق الأسوار قبل الادعاء بأن الأمثلة لا تزال تُترجم.

## ماذا بعد مسار البداية {#after-start}

| الهدف | اقرأ |
|---|---|
| تعلّم الصيغة | [الصيغة](/language/) |
| فهم الإعدادات المحلية | [إعدادات القارئ المحلية](/language/reader-locales.html) |
| استخدام المترجم | [أداة بناء Faber](/toolchain/cli.html) و[مترجم Radix](/toolchain/radix.html) |
| تصفّح البنى | [المجموعة](/corpus/) |
| البناء بالمكتبات | [النظام البيئي](/libraries/) |

## التالي {#next}

| السابق | التالي |
|---|---|
| [الأوامر التي ستستخدمها](/cheatsheet/commands.html) | [أمثلة](/examples/) |
