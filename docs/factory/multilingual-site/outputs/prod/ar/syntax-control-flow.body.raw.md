## التفريع الشرطي {#conditional-branching}

### si / sin / secus {#si-sin-secus}

<<<FENCE 0>>>

مع elseif و else:

<<<FENCE 1>>>

### تفريع مضغوط باستخدام ∴ {#compact-branch-with}

يستخدم جسم التفريع ذو العبارة الواحدة `∴` (أو مرادفه `ergo`):

<<<FENCE 2>>>

## التكرار {#iteration}

### القيم — itera ex {#values-itera-ex}

<<<FENCE 3>>>

### المفاتيح — itera de {#keys-itera-de}

<<<FENCE 4>>>

### النطاق — itera ab {#range-itera-ab}

<<<FENCE 5>>>

## حلقات while {#while-loops}

<<<FENCE 6>>>

## أقسام الحارس — custodi {#guard-sections-custodi}

`custodi` تجمّع فحوصات الخروج المبكر قبل الجسم الرئيسي للدالة.
كل شرط `si` هو حارس متسلسل:

<<<FENCE 7>>>

`custodi` غير قابل للكسر في الإصدار الأول — إنه سور حماية، وليس حلقة.

## مطابقة الأنماط — elige {#pattern-matching-elige}

`elige` تختار أول ذراع مطابق:

<<<FENCE 8>>>

## مطابقة الاتحادات الموسومة — discerne {#tagged-union-matching-discerne}

`discerne` تطابق متغيرات `discretio` بشكل شامل:

<<<FENCE 9>>>

## كتل المحاولة — fac / cape {#try-blocks-fac-cape}

`fac` تفتح كتلة قد ترمي خطأ، و `cape` تستعيد:

<<<FENCE 10>>
