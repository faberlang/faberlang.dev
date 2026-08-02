+++
translation_kind = "translated"

title = "Grammar"
section = "reference"
order = 1
sources = [
  "radix/EBNF.md",
]
+++

تُعرَّف قواعد فابر الأساسية في مستودع Radix عند `radix/EBNF.md`. وهي المرجع الرسمي لكامل صياغة اللغة.

تشمل القواعد:

- البنية المعجمية (الرموز، الكلمات المفتاحية، القيم الحرفية، التعليقات)
- التصريحات (دالة، جنس، تنفيذ، نوع، تعداد، ترتيب)
- العبارات (الربط، تدفق التحكم، الإرجاع، التكرار)
- التعابير (الاستدعاءات، المؤثرات، التحويلات، القيم الحرفية)
- التعليقات التوضيحية (صياغة @)
- تعليقات واجهة الأوامر (@ cli، @ optio، @ operandus، @ imperium)
- تعابير الأنواع (الأوليات، العموميات، الصيغ المختصرة)
- نظام الوحدات (استيراد)

```ebnf
(* excerpt: function declaration *)
funcDecl = 'functio' ident genericParams? '(' paramList ')' ('→' type)? ('⇥' type)? block;
block    = '{' stmt* '}';
```
