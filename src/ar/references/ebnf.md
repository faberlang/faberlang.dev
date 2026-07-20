+++
translation_kind = "translated"

title = "EBNF grammar"
section = "references"
order = 1
sources = [
  "radix/EBNF.md",
]


prose_hash = "sha256:901fe46feace9eaea92780fc259f6ae17c168dba45fe1ff9c0ee95e8c4858ea2"
code_hash = "sha256:4f0d91b053057a4ac78a57bb7ecb6914b647b3bd8c5855e3696e48f2c32fc265"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
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
