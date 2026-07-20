+++
translation_kind = "translated"

title = "Coreutils"
section = "ecosystem"
order = 3
sources = [
  "examples/coreutils/ (38 packages, README.md, campaign docs)",
  "examples/coreutils/packages/echo/src/main.fab",
]


prose_hash = "sha256:b413d7a121a8c7e90239de4231360a6ce0ed3d98da0d5752cc0e5bb53490c34d"
code_hash = "sha256:738161c1d064c275b5fb317f3dd18f6cf674c347cbf6d95b5a3e5edcf69af505"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
يعيد Faber تنفيذ أدوات GNU الأساسية (coreutils) كبرهان على مسار التطبيقات. هذه برامج CLI حقيقية تُظهر قدرة Faber على بناء ملفات تنفيذية عاملة باستخدام argv و stdio ورموز الخروج وإدخال/إخراج المضيف، مع التحقق منها مقابل أدوات GNU المضيفة عبر أداة فحص التكافؤ.

## الأدوات المنفَّذة {#implemented-utilities}

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

## مثال — `echo` {#example--echo}

تعرض حزمة `echo` أنماط Faber المستخدمة في جميع أدوات coreutils: تعليقات CLI التوضيحية، وتحليل الخيارات، والاختبارات المضمنة باستخدام `probandum`/`proba`/`adfirma`، والوحدات المشتركة:

```faber
importa ex "norma:consolum" privata consolum
importa ex "../../../common/gnu/format" privata gnu_format

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

## التشغيل {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
