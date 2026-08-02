+++
translation_kind = "translated"

title = "Examples"
section = "examples"
order = 5
sources = [
  "examples/README.md",
  "examples/ai-workbench/",
  "examples/vivilite/",
  "examples/ai-workbench/ (README.md, package, harness)",
  "examples/coreutils/ (38 packages, README.md, campaign docs)",
  "examples/coreutils/packages/echo/src/main.fab",
]
+++

## Examples

حزم Faber حقيقية — ليست مقاطع تجريبية. المصدر موجود في مستودع [faberlang/examples](https://github.com/faberlang/examples) العام. استخدمها حين تحتاج رؤية كيفية تنظيم التطبيقات، أو كيفية توصيل واجهات الأوامر، أو كيفية تنظيم مرجع اللغة.

### كيفية تشغيل مثال {#how-to-run}

```bash
# CLI on PATH (see Install)
faber --version

# Clone examples
git clone https://github.com/faberlang/examples.git

# Type-check a package; dependencies resolve through faber.lock
# and the Cista package store.
faber check examples/ai-workbench/packages/faber-ai

# Build / run / test when the package supports it
faber build examples/ai-workbench/packages/faber-ai -t rust
faber test examples/ai-workbench/packages/faber-ai
```

تختلف أوامر الدخل الدقيقة حسب الحزمة — اقرأ `README.md` لكل حزمة.

### حزم التطبيقات {#applications}

| الحزمة | الدور | ابدأ من هنا |
|---|---|---|
| **AI Workbench** | واجهة أوامر متعددة لجرد النماذج المحلية والتضمينات وسير عمل الاستدلال؛ مع تحقق من هيكل Python | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · الموقع: [AI Workbench](/start/examples.html) |
| **ViviLite** | واجهة أوامر محلية لمساحة البريد مبنية بـ Faber (مدعومة بالملفات + مسار SQLite اختياري) لأوامر تنسيق الوكلاء | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | حملة تطبيقية أكبر لإعادة تنفيذ الأدوات الشائعة مع هياكل تحقق متكافئة | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | درجات وعقود أحمال عمل GPU والأنظمة | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | عروض توضيحية للبرمجة النصية ومواجهة النواة | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | حزم أولية للأتمتة | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | عروض توضيحية لحزم اللغات لإعادة تعيين الكلمات المفتاحية | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | مواد مختبرية لمخزن الحزم | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

### مرجع اللغة {#corpus}

شجرة **المرجع** هي مرجع الكلمات المفتاحية والتراكيب: دليل واحد لكل تركيب، وبرامج `.fab` صغيرة متعددة. وهي مصدر الحقيقة لصفحات [المرجع](/corpus/) المولّدة على هذا الموقع.

| السطح | الرابط |
|---|---|
| شجرة المصدر | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| الوثائق المولّدة | [/corpus/](/corpus/) |
| ملاحظة النظام البيئي | [مرجع اللغة](/libraries/corpus.html) |

### جولات المكتبة المعيارية {#stdlib}

أمثلة مكتبة Norma المعيارية موجودة في مستودع **norma**، وليس تحت `examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` حين تكون موجودة
- الموقع: [Norma](/libraries/norma.html)

### ترتيب التعلم المقترح {#order}

1. [ثبّت](/start/install.html) واجهة الأوامر.
2. تصفّح [الجولة السريعة](/start/) لاستيعاب شكل اللغة.
3. افتح صفحات **المرجع** لأي كلمة مفتاحية لا تعرفها ([مركز المرجع](/corpus/)).
4. اقرأ **AI Workbench** أو **ViviLite** من البداية إلى النهاية لاستيعاب شكل التطبيق.
5. استخدم [الصياغة](/language/) و[الأدوات](/toolchain/) كمراجع أثناء التحرير.

### مسار الوكيل {#agent-path}

- مهارة: [examples](/.well-known/agent-skills/examples/SKILL.md)
- مهارة: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- فهرس: [`/llms.txt`](/llms.txt)

### السابق {#previous}

| السابق | التالي |
|---|---|
| [المشاريع والأمثلة](/start/projects.html) | [الميزات](/language/) |

## AI Workbench

محطة عمل الذكاء الاصطناعي هي تطبيق Faber للطرفية لإدارة مخزون النماذج المحلية،
وفحص البيانات الوصفية، والتضمين، والفهرسة، وسير عمل الاستدلال. وهي توضح
بناء Faber لتطبيق طرفية متعدد الأوامر وجوهري، مع إدخال وإخراج حقيقيين،
ومخرجات JSON، وتحقق بوساطة برامج Python المساعدة.

### الحزمة {#package}

`examples/ai-workbench/packages/faber-ai/` مع أوامر طرفية فرعية:

- `model inspect` — استعلام عن أسماء النماذج المحلية المستعارة ومساراتها وحالتها
- `embed` — توليد تضمينات من مُدخل نصي

### الأوامر {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

### التحقق {#validation}

تشمل محطة عمل الذكاء الاصطناعي أكثر من 20 برنامجًا مساعدًا بلغة Python تقارن
مخرجات Faber بخرائط مرجعية لمخزون النماذج، والاستدلال، وأدلة GPU، ودورة حياة
الجلسة، وإعادة استخدام الحزمة — مما يوضح التحقق عبر اللغات من ثنائيات Faber المُصرَّفة.

## Coreutils

يعيد Faber تنفيذ أدوات GNU الأساسية (coreutils) كبرهان على مسار التطبيقات. هذه برامج CLI حقيقية تُظهر قدرة Faber على بناء ملفات تنفيذية عاملة باستخدام argv و stdio ورموز الخروج وإدخال/إخراج المضيف، مع التحقق منها مقابل أدوات GNU المضيفة عبر أداة فحص التكافؤ.

### الأدوات المنفَّذة {#implemented-utilities}

**المرحلة 1 — الهيكل + `true`/`false`**
`true`، `false`

**المرحلة 2 — الدوال المساعدة المشتركة + الاختبارات المضمنة**
`echo`، `basename`، `dirname`، `printf`، `seq`

**المرحلة 3 — شرائح stdin القابلة للإلغاء**
`cat`، `head`، `tail`، `wc`، `tac`، `uniq`، `fold`، `nl`، `expand`،
`unexpand`، `sort`، `cut`، `grep`، `tr`، `tee`، `paste`

**مهيكلة — المرحلة 5 فما فوق**
`rm`، `cp`، `mv`، `mkdir`، `touch`، `pwd`، `readlink`، `realpath`،
`join`، `comm`، `od`، `cksum`، `split`، `yes`، `printenv`

### مثال — `echo` {#example--echo}

تعرض حزمة `echo` أنماط Faber المستخدمة في جميع أدوات coreutils: تعليقات CLI التوضيحية، وتحليل الخيارات، والاختبارات المضمنة باستخدام `probandum`/`proba`/`adfirma`، والوحدات المشتركة:

```faber locale=la
importa ex "norma:consolum" privata consolum

functio echo_textus(lista<textus> words) → textus {
    redde ""
}

functio echo_novam_lineam(lista<textus> words) → bivalens {
    redde falsum
}

probandum "echo formatting" tag "coreutils" {
    proba "empty operands" {
        adfirma echo_textus([]) ≡ ""
    }
    proba "-n suppresses newline" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }
}

@ cli "echo"
@ descriptio "GNU coreutils echo parity exemplum"
@ operandus ceteri textus words
incipit argumenta args {
    # ... CLI logic here
}
```

### التشغيل {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
