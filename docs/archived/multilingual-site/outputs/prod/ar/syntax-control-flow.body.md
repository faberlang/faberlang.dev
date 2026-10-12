## التفرّع الشرطي {#conditional-branching}

### si / sin / secus {#si-sin-secus}

<<<FENCE 0>>>

مع فروع else-if و else:

<<<FENCE 1>>>

### التفرّع المُدمَج باستخدام ∴ {#compact-branch-with}

يستخدم جسم التفرّع ذو العبارة الواحدة `∴` (أو الاسم المستعار `ergo`):

<<<FENCE 2>>>

## التكرار {#iteration}

### القيم — itera ex {#values-itera-ex}

<<<FENCE 3>>>

### المفاتيح — itera de {#keys-itera-de}

<<<FENCE 4>>>

### النطاق — itera ab {#range-itera-ab}

<<<FENCE 5>>>

## حلقات طالما {#while-loops}

<<<FENCE 6>>>

## أقسام الحارس — custodi {#guard-sections-custodi}

يُجمّع `custodi` فحوصات الخروج المُبكّر قبل جسم الدالة الرئيسي.
كل عبارة `si` هي حارس تسلسلي:

<<<FENCE 7>>>

`custodi` غير قابل للكسر في الإصدار 1 — إنه سور حماية، وليس حلقة.

## مطابقة الأنماط — elige {#pattern-matching-elige}

يختار `elige` أول ذراع مُطابِق:

<<<FENCE 8>>>

## مطابقة الاتحادات المُوسَمة — discerne {#tagged-union-matching-discerne}

يُطابِق `discerne` متغيرات `discretio` بشكل شامل:

<<<FENCE 9>>>

## كتل المحاولة — fac / cape {#try-blocks-fac-cape}

يفتح `fac` كتلة قد ترمي استثناءً، ويستردّ `cape` السيطرة:

<<<FENCE 10>>>
