+++
translation_kind = "translated"

title = "Triga graphics library"
section = "ecosystem"
order = 2
sources = [
  "sibling triga/ repository",
  "radix/README.md (mentions triga)",
]


prose_hash = "sha256:d2d83d9401309c449bba9b993db7ec74cdb97afc4e8cc1b2195e769c043f07a1"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
تريغا مكتبة مصدرية عامة اختيارية لعقود الأنواع الهندسية والمشهدية والموجَّهة إلى وحدة معالجة الرسوميات. في المشاريع العادية، تُعلن تريغا كتبعية حزمة Cista في `faber.toml`؛ تسجل Cista المصدر المُحلَّل في `faber.lock` ويحلله المترجم من مخزن الحزم.

`FABER_LIBRARY_HOME` هو تجاوز محلِّل للتطوير المحلي عند تعيينه. ليس مسار المنتج الأساسي لاستهلاك تريغا.

توفر تريغا أنواعًا وعمليات لـ:

- أوليات الهندسة (نقاط، متجهات، مصفوفات، تحويلات)
- هياكل الرسم البياني للمشهد
- عقود الأنواع الموجهة إلى وحدة معالجة الرسوميات المتوافقة مع مسار أنظمة Faber

تريغا ليست جزءًا من Norma. هي تبعية اختيارية تختار الحزم الانضمام إليها عندما تحتاج إلى عمل رسومي أو هندسي.
