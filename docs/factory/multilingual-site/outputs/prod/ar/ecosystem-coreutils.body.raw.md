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

<<<FENCE 0>>>

## التشغيل {#running}

<<<FENCE 1>>>
